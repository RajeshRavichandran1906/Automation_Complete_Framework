'''
Created on May 7, 2018

@author: Vpriya

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5857316&group_by=cases:section_id&group_id=436044&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5857316
TestCase Name = Upload zip file
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib import base

class C5857316_TestClass(BaseTestCase):

    def test_C5857316(self):
        
        """
        TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        
        """
        TESTCASE VARIABLES
        """
        devuser_username = 'mrid'
        devuser_password = 'mrpass'
        
        """
        Step 01:Login WF as domain developer
        """
        wftools_login_obj.invoke_home_page(devuser_username,devuser_password)
        """
        Step 02:Click on Content view from side bar
        """
        wfmain_obj.select_content_from_sidebar()
        
        """
        Step 03:Click on 'P292_S11397' > 'G436044' folder in resource tree.
        """
        utillobj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        wfmain_obj.expand_repository_folder('P292_S11397->G436044')
        utillobj.synchronize_with_visble_text(locator_obj.content_area_css, 'Other',base_obj.home_page_medium_timesleep)
        
        """
        Step 04:Click Others category and click on "Upload File" action tile.
        """
        wfmain_obj.select_action_bar_tab('Other')
        utillobj.synchronize_with_visble_text(locator_obj.content_area_css, 'Upload File',base_obj.home_page_medium_timesleep)
        wfmain_obj.select_action_bar_tabs_option('Upload File')
        time.sleep(9)
        
        """
        Step 05:Verify Open dialog appears
        Navigate to "\ibirisc2\bipgqashare\Images_and_Things" > select "Home_Thumbnail.zip" file
        """
        wfmain_obj.upload_file_using_action_bar(["Home_Thumbnail.zip"])
        utillobj.synchronize_with_visble_text(".pop-top", "Upload", wfmain_obj.home_page_long_timesleep)
        
        """
        Step 06:Verify "Home_Thumbnail.zip" file is selected.
        """
        """
        Click on Open button
        """
    
        """
        Step 07:Verify "Upload completed" message displays as below.
        """
        wfmain_obj.verify_upload_message("Home_Thumbnail.zip", "Home_Thumbnail.zip Upload completed", "Step 07: Verify upload message")
    
        """
        Click "X" in the message displayed.
        """
        wfmain_obj.click_button_on_popup_dialog("Close")
        utillobj.synchronize_with_visble_text(locator_obj.content_area_css, 'Home_Thumbnail',base_obj.home_page_medium_timesleep)
        
    
        """
        Step 08:Verify "Home_Thumbnail.zip" file appears in content area.
        """
        wfmain_obj.verify_items_in_grid_view(['Home_Thumbnail'], 'asin', 'Step 08 : Verify that the file Home_Thumbnail.zip have been uploaded')


        """
        Step09:Sign out WF
        """
        wfmain_obj.signout_from_username_dropdown_menu()   
        
if __name__ == '__main__':
    unittest.main()        