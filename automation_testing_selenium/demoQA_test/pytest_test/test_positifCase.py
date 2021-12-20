from abc import abstractclassmethod
from selenium import webdriver

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')

def test_tiket():
    driver.get('https://tiket.tokopedia.com/kereta-api/')
    driver.maximize_window()
    tiket = driver.title
    assert tiket == 'Pesan Tiket Kereta Api Online, Harga Promo dan Murah - Tokopedia'

def test_asal():
    driver.find_element_by_xpath('//*[@data-testid="selectorAsal"]').click()
    driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div/div/div[2]/section/div[3]/div/div[4]').click()
    optionText = driver.find_element_by_xpath('//H1[@class="css-1wwlanz"]').text
    assert optionText == 'Pesan tiket kereta online di Tokopedia'

def test_continue():
    driver.find_element_by_xpath('//div[@class="css-1bh52ki e4ba57s0"]').click()
    driver.find_element_by_xpath('//*[@data-testid="searchTicketButton"]').click()
    text1 = driver.title
    assert text1 == 'Pesan Tiket Kereta Api Online, Harga Promo dan Murah - Tokopedia'