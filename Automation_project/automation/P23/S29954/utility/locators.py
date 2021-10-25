'''
Created on Mar 20, 2019

@author: ml12793
'''
from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    '''
    Version 1 - this class contains reusable locators on the signin page
    
    '''
    uid = (By.ID,'SignonUserName')
    pwd = (By.ID, 'SignonPassName')
    submit= (By.ID, 'SignonbtnLogin')

class OlapLocators(object):
    
    panel_content_button = (By.CSS_SELECTOR, '.left-main-panel-content-button')
    domain_button = (By.CSS_SELECTOR, 'div[title=Domains]')
    output_popup = (By.CSS_SELECTOR, '.output-area')
    olap_panel_run_button = (By.CSS_SELECTOR, '#olaprunlabel')
    folder = (By.CSS_SELECTOR, '.folder-div')
    file = (By.CSS_SELECTOR, '.file-item')
    
class HomePageLocators(object):
    '''this class contains reusable locators on the new home page'''
    view_button = (By.CSS_SELECTOR, '.toolbar-button-div:first-child')
