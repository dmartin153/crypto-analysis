'''Running this file will make all the basic [feature] vs time figures for all
the cryptocurrency data, if the engine is set up correctly (see documentation in
cleaner.build_engine).'''
import cleaner
import os
import pdb
import plotter

def main():
    '''This initializes the engine and finds the currencies included in the engine.'''
    #Make the engine: this references is the way python will access postgres data
    engine = cleaner.build_engine() #will need to update username, password, server, and database
        #for whatever machine runs this. See cleaner.build_engine documentation.
    currencies = cleaner.find_currencies(engine) #find all the tables in the database

    figure_location = 'figures' #general figure location
    if not os.path.exists(figure_location):
        os.makedirs(figure_location) #make figure folder if it doesn't exist
    for currency in currencies: #loop over each currency
        if currency == currency[0].upper(): #check to make sure it's actually a currency
            make_time_plots(currency[0], engine, figure_location)

def make_time_plots(currency, engine, figure_location='figures'):
    '''This function makes plots for the currency of the engine provided'''
    df = cleaner.load_data(currency, engine) #load the data
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    features = df.select_dtypes(include=numerics).keys() #pick out the columns
            #that include numeric data
    for feature in features: #For each feature
        if df[feature].any(): #if the dataframe has data
            print('Plotting {name} {feature} vs time'.format(name=df['name'].unique()[0], feature=feature))
            plotter.basic_time_plot(df,feature) #plot and save the figures

if __name__ == '__main__':
    main()
