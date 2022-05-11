import outlook
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from time import sleep
import os
from selenium.webdriver.common.keys import Keys

import re
import requests
from os import environ
import threading
import time
from anycaptcha import AnycaptchaClient, HCaptchaTaskProxyless, RecaptchaV2TaskProxyless, RecaptchaV3TaskProxyless, \
    ImageToTextTask ,RecaptchaV2Task ,HCaptchaTask , FunCaptchaProxylessTask,ZaloTask
import random

def demo_imagetotext(imgpath):
    api_key = '89fd718af6f547dcb416f6e06a7ad532'
    captcha_fp = open(imgpath, 'rb')
    print(type(captcha_fp))
    client = AnycaptchaClient(api_key)
    task = ImageToTextTask(captcha_fp)
    job = client.createTask(task,typecaptcha="text")
    job.join()
    result = job.get_solution_response()
    if result.find("ERROR") != -1:
        print("error ")
    else:
        print("success ")
    return result


browser = None
    
browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://algeria.blsspainvisa.com/')
browser.find_element(By.XPATH,"//div[@class='popupCloseIcon']").click()
#browser.find_element_by_xpat("//div[@class='popupCloseIcon']").click();
print("AAA");
browser.implicitly_wait(2);
browser.find_element(By.XPATH,"/html[1]/body[1]/header[1]/div[2]/nav[1]/a[3]").click();
browser.implicitly_wait(2);
browser.find_element(By.XPATH,"//a[normalize-space()='Pour Le Centre Demande De Visa']").click();
browser.implicitly_wait(2);
browser.find_element_by_link_text("Réservez votre rendez-vous").click();
print(browser.current_url)
browser.implicitly_wait(2);

#MailAddr = input("MailAddress")
# click here
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/a[1]").click()

emailaddr = input("emailaddr")
# name /html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[1]/div[2]/input[1]
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[1]/div[2]/input[1]").send_keys("AAA")
# email /html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[2]/div[2]/input[1]
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[2]/div[2]/input[1]").send_keys(emailaddr)
# phone /html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[3]/div[2]/div[2]/input[1]
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[3]/div[2]/div[2]/input[1]").send_keys("278147874")
# location /html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[4]/div[2]/select
location = browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[4]/div[2]/select[1]")
location.click()
location.send_keys(Keys.DOWN)
location.send_keys(Keys.ENTER)
img_captcha = browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[5]/div[1]/div[1]/img[1]");
data_captcha = img_captcha.screenshot_as_png
print(data_captcha)
img_url = img_captcha.get_attribute("src")
with open(f"temp.png","wb") as file:
    file.write(data_captcha)
code = demo_imagetotext("temp.png")
print(code)
#location.send_keys(
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[6]/div[2]/input[1]").send_keys(code)

#register
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[7]/input[1]").click()



