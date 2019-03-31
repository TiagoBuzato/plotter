#!/opt/anaconda3/envs/py360/bin/python
# -*- coding: utf-8 -*-

'''
    File name: extractor.py
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

import pandas as pd
import core.tools as tools

class Plotter():
    def __init__(self, typedate, dfextracted, locate, logger, verbose=False):

        self.verbose = verbose
        self.logger = logger
        self.typedate = typedate
        self.dfextracted = dfextracted
        self.locate = locate

        return

    def chooser_graphics(self, dforigin, graphicslist, typelist, verbose):
        if verbose:
            print("Choosing the functions for make the graphics...")

        for graphic in graphicslist:
            if graphic == "variables_hours":
                self.variables_hours(dforigin, typelist, verbose)

    def variables_diarys(self, dfextracted, locate, verbose):
        if verbose:
            self.logger.debug('Making a graphics per a period.')
            print("Making a graphics per a period.")

        # Create new DataFrame with variables wished
        dfgraphic = pd.DataFrame()
        dfgraphic['datetime'] = dfextracted['datetime']
        dfgraphic['occurrences'] = dfextracted['occurrences'].astype(int)
        dfgraphic['ea'] = dfextracted['ea'].astype(int)
        dfgraphic['lightning'] = dfextracted['lightning'].astype(int)
        dfgraphic['PRECTOT'] = dfextracted['PRECTOT'].apply(lambda x: round(float(x), 2))
        dfgraphic['PS'] = dfextracted['PS'].apply(lambda x: round(float(x), 2))
        dfgraphic['QV2M'] = dfextracted['QV2M'].apply(lambda x: round(float(x), 4))
        dfgraphic['SLP'] = (dfextracted['SLP'].apply(lambda x: round(float(x), 2)))/100
        dfgraphic['T2M'] = dfextracted['T2M'].apply(lambda x: round(float(x), 2))
        dfgraphic['I2M'] = dfextracted['I2M'].apply(lambda x: round(float(x), 2))
        dfgraphic['I10M'] = dfextracted['I10M'].apply(lambda x: round(float(x), 2))

        # Change index to datetime
        dfgraphic.index = dfgraphic['datetime']

        dflist = []

        for variable in dfgraphic:
            if variable != "datetime" and variable != "ea":
                # Group by datetime
                dfgrouped = dfgraphic.groupby(pd.TimeGrouper('1H'))[variable].sum().reset_index()
                dflist.append(dfgrouped)


        tools.plot_two_variables(dflist, locate, verbose)
        exit()


        # # Group by variable EA
        # dfgraphic = dfgraphic.groupby('ea')['lightning'].count()
        # print(dfgraphic.head(10))


        pass

    def run(self):
        '''

        :return: list
        '''
        if self.typedate == 'diary':
            self.variables_diarys(self.dfextracted, self.locate, self.verbose)

        exit(0)
        pass