from selenium import webdriver
from bs4 import BeautifulSoup
import requests, sys, time


def sel():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.python.org/events/')
    event_list = driver.find_element_by_css_selector('#content ul[class="list-recent-events menu"]')
    return BeautifulSoup(event_list.get_attribute('innerHTML'), 'html.parser')


def req():
    events_html = requests.get('https://www.python.org/events/')
    return BeautifulSoup(events_html.content, 'html.parser')


if __name__ == '__main__':
    start = time.time() 
    html_list = eval(sys.argv[1])()
    times = html_list.select('time')
    locations = html_list.select('.event-location')
    for i in range(len(times)):
        print('{}\t{}'.format(times[i].text[:6], locations[i].text))
    print('------------------------------------------------')
    print('Runtime: {:.2f} s'.format(time.time()-start))