import pandas as pd

df = pd.read_csv('./salaries_by_college_major.csv')
clean_df = df.dropna()

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
