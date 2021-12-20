from os import times
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.get('https://www.tokopedia.com/')

# driver.maximize_window()

# Login to tokopedia
driver.find_element_by_xpath('//*[@data-testid="btnHeaderLogin"]').click()

driver.implicitly_wait(5)
inputEmail = driver.find_element_by_xpath('//*[@data-testid="email-phone-input"]')
inputEmail.send_keys('pbs-diar+pmext.bronze4@tokopedia.com')

driver.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()

driver.implicitly_wait(5)
inpuPassword = driver.find_element_by_xpath('//*[@id="password-input"]')
inpuPassword.send_keys('tokopedia789')

driver.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

menu = driver.find_element_by_xpath('//*[@data-testid="btnHeaderMyshop"]')
hoverMenu = ActionChains(driver)
hoverMenu.move_to_element(menu)
hoverMenu.perform()

driver.find_element_by_xpath('//*[@id="my-shop-overlay"]/div/div[2]/div/a').click()

# driver.find_element_by_xpath('//button[@class="css-evb2vf-unf-btn e1ggruw00"]').click()
button = driver.find_element_by_xpath('//button[@class="css-evb2vf-unf-btn e1ggruw00"]')
driver.execute_script("arguments[0].click();", button)

skipCoachmark = driver.find_element_by_xpath('//*[@data-testid="btnHomeCoachmarkSkip"]')
skipCoachmark.click()

print("===================")
print("Testing Passed!!!!!")