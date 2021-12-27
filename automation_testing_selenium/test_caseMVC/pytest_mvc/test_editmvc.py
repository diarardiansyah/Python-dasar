import time
import pytest 
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

emailPass = [('pbs-diar+pmext.bronze4@tokopedia.com', 'tokopedia789')]

editMvc = [('vouchertest', '30000', '30')]

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.implicitly_wait(4)

@pytest.mark.parametrize('a,b', emailPass)
def test_login(a,b):
    driver.get('https://seller.tokopedia.com/v2/vouchertoko/edit/6725880')
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    driver.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    driver.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    driver.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    title = driver.title
    assert title == "Masuk / Login | Tokopedia"

@pytest.mark.parametrize('c,e,f',editMvc)
def test_edit(c,e,f):
    time.sleep(3)
    edit1 = driver.find_element_by_xpath('//*[@data-testid="txtVoucherName"]')
    edit1.send_keys(Keys.CONTROL,'a')
    edit1.send_keys(Keys.BACKSPACE)
    edit1.send_keys(c)
    edit1 = driver.find_element_by_xpath('//*[@data-testid="txtVoucherBenefitIdr"]')
    edit1.send_keys(Keys.CONTROL,'a')
    edit1.send_keys(Keys.BACKSPACE)
    edit1.send_keys(e)
    edit1 = driver.find_element_by_xpath('//*[@data-testid="txtVoucherQuota"]')
    edit1.send_keys(Keys.CONTROL,'a')
    edit1.send_keys(Keys.BACKSPACE)
    edit1.send_keys(f)
    driver.find_element_by_xpath('//*[@data-testid="chkVoucherTNCCheckbox"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@data-testid="btnVoucherSubmit"]').click()

    title1 = driver.title
    assert title1 == "Voucher | Tokopedia"