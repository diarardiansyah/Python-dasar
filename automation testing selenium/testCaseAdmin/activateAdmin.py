import time
from selenium import webdriver

driver = webdriver.Chrome('c:\chromedriver_win32\chromedriver.exe')
driver.get('https://seller.tokopedia.com/shop/admin')

driver.maximize_window()

# Login to tokopedia seller
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
driver.find_element_by_xpath('//*[@id="zeus-root"]/div/div[3]/section/div[2]/form/button').click()

# button skip coachmark 
time.sleep(4)
driver.find_element_by_xpath("//div[@class='unf-coachmark__skip-button css-16g6whg ety06v16']").click()

# ========== activate admin ========
driver.find_element_by_xpath('//*[@data-testid="btnDeactiveAdmin"]').click()

# confirm i will activate admin
time.sleep(4) 
driver.find_element_by_xpath('//button[@class="css-evb2vf-unf-btn e1ggruw00"]').click()

# choose method verification PIN tokopedia
driver.find_element_by_xpath('//div[@class="unf-card css-1tm7yl4-unf-card eue3g1e0"]').click()

# inpu PIN tokopedia
pinTokped = '789789'
driver.find_element_by_xpath("//input[@type='tel']").send_keys(pinTokped)