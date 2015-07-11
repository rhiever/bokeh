'''
This module provides U.S. marriage and divorce statistics between 1867 and 2014

Data from the CDC's National Center for Health Statistics (http://www.cdc.gov/nchs/) (NCHS) database

Data organized by Randal S. Olson (http://www.randalolson.com)

'''
from __future__ import absolute_import

from os.path import dirname, join

try:
    import pandas as pd
except ImportError as e:
    raise RuntimeError('us_marriages_divorces data requires pandas (http://pandas.pydata.org) to be installed')

data = pd.read_csv(
    join(dirname(__file__), 'us_marriages_divorces.csv'))

# Fill in missing data with a simple linear interpolation
data = md_data.interpolate(method='linear', axis=0).ffill().bfill()
