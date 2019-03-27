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
from pymongo import MongoClient, errors
from datetime import datetime

class Extractor():
    def __init__(self, typedate, begin_date, end_date, locate, configure, logger, verbose=False):

        self.verbose = verbose
        self.logger = logger
        self.typedate = typedate
        self.begin_date = begin_date
        self.end_date = end_date
        self.locate = locate
        self.typeDB = configure['configBD']['typeDB']
        self.host = configure['configBD']['host']
        self.port = configure['configBD']['port']
        self.dbname = configure['configBD']['dbs']
        self.collection = configure['configBD']['collection']
        self.fields = configure['fields']

        return

    def connect_mongod(self, dbname, collection, host, port, verbose):
        if verbose:
            self.logger.debug("Conneting in data base "+ str(dbname) + " in mongod.")
            print("[I] - Conneting in data base ", dbname, " in mongod.")
        try:
            self.logger.info('Connecting in mongodb on host={_host} over the port={_port}.'.format(_host=host,
                                                                                                   _port=port))
            connMongo = MongoClient(host=host, port=port)
            self.logger.info('Connected in mongodb.')

            if verbose:
                self.logger.debug("Data base was connect with successful.")
                print("[I] - Data base was connect with successful.")
            database = connMongo[dbname]
            collection = database[collection]

        except errors.ConnectionFailure as ecf:
            print("[E] - Error to connect to mongod: ", ecf)
            self.logger.error(ecf)
            return False
        except errors.CollectionInvalid as eci:
            self.logger.error(eci)
            print("[E] - Error to validadte of colllection: ", eci)
            return False
        return collection

    def get_dforigin(self, conn, typedate, begin_date, end_date, locate, verbose):
        lat = float(locate.split(',')[0])
        lon = float(locate.split(',')[1])
        message = 'Getting data from database for period {begin_date} util {end_date} at lat={lat} and lon={lon}.'.\
            format(begin_date=begin_date, end_date=end_date,
                   lat=lat, lon=lon)
        if verbose:
            print("[I] - Getting data from database to dataframe.")
        self.logger.debug(message)

        listdata = []
        begin_date = datetime.strptime(begin_date, '%Y-%m-%dT%H:%M:%SZ')
        end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%SZ')

        if typedate == "period":
            query = {
                'datetime': {
                    "$gte": begin_date,
                    "$lte": end_date
                },
                'location.coordinates': [
                    lat, lon
                ]
            }

            cursor = conn.find(query, {'_id': 0})

        if typedate == "comparative":

            cursor = conn.find({}, {'datetime': 0, '_id': 0})

        del conn

        for item in list(cursor):
            for key, value in item['variables'].items():
                item[key] = value
            del item['variables']
            del item['location']
            del item['source']
            listdata.append(item)

        dforigin = pd.DataFrame(listdata)

        del listdata

        return dforigin

    def run(self):
        '''

        :return: list
        '''

        connmongo = self.connect_mongod(self.dbname, self.collection, self.host, self.port, self.verbose)
        dforigin = self.get_dforigin(connmongo, self.typedate, self.begin_date, self.end_date, self.locate,
                                     self.verbose)

        return dforigin
