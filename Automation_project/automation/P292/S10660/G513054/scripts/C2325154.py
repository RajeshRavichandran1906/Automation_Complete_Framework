'''
Created on Nov 22, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2325154
Testcase Name : Search folder in List View
'''
import unittest
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.locators import wf_mainpage_locators

class C2325154_TestClass(BaseTestCase):

    def test_C2325154(self):
        
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
        folder_name_path="P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples->InfoApps->Maps"
        long_wait=120
        
        """
            CSS
        """
        advanced_search_folder=".advanced-folder-search #SearchSelectOption"
        
        """
            Step 1: Sign in to WebFOCUS as Developer User.
        """
        wf_login.invoke_home_page('mriddev', 'mrpassdev')
        
        """
            Step 2: Click on the Content tree from the sidebar.
        """
        wf_mainpage_o.select_content_from_sidebar()
        
        """
            Step 3: Expand Domain > P292_S10660>G169261>Breadcrumb Trail and Search>Retail Samples >InfoApps>Click on "Maps" from the tree
        """
        wf_mainpage_o.select_option_from_crumb_box("Workspaces")
        wf_mainpage_o.expand_repository_folder(folder_name_path)
        utill_o.synchronize_with_number_of_element(locator_obj.files_item_css, 6, long_wait)
        
        """
            Step 4 : Click on the drop-down in the search text box
        """
        wf_mainpage_o.click_search_input_box_option_dropdown()
        utill_o.synchronize_with_number_of_element(advanced_search_folder, 1, long_wait)
        
        """
            Step 5 : Click on Search drop-down > Change Search by Name
        """
        wf_mainpage_o.search_dropdown_in_advanced_folder_search(select_options=['Name'])
        
        """
            Step 6 : Click on the search text box and Type *.htm in the Search box
        """
        utill_o.wait_for_page_loads(5, 3, 3)
        wf_mainpage_o.search_input_box_options(input_text_msg='*.htm')
        utill_o.synchronize_with_number_of_element(locator_obj.files_item_css, 1, long_wait) 
        
        """
            Verify only US Sales Map appears
        """
        wf_mainpage_o.verify_items_in_grid_view(['US Sales Map'], 'as_List_equal', msg="Step 06:01:Verify Maps folder has shown only US Sales Map")
        
        """
            Step 7 : Click on the list view toggle button to switch to list view
        """
        wf_mainpage_o.select_list_view()
       
        """
            Verify 'US Sales Map' appears in the list view.
        """
        wf_mainpage_o.verify_items_in_list_view(['US Sales Map'], 'as_List_equal', msg="Step 07:01:Verify Maps folder has shown only US Sales Map in list view")
        
        """
            Step 8 : Click on the grid view toggle button to switch to grid view
        """
        wf_mainpage_o.select_grid_view()
        
        """
            Verify 'US Sales Map' appears in the grid view.
        """
        wf_mainpage_o.verify_items_in_grid_view(['US Sales Map'], 'as_List_equal', msg="Step 08:01:Verify Maps folder has shown only US Sales Map")
        
        """
            Step 9 : Click on the drop-down in the search text box
        """
        wf_mainpage_o.click_search_input_box_option_dropdown()
        utill_o.synchronize_with_number_of_element(advanced_search_folder,1,long_wait)
        
        """
            Step 10 : Click on 'Reset' button
        """
        wf_mainpage_o.button_in_advanced_folder_search('Reset',select=True)
        
        """
            Verify that Search drop-down change by its default state as 'Title' and Search text box appears as "Search Maps"
        """
        wf_mainpage_o.search_dropdown_in_advanced_folder_search(verify_selected='Title', label_text='Search',step_number='08:01')
        wf_mainpage_o.verify_search_textbox_value('Search Maps', "Step 8:02 Verify search text box value has Search Maps")
        
        """
            Step 11 : In the banner link, click on the top right username > Sign out.
        """
        wf_mainpage_o.select_option_from_crumb_box("P292_S10660")# to revert the Breadcrumb to initial level
        wf_mainpage_o.signout_from_username_dropdown_menu()


if __name__ == "__main__":
    unittest.main()