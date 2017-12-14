'''This module contains functions related to plotting'''
import matplotlib.pyplot as plt
import os

def basic_time_plot(df,feature='price-usd'):
    '''This makes a plot of the given dataframe's feature. Saves figure in a
    figures/feature folder. Primarily meant to be called from make_basic_time_plots'''
    saveloc = 'figures/'+feature+'/'
    if not os.path.exists(saveloc):
        os.makedirs(saveloc) #Make a folder for figures if it doesn't exist
    name = df['name'].unique()[0]
    fig = plt.figure()
    plt.plot(df.index,df[feature])
    plt.xlabel('Time')
    plt.ylabel(feature)
    plt.xticks(rotation=25)
    plt.title(name + ' '+feature+' over time')
    plt.tight_layout()
    fig.savefig(saveloc+name+'-'+feature+'-v-time.jpg')
    plt.close(fig)
