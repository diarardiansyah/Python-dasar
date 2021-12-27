import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

emailPass = [('pbs-diar+pmext.bronze4@tokopedia.com', 'tokopedia789')]

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.implicitly_wait(4)


@pytest.mark.parametrize('a,b', emailPass)
def test_login(a,b):
    driver.get('https://seller.tokopedia.com/manage-product')
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    driver.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    driver.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    driver.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    title = driver.title
    assert title == "Masuk / Login | Tokopedia"

def test_delete():
    time.sleep(3)
    driver.find_element_by_xpath('//div[@class="unf-coachmark__next-button css-1pze1a ety06v15"]').click()
    driver.find_element_by_xpath('//*[@data-testid="ddlMPSettingProduct"]').click()
    
    element = driver.find_element_by_xpath('//*[@data-testid="lblMPDropdown-7"]')
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()

    time.sleep(3)
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="lblMPDropdown-7"]'))))

    driver.find_element_by_xpath('//*[@data-testid="chpMPCashback0"]').click()
    driver.find_element_by_xpath('//*[@data-testid="btnMPAturCashbackSave"]').click()
    
    title1 = driver.title
    assert title1 == "Pengaturan Produk | Tokopedia"
