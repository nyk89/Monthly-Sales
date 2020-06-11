# reporter.py

import os
import pandas as pd
#import datetime
#import itertools
#from operator import itemgetter
csv_filepath = "/Users/kellylynch/Desktop/Monthly-Sales/data/sales-201710.csv"
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71
sales = pd.read_csv(csv_filepath)
print("\nGENERATING SALES REPORT FOR MONTH OF OCTOBER 2017...\n")
print("SALES REPORT (OCTOBER 2017)\nTOTAL SALES:", to_usd(sales["sales price"].sum()),"\n")
print('TOP SELLING PRODUCTS:')
#sales.groupby(level="sales price").max()
#sales.groupby.sort()
#today = datetime.date.today()
#now = datetime.datetime.now()
#print(today)
#print(now)
print(sales)
"""
for row in sales.iterrows():
    print(sales["product"])
"""