# WordCloudPython
This is a python crawler and word cloud generator. I used the review section of a product on Target.com and crawled 1500+ of the data using the python selenium package and made a word cloud to help with business analysis.
# Tech changes this time
The webpage of Target.com is much different from Amazon.com. To get all the reviews, firstly, we have to scroll down the page to let it load all the elements; then we have to click on a 'load more' button for hundreds of times to load all the reviews on the page; finally, we can fetch all the reviews and write them into a text file.