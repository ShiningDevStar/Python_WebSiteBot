from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import csv
from faker import Faker
from faker.providers import person
import random
import string
from time import sleep as wait
import sys
from pyvirtualdisplay import Display
import json
from urllib.request import urlretrieve
import requests
import time
import os
from anycaptcha import AnycaptchaClient, HCaptchaTaskProxyless, RecaptchaV2TaskProxyless, RecaptchaV3TaskProxyless, \
    ImageToTextTask ,RecaptchaV2Task ,HCaptchaTask , FunCaptchaProxylessTask,ZaloTask

class GenerateRandom:
    def random_char(self, y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))

    def nonce(self, length=4):
        return ''.join([str(random.randint(0, 9)) for i in range(length)])
    def noncepass(self, length=8):
        return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))


class Register:
    def __init__(self):
        try:
            with open('config.json') as json_data_file:
                config = json.load(json_data_file)
                self.using_recover = config['recovery']
                self.user_password = config['user_password']
                self.proxy_file = config['proxyfile']
                self.ac_token = config['anticaptchatoken']
                self.headless = config['headless']
                self.password = config['password']
                self.locale = "en_US"
                #self.locale = config['locale']
        except FileNotFoundError:
            print("No config.json found")
        self.outlook_url = "https://outlook.live.com/owa/?nlp=1&signup=1"
        self.chrome_options = Options()
        self.chrome_options.add_argument('--disable-web-security')
        self.chrome_options.add_argument('--disable-site-isolation-trials')
        self.chrome_options.add_argument('--disable-application-cache')
        if sys.platform == "linux" or sys.platform == "linux2":
            self.exe_path = "drivers/chromedriver"
            self.chrome_options.add_argument('--no-sandbox')
            self.chrome_options.add_argument('--headless')
            self.chrome_options.add_argument('--disable-gpu')

            display = Display(visible=0, size=(800, 800))
            display.start()
        else:
            self.exe_path = "drivers/chromedriver.exe"
        # chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=1920x1080")
        if self.headless == "True":
            self.chrome_options.add_argument('--headless')
        self.fake = Faker(self.locale)
        self.gen = GenerateRandom()

    def is_visible(self, locator, timeout=30):
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, locator)))
            return True
        except TimeoutException:
            return False

    def get_proxy(self):
        with open(self.proxy_file) as f:
            proxies = f.readlines()
            proxy = random.choice(proxies)
            return str(proxy)

    def page_has_loaded(self):
        page_state = self.driver.execute_script('return document.readyState;')
        return True
    def demo_funcaptcha(self):
        website_url = "https://iframe.arkoselabs.com/B7D8911C-5CC8-A9A3-35B0-554ACEE604DA/index.html?mkt=en"
        site_key = "B7D8911C-5CC8-A9A3-35B0-554ACEE604DA"
        api_key = "89fd718af6f547dcb416f6e06a7ad532"

        client = AnycaptchaClient(api_key)
        task = FunCaptchaProxylessTask(website_url, site_key)

        job = client.createTask(task,typecaptcha="funcaptcha")
        job.join()
        result = job.get_solution_response()
        if result.find("ERROR") != -1:
            print("error ", result)
        else:
            print("success ", result)
        return result
    def make_outlook(self):
        try:
            print("Outlook-Bot in AutoBot series, Coded by JBusiness")
            print("Generating new account...")
            self.driver = webdriver.Chrome(chrome_options=self.chrome_options, executable_path=self.exe_path)
            #proxy = self.get_proxy()
            #self.chrome_options.add_argument('--proxy-server=socks://{}'.format(proxy))
            self.driver.get(self.outlook_url)
            if self.page_has_loaded() is True:
                if self.is_visible("CredentialsPageTitle") is True:
                    pass
                    print('Page Loaded')
            first, last = self.fake.first_name().rstrip(), self.fake.last_name().rstrip()
            #first , last = "John" , "Smith"
            username = first + last + str(self.gen.nonce(10))
            password_input = str(self.gen.noncepass(12))
            print(password_input)
            self.driver.find_element_by_id("MemberName").send_keys(username)
            if self.is_visible("iSignupAction") is True:
                pass
            wait(0.5)
            self.driver.find_element_by_id("iSignupAction").click()
            wait(2)
            if self.is_visible("PasswordInput") is True:
                    pass
            self.driver.find_element_by_id("PasswordInput").send_keys(password_input)
            if self.is_visible("iSignupAction") is True:
                    pass
            wait(0.5)
            self.driver.find_element_by_id("iSignupAction").click()
            wait(1)
            if self.is_visible("FirstName") is True:
                    pass
            self.driver.find_element_by_id("FirstName").send_keys(first)
            self.driver.find_element_by_id("LastName").send_keys(last)
            if self.is_visible("iSignupAction") is True:
                    pass
            wait(0.5)
            self.driver.find_element_by_id("iSignupAction").click()
            wait(1)
            if self.is_visible("Country") is True:
                    pass
            #country = requests.get('https://ipapi.co/country_name/', proxies={"http": "socks://" + proxy}).text
            #country = requests.get('https://ipapi.co/country_name/').text
            countrygeo = Select(self.driver.find_element_by_id("Country"))
            countrygeo.select_by_visible_text("United States")
            indexm = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
            indexd = random.randint(1, 28)
            indexy = random.randint(1980, 2000)
            birthM = Select(self.driver.find_element_by_id("BirthMonth"))
            birthM.select_by_visible_text(random.choice(indexm))
            birthD = Select(self.driver.find_element_by_id("BirthDay"))
            birthD.select_by_visible_text(str(indexd))
            birthY = self.driver.find_element_by_id("BirthYear")
            
            birthY.send_keys(str(indexy))
            self.driver.find_element_by_id("iSignupAction").click()
            wait(5)

            token = self.demo_funcaptcha()
            key = input("AAA")
            self.driver.execute_script('''
            var anyCaptchaToken = arguments[0];
            var enc = document.getElementById('enforcementFrame');
            var encWin = enc.contentWindow || enc;
            var encDoc = enc.contentDocument || encWin.document;
            let script = encDoc.createElement('SCRIPT');
            script.append('function AnyCaptchaSubmit(token) { parent.postMessage(JSON.stringify({ eventId: "challenge-complete", payload: { sessionToken: token } }), "*") }');            
            encDoc.documentElement.appendChild(script);
            encWin.AnyCaptchaSubmit(anyCaptchaToken);
            ''',token)

            self.driver.find_element_by_id("iSignupAction").click()
            print("{}@outlook.com:{}:{}".format(username, self.user_password, country))
            account = {"username": username + "@outlook.com", "password": self.user_password, "country": country}
            with open("output/outlook_accounts.csv", 'a', newline='') as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow(account[i] for i in account)
        except Exception as e:
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)


if __name__ == "__main__":
    threads = []
    regBot = Register()
    print("Outlook Creator -- Coded by JBusiness")
    baba = int(input("How many account would you like to create?" + "\n"))
    if regBot.password != "AAA":
#        with open(regBot.proxy_file) as f:
#            proxies = f.readlines()
            for i in range(baba):
                regBot.make_outlook()
            print("Finished.")
    else:
        print("Incorrect Password")
