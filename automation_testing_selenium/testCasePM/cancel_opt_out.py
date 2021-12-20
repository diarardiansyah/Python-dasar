import time
from selenium import webdriver

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.get('https://seller.tokopedia.com/settings/power-merchant')

driver.maximize_window()

# Login to tokopedia Seller
sendEmail = driver.find_element_by_xpath('//*[@data-testid="email-phone-input"]')
sendEmail.send_keys('pbs-diar+pmext.bronze2@tokopedia.com')

# Click button submit 
driver.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()

# Input password
driver.implicitly_wait(4)
getPassword = driver.find_element_by_xpath('//*[@id="password-input"]')
getPassword.send_keys('tokopedia789')

# click button submit
driver.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

# click cancel opt out
time.sleep(4)
driver.find_element_by_xpath('//*[@data-testid="btnConfirmOptOut"]').click()
