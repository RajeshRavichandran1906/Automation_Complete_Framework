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
        self.driver.get(setup_url + 'home8206')
        time.sleep(15)

    def logout_wf(self):
        setup_url = Selenium_Utility.get_setup_url(self)
        self.driver.get('' + setup_url + 'service/wf_security_logout.jsp')
        
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

    def verify_preview_ia_visualization_default(self, case_id, step):
        '''verify preview default view'''
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(IALocators.preview_visualization_default_string))
        expected_preview_string = 'Drop Measures or Sorts into the Query Pane'
        actual_preview_string = self.driver.find_element(*IALocators.preview_visualization_default_string).text
        Selenium_Utility.assert_equal(self, expected_preview_string, actual_preview_string, 'Step ' + step + '.1: Verify default preview string.', case_id, step + '.1')
        #verify risers:
        expected_riser_types = 3
        actual_riser_types =  len(self.driver.execute_script('return $(\'#TableChart_1 g.risers\').children();')) 
        Selenium_Utility.assert_equal(self, expected_riser_types, actual_riser_types, 'Step ' + step + '.2: Verify default preview riser types.', case_id, step + '.2')
        expected_riser_numbers = 12
        actual_riser_numbers =  len(self.driver.execute_script('return $(\'#TableChart_1 g.risers rect\');')) 
        Selenium_Utility.assert_equal(self, expected_riser_numbers, actual_riser_numbers, 'Step ' + step + '.3: Verify default preview riser numbers.', case_id, step + '.3') 
        
    def verify_preview_ia_visualization(self, expected_preview_xaxix_title, expected_preview_xaxis_labels, expected_preview_yaxis_title, expected_preview_yaxis_labels, expected_preview_risers, expected_preview_risers_color, case_id, step):
        '''verify IA visualization preview'''
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(IALocators.preview_visualization_yaxis_title))        
        #verify x axis title
        actual_preview_xaxis_title = self.driver.find_element(*IALocators.preview_visualization_xaxis_title).text
        Selenium_Utility.assert_equal(self, expected_preview_xaxix_title, actual_preview_xaxis_title, 'Step ' + step + '.1: Verify IA visualization preview x axis title.', case_id, step + '.1')   
        #verify x axis labels
        actual_preview_xaxis_labels = [label.text for label in self.driver.find_elements(*IALocators.preview_visualization_xaxis_labels)]
        Selenium_Utility.assert_equal(self, expected_preview_xaxis_labels, actual_preview_xaxis_labels, 'Step ' + step + '.2: Verify IA visualization preview x axis labels.', case_id, step + '.2')
        #verify y axis title
        actual_preview_yaxis_title = self.driver.find_element(*IALocators.preview_visualization_yaxis_title).text
        Selenium_Utility.assert_equal(self, expected_preview_yaxis_title, actual_preview_yaxis_title, 'Step ' + step + '.3: Verify IA visualization preview y axis title.', case_id, step + '.3')   
        #verify y axis labels
        actual_preview_yaxis_labels = [label.text for label in self.driver.find_elements(*IALocators.preview_visualization_yaxis_labels)]
        Selenium_Utility.assert_equal(self, expected_preview_yaxis_labels, actual_preview_yaxis_labels, 'Step ' + step + '.4: Verify IA visualization preview y axis labels.', case_id, step + '.4')
        #verify risers number and color
        actual_preview_risers = len(self.driver.find_elements(*IALocators.preview_visualization_risers))
        Selenium_Utility.assert_equal(self, expected_preview_risers, actual_preview_risers, 'Step ' + step + '.5: Verify IA visualization preview total number of risers.', case_id, step + '.5')
        actual_preview_risers_color = len(self.driver.find_elements(By.CSS_SELECTOR, '.chartPanel rect[fill="' + expected_preview_risers_color + '"]'))
        Selenium_Utility.assert_equal(self, expected_preview_risers, actual_preview_risers_color, 'Step ' + step + '.6: Verify IA visualization preview risers color.', case_id, step + '.6')
   
    def launch_text_editor_to_type_fex(self):
        '''launch text editor from home page to create fex'''
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(HomePageLocators.other_tab))
        self.driver.find_element(*HomePageLocators.other_tab).click() 
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(HomePageLocators.text_editor_button))
        self.driver.find_element(*HomePageLocators.text_editor_button).click() 
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(HomePageLocators.fex_button))
        #self.driver.find_element(*HomePageLocators.fex_button).click() 
        self.driver.execute_script('$(\'div[data-ibxp-user-value="fex"]\').click()')
        Selenium_Utility.switch_to_window(self, 2)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(TextEditorLocators.ace_text_input))
        fexObj = open('./data/fex.data', 'r')
        line = fexObj.readline()
        while line:
            ac = ActionChains(self.driver)
            ac.send_keys_to_element(self.driver.find_element(*TextEditorLocators.ace_text_input_line), line).perform()
            line = fexObj.readline()
        fexObj.close()
        time.sleep(5)
        
    def right_click_item_to_perform(self, item_type, action, item_name=None):
        '''right click fex on home page to perform actions'''
        if action == 'run':
            action_css_locator = HomePageLocators.right_click_menu_run
        if action == 'edit':
            action_css_locator = HomePageLocators.right_click_menu_edit
        if action == 'copy':
            action_css_locator = HomePageLocators.right_click_menu_copy
        if action == 'paste':
            action_css_locator = HomePageLocators.right_click_menu_paste 
        if action == 'publish': 
            action_css_locator = HomePageLocators.right_click_menu_publish
        if action == 'run in new window':
            action_css_locator = HomePageLocators.right_click_menu_run_in_new_window
        if action == 'run as -> run in new window':
            action_css_locator = HomePageLocators.right_click_menu_run_as
        if action == 'edit with text editor':
            action_css_locator = HomePageLocators.right_click_menu_edit_with_text_editor
                    
        if item_type == 'files-box':
            script_to_execute = 'return $(\'.' + item_type + '\')[0];'
        else:
            script_to_execute = 'return $(\'.' + item_type + ' .ibx-label-text:contains("' + item_name + '")\')[0];'   
        ac = ActionChains(self.driver)
        ac.move_to_element(self.driver.execute_script(script_to_execute)).context_click().perform()
        if action == 'run as -> run in new window':
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(action_css_locator))
            self.driver.find_element(*action_css_locator).click()         
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.right_click_menu_run_in_new_window))
            self.driver.find_element(*HomePageLocators.right_click_menu_run_in_new_window).click()                     
        else:   
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(action_css_locator))
            self.driver.find_element(*action_css_locator).click()         
    
    def verify_table(self, case_id, step):
        '''verify table in output'''
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(HomePageLocators.output_popup))
        time.sleep(5)
        report_table = self.driver.execute_script('var iframe = $(\'div.output-area-frame>iframe\')[0];var table = iframe.contentWindow.document.getElementsByClassName(\'gridB\')[0];return table.innerHTML;')
        expected_table = ''
        fileObj = open('./data/table.data', 'r')
        line = fileObj.readline()
        while line:
            expected_table += line
            line = fileObj.readline()
        fileObj.close()
        Selenium_Utility.assert_equal(self, expected_table, report_table, 'Step ' + step + ': Verify output report table.', case_id, step)
        self.driver.find_element(*HomePageLocators.output_area_close_button).click() 
        time.sleep(5)
        
    def verify_fex(self, case_id, step):
        '''verify fex display as expected in text editor'''
        Selenium_Utility.switch_to_window(self, 2)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(TextEditorLocators.ace_text_input))
        attempt = 0
        while(attempt < 10):
            try:
                actual_fex_lines = [line.text for line in self.driver.find_elements(*TextEditorLocators.ace_text_input)]
                break
            except exceptions.StaleElementReferenceException:
                attempt += 1 
                time.sleep(1)   
        expected_fex_lines = []
        fileObj = open('./data/fex.data', 'r')
        line = fileObj.readline()
        while line:
            expected_fex_lines.append(line.replace('\n', ''))
            line = fileObj.readline()
        fileObj.close()        
        Selenium_Utility.assert_equal(self, expected_fex_lines, actual_fex_lines, 'Step ' + step + ': Verify text editor opens and fex displays correctly.', case_id, step)

    def launch_designer_by_clicking(self, tab, tool):
        '''launch designer by clicking designer button under tab'''
        if tab == 'Common':
            tab_button_css = HomePageLocators.common_tab
        if tab == 'Designer':
            tab_button_css = HomePageLocators.designer_tab
        
        if tool == 'page designer':
            tool_button_css = HomePageLocators.page_button
        if tool == 'portal designer':           
            tool_button_css = HomePageLocators.portal_button 
        if tool == 'chart designer':
            tool_button_css = HomePageLocators.chart_button 
        if tool == 'report designer':
            tool_button_css = HomePageLocators.report_button 

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(tab_button_css))
        self.driver.find_element(*tab_button_css).click() 
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(tool_button_css))
        self.driver.find_element(*tool_button_css).click() 
        if tool == 'page designer':
            Selenium_Utility.switch_to_window(self, 2)

    def verify_new_page_dialog(self, expected_new_page_dialog_title, expected_new_page_dialog_open_existing_text, expected_new_page_dialog_select_template_text, expected_new_page_dialog_template_items_label, case_id, step):
        '''verify New Page dialog'''
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(DesignerLocators.new_page_dialog))
        #verify new page dialog title
        actual_new_page_dialog_title = self.driver.find_element(*DesignerLocators.new_page_dialog_title).text
        Selenium_Utility.assert_equal(self, expected_new_page_dialog_title, actual_new_page_dialog_title, 'Step ' + step + '.1: Verify Page Template dialog title.', case_id, step + '.1')
        #verify new page dialog open existing page button text
        actual_new_page_dialog_open_existing_text = self.driver.find_element(*DesignerLocators.new_page_dialog_open_existing).text
        Selenium_Utility.assert_equal(self, expected_new_page_dialog_open_existing_text, actual_new_page_dialog_open_existing_text, 'Step ' + step + '.2: Verify Page Template dialog open existing page button text.', case_id, step + '.2')
        #verify new page dialog select template text
        actual_new_page_dialog_select_template_text = self.driver.find_element(*DesignerLocators.new_page_dialog_select_template).text
        Selenium_Utility.assert_equal(self, expected_new_page_dialog_select_template_text, actual_new_page_dialog_select_template_text, 'Step ' + step + '.3: Verify Page Template dialog select template text.', case_id, step + '.3')
        #verify new page dialog template items label
        actual_new_page_dialog_template_items_label = [label.text for label in self.driver.find_elements(*DesignerLocators.new_page_dialog_template_item)]
        Selenium_Utility.assert_equal(self, expected_new_page_dialog_template_items_label, actual_new_page_dialog_template_items_label, 'Step ' + step + '.4: Verify Page Template dialog template items label.', case_id, step + '.4')
        
    def select_page_template(self, template): 
        '''select page template'''  
        if template == 'Blank':
            template_css_locator = DesignerLocators.new_page_dialog_template_item_blank
        self.driver.find_element(*template_css_locator).click() 

    def navigate_pd_tree(self, folder, path):
        '''navigate to the folder where fex is located'''
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(DesignerLocators.page_designer_tree_node)) 
        self.driver.execute_script('$(\'.tnode-has-parent .ibx-label-text:contains("' + folder + '")\').click();')
        folders = path.split('->')
        for folder in folders:
            time.sleep(2)
            self.driver.execute_script('$(\'.tnode-children .ibx-label-text:contains("' + folder + '")\').click();')

    def drag_and_drop_to_canvas(self, element):
        '''drag and drop fex to canvas'''
        time.sleep(3) 
        source_element = self.driver.execute_script('return $(\'.ibx-label-text:contains("' + element + '")\')[0]')
        ac = ActionChains(self.driver)
        ac.drag_and_drop(source_element, self.driver.find_element(*DesignerLocators.page_designer_grid_box)).perform()    
        
    def verify_quick_filter_button(self, case_id, step): 
        '''verify quick filter displays with correct number of filters'''   
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(DesignerLocators.page_designer_quick_filter)) 
        quick_filter_class = self.driver.execute_script('return $(\'div[title="Quick filter"]\').attr("class");')
        Selenium_Utility.assert_true(self, 'pd_filter_6' in quick_filter_class, 'Step ' + step + '.1: Verify correct number appears on quick filter button.', case_id, step + '.1')
        Selenium_Utility.assert_true(self, 'pd_filter_x' in quick_filter_class, 'Step ' + step + '.2: Verify number on quick filter button in red.', case_id, step + '.2')

    def click_and_verify_filter_bar(self, expected_number, case_id, step):
        '''verify filter bar appears with correct number of controls'''
        self.driver.find_element(*DesignerLocators.page_designer_quick_filter).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(DesignerLocators.page_designer_filter_bar)) 
        filter_bar_controls = self.driver.find_elements(*DesignerLocators.page_designer_filter_bar_control)
        filter_bar_controls_total_number = len(filter_bar_controls)
        Selenium_Utility.assert_equal(self, expected_number, filter_bar_controls_total_number, 'Step ' + step + ': Verify number of controls appears in the filter bar.', case_id, step)
        
    def click_preview_and_verify_in_run_mode(self, case_id, step):
        '''click preview button and verify page converted to run mode'''
        self.driver.find_element(*DesignerLocators.page_designer_preview).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(DesignerLocators.page_designer_preview_floating_button)) 
        pd_toolbar_style = self.driver.execute_script('return $(\'.pd-toolbar\').attr("style");')
        pd_left_pane_style = self.driver.execute_script('return $(\'.pd-left-pane\').attr("style");')
        Selenium_Utility.assert_true(self, 'margin-top: -50px' in pd_toolbar_style, 'Step ' + step + '.1: Verify toolbar offset to top by it\'s height.', case_id, step + '.1')
        Selenium_Utility.assert_true(self, 'opacity: 0' in pd_toolbar_style, 'Step ' + step + '.2: Verify toolbar set to transparent.', case_id, step + '.2')
        Selenium_Utility.assert_true(self, 'margin-left: -200px' in pd_left_pane_style, 'Step ' + step + '.3: Verify left pane offset to left by it\'s width.', case_id, step + '.3')
        Selenium_Utility.assert_true(self, 'opacity: 0' in pd_toolbar_style, 'Step ' + step + '.4: Verify left pane set to transparent.', case_id, step + '.4')

    def exit_preview_and_verify_in_design_mode(self, case_id, step):
        '''click preview floating button to exit and verity page back to design mode'''
        self.driver.execute_script('$(\'.pd-preview-button\').click();')    
        time.sleep(3)
        pd_toolbar_style = self.driver.execute_script('return $(\'.pd-toolbar\').attr("style");')
        pd_left_pane_style = self.driver.execute_script('return $(\'.pd-left-pane\').attr("style");')
        Selenium_Utility.assert_true(self, 'margin-top: 0px' in pd_toolbar_style, 'Step ' + step + '.1: Verify toolbar offset to top by 0px.', case_id, step + '.1')
        Selenium_Utility.assert_true(self, 'opacity: 1' in pd_toolbar_style, 'Step ' + step + '.2: Verify toolbar set to opaque.', case_id, step + '.2')
        Selenium_Utility.assert_true(self, 'margin-left: 0px' in pd_left_pane_style, 'Step ' + step + '.3: Verify left pane offset to left by 0px.', case_id, step + '.3')
        Selenium_Utility.assert_true(self, 'opacity: 1' in pd_toolbar_style, 'Step ' + step + '.4: Verify left pane set to opaque.', case_id, step + '.4')

    def maximize_container_and_verify(self, case_id, step):
        '''click to maximize container and verify'''
        self.driver.find_element(*DesignerLocators.page_designer_container_maximize).click()
        time.sleep(3)
        pd_container_style = self.driver.execute_script('return $(\'div[data-ibx-type="pdContainer"]\').attr("class");')
        Selenium_Utility.assert_true(self, 'pd-cont-maximized' in pd_container_style, 'Step ' + step + ': Verify report is full size.', case_id, step)

    def double_click_to_run(self, fex):
        Selenium_Utility.switch_to_window(self, 1)
        Selenium_Utility.check_view_mode(self)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.file))        
        fex_element = self.driver.find_element(By.CSS_SELECTOR, 'div[title*="' + fex + '"]')
        ActionChains(self.driver).double_click(fex_element).perform()
        
    def choose_filter_value_and_verify(self, filter_name, filter_value, case_id, step):
        time.sleep(20)
        if filter_name == 'Category':
            self.driver.execute_script('$(\'div.output-area-frame>iframe\').contents().find(\'.ibx-select-open-btn\')[0].click();')
            time.sleep(2)
            self.driver.execute_script('$(\'div.output-area-frame>iframe\').contents().find(\'.ibx-label-text:contains("' + filter_value + '")\').click();')
            time.sleep(2)
            self.driver.execute_script('$(\'div.output-area-frame>iframe\').contents().find(\'.ibx-select-open-btn\')[0].click();')
            time.sleep(2)
        legend_title = self.driver.execute_script('var iframe = $(\'div.output-area-frame>iframe\').contents().find(\'.ibx-iframe-frame\');return iframe.contents().find(\'.legend text[class*="legend-label"]\').text()')
        Selenium_Utility.assert_equal(self, filter_value, legend_title, 'Step ' + step + ': Verify only ' + filter_value + ' appears in chart legend.', case_id, step)
        time.sleep(5)
        
    def enter_portal_title_and_alias(self, folder, title, alias, case_id, step):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(DesignerLocators.portal_designer_new_dialog_title))
        self.driver.find_element(*DesignerLocators.portal_designer_new_dialog_title).send_keys(title) 
        wf_url = Selenium_Utility.get_setup_url(self) 
        expected_url_label = wf_url + 'portal/' + folder + '/' + title.replace(' ', '_')
        actual_url_label = self.driver.execute_script('return $(\'.pvd-url input\').attr(\'aria-label\');')
        Selenium_Utility.assert_equal(self, expected_url_label, actual_url_label, 'Step ' + step + '.1: Verify url label before entering alias.', case_id, step + '.1')          
        self.driver.find_element(*DesignerLocators.portal_designer_new_dialog_alias).send_keys(alias)        
        expected_url_label = wf_url + 'portal/' + alias
        actual_url_label = self.driver.execute_script('return $(\'.pvd-url input\').attr(\'aria-label\');')
        Selenium_Utility.assert_equal(self, expected_url_label, actual_url_label, 'Step ' + step + '.2: Verify url label after entering alias.', case_id, step + '.2')
        
    def create_portal(self, case_id, step):
        self.driver.find_element(*DesignerLocators.portal_designer_create_my_pages_menu_checkbox).click()
        self.driver.find_element(*DesignerLocators.portal_designer_create_button).click()
        time.sleep(2)
        portal_folder_element = self.driver.execute_script('return $(\'.folder-item .ibx-label-text:contains("Smoke Test for V5 Portal")\');')
        Selenium_Utility.assert_not_none(self, portal_folder_element, 'Step ' + step + ': Verify the V5 portal is in the content area and shows as folder.', case_id, step)

    def navigate_hp_folder(self, path):
        '''navigate to the folder where fex is located'''
        folders = path.split('->')
        domain_button = self.driver.find_element(*HomePageLocators.domain_button)
        domain_button.click()    
        for folder in folders:
            time.sleep(2)
            self.driver.execute_script('$(\'.folder-item:contains("' + folder + '")\').dblclick();') 
        
    def copy_and_paste_fex(self, ori_path, fex, dest_path, case_id, step):
        Selenium_Utility.check_view_mode(self)
        Selenium_Utility.navigate_hp_folder(self, ori_path)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.file))
        Selenium_Utility.right_click_item_to_perform(self, 'file-item', 'copy', fex)
        Selenium_Utility.navigate_hp_folder(self, dest_path)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(HomePageLocators.folder))     
        Selenium_Utility.right_click_item_to_perform(self, 'files-box', 'paste')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.file))
        copied_page_element = self.driver.execute_script('return $(\'.file-item .ibx-label-text:contains("Sales Dashboard (Filtered)")\')[0];')
        Selenium_Utility.assert_not_none(self, copied_page_element, 'Step ' + step + ': Verify page copied to V5 portal.', case_id, step)
        
    def ibx_wait(self):
        script = 'return $(\'div[data-ibx-type="ibxWaiting"]\');'
        ibx_waiting_elements = self.driver.execute_script(script)
        while len(ibx_waiting_elements) != 0:
            time.sleep(1)
            ibx_waiting_elements = self.driver.execute_script(script)       
                    
    def run_portal(self, item_name, case_id, step):
        time.sleep(3)
        Selenium_Utility.right_click_item_to_perform(self, 'home-tree-node', 'run', item_name)
        Selenium_Utility.switch_to_window(self, 2)
        time.sleep(10)
        Selenium_Utility.ibx_wait(self)
        pd_page_element = self.driver.execute_script('return $(\'div[data-ibx-type="pdPageRunner"]\');')
        Selenium_Utility.assert_not_none(self, pd_page_element, 'Step ' + step + ': Verify the V5 portal runs in another window/browser tab.', case_id, step)
    
    def click_filter_button(self, case_id, step):  
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(DesignerLocators.portal_designer_run_filter))     
        self.driver.find_element(*DesignerLocators.portal_designer_run_filter).click()
        pd_filter_bar_element = self.driver.execute_script('return $(\'div[data-ibx-type="pdFilterGrid"]\');')
        Selenium_Utility.assert_not_none(self, pd_filter_bar_element, 'Step ' + step + ': Verify the filter bar appears.', case_id, step)
        
    def pd_choose_filter_value_and_verify(self, filter_value, expected_actual_category_sales_total_revenue, expected_regional_sales_trend_risers_number, expected_discount_by_region_label, expected_regional_profit_by_category_yaxis_upper_bound, expected_tab_container_legend_label, expected_carousel_container_color_scale_upper_bound, case_id, step):    
        self.driver.execute_script('$(\'.pd-regular-filter-wrapper .ibx-select-open-btn\')[0].click();')
        time.sleep(2)
        self.driver.execute_script('$(\'.ibx-paged-item .ibx-label-text:contains("' + filter_value + '")\').click();')
        time.sleep(5)
        Selenium_Utility.ibx_wait(self)
        #Verify Category Sales panel total revenue
        actual_category_sales_total_revenue = self.driver.execute_script('return $(\'.grid-stack-item:first-child .pd-cont-iframe>iframe\').contents().find(\'text[class*="totalLabel"]\').text();')
        Selenium_Utility.assert_equal(self, expected_actual_category_sales_total_revenue, actual_category_sales_total_revenue, 'Step ' + step + '.1: Verify Category Sales panel total revenue.', case_id, step + '.1')
        #Verify Regional Sales Trend panel risers number
        regional_sales_trend_risers = self.driver.execute_script('return $(\'.grid-stack-item:nth-child(2) .pd-cont-iframe>iframe\').contents().find(\'.risers\').children();')
        actual_regional_sales_trend_risers_number = len(regional_sales_trend_risers)
        Selenium_Utility.assert_equal(self, expected_regional_sales_trend_risers_number, actual_regional_sales_trend_risers_number, 'Step ' + step + '.2: Verify Regional Sales Trend panel risers number.', case_id, step + '.2')
        #Verify Discount by Region panel label
        actual_discount_by_region_label = self.driver.execute_script('return $(\'.grid-stack-item:nth-child(3) .pd-cont-iframe>iframe\').contents().find(\'text[class*="zaxisOrdinal-labels"]\').text();')
        Selenium_Utility.assert_equal(self, expected_discount_by_region_label, actual_discount_by_region_label, 'Step ' + step + '.3: Verify Discount by Region panel label.', case_id, step + '.3')
        #Verify Regional Profit by Category panel y-axis upper bound
        actual_regional_profit_by_category_yaxis_upper_bound = self.driver.execute_script('return $(\'.grid-stack-item:nth-child(4) .pd-cont-iframe>iframe\').contents().find(\'text[class*="yaxis-labels"]:last-child\').text();')
        Selenium_Utility.assert_equal(self, expected_regional_profit_by_category_yaxis_upper_bound, actual_regional_profit_by_category_yaxis_upper_bound, 'Step ' + step + '.4: Verify Regional Profit by Category panel y-axis upper bound.', case_id, step + '.4')
        #Verify tab container legend label
        actual_tab_container_legend_label = self.driver.execute_script('return $(\'.grid-stack-item:nth-child(5) .pd-cont-iframe>iframe\').contents().find(\'text[class*=legend-labels]\').text();')
        Selenium_Utility.assert_equal(self, expected_tab_container_legend_label, actual_tab_container_legend_label, 'Step ' + step + '.5: Verify tab container legend label.', case_id, step + '.5')
        #Verify carousel container color scale upper bound
        actual_carousel_container_color_scale_upper_bound = self.driver.execute_script('return $(\'.grid-stack-item:nth-child(6) .pd-cont-iframe>iframe\').contents().find(\'text[class*=colorScale-labels]:last-child\').text();')
        Selenium_Utility.assert_equal(self, expected_carousel_container_color_scale_upper_bound, actual_carousel_container_color_scale_upper_bound, 'Step ' + step + '.6: Verify carousel container color scale upper bound.', case_id, step + '.6')

    def click_left_panel_folder(self, folder, case_id, step):
        self.driver.execute_script('$(\'.ibx-accordion-page .ibx-label-text:contains("' + folder + '")\').click();')
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(DesignerLocators.portal_designer_run_folder))
        actual_content = self.driver.execute_script('return $(\'.ibx-accordion-page .bundle-folder-item\').text();')
        expected_content = '+'
        Selenium_Utility.assert_equal(self, expected_content, actual_content, 'Step ' + step + ': Verify + sign appearing after clicking My Pages folder.', case_id, step)
        
    def pd_verify_new_page_dialog(self, expected_new_page_dialog_title, expected_new_page_dialog_open_existing_text, expected_new_page_dialog_select_template_text, expected_new_page_dialog_template_items_label, case_id, step):
        '''verify New Page dialog of portal designer run time'''
        self.driver.execute_script('$(\'.ibx-accordion-page .bundle-folder-item:contains("+")\').click();')
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(DesignerLocators.portal_designer_new_page_dialog))
        #verify new page dialog title
        actual_new_page_dialog_title = self.driver.find_element(*DesignerLocators.portal_designer_new_page_dialog_title).text
        Selenium_Utility.assert_equal(self, expected_new_page_dialog_title, actual_new_page_dialog_title, 'Step ' + step + '.1: Verify Page Template dialog title.', case_id, step + '.1')
        #verify new page dialog open existing page button text
        actual_new_page_dialog_open_existing_text = self.driver.find_element(*DesignerLocators.portal_designer_new_page_dialog_open_existing).text
        Selenium_Utility.assert_equal(self, expected_new_page_dialog_open_existing_text, actual_new_page_dialog_open_existing_text, 'Step ' + step + '.2: Verify Page Template dialog open existing page button text.', case_id, step + '.2')
        #verify new page dialog select template text
        actual_new_page_dialog_select_template_text = self.driver.find_element(*DesignerLocators.portal_designer_new_page_dialog_select_template).text
        Selenium_Utility.assert_equal(self, expected_new_page_dialog_select_template_text, actual_new_page_dialog_select_template_text, 'Step ' + step + '.3: Verify Page Template dialog select template text.', case_id, step + '.3')
        #verify new page dialog template items label
        actual_new_page_dialog_template_items_label = [label.text for label in self.driver.find_elements(*DesignerLocators.portal_designer_new_page_dialog_template_item)]
        Selenium_Utility.assert_equal(self, expected_new_page_dialog_template_items_label, actual_new_page_dialog_template_items_label, 'Step ' + step + '.4: Verify Page Template dialog template items label.', case_id, step + '.4')
 
    def pd_choose_page_template(self, template, expected_container_number, case_id, step):
        if template == 'Grid 2-1':
            template_css_locator = DesignerLocators.portal_designer_new_page_dialog_template_item_grid21
        self.driver.find_element(*template_css_locator).click() 
        time.sleep(10)
        actual_containers = self.driver.execute_script('return $(\'div[data-ibx-type="pdPageRunner"]:last-child .grid-stack-item\');')
        actual_container_number = len(actual_containers)
        Selenium_Utility.assert_equal(self, expected_container_number, actual_container_number, 'Step ' + step + '.1: Verify new page container number.', case_id, step + '.1')
        containers_width = []
        for i in range(3):
            containers_width.append(int(self.driver.execute_script('return $(\'div[data-ibx-type="pdPageRunner"]:last-child .grid-stack-item:nth-child(' + str(i+1) + ')\').attr(\'data-gs-width\')')))
        Selenium_Utility.assert_true(self, containers_width[0] + containers_width[1] == containers_width[2], 'Step ' + step + '.2: Verify the sum of width of container 1 and container 2 equals to the width of container 3.', case_id, step + '.2')
        
    def verify_metadata_tree(self, expected_dimension_nodes, expected_measure_nodes, case_id, step):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(DesignerLocators.chart_designer_dimension_tree))
        time.sleep(5)
        #verify in metadata panel, Fields tab is selected, Variables tab is not selected
        fields_tab_selected = self.driver.execute_script('return $(\'.id-md-panel .ibx-tab-button:first-child\').attr(\'aria-selected\');')
        Selenium_Utility.assert_true(self, fields_tab_selected == 'true', 'Step ' + step + '.1: Verify Fields tab in metadata panel is selected.', case_id, step + '.1')
        variables_tab_selected = self.driver.execute_script('return $(\'.id-md-panel .ibx-tab-button:last-child\').attr(\'aria-selected\');')
        Selenium_Utility.assert_true(self, variables_tab_selected == 'false', 'Step ' + step + '.2: Verify Variables tab in metadata panel is not selected.', case_id, step + '.2')
        #verify dimension and measure tree nodes
        actual_dimension_tree_nodes = self.driver.execute_script('return $(\'.wfc-mdfp-dimension-tree .tnode-children .tnode-label\').text();')
        Selenium_Utility.assert_equal(self, ''.join(expected_dimension_nodes), actual_dimension_tree_nodes, 'Step ' + step + '.3: Verify Dimension tree nodes.', case_id, step + '.3')
        actual_measure_tree_nodes = self.driver.execute_script('return $(\'.wfc-mdfp-measure-tree .tnode-children .tnode-label\').text();')
        Selenium_Utility.assert_equal(self, ''.join(expected_measure_nodes), actual_measure_tree_nodes, 'Step ' + step + '.4: Verify Measure tree nodes.', case_id, step + '.4')   
        
    def click_designer_tab(self, tab, designer_mode='old'):
        if designer_mode == 'old':  
            self.driver.execute_script('$(\'.ibx-tab-button .ibx-label-text:contains("' + tab + '")\').click();') 
        if designer_mode == 'new':
            self.driver.execute_script('$(\'div[title="' + tab + ' tool"]\').click()')
        
    def verify_data_prep_canvas(self, case_id, step):
        time.sleep(30)
        data_prep_canvas = self.driver.execute_script('return $(\'.id-data-rs-data-flow-iframe>iframe\').contents().find(\'canvas\')[0];')  
        Selenium_Utility.assert_not_none(self, data_prep_canvas, 'Step ' + step + ': Verify Data Prep canvas is loaded.', case_id, step)    
        
    def navigate_join_tool_tree(self, path):
        folders = path.split('->')
        for folder in folders:
            time.sleep(2)
            self.driver.execute_script('$(\'.id-data-rs-data-flow-iframe>iframe\').contents().find(\'.ibx-label-text:contains("' + folder + '")\').click();')

    def get_element_center_coordinates(self, element_js):
        element_top = self.driver.execute_script(element_js + '.offset().top;') 
        element_left = self.driver.execute_script(element_js + '.offset().left;') 
        element_height = self.driver.execute_script(element_js + '.height();') 
        element_width = self.driver.execute_script(element_js + '.width();') 
        return element_left + 0.5 * element_width, element_top + 0.5 * element_height + 120

    def join_tool_drag_and_drop_to_canvas(self, element, case_id, step):    
        time.sleep(3) 
        move_to_element_script = 'return $(\'.id-data-rs-data-flow-iframe>iframe\').contents().find(\'div[data-ibx-type="ibxTreeBrowser"]\')'
        move_to_element_center_x, move_to_element_y = Selenium_Utility.get_element_center_coordinates(self, move_to_element_script)
        pyautogui.moveTo(move_to_element_center_x, move_to_element_y, 2)
        time.sleep(2)
        pyautogui.scroll(-1000)
        time.sleep(2)
        source_element_script = 'return $(\'.id-data-rs-data-flow-iframe>iframe\').contents().find(\'.ibx-label-text:contains("' + element + '")\')'
        source_element_x, source_element_y = Selenium_Utility.get_element_center_coordinates(self, source_element_script)
        pyautogui.mouseDown(source_element_x, source_element_y)
        time.sleep(10)
        target_element_script = 'return $(\'.id-data-rs-data-flow-iframe>iframe\').contents().find(\'canvas\')'  
        target_element_x, target_element_y = Selenium_Utility.get_element_center_coordinates(self, target_element_script)
        pyautogui.mouseDown(target_element_x, target_element_y)
        time.sleep(2)
        pyautogui.mouseUp(target_element_x, target_element_y)   
        time.sleep(10)
        #Verify Data Join widget displays.
        join_widget = self.driver.execute_script('return $(\'.id-data-rs-data-flow-iframe>iframe\').contents().find(\'.wcx-graph-top div[qa="Join 1"]\')[0];')
        Selenium_Utility.assert_not_none(self, join_widget, 'Step ' + step + '.1: Verify Data Join widget displays.', case_id, step + '.1') 
        #Verify master file widget displays
        element_widget = self.driver.execute_script('return $(\'.id-data-rs-data-flow-iframe>iframe\').contents().find(\'.wcx-graph-top div[qa="' + element + ' (T02)"]\')[0];')
        Selenium_Utility.assert_not_none(self, element_widget, 'Step ' + step + '.2: Verify ' + element + ' widget displays.', case_id, step + '.2') 
