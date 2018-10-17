from selenium import webdriver
import time 

def displayCookies():
    all = ''
    for c in driver.get_cookies():
        all += c['name'] + ' : ' + c['value'] + '\n'
    return all

driver = webdriver.Chrome()
driver.get('http://localhost/se/34.html')
driver.delete_all_cookies()
driver.add_cookie({'name' : 'foo', 'value' : 'bar'})
# driver.execute_script("document.body.style.zoom = '1.5'")
# time.sleep(1)
# driver.find_element_by_id('display_all').click()
print('\nCookies:\n{}'.format(displayCookies()))
# time.sleep(1)
driver.find_element_by_id('john').click()
# time.sleep(1)
# driver.find_element_by_id('display_all').click()
print('\nCookies:\n{}'.format(displayCookies()))
# time.sleep(1)
driver.find_element_by_id('doe').click()
# time.sleep(1)
# driver.find_element_by_id('display_all').click()
print('\nCookies:\n{}'.format(displayCookies()))
print('\n\nCookies:\n{}'.format(driver.get_cookies()))
# time.sleep(1)
driver.close()