import outlook
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from time import sleep
import os

def get_otp_from_email(mailAddr,mailPass):
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

    print(find_otp(mail.mailbody()))
    mail.logout()

def find_otp(mailbody):
    index = mailbody.find("OTP - ")
    print(mailbody[index:])
    indexend = mailbody[index:].find('<')
    print(indexend)
    return mailbody[index+6:index+indexend]


browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://algeria.blsspainvisa.com/')
browser.find_element(By.XPATH,"//div[@class='popupCloseIcon']").click()
print("AAA");
browser.implicitly_wait(2);
browser.find_element(By.XPATH,"/html[1]/body[1]/header[1]/div[2]/nav[1]/a[3]").click();
browser.implicitly_wait(2);
browser.find_element(By.XPATH,"//a[normalize-space()='Pour Le Centre Demande De Visa']").click();
browser.implicitly_wait(2);
browser.find_element_by_link_text("Réservez votre rendez-vous").click();
print(browser.current_url)
browser.implicitly_wait(2);

browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/a[1]").click()
Name = input("Name")
Email = input("Email ID")
Mobile = "12547874"



