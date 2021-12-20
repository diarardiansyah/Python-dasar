from selenium import webdriver
import time

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.get('https://seller.tokopedia.com/settings/power-merchant')

driver.maximize_window()

# Login to tokopedia Seller
sendEmail = driver.find_element_by_xpath('//*[@data-testid="email-phone-input"]')
sendEmail.send_keys('pbs-diar+new.end2@tokopedia.com')

# Click button submit 
driver.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()

# Input password
driver.implicitly_wait(4)
getPassword = driver.find_element_by_xpath('//*[@id="password-input"]')
getPassword.send_keys('tokopedia789')

# click button submit
driver.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

# Click cta button daftar sekarang
time.sleep(4)
btnDaftarSekarang = driver.find_element_by_xpath('//button[@class="css-zez37h-unf-btn e1ggruw00"]')
btnDaftarSekarang.click()

# click button add 1 product active
driver.find_element_by_xpath('//button[@class="css-lby9rr-unf-btn e1ggruw00"]').click()