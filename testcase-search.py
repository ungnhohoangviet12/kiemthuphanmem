from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


test_driver = webdriver.Chrome()

#Step 1: Di chuyển đến địa chỉ "https://vlogtruyen.net"
test_driver.get('https://vlogtruyen.net')


#Step 2: Bấm vào button "Đăng nhập"
test_driver.find_element(By.CSS_SELECTOR, '#qsearch').send_keys('Để có thể sống sót')

test_driver.implicitly_wait(4)

#Step 3: Bấm vào button "Đăng nhập"


test_driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/div[2]/div/form/div[1]/div[2]/button/i').click()



#tắt testcase
# test_driver.quit()