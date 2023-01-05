from datetime import date
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv
from lib2to3.pgen2 import driver
from selenium import webdriver
import time
path_to_file = "D:\Aaditya\CSV Files\Wayanad\Indore.csv"
url = "https://www.tripadvisor.in/Attraction_Review-g494941-d2615288-Reviews-Sarafa_Bazaar-Indore_Indore_District_Madhya_Pradesh.html"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
time.sleep(20)
csvFile = open(path_to_file, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
pages_to_scrape = 1500

for i in range(0, pages_to_scrape):
    #give the DOM time to load
    time.sleep(10)
    # Now we'll ask Selenium to look for elements in the page and save them to a variable. First lets define a  container that will hold all the reviews on the page. In a moment we'll parse these and save them:
    container = driver.find_elements("xpath", "//div[@data-automation= 'reviewCard']")
    # Next we'll grab the date of the review:
    dates =  driver.find_elements("xpath", ".//div[@class='biGQs _P pZUbB ncFvv osNWb']" )
    # Now we'll look at the reviews in the container and parse them out
    for j in range(len(container)):
        # Grab the title
        title = container[j].find_element("xpath", ".//div[@class='biGQs _P fiohW qWPrE ncFvv fOtGX']").text
        #Grab the review
        review =  container[j].find_element("xpath",".//div[@class = 'biGQs _P pZUbB KxBGd']//span[@class='yCeTE']").text.replace("\n"," ")
        #grab the data
        date = " ".join(dates[j].text.split(" ")[-2:])
        #Save that data in the csv and then continue to process the next review
        csvWriter.writerow([date,title,review])
    # When all the reviews in the container have been processed, change the page and repeat 
    driver.find_element("xpath", "//div[@class = 'xkSty']//a[@class='BrOJk u j z _F wSSLS tIqAi unMkR']").click()

driver.quit()

