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
import pytz

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
            df['time'] = df['Hora'] + ":00"

            # Creating datetime column
            df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))

            # Set datetime column to index
            df = df.set_index(['datetime'])

            # Remove columns it's not will used
            df = df.drop(['date', 'time', 'Data', 'Hora'], axis=1)
            df = df.drop(df.columns[1], axis=1)

            # Create column with name of tower
            towername = df.columns[0].split('_')[-1]
            df['tower'] = towername

            # Rename Column wind speed and wind direction
            df.rename(columns={df.columns[0]: 'speed_gfs'}, inplace=True)

            # replace comma to dot
            df['speed_gfs'] = df['speed_gfs'].apply(lambda x: x.replace(',', '.'))

            # Convert string to float with 2 decimal houses
            df['speed_gfs'] = df['speed_gfs'].apply(lambda x: round(float(x), 2))

            # Join dataframe for create just one
            dfgfs = pd.concat([df, dfgfs], sort=False)

        del df

        return dfgfs

    def loading_ncap(self, _ncappath, _verbose):
        if _verbose:
            print("[I] Loading ncap data from {path}".format(path=_ncappath))
        self.logger.info('Loading ncap data from {path}'.format(path=_ncappath))

        # Variables created
        dfncap = pd.DataFrame()

        # Loading files in a list
        listncapfile = glob.glob(_ncappath+'*.dat')

        for file in listncapfile:
            df = pd.read_csv(file, sep=' ', header=0, encoding='ISO-8859-1')

            # Convert date and hour to datetime type
            df['date'] = pd.to_datetime(df['Data'])
            df['date'] = df['date'].dt.strftime('%d/%m/%Y')
            df['time'] = df['Hora'] + ":00"

            # Creating datetime column
            df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))

            # Set datetime column to index
            df = df.set_index(['datetime'])

            # Remove columns it's not will used
            df = df.drop(['date', 'time', 'Data', 'Hora'], axis=1)
            df = df.drop(df.columns[1], axis=1)

            # Create column with name of tower
            towername = df.columns[0].split('_')[-1]
            df['tower'] = towername

            # Rename Column wind speed and wind direction
            df.rename(columns={df.columns[0]: 'speed_ncap'}, inplace=True)

            # replace comma to dot
            df['speed_ncap'] = df['speed_ncap'].apply(lambda x: x.replace(',', '.'))

            # Convert string to float with 2 decimal houses
            df['speed_ncap'] = df['speed_ncap'].apply(lambda x: round(float(x), 2))

            # Join dataframe for create just one
            dfncap = pd.concat([df, dfncap], sort=False)

        del df

        return dfncap

    def loading_wrf(self, _wrfpath, _verbose):
        if _verbose:
            print("[I] Loading wrf data from {path}".format(path=_wrfpath))
        self.logger.info('Loading wrf data from {path}'.format(path=_wrfpath))

        # Variables created
        dfwrf = pd.DataFrame()

        # Loading files in a list
        listwrffile = glob.glob(_wrfpath + '*.dat')

        for file in listwrffile:
            df = pd.read_csv(file, sep=' ', header=0, encoding='ISO-8859-1')

            # Convert date and hour to datetime type
            df['date'] = pd.to_datetime(df['Data'])
            df['time'] = df['Hora']+":00"

            # Creating datetime column
            df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))

            # Set datetime column to index
            df = df.set_index(['datetime'])

            # Apply time zone
            df = df.tz_localize(pytz.utc).tz_convert("America/Sao_Paulo")
            df = df.tz_localize(None)

            # Remove columns it's not will used
            df = df.drop(['date', 'time', 'Data', 'Hora'], axis=1)
            df = df.drop(df.columns[1], axis=1)

            # Create column with name of tower
            towername = df.columns[0].split('_')[-1]
            df['tower'] = towername

            # Rename Column wind speed and wind direction
            df.rename(columns={df.columns[0]: 'speed_wrf'}, inplace=True)

            # replace comma to dot
            df['speed_wrf'] = df['speed_wrf'].apply(lambda x: x.replace(',', '.'))

            # Convert string to float with 2 decimal houses
            df['speed_wrf'] = df['speed_wrf'].apply(lambda x: round(float(x), 2))

            # Join dataframe for create just one
            dfwrf = pd.concat([df, dfwrf], sort=False)

        del df

        return dfwrf

    def run(self):
        '''

        :return: list
        '''

        # Loading gfs files to dataframe
        dfgfs = self.loading_gfs(self.gfssource, self.verbose)

        # Loading ncap files to dataframe
        dfncap = self.loading_ncap(self.ncapsource, self.verbose)

        # Loading wrf files to dataframe
        dfwrf = self.loading_wrf(self.wrfsource, self.verbose)

        # # dfgfs = pd.DataFrame({'pig': [20, 18, 489, 675, 1776],'horse': [4, 25, 281, 600, 1900]},
        # #                      index=[1990, 1997, 2003, 2009, 2014])
        # # dfncap = pd.DataFrame({'pig': [15, 20, 600, 350, 2000], 'horse': [18, 55, 150, 700, 3000]},
        # #                       index=[1990, 1997, 2003, 2009, 2014])
        # dfwrf = pd.DataFrame({'pig': [8, 60, 800, 475, 1900], 'horse': [12, 33, 200, 900, 1500]},
        #                      index=[1990, 1997, 2003, 2009, 2014])

        return dfgfs, dfncap, dfwrf