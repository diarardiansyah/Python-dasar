import time
from selenium import webdriver

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.get('https://seller.tokopedia.com/shop/admin')

driver.maximize_window()

# Login to tokopedia Seller
sendEmail = driver.find_element_by_xpath('//*[@data-testid="email-phone-input"]')
sendEmail.send_keys('pbs-deyandra.a+37@tokopedia.com')

# Click button submit 
driver.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
 
# Input password
driver.implicitly_wait(4)
getPassword = driver.find_element_by_xpath('//*[@id="password-input"]')
getPassword.send_keys('tokopedia789')

# click button submit
driver.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

# btn skip coachmark
time.sleep(3)
driver.find_element_by_xpath('//div[@class="unf-coachmark__skip-button css-16g6whg ety06v16"]').click()

# click button add admin 
driver.find_element_by_xpath('//*[@data-testid="btnAddAdmin"]').click()

# choose location admin 
driver.find_element_by_xpath('//*[@data-testid="btnAddAdminLokasi"]').click()

# input email admin 
emailInput = driver.find_element_by_xpath('//*[@data-testid="txtAdminEmail"]')
emailInput.send_keys('pbs-diar+adm80@tokopedia.com')

# click dropdown jenis akses
time.sleep(3)
driver.find_element_by_xpath('//*[@data-testid="ddlAccessAdmin"]').click()

# choose role admin 
driver.find_element_by_xpath('//*[@data-testid="chkAccessList-5"]').click()

# click dropdown location admin 
driver.find_element_by_xpath('//*[@data-testid="ddlShopLocation"]').click()

# choose location admin 
driver.find_element_by_xpath('//*[@data-testid="ddlShopLocationList-0"]').click()

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



