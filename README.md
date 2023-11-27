# A Study on the Attributes of Companies, and their Effect on the Overall Glassdoor Company Rating
### By Erin Swan-Siegel
### Northwest Missouri State University - Master's of Science: Data Science 
### 44-688 Data Science Capstone

GitHub Link: https://github.com/progswan2022/scraping-glassdoor-selenium

Project Paper: https://www.overleaf.com/read/nyznvznbhjpg#83cf4e

## Introduction
As consumers, our lives are filled with reviews that aid us in deciding what products and services to purchase; five gold stars helping us make even the most minute of decisions. When we see similar items boasting similar ratings, it would be reasonable to conclude that the items are comparable in some way - sharing common characteristics. Applying it to employers present on the job-search platform, Glassdoor, this hypothesis is explored and tested. 
A strategic web-scraper was built to gather company attributes found on each employer's profile, accessed from a specific starting page. Once completed, supplemented, and cleaned, 3,829 records consisting of seven primary attributes were analyzed in an effort to determine the validity of the supposition.
Training the data in Random Forest, Decision Trees, Gradient Boosting, Lasso Regression, and K-Nearest Neighbor classification models. After Hyperparameter tuning, the Random Forest model performed the best with an average error of 0.42. The maximum accuracy of the model is only 14.3\%. This is either due to the smaller sample size, outliers within the data, or the complexity of the resulting Company, compared to the attribute data recorded on Glassdoor.

## How to use this repository
* glassdoor_scraping_Erin.py - Web Scraper
* Cleaning.ipynb - Data Cleaning script
* Company_Rating_Data.csv - Project Data
* EDA_Full_Clean.csv - Categorized data with numeric replacement for Exploratory Data Analysis
* ModelBuilding.ipynb - Model Building script

### References
* Scraping_Example_Source1
* Scraping_Example_Source2.ipynb
* Raw_all_jobs.csv - Raw Supplemental Data
* Procesed_all_jobs.csv - Processed Supplemental Data

1. AI, L., Community: What is the difference between mean squared error and mean
absolute error in machine learning metrics?, https://www.linkedin.com/advice/
0/what-difference-between-mean-squared-error-tz1mc
1. Catalogue, T.D.V.: Box and whisker plots, https://datavizcatalogue.com/
methods/box_plot.html
1. Community, S.E.: Random forest underfitting, https://stats.stackexchange.
com/questions/151556/random-forest-underfitting
1. Frost, J.: Root mean squared error, https://statisticsbyjim.com/regression/
root-mean-square-error-rmse/
1. Glassdoor: Glassdoor research: Satisfaction drivers remain intact, https://www.
glassdoor.com/research/satisfaction-drivers-remain-intact
1. Glassdoor: Glassdoor research: Satisfied workers stay, https://www.glassdoor.
com/research/satisfied-workers-stay
1. Glassdoor: How did my company get on glassdoor?, https://stage-help.
glassdoor.com
1. GPT, C.: Why websites prevent data scraping, https://chat.openai.com/ (Chat_Openai_Results.docx)
1. IBM: What is supervised learning?, https://www.ibm.com/topics/
supervised-learning
1. Jee, K.: Data science project from scratch, https://www.youtube.com/@KenJee_ds
