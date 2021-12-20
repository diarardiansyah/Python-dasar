import time
from selenium import webdriver
import selenium
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

# click button disini 
driver.implicitly_wait(6)
driver.find_element_by_xpath('//*[@data-testid="btnOptOut"]').click()

# choose opt out from PM PRO to PM 
driver.find_element_by_xpath('//*[@data-testid="btnConfirmDowngradeToPM"]').click()

# choose rate
driver.find_element_by_xpath('//*[@data-testid="btnPMRate"]').click()

# click checkbox quisioner 1
driver.find_element_by_xpath('//*[@data-testid="chkFirstReason"]').click()

# click checkbox second quisionaire
element = driver.find_element_by_xpath('//*[@data-testid="chkSecondReasonTwo"]')

actions = ActionChains(driver)
actions.move_to_element(element)
actions.perform()

time.sleep(4)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="chkSecondReasonTwo"]'))))

# click submit
driver.find_element_by_xpath('//*[@data-testid="btnSendReason"]').click()

