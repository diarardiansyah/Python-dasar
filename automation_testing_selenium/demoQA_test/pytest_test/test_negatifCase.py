from selenium import webdriver

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')

def test_tiket():
    driver.get('https://tiket.tokopedia.com/kereta-api/')
    tiket = driver.title
    assert tiket == 'Pesan Tiket Kereta Api Online, Harga Promo dan Murah - Tokopedia'

def test_tiket2():
    driver.find_element_by_xpath('//*[@data-testid="selectorAsal"]').click()
    driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div/div/div[2]/section/div[3]/div/div[2]').click()
    error = driver.find_element_by_xpath('//div[@class="error-text"]').text
    assert error == 'Stasiun keberangkatan dan tujuan tidak boleh sama.'
    