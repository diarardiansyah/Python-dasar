import time
from attr.setters import NO_OP
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

unamePass = [
    ("pbs-diar+pmext.bronze2@tokopedia.com", "tokopedia789")
    ]

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.implicitly_wait(6)

@pytest.mark.parametrize('a,b', unamePass)
def test_login(a,b):
    driver.get('https://seller.tokopedia.com/settings/power-merchant')
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    driver.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    driver.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    driver.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    Title = driver.title
    assert Title == "Masuk / Login | Tokopedia"

def test_klik():
    time.sleep(4)
    klikDisini = driver.find_element_by_xpath('//*[@data-testid="btnOptOut"]').click()
    assert klikDisini == None

def test_to_RM():
    driver.implicitly_wait(4)
    optOutRM = driver.find_element_by_xpath('//*[@data-testid="btnConfirmDowngradeToRM"]').click()
    assert optOutRM == None

def test_rate():
    ratePM = driver.find_element_by_xpath('//*[@data-testid="btnPMRate"]').click()
    assert ratePM == None

def test_quis1():
    time.sleep(4)
    quisFirst = driver.find_element_by_xpath('//*[@data-testid="chkFirstReason"]').click()
    quisFirst == None

def test_quis2():
    element = driver.find_element_by_xpath('//*[@data-testid="chkSecondReasonTwo"]')
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()
    time.sleep(4)
    quisSecond = driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="chkSecondReasonTwo"]'))))
    assert quisSecond == None

def test_submit():
    btnSubmit = driver.find_element_by_xpath('//*[@data-testid="btnSendReason"]').click()
    assert btnSubmit == None