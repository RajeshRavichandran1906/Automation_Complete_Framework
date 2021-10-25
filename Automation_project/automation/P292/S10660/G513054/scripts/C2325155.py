'''
Created on Nov 22, 2018

@author: KK14897
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2325155
Testcase Name : Run report from search results
'''
import unittest
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.locators import wf_mainpage_locators

class C2325155_TestClass(BaseTestCase):

    def test_C2325155(self):
        
        """
            CLASS OBJECTS
        """
        wf_login=login.Login(self.driver)
        wf_mainpage_o=wf_mainpage.Wf_Mainpage(self.driver)
        utill_o=utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        content_items = ['Brand Pie', 'Pie Chart', 'Pie Matrix - Quantity By Region','Pie Matrix - Quantity By Region']
        
        """
            TESTCASE VARIABLE
        """
        folder_name_path="P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples->Visualizations"
        long_wait=120
        
        """
            Step 1: Sign in to WebFOCUS as Developer User.
        """
        wf_login.invoke_home_page('mriddev', 'mrpassdev')
        
        """
            Step 2: Click on the Content tree from the sidebar.
        """
        wf_mainpage_o.select_content_from_sidebar()
        
        """
            Step 3: Expand Domain > P292_S10660>G169261>Breadcrumb Trail and Search>Retail Samples >Visualizations" from the tree
        """
        wf_mainpage_o.select_option_from_crumb_box("Workspaces")
        wf_mainpage_o.expand_repository_folder(folder_name_path)
        utill_o.synchronize_with_number_of_element(locator_obj.files_item_css, 4, long_wait)
        
        """
            Step 4 : Type 'x' in the search box
        """
        wf_mainpage_o.search_input_box_options(input_text_msg='x')
        
        """
            Step 5 : Click on list toggle button to switch to list view
        """
        wf_mainpage_o.select_list_view()
        
        """
            Step 6 : Double click Executive Dashboard
        """
        click_ele=self.driver.find_element_by_css_selector('#files-box-files-area [class*="ibx-label-text"]')
        utill_o.default_click(click_ele, click_option=2)
        utill_o.synchronize_with_visble_text(".output-area-label .ibx-label-text", 'Executive Dashboard', long_wait)
        
        """
            Step 7 : Click X to close the run window
        """
        wf_mainpage_o.close_view_dialog("Executive Dashboard")
       
        """
            Step 8 : Click on gid toggle button to switch to grid view
        """
        wf_mainpage_o.select_grid_view()
        
        
        """
        Step 9: If it is chrome, IE 11 and Edge browsers, Hover over the mouse to the search box
        Step 10: Or else for FF browser, use the backspace to clear the search box
        Verify search box is cleared and "Search Visualizations" appears in the box
        """
        wf_mainpage_o.search_input_box_options(option_type ='clear')
        wf_mainpage_o.verify_items_in_grid_view(content_items, 'asnotin', 'Step 5.2: Verify items not present in Content area')
        
        """
            Step 11 : In the banner link, click on the top right username > Sign out.
        """
        wf_mainpage_o.signout_from_username_dropdown_menu()


if __name__ == "__main__":
    unittest.main()