#         #Verify configure join widget displays
#         configure_join_widget = self.driver.execute_script('return $(\'.id-data-rs-data-flow-iframe>iframe\').contents().find(\'.wcx-multiframes-content-pane .ibx-label-text:contains("Configure \\\'Join 1\\\'")\')[0];')
#         Selenium_Utility.assert_not_none(self, configure_join_widget, 'Step ' + step + '.3: Verify configure \'Join 1\' widget displays.', case_id, step + '.3') 
#         #Verify data profiler widget displays
#         data_profiler_widget = self.driver.execute_script('return $(\'.id-data-rs-data-flow-iframe>iframe\').contents().find(\'.wcx-multiframes-content-pane .ibx-label-text:contains("Sample Data")\')[0];')
#         Selenium_Utility.assert_not_none(self, data_profiler_widget, 'Step ' + step + '.4: Verify Data Profiler widget displays.', case_id, step + '.4') 
        
    def add_nodes(self, search_pattern, dimension_node, measure_node):
        self.driver.find_element(*DesignerLocators.chart_designer_search_box).send_keys(search_pattern)
        time.sleep(2)
        self.driver.execute_script('$(\'.ibx-label-text:contains("' + dimension_node + '")\').dblclick();')       
        for _ in range(5):
            self.driver.find_element(*DesignerLocators.chart_designer_search_box).send_keys(keys.Keys.BACKSPACE)
        self.driver.execute_script('$(\'.measure-tree-box\').attr("style", "height: 600px;");')
        time.sleep(2)
        if measure_node == 'Revenue':
            measure_node = self.driver.execute_script('return $(\'.ibx-label-text:contains("' + measure_node + '")\')[1];')   
        else:
            measure_node = self.driver.execute_script('return $(\'.ibx-label-text:contains("' + measure_node + '")\')[0];')   
        ac = ActionChains(self.driver)
        ac.move_to_element(measure_node).context_click().perform()
        #WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(DesignerLocators.chart_designer_right_click_add_to_chart))
        time.sleep(3)
        self.driver.find_element(*DesignerLocators.chart_designer_right_click_add_to_chart).click()         

    def verify_preview_designer_chart(self, expected_preview_xaxix_title, expected_preview_xaxis_labels, expected_preview_yaxis_title, expected_preview_yaxis_labels, expected_preview_risers, expected_preview_risers_color, case_id, step):
        '''verify chart designer preview'''
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(DesignerLocators.chart_designer_preview_xaxis_title))        
        time.sleep(5)
        #verify risers number and color
        actual_preview_risers = len(self.driver.find_elements(*DesignerLocators.chart_designer_preview_risers))
        Selenium_Utility.assert_equal(self, expected_preview_risers, actual_preview_risers, 'Step ' + step + '.1: Verify chart designer preview total number of risers.', case_id, step + '.1')
        actual_preview_risers_color = len(self.driver.find_elements(By.CSS_SELECTOR, '.chartPanel rect[fill="' + expected_preview_risers_color + '"]'))
        Selenium_Utility.assert_equal(self, expected_preview_risers, actual_preview_risers_color, 'Step ' + step + '.2: Verify chart designer preview risers color.', case_id, step + '.2')
        #verify x axis title
        actual_preview_xaxis_title = self.driver.find_element(*DesignerLocators.chart_designer_preview_xaxis_title).text
        Selenium_Utility.assert_equal(self, expected_preview_xaxix_title, actual_preview_xaxis_title, 'Step ' + step + '.3: Verify chart designer preview x axis title.', case_id, step + '.3')   
        #verify x axis labels
        actual_preview_xaxis_labels = [label.text for label in self.driver.find_elements(*DesignerLocators.chart_designer_preview_xaxis_labels)]
        Selenium_Utility.assert_equal(self, expected_preview_xaxis_labels, actual_preview_xaxis_labels, 'Step ' + step + '.4: Verify chart designer preview x axis labels.', case_id, step + '.4')
        #verify y axis title
        if expected_preview_yaxis_title is not None:
            actual_preview_yaxis_title = self.driver.find_element(*DesignerLocators.chart_designer_preview_yaxis_title).text
            Selenium_Utility.assert_equal(self, expected_preview_yaxis_title, actual_preview_yaxis_title, 'Step ' + step + '.5: Verify chart designer preview y axis title.', case_id, step + '.5')   
        #verify y axis labels
        if expected_preview_yaxis_labels is not None:
            actual_preview_yaxis_labels = [label.text for label in self.driver.find_elements(*DesignerLocators.chart_designer_preview_yaxis_labels)]
            Selenium_Utility.assert_equal(self, expected_preview_yaxis_labels, actual_preview_yaxis_labels, 'Step ' + step + '.6: Verify chart designer preview y axis labels.', case_id, step + '.6')

    def click_preview_and_verify_in_run_mode_designer(self, case_id, step):
        self.driver.find_element(*DesignerLocators.chart_designer_preview).click()
        time.sleep(5)
        preview_box_style = self.driver.execute_script('return $(\'.ides-tool-preview-box\').attr("style");')
        Selenium_Utility.assert_equal(self, 'visibility: visible;', preview_box_style, 'Step ' + step + ': Verify preview box displays.', case_id, step)
        
    def exit_preview_and_verify_in_design_mode_designer(self, case_id, step):
        '''click preview floating button to exit and verity page back to design mode'''
        self.driver.execute_script('$(\'#idesToolPeviewBtn\').click();')    
        time.sleep(3)
        preview_box_style = self.driver.execute_script('return $(\'.ides-tool-preview-box\').attr("style");')
        Selenium_Utility.assert_equal(self, 'visibility: hidden;', preview_box_style, 'Step ' + step + ': Verify preview box is hidden.', case_id, step)

    def run_in_new_window(self, report_type, expected_runtime_xaxix_title, expected_runtime_xaxis_labels, expected_runtime_yaxis_title, expected_runtime_yaxis_labels, expected_runtime_risers, expected_tuntime_risers_color, case_id, step):
        time.sleep(5)
        self.driver.get(Selenium_Utility.get_setup_url(self) + 'home8206')
        Selenium_Utility.navigate_to_case_folder(self)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(HomePageLocators.file))
        if report_type == 'chart':        
            Selenium_Utility.right_click_item_to_perform(self, 'file-item', 'run as -> run in new window', case_id)
        if report_type == 'workbook':
            Selenium_Utility.right_click_item_to_perform(self, 'file-item', 'run in new window', case_id)
        Selenium_Utility.switch_to_window(self, 2)
        if report_type == 'workbook':
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(DesignerLocators.chart_designer_iframe))        
            self.driver.switch_to.frame(self.driver.find_element(*DesignerLocators.chart_designer_iframe))
        Selenium_Utility.verify_preview_designer_chart(self, expected_runtime_xaxix_title, expected_runtime_xaxis_labels, expected_runtime_yaxis_title, expected_runtime_yaxis_labels, expected_runtime_risers, expected_tuntime_risers_color, case_id, step)
    
    def edit_with_text_editor(self, case_id, step):    
        self.driver.close()
        Selenium_Utility.switch_to_window(self, 1)
        time.sleep(1)
        Selenium_Utility.right_click_item_to_perform(self, 'file-item', 'edit with text editor', case_id)
        Selenium_Utility.switch_to_window(self, 2)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(TextEditorLocators.ace_text_layer))        
        editor_text = self.driver.execute_script('return $(\'.ace_text-layer\').text();')
        join_request = ''
        fileObj = open('./data/join_request.data', 'r')
        line = fileObj.readline()
        while line:
            join_request += line.replace('\n', '')
            line = fileObj.readline()
        fileObj.close()    
        self.assert_true(join_request in editor_text, 'Step ' + step + '.1: Verify join request in fex.', case_id, step + '.1')  
        chart_request = ''
        fileObj = open('./data/chart_request.data', 'r')
        line = fileObj.readline()
        while line:
            chart_request += line.replace('\n', '')
            line = fileObj.readline()
        fileObj.close()    
        self.assert_true(chart_request in editor_text, 'Step ' + step + '.2: Verify chart request in fex.', case_id, step + '.2')  
    
    def reopen_join_fex(self, expected_preview_xaxix_title, expected_preview_xaxis_labels, expected_preview_yaxis_title, expected_preview_yaxis_labels, expected_preview_risers, expected_preview_risers_color, case_id, step):
        self.driver.close()
        Selenium_Utility.switch_to_window(self, 1)
        time.sleep(1)
        Selenium_Utility.right_click_item_to_perform(self, 'file-item', 'edit', case_id)   
        Selenium_Utility.switch_to_window(self, 2)
        Selenium_Utility.verify_preview_designer_chart(self, expected_preview_xaxix_title, expected_preview_xaxis_labels, expected_preview_yaxis_title, expected_preview_yaxis_labels, expected_preview_risers, expected_preview_risers_color, case_id, step)
        dimension_tree_labels = self.driver.execute_script('return $(\'.dimension-tree-box .ibx-label-text\').text();')
        Selenium_Utility.assert_true(self, 'Store Info' in dimension_tree_labels, 'Step ' + step + '.7: Verify join node displays in dimension tree.', case_id, step + '.7')
        measure_tree_labels = self.driver.execute_script('return $(\'.measure-tree-box .ibx-label-text\').text();')
        Selenium_Utility.assert_true(self, 'Store Info' in measure_tree_labels, 'Step ' + step + '.8: Verify join node displays in measure tree.', case_id, step + '.8')
        vertical_bucket_pill_title = self.driver.execute_script('return $(\'.wfc-bucket:first-child .wfc-bucket-pill\').attr(\'title\');')
        Selenium_Utility.assert_true(self, 'Name: REVENUE_US' in vertical_bucket_pill_title, 'Step ' + step + '.9: Verify Vertical bucket contains correct field.', case_id, step + '.9')
        horizontal_bucket_pill_title = self.driver.execute_script('return $(\'.wfc-bucket:nth-child(2) .wfc-bucket-pill\').attr(\'title\');')
        Selenium_Utility.assert_true(self, 'Title: Store Type' in horizontal_bucket_pill_title, 'Step ' + step + '.10: Verify Horizontal bucket contains correct field.', case_id, step + '.10')
    
    def verify_join_nodes(self, expected_node_header, case_id, step, designer_mode='old'):
        time.sleep(20)
        if designer_mode == 'old':
            join_nodes = self.driver.execute_script('return $(\'.id-data-rs-data-flow-iframe>iframe\').contents().find(\'.wcx-gnode\');') 
            actual_node_header = self.driver.execute_script('return $(\'.id-data-rs-data-flow-iframe>iframe\').contents().find(\'.wcx-gnode-header\').text();')
        if designer_mode == 'new':  
            join_nodes = self.driver.execute_script('return $(\'iframe.ibx-shell-tool-host\').contents().find(\'.wcx-graph-node\');')
            actual_node_header = self.driver.execute_script('return $(\'iframe.ibx-shell-tool-host\').contents().find(\'.wcx-gnode-header\').text();')
        Selenium_Utility.assert_equal(self, 3, len(join_nodes), 'Step ' + step + '.1: Verify number of join nodes.', case_id, step + '.1') 
        Selenium_Utility.assert_equal(self, ''.join(expected_node_header), actual_node_header, 'Step ' + step + '.2: Verify join nodes headers', case_id, step + '.2')
        
    def upload_data(self, upload_data_type, upload_data_file):
        time.sleep(3)
        self.driver.execute_script('$(\'.ibx-dialog-button-box .ibx-label-text:contains("Upload")\').click()')
        Selenium_Utility.switch_to_window(self, 2)
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(ServerLocators.console_frame))
        ac = ActionChains(self.driver)
        ac.move_to_element(self.driver.execute_script('return $(\'.ibx-label-text:contains("' + upload_data_type + '")\')[0];')).context_click().perform()
        time.sleep(2)
        self.driver.execute_script('$(\'.ibx-label-text:contains("Upload Data")\').click()')
        time.sleep(2)
        if sys.platform == 'linux':
            pyautogui.click(20, 10)
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'l')
            time.sleep(2)
            pyautogui.typewrite(upload_data_file)
            time.sleep(2)
            pyautogui.press('enter')
        else:
            '''TODO: windows open dialog to open file'''
            pass
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(ServerLocators.load_button))
        self.driver.find_element(*ServerLocators.load_button).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ServerLocators.input_app_ibisamp))
        self.driver.find_element(*ServerLocators.input_app_ibisamp).clear()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ServerLocators.input_default))
        self.driver.find_element(*ServerLocators.input_default).send_keys('baseapp')
        self.driver.execute_script('$(\'.ibx-label-text:contains("Proceed to Load")\').click()')
        
    def verify_preview_designer_chart_default(self, case_id, master_file, step):
        '''verify preview default view'''
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(DesignerLocators.chart_designer_preview_default_string))
        expected_preview_string = 'Drop measures and dimensions here'
        actual_preview_string = self.driver.find_element(*DesignerLocators.chart_designer_preview_default_string).text
        Selenium_Utility.assert_equal(self, expected_preview_string, actual_preview_string, 'Step ' + step + '.1: Verify default preview string.', case_id, step + '.1')
        #verify risers:
        expected_riser_types = 5
        actual_riser_types =  len(self.driver.execute_script('return $(\'.groupPanel g.risers\').children();')) 
        Selenium_Utility.assert_equal(self, expected_riser_types, actual_riser_types, 'Step ' + step + '.2: Verify default preview riser types.', case_id, step + '.2')
        expected_riser_numbers = 25
        actual_riser_numbers =  len(self.driver.execute_script('return $(\'.groupPanel g.risers rect\');')) 
        Selenium_Utility.assert_equal(self, expected_riser_numbers, actual_riser_numbers, 'Step ' + step + '.3: Verify default preview riser numbers.', case_id, step + '.3') 
        #verify master file
        actual_master_file = self.driver.execute_script('return $($(\'.wfc-mdfp-master-button > .ibx-label-text\')[0]).text()')
        Selenium_Utility.assert_equal(self, master_file, actual_master_file, 'Step ' + step + '.4: Verify master file.', case_id, step + '.4')

    def add_field(self, field):
        self.driver.find_element(*DesignerLocators.chart_designer_search_box).clear()
        self.driver.find_element(*DesignerLocators.chart_designer_search_box).send_keys(field)
        time.sleep(2)
        self.driver.execute_script('$(\'.ibx-label-text:contains("' + field + '")\').dblclick();')
        
    def click_preview_and_verify_output(self, expected_runtime_xaxix_title, expected_runtime_xaxis_labels, expected_runtime_yaxis_title, expected_runtime_yaxis_labels, expected_runtime_risers, expected_tuntime_risers_color, case_id, step):
        self.driver.find_element(*DesignerLocators.chart_designer_preview).click()
        time.sleep(5)
        Selenium_Utility.verify_preview_designer_chart(self, expected_runtime_xaxix_title, expected_runtime_xaxis_labels, expected_runtime_yaxis_title, expected_runtime_yaxis_labels, expected_runtime_risers, expected_tuntime_risers_color, case_id, step)

    def exit_preview(self):
        '''click preview floating button to exit'''
        self.driver.execute_script('$(\'#idesToolPeviewBtn\').click();')    
        time.sleep(3)
        
    def add_field_by_expanding_tree_node(self, tree_node, field):
        self.driver.execute_script('$(\'div[title~="' + tree_node + '"] .tnode-btn-collapsed\').click()')
        time.sleep(2)
        if field == 'VALUE1':
            self.driver.execute_script('$($(\'.ibx-label-text:contains("' + field + '")\')[0]).dblclick()')
        else:
            self.driver.execute_script('$(\'.ibx-label-text:contains("' + field + '")\').dblclick();')
            
    def verify_preview_designer_report_default_with_file(self, case_id, master_file, step):
        Selenium_Utility.verify_preview_designer_report_default(self, case_id, step)
        #verify master file
        actual_master_file = self.driver.execute_script('return $($(\'.wfc-mdfp-master-button > .ibx-label-text\')[0]).text()')
        Selenium_Utility.assert_equal(self, master_file, actual_master_file, 'Step ' + step + '.4: Verify master file.', case_id, step + '.4')
     
    def click_preview_and_verify_report_output(self, expected_preview, case_id, step):
        self.driver.find_element(*DesignerLocators.chart_designer_preview).click()
        time.sleep(5)
        Selenium_Utility.verify_preview_designer_report(self, expected_preview, case_id, step)