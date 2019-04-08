# -*- coding: utf-8 -*-

'''
    File name: line_graphic.py
    Python Version: 3.6.0

    ##########   DATAPROCESSOR   ##########
    Ca

'''

__author__ = "Tiago S. Buzato"
__version__ = "0.1"
__email__ = "maxempresarial@yahoo.com.br"
__status__ = "Development"

# Tag das Mensagens:
# [I] -> Informacao
# [A] -> Aviso/Alerta
# [E] -> Erro

import pandas as pd
import bin.tools as tools
import sys

class Line_graphic():
    def __init__(self, _dfgfs, _dfncap, _dfwrf, _output, _logger, _verbose=False):

        self.verbose = _verbose
        self.logger = _logger
        self.dfgfs = _dfgfs
        self.dfncap = _dfncap
        self.dfwrf = _dfwrf
        self.output = _output

        return

    def graphic(self, _dfgfs, _dfncap, _dfwrf, _output, _verbose):
        if _verbose:
            print('[I] Making line graphic of comparison.')
        self.logger.info('Making line graphic of comparison.')

        import matplotlib.pyplot as plt

        _dfgfs.plot()
        plt.show()
        sys.exit(0)

        ax = _dfgfs.plot()
        _dfncap.plot(ax=ax)
        # _dfwrf.plot(ax=ax)
        plt.show()

        return

    def run(self):
        '''

        :return: list
        '''
        print("dentro do plot line graphic")
        self.graphic(self.dfgfs, self.dfncap, self.dfwrf, self.output, self.verbose)

        sys.exit(0)
        pass