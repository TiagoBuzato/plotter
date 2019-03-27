# -*- coding: utf-8 -*-

'''
    File name: settings.py
    Python Version: 3.6
    Configurações padrão
'''

__author__ = "Tiago S. Buzato"
__version__ = "0.1"
__email__ = "tiago.buzato@climatempo.com.br"
__status__ = "Development"

# Tag das Mensagens:
# [I] -> Informacao
# [A] -> Aviso/Alerta
# [E] -> Erro

import os
import logging
from datetime import datetime

def get_rootDir():
    # Referência do diretorio do projeto
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    return BASE_DIR

def logger_create(projectname):
    BASE_DIR = get_rootDir()

    formatter = ('%(asctime)-15s - %(name)s - %(levelname)s - %(message)s')

    logging.basicConfig(filename=(BASE_DIR + '/logs/'+projectname+'.{_data:%Y%m%d%H%M}_1.log'.
                                  format(_data=datetime.now())), level=logging.DEBUG, format=formatter)

    logger = logging.getLogger('root')

    return logger

def set_pd_to_csv(outfile, dataframe, verbose):
    if verbose:
        print("Saving DataFrame in csv file...")

    try:
        dataframe.to_csv(outfile, sep=',', encoding='utf-8', index=False)
    except Exception as escsv:
        print("Fail to save Pandas DataFrame in *.csv file. Error: ")
        print(escsv)
        return False
    return True