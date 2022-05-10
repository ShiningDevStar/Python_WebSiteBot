from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
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
browser.find_element_by_xpath("//div[@class='popupCloseIcon']").click();
print("AAA");
sleep(1);

browser.find_element_by_xpath("/html[1]/body[1]/header[1]/div[2]/nav[1]/a[3]").click();
browser.find_element_by_xpath("//a[normalize-space()='Pour Le Centre Demande De Visa']").click();
browser.find_element_by_xpath("//a[normalize-space()='Réservez votre rendez-vous']").click();



print(browser.current_url)
