import pytest
import base64
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# ========= Paswword encryption ===============
message = 'dG9rb3BlZGlhNzg5'
message_bytes = message.encode('ascii')
base64_bytest = base64.b64decode(message_bytes)
base64_message = base64_bytest.decode('ascii')

emailPass = [('pbs-diar+end.game4@tokopedia.com',base64_message)]

@pytest.fixture
def main():
    driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get('https://seller.tokopedia.com/settings/power-merchant')
    yield driver
    driver.quit()

@pytest.mark.parametrize('a,b', emailPass)
def test_toRM(main,a,b):
    # =============== Login =====================
    main.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    main.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    main.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    main.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    # =============== Opt Out Process =================
    time.sleep(3)
    main.find_element_by_xpath('//*[@data-testid="btnOptOut"]').click()
    main.find_element_by_xpath('//*[@data-testid="btnConfirmDowngradeToRM"]').click()
    main.find_element_by_xpath('//*[@data-testid="btnPMRate"]').click()
    main.find_element_by_xpath('//*[@data-testid="chkFirstReason"]').click()

    element = main.find_element_by_xpath('//*[@data-testid="chkSecondReasonTwo"]')
    actions = ActionChains(main)
    actions.move_to_element(element)
    actions.perform()

    main.execute_script("arguments[0].click();", WebDriverWait(main, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="chkSecondReasonTwo"]'))))

    main.find_element_by_xpath('//*[@data-testid="btnSendReason"]').click()
    
    title = main.title
    assert title == "Power Merchant | Tokopedia"

@pytest.mark.parametrize('a,b', emailPass)
def test_cancel(main,a,b):
    # =============== Login =====================
    main.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    main.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    main.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    main.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    # ============== Cancel Opt Out =============
    time.sleep(4)
    main.find_element_by_xpath('//*[@data-testid="btnConfirmOptOut"]').click()

    title = main.title
    assert title == "Power Merchant | Tokopedia"

@pytest.mark.parametrize('a,b', emailPass)
def test_optOutPM(main,a,b):
    # =============== Login =====================
    main.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    main.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    main.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    main.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    # ============== Opt out process to PM =========
    time.sleep(3)
    main.find_element_by_xpath('//*[@data-testid="btnOptOut"]').click()
    main.find_element_by_xpath('//*[@data-testid="btnConfirmDowngradeToPM"]').click()
    main.find_element_by_xpath('//*[@data-testid="btnPMRate"]').click()
    main.find_element_by_xpath('//*[@data-testid="chkFirstReason"]').click()

    element = main.find_element_by_xpath('//*[@data-testid="chkSecondReasonTwo"]')
    actions = ActionChains(main)
    actions.move_to_element(element)
    actions.perform()

    main.execute_script("arguments[0].click();", WebDriverWait(main, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="chkSecondReasonTwo"]'))))

    main.find_element_by_xpath('//*[@data-testid="btnSendReason"]').click()
    
    title = main.title
    assert title == "Power Merchant | Tokopedia"




