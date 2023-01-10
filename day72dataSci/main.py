import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

#highest total num of posts of ALL TIME
print(df.groupby('TAG').sum())

#total submitted count of posts per language over time every month
print(df.groupby('TAG').count())

df.DATE = pd.to_datetime(df.DATE)
df.head()

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
print(reshaped_df.head)

roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16,10)) # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
for column in reshaped_df.columns:
    plt.plot(roll_df.index, roll_df[column], linewidth=3, label=roll_df[column].name)
 
plt.legend(fontsize=16) 

plt.show()