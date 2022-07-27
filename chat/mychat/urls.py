from django.urls import path
from .views import *

urlpatterns = [
    path('index',current_datetime),
    path('finanace',yahoofinance_Api.as_view()),
    path('live_price',yahoo_live_Api.as_view()),
    path('indian_stocks',indian_stock),
    path('live_price_stocks',live_price_of_stock),
    path('stocks',info),
    
]
