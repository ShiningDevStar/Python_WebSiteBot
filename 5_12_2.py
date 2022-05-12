import outlook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
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


class AutoRegisterAccount():
    def __init__(self,emailaddr,emailpassword):
        self.driver = None
        self.chrome_options = Options()
        self.exe_path = "drivers/chromedriver"
        self.username = emailaddr
        self.password = emailpassword
        pass
    def demo_imagetotext(self,imgpath):
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
    def is_visible(self, locator, timeout=30):
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, locator)))
            return True
        except TimeoutException:
            return False
    def page_has_loaded(self):
        page_state = self.driver.execute_script('return document.readyState;')
        return True
    def AccountRegist(self,name,phonenumber):
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options, executable_path=self.exe_path)
        
        self.driver.get('https://algeria.blsspainvisa.com/')
        if self.page_has_loaded() is True:
            pass

        self.driver.find_element(By.XPATH,"//div[@class='popupCloseIcon']").click()
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/header[1]/div[2]/nav[1]/a[3]").click();
        self.driver.implicitly_wait(2);
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Pour Le Centre Demande De Visa']").click();
        self.driver.implicitly_wait(2);
        self.driver.find_element_by_link_text("Réservez votre rendez-vous").click();
        print(self.driver.current_url)
        self.driver.implicitly_wait(2);
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[1]/div[2]/input[1]").send_keys(name)
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[2]/div[2]/input[1]").send_keys(self.username)
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[3]/div[2]/div[2]/input[1]").send_keys(phonenumber)
        location = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[4]/div[2]/select[1]")
        location.click()
        location.send_keys(Keys.DOWN)
        location.send_keys(Keys.ENTER)
        img_captcha = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[5]/div[1]/div[1]/img[1]");
        data_captcha = img_captcha.screenshot_as_png
        print(data_captcha)
        img_url = img_captcha.get_attribute("src")
        with open(f"temp.png","wb") as file:
            file.write(data_captcha)
        code = self.demo_imagetotext("temp.png")
        print(code)
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[6]/div[2]/input[1]").send_keys(code)
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/form[1]/div[7]/input[1]").click()
        print("Complete")
    def AccountVerify(self):
        try:
            mail = outlook.Outlook()
            mail.login(self.username,self.password)
            mail.inbox()
            mail.read()
            mailText = mail.mailbody()
            print(mailText)
            mail.logout()
            self.userInfo(mailText)
            self.verify(mailText)
        except Exception as e:
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
    def userInfo(self,mailbody):
        try:
            index = mailbody.find("Username:")
            indexend = mailbody[index:].find('</')
            print(mailbody[index+18:index+indexend])
            index = mailbody.find("Password:")
            indexend = mailbody[index:].find('</')
            print(mailbody[index+18:index+indexend])
        except Exception as e:
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
    def verify(self,mailbody):
        index = mailbody.find("href=")
        indexend = mailbody[index:].find('>')
        verifyurl = mailbody[index+6:index+indexend-1]
        verfiy_driver = webdriver.Chrome(chrome_options=self.chrome_options, executable_path=self.exe_path)
        print(verifyurl)
        verfiy_driver.get(verifyurl)
        verify_driver.quit()
        sleep(5)
    
class AutoLogIn():
    def __init__(self,emailaddr,emailpassword):
        self.driver = None
        self.chrome_options = Options()
        self.exe_path = "drivers/chromedriver"
        self.username = emailaddr
        self.password = emailpassword
        pass
    def LogIn(self):
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options, executable_path=self.exe_path)
        self.driver.get('https://algeria.blsspainvisa.com/')
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
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/input[1]").send_keys(self.password)
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/input[2]").click();

        self.check_isOpen()
    def get_otp_from_email(self):
            mail = outlook.Outlook()
            mail.login(self.username,self.password)
            mail.inbox()
            mail.read()
            mailText = mail.mailbody()
            mail.logout()
            return self.find_otp(mailText)
    def find_otp(self,mailbody):
            index = mailbody.find("OTP - ")
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
if __name__ == "__main__":
    threads = []
    #registerBot = AutoRegisterAccount('devtest0317@outlook.com', 'slwgidaik1')
    #registerBot.AccountRegist("John","542136874")
    #registerBot.AccountVerify()
    logBot = AutoLogIn('devtest0317@outlook.com','slwgidaik1')
    print("Outlook Creator ")
    logBot.LogIn()
