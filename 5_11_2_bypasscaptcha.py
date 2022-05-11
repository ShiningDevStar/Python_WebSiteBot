import re
import requests
from os import environ
import threading
import time
from anycaptcha import AnycaptchaClient, HCaptchaTaskProxyless, RecaptchaV2TaskProxyless, RecaptchaV3TaskProxyless, \
    ImageToTextTask ,RecaptchaV2Task ,HCaptchaTask , FunCaptchaProxylessTask,ZaloTask
import random


def demo_imagetotext():
    api_key = '89fd718af6f547dcb416f6e06a7ad532'
    captcha_fp = open('captcha.jpg', 'rb')
    print(type(captcha_fp))
    client = AnycaptchaClient(api_key)
    task = ImageToTextTask(captcha_fp)
    job = client.createTask(task,typecaptcha="text")
    job.join()
    result = job.get_solution_response()
    if result.find("ERROR") != -1:
        print("error ", result)
    else:
        print("success ", result)

demo_imagetotext()
