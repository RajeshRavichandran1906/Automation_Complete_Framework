'''
Created on April 11, 2019

@author: Varun

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8261523
TestCase Name = Browser tab icon for WF 
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login 
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261523_TestClass(BaseTestCase):

    def test_C8261523(self):
        """
        TESTCASE VARIABLES
        """
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        head_icon_css = "head link[rel='icon']"
        
        """ 
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        Verify WebFOCUS Home page opens in new tab with new logo
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, main_page_obj.home_page_long_timesleep)
        head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
        util_obj.asin('favicon.ico', head_icon_obj, "Step 1: Verify the new icon")
        
        """
        Step 2: Click Content View from the side bar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.wait_for_page_loads(main_page_obj.home_page_long_timesleep)
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.click_repository_folder('Retail Samples')
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 4: Click on Data category button ->Click on Upload Data action tile
        Verify web console open in new tab without the new logo
        """
        main_page_obj.select_action_bar_tab('Data')
        main_page_obj.select_action_bar_tabs_option('Upload Data')
        core_util_obj.switch_to_new_window()
        try:
            head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
            util_obj.asequal(False, True, 'Step 4.1: Failure in the icon')
        except:
            util_obj.asequal(True, True, 'Step 4.1: New icon is not present')
        
        """
        Step 5: Close the Web console tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 6: Click on Data category button ->Click on Connect action tile
        """
        main_page_obj.select_action_bar_tab('Data')
        main_page_obj.select_action_bar_tabs_option('Connect')
        core_util_obj.switch_to_new_window()
        try:
            head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
            util_obj.asequal(False, True, 'Step 6.1: Failure in the icon')
        except:
            util_obj.asequal(True, True, 'Step 6.1: New icon is not present')
        
        """
        Step 7: Close the Web console tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 8: Click on Data category button ->Click on Metadata action tile
        Verify web console open in new tab without the new logo
        """
        main_page_obj.select_action_bar_tab('Data')
        main_page_obj.select_action_bar_tabs_option('Metadata')
        core_util_obj.switch_to_new_window()
        try:
            head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
            util_obj.asequal(False, True, 'Step 8.1: Failure in the icon')
        except:
            util_obj.asequal(True, True, 'Step 8.1: New icon is not present')
            
        """
        Step 9: Close the Web console tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 10: Click on Data category button ->Click on ReportingObject action tile
        Verify ReportingObject open in new tab with the new logo
        """
        main_page_obj.select_action_bar_tab('Data')
        main_page_obj.select_action_bar_tabs_option('Reporting Object')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element("#dlgIbfsOpenFile7", 1, main_page_obj.home_page_medium_timesleep)
        head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
        util_obj.asin('favicon.ico', head_icon_obj, "Step 10: Verify the new icon")
        
        """
        Step 11: Close the ReportingObject tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 12: Click on Designer category button ->Click on Workbook select baseapp ->wf_retail_lite.mas
        Verify Workbook open in new tab with the new logo
        """
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Workbook')
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption ","Open", main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_crumb_item_from_resource_dialog('EDASERVE')
        main_page_obj.select_file_or_folder_from_resource_dialog('baseapp', selection_type='double')
        main_page_obj.select_file_or_folder_from_resource_dialog('wf_retail_lite.mas', selection_type='double')
        core_util_obj.switch_to_new_window()
        util_obj.wait_for_page_loads(main_page_obj.home_page_long_timesleep)
        util_obj.synchronize_with_number_of_element("div .id-main-box", 1, main_page_obj.home_page_long_timesleep)
        head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
        util_obj.asin('favicon.ico', head_icon_obj, "Step 12: Verify the new icon")
         
        """
        Step 13: Close the Workbook tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
         
        """
        Step 14: Click on Designer category button ->Click on Chart select baseapp ->wf_retail_lite.mas
        Verify Chart open in new tab with the new logo
        """
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Chart')
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption ","Open", main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_crumb_item_from_resource_dialog('EDASERVE')
        main_page_obj.select_file_or_folder_from_resource_dialog('baseapp', selection_type='double')
        main_page_obj.select_file_or_folder_from_resource_dialog('wf_retail_lite.mas', selection_type='double')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element("div[data-ibx-name=\"cmdAddToChart\"]", 1, main_page_obj.home_page_long_timesleep)
        head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
        util_obj.asin('favicon.ico', head_icon_obj, "Step 14: Verify the new icon")
         
        """
        Step 15: Close the Chart tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 16: Click on Designer category button ->Click on Page action tile
        Verify Page open in new tab with new logo
        """
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption", 'New Page', main_page_obj.home_page_medium_timesleep)
        head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
        util_obj.asin('favicon.ico', head_icon_obj, "Step 16: Verify the new icon")
        
        """
        Step 17: Close the Page tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 18: Click on InfoAssist category button ->Click on Chart action tile
        Verify WebFOCUSInfoAssist open in new tab with the new logo
        """
        main_page_obj.select_action_bar_tab('InfoAssist')
        main_page_obj.select_action_bar_tabs_option('Chart')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element("#dlgIbfsOpenFile7", 1, main_page_obj.home_page_medium_timesleep)
        head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
        util_obj.asin('favicon.ico', head_icon_obj, "Step 18: Verify the new icon")
        
        """
        Step 19: Close the WebFOCUSInfoAssist tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 20: Click on InfoAssist category button ->Click on Visualization action tile
        Verify WebFOCUSInfoAssist open in new tab with the new logo
        """
        main_page_obj.select_action_bar_tab('InfoAssist')
        main_page_obj.select_action_bar_tabs_option('Visualization')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element("#dlgIbfsOpenFile7", 1, main_page_obj.home_page_medium_timesleep)
        head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
        util_obj.asin('favicon.ico', head_icon_obj, "Step 20: Verify the new icon")
        
        """
        Step 21: Close the WebFOCUSInfoAssist tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 22: Click on InfoAssist category button ->Click on Report action tile
        Verify WebFOCUSInfoAssist open in new tab with the new logo
        """
        main_page_obj.select_action_bar_tab('InfoAssist')
        main_page_obj.select_action_bar_tabs_option('Report')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element("#dlgIbfsOpenFile7", 1, main_page_obj.home_page_medium_timesleep)
        head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
        util_obj.asin('favicon.ico', head_icon_obj, "Step 22: Verify the new icon")
        
        """
        Step 23: Close the WebFOCUSInfoAssist tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 24: Click on InfoAssist category button ->Click on Document action tile
        Verify WebFOCUSInfoAssist open in new tab with the new logo
        """
        main_page_obj.select_action_bar_tab('InfoAssist')
        main_page_obj.select_action_bar_tabs_option('Document')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element("#dlgIbfsOpenFile7", 1, main_page_obj.home_page_medium_timesleep)
        head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
        util_obj.asin('favicon.ico', head_icon_obj, "Step 24: Verify the new icon")
        
        """
        Step 25: Close the WebFOCUSInfoAssist tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 26: Click on InfoAssist category button ->Click on Alert action tile
        Verify Alert-WebFOCUSAlertAssist open in new tab with the new logo
        """
        main_page_obj.select_action_bar_tab('InfoAssist')
        main_page_obj.select_action_bar_tabs_option('Alert')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element("#AARibbon", 1, main_page_obj.home_page_medium_timesleep)
        head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
        util_obj.asin('favicon.ico', head_icon_obj, "Step 26: Verify the new icon")
        
        """
        Step 27: Close the Alert-WebFOCUSAlertAssist tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 28: Click on Schedule category button ->Click on Access List action tile
        Verify Untitled-Library Access List open in new tab with the new logo
        """
        main_page_obj.select_action_bar_tab('Schedule')
        main_page_obj.select_action_bar_tabs_option('Access List')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element("#AccessListEditor_ribbonTabPane", 1, main_page_obj.home_page_medium_timesleep)
        head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
        util_obj.asin('favicon.ico', head_icon_obj, "Step 28: Verify the new icon")
        
        """
        Step 29: Close the Untitled-Library Access List tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 30: Click on Schedule category button ->Click on Distribution List action tile
        Verify Untitled-Distribution List open in new tab with the new logo
        """
        main_page_obj.select_action_bar_tab('Schedule')
        main_page_obj.select_action_bar_tabs_option('Distribution List')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element("#AddrbookEditor_tabPage", 1, main_page_obj.home_page_medium_timesleep)
        head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
        util_obj.asin('favicon.ico', head_icon_obj, "Step 30: Verify the new icon")
        
        """
        Step 31: Close the Untitled-Distribution List tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 32: Click on Schedule category button ->Click on Schedule action tile
        Verify Untitled-Schedule open in new tab with the new logo
        """
        main_page_obj.select_action_bar_tab('Schedule')
        main_page_obj.select_action_bar_tabs_option('Schedule')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element("#ScheduleEditor_ribbonTabPane", 1, main_page_obj.home_page_medium_timesleep)
        head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
        util_obj.asin('favicon.ico', head_icon_obj, "Step 32: Verify the new icon")
        
        """
        Step 33: Close the Untitled-Schedule tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 34: Click on Other category button ->Click on Text Editor action tile and select fex
        Verify Editor open in new tab with the new logo
        """
        main_page_obj.select_action_bar_tab('Other')
        main_page_obj.select_action_bar_tabs_option('Text Editor')
        util_obj.synchronize_with_number_of_element("div[data-ibxp-user-value=\"fex\"]", 1, main_page_obj.home_page_medium_timesleep)
        fex_obj = util_obj.validate_and_get_webdriver_object("div[data-ibxp-user-value=\"fex\"]", 'fex')
        core_util_obj.left_click(fex_obj)
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(".te-menu-bar", 1, main_page_obj.home_page_medium_timesleep)
        head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
        util_obj.asin('favicon.ico', head_icon_obj, "Step 34: Verify the new icon")
        
        """
        Step 35: Close the Editor tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 36: Click on Other category button ->Click on Portal page action tile
        Verify Page Designer open in new tab with the new logo
        """
        main_page_obj.select_action_bar_tab('Other')
        main_page_obj.select_action_bar_tabs_option('Portal Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element("#dlgTitleExplorer", 1, main_page_obj.home_page_medium_timesleep)
        head_icon_obj = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(head_icon_css, 'icon'), 'href')
        util_obj.asin('favicon.ico', head_icon_obj, "Step 36: Verify the new icon")
        
        """
        Step 37: Close the Page Designer tab
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 38: Sign out WebFocus.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
        