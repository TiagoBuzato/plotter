# -*- coding: utf-8 -*-

'''
    File name: settings.py
    Python Version: 3.6
    Configurações padrão
'''
from builtins import print

__author__ = "Tiago S. Buzato"
__version__ = "0.1"
__email__ = "tiago.buzato@climatempo.com.br"
__status__ = "Development"

# Tag das Mensagens:
# [I] -> Informacao
# [A] -> Aviso/Alerta
# [E] -> Erro

import matplotlib.pyplot as plt
from configinit.util import get_rootDir


def plot_two_variables(dflist, locate, verbose):
    if verbose:
        print("creating graphics")

    dfleght = len(dflist)
    print(dfleght)

    date = str(dflist[0][dflist[0].columns[0]].iloc[0]).split(' ')[0]
    rows = 0
    columns = 0
    i = 0

    # plt.figure(figsize=(6.4, 4.8))
    fig, axes = plt.subplots(nrows=dfleght, ncols=1, figsize=(15, 15))

    for df in dflist:
        print(df.head(1))
        df.plot(x='datetime', y=df.columns[1], ax=axes[rows])

        rows = rows + 1
        columns = 0
        i = i+1
        if i == dfleght:
            plt.title("Evaluation of day " + str(date))
            plt.xlabel("Time")
            plt.savefig(get_rootDir() + '/figures/graphics_day_' + str(date.replace('-', '')) + '.png')
            plt.show()

    exit(0)
    fig, axes = plt.subplots(nrows=2, ncols=1)

    for i, df in zip(range(0, dfleght), dflist):
        print(df.head(1))
        print(df['datetime'].head(1))
        variablename = df.columns[1]

        df.plot(x='datetime', y=variablename, ax=axes[0,i])
        if i == 1:
            plt.xlabel("Time")
            plt.show()

        # dataFrame.plot(x='datetime', y='lightning')
        # plt.show()


        #
        # df.subplot(rows, 1, i)
        # df.plot(x='datetime', y=variablename)
        # plt.ylabel(variablename)
        #
        # plt.plot(x=df[df.columns[0]], y=df[variablename])
        # plt.ylabel(variablename)
        # if i == 3:
        #     plt.xlabel("Time")
        #     plt.show()

    # plt.title("Variables over the time")

    return