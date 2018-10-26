import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestPythonOrg(unittest.TestCase):
    """
    Example tests for testing python.org
    """
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_TC001_py3_doc_button(self):
        self.driver.get("https://www.python.org")
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "documentation")))
        ActionChains(self.driver).move_to_element(element).perform()
        css_selector = "#documentation > ul > li.tier-2.super-navigation > p.download-buttons > a:nth-child(1)"
        py3docbutton = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
        assert py3docbutton.text == "Python 3.x Docs"
        py3docbutton.click()
        assert self.driver.current_url == 'https://docs.python.org/3/'

    def test_TC002_pass_mismatch_message(self):
        self.driver.get("https://www.python.org")
        self.driver.find_element_by_css_selector('#id-search-field').send_keys('blahblah')
        self.driver.find_element_by_css_selector('#submit').click()
        results_elem = self.driver.find_element_by_xpath("//h3[text()='Results']/following-sibling::ul")
        assert results_elem.text == 'No results found.'

    def test_TC003_verify_upcoming_events_section_present(self):
        self.driver.get("https://www.python.org/about/")
        css_locator = "#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > h2"
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_locator)))
        assert element.text == "Upcoming Events"

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()