'''
Created on November 22, 2018

@author: varun
Testcase Name : Search folder - lower and upper case
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325163
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity

class C2325163_TestClass(BaseTestCase):
    
    def test_C2325163(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        content_css = "[title='Content view']"
        domains_css = ".left-pane .ibfs-label .ibx-label-text"
        content_items = ['Analytical Dashboard','Executive Dashboard']
        expected_placeholder_text = "Search Visualizations"
        items_css = ".file-item"
        
        """ 
        Step 1: Sign in to WebFOCUS as Basic User.
        """
        login_obj.invoke_home_page('mridbas', 'mrpassbas')
        util_obj.synchronize_with_number_of_element(content_css, 1, 190)
        
        """ 
        Step 2: Click on the Content tree from the sidebar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(domains_css, 'Workspaces', 160)
        
        """
        Step 3: Expand Domain > P292_S10660>G169261>Breadcrumb Trail and Search>Retail Samples > 
        Click on "Visualizations" from the tree
        """
        main_page_obj.expand_repository_folder("Domains->P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples->Visualizations")

        """
        Step 4: Click on the search text box and type 'dash' in the search box.
        Verify two reports (Analytical Dashboard and Executive Dashboard) are appears
        """
        main_page_obj.search_input_box_options(input_text_msg='dash')
        util_obj.synchronize_with_number_of_element(items_css, 2, 60)
        main_page_obj.verify_items_in_grid_view(content_items, 'asequal', 'Step 4.1: Verify items present in Content area ')
                
        """
        Step 5: If it is chrome, IE 11 and Edge browsers, Hover over the mouse to the search box
        Step 6: Click X to clear the search box
        Step 7: Or else for FF browser, use the backspace to clear the search box
        Verify search box is cleared and "Search Visualizations" appears in the box
        """
        main_page_obj.search_input_box_options(option_type ='clear')
        main_page_obj.verify_search_textbox_value(expected_placeholder_text, "Step 5.1: Verify Placeholder in searchbox")
        
        """
        Step 8: In the banner link, click on the top right username > Sign out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()