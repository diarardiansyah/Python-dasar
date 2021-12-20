import pytest
import time
from selenium import webdriver

unamePass = [('pbs-diar+new.end7@tokopedia.com', 'tokopedia789')]

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.implicitly_wait(4)

@pytest.mark.parametrize('a,b', unamePass)
def test_login(a,b):
    driver.get('https://seller.tokopedia.com/shop/admin/add')
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    driver.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    driver.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    driver.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    title = driver.title
    assert title == "Masuk / Login | Tokopedia"

def test_inputEmail():
    time.sleep(3)
    driver.find_element_by_xpath('//*[@data-testid="txtAdminEmail"]').send_keys('pbs-diar+adminprod1@tokopedia.com')
    error = driver.find_element_by_xpath('//P[@class="css-t9c9fq ed3tosx8"]').text

    assert error == "User sudah menjadi admin toko lain."



