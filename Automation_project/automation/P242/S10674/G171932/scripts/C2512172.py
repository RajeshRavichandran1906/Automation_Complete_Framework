'''
Created on 06 July, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2512172
TestCase Name = Sort Order not saved
'''
import unittest,time, keyboard as localkey
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.pages import wf_mainpage
from common.lib import utillity, core_utility


class C2512172_TestClass(BaseTestCase):

    def test_C2512172(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        proj_sub_folder="Retail Samples->Reports"
        proj_sub_folder_item='Sales Metrics YTD'
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        property_dialog_css='.properties-page.propPage'
        selected_item_css="div[class*='files-box-files'] div[class*='file-item-shown'] .ibx-label-text"
        text_feild_css="[data-ibx-type='ibxTextField']"
        
        """ Step 1: Login to WebFOCUS as a Developer
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
        
        """ Step 5: Click Advanced tab
        """
        wf_mainobj.edit_property_dialog_value('Advanced', 'tab_value', 'Advanced')
        
        """ Step 6: Type -100 in 'Sort order' box
                    Save
                    Verify Sales Metrics YTD appears first in content area:
        """
        wf_mainobj.edit_property_dialog_value('Sort order', 'text_value', "-100", tab_name='Advanced')
        wf_mainobj.select_property_dialog_save_cancel_button('Save')
        report_list_order=[elem.text.strip() for elem in self.driver.find_elements_by_css_selector(selected_item_css)]
        expected_list_order=['Sales Metrics YTD', 'Margin by Product Category', 'Quantity Sold By Stores', 'Yearly Product Metrics']
        utillobj.as_List_equal(expected_list_order, report_list_order, "Step 5: Verify Sales Metrics YTD appears first in content area.")
        
        """ Step 7: Click Advanced tab
                    Remove -100 in 'Sort order' box
                    Save
                    Verify Sales Metrics YTD appears third in content area:
        """
        wf_mainobj.edit_property_dialog_value('Advanced', 'tab_value', 'Advanced')
        sort_order_elem=wf_mainobj.get_property_dialog_rows_object('Sort order', '7')
        sort_order_textfield_elem=sort_order_elem.find_element_by_css_selector(text_feild_css)
        text_input_value=sort_order_textfield_elem.find_element_by_css_selector('input').get_attribute('value')
        core_utilobj.python_left_click(sort_order_textfield_elem)
        for i in range(len(text_input_value)+3):
            localkey.send('\x08')
        del i
        wf_mainobj.select_property_dialog_save_cancel_button('Save')
        report_list_order=[elem.text.strip() for elem in self.driver.find_elements_by_css_selector(selected_item_css)]
        expected_list_order=['Margin by Product Category', 'Quantity Sold By Stores', 'Sales Metrics YTD', 'Yearly Product Metrics']
        utillobj.as_List_equal(expected_list_order, report_list_order, "Step 7.1: Verify Sales Metrics YTD appears first in content area.")
        
        """ Step 8: Cancel
        """
        wf_mainobj.select_property_dialog_save_cancel_button('Cancel')
        
        """ Step 9: Sign out
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()