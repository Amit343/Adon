from django.http import HttpResponse
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
import yfinance as yf
from rest_framework import status
from yahoo_fin import stock_info as si

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


# this api fetch the  with the interval of api
class yahoofinance_Api(APIView):
    def get(self,request):
        data = yf.download("SPY", start="2022-07-24", end="2022-07-26", interval = "1m")
        return Response({'status':'success','data':data},status=status.HTTP_200_OK)


#this Api is for the live price and income statement

class yahoo_live_Api(APIView):
    def get(self,request):
        dow_list=['AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'CSCO', 'CVX', 'DIS', 'DOW', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH', 'V', 'VZ', 'WBA', 'WMT']
        l={}
        live_price=si.get_live_price('BA')
        live_price1=si.get_live_price('CAT')
        l['BA']=live_price
        l['CAT']=live_price1
        return Response({'status':'success','live_price':l},status=status.HTTP_200_OK)


        

def live_price_of_stock(request):
    dow_list = si.tickers_dow()
    value=dow_list[0:8]
    list_of_live_price=[]
    value_of_live_price={}
    for i in value:
        data=si.get_live_price(i)
        print(data,i)
        value_of_live_price[i]=data
    list_of_live_price.append(value_of_live_price)
    return HttpResponse("<html><body><h3>This is info of the live prices</h3<br> <p>%s</p>.</body></html>" % list_of_live_price)



#this is data of indian stock parket
from nsepython import *
def indian_stock(symbol,attribute="lastPrice"):
    positions = nsefetch('https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O')
    indian_stocks=[]
    for x in range(0, 10):
        indian_stocks.append(positions['data'][x])
    return HttpResponse("<html><body><h3>This is data of indian stock market</h3><br> <p>%s</p>.</body></html>" % indian_stocks)


def info(request):
    data = yf.download("SPY", start="2022-07-24", end="2022-07-26", interval = "1m")
    return HttpResponse("<html><body><h3>This is data of  stock market</h3><br> <p>%s</p>.</body></html>" % data)
    
