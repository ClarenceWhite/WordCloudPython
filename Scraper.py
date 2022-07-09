from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# set up some options to let it run headless/non-headless
options = webdriver.ChromeOptions()
options.headless = False
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

# get chrome driver path
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

link = 'https://www.target.com/p/waterwipes-unscented-baby-wipes-select-count/-/A-79813633?preselect=14409160#lnk=sametab'
driver.get(link)
try:
    #Scroll down to let the page load all elements
    for i in range(5000):
        driver.execute_script("window.scrollTo(0,"+str(i)+")")
    time.sleep(10)

    #Find matching reviews message
    print("Finding matching reviews message...")
    matching_reviews_msg_xpath = """//*[@id="pageBodyContainer"]/div[11]/div[6]"""
    matching_reviews_msg = driver.find_element(By.XPATH, matching_reviews_msg_xpath)
    print("Found matching reviews:", matching_reviews_msg.text)

    #Get number of matching reviews from matching reviews message
    matching_reviews_num_str = ""
    for char in matching_reviews_msg.text:
        if char.isdigit():
            matching_reviews_num_str += char
    num_matching_reviews = int(matching_reviews_num_str)
    print("Number of matching reviews:", num_matching_reviews)

    # Find 'load 8 more' button and cilck it for ((num /8)-1) times to get all reviews in a single container
    for i in range(int(num_matching_reviews/8 -1)):
        print("Finding load more button......No.", i)
        load_more_button = driver.find_element(By.CSS_SELECTOR, "#pageBodyContainer > div.h-text-center.h-padding-h-default.h-margin-t-default.h-margin-b-wide > div.h-text-center.h-padding-v-tight > button")
        print("Found load more button No.", i, ":", load_more_button.text)
        time.sleep(1)
        print("Clicking No.", i, "button......")
        load_more_button.click()
    
    print("Finished clicking...... sleeping for 15s")
    time.sleep(15)

    #Start to collect reviews headings
    print("Finding headings...")
    headings = driver.find_elements(By.CSS_SELECTOR, "h3[class~=Heading__StyledHeading-sc-1mp23s9-0]")
    print("Len of headings list is:", len(headings))
    print("Writing headings into a text file...")
    for heading in headings:
        with open("headings.txt", 'a') as f:
            f.write(heading.text+"\n")
        f.close()
    print("*****Successfully collected headings!!*****")
    
    #Collect contents under headings
    print("Finding contents under headings...")
    contents = driver.find_elements(By.CSS_SELECTOR, "div[class='h-margin-t-default h-text-md']")
    print("Len of contents is:", len(contents))
    print("Writing contents into a text file...")
    for comment in contents:
        with open("contents.txt", "a") as f:
            f.write(comment.text+"\n")
        f.close()
    print("*****Successfully collected contents!!*****")

except Exception as e:
    print(e)