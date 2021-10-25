"""-------------------------------------------------------------------------------------------
Created on June 24, 2019
@author: Niranjan/Rajesh

Test Case Link  =  http://172.19.2.180/testrail/index.php?/tests/view/22062765
Test Case Title =  Check Defaults
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer
from common.wftools import wf_mainpage

class C6424216_TestClass(BaseTestCase):

    def test_C6424216(self):
        
        """
            CLASS OBJECTS 
        """
        pd_design=page_designer.Design(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        TEMPLATE_NAME='Blank'

        """
            STEP 1 : Login WF as domain developer
            STEP 2 : Click on Content view from side bar
            STEP 3 : Expand 'P292_S11397' domain;
            Click on 'G470366' folder and click on 'page' action tile from under Designer category
            STEP 4 : Choose blank template
        """
        pd_design.invoke_page_designer_and_select_template(TEMPLATE_NAME)
              
        """
            STEP 5 : From Content tab, open Repository Widgets
        """
        pd_design.expand_and_collapse_content_tab("collapse")
        pd_design.expand_and_collapse_repository_widgets_tab("expand")
        
        """
            STEP 05.01 : Verify Explorer Widget is available as below
        """
        msg = "Step 5.01 : Verify Explorer Widget is available as below"
        pd_design.verify_repository_widgets_items_text(["Explorer"], msg, assert_type="asin")
        
        """
            STEP 6 : Close the Page Designer from application menu without saving.
        """
        pd_design.close_page_designer_without_save_page()
        pd_design.switch_to_previous_window(driver_close=False)
        
        """
            STEP 7 : In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main() 