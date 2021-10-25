'''
Created on May 07, 2019

@author: Niranjan

http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5857317
TestCase Name = Upload ely file
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.wftools import wf_mainpage
from common.wftools import login
from common.locators import wf_mainpage_locators
from common.lib import base

class C5857317_TestClass(BaseTestCase):

    def test_C5857317(self):
        
        """
        TESTCASE OBJECTS
        """
        util_obj = utillity.UtillityMethods(self.driver)
        main_page_obj =wf_mainpage.Wf_Mainpage(self.driver)
        login_obj = login.Login(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        
        """
        TESTCASE CSS
        """
        
        """
        TESTCASE VARIABLES
        """
        
        """
        Step 01:01: Login WF as domain developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 02:01: Click on Content View from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 03:01: Click on 'P292_S11397' > 'G436044' folder
        """
        main_page_obj.expand_repository_folder('P292_S11397->G436044')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Other',base_obj.home_page_medium_timesleep)
        
        """
        Step 04:01: Click Others category and click on "Upload file" action tile.
        Verify Open dialog display
        """
        main_page_obj.select_action_bar_tab("Other")
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Upload File',base_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Upload File')
        
        """
        Step 05:01: Navigate to "\ibirisc2\bipgqashare\Images_and_Things" > select "ImageObject.ely" file
        Verify "ImageObject.ely" file is selected
        """

        """
        Step 06:01: Click on Open button
        Verify "Upload completed" message displays as below
        """
        main_page_obj.upload_file_using_action_bar(["ImageObject.ely"])
        main_page_obj.verify_upload_message("ImageObject.ely", "ImageObject.ely Upload completed", "Step 06.01: Verify upload message")
        
        """
        Step 07.01 : Click "X" in the message displayed
        Verify "ImageObject.ely" file appears in content area
        """
        main_page_obj.click_button_on_popup_dialog("Close")
        main_page_obj.verify_items_in_grid_view(['ImageObject'], 'asin', 'Step 07.01 : Verify that the file ImageObject.ely.zip have been uploaded')
        
        """
        Step 08.01: Sign out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()

if __name__ == "__main__":
    unittest.main()
        
        
        