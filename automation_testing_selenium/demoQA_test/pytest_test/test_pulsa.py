import pytest
import time
from selenium import webdriver

unamePass = [('pbs-diar+new.end7@tokopedia.com', 'tokopedia789')]

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.implicitly_wait(4)

@pytest.mark.parametrize('a,b', unamePass)
def test_login(a,b):
    driver.get('https://www.tokopedia.com/')
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@data-testid="btnHeaderLogin"]').click()
    driver.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    driver.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    driver.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    driver.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    title = driver.title
    assert title == 'Situs Jual Beli Online Terlengkap, Mudah & Aman | Tokopedia'

def test_closePopUp():
    time.sleep(4)
    driver.find_element_by_xpath('//button[@class="css-18i7x95-unf-modal__icon e1s17eky1"]').click()

    title = driver.title
    assert title == 'Situs Jual Beli Online Terlengkap, Mudah & Aman | Tokopedia'

def test_pulsa():
    time.sleep(4)
    driver.find_element_by_xpath('//input[@name="clientNumber"]').send_keys('08787612777')
    driver.implicitly_wait(4)
    driver.find_element_by_xpath('//div[@class="css-1qyfhhl e15j6tp63"]').click()
    driver.find_element_by_xpath('//*[@data-testid="Rp11.500"]').click()
    driver.find_element_by_xpath('//button[@class="css-12s922k-unf-btn e1ggruw00"]').click()

    title = driver.title
    assert title == 'Pembayaran | Tokopedia'
    