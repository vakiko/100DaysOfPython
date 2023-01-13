import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

btc_search = pd.read_csv('data/Bitcoin Search Trend.csv')
btc_price = pd.read_csv('data/Daily Bitcoin Price.csv')
tesla_search = pd.read_csv('data\TESLA Search Trend vs Price.csv')
UE_benefits_v_search_4_19 = pd.read_csv("data/UE_Benefits_Search_vs_UE_Rate_2004-19.csv")
df_UE = pd.read_csv("data/UE_Benefits_Search_vs_UE_Rate_2004-20.csv")

print(btc_search.isnull().values.any())
print(btc_price.isnull().values.any())
print(tesla_search.isnull().values.any())
print(df_UE.isnull().values.any())

print(btc_price.isnull().values.any())
btc_price = btc_price.dropna()
print('NaN value dropped')
print(btc_price.isnull().values.any())


btc_search.MONTH = pd.to_datetime(btc_search.MONTH)
tesla_search.MONTH = pd.to_datetime(tesla_search.MONTH)
btc_price.DATE = pd.to_datetime(btc_price.DATE)
df_UE.MONTH = pd.to_datetime(df_UE.MONTH)

btc_monthly = btc_price.resample('M', on='DATE').last() #resample btc prices with a monthly frequency
print(btc_monthly.head())
print(btc_search.shape)
#plot tesla stock across tesla search volume

plt.figure(figsize=(14,8), dpi=120) 
plt.title('Tesla Web Search vs Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(tesla_search.MONTH, tesla_search.TSLA_WEB_SEARCH, color='red')
ax2.plot(tesla_search.MONTH, tesla_search.TSLA_USD_CLOSE, color='blue')

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
ax1.set_ylim([0, 150])
ax1.set_xlim([tesla_search.MONTH.min(), tesla_search.MONTH.max()])

ax1.set_xlabel('Year')
ax1.set_ylabel('Tesla Search Volume', color='red', fontsize=14)
ax2.set_ylabel('Tesla Stock Price', color='blue', fontsize=14)

plt.show()

#btc price chart

plt.figure(figsize=(14,8), dpi=120) 
plt.title('BTC Search Volume vs Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(btc_search.MONTH, btc_search.BTC_NEWS_SEARCH, color='red', marker='o')
ax2.plot(btc_price.DATE, btc_price.CLOSE, color='blue', linestyle='dashed')

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
ax1.set_ylim([0, 150])

ax1.set_xlim([btc_search.MONTH.min(), btc_search.MONTH.max()])

ax1.set_xlabel('Year')
ax1.set_ylabel('BTC Search Volume', color='red', fontsize=14)
ax2.set_ylabel('BTC Market Price', color='blue', fontsize=14)

plt.show()

#unemployment chart

plt.figure(figsize=(14,8), dpi=120) 
plt.title('Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020', fontsize=18)
plt.xticks(fontsize=14, rotation=45)
plt.grid()

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(df_UE.MONTH, df_UE.UE_BENEFITS_WEB_SEARCH, color='pink')
ax2.plot(df_UE.MONTH, df_UE.UNRATE, color='blue', linestyle='dashed')

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_xlim([df_UE.MONTH.min(), df_UE.MONTH.max()])

ax1.set_xlabel('Year')
ax1.set_ylabel('UE Search Volume', color='red', fontsize=14)
ax2.set_ylabel('FRED U/E Rate', color='blue', fontsize=14)


plt.show()