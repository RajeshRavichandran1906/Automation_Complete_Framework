'''
Created on Jun 12, 2018

@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2326008
TestCase Name = Check functionality of all Public User banner link options
'''

import unittest, time, os, sys
from selenium import webdriver
from configparser import ConfigParser
from common.lib.configfiles import settings
from common.wftools import login, wf_mainpage
from common.lib import utillity, core_utility
from common.lib import javascript, global_variables
from common.lib.utillity import UtillityMethods
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.color import Color
from common.lib.basetestcase import BaseTestCase

class C2313993_TestClass(BaseTestCase):

    def setUp(self):
        UtillityMethods.asert_failure_count=0
        browser = UtillityMethods.parseinitfile(self,'browser')
        configFile = 'config.ini'
        parser = ConfigParser()
        parser.read(os.path.join(settings.CONFIG_ROOT, configFile)) 
        option = 'executables_path'
        if browser.lower() == 'firefox':
            section = 'firefox'
            targetPath = parser[section][option]
            option = 'executable'
            firefoxTargetExec = parser[section][option]
            targetExec = targetPath + firefoxTargetExec
            self.driver = webdriver.Firefox(executable_path=targetExec)
        elif browser.lower() == 'chrome':
            section = 'chrome'      
            targetPath = parser[section][option]    
            option = 'executable'
            chromeTargetExec = parser[section][option]
            targetExec = targetPath + r'\\' + chromeTargetExec
            options = webdriver.ChromeOptions()
            prefs = {"download.prompt_for_download": bool(parser[section]['prompt_for_download'])}
            options.add_experimental_option("prefs", prefs)
            opts=parser[section]['argument'].split(',')
            for opt in opts:
                options.add_argument(opt)
            self.driver = webdriver.Chrome(executable_path=targetExec, chrome_options=options)
        elif browser.lower() == 'ie':
            section = 'ie'
            targetPath = parser.get(section, option)
            sys.path.append(targetPath)
            cap = DesiredCapabilities.INTERNETEXPLORER
            cap['requireWindowFocus']=bool(parser[section]['requireWindowFocus'])
            option = 'executables_path'
            targetPath = parser[section][option]    
            option = 'executable'
            ieTargetExec = parser[section][option]
            targetExec = targetPath + ieTargetExec
            self.driver = webdriver.Ie(executable_path=targetExec)
        elif browser.lower() == 'edge':
            section = 'edge'
            option = 'pageLoadStrategy'
            pageLoadStrategy_ = parser[section][option]    
            cap = DesiredCapabilities.EDGE
            cap['pageLoadStrategy'] = pageLoadStrategy_
            option = 'executables_path'
            targetPath = parser[section][option]    
            option = 'executable'
            edgeTargetExec = parser[section][option]
            targetExec = targetPath + edgeTargetExec
            self.driver=webdriver.Edge(executable_path=targetExec, capabilities=cap)
        self.driver.maximize_window()
        UtillityMethods.windows=self.driver.window_handles
        global_variables.Global_variables.windows_handles=self.driver.window_handles
        global_variables.Global_variables.current_test_case=self._testMethodName.replace('test_', '').strip()
        BRWSR_NAME=self.driver.desired_capabilities['browserName'].lower()
        if BRWSR_NAME=='microsoftedge':
            UtillityMethods.reset_edge_browser_zoom(self)
            global_variables.Global_variables.browser_name='edge'
        elif BRWSR_NAME=='internet explorer':
            global_variables.Global_variables.browser_name='ie'
        else:
            global_variables.Global_variables.browser_name=BRWSR_NAME
    def tearDown(self):
        filename_obj=self._testMethodName
        setup_url = UtillityMethods.get_setup_url(self)
