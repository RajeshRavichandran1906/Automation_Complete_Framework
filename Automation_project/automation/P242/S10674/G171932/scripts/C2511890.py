'''
Created on 29 June, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2511890
TestCase Name = Properties: hit Backspace key in some boxes, return to sign on window
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity, core_utility
from selenium.common.exceptions import NoSuchElementException


class C2511890_TestClass(BaseTestCase):

    def test_C2511890(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        proj_sub_folder="Retail Samples->Reports"
        proj_sub_folder_item='Margin by Product Category'
        property_dialog_css='.properties-page.propPage'
        created_modified_accessed_date_text_css='.properties-general-file-created .ibx-label-text'
        
        """ Step 1: Login to WebFOCUS as a Developer.
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content from side bar.
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Open Retail Samples/Reports
        """
        """ Step 4: Right click 'Margin by Product Category' and select Properties
        """
        wf_mainobj.select_repository_folder_item_context_menu(proj_sub_folder_item, context_menu_item_path='Properties', folder_path=proj_sub_folder)
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        
        """ Step 5: Attempt to put cursor anywhere in Created, Modified and Accessed dates
                    Verify all dates are disabled for editing
        """
        created_elem=wf_mainobj.get_property_dialog_rows_object('Created', '5')
        core_utilobj.python_left_click(created_elem)
        try:
            created_status=created_elem.find_element_by_css_selector(created_modified_accessed_date_text_css).is_displayed()
        except NoSuchElementException:
            created_status=False
        modified_elem=wf_mainobj.get_property_dialog_rows_object('Modified', '5')
        core_utilobj.python_left_click(modified_elem)
        try:
            modified_status=created_elem.find_element_by_css_selector(created_modified_accessed_date_text_css).is_displayed()
        except NoSuchElementException:
            modified_status=False
        accessed_elem=wf_mainobj.get_property_dialog_rows_object('Accessed', '5')
        core_utilobj.python_left_click(accessed_elem)
        try:
            accessed_status=created_elem.find_element_by_css_selector(created_modified_accessed_date_text_css).is_displayed()
        except NoSuchElementException:
            accessed_status=False
        if created_status==modified_status==accessed_status:
            utillobj.asequal(True, True, "Step 5.1: Verify all dates are disabled for editing")
        else:
            utillobj.asequal(True, False, "Step 5.1: Verify all dates are disabled for editing")
        
        """ Step 6: Close Properties panel
        """
        wf_mainobj.close_property_dialog()
        
        """ Step 7: Sign out
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()