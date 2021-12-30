from _pytest.monkeypatch import derive_importpath
import pytest
from selenium import webdriver
from getpass import getpass

username = input('enter username/email : ')
password = getpass('enter password : ')

emailPass = [(username, password)]

@pytest.fixture
def main():
    driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get('https://seller.tokopedia.com/v2/vouchertoko?status=ongoing')
    yield driver
    driver.quit()

@pytest.mark.parametrize('a,b',emailPass)
def test_filter(main,a,b):
    main.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    main.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    main.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    main.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    main.find_element_by_xpath('//*[@data-testid="cboVoucherType"]').click()
    main.find_element_by_xpath('//*[@id="merchant-root"]/div/div[2]/div/section/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/ul/li[2]/div').click()

    empty_state = main.find_element_by_xpath('//H3[@class="css-156jkm2-unf-heading-unf-heading e1qvo2ff3"]').text
    assert empty_state == "Belum ada voucher toko, nih"


    
