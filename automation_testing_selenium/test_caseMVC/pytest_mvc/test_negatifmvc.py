import time
import pytest
from selenium import webdriver

emailPass = [('pbs-diar+pmext.bronze4@tokopedia.com', 'tokopedia789')]

@pytest.fixture
def setup():
    driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get('https://seller.tokopedia.com/v2/vouchertoko/?status=ongoing')
    yield driver
    driver.quit()

@pytest.mark.parametrize('a,b', emailPass)
def test_negatifCase(setup,a,b):
    setup.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    setup.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    setup.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    setup.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    time.sleep(3)
    setup.find_element_by_xpath('//*[@data-testid="btnVoucherMainActionList-setting"]').click()
    setup.find_element_by_xpath('//*[@data-testid="cboVoucherActionList-duplikat"]').click()
    setup.find_element_by_xpath('//div[@class="css-26xadv"]').click()
    setup.find_element_by_xpath('//*[@data-testid="chkVoucherTNCCheckbox"]').click()
    
    error = setup.find_element_by_xpath('//P[@class="css-t9c9fq ed3tosx8"]').text
    assert error == "Kode voucher tidak boleh kosong."

    