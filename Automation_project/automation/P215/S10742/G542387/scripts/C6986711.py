'''
Created on Oct 24, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6986711&group_by=cases:section_id&group_order=asc&group_id=542387
Testcase Name : Verify the pages under Retail Samples Resources
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators


class C6986711_TestClass(BaseTestCase):

    def test_C6986711(self):
        
        """
            CLASS OBJECTS 
        """
        
        wf_login = login.Login(self.driver)
        wf_home = wf_mainpage.Wf_Mainpage(self.driver)
        utill=utillity.UtillityMethods(self.driver)
        locator_obj = WfMainPageLocators()

        
        """ 
            VARIABLES
        """
        USERNAME='mrdevid'
        PASSWORD='mrdevpass'
        
        EXPECTED_LIST=['Sales Dashboard', 'Workbench', 'My Page']
        HIDDEN_FOLDER_NAME='Retail Samples Resources'
        FOLDER_PATH='Domains->Retail Samples->Portal'
        MEDIUM_WAIT=190
        
        """ 
            CSS 
        """
        NO_OF_ITEMS_CSS=".content-box.ibx-widget .files-box .file-item .ibx-label-text"
        
        """
            Step 1:Sign to WebFocus using 'rsdev' user
            http://machine:port/ibi_apps
        """
        wf_login.invoke_home_page(USERNAME, PASSWORD)
         
        """
            Step 2:Expand Retail Samples => Portal
            Verify the "Retail Samples Resources" folder is hidden by default
        """
        utill.synchronize_with_number_of_element(locator_obj.PORTAL_ICON_CSS, 1, MEDIUM_WAIT)
        wf_home.expand_repository_folder(FOLDER_PATH)
        wf_home.verify_hidden_repository_folder(HIDDEN_FOLDER_NAME,"Step 02: Verify Retail Samples Resources are hidden")
        
        """
            Step 3:Click Retail Samples Resources
            Verify the following pages are available
        """
        wf_home.click_repository_folder(HIDDEN_FOLDER_NAME)
        utill.synchronize_with_visble_text(locator_obj.content_area_css, "Workbench", MEDIUM_WAIT)
        wf_home.verify_items_in_grid_view(EXPECTED_LIST, 'asin', "Step 03: Verify Retail Samples Resources")
        
        """
            Step 4:Logout:
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()