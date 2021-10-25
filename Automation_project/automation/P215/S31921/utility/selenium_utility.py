'''
Created on July 10th, 2019

@author: ml12793

@descrpition: selenium common library for smoke test
'''

import unittest
import re
import time
from utility.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Selenium_Utility(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.node = Selenium_Utility.parseinitfile(self, 'nodeid')
        self.port = Selenium_Utility.parseinitfile(self, 'httpport')
        self.context = Selenium_Utility.parseinitfile(self, 'wfcontext')
        self.project = Selenium_Utility.parseinitfile(self, 'project_id')
        self.suite = Selenium_Utility.parseinitfile(self, 'suite_id')
        self.group = Selenium_Utility.parseinitfile(self, 'group_id')

    def parseinitfile(self, key):
        init_file = 'config.init'
        config_pair = {}
        try:
            fileObj = open(init_file, "r")
            line = fileObj.readline()
            while line:
                lineObjbj = re.match(r'(\S*)\s(.*)', line)
                keyName = lineObjbj.group(1)
                config_pair[keyName] = lineObjbj.group(2)
                line = fileObj.readline()
            fileObj.close()
        except IOError:
            exit()
        if key in config_pair:
            return (config_pair[key])
        else:
            return ('Key not found')
        
    def get_setup_url(self):
        setup_url = 'http://' + self.node + ':' + self.port + self.context + '/'
        return(setup_url)    
    
    def login_wf(self):
        setup_url = Selenium_Utility.get_setup_url(self)
        uid = Selenium_Utility.parseinitfile(self, 'mrid')
        pwd = Selenium_Utility.parseinitfile(self, 'mrpass')
        self.driver.get(setup_url)
        response_text= self.driver.find_element_by_css_selector("body").text
        if "refused to connect" in response_text:
            raise EnvironmentError('Unable to connect ' + setup_url)       
        username = self.driver.find_element(*LoginPageLocators.uid)
        username.click()
        username.send_keys(uid)
        password = self.driver.find_element(*LoginPageLocators.pwd)
        password.click()
        password.send_keys(pwd)
        time.sleep(1)
        sign_in = self.driver.find_element(*LoginPageLocators.submit)
        sign_in.click()
        time.sleep(15)
        
    def go_to_paris_home_page(self):
        paris_url = Selenium_Utility.get_setup_url(self) + 'paris'
        self.driver.get(paris_url)
        
    def verify_banner_link_menus(self, expected_tooltips, case_id, step):
#         menus = [menu for menu in self.driver.find_elements(*ParisHomePageLocators.banner_link_menus)]
#         print(menus)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(ParisHomePageLocators.banner_link_menus)) 
        tooltips = self.driver.execute_script('var titles=[];menus = $(\'div[data-ibx-type="homeMenus"] div[role="button"]\');for (i=0;i<menus.length;i++){titles[i] = menus[i].title}; return titles;')
        Selenium_Utility.assert_equal(self, expected_tooltips, tooltips, 'Step ' + step + ': Verify banner link tooltips.', case_id, step)
        
    def logout_wf(self):
        setup_url = Selenium_Utility.get_setup_url(self)
        self.driver.get('' + setup_url + 'service/wf_security_logout.jsp')
        
    def assert_equal(self, expected, actual, verification_msg, case_id, step):
        tc = unittest.TestCase()
        msg = verification_msg + ' - FAILED.'
        tc.assertEqual(expected, actual, msg)
        print(verification_msg + ' - PASSED.')
        Selenium_Utility.verification_screenshot_capture(self, case_id, step)

    def assert_true(self, expression, verification_msg, case_id, step):
        tc = unittest.TestCase()
        msg = verification_msg + ' - FAILED.'
        tc.assertTrue(expression, msg)
        print(verification_msg + ' - PASSED.')
        Selenium_Utility.verification_screenshot_capture(self, case_id, step)
        
    def verification_screenshot_capture(self, case_id, step):
        try:
            self.driver.save_screenshot(case_id + '_' + step + '.png')
        except:
            print('Exception in save screenshot of verification step ' + step)          
        
    def click_tab_button(self, tab):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ParisHomePageLocators.tab_buttons)) 
        self.driver.execute_script('$(\'.ibx-tab-button:contains("' + tab + '")\').click();')
        
    def navigate_domain_folders(self, folder_path):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ParisHomePageLocators.home_domains_breadcrumb_items)) 
        self.driver.execute_script('$(\'.home-domains-breadcrumb-item:contains("Domains")\').click();')
        time.sleep(2)
        folders = folder_path.split('->')
        for folder in folders:
            self.driver.execute_script('$(\'.home-content-page-folder:contains("' + folder + '")\').dblclick()')
            time.sleep(2)
         
    def right_click_item_to_perform(self, item, action):
        if action == 'Run':
            action_css_locator = ParisHomePageLocators.right_click_menu_run        
        if action == 'Add to Favorites':
            action_css_locator = ParisHomePageLocators.right_click_menu_favorites
        ac = ActionChains(self.driver)
        ac.move_to_element(self.driver.execute_script('return $(\'.domains-item-div .ibx-label-text:contains("' + item + '")\')[0];')).context_click().perform()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(action_css_locator)) 
        self.driver.find_element(*action_css_locator).click()
        time.sleep(10)
        
    def close_report(self):
        self.driver.execute_script('$(\'.output-area-close-button\').click();')
        time.sleep(3)
    
    def verify_report_added(self, item, case_id, step):
        time.sleep(5)
        recent_items = self.driver.execute_script('var items=[];labels = $(\'div[data-ibx-type="homeRecent"] .ibx-csl-items-box .test-item .ibx-label-text\');for(i=0;i<labels.length;i++) items[i]=$(labels[i]).text();return items;')
        Selenium_Utility.assert_true(self, item in recent_items, 'Step ' + step + '.1: Verify report is added to Recent.', case_id, step)
        favorites_items = self.driver.execute_script('var items=[];labels = $(\'div[data-ibx-type="homeFavorites"] .ibx-csl-items-box .test-item .ibx-label-text\');for(i=0;i<labels.length;i++) items[i]=$(labels[i]).text();return items;')
        Selenium_Utility.assert_true(self, item in favorites_items, 'Step ' + step + '.2: Verify report is added to Favorites.', case_id, step)
