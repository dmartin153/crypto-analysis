# crypto-analysis
This repository contains analysis scripts for my crypto currency project.

## How data is stored and moved

The majority of this project assumes data is stored in postgres databases. The
analysis code primarily uses python, pandas, and matplotlib to create visuals.

## How to make basic figures

1. Have the data in a postgres database somewhere.

2. Change the default username, password, server, and database name in the build_engine function of cleaner.py to match where the data is stored.

3. Enter the command
```python make_basic_time_plots.py```
from the directory with the scripts. The code will create a figures folder with
time data for each of the cryptocurrencies in the database.
