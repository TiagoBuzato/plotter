# -*- coding: utf-8 -*-

from configinit.settings import Settings
from bin.loading import Loading

'''
    File name: controller.py
    Project: Plotter
    Python Version: 3.6.0
'''
__author__ = "Tiago S. Buzato"
__version__ = "0.1"
__email__ = "maxempresarial@yahoo.com.br"
__status__ = "Development"


# Tag das Mensagens:
# [I] -> Informacao
# [A] -> Aviso/Alerta
# [E] -> Erro

def run(rootpath, logger, settings: Settings, verbose=False):
    if settings.filesource:
        print('[I] Starting file treat with those source: gfs: {gfs}, ncap: {ncap}, wrf: {wrf}'.format(
            gfs=settings.gfssource, ncap=settings.ncapsource, wrf=settings.wrfsource))
        logger.info('[I] Starting file treat with those source: gfs: {gfs}, ncap: {ncap}, wrf: {wrf}'.format(
            gfs=settings.gfssource, ncap=settings.ncapsource, wrf=settings.wrfsource))

        Loading(rootpath, settings.gfssource, settings.ncapsource, settings.wrfsource, logger, verbose).run()

    return
