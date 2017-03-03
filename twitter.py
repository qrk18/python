"""
The script visits the profile of a given twitter user, scrolls down the screen twice to load more tweets,
and then write the text and number of likes for each tweet to a file.
"""


from selenium import webdriver
import time
import codecs



url='https://twitter.com/SHAQ'

#open the browser and visit the url
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

#scroll down twice to load more tweets
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

#find all elements with a class that ends in 'tweet-text'
tweets=driver.find_elements_by_css_selector("[data-item-type=tweet]")

"""
for tweet in tweets:
    print (tweet.find_element_by_css_selector("[class$=tweet-text"))
"""

#write the tweets to a file
#fw=open('tweets.txt','w')
fw=codecs.open('tweets.txt','w',encoding='utf-8')
for tweet in tweets:
    txt,retweets,retweetsFav,retweetsReply='NA','NA','NA','NA'
    
    try: 
        txt=tweet.find_element_by_css_selector("[class$=tweet-text]").text
    except: 
        print ('no text')  
    
    try:
        retweetElement=tweet.find_element_by_css_selector("[class$=js-actionRetweet]")
        retweets=retweetElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text   
    
    except:
        print ('no retweets')
        

    try:
        retweetFavElement=tweet.find_element_by_css_selector("[class$=js-actionFavorite]")
        retweetsFav=retweetFavElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text         
   
    except:
        print ('no fav')
        
        
    try:
        replyTweets=tweet.find_element_by_css_selector("[class$=js-actionReply]")
        retweetsReply=replyTweets.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text 
    except:
        print ('no reply')
        
    try:
        dateMonthTweets=tweet.find_element_by_css_selector("[data-long-form=true]").text
       #dateMonthTweets=dateMonth.find_element_by_css_selector('[class=_timestamp js-short-timestamp]').text 
    except:
        print('no dates')
   
    fw.write(txt.replace('\n',' ')+'\t'+str(retweets)+'\t'+str(retweetsFav)+'\t'+str(retweetsReply)+'\t'+str(dateMonthTweets)+'\n')

fw.close()


driver.quit()#close the browser
