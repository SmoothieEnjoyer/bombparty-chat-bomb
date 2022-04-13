import time
import random
import string
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

threads = []

def spam(text, textarea):
    while True:
        try:
            textarea.send_keys(text)
            textarea.send_keys(Keys.ENTER)
        except:
            time.sleep(5)

def chatbomb(code, text, bot_amount, element_timeout):
    for s in range(bot_amount):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome("chromedriver", options=chrome_options)

        driver.get("https://www.jklm.fun/" + code.upper())
        nickname_entry = driver.find_element_by_css_selector("input.styled.nickname")
        nickname_entry.send_keys("bpcb_" + "".join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(16)))

        ok_button = driver.find_element_by_css_selector("button.styled")
        ok_button.click()

        sidebar_toggle = WebDriverWait(driver, element_timeout).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "button.sidebarToggle")))
        sidebar_toggle.click()

        textarea = WebDriverWait(driver, element_timeout).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "textarea")))
        threads.append(threading.Thread(target=spam, args=(text, textarea)))
        threads[s].start()
