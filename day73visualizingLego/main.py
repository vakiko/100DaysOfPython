import pandas as pd
import matplotlib.pyplot as plt

colors = pd.read_csv('data/colors.csv')
sets = pd.read_csv('data/sets.csv')
themes = pd.read_csv('data/themes.csv')

# print(sets.head())
print(colors.is_trans.value_counts())

#In which year were the first LEGO sets released and what were these sets called?

print(sets.sort_values('year').head)


#How many different products did the LEGO company sell in their first year of operation?
print(sets[sets['year'] == 1949])

#fixing plot formatting

#What are the top 5 LEGO sets with the most number of parts? 

print(sets.sort_values('num_parts', ascending=False).head())

sets_by_year = sets.groupby('year').count()
sets_by_year['set_num'].head()
sets_by_year['set_num'].tail()


#showing number of themes per year

themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns = {'theme_id': 'nr_themes'}, inplace=True)
print(themes_by_year.head())


ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='red')
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color='blue')

#plot formatting

ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='red')
ax2.set_ylabel('Number of Themes', color='blue')

plt.show()

avg_parts_by_year = sets.groupby('year').agg({'num_parts': pd.Series.mean})
# print(avg_parts_by_year.head())

plt.scatter(avg_parts_by_year.index[:-2], avg_parts_by_year.num_parts[:-2])
plt.xlabel('Year')
plt.ylabel('Number of Average Parts')

plt.show()

#counting themes of sets by id
set_theme_count = sets['theme_id'].value_counts()
set_theme_count[:5]
set_theme_count = pd.DataFrame({'id': set_theme_count.index,
                                'set_count': set_theme_count.values})
# print(set_theme_count.head())

merged_df = pd.merge(set_theme_count, themes, on='id')
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.show()