import outlook
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from time import sleep
import os
from plyer import notification
browser = None
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

def check_isOpen():
    global browser
    while True :
        browser.refresh()
        browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]").click()
        try:        
            isCancle = browser.find_element(By.XPATH,"/html[1]/body[1]/div[3]/form[1]/section[1]/div[1]/div[1]/h2[1]")
        except NoSuchElementException:
            break;
        sleep(30)
    notification.notify(
        title = 'testing',
        message = 'message',
        app_icon = None,
        timeout = 10,
    )
    
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
MailAddr = 'gikkunorte@vusra.com'
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]").click();
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys(MailAddr);
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/input[2]").click();
sleep(2);
browser.implicitly_wait(2);
#get_otp_from_email(MailAddr,'slwgidaik1')
OTPcode=input("Please Input OTP code");

Password = 'lzp!m&tk'
#browser.find_element(By.XPATH,"").click();
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys(OTPcode)
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/input[1]").send_keys(Password)
browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/input[2]").click();

check_isOpen()
# /html[1]/body[1]/div[1]/div[1]
#"Appointment dates are not available."
#//h2[normalize-space()='Appointment dates are not available.']
# /html[1]/body[1]/div[3]/form[1]/section[1]/div[1]/div[1]/h2[1]
