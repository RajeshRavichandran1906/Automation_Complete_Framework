from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for login page locators. All login page locators should come here"""
    uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
    pword = (By.CSS_SELECTOR, 'input[id=SignonPassName]')
    submit= (By.CSS_SELECTOR, '[id=SignonbtnLogin]')
    continue_login = (By.ID, 'ContinueSigninBtn')
    loader_css = "body.ibx-visible"
    
class LoginPage:
    
    user_name   =  (By.ID, "SignonUserName")
    password    =  (By.ID, 'SignonPassName')
    sign_in     =  (By.ID, "SignonbtnLogin")
    error_msg   =  (By.CSS_SELECTOR, ".dm-error")
    tour_wf     =  (By.CSS_SELECTOR, "div.dm-learn-about-webfocus")
    visit_kb    =  (By.CSS_SELECTOR, "div.dm-help-about")
