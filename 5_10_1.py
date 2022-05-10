from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from time import sleep
import os

#from selenium.webdriver.chrome.options import Options
#chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
#chrome_options.add_argument("--headless")
#driver = webdriver.Chrome(options=chrome_options)

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

MailAddr = input("MailAddress")
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]").click();
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys(MailAddr);
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/input[2]").click();

OTPcode=input("Please Input OTP code");
Password = input("loginPassword:")
sleep(2);
browser.implicitly_wait(2);
#browser.find_element(By.XPATH,"").click();
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys(OTPcode)
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/input[1]").send_keys(Password)
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/input[2]").click();

#//input[@placeholder='Enter OTP']
#//input[contains(@placeholder,'Enter Your Password')]
#//body/div[contains(@class,'row innerbodypanel')]/section[contains(@class,'row aboutUsPanel')]/div[contains(@class,'wrap')]/div[contains(@class,'col-sm-5 container')]/div[contains(@class,'row')]/div[contains(@class,'col-sm-8 loginPanel container')]/form[@id='al_login']/div[contains(@class,'paddingInBoxExtra roundCornerExtra')]/div[1]
