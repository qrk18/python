"""
The script visits the profile of a given twitter user, scrolls down the screen twice to load more tweets,
and then write the text and number of likes for each tweet to a file.
"""


from selenium import webdriver
import time


url='https://twitter.com/SHAQ'

#open the browser and visit the url
#Windows
#driver = webdriver.Chrome('chromedriver.exe')
#Mac
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

#scroll down twice to load more tweets
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

#find all elements with a data item type as 'tweet'
tweets=driver.find_elements_by_css_selector("[data-item-type=tweet]")

#write the tweets to a file
fw=open('tweets.txt','w')
for tweet in tweets:
    txt,retweets='NA','NA'
#find elements vs. element    
    try: txt=tweet.find_element_by_css_selector("[class$=tweet-text]").text
    except: print ('no text')     

    try:
        retweetElement=tweet.find_element_by_css_selector("[class$=js-actionRetweet]")
        retweets=retweetElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                                                       
    except:
        print ('no retweets')

#    fw.write(txt.replace('\n',' ')+'\t'+str(retweets)+'\n')
    fw.write(txt.replace('\n',' ').encode('utf-8')+'\t'+retweets.encode('utf-8')+'\n')

fw.close()


driver.quit()#close the browser
