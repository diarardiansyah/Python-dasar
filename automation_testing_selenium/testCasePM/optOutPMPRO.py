import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('c:\chromedriver_win32\chromedriver.exe')
driver.get('https://seller.tokopedia.com/settings/power-merchant')

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

# click cta 'klik disini'
driver.find_element_by_xpath('//*[@data-testid="btnOptOut"]').click()
# Confirm downgrade to PM 
driver.find_element_by_xpath('//*[@data-testid="btnConfirmDowngradeToPM"]').click()

# Choose rate 
driver.find_element_by_xpath('//*[@data-testid="btnPMRate"]').click()
# Click checkbos 
driver.find_element_by_xpath('//*[@data-testid="chkFirstReason"]').click()

# Scrool to element 
element = driver.find_element_by_xpath('//*[@data-testid="chkSecondReasonTwo"]')
actions = ActionChains(driver)
actions.move_to_element(element).perform()

# Click second quisioniare opt out from PM PRO
time.sleep(3)
driver.find_element_by_xpath('//*[@data-testid="chkSecondReasonTwo"]').click()

time.sleep(3)
driver.find_element_by_xpath('//*[@data-testid="btnSendReason"]').click()

print('Testing Passed')