#!~/anaconda3/envs/py360/bin/python
# -*- coding: utf-8 -*-

'''
    File name: service.py
    Python Version: 3.6.0

    ##########   DATAPROCESSOR   ##########
    Class of parameters for begin.

'''

__author__ = "Tiago S. Buzato"
__version__ = "0.1"
__email__ = "maxempresarial@yahoo.com.br"
__status__ = "Development"

# Tag das Mensagens:
# [I] -> Informacao
# [A] -> Aviso/Alerta
# [E] -> Erro

import sys
import argparse
import controller
from datetime import datetime
from configinit.util import logger_create, get_rootDir
from configinit.settings import Settings

parser = argparse.ArgumentParser(description='''''', formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("-v", "--verbose", action='store_true', dest='verbose', help="Verbose", default=False)

parser.add_argument("-conff", "--config-file", type=str, dest='config_ini',
                    help="Configuração de inicialização. ", default=None)

parser.add_argument("-s", "--source", nargs='*', type=str, dest='source',
                    help="Choose what the source data from. [db|file]", default=False)

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
    settings = Settings()

    if args.source:
        if args.source[0] == "file":
            print("[I] The files will be treat.")
            logger.info("The files will be treat.")

            settings.filesource = args.source

    else:
        print("[I] It's necessary to pass data source like [db|file].")
        logger.info("It's necessary to pass data source like [db|file].")

    print('[I] Into the controller.')
    logger.info('Into the controller.')
    controller.run(rootpath=BASE_DIR, logger=logger, settings=settings, verbose=args.verbose)

    sys.exit(0)

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("[I] Fim - %s  (%s)." % (now, sys.argv[0]))
    exit(0)
