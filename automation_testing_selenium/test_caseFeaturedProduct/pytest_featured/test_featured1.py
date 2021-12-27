from _pytest.monkeypatch import derive_importpath
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

emailPass = [('pbs-diar+pmext.bronze4@tokopedia.com', 'tokopedia789')]

@pytest.fixture
def main():
    driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get('https://seller.tokopedia.com/manage-product')
    yield driver
    driver.quit()

@pytest.mark.featuredProduct
@pytest.mark.parametrize('a,b',emailPass)
def test_featuredProduct(main,a,b):
    main.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    main.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    main.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    main.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    main.find_element_by_xpath('//div[@class="unf-coachmark__next-button css-1pze1a ety06v15"]').click()
    main.find_element_by_xpath('//*[@data-testid="ddlMPSettingProduct"]').click()

    element = main.find_element_by_xpath('//*[@data-testid="lblMPDropdown-8"]')
    actions = ActionChains(main)
    actions.move_to_element(element)
    actions.perform()

    main.execute_script("arguments[0].click();", WebDriverWait(main, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="lblMPDropdown-8"]'))))

    main.find_element_by_xpath('//*[@data-testid="btnMPTambahkan"]').click()

    title = main.title
    assert title == "Pengaturan Produk | Tokopedia"

@pytest.mark.filterFeatured
@pytest.mark.parametrize('a,b',emailPass)
def test_filter(main,a,b):
    main.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    main.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    main.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    main.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    main.find_element_by_xpath('//div[@class="unf-coachmark__next-button css-1pze1a ety06v15"]').click()
    main.find_element_by_xpath('//*[@data-testid="cboMPOtherFilter"]').click()
    main.find_element_by_xpath('//*[@data-testid="lstMPFilterBy-isFeaturedOnly"]').click()

    title = main.title
    assert title == "Pengaturan Produk | Tokopedia"


        