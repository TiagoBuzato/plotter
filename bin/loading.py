'''
    File name: loading.py
    Python Version: 3.6.0

    ##########   DATAPROCESSOR   ##########
    That Class load the data and treat for return dataframe.

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
import glob
import pandas as pd

class Loading():
    def __init__(self, _rootpath, _gfssource, _ncapsource, _wrfsource, _logger, _verbose=False):

        self.verbose = _verbose
        self.logger = _logger
        self.gfssource = _rootpath + _gfssource
        self.ncapsource = _rootpath + _ncapsource
        self.wrfsource = _rootpath + _wrfsource

        return

    def loading_gfs(self, _gsfpath, _verbose):
        if _verbose:
            print("[I] Loading gfs data from {path}".format(path=_gsfpath))
        self.logger.info('Loading gfs data from {path}'.format(path=_gsfpath))

        # Variables created
        dfgfs = pd.DataFrame()

        # Loading files in a list
        listgfsfile = glob.glob(_gsfpath+'*.dat')

        for file in listgfsfile:
            df = pd.read_csv(file, sep=' ', header=0, encoding='ISO-8859-1')

            # Convert date and hour to datetime type
            df['date'] = pd.to_datetime(df['Data'])
            df['time'] = pd.to_datetime(df['Hora'], format='%H:%M')

            df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))

            # Remove columns it's not will used
            df = df.drop(['date', 'time', 'Data', 'Hora'], axis=1)

            # Create column with name of tower
            towername = df.columns[1].split('_')[-1]
            df['tower'] = towername

            # Rename Column wind speed and wind direction
            df.rename(columns={df.columns[0]: 'speed'}, inplace=True)
            df.rename(columns={df.columns[1]: 'direction'}, inplace=True)

            # Join dataframe for create just one
            dfgfs = pd.concat([df, dfgfs], sort=False)

        del df

        return dfgfs

    def loading_ncap(self, _ncappath, _verbose):
        if _verbose:
            print("[I] Loading gfs data from {path}".format(path=_ncappath))
        self.logger.info('Loading gfs data from {path}'.format(path=_ncappath))

        # Variables created
        dfncap = pd.DataFrame()

        # Loading files in a list
        listncapfile = glob.glob(_ncappath+'*.dat')

        for file in listncapfile:
            print("Dentro do for")
            sys.exit(0)
            df = pd.read_csv(file, sep=' ', header=0, encoding='ISO-8859-1')

            print(df.head(4))
            sys.exit(0)

            # Convert date and hour to datetime type
            df['date'] = pd.to_datetime(df['Data'])
            df['time'] = pd.to_datetime(df['Hora'], format='%H:%M')

            df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))

            # Remove columns it's not will used
            df = df.drop(['date', 'time', 'Data', 'Hora'], axis=1)

            # Create column with name of tower
            towername = df.columns[1].split('_')[-1]
            df['tower'] = towername

            # Rename Column wind speed and wind direction
            df.rename(columns={df.columns[0]: 'speed'}, inplace=True)
            df.rename(columns={df.columns[1]: 'direction'}, inplace=True)

            # Join dataframe for create just one
            dfgfs = pd.concat([df, dfgfs], sort=False)

        del df

        return dfgfs

    def run(self):
        '''

        :return: list
        '''

        # Loading gfs files to dataframe
        #dfgfs = self.loading_gfs(self.gfssource, self.verbose)
        dfncap = self.loading_ncap(self.ncapsource, self.verbose)


        sys.exit(0)
        return