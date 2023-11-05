from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd


def get_jobs(num_jobs, slp_time): #'path' (for the chromedriver) and 'keyword' (for URL re-usability) can be added, if needed
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    #options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome()
    driver.set_window_size(1120, 1000)

    url = 'https://www.glassdoor.com/Explore/top-consultant-companies_IO.4,14.htm'
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(slp_time)

        # #Test for the "Sign Up" prompt and get rid of it.
        # try:
        #     driver.find_element_by_class_name("selected").click()
        # except ElementClickInterceptedException:
        #     pass

        # time.sleep(.1)

        # try:
        #     driver.find_element_by_css_selector('[alt="Close"]').click()
        #     #driver.find_element_by_class_name("ModalStyle__xBtn___29PT9").click()  #clicking to the X.
        #     print(' x out worked')
        # except NoSuchElementException:
        #     print(' x out failed')
        #     pass

        #Company high-level
        company_buttons = driver.find_elements(By.XPATH, "//div[@data-test = 'employer-card-single']") #These are the buttons we're going to click.
        for company_button in company_buttons:  

            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            collected_successfully = False
            
            while not collected_successfully:
                try:
                    company_name = company_button.find_element(By.XPATH, ".//h2[contains(@data-test, 'employer-short-name')]").text  #find_element_by_xpath('.//div[@class="employerName"]').text
                except NoSuchElementException:
                    company_name = "not found"
                try:
                    Num_reviews = company_button.find_element(By.XPATH, ".//h3[contains(@data-test, 'cell-Reviews-count')]").text  #find_element_by_xpath('.//div[@class="employerName"]').text
                except NoSuchElementException:
                    Num_reviews = "not found"
                try:
                    Avg_Salary = company_button.find_element(By.XPATH, ".//h3[contains(@data-test, 'cell-Salaries')]").text  #find_element_by_xpath('.//div[@class="employerName"]').text
                except NoSuchElementException:
                    Avg_Salary = "not found"
                try:
                    Job_Openings = company_button.find_element(By.XPATH, ".//h3[contains(@data-test, 'cell-Jobs-count')]//a").text
                except NoSuchElementException:
                    Job_Openings = "not found"
                try:
                    location_href = company_button.find_element(By.XPATH, ".//span[contains(@data-test, 'employer-location')]//a").get_attribute("href")
                except NoSuchElementException:
                    location_href = "not found"
                try:    
                    global_size = company_button.find_element(By.XPATH, ".//span[contains(@data-test, 'employer-size')]").text
                except NoSuchElementException:
                    global_size = "not found"                    
                try:    
                    industry = company_button.find_element(By.XPATH, ".//span[contains(@data-test, 'employer-industry')]").text
                except NoSuchElementException:
                    industry = "not found"                    
                try:   
                    company_description = company_button.find_element(By.XPATH, ".//div[contains(@class, 'order-5')]//div//p").text
                except NoSuchElementException:
                    company_description = "not found" 
                try:    
                    rating = company_button.find_element(By.XPATH, ".//span[contains(@data-test, 'rating')]//b").text
                except NoSuchElementException:
                    rating = -1 
                collected_successfully = True
            time.sleep(7)

            print(company_name)
            addtional_data = company_page(driver, company_button, slp_time)
            jobs.append({
            "Company Name" : company_name,
            "Number of Reviews" : Num_reviews,
            "Average Salary" : Avg_Salary,
            "Job Openings" : Job_Openings,
            "Location Website" : location_href,
            "Size" : global_size,
            "Industry" : industry,
            "Description" : company_description,
            "Rating" : rating,
            "Additional Data": addtional_data,
            # "Company Website" : company_website,
            # "Headquarters" : Headquarters,
            # "Company Structure" : Prv_pub_held,
            # "Revenue" : Est_rev,
            # "Year Founded" : Founded,
            })

        #Clicking on the "next page" button
        try:
            driver.find_element(By.XPATH,'.//button[@class="nextButton"]').click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break

    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.

# https://www.selenium.dev/documentation/webdriver/interactions/windows/
def company_page(driver, element, slp_time):
    ow = driver.current_window_handle;
    wait = WebDriverWait(driver, slp_time)
    element.click()
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != ow:
            driver.switch_to.window(window_handle)
            break
    company_profile = driver.find_element(By.XPATH, '//ul[@data-test="companyDetails"]')
    profile_lines = company_profile.find_elements(By.XPATH, ".//li")
    values = []
    for line_item in profile_lines:
        values.append(line_item.text)
    driver.close()
    driver.switch_to.window(ow)
    return ";".join(values)

df = get_jobs(15, 6)
df.to_csv('Output_v2.csv')