import requests

api_key = "AO2GGD8VRKOER2IU"
# api_url = "https://www.alphavantage.co/"

# symbol = "IBM"
# interval = "5min"

# query = f"query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={api_key}"


# print(api_url+query)

# def get_stock_data():
#     response = requests.get(url=api_url+query)
#     print(response.json())


# get_stock_data()

api_url = "https://www.alphavantage.co/"
symbol = "IBM"

query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

print(api_url+query)

def get_stock_data():
   response = requests.get(url=api_url+query)
   print(response.json())

get_stock_data()