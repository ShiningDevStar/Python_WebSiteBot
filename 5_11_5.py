import outlook
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from time import sleep
import os
browser = None
def registermail(mailAddr,mailPass):
    mail = outlook.Outlook()
    mail.login(mailAddr,mailPass)
    mail.inbox()
    
    print(mail.read())
    print(mail.mailsubject())
    print(mail.mailfrom())
    print(mail.mailto())
    print(mail.maildate())
    print(mail.mailbodydecoded())
    print(mail.mailbody())

    userInfo(mail.mailbody())
    verify(mail.mailbody())
    mail.logout()

def userInfo(mailbody):
    index = mailbody.find("Username:")
    indexend = mailbody[index:].find('</')
    print(mailbody[index+18:index+indexend])
    index = mailbody.find("Password:")
    indexend = mailbody[index:].find('</')
    print(mailbody[index+18:index+indexend])
def verify(mailbody):
    global browser
    index = mailbody.find("href=")
    indexend = mailbody[index:].find('>')
    verifyurl = mailbody[index+6:index+indexend-1]
    browser = webdriver.Chrome(ChromeDriverManager().install())
    print(verifyurl)
    browser.get(verifyurl)
    sleep(10)


registermail('devtest0316@outlook.com','slwgidaik1')
