from selenium import webdriver

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')

def test_setup():
    driver.get('https://www.tokopedia.com/unilever')
    skip = driver.find_element_by_xpath('//div[@class="unf-coachmark__next-button css-64apm5 ety06v15"]').click()
    assert skip == None

def test_search():
    inputProductName = driver.find_element_by_xpath('//input[@class="css-ubsgp5 e16vycsw0"]').send_keys('ponds')
    driver.find_element_by_xpath('//button[@class="css-1czin5k e1v0ehno1"]').click()
    assert inputProductName == None

def test_product():
    driver.implicitly_wait(4)
    clickProduct = driver.find_element_by_xpath('//*[@data-testid="master-product-card"]').click()
    assert clickProduct == None

def test_share():
    driver.find_element_by_xpath('//*[@data-testid="pdpShareButton"]').click()
    shareProduct = driver.find_element_by_xpath('//*[@data-testid="btnTwitterShare"]').click()
    assert shareProduct == None