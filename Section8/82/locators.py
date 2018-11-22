from selenium.webdriver.common.by import By

class CommonPageLocators:
    pass

class LoginPageLocators:
    USERNAME = (By.ID, 'txtUsername')
    PASSWORD = (By.ID, 'txtPassword')
    LOGIN_BUTTON = (By.ID, 'btnLogin')
    LOGIN_PANEL = (By.ID, 'logInPanelHeading')
    SPAN_MSG = (By.ID, 'spanMessage')

    