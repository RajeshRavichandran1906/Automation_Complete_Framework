'''
Created on 25 June, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2511895
TestCase Name = Clicking save on the properties panel will result in showing the property for the main folder
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.pages import wf_mainpage
from common.lib import utillity
from selenium.common.exceptions import NoSuchElementException


class C2511895_TestClass(BaseTestCase):

    def test_C2511895(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        proj_sub_folder="Retail Samples->Reports"
        proj_sub_folder_item='Sales Metrics YTD'
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        property_dialog_css='.properties-page.propPage'
        selected_item_css="div[class*='files-box-files'] div[class*='file-item-shown'] .file-item-selected .ibx-label-text"
        
        """ Step 1: Login to WebFOCUS as a Developer.
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content from side bar.
        """
        wf_mainobj.select_left_panel('Content')
        
        """ Step 3: Open Retail Samples/Reports
        """
        """ Step 4: Right click Sales Metrics YTD and select Properties
        """
        wf_mainobj.select_repository_folder_item_context_menu(proj_sub_folder_item, context_menu_item_path='Properties', folder_path=proj_sub_folder)
        utillobj.synchronize_with_number_of_element(property_dialog_css, 1, 190)
        
        """ Step 5: Type 'text' in Summary box
                    Save
                    Verify Reports is still selected in tree
        """
        wf_mainobj.edit_property_dialog_value('Summary', 'text_area', "text ")
        wf_mainobj.select_property_dialog_save_cancel_button('Save')
        try:
            selected_report=self.driver.find_element_by_css_selector(selected_item_css).text.strip()
        except NoSuchElementException:
            raise AttributeError("No Reports is selected in tree")
        utillobj.asequal('Sales Metrics YTD', selected_report, "Step 5: Verify Reports is still selected in tree")
        
        """ Step 6: Delete the text in Summary and Save.
        """
        wf_mainobj.edit_property_dialog_value('Summary', 'text_area', '')
        wf_mainobj.select_property_dialog_save_cancel_button('Save')
        
        """ Step 7: Close Properties panel
        """
        wf_mainobj.close_property_dialog()
        
        """ Step 8: Sign out
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()