
import numpy as np, pandas as pd, requests, xlsxwriter, Math
stocks = pd.read_csv('/sp500TCKRs.csv')
IEX_CLOUD_API_TOKEN = 'wi_thismanyprobelmswhoneedsagoodone'
symbol = 'AAPL'
api_url = f'https://cloud.iexapis.com/v1/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()
price = data['latestPrice']
market_cap = data['marketCap']
my_columns = ['Ticker', 'Stock Price', 'Market Capitalization', 'Number of Shares to Buy']
final_dataframe = pd.DataFrame(columns = my_columns)
final_dataframe.append(
    pd.Series(
    [
        symbol,
        price,
        market_cap,
        'N/A'
    ],
    index = my_columns    
    ),
    ignore_index=True
)
final_dataframe = pd.DataFrame(columns=my_columns)
for stock in stocks['TICKER']:
    api_url = f'https://cloud.iexapis.com/v1/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(api_url).json()
    final_dataframe = final_dataframe.append(
        pd.Series(
        [
            stock,
            data['latestPrice'],
            data['marketCap'],
            'N/A'
        ],
        index = my_columns),
    ignore_index=True
    )

    # to be continued...