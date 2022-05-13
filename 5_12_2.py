import outlook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as ChromeService # Similar thing for firefox also!
from subprocess import CREATE_NO_WINDOW # This flag will only be available in window
import time
from time import sleep
import os
import re
import requests
from os import environ
import threading
import time
from anycaptcha import AnycaptchaClient, HCaptchaTaskProxyless, RecaptchaV2TaskProxyless, RecaptchaV3TaskProxyless, \
    ImageToTextTask ,RecaptchaV2Task ,HCaptchaTask , FunCaptchaProxylessTask,ZaloTask
import random
import sys


    
class AutoLogIn():
    def __init__(self,emailaddr,emailpassword,visapassword):
        self.driver = None
        self.chrome_options = Options()
        #self.chrome_options.add_argument('--headless')
        self.exe_path = "drivers/chromedriver"
        self.username = emailaddr
        self.password = emailpassword
        self.visapass = visapassword
        self.chrome_service = ChromeService('drivers\chromedriver')
        self.chrome_service.creationflags = CREATE_NO_WINDOW

        pass
    def LogIn(self):
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options, executable_path=self.exe_path , service=self.chrome_service)
        start = time.time();
        self.driver.get('https://algeria.blsspainvisa.com/')
        while "504" in self.driver.title :
            self.driver.get('https://algeria.blsspainvisa.com/')
        finish = time.time();
        totalTime = finish - start; 
        print(totalTime); 
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH,"//div[@class='popupCloseIcon']").click()
        #self.driver.find_element_by_xpat("//div[@class='popupCloseIcon']").click();
        print("AAA");
        self.driver.implicitly_wait(2);
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/header[1]/div[2]/nav[1]/a[3]").click();
        self.driver.implicitly_wait(2);
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Pour Le Centre Demande De Visa']").click();
        self.driver.implicitly_wait(2);
        self.driver.find_element_by_link_text("Réservez votre rendez-vous").click();
        print(self.driver.current_url)
        self.driver.implicitly_wait(2);

        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]").click();
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys(self.username);
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/input[2]").click();
        sleep(2);
        self.driver.implicitly_wait(2);
        OTPcode = self.get_otp_from_email()
        #OTPcode=input("Please Input OTP code");

        #self.driver.find_element(By.XPATH,"").click();
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys(OTPcode)
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/input[1]").send_keys(self.visapass)
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/input[2]").click();

        self.check_isOpen()
    def get_otp_from_email(self):
            mail = outlook.Outlook()
            mail.login(self.username,self.password)
            mail.inbox()
            mail.read()
            mailText = mail.mailbody()
            mail.logout()
            OTP = self.find_otp(mailText)
            if OTP != -1:
                return OTP
            mail.login(self.username,self.password)
            mail.junk()
            mail.read()
            mailText = mail.mailbody()
            mail.logout()
            OTP = self.find_otp(mailText)
            return OTP
    def find_otp(self,mailbody):
            index = mailbody.find("OTP - ")
            if index == -1:
                 return index
            print(mailbody[index:])
            indexend = mailbody[index:].find('<')
            print(indexend)
            return mailbody[index+6:index+indexend]
    def check_isOpen(self):
        while True :
            self.driver.refresh()
            self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]").click()
            try:        
                isCancle = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/form[1]/section[1]/div[1]/div[1]/h2[1]")
            except NoSuchElementException:
                break;
            sleep(30)
        notification.notify(
            title = 'testing',
            message = 'message',
            app_icon = None,
            timeout = 10,
        )
def logthread(username , password, visapass):
    logBot = AutoLogIn(username, password, visapass)
    logBot.LogIn()
    
if __name__ == "__main__":
    threads = []
    #registerBot = AutoRegisterAccount('devtest0317@outlook.com', 'slwgidaik1')
    #registerBot.AccountRegist("John","542136874")
    #registerBot.AccountVerify()
    u = ["devtest0312@outlook.com", "devtest0315@outlook.com","devtest0316@outlook.com", "devtest0318@outlook.com" ,"devtest0320@outlook.com"]
    p = ["slwgidaik1","slwgidaik1","slwgidaik1","slwgidaik1","slwgidaik1"]
    v = ["U0IQ0AiF","ZKEn@OV5","xf21?lb6","Ni8i9yba","xbrXLh3t"]
    for k in range(5):
        t = threading.Thread(target=logthread, args=(u[k], p[k], v[k],))
        threads.append(t)
        t.start()
    #logBot = AutoLogIn('devtest0312@outlook.com','slwgidaik1','U0IQ0AiF')
    #logBot = AutoLogIn('devtest0315@outlook.com','slwgidaik1','ZKEn@OV5')
    #logBot = AutoLogIn('devtest0316@outlook.com','slwgidaik1','xf21?lb6')
    #logBot = AutoLogIn('devtest0318@outlook.com','slwgidaik1','Ni8i9yba')
    # AutoLogIn('devtest0320@outlook.com','slwgidaik1','xbrXLh3t') 
    #logBot.LogIn()
