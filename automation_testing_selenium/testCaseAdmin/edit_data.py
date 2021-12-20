import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.get('https://seller.tokopedia.com/shop/admin')

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

# btn skip coachmark
driver.implicitly_wait(5)
driver.find_element_by_xpath('//div[@class="unf-coachmark__skip-button css-16g6whg ety06v16"]').click()

# click dropdown button atur 
driver.find_element_by_xpath('//*[@data-testid="btnAdminListActions"]').click()

# click cta button atur ubah data
driver.find_element_by_xpath('//*[@data-testid="btnAturUbahDataAdmin"]').click()

# delete old admin email
time.sleep(4)
oldEmail = driver.find_element_by_xpath('//*[@data-testid="txtHandleAdminEmail"]')
oldEmail.send_keys(Keys.CONTROL, 'a')
oldEmail.send_keys(Keys.BACKSPACE)

# input new email admin 
newEmail = driver.find_element_by_xpath('//*[@data-testid="txtHandleAdminEmail"]')
newEmail.send_keys('pbs-diar+adminprod8@tokopedia.com')

# click button simpan 
time.sleep(4)
driver.find_element_by_xpath('//*[@data-testid="btnSubmitAdmin"]').click()

# choose method verification PIN 
driver.find_element_by_xpath('//div[@class="unf-card css-1tm7yl4-unf-card eue3g1e0"]').click()

# input PIN tokopedia
pinTokped = '789789'
inputPIN = driver.find_element_by_xpath('//input[@type="tel"]')
inputPIN.send_keys(pinTokped)




