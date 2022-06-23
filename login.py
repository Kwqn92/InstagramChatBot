from selenium import webdriver
import configparser
import selenium
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randrange


############################################################
parser = configparser.ConfigParser()
parser.read("config.ini")

loginq = parser['login1']

uname = loginq.get("username")
pword = loginq.get("password")
site = loginq.get("site")
############################################################

my_username = uname
my_password = pword


############################################################

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(site)

input_username = browser.find_element_by_name('username')
input_password = browser.find_element_by_name('password')

def login(username,password):
    sleep(1)
    input_username.send_keys(username)
    sleep(1)
    input_password.send_keys(password)
    sleep(1)
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep(5)
    simdidegil = browser.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]').click()
    sleep(0.5)
    simdidegil = browser.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]').click()
    sleep(2)
login(username=my_username,password=my_password)







browser.close()