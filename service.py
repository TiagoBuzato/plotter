#!/opt/anaconda3/envs/py360/bin/python
# -*- coding: utf-8 -*-

'''
    File name: service.py
    Python Version: 3.6.0

    ##########   DATAPROCESSOR   ##########
    Ca

'''

__author__ = "Tiago S. Buzato"
__version__ = "0.1"
__email__ = "tiago.buzato@climatempo.com.br"
__status__ = "Development"

# Tag das Mensagens:
# [I] -> Informacao
# [A] -> Aviso/Alerta
# [E] -> Erro

import sys
import argparse
import json
import pandas as pd
from datetime import datetime
from core.extractor import Extractor
from core.plotter import Plotter
from configinit.util import logger_create, get_rootDir

parser = argparse.ArgumentParser(description='''''', formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("-v", "--verbose", action='store_true', dest='verbose', help="Verbose", default=False)

parser.add_argument("-conff", "--config-file", type=str, dest='config_ini',
                    help="Configuração de inicialização. ", default=None)

parser.add_argument("-g", "--graphics", nargs='*', type=str, dest='graphics',
                    help="Operation to list what the graphics the system will need to make.", default=False)

parser.add_argument("-dg", "--diary_graphics", nargs='*', type=str, dest='diary_graphics',
                    help="Operation to make the graphics for range. It's waiting for begin and end date and locate "
                         "example:<2017-06-08T00:00:00Z 2017-06-08T23:59:59Z [lat, lon]>", default=False)

# parser.add_argument("-tg", "--graphics_type", nargs='*', type=str, dest='graphics_type',
#                     help="Operation to list the kind os graphics the users want to see.", default=False)


if __name__=="__main__":
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("[I] Inicio - {} ({}).".format(now, sys.argv[0]))

    # Created Variables
    args = parser.parse_args()
    BASE_DIR = get_rootDir()
    logger = logger_create('plotter')
    logger.debug("[I] Inicio - {} ({}).".format(now, sys.argv[0]))
    dfextracted = pd.DataFrame()

    # To test
    ## begin
    # Set the database configures
    args.config_ini = BASE_DIR + "/configinit/bdmongo_cpfl_rgerange40.json"
    configure = args.config_ini

    # Comparative graphics
    args.graphics = "variables_hours", "vento_ea"
    graphicslist = args.graphics

    # Diary Graphic
    # # args.diary_graphics = "2017-06-07T00:00:00Z", "2017-06-08T23:59:59Z", "-29, -51.25"
    # # args.diary_graphics = "2017-06-08T00:00:00Z", "2017-06-08T23:59:59Z", "-29, -51.25"
    # # args.diary_graphics = "2017-01-03T00:00:00Z", "2017-01-05T23:59:59Z", "-30, -51.25"
    # # args.diary_graphics = "2015-12-18T00:00:00Z", "2015-12-19T23:59:59Z", "-29.5, -50.625"
    # args.diary_graphics = "2015-06-01T00:00:00Z", "2015-06-30T23:59:59Z", "-29.5, -50.625"
    # begin_date = args.diary_graphics[0]
    # end_date = args.diary_graphics[1]
    # locate = args.diary_graphics[2]

    ##end Test

    # configure = args.config_ini
    configure = json.loads(open(configure, 'r').read())

    if args.diary_graphics:
        begin_date = args.diary_graphics[0]
        end_date = args.diary_graphics[1]
        locate = args.diary_graphics[2]
        logger.debug('Data Extracting...')
        print('Data Extracting...')
        dfextracted = Extractor('period', begin_date, end_date, locate, configure, logger, args.verbose).run()
        logger.debug('Data Extracted.')
        print('Data Extracted.')
        logger.debug('Making Diary Graphics...')
        print("Making Diary Graphics...")
        Plotter('diary', dfextracted, locate, logger, args.verbose).run()
        exit(0)

    if args.graphics:
        # graphicslist = args.graphics
        begin_date = "1500-04-22T00:00:00Z"
        end_date = "2002-01-01T00:00:00Z"
        locate = "0, 0"
        logger.debug('Data Extracting...')
        print('Data Extracting...')
        dfextracted = Extractor('comparative', begin_date, end_date, locate, configure, logger, args.verbose).run()
        logger.debug('Data Extracted.')
        exit(0)

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("[I] Fim - %s  (%s)." % (now, sys.argv[0]))
    exit(0)
