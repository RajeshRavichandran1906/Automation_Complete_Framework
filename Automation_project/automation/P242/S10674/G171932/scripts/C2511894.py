'''
Created on 02 July, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2511894
TestCase Name = Properties:Favorites-Cannot save any changes,script error
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity


class C2511894_TestClass(BaseTestCase):

    def test_C2511894(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        proj_sub_folder="Retail Samples->Reports"
        proj_sub_folder_item='Sales Metrics YTD'
        favorites_crum_css=".right-main-panel .crumb-box .ibx-label-text"
        property_dialog_css='.properties-page.propPage'
        context_menu='Add to Favorites'
        
        """ Step 1: Login to WebFOCUS as a Developer.
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content from side bar.
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Open Retail Sample/Reports
        """
        """ Step 4: Right click Sales Metrics YTD and select Add to Favorites
        """
        wf_mainobj.select_repository_folder_item_context_menu(proj_sub_folder_item, context_menu_item_path=context_menu, folder_path=proj_sub_folder)
        time.sleep(9)
        
        """ Step 5: Select Favorites in sidebar
        """
        wf_mainobj.select_left_panel('Favorites')
        utillobj.synchronize_with_visble_text(favorites_crum_css, 'Favorites', 190)
        
        """ Step 6: Right click Sales Metrics YTD and select Properties
        """
        wf_mainobj.select_repository_folder_item_context_menu(proj_sub_folder_item, context_menu_item_path='Properties')
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        
        """ Step 7: Change the Title
                    Save
                    Verify no error occurs
        """
        wf_mainobj.edit_property_dialog_value('Title', 'text_value', "Sales Metrics YTD Title")
        wf_mainobj.select_property_dialog_save_cancel_button('Save')
        wf_mainobj.verify_property_dialog_value('Title', 'text_value', "Step 7: Verify no error occurs.", property_value="Sales Metrics YTD Title")
        
        """ Step 8: Close Properties panel
        """
        wf_mainobj.close_property_dialog()
        
        """ Step 9: Reopen Properties panel
                    Verify Title was changed.
        """
        wf_mainobj.select_repository_folder_item_context_menu(proj_sub_folder_item+' Title', context_menu_item_path='Properties')
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        wf_mainobj.verify_property_dialog_value('Title', 'text_value', "Step 9: Verify Title was changed.", property_value="Sales Metrics YTD Title")
        
        """ Step 10: Close Properties panel
        """
        wf_mainobj.close_property_dialog()
        
        """ Step 11: Sign out
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()