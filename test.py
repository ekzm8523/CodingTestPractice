"""
auto_complete.py
@Name: Auto Complete Inflearn Lecture
@Author: Seongil Kim
@Date: 2022. 9. 20
@Description: Complete all lecture in inflearn
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Setting chromedriver
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)

    return driver

# login infleran
def login(email_str, password_str, driver):
    url = 'https://www.inflearn.com/business/126'
    driver.get(url)

    email = driver.find_element("xpath",'//*[@id="main"]/section/form/input[1]')
    password = driver.find_element("xpath",'//*[@id="main"]/section/form/input[2]')

    email.send_keys(email_str)
    password.send_keys(password_str)

    btn = driver.find_element("xpath",'//*[@id="main"]/section/form/button')
    btn.click()

    sleep(2)

    driver.find_element("xpath",'//*[@id="root"]/div[4]/div[2]/div[2]/div/button[2]').click()

# auto complete lecture
def auto_complete(driver, course_name, cur, end):
    for idx in range(cur,end+1):
        lecture_url = f'https://www.inflearn.com/course/{course_name}/unit/{idx}?tab=curriculum'
        driver.get(lecture_url)

        sleep(3)

        elements = driver.find_elements(by= By.TAG_NAME, value='button')

        for element in elements:
            if element.text.find('봤어요') != -1:
                element.click()
                break

if __name__ == "__main__":
    email_str = ""
    password_str = ""
    course_name = '' # utf-8로 인코딩 된 코스 이름 ex) jpa-spring-data-%EA%B8%B0%EC%B4%88
    cur = 98245 # 시작하는 강의 번호
    end = 98231# 끝나는 강의 번호

    driver = setup_driver()
    login(email_str, password_str, driver)
    auto_complete(driver, course_name, cur, end)

    driver.quit()