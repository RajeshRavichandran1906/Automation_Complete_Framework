'''
Created on Jun 06, 2018

@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2326006
TestCase Name = Check functionality of all Advanced User banner link options
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

class C2326006_TestClass(unittest.TestCase):

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
    
    def test_C2326006(self):
        
        """
        TESTCASE VARIABLES
        """
        
        advanced_username = 'mrid02'
        advanced_password = 'mrpass02'
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
        Step01: Sign into WebFOCUS Home Page as Advanced User.
        """
        wftools_login_obj.invoke_home_page(advanced_username, advanced_password)
        folders_css = ".menu-btn div[class*='down']"
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        
        """
        Step02: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        files_box_css = ".content-box.ibx-widget .files-box"
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Folders", medium_wait)
        wfmain_obj.select_option_from_crumb_box('Domains')
        
        """
        Step02: In the banner link, click on the top right username > Tools > click Deferred Status.
        Verify Deferred Report Status opens in a new tab.
        """
        select_and_verify_new_tab('Tools->Deferred Status', 'Step02.1', 'Deferred Report Status')
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
        Step03: Close Deferred Report Status tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
              
        """
        Step04: In the banner link, click on the top right username > Tools > click Stop Requests.
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
        Step05: Close Stop Requests dialog box.
        """
        close_button_ele = self.driver.find_element_by_css_selector("[class*='dialog-main-box'] [class*='close-button']")
        core_utilobj.left_click(close_button_ele)
          
        """
        Step06: In the banner link, click on the top right username > Tools > click ReportCaster Explorer.
        Verify ReportCaster Explore opens in a new tab.
        """
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        select_and_verify_new_tab('Tools->ReportCaster Explorer', 'Step06', 'ReportCaster Explorer')
        explorer_path_item_css = "#IbfsExplorerPane_hbPath [id*='ExplorerPathBarItem']"
        utillobj.synchronize_with_number_of_element(explorer_path_item_css, 1, medium_wait)        
            
        title= 'ReportCaster Explorer'; report_caster_image= 'report_caster.png'; step_no='Step06'
        verify_title_and_tabs(title, step_no, expected_image=report_caster_image, expected_tab_list=['Domains'], css=explorer_path_item_css)
          
        organize_label_elem = self.driver.find_element_by_css_selector("#IbfsExplorerPane_toolBar")
        actual_organize_label = utillobj.get_attribute_value(organize_label_elem, 'dom_visible_text')
        utillobj.asequal("Organize", actual_organize_label['dom_visible_text'], "Step06.5a: Verify Organize text in ReportCaster Explorer")
          
        organize_drop_down_css ="#IbfsExplorerPane_btnOrganize [class*='drop-down-arrow']"
        utillobj.verify_object_visible(organize_drop_down_css, True, "Step06.5b: Verify Organize drop down exists")
          
        domain_list_elems = self.driver.find_elements_by_css_selector("#paneIbfsExplorer_exTree [class*='tree-view-body-content'] td")
        actual_domain_list = [a.text for a in domain_list_elems if a.text!=' ']
        expected_domain_list = ['Domains', 'Public', 'Retail Samples']
        cn=1
        for item in expected_domain_list:
            utillobj.asin(item, actual_domain_list, "Step06.6.{0}: Verify '{1}' Domains list".format(cn,item))
            cn+=1
        header_list_elems = self.driver.find_elements_by_css_selector("#paneIbfsExplorer [id*='paneIbfsExplorer_pnlHorizontal'] td")
        expected_header_list = ['Title', 'ScheduleID', 'Path', 'Owner', 'LastTimeExecuted', 'LastJobStatus', 'NextRunTime', 'Method', 'DestinationAddress', 'Priority']
        #expected_header_list = ['Title', 'ScheduleID', 'Path', 'Owner', 'LastTimeExecuted', 'LastJobStatus', 'NextRunTime']
        actual_header_list = [e.text.replace(' ','') for e in header_list_elems if e.text.replace(' ','')!='']
        utillobj.as_List_equal(expected_header_list, actual_header_list, "Step06.7: Verify titles in ReportCaster Panel explorer")
          
        utillobj.verify_picture_using_sikuli('rc_filter.png', "Step06.8: Verify filter image in "+title+" tab")
        utillobj.verify_picture_using_sikuli('rc_folder_view.png', "Step06.9: Verify folder view image in "+title+" tab")
          
        """
        Step07: Close ReportCaster Explorer tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
          
        """
        Step08: In the banner link, click on the top right username > Tools > click ReportCaster Status.
        Verify ReportCaster Status opens in a new tab and there should be three ribbon tabs at the top with the following options:
        """
        select_and_verify_new_tab('Tools->ReportCaster Status', 'Step08.1', 'ReportCaster Status')
          
        ribbon_tab_css = "#Console_ribbonTabPane [selected][class*='tab-button']"
        utillobj.synchronize_with_number_of_element(ribbon_tab_css, 1, medium_wait)        
            
        title= 'ReportCaster Status'; job_status_image= 'rc_job_status.png'; step_no='Step08.1'
        verify_title_and_tabs(title, step_no, expected_image=job_status_image)
        """
        1.Manage Job Status
        i.Priority, ii. Auto Refresh 5 Sec with dropdown menu, iii.Delete, iv.View Log and View Trace
        """
        expected_job_status = ['Priority', 'Delete', 'Auto Refresh 5 Sec', ' View Log', 'View Trace', 'Manage Job Status']
        actual_job_status = self.driver.find_element_by_css_selector("#wfBiRCConsoleTabPage #RCConsoleTabPage_manageJobStatusVBox").text.split('\n')
        utillobj.as_List_equal(expected_job_status, actual_job_status, "Step08.1.4: Verify Manage Job Status options")
          
        job_status_refresh_drop_down_css = "[id*='manageJobStatusRefresh'] [class*='drop-down-arrow']"
        utillobj.verify_object_visible(job_status_refresh_drop_down_css, True, "Step08.1.5: Verify Manage Job Status Refresh drop down exists")
          
        job_status_checked_css = "#wfBiConsole [id*='BiVBox'][class*='ribbon-group']:not([style*='hidden'])>div>div:nth-child(3)[class*='button-checked']"
        utillobj.verify_object_visible(job_status_checked_css, True, "Step08.1.6: Verify Manage Job Status button checked exists")
          
        job_status_disabled_count = self.driver.find_elements_by_css_selector("#RCConsoleTabPage_manageJobStatusVBox [disabled='true']")
        utillobj.asequal(8,len(job_status_disabled_count), "Step08.1.7: Verify Manage Job Status disabled buttons and labels count")
          
        """
        2.Show
        i.Job Status, ii.Job Log, iii.Blackout Periods and iv.Execution IDs
        """
        expected_show_options = ['Job Status', 'Job Log', 'Blackout', 'Periods', 'Execution', 'IDs', 'Show']
        show_elemns = self.driver.find_element_by_css_selector("#wfBiConsole [id*='BiVBox'][class*='ribbon-group']:not([style*='hidden'])")
        actual_show_options = show_elemns.text.replace('\n\n','\n').replace('\n\n','\n').split('\n')
        utillobj.as_List_equal(expected_show_options, actual_show_options, "Step08.2.1: Verify show ribbon tabs options")
                
        utillobj.verify_picture_using_sikuli('rc_job_log.png', "Step08.2.2: Verify Job Log image in "+title+" tab")
        utillobj.verify_picture_using_sikuli('rc_blackout.png', "Step08.2.3: Verify Blackout image in "+title+" tab")
        utillobj.verify_picture_using_sikuli('rc_execution_id.png', "Step08.2.4: Verify Execution IDs image in "+title+" tab")
          
        """
        3.Actions
        i.Refresh
        """
        expected_actions_options = ['Refresh', 'Actions']
        actual_actions_options = self.driver.find_element_by_css_selector("#wfBiConsole #RCConsoleTabPage_generalActionsVBox").text.split('\n\n\n\n')
        utillobj.as_List_equal(expected_actions_options, actual_actions_options, "Step08.3.1: Verify Actions ribbon tabs options")
        utillobj.verify_picture_using_sikuli('rc_refresh.png', "Step08.3.2: Verify Refresh image in "+title+" tab")
          
        """
        Step09: Close ReportCaster Status tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
            
        """
        Step10: In the banner link, click on the top right username > Tools > click Magnify Search Page.
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
        select_and_verify_new_tab('Tools->Magnify Search Page', 'Step10', 'Search Results:')
        search_result_css = "div input:not([type*='hidden'])"
        utillobj.synchronize_with_number_of_element(search_result_css, 2, medium_wait)        
            
        title= 'Search Results:';search_results_image= 'search_results_century.png';step_no='Step10.1'
        verify_title_and_tabs(title, step_no, expected_image=search_results_image)
            
        search_text_box_css = "input[placeholder='Type your search term here']"
        utillobj.verify_object_visible(search_text_box_css, True, "Step10.2: Verify search_text_box object is displaying")
            
        collection_list_box_css = "select#site>option[value='default_collection']"
        verify_htmltag_text(collection_list_box_css, "Century Electronics KB", "Step10.3: Verify Collection list box listed as drop down.")
            
        search_button_css=self.driver.find_element_by_css_selector("input[name][type='submit']")
        search_button = utillobj.get_element_attribute(search_button_css, 'value')
        utillobj.asequal("Search", search_button, "Step10.4: Verify Search button")
            
        verify_btn_css="html input[name='btnG']";text_css="html #sf span:nth-child(1)"
        utillobj.verify_popup(verify_btn_css,'Step10.5a: Verify Magnify Search Page displays Results Per Page', popup_text_css=text_css, popup_text="Results Per Page")        
        results_per_page_num_css = "span>select>option[selected]"
        verify_htmltag_text(results_per_page_num_css, "10", "Step10.5b: Verify no. of pages as drop down")
            
        advance_search_css = "[title*='advance'][title*='search'][href], [title*='Advanced'][title*='Search'][href]"
        verify_htmltag_text(advance_search_css, "Advanced Search", "Step10.6a: Verify Advanced Search text and hyperlink")
        verify_htmltag_property(advance_search_css, 'text-decoration','underline', "Step06.6b: Verify Advanced Search  text underline")
        verify_color(advance_search_css, 'hyper_link_blue', "Step10.6b: Verify Advanced Search text color")
            
        sign_out_css = "[title='Sign Out'][href]"
        verify_htmltag_text(sign_out_css, "Sign Out", "Step10.7a: Verify Sign Out text and hyperlink")
        verify_htmltag_property(sign_out_css, 'text-decoration','underline', "Step10.7b: Verify Sign Out text underline")
        verify_color(sign_out_css, 'hyper_link_blue', "Step10.7c: Verify Sign Out text color")
            
        verify_btn_css="html a[title='Go to Magnify Search Home']";text_css="html #ddd > table > tbody > tr > td:nth-child(2) > div > b"
        utillobj.verify_popup(verify_btn_css,'Step10.8: Verify the element Search Tips is Visible as expected.', popup_text_css=text_css, popup_text="Search Tips")
            
        """
        Step11: Close "Search Results:" tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
           
        """
        Step12: In the banner link, click on the top right username > Preferences.
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
            
        title= 'WebFOCUS Home Page'; step_no='Step12'; text_css="[class*='dialog-main-box'] [class*='ibx-label'][class*='label-text']"
        stop_request_tab_list= ['My Preferences', 'Display', 'Title', 'Name', 'Language', 'Reset preferences', 'OK', 'Cancel']
         
        verify_title_and_tabs(title, step_no, expected_tab_list=stop_request_tab_list, css=preferences_dialog_css)
           
        background_css = "[class*='ibx-popup-glass-pane']"
        actual_background_layer = self.driver.find_element_by_css_selector(background_css).value_of_css_property('opacity')
        utillobj.asequal("0.5", str(actual_background_layer), "Step12: Verify background gray layer when preferences dialog opens")
           
        """
        Step13: Close Preferences dialog box.
        """
        close_button_ele = self.driver.find_element_by_css_selector("[class*='dialog-main-box'] [class*='close-button']")
        core_utilobj.left_click(close_button_ele)
          
        """
        Step14: In the banner link, click on the top right username > Help > click Information Center.
        Verify WebFOCUS Information Center opens in a new tab with following options:
        1.Learn.
        2.Connect.
        3.Technical Support.
        """
        select_and_verify_new_tab('Help->Information Center', 'Step14', 'WebFOCUS Release*')
        verify_title_and_tabs('Information Center', "Step14.2")
          
        bth_css = self.driver.find_elements_by_css_selector("[class*='col-md-4'] [class*='h3']")
        actual_text_items=[e.text for e in bth_css if e!='']
        expected_list = ['Learn', 'Connect', 'Technical Support']
        utillobj.as_List_equal(expected_list, actual_text_items, "Step14.3: Verify Learn, Connect, Technical Support in Information Center")
          
        """
        Step15: Close Information Center tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
          
        """
        Step16: In the banner link, click on the top right username > Help > click VideoAssist.
        Verify a new tab should opens with links to informational videos.
        """
        select_and_verify_new_tab('Help->VideoAssist', 'Step16', 'Videos')
        verify_title_and_tabs('Videos', "Step16.1c")
          
        videos = self.driver.find_elements_by_css_selector("[href*='.mp4']")
        utillobj.as_LE(207,len(videos),"Step16.2: Verify .mp4 video files in VideoAssist page")
          
        """
        Step17: Close VideoAssist tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
          
        """
        Step18: In the banner link, click on the top right username > Help > click Technical Library.
        Verify WebFOCUS Technical Content opens in a new tab.
        """
        select_and_verify_new_tab('Help->Technical Library', 'Step18', '*Technical Content*', control_type='tab1')
        verify_title_and_tabs('Technical Content', "Step18.1c")
          
        verify_btn_css="html #magnify-search-2 button"
        utillobj.verify_popup(verify_btn_css,'Ste18.2a: Verify Technical Content' , popup_text_css="html h1", popup_text="Technical Content")
          
        """
        Step19: Close WebFOCUS Technical Content tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
          
        """
        Step20: In the banner link, click on the top right username > Help > click Community.
        Verify a new tab should opens with links to different Information Builders Communities.
        """
        select_and_verify_new_tab('Help->Community', 'Step20', 'Information Builders Community | Information Builders')
        verify_title_and_tabs('Information Builders Community | Information Builders', "Step20")
          
        hyper_link = self.driver.find_elements_by_css_selector("[class*='columns small-12'] [href]")
        utillobj.as_GE(40,len(hyper_link),"Step20.2: Verify hyper link references in Community page")
          
          
        """
        Step21: Close Information Builders Communities tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
          
        """
        Step22: In the banner link, click on the top right username > Help > click Information Builders Home.
        Verify Business Intelligence and Data Management Software opens in a new tab.
        """
        select_and_verify_new_tab('Help->Information Builders Home', 'Step22', 'Business Intelligence and Data Management Software*')
        verify_title_and_tabs('Business Intelligence and Data Management Software | Information Builders', "Step22.1")
          
          
        """
        Step23: Close Business Intelligence and Data Management Software tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
          
        """
        Step24: In the banner link, click on the top right username > Help > click About WebFOCUS.
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
        utillobj.asequal("About WebFOCUS", self.driver.find_element_by_css_selector(about_css).text, "Step24: Verify dialog title")
          
        left_panel_css ="[class*='dialog-main-box'] [class*='left-panel'] [class*='ibx-label'][class*='label-text']"
        left_panel_items = self.driver.find_elements_by_css_selector(left_panel_css)
        actual_left_panel_items=[e.text for e in left_panel_items if e!='']
        expected_left = ['Edition', 'Product release', 'Service pack', 'Package name', 'Release ID', 'Build/GEN number', 'Build/GEN date', 'Application Server']
        utillobj.as_List_equal(expected_left, actual_left_panel_items, "Step24.1: Verify About dialog left menu")
          
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
            utillobj.asequal(True, status, "Step24.2: Verify About page gen information verification.") 
           
        background_css = "[class*='ibx-popup-glass-pane']"
        actual_background_layer = self.driver.find_element_by_css_selector(background_css).value_of_css_property('opacity')
        utillobj.asequal("0.5", str(actual_background_layer), "Step24.3: Verify background gray layer when About WebFOCUS dialog opens")
           
        """
        step25: Click OK button to close "About WebFOCUS" dialog box.
        """
        close_button_ele = self.driver.find_element_by_css_selector("[class*='dialog-main-box'] [class*='close-button']")
        core_utilobj.left_click(close_button_ele)
          
        """
        Step26: In the banner link, click on the top right username > Help > click Licenses.
        Verify 3rd Party Information opens in a new tab with a list of licenses.
        """
        select_and_verify_new_tab('Help->Licenses', 'Step26.1', '3rd Party Information')
        verify_title_and_tabs('3rd Party Information', "Step26.2")
          
        Party_header_css="table td.console-header span"
        Party_header_elems = self.driver.find_elements_by_css_selector(Party_header_css)
        actual_item = [elem for elem in [elem.text.strip() for elem in Party_header_elems if elem != ''] if elem != '']
        expected_item = ['Description', 'Version', 'File(s)', 'Licenses', 'Third Party Links', 'Release', 'Update History', 'Date']
        utillobj.as_List_equal(expected_item, actual_item, "Step26.3: Verify labels in 3rd Party Information")
          
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
            utillobj.asequal(True, status_, "Step26.4: Verify 3rd Party Information verification.") 
        else:
            utillobj.asin('Apache', acutal_info, "Step26.5: Verify 3rd Party Information verification.")
          
        """
        Step27: Close 3rd Party Information tab.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
          
        """
        Step28: In the banner link, click on the top right username > Legacy Home Page.
        Verify WebFOCUS Legacy Home opens in a new tab.
        """
        select_and_verify_new_tab('Legacy Home Page', 'Step28.1', 'WebFOCUS Legacy Home')
        verify_title_and_tabs('WebFOCUS Legacy Home', "Step28.2")
          
        domain_img_css = "[src*='discovery_domain']"
        utillobj.verify_object_visible(domain_img_css, True, "Step28.3: Verify domain image object is displaying")
          
        """
        Step29: Close WebFOCUS Legacy Home.
        """
        core_utilobj.switch_to_previous_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        utillobj.synchronize_with_number_of_element(folders_css, 1, medium_wait)
         
        """
        Step30: In the banner link, click on the top right username > Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()        