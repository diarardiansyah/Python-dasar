import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

emailPass = [('pbs-diar+end.game4@tokopedia.com', 'tokopedia789')]

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.implicitly_wait(4)

@pytest.mark.parametrize('a,b', emailPass)
def test_login(a,b):
    driver.get('https://seller.tokopedia.com/settings/power-merchant')
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    driver.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    driver.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    driver.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    title = driver.title
    assert title == "Masuk / Login | Tokopedia"

def test_register():
    time.sleep(3)
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="btnUpgradePMPRO"]'))))
    
    title = driver.title
    assert title == "Power Merchant | Tokopedia"
