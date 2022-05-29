from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# set up some options to let it run headless/non-headless
options = webdriver.ChromeOptions()
options.headless = True
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

link = 'https://www.amazon.com/WaterWipes-Sensitive-Wipes-Count-Packs/product-reviews/B008KJEYLO/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber='
for i in range(1, 501): #from 1-500, because the max page number is 500
    print("Now processing page:", i)
    driver.get(link+str(i)) #get the review page with the page number 'i'
    try:
        comment = driver.find_elements(By.CSS_SELECTOR, "span[class ~= review-text-content]") #find 10 reviews on the page, this is a list of 10 element objects
        with open('reviews.txt', 'a', newline='') as f:
            # Pass the data in the list to write method
            for j in range(len(comment)):
                f.write(comment[j].text)
            f.close()
        time.sleep(1.5)
        # print(len(comment))
        # for i in range(len(comment)):
        #     print("============================================")
        #     print(comment[i].text)
    except Exception as e:
        print("Error happened:", e)









# a-size-base review-text review-text-content
# with open('test.html', 'w') as f:
#     f.write(driver.page_source)

