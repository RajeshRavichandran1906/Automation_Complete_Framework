'''
Created on May 29, 2018

@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2326005
TestCase Name = Check functionality of all Basic User banner link options
'''

import unittest, time, os, sys, uiautomation
from threading import Thread 
from selenium import webdriver
from configparser import ConfigParser
from common.lib.configfiles import settings
from common.wftools import login, wf_mainpage
from common.lib import utillity, core_utility, global_variables
from common.lib import javascript
from common.lib.utillity import UtillityMethods
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.color import Color

class C2326005_TestClass(unittest.TestCase):

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
        self.driver.maximize_window()
        UtillityMethods.windows=self.driver.window_handles
        global_variables.Global_variables.windows_handles=self.driver.window_handles
        global_variables.Global_variables.current_test_case=self._testMethodName.replace('test_', '').strip()
        global_variables.Global_variables.browser_name=self.driver.desired_capabilities['browserName'].lower().replace('internet explorer','ie')
    def tearDown(self):
        filename_obj=self._testMethodName
        setup_url = UtillityMethods.get_setup_url(self)
        script_failure_occurred=False
        for method, error in self._outcome.errors:
            if error:
                script_failure_occurred=True
                try:
                    utillity.UtillityMethods.take_monitor_screenshot(self, filename_obj, image_type='fail')
                except:
                    print("Exception in save_screenshot")
                    utillity.UtillityMethods.take_monitor_screenshot(self, filename_obj, image_type='fail')
        if global_variables.Global_variables.browser_name == 'edge' :
            logout_process = Thread(target=self.logout_webfocus)
            click_leave_button_process = Thread(target=self.click_on_leave_page_button)
            logout_process.start()
            click_leave_button_process.start()
            click_leave_button_process.join()
            logout_process.join()
        else :
            self.logout_webfocus()
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
    
    def logout_webfocus(self): 
        """
        This method used to close window if opened more than one window and logout webfocus
        Note : This method should be remove once https://developer.microsoft.com/en-us/microsoft-edge/platform/issues/16904736/ issue fixed for Edge browser 
        """
        try:
            UtillityMethods.switch_to_main_window(self)
            UtillityMethods.infoassist_api_logout(self)
        except:
            pass
    
    def click_on_leave_page_button(self):
        """
        This method used to click on Leave page button when leave page pop up widow appear.
        Note : This method should be remove once https://developer.microsoft.com/en-us/microsoft-edge/platform/issues/16904736/ issue fixed for Edge browser 
        """
        try :
            button = uiautomation.ButtonControl(Name='Leave')
            button.Click()
        except :
            pass
    
    
    
    def test_C2326005(self):
        
        """
        TESTCASE VARIABLES
        """
        
        basic_username = 'mrid01'
        basic_password = 'mrpass01'
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
                tab_button_label_css=css
                tab_button_elements = self.driver.find_elements_by_css_selector(tab_button_label_css) 
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
        Step01: Sign into WebFOCUS Home Page as Basic User.
        """
        wftools_login_obj.invoke_home_page(basic_username, basic_password)
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
        Step03: In the banner link, click on the top right username > Tools > click Deferred Status.
        Verify Deferred Report Status opens in a new tab.
        """
        select_and_verify_new_tab('Tools->Deferred Status', 'Step02', 'Deferred Report Status')
                   
        deferred_css = "table[id]"
        utillobj.synchronize_with_number_of_element(deferred_css, 1, medium_wait)        
            
        title= 'Deferred Report Status'
        deferred_image= 'deferred.png'
        step_no='Step02'
        verify_title_and_tabs(title, step_no, expected_image=deferred_image)
        refresh_image_css = "img[src*='defresh1.gif']"
        sort_image_css = "img[src*='def_sort_az.gif']"
        delete_image_css = "img[src*='Delete16.gif']"
        utillobj.verify_object_visible(refresh_image_css, True, "Step02.1c: Verify Refresh image object is displaying")
        utillobj.verify_object_visible(sort_image_css, True, "Step02.1c: Verify sort image object is displaying")
        utillobj.verify_object_visible(delete_image_css, True, "Step02.1c: Verify delete image object is displaying")
                    
        expected_text_list_1 = ['DeferredReportStatusasof', 'Refresheveryseconds.(min.5seconds)EnableRefresh:']
        verify_text(expected_text_list_1)        
            
        text = self.driver.find_elements_by_css_selector("td img[title]")
        actual_text_list_2 = [e.get_attribute('title') for e in text]        
        expected_text_list_2 = ['Refresh', 'Refresh', 'Sort By', 'Reverse Sort Order', 'Delete All', 'All', 'Help']
        utillobj.as_List_equal(expected_text_list_2, actual_text_list_2, "Step02.2b: Verify text Refresh, Sort By, Delete, Help")
            
        href = self.driver.find_elements_by_css_selector("td a[href]")
        actual_href_count = len(href)
        utillobj.asequal(4, actual_href_count, "Step02.2c: Verify hyperlink count in Deferred Status Report page")       
            
        dropdown_css ="[name='IBIMR_def_sortoption'] [selected]"
        actual_css = self.driver.find_element_by_css_selector(dropdown_css).get_attribute('value')
        utillobj.asequal("Date", actual_css, "Step02.2d: Verify Date selected in Sort By dropdown")
            
        """
        Step04: Close Deferred Report Status tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
            
        """
        Step05: In the banner link, click on the top right username > Tools > click Stop Requests.
        Verify Stop Requests dialog box opens with background transparent gray layer over the rest of the WebFOCUS Home Page and
        should display message as "No outstanding requests to stop."
        """
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        wfmain_obj.select_username_dropdown_menu(navigate_path='Tools->Stop Requests')
            
        stop_request_popup_css = "[class*='dialog-main-box'] [class*='ibx-label'][class*='label-text']"
        utillobj.synchronize_with_number_of_element(stop_request_popup_css, 6, medium_wait)
            
        title= 'WebFOCUS Home Page'
        text_css="[class*='dialog-main-box'] [class*='ibx-label'][class*='label-text']"
        stop_request_tab_list= ['Stop Requests', 'No outstanding requests to stop.', 'OK']
        step_no='Step04'
        verify_title_and_tabs(title, step_no, expected_tab_list=stop_request_tab_list, css=text_css)
            
        background_css = "[class*='ibx-popup-glass-pane']"
        actual_background_layer = self.driver.find_element_by_css_selector(background_css).value_of_css_property('opacity')
        utillobj.asequal("0.5", str(actual_background_layer), "Step04: Verify background gray layer when stop request dialog opens")
            
        """
        Step06: Close Stop Requests dialog box.
        """
        close_button_ele = self.driver.find_element_by_css_selector("[class*='dialog-main-box'] [class*='close-button']")
        core_utilobj.left_click(close_button_ele)
           
        """
        Step07: In the banner link, click on the top right username > Tools > click Magnify Search Page.
        Verify Search Results: opens in a new tab with the following options in this window:
   
        1.Century Electronics logo available at the topmost left corner.
        2.Search text box.
        3.Collection list box listed as drop down. 
        4.Search button
        5.Results Per Page listed with the no. of pages as drop down.
        6.Advance search link.
        7. Sign Out link available at the topmost right corner.
        """
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        select_and_verify_new_tab('Tools->Magnify Search Page', 'Step06', 'Search Results:')
        search_result_css = "div input:not([type*='hidden'])"
        utillobj.synchronize_with_number_of_element(search_result_css, 2, medium_wait)        
           
        title= 'Search Results:';search_results_image= 'search_results_century.png';step_no='Step06.1'
        verify_title_and_tabs(title, step_no, expected_image=search_results_image)
           
        search_text_box_css = "input[placeholder='Type your search term here']"
        utillobj.verify_object_visible(search_text_box_css, True, "Step06.2: Verify search_text_box object is displaying")
           
        collection_list_box_css = "select#site>option[value='default_collection']"
        verify_htmltag_text(collection_list_box_css, "Century Electronics KB", "Step06.3: Verify Collection list box listed as drop down.")
           
        search_button_css=self.driver.find_element_by_css_selector("input[name][type='submit']")
        search_button = utillobj.get_element_attribute(search_button_css, 'value')
        utillobj.asequal("Search", search_button, "Step06.4: Verify Search button")
           
        verify_btn_css="html input[name='btnG']";text_css="html #sf span:nth-child(1)"
        utillobj.verify_popup(verify_btn_css,'Step06.5a: Verify Magnify Search Page displays Results Per Page', popup_text_css=text_css, popup_text="Results Per Page")        
        results_per_page_num_css = "span>select>option[selected]"
        verify_htmltag_text(results_per_page_num_css, "10", "Step06.5b: Verify no. of pages as drop down")
           
        advance_search_css = "[title*='advance'][title*='search'][href], [title*='Advanced'][title*='Search'][href]"
        verify_htmltag_text(advance_search_css, "Advanced Search", "Step06.6a: Verify Advanced Search text and hyperlink")
        verify_htmltag_property(advance_search_css, 'text-decoration','underline', "Step06.6b: Verify Advanced Search  text underline")
        verify_color(advance_search_css, 'hyper_link_blue', "Step06.6b: Verify Advanced Search text color")
           
        sign_out_css = "[title='Sign Out'][href]"
        verify_htmltag_text(sign_out_css, "Sign Out", "Step06.7a: Verify Sign Out text and hyperlink")
        verify_htmltag_property(sign_out_css, 'text-decoration','underline', "Step06.7b: Verify Sign Out text underline")
        verify_color(sign_out_css, 'hyper_link_blue', "Step06.7c: Verify Sign Out text color")
           
        verify_btn_css="html a[title='Go to Magnify Search Home']";text_css="html #ddd > table > tbody > tr > td:nth-child(2) > div > b"
        utillobj.verify_popup(verify_btn_css,'Step06.8: Verify the element Search Tips is Visible as expected.', popup_text_css=text_css, popup_text="Search Tips")
           
        """
        Step08: Close "Search Results:" tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
           
        """
        Step09: In the banner link, click on the top right username > Preferences.
        Verify My Preferences dialog box opens with a background transparent gray layer over the rest of the WebFOCUS Home Page and should display with the following options:
        1.Change the Display from Title or Name radio buttons. 
        2.Drop down menu for language option (By default English is selected).
        3.Reset Preferences button.
        4.OK button. 
        5.Cancel button.
        """
        wfmain_obj.select_username_dropdown_menu(navigate_path='Preferences')
            
        preferences_dialog_css = "[class*='dialog-main-box'] [class*='ibx-label'][class*='label-text']"
        utillobj.synchronize_with_number_of_element(preferences_dialog_css, 11, medium_wait)
            
        title= 'WebFOCUS Home Page'
        text_css="[class*='dialog-main-box'] [class*='ibx-label'][class*='label-text']"
        stop_request_tab_list= ['My Preferences', 'Display', 'Title', 'Name', 'Language', 'Reset preferences', 'OK', 'Cancel']
        step_no='Step08'
        verify_title_and_tabs(title, step_no, expected_tab_list=stop_request_tab_list, css=preferences_dialog_css)
           
        background_css = "[class*='ibx-popup-glass-pane']"
        actual_background_layer = self.driver.find_element_by_css_selector(background_css).value_of_css_property('opacity')
        utillobj.asequal("0.5", str(actual_background_layer), "Step08: Verify background gray layer when preferences dialog opens")
           
        """
        Step10: Close Preferences dialog box.
        """
        close_button_ele = self.driver.find_element_by_css_selector("[class*='dialog-main-box'] [class*='close-button']")
        core_utilobj.left_click(close_button_ele)
           
        """
        Step11: In the banner link, click on the top right username > Help > click Information Center.
        Verify WebFOCUS Information Center opens in a new tab with following options:
        1.Learn.
        2.Connect.
        3.Technical Support.
        """
        select_and_verify_new_tab('Help->Information Center', 'Step 10.1', 'WebFOCUS Release*')
        verify_title_and_tabs('WebFOCUS Release 8.2 Information Center', "Step 10.2")
           
        bth_css = self.driver.find_elements_by_css_selector("[class*='col-md-4'] [class*='h3']")
        actual_text_items=[e.text for e in bth_css if e!='']
        expected_list = ['Learn', 'Connect', 'Technical Support']
        utillobj.as_List_equal(expected_list, actual_text_items, "Step 10.3: Verify Learn, Connect, Technical Support in Information Center")
           
        """
        Step 12: Close Information Center tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
           
        """
        Step 13: In the banner link, click on the top right username > Help > click VideoAssist.
        Verify a new tab should opens with links to informational videos.
        """
        select_and_verify_new_tab('Help->VideoAssist', 'Step 12', 'Videos')
        verify_title_and_tabs('Videos', "Step 12.1c")
           
        videos = self.driver.find_elements_by_css_selector("[href*='.mp4']")
        utillobj.as_LE(207,len(videos),"Step 12.2: Verify .mp4 video files in VideoAssist page")
           
        """
        Step 14: Close VideoAssist tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
          
        """
        Step15: In the banner link, click on the top right username > Help > click Technical Library.
        Verify WebFOCUS Technical Content opens in a new tab.
        """
        select_and_verify_new_tab('Help->Technical Library', 'Step 14', '.*Technical Content.*')
        verify_title_and_tabs('WebFOCUS 8.2 Technical Content', "Step 14.1c")
          
        verify_btn_css="html #magnify-search-2 button"
        utillobj.verify_popup(verify_btn_css,'Step 14.2a: Verify Technical Content' , popup_text_css="html h1", popup_text="Technical Content")
          
        """
        Step 16: Close WebFOCUS Technical Content tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
          
        """
        Step 17: In the banner link, click on the top right username > Help > click Community.
        Verify a new tab should opens with links to different Information Builders Communities.
        """
        select_and_verify_new_tab('Help->Community', 'Step 16.1', 'Information Builders Community | Information Builders')
        verify_title_and_tabs('Information Builders Community | Information Builders', "Step 16.2")
          
        hyper_link = self.driver.find_elements_by_css_selector("[class*='columns small-12'] [href]")
        utillobj.as_GE(38,len(hyper_link),"Step 16.3: Verify hyper link references in Community page")
          
        bth_css = self.driver.find_elements_by_css_selector("[class*='m-card-title']")
        actual_text_items=[e.text for e in bth_css if e!='']
        expected_list = ['User Groups', 'Focal Point Forums', 'Announcement', 'User Group Webinars', 'Forum Highlights', 'Resources']
        utillobj.as_List_equal(expected_list, actual_text_items, "Step 16.4: m-card title in Community page")
          
        """
        Step 18: Close Information Builders Communities tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
          
        """
        Step 19: In the banner link, click on the top right username > Help > click Information Builders Home.
        Verify Business Intelligence and Data Management Software opens in a new tab.
        """
        select_and_verify_new_tab('Help->Information Builders Home', 'Step 18.1', 'Business Intelligence and Data Management Software*')
        verify_title_and_tabs('Business Intelligence and Data Management Software | Information Builders', "Step 18.2")
          
        bth_css = self.driver.find_elements_by_css_selector("[class*='m-card-title']")
        actual_text_items=[e.text for e in bth_css if e!='']
        expected = ['Join Our Customer Community', 'Top Analysts Talk 2018 Tech Trends', 'Unlocking IoT Potential', 'About Us', 'Support and Services']
        utillobj.as_List_equal(expected, actual_text_items, "Step 18.3: m-card title in Information Builders Home page")
          
        """
        Step 20: Close Business Intelligence and Data Management Software tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
          
        """
        Step 21: In the banner link, click on the top right username > Help > click About WebFOCUS.
        Verify About WebFOCUS dialog box opens with a background transparent gray layer over the rest of the WebFOCUS Home Page.
        1.Edition
        2.Product release
        3.Service pack
        4.Package name
        5.Release ID
        6.Build/GEN number
        7.Build/GEN date
        8.Application Server
        """
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        wfmain_obj.select_username_dropdown_menu(navigate_path='Help->About WebFOCUS')
          
        about_css= "[class*='dialog-main-box'] [class*='ibx-label'][class*='label-text']"
        utillobj.synchronize_with_number_of_element(about_css, 21, medium_wait)
        utillobj.asequal("About WebFOCUS", self.driver.find_element_by_css_selector(about_css).text, "Step 20.1: Verify dialog title")
          
        left_panel_css ="[class*='dialog-main-box'] [class*='left-panel'] [class*='ibx-label'][class*='label-text']"
        left_panel_items = self.driver.find_elements_by_css_selector(left_panel_css)
        actual_left_panel_items=[e.text for e in left_panel_items if e!='']
        expected_left = ['Edition', 'Product release', 'Service pack', 'Package name', 'Release ID', 'Build/GEN number', 'Build/GEN date', 'Application Server']
        utillobj.as_List_equal(expected_left, actual_left_panel_items, "Step 20.2: Verify About dialog left menu")
          
        right_panel_css = "[class*='dialog-main-box'] [class*='right-panel'] [class*='ibx-label'][class*='label-text']"
        right_items = self.driver.find_elements_by_css_selector(right_panel_css)
          
        for item in right_items:
            if item.text != None:
                status=True
            else:
                print(item.text+" might be None.")
                status=False
                break
        if status== True:
            utillobj.asequal(True, status, "Step 20.3: Verify About page gen information verification.") 
           
        background_css = "[class*='ibx-popup-glass-pane']"
        actual_background_layer = self.driver.find_element_by_css_selector(background_css).value_of_css_property('opacity')
        utillobj.asequal("0.5", str(actual_background_layer), "Step 20.4: Verify background gray layer when About WebFOCUS dialog opens")
           
        """
        step 22: Click OK button to close "About WebFOCUS" dialog box.
        """
        close_button_ele = self.driver.find_element_by_css_selector("[class*='dialog-main-box'] [class*='close-button']")
        core_utilobj.left_click(close_button_ele)
          
        """
        Step 23: In the banner link, click on the top right username > Help > click Licenses.
        Verify 3rd Party Information opens in a new tab with a list of licenses.
        """
        select_and_verify_new_tab('Help->Licenses', 'Step 22.1', '3rd Party Information')
        verify_title_and_tabs('3rd Party Information', "Step 22.2")
          
        Party_header_css="table td.console-header span"
        Party_header_elems = self.driver.find_elements_by_css_selector(Party_header_css)
        actual_item = [elem for elem in [elem.text.strip() for elem in Party_header_elems if elem != ''] if elem != '']
        expected_item = ['Description', 'Version', 'File(s)', 'Licenses', 'Third Party Links', 'Release', 'Update History', 'Date']
        utillobj.as_List_equal(expected_item, actual_item, "Step 22..3: Verify labels in 3rd Party Information")
          
        party_info_css="table td.console-header a"
        b4_obj=utillobj.beautifulsoup_object_creation()
        total_info = b4_obj.select(party_info_css)
        acutal_info = [elem for elem in [elem.get_text(strip=True) for elem in total_info] if elem != '']
        for item in acutal_info:
            if 'Apache' in item:
                status_=True
                break
            else:
                status_=False
        if status_== True:
            utillobj.asequal(True, status_, "Step 22.4: Verify 3rd Party Information verification.") 
        else:
            utillobj.asin('Apache', acutal_info, "Step 22.4: Verify 3rd Party Information verification.")
          
        """
        Step 24: Close 3rd Party Information tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
          
        """
        Step 25: In the banner link, click on the top right username > Legacy Home Page.
        Verify WebFOCUS Legacy Home opens in a new tab.
        """
        select_and_verify_new_tab('Legacy Home Page', 'Step 24.1', 'WebFOCUS Legacy Home')
        verify_title_and_tabs('WebFOCUS Legacy Home', "Step 24.2")
          
        domain_img_css = "[src*='discovery_domain']"
        utillobj.verify_object_visible(domain_img_css, True, "Step 24.3: Verify domain image object is displaying")
          
        """
        Step 26: Close WebFOCUS Legacy Home.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
         
        
        """
        Step 27: In the banner link, click on the top right username > Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
        
                
        
if __name__ == '__main__':
    unittest.main()        