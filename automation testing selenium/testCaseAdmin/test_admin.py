import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('c:\chromedriver_win32\chromedriver.exe') 
driver.get('https://seller.tokopedia.com/shop/admin')

driver.maximize_window()

#driver.execute_script("document.body.style.zoom='80%'")
send_email = driver.find_element_by_xpath('//*[@data-testid="email-phone-input"]')
# input email user
send_email.send_keys('pbs-diar+pmext.bronze@tokopedia.com')

# Click cta selanjutnya 
driver.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()

# input password user 
driver.implicitly_wait(4)
setPasword = driver.find_element_by_xpath('//*[@id="password-input"]')
setPasword.send_keys('tokopedia789')

# click button submit
driver.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

# click button add admin
driver.implicitly_wait(4)
driver.find_element_by_xpath('//*[@data-testid="btnAddAdminEmpty"]').click()

# input email admin
emailAdmin = driver.find_element_by_xpath('//*[@data-testid="txtAdminEmail"]')
emailAdmin.send_keys('pbs-diar+adminprod6@tokopedia.com')

# click dropdown jenis akses
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="merchant-root"]/div/div[2]/div/div/div[2]/div/section/div[2]/div[4]/div/div/div[1]').click()

# click role balas pesan pembeli
driver.find_element_by_xpath('//*[@data-testid="chkAccessList-1"]').click()

driver.find_element_by_xpath('//*[@id="merchant-root"]/div/div[2]/div/div/div[2]/div/section/div[2]/div[4]/div/div/div[1]').click()

# click checkbox tnc
# driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="merchant-root"]/div/div[2]/div/div/div[3]/div/div').click()

# click button kirim akses
time.sleep(3)
clickCta = driver.find_element_by_xpath('//*[@data-testid="btnSendAkses"]')
clickCta.click()

# choose method verified PIN
driver.find_element_by_xpath('//div[@class="unf-card css-1tm7yl4-unf-card eue3g1e0"]').click()

# input PIN tokopedia
pin = '789789'
driver.find_element_by_xpath("//input[@type='tel']").send_keys(pin)

print('pengujian sukses')