#         filename = os.getcwd() + "\\failure_captures\\"+ self._testMethodName + ".png"
        script_failure_occurred=False
        for method, error in self._outcome.errors:
            if error:
                script_failure_occurred=True
                try:
                    utillity.UtillityMethods.take_monitor_screenshot(self, filename_obj, image_type='fail')
                except:
                    print("Exception in save_screenshot")
                    utillity.UtillityMethods.take_monitor_screenshot(self, filename_obj, image_type='fail')
        utillobj = utillity.UtillityMethods(self.driver)
        try:
            utillobj.switch_to_main_window() if global_variables.Global_variables.ie_crash_wndnum != 0 else time.sleep(1)
            time.sleep(3)
            utillobj.infoassist_api_logout()
        except:
            pass
        time.sleep(2)
        try:
            self.driver.quit()
        except:
            pass 
        verification_failure_msg='Check Point failure List: '       
        if global_variables.Global_variables.asert_failure_count>0 and script_failure_occurred==False:
            for item in global_variables.Global_variables.verification_failure_msg_list:
                verification_failure_msg = verification_failure_msg + '\n' + item
            raise_msg='Verification check point failed. The set up used is [{0}]. {1}'.format(setup_url, verification_failure_msg)
            raise ValueError(raise_msg)
        elif script_failure_occurred==True:
            script_filure_error_msg='Script failed to complete the run. The set up used is [' + setup_url + '].'
            raise RuntimeError(script_filure_error_msg)

    
    
    def test_C2326008(self):
        
        """
        TESTCASE VARIABLES
        """
        long_wait = 120
        medium_wait = 60

        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        core_utilobj = core_utility.CoreUtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        javascript_obj = javascript.JavaScript(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        def verify_title_and_tabs(title, step_no, expected_image=None, expected_tab_list=None, css=None):
            utillobj.asin(title, driver.title, step_no+".2: Verify "+ title +" title displayed in new tab") 
            
            if expected_tab_list != None:
                tab_button_elements = self.driver.find_elements_by_css_selector(css) 
                actual_tab_list = [el.text for el in tab_button_elements if el.text!=''] 
                utillobj.as_List_equal(expected_tab_list, actual_tab_list, step_no+".3: Verify text displayed in "+title+" tab") 
            if expected_image != None:
                utillobj.verify_picture_using_sikuli(expected_image, step_no+".4: Verify image in "+title+" tab")
        
        def select_and_verify_new_tab(path, step_no, new_tab_name, control_type='tab'):
            wfmain_obj.select_username_dropdown_menu(navigate_path=path)
            if len(driver.window_handles) != 2:
                time.sleep(90)
            utillobj.asequal(len(driver.window_handles),2, step_no+".1a: Verify new tab handle appears")       
            core_utilobj.switch_to_new_window(window_maximize=False)
            if control_type=='tab':    
                try:
                    utillobj.verify_tab_item_using_uiautomation(new_tab_name)
                except:
                    utillobj.asequal(False,True, "StepX: {0} tab name doesn't exist exception".format(new_tab_name))
        
        def verify_htmltag_text(css,expected_text, msg):
            advance_search_css = self.driver.find_element_by_css_selector(css)
            advance_search_text = utillobj.get_attribute_value(advance_search_css, 'dom_visible_text')
            utillobj.asequal(expected_text, advance_search_text['dom_visible_text'], msg)
            
        def verify_htmltag_property(css, prop, expected_text, msg):
            advance_search_css = self.driver.find_element_by_css_selector(css)
            actual_text = utillobj.get_element_css_propery(advance_search_css, prop)
            utillobj.asin(expected_text, actual_text, msg)
            
        def verify_color(css, expected, msg):
            actual_color = Color.from_string(self.driver.find_element_by_css_selector(css).value_of_css_property('color')).rgba
            expected_color=UtillityMethods.color_picker(self, expected, 'rgba')
            utillobj.asequal(expected_color, actual_color, msg)
        
        def verify_text(expected_text_list_1):
            text_elems=self.driver.find_elements_by_css_selector("td")
            text= javascript_obj.get_elements_text(text_elems)        
            actual_text_items=[e.strip().replace(' ','').replace('\n','') for e in text if e!='']
            for i in expected_text_list_1:
                for j in actual_text_items:
                    if i in j:
                        status = True
                        break
                    else:
                        status=False
                if status == False:
                    break
            utillobj.asequal(True, status, "Step02.1d: Verify text present in DeferredReportStatus window")
        
        """
        Step01: Sign into WebFOCUS Home Page as Public User by clicking the Public access Link.
        """
        wftools_login_obj.invoke_home_page_with_public_access()
        folders_css=".menu-btn div[class*='down']"
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        
        """
        Step02: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        files_box_css = ".content-box.ibx-widget .files-box"
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Folders", medium_wait)
        wfmain_obj.select_option_from_crumb_box('Domains')
        
        """
        Step02: In the banner link, click on the top right username > Help > click Information Center.
        Verify WebFOCUS Information Center opens in a new tab with following options:
        1.Learn.
        2.Connect.
        3.Technical Support.
        """
        select_and_verify_new_tab('Help->Information Center', 'Step02.1', 'WebFOCUS Release.*')
        verify_title_and_tabs('Information Center', "Step 02.2")
           
        bth_css = self.driver.find_elements_by_css_selector("[class*='col-md-4'] [class*='h3']")
        actual_text_items=[e.text for e in bth_css if e!='']
        expected_list = ['Learn', 'Connect', 'Technical Support']
        utillobj.as_List_equal(expected_list, actual_text_items, "Step 02.3: Verify Learn, Connect, Technical Support in Information Center")
           
        """
        Step 03: Close Information Center tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
           
        """
        Step 04: In the banner link, click on the top right username > Help > click VideoAssist.
        Verify a new tab should opens with links to informational videos.
        """
        select_and_verify_new_tab('Help->VideoAssist', 'Step 04', 'Videos')
        verify_title_and_tabs('Videos', "Step 04.1c")
           
        videos = self.driver.find_elements_by_css_selector("[href*='.mp4']")
        utillobj.as_LE(207,len(videos),"Step 04.2: Verify .mp4 video files in VideoAssist page")
           
        """
        Step 05: Close VideoAssist tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
           
        """
        Step 06: In the banner link, click on the top right username > Help > click Technical Library.
        Verify WebFOCUS Technical Content opens in a new tab.
        """
        select_and_verify_new_tab('Help->Technical Library', 'Step 06', '.*Technical Content.*')
        verify_title_and_tabs('Technical Content', "Step 06.1c")
           
        verify_btn_css="html #magnify-search-2 button"
        utillobj.verify_popup(verify_btn_css,'Step 06.2a: Verify Technical Content' , popup_text_css="html h1", popup_text="Technical Content")
           
        """
        Step 07: Close WebFOCUS Technical Content tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
           
        """
        Step08: In the banner link, click on the top right username > Help > click Community.
        Verify a new tab should opens with links to different Information Builders Communities.
        """
        select_and_verify_new_tab('Help->Community', 'Step 08', 'Information Builders Community | Information Builders')
        verify_title_and_tabs('Information Builders Community | Information Builders', "Step 08.1")
           
        hyper_link = self.driver.find_elements_by_css_selector("[class*='columns small-12'] [href]")
        utillobj.as_GE(38,len(hyper_link),"Step 08.2: Verify hyper link references in Community page")
           
        bth_css = self.driver.find_elements_by_css_selector("[class*='m-card-title']")
        actual_text_items=[e.text for e in bth_css if e!='']
        expected_list = ['User Groups', 'Focal Point Forums', 'Announcement', 'User Group Webinars', 'Forum Highlights', 'Resources']
        utillobj.as_List_equal(expected_list, actual_text_items, "Step 08.3: m-card title in Community page")
           
        """
        Step 09: Close Information Builders Communities tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
           
        """
        Step 10: In the banner link, click on the top right username > Help > click Information Builders Home.
        Verify Business Intelligence and Data Management Software opens in a new tab.
        """
        select_and_verify_new_tab('Help->Information Builders Home', 'Step 10', 'Business Intelligence and Data Management Software*')
        verify_title_and_tabs('Business Intelligence and Data Management Software | Information Builders', "Step 10.1")
           
        bth_css = self.driver.find_elements_by_css_selector("[class*='m-card-title']")
        actual_text_items=[e.text for e in bth_css if e!='']
        expected = ['Join Our Customer Community', 'Top Analysts Talk 2018 Tech Trends', 'Unlocking IoT Potential', 'About Us', 'Support and Services']
        utillobj.as_List_equal(expected, actual_text_items, "Step 10.2: m-card title in Information Builders Home page")
           
        """
        Step 11: Close Business Intelligence and Data Management Software tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
           
        """
        Step 12: In the banner link, click on the top right username > Legacy Home Page.
        Verify WebFOCUS Legacy Home opens in a new tab.
        """
        select_and_verify_new_tab('Legacy Home Page', 'Step 12.1', 'WebFOCUS Legacy Home')
        verify_title_and_tabs('WebFOCUS Legacy Home', "Step 12.2")
           
        domain_img_css = "[src*='discovery_domain']"
        utillobj.verify_object_visible(domain_img_css, True, "Step 12.3: Verify domain image object is displaying")
           
        """
        Step 13: Close WebFOCUS Legacy Home.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
         
        """
        Step 14: In the banner link, click on the top right username > Click Sign In.
        Verify it back to WebFOCUS Sign In Page.
        """
        wfmain_obj.signin_from_username_dropdown_menu()
                
        
if __name__ == '__main__':
    unittest.main()        