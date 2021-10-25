'''
Created on Apr 08, 2019

@author: ml12793

@descrpition: selenium common library for smoke test
'''

import unittest
import re
import time
import sys
from utility.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from selenium.webdriver.common import keys
from selenium.common import exceptions

class Action():
    L_CLICK = 'click'
    R_CLICK = 'context_click'

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
        self.driver.get(setup_url)

    def logout_wf(self):
        setup_url = Selenium_Utility.get_setup_url(self)
        self.driver.get('' + setup_url + 'service/wf_security_logout.jsp')
    
    @staticmethod    
    def wait_and_act(driver, action_method, element_locator):
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(element_locator))
        element = driver.find_element(*element_locator)
        getattr(ActionChains(driver), action_method)(element).perform()
        time.sleep(1)
        
    def check_view_mode(self):
        '''make sure list view is selected'''
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.view_button))          
        list_view_style = self.driver.execute_script('return $(\'.btn-how-view-grid\').attr(\'style\')')
        if list_view_style == 'display: none;':  #handles situation when grid view is selected
            self.driver.find_element(*HomePageLocators.view_button).click()
            
    def navigate_to_case_folder(self):
        '''navigate to specific folder in new home page'''
        folder = self.project + '_' + self.suite 
        subfolder = self.group
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(HomePageLocators.panel_content_button))
        self.driver.find_element(*HomePageLocators.panel_content_button).click()
        time.sleep(2)
        self.driver.execute_script('$(\'.home-tree-node:contains("Workspaces")\').click()')
        Selenium_Utility.check_view_mode(self)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(HomePageLocators.folder))     
        self.driver.execute_script('$(\'.folder-item:contains("' + folder + '")\').dblclick();') 
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.folder))       
        self.driver.execute_script('$(\'.folder-image-text:contains("' + subfolder + '")\').dblclick();')
                    
    def click_home_tree_folder(self, folder):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(HomePageLocators.panel_content_button))
        self.driver.find_element(*HomePageLocators.panel_content_button).click()
        domain_button = self.driver.find_element(*HomePageLocators.domain_button)
        domain_button.click()    
        domain_folder_css = 'div[data-ibfs-path="IBFS:/WFC/Repository/' + folder.replace(' ', '_') + '"] .ibx-label-text'
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, domain_folder_css)))        
        self.driver.find_element(By.CSS_SELECTOR, domain_folder_css).click()
    
    def assert_equal(self, expected, actual, verification_msg, case_id, step):
        tc = unittest.TestCase()
        msg = verification_msg + ' - FAILED.'
        tc.assertEqual(expected, actual, msg)
        print(verification_msg + ' - PASSED.')
        Selenium_Utility.verification_screenshot_capture(self, case_id, step)
        
    def assert_equal_no_exit_on_error(self, expected, actual, verification_msg, case_id, step):
        tc = unittest.TestCase()
        try:
            tc.assertEqual(expected, actual)
            print(verification_msg + ' - PASSED.')
        except:
            print(verification_msg + ' - FAILED.')
        Selenium_Utility.verification_screenshot_capture(self, case_id, step)
        
    def assert_true(self, expression, verification_msg, case_id, step):
        tc = unittest.TestCase()
        msg = verification_msg + ' - FAILED.'
        tc.assertTrue(expression, msg)
        print(verification_msg + ' - PASSED.')
        Selenium_Utility.verification_screenshot_capture(self, case_id, step)
        
    def assert_not_none(self, expression, verification_msg, case_id, step):
        tc = unittest.TestCase()
        msg = verification_msg + ' - FAILED.'
        tc.assertIsNotNone(expression, msg)
        print(verification_msg + ' - PASSED.')
        Selenium_Utility.verification_screenshot_capture(self, case_id, step)    
        
    def verification_screenshot_capture(self, case_id, step):
        try:
            self.driver.save_screenshot(case_id + '_' + step + '.png')
        except:
            print('Exception in save screenshot of verification step ' + step)    
            
    def switch_to_window(self, window_number):
        windows = self.driver.window_handles
        accumulate_wait = 0
        while len(windows) != window_number and accumulate_wait < 20:
            time.sleep(1)
            accumulate_wait += 1
            windows = self.driver.window_handles  
        if accumulate_wait < 20:    
            self.driver.switch_to.window(windows[window_number - 1]) 
        else:
            raise TimeoutError
        
    def launch_tool(self, tool, tool_mode, master_file):
        '''launch tool via url api call'''
        url_designer = 'http://' + self.node + ':' + self.port + self.context + '/' + tool + '?&master=' + master_file + '&item=IBFS:/WFC/Repository/' + self.project + '_' + self.suite + '/' + self.group + '&tool=' + tool_mode
        self.driver.get(url_designer)   
        
    def double_click_to_add_field(self, tool, field):
        '''double click to add field'''
        if tool == 'designer':
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(DesignerLocators.demension_tree_box))
            self.driver.execute_script('$(\'.ibx-label-text:contains("' + field + '")\').dblclick();')  
        if tool == 'ia':
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(IALocators.metadata_browser))
            field_to_click = self.driver.execute_script('return $(\'#iaMetaDataBrowser td:contains("' + field + '") img.icon\');')[0] 
            ActionChains(self.driver).move_to_element(field_to_click).double_click().perform()
    
    def verify_preview_designer_report_default(self, case_id, step):
        '''verify preview default view'''
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(DesignerLocators.preview_report_default))
        time.sleep(10)
        expected_preview_string = 'Drag and drop fields onto the canvas or into the query pane to begin building your report.'
        actual_preview_string = self.driver.find_element(*DesignerLocators.preview_report_default).text.replace('\n', ' ')
        Selenium_Utility.assert_equal(self, expected_preview_string, actual_preview_string, 'Step ' + step + ': Verify default preview.', case_id, step)
            
    def verify_preview_designer_report(self, expected_preview, case_id, step):
        '''verify preview content'''
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(DesignerLocators.preview_report_title))
        actual_preview_title = [title.text for title in self.driver.find_elements(*DesignerLocators.preview_report_title)]
        actual_preview_data = [data.text for data in self.driver.find_elements(*DesignerLocators.preview_report_data)]
        actual_preview = actual_preview_title + actual_preview_data       
        Selenium_Utility.assert_equal(self, expected_preview, actual_preview, 'Step ' + step + ': Verify table preview.', case_id, step)
                
    def save_fex_as(self, tool, case_id):
        '''click save button to bring up save dialog to save fex'''
        if tool == 'designer':
            toolLocators = DesignerLocators
            self.driver.find_element(*toolLocators.save_button).click()
        if tool == 'ia':
            toolLocators = IALocators 
            self.driver.find_element(*toolLocators.save_button).click()
        if tool == 'text editor':
            toolLocators = TextEditorLocators     
            self.driver.find_element(*toolLocators.main_menu_button).click()
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(toolLocators.main_menu_save_as))
            self.driver.find_element(*toolLocators.main_menu_save_as).click()
        if tool == 'page designer':
            toolLocators = DesignerLocators
            self.driver.find_element(*toolLocators.page_designer_main_menu).click()
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(toolLocators.page_designer_main_menu_close))
            self.driver.find_element(*toolLocators.page_designer_main_menu_close).click()
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(toolLocators.page_designer_warning_dialog_yes))
            #self.driver.find_element(*toolLocators.page_designer_warning_dialog_yes).click()   
            self.driver.execute_script('$(\'.pd-warning-dirty-yes\').click()')                     
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(toolLocators.save_dialog_input_title))
        self.driver.find_element(*toolLocators.save_dialog_input_title).clear()
        self.driver.find_element(*toolLocators.save_dialog_input_title).send_keys(case_id)
        self.driver.find_element(*toolLocators.save_dialog_save_button).click()
        time.sleep(5)

    def exit_tool(self, tool):
        '''click close in main menu to exit designer'''
        if tool == 'text editor':
            main_menu_button_css = TextEditorLocators.main_menu_button
            main_menu_exit_css = TextEditorLocators.main_menu_exit
        if tool == 'designer':
            main_menu_button_css = DesignerLocators.main_menu_button
            main_menu_exit_css = DesignerLocators.main_menu_close
        self.driver.find_element(*main_menu_button_css).click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(main_menu_exit_css))
        self.driver.find_element(*main_menu_exit_css).click() 
        Selenium_Utility.switch_to_window(self, 1)
        time.sleep(5)
        
    def edit_saved_fex(self, tool, tool_mode, case_id):
        '''reopen saved fex via url api call'''
        url_designer_report = 'http://' + self.node + ':' + self.port + self.context + '/' + tool + '?item=IBFS:/WFC/Repository/' + self.project + '_' + self.suite + '/' + self.group + '/' + case_id + '.fex&tool=' + tool_mode
        self.driver.get(url_designer_report)   
        
