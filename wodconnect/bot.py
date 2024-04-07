import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import requests


def initialize_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("start-maximized")
    time.sleep(2)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver


def login(driver, username, password):
    driver.get("https://www.wodconnect.com/users/sign_in")
    username_elem = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "user_email")))
    username_elem.send_keys(username)
    password_elem = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "user_password")))
    password_elem.send_keys(password)
    password_elem.send_keys(Keys.RETURN)


def select_calendar_date(driver, date):
    time.sleep(2)
    calendar_button_text = driver.find_element("css selector", ".selected_date.js_selected_date_indicator")
    driver.execute_script("arguments[0].click();", calendar_button_text)
    time.sleep(2)
    date_element = driver.find_element("css selector", f'[aria-label="{date}"]')
    driver.execute_script("arguments[0].click();", date_element)


def book_class(driver, class_time):
    time.sleep(2)
    scroll_element = driver.find_element(By.XPATH, f"//h2[contains(text(),'{class_time}')]")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
    parent_div = scroll_element.find_element(By.XPATH, "./ancestor::div[@class='workout_info']")
    book_button = parent_div.find_element(By.XPATH, ".//input[@class='book-class']")
    book_button.click()


def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.get(url, params)
    if response.status_code != 200:
        print(f"Failed to send Telegram message. Response: {response.text}")
