'''
Created on Aug 29, 2019

@author: Niranjan 
Test case : Context Menu:Verify Homepage Context menu for Reporting Object item as Developer.
Test rail : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9925885
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators

class C9925885_TestClass(BaseTestCase):

    def test_C9925885(self):
        
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
        Step 01: Sign into WebFOCUS Home Page as Developer User.
        """
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 02: Under Domain tree >> Navigate to 'P292_S10660' domain >> G671733 >> Click on folder ReportingObject.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(locatorsobj.REPOSITORY_TREE_CSS,1, wfmain_obj.home_page_long_timesleep)
        wfmain_obj.click_repository_folder('Domains')
        wfmain_obj.expand_repository_folder('Domains->P292_S10660')
        utillobj.synchronize_with_visble_text('#files-box-area', 'G671733', wfmain_obj.home_page_long_timesleep)
        wfmain_obj.expand_repository_folder('Domains->P292_S10660->G671733')
        utillobj.synchronize_with_visble_text('#files-box-area', 'ReportingObject', wfmain_obj.home_page_long_timesleep)
        wfmain_obj.double_click_on_content_area_items('ReportingObject')
        
        """
        Step 03 : Right click on ReportingObject_Context
        Verify context menu,
        Run.
        Run (Run in new window/Run deferred).
        Edit.
        Duplicate.
        Cut.
        Copy.
        Create Shortcut.
        Delete.
        New (Designer[Workbook/Chart/Report], InfoAssist[Report/Chart/Document]).
        Add to Favorites.
        Unpublish/Publish.
        Hide/Show.
        Security (Rules on this resource/Effective Policy/Owner).
        Properties.
        """
        expected_context_menu = ['Run', 'Run...', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'open_in_new New', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        wfmain_obj.verify_repository_folder_item_context_menu('ReportingObject_Context', expected_context_menu, msg="Step 03.01")
        leftpanel_elem = utillobj.validate_and_get_webdriver_object('.main-panel .left-main-panel', 'left panel')
        core_utils.left_click(leftpanel_elem) 
        wfmain_obj.verify_repository_folder_item_context_submenu('ReportingObject_Context', 'New', ['Designer', 'InfoAssist'], msg='Step 03.02')
        wfmain_obj.verify_repository_folder_item_context_submenu('ReportingObject_Context', 'New->Designer', ['Workbook', 'Chart', 'Report'], msg='Step 03.03')
        wfmain_obj.verify_repository_folder_item_context_submenu('ReportingObject_Context', 'New->InfoAssist',['Report', 'Chart', 'Document'], msg='Step 03.04')
        wfmain_obj.verify_repository_folder_item_context_submenu('ReportingObject_Context', 'Run...',['Run in new window', 'Run deferred'], msg='Step 03.05')
        wfmain_obj.verify_repository_folder_item_context_submenu('ReportingObject_Context', 'Security',['Rules on this resource...', 'Effective policy...', 'Owner...'], msg='Step 03.06')
        
        """
        Step 04 : In the banner link, click on the top right username > Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
                
if __name__ == '__main__':
    unittest.main()  