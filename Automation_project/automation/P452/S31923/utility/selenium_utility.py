'''
Created on Dec 08, 2019

@author: td13786

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
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pyautogui
from selenium.webdriver.common import keys
from selenium.common import exceptions

class Action():
    L_CLICK = 'click'
    R_CLICK = 'context_click'
    D_CLICK = 'double_click'
    DRAG_DROP = 'drag_and_drop'
    MOVE_TO = 'move_to_element'

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
    def wait_and_act(driver, action_method, element_locator, target_locator=None, index=0, wait_time=30, condition="clickable"):
        element = Selenium_Utility.find_object(driver, element_locator, index, wait_time, condition)
        if (target_locator is not None and action_method == 'drag_and_drop'):
            #target index is always 0. Index argument is created for element locating. 
            target = Selenium_Utility.find_object(driver, target_locator, 0, wait_time, condition)
            getattr(ActionChains(driver), action_method)(element, target).perform()
        else:
            getattr(ActionChains(driver), action_method)(element).perform()
        time.sleep(1)
    
    @staticmethod
    def wait_for_object(driver, obj_locator, index=1, wait_time=30, condition="visible"):
        if index > 1: #when index is not zero, plug index to the xpath
            obj_locator = obj_locator[0], '(' + obj_locator[1] + ")[" + str(index) + ']'
            print(obj_locator)
        if condition == "clickable":
            WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable(obj_locator))
        elif condition == "visible":
            WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located(obj_locator))
        else:
            WebDriverWait(driver, wait_time).until(EC.presence_of_element_located(obj_locator))
            
    @staticmethod
    def wait_for_refresh(driver, obj_locator):
        count = 0
        while (count < 20 and Selenium_Utility.obj_exists(driver, obj_locator)): #if the refresh hourglass is still there, keep waiting
            count += 1
            time.sleep(0.5)      
            
    @staticmethod
    def wait_for_ajax(driver, wait_time=30):
        wait = WebDriverWait(driver, wait_time)
        try:
            wait.until(lambda driver: driver.execute_script('return jQuery.active') == 0)
            wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        except Exception as e:
            print(str(e))        
            
    @staticmethod
    def switch_to_iframe(driver, iframe_locator):
        iframe = Selenium_Utility.find_object(driver, iframe_locator)
        driver.switch_to.frame(iframe)
        
    @staticmethod
    def find_object(driver, obj_locator, index=0, wait_time=30, condition="clickable"):
        Selenium_Utility.wait_for_object(driver, obj_locator, index+1, wait_time, condition)
        return driver.find_elements(*obj_locator)[index]
    
    @staticmethod
    def obj_exists(driver, obj_locator):
        objs_found = driver.find_elements(*obj_locator)
        return len(objs_found) > 0
    
    @staticmethod
    def enter_input(driver, input_locator, input_string):
        input_field = Selenium_Utility.find_object(driver, input_locator)
        input_field.clear()
        ActionChains(driver).click(input_field).send_keys(input_string).perform()
        time.sleep(1)
        return input_field.get_attribute("value")
    
    @staticmethod
    def count_objects(driver, obj_locator, condition='visible'):
        try:
            Selenium_Utility.wait_for_object(driver, obj_locator, condition=condition)
        except TimeoutException:
            pass
        count = len(driver.find_elements(*obj_locator))
        return count
            
    def assert_equal(self, expected, actual, verification_msg, case_id, step):
        tc = unittest.TestCase()
        verification_msg = "Step " + str(step) + " : " +  verification_msg
        msg = verification_msg + ' - FAILED.'
        tc.assertEqual(expected, actual, msg)
        print(verification_msg + ' - PASSED.')
        Selenium_Utility.verification_screenshot_capture(self, case_id, step)
        
    def assert_equal_no_exit_on_error(self, expected, actual, verification_msg, case_id, step):
        tc = unittest.TestCase()
        verification_msg = "Step " + str(step) + " : " +  verification_msg
        try:
            tc.assertEqual(expected, actual)
            print(verification_msg + ' - PASSED.')
        except:
            print(verification_msg + ' - FAILED.')
        Selenium_Utility.verification_screenshot_capture(self, case_id, step)
        
    def assert_true(self, expression, verification_msg, case_id, step):
        tc = unittest.TestCase()
        verification_msg = "Step " + str(step) + " : " +  verification_msg
        msg = verification_msg + ' - FAILED.'
        tc.assertTrue(expression, msg)
        print(verification_msg + ' - PASSED.')
        Selenium_Utility.verification_screenshot_capture(self, case_id, step)
        
    def assert_not_none(self, expression, verification_msg, case_id, step):
        tc = unittest.TestCase()
        verification_msg = "Step " + str(step) + " : " +  verification_msg
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
        Selenium_Utility.wait_for_ajax(self.driver)
        
    def close_window(self):
        self.driver.close()

    def launch_tool(self, tool, tool_mode, master_file):
        '''launch tool via url api call'''
        url_designer = 'http://' + self.node + ':' + self.port + self.context + '/' + tool + '?&master=' + master_file + '&item=IBFS:/WFC/Repository/' + self.project + '_' + self.suite + '/' + self.group + '&tool=' + tool_mode
        self.driver.get(url_designer)   

    def exit_tool(self, tool):
        pass
        
    def edit_saved_fex(self, tool, tool_mode, case_id):
        '''reopen saved fex via url api call'''
        url_designer_report = 'http://' + self.node + ':' + self.port + self.context + '/' + tool + '?item=IBFS:/WFC/Repository/' + self.project + '_' + self.suite + '/' + self.group + '/' + case_id + '.fex&tool=' + tool_mode
        self.driver.get(url_designer_report)   
        
#****workflow case from Paris Home
class ParisHomeUtility():
    
    def __init__(self, driver):
        self.driver = driver
        self.toolLocators = ParisHomeLocators
    
    def select_workspace(self):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.workspaces_button)
        
    def switch_to_workspace_iframe(self):
        Selenium_Utility.switch_to_iframe(self.driver, self.toolLocators.workspaces_iframe)
        
    def refresh_workspace(self):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.refresh_button)
        
    def navigate_to_workspace_folder(self, folder_name):
        folder =  self.toolLocators.create_xpath_locator_with_text(self.toolLocators.tree_folder_xpath_template, folder_name.strip())
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, folder)
        
    def navigate_path(self, folder_path):
        for folder in folder_path:
            folder_locator = self.toolLocators.create_xpath_locator_with_text(self.toolLocators.content_folder_xpath_template, folder.strip())
            Selenium_Utility.wait_and_act(self.driver, Action.D_CLICK, folder_locator, wait_time=10) 
        
    def select_application_button(self):    
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.application_button) 
        
    def run_by_locator(self, locator):
        Selenium_Utility.wait_and_act(self.driver, Action.R_CLICK, locator)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.run_context_button)        
    
    def delete_by_locator(self, locator):
        Selenium_Utility.wait_and_act(self.driver, Action.R_CLICK, locator)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.delete_context_button)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.current_popup_dialog)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.delete_ok_button)
        
    def publish_by_locator(self, locator):
        Selenium_Utility.wait_and_act(self.driver, Action.R_CLICK, locator)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.publish_context_button)
        
    def copy_by_locator(self, locator):
        Selenium_Utility.wait_and_act(self.driver, Action.R_CLICK, locator)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.copy_context_button)
    
    def edit_by_locator(self, locator):
        Selenium_Utility.wait_and_act(self.driver, Action.R_CLICK, locator)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.edit_context_button)
    
    def create_new_portal(self, name):
        portal_folder_locator = self.toolLocators.create_xpath_locator_with_text(self.toolLocators.content_folder_xpath_template, name)
        if Selenium_Utility.obj_exists(self.driver, portal_folder_locator):
            self.delete_portal_folder(name)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.portal_button)
        name_entered = ''
        while(name_entered != name.strip()):
            name_entered = Selenium_Utility.enter_input(self.driver, self.toolLocators.title_in_dialog, name)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.theme_in_dialog)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.light_theme_option_in_dialog)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.create_my_page_checkbox_in_dialog)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.create_button_in_dialog)

    def delete_portal_folder(self, name):
        portal_folder_locator = self.toolLocators.create_xpath_locator_with_text(self.toolLocators.content_folder_xpath_template, name)
        self.delete_by_locator(portal_folder_locator)
        
    def publish_portal_folder(self, name):
        portal_folder_locator = self.toolLocators.create_xpath_locator_with_text(self.toolLocators.content_folder_xpath_template, name)
        self.publish_by_locator(portal_folder_locator)
        Selenium_Utility.wait_and_act(self.driver, Action.R_CLICK, portal_folder_locator)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.open_context_button) 
        
    def create_content(self, action):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.plus_sign_button)    
        menu_option_locator = self.toolLocators.create_xpath_locator_with_text(self.toolLocators.plus_sign_menu_template, action)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, menu_option_locator)
        
    def copy_content(self, content_name):
        content_locator = self.toolLocators.create_xpath_locator_with_text(self.toolLocators.content_file_xpath_template, content_name)
        self.copy_by_locator(content_locator)
        
    def edit_content(self, content_name):
        content_locator = self.toolLocators.create_xpath_locator_with_text(self.toolLocators.content_file_xpath_template, content_name)
        self.edit_by_locator(content_locator)
    
    def delete_content(self, content_name):
        content_locator = self.toolLocators.create_xpath_locator_with_text(self.toolLocators.content_file_xpath_template, content_name)
        self.delete_by_locator(content_locator)
        
    def paste_content(self, content_name):
        content_locator = self.toolLocators.create_xpath_locator_with_text(self.toolLocators.content_file_xpath_template, content_name)
        if Selenium_Utility.obj_exists(self.driver, content_locator):
            self.delete_by_locator(content_locator)
        Selenium_Utility.wait_and_act(self.driver, Action.R_CLICK, self.toolLocators.dropable_area)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.paste_context_button)
    
    def run_content_from_homepage(self, content_path):
        content_locator = self.toolLocators.create_xpath_locator_with_text(self.toolLocators.content_file_xpath_ibfs_path_template, content_path)
        self.run_by_locator(content_locator)
        
    def run_content_from_tree(self, content_name):
        content_folder_locator =  self.toolLocators.create_xpath_locator_with_text(self.toolLocators.tree_folder_xpath_template, content_name.strip())
        self.run_by_locator(content_folder_locator)
        
    def launch_designer(self):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.visualize_data_button)     
        
    def locate_fex(self, fex_name):
        fex_item_locator = self.toolLocators.create_xpath_locator_with_text(self.toolLocators.fex_xpath_template, fex_name)
        try:
            Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, fex_item_locator) 
            return True
        except (NoSuchElementException, TimeoutException):
            return False   
        
class DesignerUtility():
    
    def __init__(self, driver):
        self.driver = driver
        self.toolLocators = DesignerLocators
        
    def change_chart_type(self, chart_type_name):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_chart_type_expand_collapse)
        chart_type_locator = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.designer_chart_type_template, chart_type_name)
        time.sleep(1)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, chart_type_locator)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_chart_type_expand_collapse)
          
    def select_data_source(self, master_name, folder_name, eda_folder_name=None):
        Selenium_Utility.wait_and_act(self.driver, Action.MOVE_TO, self.toolLocators.select_data_source)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.select_data_source)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.data_source_workspace_button)
        folder = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.data_source_workspace_template, folder_name)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, folder)
        eda_folder = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.eda_source_workspace_template, eda_folder_name)
        Selenium_Utility.wait_and_act(self.driver, Action.D_CLICK, eda_folder)
        time.sleep(1)
        Selenium_Utility.enter_input(self.driver, self.toolLocators.data_source_search_input, master_name)
        if eda_folder_name is not None:
            master_name = eda_folder_name+'/'+master_name
        master = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.data_source_master_template, master_name)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, master)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.data_source_select_button)
        
    def get_data_source_title(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.toolLocators.data_source_title))
        return self.driver.find_element(*self.toolLocators.data_source_title).text
            
    def search_for_field(self, field_name):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_search_box)
        Selenium_Utility.enter_input(self.driver, self.toolLocators.designer_search_box, field_name)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_search_button)
        field_node_locator = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.designer_field_name_xpath_template, field_name)
        return field_node_locator
    
    def add_field(self, source_element_locator, target_element_locator=None, drag=False, index=0):
        if drag:
            if target_element_locator:
                Selenium_Utility.wait_and_act(self.driver, Action.DRAG_DROP, source_element_locator, target_element_locator, index=index)
            else:
                raise("Please specify a target element to drop to")
        else:
            Selenium_Utility.wait_and_act(self.driver, Action.D_CLICK, source_element_locator, index=index)
            
    def add_visualization(self):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_add_viz_button)
        time.sleep(1)
        
    def convert_to_page(self):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_convert_to_page_button)
        time.sleep(1)
    
    def select_format_tab(self):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_format_tab_button, index=0)
        
    def select_page_container(self): #by clicking on the header
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_page_header)
        
    def change_page_theme(self, theme_name):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_format_theme)
        theme_option_tuple = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.designer_style_option_xpath_template, theme_name)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, theme_option_tuple)
    
    def select_container(self, name):
        container_tuple = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.designer_container_name_template, name)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, container_tuple)
        
    def delete_container(self, container_num, wait_time=60):
        container_name = "Container " + str(container_num)
        container_tuple = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.designer_container_name_template, container_name)
        Selenium_Utility.wait_for_object(self.driver, self.toolLocators.designer_format_container_content, index=container_num, wait_time=wait_time, condition='visible')        
        Selenium_Utility.wait_and_act(self.driver, Action.R_CLICK, container_tuple)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_container_context_delete)
    
    def change_container_style(self, container_num, style_name):
        if isinstance(container_num, int) :
            container_name = "Container " + str(container_num)
        else:
            container_name = str(container_num)
        self.select_container(container_name)
        sty_option_tuple = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.designer_format_container_style_xpath_template, style_name)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, sty_option_tuple)
    
    def change_container_theme(self, container_num, theme_name):
        Selenium_Utility.wait_and_act(self.driver, Action.MOVE_TO, self.toolLocators.designer_format_container_content, index=container_num, condition='visible')
        Selenium_Utility.wait_for_refresh(self.driver, self.toolLocators.designer_preview_timer)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_format_container_content, index=container_num, condition='visible')
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_format_container_theme)
        theme_option_tuple = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.designer_style_option_xpath_template, theme_name)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, theme_option_tuple)     
    
    def find_element_attribute_value(self, element_locator, attribute_name):
        element = Selenium_Utility.find_object(self.driver, element_locator)
        if element.get_attribute(attribute_name) is not None:
            return element.get_attribute(attribute_name)
        else:
            return element.value_of_css_property(attribute_name)
        
    def locate_container(self, x, y):
        xpath_tuple = self.toolLocators.create_container_xpath_with_coordinate(x, y, self.toolLocators.designer_container_coordinate_template)  
        return self.driver.find_element(*xpath_tuple)
    
    def set_attribute(self, web_element, attr, val):
        self.driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])", web_element, attr, val)
    
    def move_container(self, container, x, y):
        self.set_attribute(container, 'data-gs-x', x)
        self.set_attribute(container, 'data-gs-y', y)

    def resize_container(self, container, width=0, height=0):
        if width:
            self.set_attribute(container, 'data-gs-width', width)
        if height:
            self.set_attribute(container, 'data-gs-height', height)
    
    def press_save_button(self):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_save_button)
    
    def save_chart(self, name):
        try:
            #if save dialog doesn't come up (a fex has been created), go to except and do nothing
            Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_save_dialog, wait_time=2)
            Selenium_Utility.enter_input(self.driver, self.toolLocators.save_file_title, name)
            Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_popup_ok_btn)
            #If item exists, click ok to overwrite. Else, go to except and do nothing
            Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_popup_ok_btn, index=1)
        except (NoSuchElementException, TimeoutException) as e: 
            return 
    
    def save_with_navigation(self, name, path):
        try:
            #if save dialog doesn't come up (a fex has been created), go to except and do nothing
            Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_save_dialog, wait_time=2)
            workspaces_breadcrumb = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.designer_save_dialog_breadcrumb_template, "Workspaces")
            Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, workspaces_breadcrumb)
            for folder in path:
                folder_lable = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.designer_save_dialog_folder_template, folder)
                Selenium_Utility.wait_and_act(self.driver, Action.D_CLICK, folder_lable)
            Selenium_Utility.enter_input(self.driver, self.toolLocators.save_file_title, name)
            Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_popup_ok_btn)
            #If item exists, click ok to overwrite. Else, go to except and do nothing
            Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_popup_ok_btn, index=1)
        except (NoSuchElementException, TimeoutException) as e: 
            return         
        
    def open_logo_menu(self):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_logo_button)   
    
    def select_save_as_menu_item(self):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_save_as_menu_option)
        
    def select_close(self):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_close_menu_option)

    def choose_template_by_name(self, template_name):
        template_locator = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.designer_template_option_xpath_template, template_name)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, template_locator)
        Selenium_Utility.wait_for_ajax(self.driver)
        
    def navigate_content_folders_up(self, folders):
        for folder_name in folders:
            folder_locator = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.designer_folder_nav_xpath_template, folder_name)
            Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, folder_locator)
    
    def navigate_content_folders_down(self, folders):
        for folder_name in folders:
            folder_locator = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.designer_content_nav_xpath_template, folder_name)
            Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, folder_locator)
    
    def add_content_to_container(self, content_name, container_name):
        content_locator = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.designer_content_nav_xpath_template, content_name)
        container_locator = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.designer_content_container_xpath_template, container_name)
        Selenium_Utility.wait_and_act(self.driver, Action.DRAG_DROP, content_locator, container_locator)    
        Selenium_Utility.wait_for_ajax(self.driver)
        
    def auto_create_filters(self):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.designer_filter_button)
        Selenium_Utility.wait_for_ajax(self.driver)
        
    def get_filter_dropdown_count(self):
        Selenium_Utility.wait_for_object(self.driver, self.toolLocators.designer_filter_grid, condition='visible')
        count = Selenium_Utility.count_objects(self.driver, self.toolLocators.designer_filter_dropdown, condition='presence')
        return count        
        
    
class PortalRuntimeUtility():
    
    def __init__(self, driver):
        self.driver = driver
        self.toolLocators = PortalRuntimeLocators
        
    def click_page(self, page_name, wait_time=45):
        page_locator = ParisHomeLocators.create_xpath_locator_with_text(self.toolLocators.page_name_xpath_template, page_name)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, page_locator)
        Selenium_Utility.wait_for_ajax(self.driver, wait_time)
        
    def get_chart_container_count(self, first_container_id=0):
        Selenium_Utility.wait_for_object(self.driver, self.toolLocators.page_container, index=first_container_id, wait_time=45, condition='visible')
        count = Selenium_Utility.count_objects(self.driver, self.toolLocators.page_container, condition='presence')
        Selenium_Utility.wait_for_object(self.driver, self.toolLocators.page_container_content, index=count, wait_time=45, condition='visible')
        return count
    
    def add_portal_page(self, page_name, page_path):
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.page_add_plus_sign) 
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, self.toolLocators.link_to_exiting_page)
        workspaces_breadcrumb = ParisHomeLocators.create_xpath_locator_with_text(DialogLocators.folder_breadcrumb_template, "Workspaces")
        Selenium_Utility.wait_and_act(self.driver, Action.D_CLICK, workspaces_breadcrumb)
        for folder in page_path:
            folder_lable = ParisHomeLocators.create_xpath_locator_with_text(DialogLocators.folder_template, folder)
            Selenium_Utility.wait_and_act(self.driver, Action.D_CLICK, folder_lable) 
        page_locator = ParisHomeLocators.create_xpath_locator_with_text(DialogLocators.dialog_item_template, page_name)
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, page_locator)    
        Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, DialogLocators.ok_btn, index=1)
        # to handle pop-up "portal already added" to make reruns possible
        if Selenium_Utility.obj_exists(self.driver, DialogLocators.ok_btn):
            Selenium_Utility.wait_and_act(self.driver, Action.L_CLICK, DialogLocators.ok_btn)
            
        