from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


def get_jobs(num_jobs, verbose, slp_time): #'path' (for the chromedriver) and 'keyword' (for URL re-usability) can be added, if needed
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
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

        
        #Going through each company in this page
        company_buttons = driver.find_elements(By.XPATH, "//div[@data-test = 'employer-card-single']") #These are the buttons we're going to click.
        for company_button in company_buttons:  

            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            collected_successfully = False
            company_name = None
            location_href = None
            global_size = None
            industry = None
            company_description = None
            rating = None
            
            while not collected_successfully:
                try:
                    company_name = company_button.find_element(By.XPATH, ".//h2[contains(@data-test, 'employer-short-name')]").text  #find_element_by_xpath('.//div[@class="employerName"]').text
                    location_href = company_button.find_element(By.XPATH, ".//span[contains(@data-test, 'employer-location')]//a").get_attribute("href")
                    global_size = company_button.find_element(By.XPATH, ".//span[contains(@data-test, 'employer-size')]").text
                    industry = company_button.find_element(By.XPATH, ".//span[contains(@data-test, 'employer-industry')]").text
                    company_description = company_button.find_element(By.XPATH, ".//div[contains(@class, 'order-5')]//div//p").text
                    rating = company_button.find_element(By.XPATH, ".//span[contains(@data-test, 'rating')]//b").text
                    collected_successfully = True
                except:
                    time.sleep(5)

            #Printing for debugging
            if verbose:
                # print("Job Title: {}".format(job_title))
                # print("Salary Estimate: {}".format(salary_estimate))
                # print("Job Description: {}".format(job_description[:500]))
                #print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                #print("Location: {}".format(location))

            # #Going to the Company tab...
            # #clicking on this:
            # #<div class="tab" data-tab-type="overview"><span>Company</span></div>
            # try:
            #     driver.find_element_by_xpath('.//div[@class="tab" and @data-tab-type="overview"]').click()

            #     try:
            #         #<div class="infoEntity">
            #         #    <label>Headquarters</label>
            #         #    <span class="value">San Francisco, CA</span>
            #         #</div>
            #         headquarters = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*').text
            #     except NoSuchElementException:
            #         headquarters = -1

            #     try:
            #         size = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Size"]//following-sibling::*').text
            #     except NoSuchElementException:
            #         size = -1

            #     try:
            #         founded = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Founded"]//following-sibling::*').text
            #     except NoSuchElementException:
            #         founded = -1

            #     try:
            #         type_of_ownership = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Type"]//following-sibling::*').text
            #     except NoSuchElementException:
            #         type_of_ownership = -1

            #     try:
            #         industry = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Industry"]//following-sibling::*').text
            #     except NoSuchElementException:
            #         industry = -1

            #     try:
            #         sector = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Sector"]//following-sibling::*').text
            #     except NoSuchElementException:
            #         sector = -1

            #     try:
            #         revenue = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Revenue"]//following-sibling::*').text
            #     except NoSuchElementException:
            #         revenue = -1

            #     try:
            #         competitors = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text
            #     except NoSuchElementException:
            #         competitors = -1

            # except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
            #     headquarters = -1
            #     size = -1
            #     founded = -1
            #     type_of_ownership = -1
            #     industry = -1
            #     sector = -1
            #     revenue = -1
            #     competitors = -1

                
            # if verbose:
            #     print("Headquarters: {}".format(headquarters))
            #     print("Size: {}".format(size))
            #     print("Founded: {}".format(founded))
            #     print("Type of Ownership: {}".format(type_of_ownership))
            #     print("Industry: {}".format(industry))
            #     print("Sector: {}".format(sector))
            #     print("Revenue: {}".format(revenue))
            #     print("Competitors: {}".format(competitors))
            #     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({
            "Company Name" : company_name,
            "Location" : location_href,
            "Industry" : industry,
            "Size" : global_size,
            "Rating" : rating,
            "Description" : company_description
            })
            #add job to jobs

        #Clicking on the "next page" button
        try:
            driver.find_element(By.XPATH,'.//button[@class="nextButton"]').click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break

    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.


df = get_jobs(10, False, 5)
df.to_csv('Output1.csv')