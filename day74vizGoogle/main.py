import pandas as pd
import numpy as np

btc_search = pd.read_csv('data/Bitcoin Search Trend.csv')
btc_price = pd.read_csv('data/Daily Bitcoin Price.csv')
tesla_search = pd.read_csv('data/Bitcoin Search Trend.csv')
UE_benefits_v_search_4_19 = pd.read_csv("data/UE_Benefits_Search_vs_UE_Rate_2004-19.csv")
UE_benefits_v_search_4_20 = pd.read_csv("data/UE_Benefits_Search_vs_UE_Rate_2004-20.csv")

print(btc_search.isnull().values.any())
print(btc_price.isnull().values.any())
print(tesla_search.isnull().values.any())
print(UE_benefits_v_search_4_19.isnull().values.any())
print(UE_benefits_v_search_4_20.isnull().values.any())

print(btc_price.isnull().values.any())
btc_price = btc_price.dropna()
print('NaN value dropped')
print(btc_price.isnull().values.any())


btc_search.MONTH = pd.to_datetime(btc_search.MONTH)
tesla_search.MONTH = pd.to_datetime(tesla_search.MONTH)
btc_price.MONTH = pd.to_datetime(btc_price.DATE)
UE_benefits_v_search_4_20.DATE = pd.to_datetime(UE_benefits_v_search_4_20.MONTH)

btc_monthly = btc_price.resample('M', on='DATE').last() #resample with a monthly frequency

#plot tesla stock across tesla price volume


