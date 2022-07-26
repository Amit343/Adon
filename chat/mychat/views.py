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


        

