'''
Created on July 10th, 2019

@author: ml12793
'''
from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    '''this class contains reusable locators on the signin page'''
    uid = (By.ID,'SignonUserName')
    pwd = (By.ID, 'SignonPassName')
    submit= (By.ID, 'SignonbtnLogin')
    
class ParisHomePageLocators(object):
    '''this class contains reusable locators on the paris home page'''
    banner_link_menus = (By.CSS_SELECTOR, 'div[data-ibx-type="homeMenus"] div[role="button"]')
    tab_buttons = (By.CSS_SELECTOR, '.ibx-tab-button')
    home_domains_breadcrumb_items = (By.CSS_SELECTOR, '.home-domains-breadcrumb-item')
    right_click_menu_run = (By.CSS_SELECTOR, 'div[action="run"]')
    right_click_menu_favorites = (By.CSS_SELECTOR, 'div[action="favorites"]')

class HomePageLocators(object):
    '''this class contains reusable locators on the new home page'''
    panel_content_button = (By.CSS_SELECTOR, '.left-main-panel-content-button')
    domain_button = (By.CSS_SELECTOR, 'div[title=Domains]')
    folder = (By.CSS_SELECTOR, '.folder-div')
    view_button = (By.CSS_SELECTOR, '.toolbar-button-div:first-child')
    file = (By.CSS_SELECTOR, '.file-item')
    common_tab = (By.CSS_SELECTOR, '.ibx-csl-item:first-child')
    other_tab = (By.CSS_SELECTOR, '.ibx-csl-item:last-child')
    designer_tab = (By.CSS_SELECTOR, '.ibx-csl-item:nth-child(3)')
    page_button = (By.CSS_SELECTOR, 'div[data-ibxp-text="Page"]')
    portal_button = (By.CSS_SELECTOR, 'div[data-ibxp-text="Portal"]')
    text_editor_button = (By.CSS_SELECTOR, 'div[data-ibxp-text="Text Editor"]')
    fex_button = (By.CSS_SELECTOR, 'div[data-ibxp-user-value="fex"]')
    right_click_menu_run = (By.CSS_SELECTOR, 'div[data-ibxp-command="cmdRun"]')
    right_click_menu_edit = (By.CSS_SELECTOR, 'div[data-ibxp-command="cmdEdit"]')
    right_click_menu_copy = (By.CSS_SELECTOR, 'div[data-ibxp-command="cmdCopy"]')
    right_click_menu_paste = (By.CSS_SELECTOR, 'div[data-ibxp-command="cmdPaste"]')
    right_click_menu_publish = (By.CSS_SELECTOR, 'div[data-ibxp-command="cmdPublish"]')   
    right_click_menu_run_as = (By.CSS_SELECTOR, 'div[data-ibx-name="miMenuItemRunDS"]')
    right_click_menu_run_in_new_window = (By.CSS_SELECTOR, 'div[action="runInWindow"]')
    right_click_menu_edit_with_text_editor = (By.CSS_SELECTOR, 'div[action="editor"]')
    output_popup = (By.CSS_SELECTOR, '.output-area')
    output_area_close_button = (By.CSS_SELECTOR, '.output-area-close-button')
    output_area_filter_category = (By.CSS_SELECTOR, 'div[data-ibxp-amper-name="PRODUCT_CATEGORY"]')

