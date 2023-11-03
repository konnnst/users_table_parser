# Importing necessary libraries
from selenium import webdriver
from constants import *
from selenium.webdriver.common.by import By
import time
import pandas as pd


# Checking if current page not the last page to continue while loop
def not_last_page(current_page):
    browser.get(USER_TABLE_URL.format(current_page))
    page = browser.find_element(By.XPATH, LAST_PAGE_PATH)
    page_number = int(page.get_attribute("innerHTML"))
    return page_number != current_page - 1


# Starting browser application
browser = webdriver.Firefox()

# Running LOGIN_URL page in browser
browser.get(LOGIN_URL)

# Filling login and password fields and clicking button
browser.find_element(By.XPATH, LOGIN_PATH).send_keys(LOGIN)
browser.find_element(By.XPATH, PASSWORD_PATH).send_keys(PASSWORD)
browser.find_element(By.XPATH, BUTTON_PATH).click()

# Waiting for login procedure finished
time.sleep(1)

user_list = []
now_page = 1

# Getting users data from every page
while not_last_page(now_page):
    # Loading another page and get all user data rows from it
    browser.get(USER_TABLE_URL.format(now_page))
    rows = browser.find_elements(By.TAG_NAME, "tr")[2:]

    # Getting user data from each row
    for row in rows:
        user_raw_data = row.find_elements(By.TAG_NAME, "td")[:-1]
        user = dict()
        user["id"] = user_raw_data[0].get_attribute("innerHTML")
        user["name"] = user_raw_data[1].find_element(By.TAG_NAME, "a").get_attribute("innerHTML")
        user["card_id"] = user_raw_data[2].get_attribute("innerHTML")
        user["cash"] = user_raw_data[3].get_attribute("innerHTML").split()[0]
        user["phone"] = user_raw_data[4].get_attribute("innerHTML").replace(" ", "")
        user_list.append(user)
    now_page += 1

# Exporting our list of user dicts to Excel
table = pd.DataFrame.from_dict(user_list)
table.to_excel("users.xlsx", index=False);
