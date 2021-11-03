import json
import requests
import datetime
from datetime import datetime
import csv

apikey='TAMT0mMvg866i836yr36Y3gBU2yY9IwP3lsUMfLb'


url = "https://yfapi.net/v6/finance/quote"
querystring = {"symbols":"ORCL"}
headers = {
  'x-api-key': apikey
   }


response = requests.request("GET", url, headers=headers, params=querystring)
#print(response.text)

response.raise_for_status()  # raises exception when not a 2xx response
#if response.status_code != 204:
stock_json = response.json()
#print(stock_json['quoteResponse']['result'][0]["displayName"] + " Price:$" + str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"]))

# time, referenced https://stackabuse.com/how-to-get-the-current-date-and-time-in-python/
current_datetime = datetime.now()
#print(current_datetime)


def quiz2():
    ticker = str(input("Enter a stock abbreviation: "))
    apikey = 'TAMT0mMvg866i836yr36Y3gBU2yY9IwP3lsUMfLb'
    url = "https://yfapi.net/v6/finance/quote"
    querystring = {"symbols": ticker}
    headers = {
        'x-api-key': apikey
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    stockabbrev = ticker
    # response.raise_for_status()  # raises exception when not a 2xx response
    current_datetime = datetime.now()
    timestampStr = current_datetime.strftime(
        "%H:%M:%S.%f - %b %d %Y")  # referenced https://thispointer.com/python-how-to-convert-datetime-object-to-string-using-datetime-strftime/
    stock_json = response.json()
    # for time code, referenced https://stackabuse.com/how-to-get-the-current-date-and-time-in-python/
    if response.status_code != 204:
        try:
            newline = str(ticker), str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"]), current_datetime
            # print(stock_json['quoteResponse']['result'][0]["displayName"] , str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"]),current_datetime)
            # print(str(ticker) , str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"]),current_datetime)
            with open(r'name2', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(
                    newline)  # referenced https://www.codegrepper.com/code-examples/python/how+to+append+a+string+to+a+csv+file+in+python

        except KeyError:
            print("Invalid stock. Please try again.")  # referenced https://realpython.com/python-keyerror/
        except UnboundLocalError:
            print("Invalid stock. Please try again.")
        except IndexError:
            print("Invalid stock. Please try again.")



quiz2()