"""
Created on Saturday Nocember 4th, 2023
Author: Erin Swan-Siegel
Direction from @kenjee YouTube
"""

import pandas as pd

#Correct for character error
# data = pd.read_csv('Kaggle_data.csv')
# data.head()
# data.replace(to_replace='?')

df = pd.read_csv('Kaggle_Data.csv', encoding='latin-1')
# Replace Company Name with an ID ?

# Remove "K" from Number of Reviews, Average Company Salary, and Num of Jobs Open
# Then multiply each number by 1,000

# Parse Number of Employees
# NLP on Company Description


# Remove location; there isn't much there we can really use. 
# Big companies like Lowe's and Home Depot only have 1 location listed and EY has just "United States". 
# I don't think it's going to give us much to go on.
df = df.drop('Location', axis=1)

# Check for -1, NULL, 'Unknown'
df = df[df['Company rating'] != '-1']
df = df[df['Number of Reviews'] != '-1']
df = df[df['Average Company Salary'] != '-1']
df = df[df['Number of Open Jobs'] != '-1']
df = df[df['Number of Employees'] != '-1']
df = df[df['Company rating'] != 'Unknown']
df = df[df['Number of Reviews'] != 'Unknown']
df = df[df['Average Company Salary'] != 'Unknown']
df = df[df['Number of Open Jobs'] != 'Unknown']
df = df[df['Number of Employees'] != 'Unknown']