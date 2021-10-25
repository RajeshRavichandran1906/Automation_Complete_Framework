from selenium.webdriver.common.by import By
class MobileLoginPageLocators(object):

    ''''Mobile Favs login Page'''
    
    username=(By.ID,"IBIB_userid")
    password=(By.ID,"IBIB_password")
    signin=(By.CSS_SELECTOR,"a[role='button'][onclick*='javascript:submitSignonRequest']")

    ''' Mobile View Login Page '''
    
    mv_username=(By.ID,'SignonUserName')
    mv_password=(By.ID,'SignonPassName')
    mv_signin=(By.ID,'SignonbtnLogin')
    