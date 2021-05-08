import selenium
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
        
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweets(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=typed_query')
        time.sleep(3)
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)

            tweetLinks = [i.get_attribute('href')
            for i in bot.find_elements_by_xpath("//a[@dir='auto']")]
            filteredLinks = list(filter(lambda x: 'status' in x, tweetLinks))
            # print(filteredLinks) 

            for link in filteredLinks :
                    bot.get(link)
                    time.sleep(5)
                    try:
                        bot.find_element_by_xpath("//div[@data-testid='like']").click()
                        time.sleep(10)
                    except Exception as ex :
                        time.sleep(10)

            # tweets = bot.find_elements_by_class_name('tweet')
            # links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            # print(links)
            # for link in links:
            #     bot.get('https://twitter.com/' + link)
            #     try:
            #         bot.find_element_by_class_name('HeartAnimation').click()
            #         time.sleep(10)
            #     except Exception as ex:
            #         time.sleep(30)

username = '@username'
password = 'password'
account = TwitterBot(username, password)
account.login()
account.like_tweets('netflix')





