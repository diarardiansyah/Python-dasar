from _pytest.monkeypatch import derive_importpath
import py
import pytest
from selenium import webdriver

emailPass = [('pbs-diar+pmext.bronze4@tokopedia.com', 'tokopedia789')]

@pytest.fixture
def main():
    driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get('https://seller.tokopedia.com/manage-product?tab=0')
    yield driver
    driver.quit()

@pytest.mark.parametrize('a,b',emailPass)
def test_filterNegatif(main,a,b):
    main.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    main.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    main.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    main.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    main.find_element_by_xpath('//div[@class="unf-coachmark__next-button css-1pze1a ety06v15"]').click()
    main.find_element_by_xpath('//*[@data-testid="cboMPCategory"]').click()
    main.find_element_by_xpath('//*[@data-testid="lstMPCategory-78"]').click()

    emptyState = main.find_element_by_xpath('//H3[@class="css-qdo48k-unf-heading-unf-heading e1qvo2ff3"]').text
    assert emptyState == "Oops, produk yang kamu cari tidak ditemukan"

@pytest.mark.parametrize('a,b',emailPass)
def test_positifCase(main,a,b):
    main.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    main.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    main.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    main.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    main.find_element_by_xpath('//div[@class="unf-coachmark__next-button css-1pze1a ety06v15"]').click()
    main.find_element_by_xpath('//*[@data-testid="cboMPCategory"]').click()
    main.find_element_by_xpath('//*[@data-testid="lstMPCategory-57"]').click()

    title = main.title
    assert title == "Pengaturan Produk | Tokopedia"
    

