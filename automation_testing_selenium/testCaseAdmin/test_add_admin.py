import time
from selenium import webdriver

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

# Click button add admin 
driver.find_element_by_xpath('//*[@data-testid="btnAddAdminEmpty"]').click()

# fill email admin 
fillEmail = driver.find_element_by_xpath('//*[@data-testid="txtAdminEmail"]')
fillEmail.send_keys('pbs-diar+adm80@tokopedia.com')

# click dropdown jenis akses
time.sleep(3)
driver.find_element_by_xpath('//*[@id="merchant-root"]/div/div[2]/div/div/div[2]/div/section/div[2]/div[4]/div/div/div[1]').click()

# choose jenis akses admin 
driver.find_element_by_xpath('//*[@data-testid="chkAccessList-2"]').click()

# click t&c 
driver.find_element_by_xpath('//*[@id="merchant-root"]/div/div[2]/div/div/div[3]/div/div').click()

# click button kirim akses
time.sleep(4)
driver.find_element_by_xpath('//*[@data-testid="btnSendAkses"]').click()

# choose method verification PIN 
driver.find_element_by_xpath('//div[@class="unf-card css-1tm7yl4-unf-card eue3g1e0"]').click()

# input PIN tokopedia
pinTokped = '789789'
inputPIN = driver.find_element_by_xpath('//input[@type="tel"]')
inputPIN.send_keys(pinTokped)

