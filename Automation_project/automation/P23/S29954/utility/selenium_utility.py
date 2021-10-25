'''
Created on Mar 20, 2019

@author: ml12793

@descrpition: selenium library for OLAP smoke test
'''
import re
import time
from utility.locators import LoginPageLocators
from utility.locators import OlapLocators
from utility.locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Selenium_Utility(object):
    
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
        node = Selenium_Utility.parseinitfile(self, 'nodeid')
        port = Selenium_Utility.parseinitfile(self, 'httpport')
        context = Selenium_Utility.parseinitfile(self, 'wfcontext')
        setup_url = 'http://' + node + ':' + port + context + '/'
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
        
    def navigate_to_folder(self):
        '''navigate to specific folder in new home page'''
        project = Selenium_Utility.parseinitfile(self, 'project_id')
        suite = Selenium_Utility.parseinitfile(self, 'suite_id')
        group = Selenium_Utility.parseinitfile(self, 'group_id')
        folder = project + '_' + suite 
        subfolder = group
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(OlapLocators.panel_content_button))
        self.driver.find_element(*OlapLocators.panel_content_button).click()
        time.sleep(2)
        self.driver.execute_script('$(\'.home-tree-node:contains("Workspaces")\').click()')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomePageLocators.view_button))          
        list_view_style = self.driver.execute_script('return $(\'.btn-how-view-grid\').attr(\'style\')')
        if list_view_style == 'display: none;':  #handles situation when grid view is selected
            self.driver.find_element(*HomePageLocators.view_button).click()    
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(OlapLocators.folder))     
        self.driver.execute_script('$(\'.folder-item:contains("' + folder + '")\').dblclick();') 
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OlapLocators.folder))       
        self.driver.execute_script('$(\'.folder-image-text:contains("' + subfolder + '")\').dblclick();')   
        
    def run_olap_report(self, case_id):
        Selenium_Utility.navigate_to_folder(self)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(OlapLocators.file))
        self.driver.execute_script('$(\'.file-item:contains("' + case_id + '")\').dblclick();')
        
    def activate_olap_panel_and_run(self):
        '''click Olap button control to bring up Olap panel, then click run button'''
        self.driver.execute_script('var iframe = $(\'div.output-area-frame>iframe\')[0];iframe.contentWindow.document.body.getElementsByTagName(\'frame\')[1].contentDocument.getElementById(\'olapbuttonclear\').click();')      
        windows = self.driver.window_handles
        while len(windows) != 2:
            time.sleep(1)
            windows = self.driver.window_handles
        
        self.driver.switch_to.window(windows[1])
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OlapLocators.olap_panel_run_button))
        self.driver.find_element(*OlapLocators.olap_panel_run_button).click()
        
        windows = self.driver.window_handles
        while len(windows) != 1:
            time.sleep(1)
            windows = self.driver.window_handles
        
        self.driver.switch_to.window(windows[0])
        
    def click_run_in_olap_pane(self):
        self.driver.execute_script('var iframe = $(\'div.output-area-frame>iframe\')[0];iframe.contentWindow.document.getElementById(\'olaprunbuttonclear\').click();')      

    def verify_table(self, olap_pane_mode, case_id, step):
        '''verify table displays correctly after clicking run button in Olap pane'''
        msg = 'Step ' + step + ': Verify output table. - FAILED.'
        expected_table = ''
        fileObj = open('./data/table.data', "r")
        line = fileObj.readline()
        while line:
            expected_table += line
            line = fileObj.readline()
        fileObj.close()
        
        report_table = Selenium_Utility.report_table(self, olap_pane_mode)
        context = Selenium_Utility.parseinitfile(self, 'wfcontext')
        report_table = re.sub('src="' + context + '/ibi_html/S[0-9]+[.]*[0-9]*_[0-9]+F', '', report_table)
        self.assertEqual(expected_table, report_table, msg)
        print('Step ' + step + ': Verify output table. - PASSED.')
        Selenium_Utility.verification_screenshot_capture(self, case_id, step)
        
    def report_table(self, olap_pane_mode):
        '''return table source in different Olap run formats'''
        if olap_pane_mode == 'olap_pane_control':
            return self.driver.execute_script('var iframe = $(\'div.output-area-frame>iframe\')[0];var table = iframe.contentWindow.document.body.getElementsByTagName(\'frame\')[0].contentDocument.getElementsByClassName(\'gridB\')[0];return table.innerHTML;')
        if olap_pane_mode == 'olap_pane':
            return self.driver.execute_script('var iframe = $(\'div.output-area-frame>iframe\')[0];var table = iframe.contentWindow.document.body.getElementsByTagName(\'iframe\')[0].contentDocument.getElementsByClassName(\'gridB\')[0];return table.innerHTML;')

    def verify_olap_button_control_position(self, case_id, step):
        '''verify Olap button control appears at left lower corner'''
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(OlapLocators.output_popup))
        olap_button_control_doc_vertical_position = self.driver.execute_script('var iframe = $(\'div.output-area-frame>iframe\')[0];var olapbuttonDoc = iframe.contentWindow.document.body.getElementsByTagName(\'frame\')[1].contentDocument;return $(olapbuttonDoc).height();')
        output_frame_height = self.driver.execute_script('var iframe = $(\'div.output-area-frame>iframe\')[0];var outputFrame = iframe.contentWindow.document;return $(outputFrame).height();')    
        olap_button_control_horizontal_position = self.driver.execute_script('var iframe = $(\'div.output-area-frame>iframe\')[0];var olapbutton = iframe.contentWindow.document.body.getElementsByTagName(\'frame\')[1].contentDocument.getElementById(\'olapbuttonclear\');return $(olapbutton).offset().left;')
        olap_button_control_doc_width = self.driver.execute_script('var iframe = $(\'div.output-area-frame>iframe\')[0];var olapbuttonDoc = iframe.contentWindow.document.body.getElementsByTagName(\'frame\')[1].contentDocument;return $(olapbuttonDoc).width();')
        msg_vertical = 'Step ' + step + ': Verify the Olap Button Control is displayed in lower left corner(vertical position verification). - FAILED.'
        msg_horizontal = 'Step ' + step + ': Verify the Olap Button Control is displayed in lower left corner(horizontal position verification). - FAILED.'
        self.assertTrue(olap_button_control_doc_vertical_position < .2 * output_frame_height, msg_vertical)
        self.assertTrue(olap_button_control_horizontal_position < .2 * olap_button_control_doc_width, msg_horizontal)
        print('Step ' + step + ': Verify the Olap Button Control is displayed in lower left corner. - PASSED.')
        Selenium_Utility.verification_screenshot_capture(self, case_id, step)

    def verify_olap_pane_position(self, expected_position, case_id, step):
        '''verify olap pane position'''
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(OlapLocators.output_popup))
        olap_pane_vertical_position = self.driver.execute_script('var iframe = $(\'div.output-area-frame>iframe\')[0];var olappane = iframe.contentWindow.document.getElementById(\'OLAPPANE\');return $(olappane).offset().top;')    
        output_frame_height =  self.driver.execute_script('var iframe = $(\'div.output-area-frame>iframe\')[0];var outputFrame = iframe.contentWindow.document;return $(outputFrame).height();')    
        if olap_pane_vertical_position < .2 * output_frame_height:
            olap_pane_position = 'top'
        if olap_pane_vertical_position > .8 * output_frame_height:
            olap_pane_position = 'bottom'
        msg = 'Step ' + step + ': Verify Olap Pane at ' + expected_position + '. - FAILED.'
        self.assertEqual(expected_position, olap_pane_position, msg)
        print('Step ' + step + ': Verify Olap Pane at ' + expected_position + '. - PASSED.')
        Selenium_Utility.verification_screenshot_capture(self, case_id, step)

    def verification_screenshot_capture(self, case_id, step):
        try:
            self.driver.save_screenshot(case_id + '_' + step + '.png')
        except:
            print('Exception in save screenshot of verification step ' + step)