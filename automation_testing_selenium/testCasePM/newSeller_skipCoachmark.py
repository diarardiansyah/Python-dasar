import time
from selenium import webdriver

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.get('https://seller.tokopedia.com/settings/power-merchant')

driver.maximize_window()

# Login to tokopedia Seller
sendEmail = driver.find_element_by_xpath('//*[@data-testid="email-phone-input"]')
sendEmail.send_keys('pbs-diar+new.end7@tokopedia.com')

# Click button submit 
driver.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
 
# Input password
driver.implicitly_wait(4)
getPassword = driver.find_element_by_xpath('//*[@id="password-input"]')
getPassword.send_keys('tokopedia789')

# click button submit
driver.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

# skip coachmark 1 
time.sleep(3)
skipCoachmark1 = driver.find_element_by_xpath('//div[@class="unf-coachmark__next-button css-1itmyze ety06v15"]')
skipCoachmark1.click()

# skip coachmark 2
driver.implicitly_wait(3)
skipCoachmark2 = driver.find_element_by_xpath('//div[@class="unf-coachmark__next-button css-1itmyze ety06v15"]')
skipCoachmark2.click()

# skip coachmark 3
driver.implicitly_wait(3)
skipCoachmark3 = driver.find_element_by_xpath('//div[@class="unf-coachmark__next-button css-1itmyze ety06v15"]')
skipCoachmark3.click()