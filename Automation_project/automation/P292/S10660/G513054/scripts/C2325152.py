'''
Created on Nov 21, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2325152
Testcase Name : Search folder - mixed case
'''
import unittest
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.locators import wf_mainpage_locators
import time

class C2325152_TestClass(BaseTestCase):

    def test_C2325152(self):
        
        """
            CLASS OBJECTS
        """
        wf_login=login.Login(self.driver)
        wf_mainpage_o=wf_mainpage.Wf_Mainpage(self.driver)
        utill_o=utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
            TESTCASE VARIABLE
        """
        folder_name_path="P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples->Visualizations"
        long_wait=120
        
        """
            Step 1:Sign in to WebFOCUS as Developer User.
        """
        wf_login.invoke_home_page('mriddev', 'mrpassdev') 
             
        """ 
            Step 2:Click on the Content tree from the sidebar.
        """ 
        
        wf_mainpage_o.select_content_from_sidebar()   
        time.sleep(10)
             
        """ 
            Step 3:Expand Domain > P292_S10660>G169261>Breadcrumb Trail and Search>Retail Samples > Click on "Visualizations" from the tree
        """
        wf_mainpage_o.select_option_from_crumb_box("Workspaces")
        wf_mainpage_o.expand_repository_folder(folder_name_path)
        utill_o.synchronize_with_number_of_element(locator_obj.files_item_css, 4, long_wait)
             
        """ 
            Step 4:Click on the search text box and type 'DaSh' in the search box.
            Verify two reports (Analytical Dashboard and Executive Dashboard) are appears
        """
        wf_mainpage_o.search_input_box_options(input_text_msg='DaSh') 
        utill_o.synchronize_with_number_of_element(locator_obj.files_item_css, 2, long_wait)
        wf_mainpage_o.verify_file_item_grid_view('Analytical Dashboard', 'Executive Dashboard', "Step 4:Verify file item")
            
        """ 
            Step 5:If it is chrome, IE 11 and Edge browsers, Hover over the mouse to the search box
            Step 6:Click X to clear the search box
            Verify search box is cleared and "Search Visualizations" appears in the box
            Step 7:Or else for FF browser, use the backspace to clear the search box
            Verify search box is cleared and "Search Visualizations" appears in the box
        """ 
        wf_mainpage_o.search_input_box_options(option_type = 'clear') 
         
        wf_mainpage_o.verify_search_textbox_value("Search Visualizations", "Step 5: Verify place holder value shows Sear Visualizations")
            
            
        """ 
            Step 8:In the banner link, click on the top right username > Sign out.
        """
        
        wf_mainpage_o.signout_from_username_dropdown_menu()


if __name__ == "__main__":
    unittest.main()