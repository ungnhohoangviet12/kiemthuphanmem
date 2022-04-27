from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


test_driver = webdriver.Chrome()

#Step 1: Di chuyển đến địa chỉ "https://vlogtruyen.net"
test_driver.get('https://vlogtruyen.net')


#Step 2: Bấm vào button "Đăng nhập"
test_driver.find_element(By.CSS_SELECTOR, '#btnLogin').click()

test_driver.implicitly_wait(4)

#Step 3: Bấm vào button "Đăng nhập"
test_driver.find_element(By.XPATH, '/html/body/div[8]/div/div[2]/div[2]/form[1]/div[3]/button').click()

test_driver.find_element(By.XPATH, '/html/body/div[8]/div/div[2]/div[2]/form[1]/div[3]/a').click()

test_driver.find_element(By.XPATH, '/html/body/div[8]/div/div[2]/div[2]/form[2]/div[1]/input').send_keys('vietdepchai')
test_driver.find_element(By.XPATH, '/html/body/div[8]/div/div[2]/div[2]/form[2]/div[2]/input').send_keys('vietkenny2207')
test_driver.find_element(By.XPATH, '/html/body/div[8]/div/div[2]/div[2]/form[2]/div[3]/input').send_keys('Naninonenine23')
test_driver.find_element(By.XPATH, '/html/body/div[8]/div/div[2]/div[2]/form[2]/div[4]/input').send_keys('Naninonenine23')
test_driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div/span/div[4]').click()
test_driver.implicitly_wait(4)
test_driver.find_element(By.CSS_SELECTOR, '#recaptcha-anchor > div.recaptcha-checkbox-border').click()




#tắt testcase
# test_driver.close()
# test_driver.quit()