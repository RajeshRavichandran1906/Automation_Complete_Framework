'''
Created on Aug 28, 2019

@author: Vishnu_priya
Test case : Context Menu:Verify Homepage Context menu for Reporting Object item as Advanced User.
Test rail : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9925893
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators

class C9925893_TestClass(BaseTestCase):

    def test_C9925893(self):
        
        """
        TESTCASE VARIABLES
        """

        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        locatorsobj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        Step 01: Sign into WebFOCUS Home Page as Admin User.
        """
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(locatorsobj.CONTENT_CSS, 1, wfmain_obj.home_page_long_timesleep)
        
        """
        Step 02: Under Domain tree >> Navigate to 'P292_S10660' domain >> G671733 >> Click on folder ReportingObject.
        """
        wfmain_obj.click_repository_folder('Domains')
        wfmain_obj.expand_repository_folder('Domains->P292_S10660')
        utillobj.synchronize_with_visble_text('#files-box-area', 'G671733', wfmain_obj.home_page_long_timesleep)
        wfmain_obj.expand_repository_folder('Domains->P292_S10660->G671733')
        utillobj.synchronize_with_visble_text('#files-box-area', 'ReportingObject', wfmain_obj.home_page_long_timesleep)
        wfmain_obj.double_click_on_content_area_items('ReportingObject')
        utillobj.synchronize_with_visble_text("div.files-box-files", "ReportingObject_Context", 30)
        
        """
        Step 03 : Right click on ReportingObject_Context
        """
        expected_context_menu = ['Copy Ctrl+C', 'open_in_new New', 'Properties']
        wfmain_obj.verify_repository_folder_item_context_menu('ReportingObject_Context', expected_context_menu, msg="Step 03.01")
        banner_area_elem = utillobj.validate_and_get_webdriver_object('.banner-group-spacer', 'banner area')
        core_utils.left_click(banner_area_elem) 
        wfmain_obj.verify_repository_folder_item_context_submenu('ReportingObject_Context', 'New', ['Designer', 'InfoAssist'], msg='Step 03.04')
        wfmain_obj.verify_repository_folder_item_context_submenu('ReportingObject_Context', 'New->Designer', ['Workbook', 'Chart', 'Report'], msg='Step 03.05')
        wfmain_obj.verify_repository_folder_item_context_submenu('ReportingObject_Context', 'New->InfoAssist',['Report', 'Chart', 'Document'], msg='Step 03.06')
        
        """
        Step 04 : In the banner link, click on the top right username > Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
                
if __name__ == '__main__':
    unittest.main()  