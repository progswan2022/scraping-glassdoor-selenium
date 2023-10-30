import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/erins/OneDrive/Desktop/MS_Data_analytics/44-688/Capstone_Project/scraping-glassdoor-selenium/chromedriver"

df = gs.get_jobs(15, False,15)