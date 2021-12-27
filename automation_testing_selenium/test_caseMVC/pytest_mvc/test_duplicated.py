import time
import pytest 
from selenium import webdriver

emailPass = [('pbs-diar+pmext.bronze4@tokopedia.com', 'tokopedia789')]

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.implicitly_wait(4)

@pytest.mark.parametrize('a,b', emailPass)
def test_login(a,b):
    driver.get('https://seller.tokopedia.com/v2/vouchertoko/?status=ongoing')
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    driver.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    driver.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    driver.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    title = driver.title
    assert title == "Masuk / Login | Tokopedia"

def test_duplicated():
    time.sleep(3)
    driver.find_element_by_xpath('//*[@data-testid="btnVoucherMainActionList-setting"]').click()
    driver.find_element_by_xpath('//*[@data-testid="cboVoucherActionList-duplikat"]').click()
    driver.find_element_by_xpath('//div[@class="css-26xadv"]').click()
    driver.find_element_by_xpath('//*[@data-testid="txtVoucherCode"]').send_keys('221296')
    driver.find_element_by_xpath('//*[@data-testid="chkVoucherTNCCheckbox"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@data-testid="btnVoucherSubmit"]').click()

    title1 = driver.title
    assert title1 == "Voucher | Tokopedia"