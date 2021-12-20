import time
import pytest
from selenium import webdriver

unamePass = [
    ("pbs-diar+pmext.bronze2@tokopedia.com", "tokopedia789")
    ]

@pytest.fixture
def setup():
    driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
    driver.implicitly_wait(6)
    driver.get('https://seller.tokopedia.com/settings/power-merchant')
    # driver.maximize_window()
    yield driver

@pytest.mark.login
@pytest.mark.parametrize('a,b', unamePass)
def test_login(setup,a,b):
    setup.find_element_by_xpath('//*[@data-testid="email-phone-input"]').send_keys(a)
    setup.find_element_by_xpath('//*[@data-testid="email-phone-submit"]').click()
    setup.find_element_by_xpath('//*[@id="password-input"]').send_keys(b)
    setup.find_element_by_xpath('//button[@class="css-ow4jg3-unf-btn e1ggruw00"]').click()

    Title = setup.title
    assert Title == "Masuk / Login | Tokopedia"

@pytest.mark.cancel
def test_cancel(setup):
    btnCancel = setup.find_element_by_xpath('//*[@data-testid="btnConfirmOptOut"]').click()
    assert btnCancel == None