#****workflow case from Paris Home
class ParisHomeUtility():
    
    def __init__(self, driver):
        self.driver = driver
        self.toolLocators = ParisHomeLocators
    
    def navigate_to_workspace_folder(self, folder_name):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.workspaces_button)
        workspaces_iframe = self.driver.find_element(*self.toolLocators.workspaces_iframe)
        self.driver.switch_to.frame(workspaces_iframe)
        retail_samples_folder =  self.toolLocators.create_xpath_locator_with_text(self.toolLocators.tree_folder_xpath_template, folder_name)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, retail_samples_folder)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.application_button) 
    
    def create_new_portal(self, name):
        portal_folder_locator = self.toolLocators.create_xpath_locator_with_text(self.toolLocators.content_folder_xpath_template, name)
        if len(self.driver.find_elements(*portal_folder_locator)):
            self.delete_portal_folder(name)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.portal_button)
        portal_title = self.driver.find_element(*self.toolLocators.title_in_dialog)
        portal_title.send_keys(name)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.theme_in_dialog)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.light_theme_option_in_dialog)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.create_my_page_checkbox_in_dialog)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.create_button_in_dialog)

    def delete_portal_folder(self, name):
        portal_folder_locator = self.toolLocators.create_xpath_locator_with_text(self.toolLocators.content_folder_xpath_template, name)
        Selenium_Utility.wait_and_act(self.driver, Action.R_CLICK, portal_folder_locator)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.delete_context_button)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.current_popup_dialog)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.delete_ok_button)
        
    def publish_portal_folder(self, name):
        portal_folder_locator = self.toolLocators.create_xpath_locator_with_text(self.toolLocators.content_folder_xpath_template, name)
        Selenium_Utility.wait_and_act(self.driver, Action.R_CLICK, portal_folder_locator)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.publish_context_button)
        Selenium_Utility.wait_and_act(self.driver, Action.R_CLICK, portal_folder_locator)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.open_context_button)
        
    def launch_designer(self):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.visualize_data_button)        
      
        
class DesignerUtility():
    
    def __init__(self, driver):
        self.driver = driver
        self.toolLocators = DesignerLocators
          
    def select_data_source(self, master_name):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.add_data_button)
        
        
        
        
        
        
        
        
        
        
        