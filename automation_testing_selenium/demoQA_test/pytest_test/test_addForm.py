import pytest
from selenium import webdriver

inputValue = [('Diar', 'Ardiansyah', 'diar11@gmail.com', '20', '700000', 'QA')]

driver = webdriver.Chrome('C://chromedriver_win32/chromedriver')
driver.implicitly_wait(4)

@pytest.mark.parametrize('a,b,c,d,e,f', inputValue)
def test_add(a,b,c,d,e,f):
    driver.get('https://demoqa.com/webtables')
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@id="addNewRecordButton"]').click()
    driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(a)
    driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(b)
    driver.find_element_by_xpath('//*[@id="userEmail"]').send_keys(c)
    driver.find_element_by_xpath('//*[@id="age"]').send_keys(d)
    driver.find_element_by_xpath('//*[@id="salary"]').send_keys(e)
    driver.find_element_by_xpath('//*[@id="department"]').send_keys(f)
    driver.find_element_by_xpath('//*[@id="submit"]').click()

    title = driver.title
    assert title == "ToolsQA"