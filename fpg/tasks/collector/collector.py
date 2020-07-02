"""
Basic function to download data from Yahoo database
"""


import pandas as pd
import yfinance as yf


def collect_stock_data(tick_list: pd.Series) -> pd.DataFrame:

    """
    Get stock data from Yahoo DB

    Parameters
    ----------
    tick_list:
        List of company tickers to fetch

    Returns
    -------
    df_stock:
        dataframe containing stock data

    """


    for tick in tick_list:

        security = yf.Ticker(tick)


        try:
            # get historical market data
            _data = security.history(period="10y")
            print(_data.head())
            if type(_data) is not type(None):
                _data.to_csv('../data/stock_ts/stock_ts_{}.csv'.format(tick))

        except:
            print('security ts not found')

        try:
            _sust = security.sustainability
            if type(_sust) is not type(None):
                _sust.to_csv('../data/sustainability/sust_{}.csv'.format(tick))

        except:
            print('sustainability not found')

        try:
            _recc = security.recommendations
            if type(_recc) is not type(None):
                _recc.to_csv('../data/recommendations/reco_ts_{}.csv'.format(tick))
        except:
            print('recommendations not found')

        try:
         _cale = security.calendar
         if type(_cale) is not type(None):
             _cale.to_csv('../data/calendar/cale_{}.csv'.format(tick))

        except:
            print('calendar not found')

        try:
         _financials = security.financials
         if type(_financials) is not type(None):
             _financials.to_csv('../data/financials/financials_{}.csv'.format(tick))

        except:
            print('financials not found')

        try:
            _q_financials = security.quarterly_financials
            if type(_q_financials) is not type(None):
                _q_financials.to_csv('../data/quart_fin/q_financials_{}.csv'.format(tick))

        except:
            print('quarter financials not found')














    return None

