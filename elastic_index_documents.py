import os
import logging
import json
import elasticsearch
import argparse
import re


_host = 'http://192.168.0.106:9200/'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s -- %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(__name__)


def check_directory_and_get_files(dir_path):
    """ Returns a list of json file(s) if found in the given directory.
    """
    if os.path.isdir(dir_path):
        files = os.listdir(dir_path)
        files = [file for file in files if file.lower().endswith('.json')]
        if files:
            return [dir_path + '/' + file if not dir_path.endswith('/')
                    else dir_path + file for file in files]
        else:
            raise FileNotFoundError(
                'No scraped data files found, expecting .json files in: {}'.format(dir_path))
    else:
        raise FileNotFoundError('Directory not found! Please check: {}'.format(dir_path))


def index_document(file_name, elastic_obj, index, doc_type, ):
    """ Indexes content from the given json file to ElasticSearch,
    where each line in the json file is considered a document.
    """
    logger.info('Indexing data to ElasticSearch ...')
    docs_new = 0
    docs_updated = 0
    with open(file_name, 'r') as fh:
        for line in fh:
            if line.startswith(('[', ']')):
                continue
            doc = json.loads(line.rstrip(',\n'))
            doc_clean = {}
            for key, val in doc.items():
                if isinstance(val, str):
                    doc_clean[key] = val
                else:
                    doc_clean[key] = [item.strip() for item in val if item.strip()]
            url = doc_clean['url']

            # ignore urls with "replytocom" appearing in them, these are duplicates
            if re.search(r'\?replytocom=\d+', url):
                continue
            try:
                if elastic_obj.indices.exists(index=index):
                    elastic_obj.indices.refresh(index=index)
                if not elastic_obj.exists(index=index, doc_type=doc_type, id=doc_clean['url']):
                    doc_clean['date_created'] = doc_clean['date_last_seen']
                    elastic_obj.index(index=index, doc_type=doc_type, id=url, body=doc_clean)
                    docs_new += 1
                else:
                    elastic_obj.update(
                        index=index, doc_type=doc_type, id=url, body={'doc': doc_clean})
                    docs_updated += 1
            except elasticsearch.TransportError:
                raise
            except elasticsearch.ElasticsearchException:
                raise
    return docs_new, docs_updated


def total_docs_processed(new_doc_count, updated_doc_count):
    logger.info("{} new documents were indexed.".format(new_doc_count))
    logger.info("{} documents were updated".format(updated_doc_count))


def docs_processed_per_file(dict_obj):
    for key, val in dict_obj.items():
        logger.info("For data dump: {} ... ".format(key))
        for type_, count in val.items():
            logger.info("  Documents indexed: {0} => {1}".format(type_, count))


def display_time(time_description):
    logger.info(time_description)


def arg_parser():
    parser = argparse.ArgumentParser(
        description='Index document from a json file into ElasticSearch.')
    parser.add_argument(
        '-d', '--input_dir', dest='input_dir', required=True, nargs='?',
        type=str, help='path to directory containing json file(s) to be indexed.')
    parser.add_argument(
        '-i', '--index', dest='index', required=True, nargs='?',
        type=str, help='name of elasticsearch index.')
    parser.add_argument(
        '-t', '--doc_type', dest='doc_type', required=True, nargs='?',
        type=str, help='name of elasticsearch document type.')
    return vars(parser.parse_args())


def main():
    params = arg_parser()
    data_dir = params['input_dir']
    index = params['index']
    doc_type = params['doc_type']
    file_stats = {}
    data_files = check_directory_and_get_files(data_dir)
    es = elasticsearch.Elasticsearch(_host)
    for file in data_files:
        docs_new, docs_updated = index_document(file, es, index, doc_type)
        file_stats[file] = {
            'new': docs_new,
            'updated': docs_updated,
        }
    docs_processed_per_file(file_stats)
    display_time('--End--')


if __name__ == '__main__':
    main()
