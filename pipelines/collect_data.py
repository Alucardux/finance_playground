"""
Basic pipeline to get finance data from Yahoo

"""

# Import dependencies
# import clp.tasks.engine.... as ...
import fpg.tasks.collector.collector as collector
import pandas as pd

# load updated company tickers list
tick_list = pd.read_csv('../data/company_tickers/constituents.csv')
tick_list = tick_list['Symbol'].values
# download stock data from yahoo
data = collector.collect_stock_data(tick_list)

