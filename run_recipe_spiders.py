# -*- coding: utf-8 -*-
import os
import argparse
import itertools
from multiprocessing.dummy import Pool as ThreadPool


# names of spider crawlers defined in the spider project
SPIDERS = [
    'recipes_allrecipes',
    'recipes_asdagoodliving',
    'recipes_bbcgoodffood',
    'recipes_bbcrecipes',
    'recipes_homemadebyyou',
    'recipes_jamieoliver',
    'recipes_lovefoodhatewaste',
    'recipes_realfoodtesco'
]


def crawl(scrapy_project_dir, scraped_data_dir, spider_name=None):
    """ Executes the command to run a crawler and outputs the scraped data to the named directory.
    """
    if spider_name:
        if os.path.isdir(scrapy_project_dir) and os.path.isdir(scraped_data_dir):
            os.chdir(scrapy_project_dir)
            os.system('scrapy crawl {0} -o {1}/{0}_items.json -t json'.format(
                spider_name, scraped_data_dir))
        else:
            raise FileNotFoundError(
                'Directory not found! Please check Scrapy project root and output directory paths '
                'passed in as arguments.')
    return


def arg_parser():
    parser = argparse.ArgumentParser(
        description='Script designed to run a series of spider scrapers to scrape data from '
                    'remote sites.')
    parser.add_argument(
        '-p', dest='scrapy_project', required=True, nargs='?', type=str,
        help='location to scrapy project root directory.')
    parser.add_argument(
        '-o', dest='output_dir', required=True, nargs='?', type=str,
        help='location to output directory.')
    return vars(parser.parse_args())


if __name__ == '__main__':
    params = arg_parser()
    output_dir = params['output_dir']
    project_dir = params['scrapy_project']
    pool = ThreadPool(len(SPIDERS))
    pool.starmap(
        crawl, zip(itertools.repeat(project_dir), itertools.repeat(output_dir), SPIDERS))
    pool.close()
