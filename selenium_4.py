from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://orteil.dashnet.org/cookieclicker/")


driver.implicitly_wait(10)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("ProductPrice"+str(i) for i in range(1,-1,1))]


actions = ActionChains(driver)
actions.click(cookie)
for i in range(5000):
    actions.perform()
    count = cookie_count.text
    print(count)
