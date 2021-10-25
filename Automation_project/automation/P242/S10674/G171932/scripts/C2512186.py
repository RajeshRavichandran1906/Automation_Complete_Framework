'''
Created on 26 June, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2512186
TestCase Name = Properties: Thumbnail is outside the box in Advanced tab
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity


class C2512186_TestClass(BaseTestCase):

    def test_C2512186(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        proj_sub_folder="Retail Samples->Reports"
        proj_sub_folder_item='Sales Metrics YTD'
        property_dialog_css='.properties-page.propPage'
        advanced_tab_css=".tpg-selected .properties-advanced-item-fex"
        
        """ Step 1: Login to WebFOCUS as a Developer
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content from side bar.
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Open Retail Samples/Reports
        """
        """ Step 4: Right click any report and select Properties
        """
        wf_mainobj.select_repository_folder_item_context_menu(proj_sub_folder_item, context_menu_item_path='Properties', folder_path=proj_sub_folder)
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        
        """ Step 5: Click Advanced tab
                    Verify thumbnail is inside box:
        """
        wf_mainobj.edit_property_dialog_value('Advanced', 'tab_value', 'Advanced')
        utillobj.synchronize_with_number_of_element(advanced_tab_css, 1, 190)
        properties_advanced_item_elem=self.driver.find_element_by_css_selector(advanced_tab_css)
        utillobj.verify_regional_picture_using_sikuli('report_thumnail.png', "Step 5: Verify thumbnail is inside box.", parent_element=properties_advanced_item_elem)
        
        """ Step 6: Cancel
        """
        wf_mainobj.select_property_dialog_save_cancel_button('Cancel')
        
        """ Step 7: Sign out
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()