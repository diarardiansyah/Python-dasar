import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

emailPass = [('pbs-diar+pmext.bronze4@tokopedia.com', 'tokopedia789')]

@pytest.fixture
def setup():
    driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get('https://seller.tokopedia.com/manage-product?tab=0')
    yield driver
    driver.quit()

@pytest.mark.parametrize('a,b', emailPass)
def test_negatifSetPrice(setup,a,b):
    setup.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    setup.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    setup.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    setup.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    setup.find_element_by_xpath('//div[@class="unf-coachmark__next-button css-1pze1a ety06v15"]').click()
    setup.find_element_by_xpath('//*[@data-testid="ddlMPSettingProduct"]').click()
    setup.find_element_by_xpath('//*[@data-testid="lblMPDropdown-0"]').click()

    element = setup.find_element_by_id("txtAEPPrice")
    actions = ActionChains(setup)
    actions.move_to_element(element)
    actions.perform()

    time.sleep(3)
    setup.execute_script("arguments[0].click();", WebDriverWait(setup, 20).until(EC.element_to_be_clickable((By.XPATH, "txtAEPPrice"))))

    # element = setup.find_element_by_xpath('//*[@data-testid="txtAEPPrice"]')
    element.send_keys(Keys.CONTROL,'a')
    element.send_keys(Keys.BACKSPACE)

    error_state = setup.find_element_by_xpath('//div[@class="css-1sgbou1"]').text
    assert error_state == "Harga minimum produk adalah Rp 100"
