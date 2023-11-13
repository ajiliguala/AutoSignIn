import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# MES

options = Options()
port_number = "127.0.0.1:9527"
chromedriver_address = r"D:\Program Files\Scoop\apps\chromedriver\119.0.6045.105\chromedriver.exe"

options.add_experimental_option("debuggerAddress", port_number)

service = Service(executable_path=chromedriver_address)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://link-ai.tech/home')
time.sleep(3)
# 手机登录
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div/div/div/div[3]").click()
# 账户
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/input").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/input").clear()
driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/input").send_keys(
    '17356027574')
# 密码
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div[2]/div/div[4]/div/div/input").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div[2]/div/div[4]/div/div/input").clear()
driver.find_element(By.XPATH,
                    "/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div[2]/div/div[4]/div/div/input").send_keys(
    '112233669')
# 登录
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div[2]/div/div[5]/button").click()

# 获取下拉菜单
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]").click()
# 签到
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[3]/div/div[2]").click()
# 确定
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button").click()
time.sleep(2000)
