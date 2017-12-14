'''This module contains functions related to gathering and cleaning data'''
import pandas as pd
from sqlalchemy import create_engine

def load_data(currency,engine):
    '''This function returns a clean version of the currency provided, given the
    appropriate engine to call data from'''
    df = pd.read_sql_query('select * from "{}"'.format(currency),con=engine)
    df['date'] = pd.to_datetime(df['date']) #convert string to datetime object
    df.set_index('date',inplace=True) #Make date the index
    df.sort_index(inplace=True) #Sort by date (some data is not sorted)
    df['price-usd']=pd.to_numeric(df['price-usd']) #convert data to numeric
    df['market-cap-usd']= pd.to_numeric(df['market-cap-usd'])
    df['24-hour-trade-vol-usd'] = pd.to_numeric(df['24-hour-trade-vol-usd'])
    df.drop(['id'],axis=1,inplace=True) #remove unneccessary column
    df['name']=currency #Store the name of the currency in the dataframe
    return df

def build_engine(username='david',password='test', server='localhost',database='first_crypto'):
    '''This creates the connection to the database with the tables. General format is:
    engine = create_engine("postgresql://$USER:$PASSWORD@$SERVER/$DATABASE")
    In my case, prior to running this, I installed postgres on my local machine,
    made my postgres password test temporarily, and loaded the dbexport.pgsql file
    Titus gave me with the cryptocurrency data into a database called first_crypto.
    Pass in different arguments or change the defaults to meet your needs.'''
    return create_engine("postgresql://{user}:{pwd}@{server}/{db}".format(user=username,
                                                                          pwd=password,
                                                                          server=server,
                                                                          db=database))
def find_currencies(engine):
    '''This returns a list of the currencies available in the engine's database'''
    #Select all the different currencies we have data on
    currencies = pd.read_sql_query("SELECT table_name from INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'",con=engine)
    return currencies.values
