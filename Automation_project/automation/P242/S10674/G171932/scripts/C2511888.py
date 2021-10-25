'''
Created on 28 June, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2511888
TestCase Name = Truncated Properties window after clearing Search box and Cancel in Properties
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity, core_utility
from selenium.common.exceptions import NoSuchElementException


class C2511888_TestClass(BaseTestCase):

    def test_C2511888(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        proj_sub_folder="Retail Samples->Reports"
        proj_sub_folder_item='Sales Metrics YTD'
        property_dialog_css='.properties-page.propPage'
        search_box_css=".div-search .txt-search input"
        search_box_string='M'
        
        """ Step 1: Login to WebFOCUS as a Developer.
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content from side bar.
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Open Retail Samples / Reports
                    Open properties of any report
        """
        wf_mainobj.select_repository_folder_item_context_menu(proj_sub_folder_item, context_menu_item_path='Properties', folder_path=proj_sub_folder)
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        
        """ Step 4: Type M In Search box 
                    Click X to clear search box
        """
        try:
            search_box_elem=self.driver.find_element_by_css_selector(search_box_css)
            utillobj.set_text_to_textbox_using_keybord(search_box_string, text_box_elem=search_box_elem)
        except NoSuchElementException:
            raise AttributeError("Search box not fond in Web page.")
        utillobj.synchronize_with_visble_text(search_box_css, search_box_string, 45, text_option='text_value')
        core_utilobj.python_left_click(search_box_elem, element_location='middle_right', xoffset=-9)
        
        """ Step 5: Click Cancel in Properties window
                    Verify a truncated Properties window does not appear
        """
        wf_mainobj.select_property_dialog_save_cancel_button('Cancel')
        repository_tree_appear_status = self.driver.find_element_by_css_selector(property_dialog_css).is_displayed()
        utillobj.asequal(False, repository_tree_appear_status, "Step 2.1: Verify a truncated Properties window does not appear.")
        
        """ Step 6: Sign out
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()