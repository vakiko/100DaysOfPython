import pandas as pd

df = pd.read_csv('./salaries_by_college_major.csv')
clean_df = df.dropna()
# print(df.head())

#What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).
MidCareerMajorMax = (clean_df['Mid-Career Median Salary'].max())
MidCareerMajorMaxRow = clean_df['Mid-Career Median Salary'].idxmax()
MaxMidCareerMajor = clean_df['Undergraduate Major'][MidCareerMajorMaxRow]
print(MaxMidCareerMajor, "has the highest mid-career salary, earning a total of", MidCareerMajorMax)

#Which college major has the lowest starting salary and how much do graduates earn after university?

StartCareerMajorMin = (clean_df['Mid-Career Median Salary'].min())
StartCareerMajorMinRow = clean_df['Starting Median Salary'].idxmin()
StartCareerMajor = clean_df['Undergraduate Major'][StartCareerMajorMinRow]
print(StartCareerMajor, "has the lowest starting-career salary, earning a total of", StartCareerMajorMin)

#Which college major has the lowest mid-career salary and how much can people expect to earn with this degree? 

MidCareerMajorMin = (clean_df['Mid-Career Median Salary'].min())
MidCareerMajorMinRow = clean_df['Starting Median Salary'].idxmin()
MinMidCareerMajor = clean_df['Undergraduate Major'][MidCareerMajorMinRow]
print(MinMidCareerMajor, "has the lowest starting-career salary, earning a total of", MidCareerMajorMin)

#analyzing the lowest risk majors

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()
low_risk = clean_df.sort_values('Spread')
print(low_risk[['Undergraduate Major', 'Spread']].head())

#can you find the degrees with the highest potential? Find the top 5 degrees with the highest values in the 90th percentile. 

highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()
print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())

#find the degrees with the greatest spread in salaries. Which majors have the largest difference between high and low earners after graduation.

maxSpread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Starting Median Salary']
clean_df.insert(1, 'Spread of High v Low', maxSpread_col)
clean_df.head()
maxSpread_risk = clean_df.sort_values('Spread of High v Low')
print(maxSpread_risk[['Undergraduate Major', 'Spread of High v Low']].head())