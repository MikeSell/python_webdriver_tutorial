import unittest
from selenium import webdriver
from page import LoginPage
from locators import CommonPageLocators
from locators import LoginPageLocators
from locators import AdminPageLocators


class TestPyOrgBase(unittest.TestCase):
    """
    TBD
    """
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        self.driver.close()

class TestLogin(TestPyOrgBase):
    """
    TBD
    """
    def setUp(self):
        super().setUp()
        self.login = LoginPage(self.driver)

    def test_TC_L_001(self):
        self.login.assert_elem_text(LoginPageLocators.LOGIN_PANEL, 'LOGIN Panel')
        usr_name_input = self.login.driver.find_element(*LoginPageLocators.USERNAME)
        self.assertEqual(usr_name_input.tag_name, 'input')
        password_input = self.login.driver.find_element(*LoginPageLocators.PASSWORD)
        self.assertEqual(password_input.tag_name, 'input')
        self.login.is_clickable(LoginPageLocators.LOGIN_BUTTON)


    def test_TC_L_002(self):
        self.login.send_text(LoginPageLocators.USERNAME, self.login.default_username)
        self.login.send_text(LoginPageLocators.PASSWORD, self.login.default_password)
        self.login.click(LoginPageLocators.LOGIN_BUTTON)
        self.assertTrue('dashboard' in self.login.driver.current_url)
        self.assertTrue('<h1>Dashboard</h1>' in self.login.driver.page_source)

    def test_TC_L_003(self):
        self.login.send_text(LoginPageLocators.USERNAME, self.login.default_username)
        self.login.send_text(LoginPageLocators.PASSWORD, 'password')
        self.login.click(LoginPageLocators.LOGIN_BUTTON)
        self.login.assert_elem_text(LoginPageLocators.SPAN_MSG, 'Invalid credentials')


class TestAdmin(TestPyOrgBase):

    @classmethod
    def setUpClass(cls):
        super().setUp(cls)
        cls.login = LoginPage(cls.driver)
        cls.login.login()
        cls.page = cls.login

    def test_TC_A_001(self):
        job_title = 'QA automation developer'
        job_description = 'Automating tests in Python and Selenium Webdriver.'
        self.page.hover_to(CommonPageLocators.ADMIN)
        self.page.hover_to(AdminPageLocators.JOB)
        self.page.click(AdminPageLocators.JOB_TITLES)
        self.page.click(AdminPageLocators.JOB_TITLE_ADD_BTN)
        self.page.send_text(AdminPageLocators.JOB_TITLE_JT_FIELD, job_title)
        self.page.send_text(AdminPageLocators.JOB_TITLE_JD_FIELD, job_description)
        self.page.click(AdminPageLocators.JOB_TITLE_SAVE_BTN)
        table = self.page.get_elem(AdminPageLocators.JOB_TITLE_TABLE)
        assert job_title in table.get_attribute('innerHTML')


    def test_TC_A_002(self):
        pass

    @classmethod
    def tearDownClass(cls):
        super().tearDown(cls)


if __name__ == '__main__':
    unittest.main()