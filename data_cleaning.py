"""
Created on Saturday November 4th, 2023
Author: Erin Swan-Siegel
Direction from @kenjee YouTube
"""

import pandas as pd

#Correct for character error
# data = pd.read_csv('Kaggle_data.csv')
# data.head()
# data.replace(to_replace='?')

df = pd.read_csv(r"C:\Users\erins\OneDrive\Desktop\MS_Data_analytics\44-688\Capstone_Project\scraping-glassdoor-selenium\Company_Rating_Data.csv", encoding='latin-1')
# Replace Company Name with an ID ?


df = df.drop(['Number of Reviews','Average Salary','Job Openings','Location Website', 'Company Webpage', 'Global Size 2', 'Company Location', 'Industry 2'], axis=1)

# Check for 'Unknown', -1; numbers will be reduced due to the removal of Headquarters and Industry
df = df[df['Company Name'] != ['Unknown', '-1']] # none
df = df[df['Global Size'] != ['Unknown', '-1']] # 883 additional
df = df[df['Industry'] != ['Unknown', '-1']] # 746 additional ---- REMOVE
df = df[df['Description'] != ['Unknown', '-1']] # none
df = df[df['Company Rating'] != ['Unknown', '-1']] # 144 additional
df = df[df['Headquarters'] != ['Unknown', '-1']] # 7 additional ----- REMOVE
df = df[df['Company Ownership Type'] != ['Unknown', '-1']] # 27 additional
df = df[df['Year Founded'] != ['Unknown', '-1']] # 1,053 additional
df = df[df['Est Revenue'] != ['Unknown / Non-Applicable', '-1']] # 1,430 additional

# All of the non-numeric substitutions need to be laid-out here.

# NLP on Company Description