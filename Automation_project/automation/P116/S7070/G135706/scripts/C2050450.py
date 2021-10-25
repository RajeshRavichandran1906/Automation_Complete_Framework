
'''
Created on Aug 18, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050450
'''

import unittest
import time,re
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, active_filter_selection,\
    wf_mainpage
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from common.lib import utillity


class C2050450_TestClass(BaseTestCase):

    def test_C2050450(self):

        driver = self.driver #Driver reference object created
        Test_Case_ID = 'C2050450'
        
        """Step 01: Run the attached 138557.fex"""
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        filterobj = active_filter_selection.Active_Filter_Selection(self.driver)
        result_obj=visualization_resultarea.Visualization_Resultarea(self.driver)
        
        utillobj.active_run_fex_api_login('138557.fex','S7070','mrid','mrpass')
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(7) 
        active_misobj.verify_page_summary('0','241of241records,Page1of5', 'Step 01.1: Verify Page summary 241 of 241')
        column=['Package', 'Order Date', 'Product', 'Product Code', 'Vendor Name', 'Size', 'Unit Price']
        active_misobj.verify_column_heading('ITableData0', column, "Step 01.2: Verify Column heading of 138557")
        parent_css="#ITableData0 tr:nth-child(2) td:nth-child(1)"
        result_obj.wait_for_property(parent_css, 1, string_value='Case', with_regular_exprestion=True)
        utillobj.verify_data_set('ITableData0','I0r','138557.xlsx',"Step 01.3: Verify 138557 dataset")
                
        """
        Step 02: On the product column select Filter equals
        """ 
        time.sleep(5)
        active_misobj.select_menu_items('ITableData0', 2, 'Filter', 'Equals')
       
        """ 
        Step 03: From Filter Selection Select biscotti from the dropdown list and click filter
        """
        time.sleep(5)
        filterobj.create_filter(1, 'Equals', value1='Biscotti')
        time.sleep(3)
        filterobj.filter_button_click('Filter')
        
        """
        Step 04: Verify 24of241 records, are displayed under page 1 of 1
        """
        time.sleep(3)
        filterobj.verify_filter_selection_dialog(True,'Step 04: Verify filter row.',['Product', 'Equals', 'Biscotti'])
        active_misobj.verify_page_summary('0','24of241records,Page1of1', 'Step 04.1: Verify Page summary 24 of 241') 
        parent_css="#ITableData0 tr:nth-child(2) td:nth-child(1)"
        result_obj.wait_for_property(parent_css, 1, string_value='Case', with_regular_exprestion=True)  
        utillobj.verify_data_set('ITableData0','I0r','C2050450_Ds01.xlsx',"Step 04.2: Verify filtered dataset")
        
        """
        Step 05: Click Highlight and verify fields gets highlighted
        """
        time.sleep(5)
        filterobj.filter_button_click('Highlight')
        parent_css="#ITableData0 tr:nth-child(2) td:nth-child(1)"
        result_obj.wait_for_property(parent_css, 1, string_value='Case', with_regular_exprestion=True)  
        utillobj.verify_data_set_old('ITableData0','bgcolor','C2050450_Ds02.xlsx',"Step 05.1: Verify highlighted page1 dataset",color='navy')
        
        """
        Step 06: Click clear all then the fileds gets cleared and displayed empty filter box
        """
        time.sleep(5)
        filterobj.filter_button_click('Clear All')
        time.sleep(10)
        filterobj.verify_filter_selection_dialog(False,'Step 06: Verify filter row removed',['Product', 'Equals', 'Biscotti'])
        
        """
        Step 07: Click the X to close the filter box
        """
        filterobj.close_filter_dialog()
        
        """
        Step 08: Select another column title, and repeat steps 4 to 8
        """
        active_misobj.select_menu_items('ITableData0', '3', 'Filter', 'Equals')
        time.sleep(5)
        filterobj.create_filter(1, 'Equals', value1='G100')
        filterobj.filter_button_click('Filter')
        time.sleep(3)
        filterobj.verify_filter_selection_dialog(True,'Step 04: Verify filter row.',['Product Code', 'Equals', 'G100'])
        active_misobj.verify_page_summary('0','24of241records,Page1of1', 'Step 08.1: Verify Page summary 24 of 241')
        parent_css="#ITableData0 tr:nth-child(2) td:nth-child(1)"
        result_obj.wait_for_property(parent_css, 1, string_value='Case', with_regular_exprestion=True)     
        utillobj.verify_data_set('ITableData0','I0r','C2050450_Ds03.xlsx',"Step 08.2: Verify filtered dataset")
        time.sleep(5)
        filterobj.filter_button_click('Highlight')
        time.sleep(5)
#         parent_css="#ITableData0 tr:nth-child(2) td:nth-child(1)"
#         result_obj.wait_for_property(parent_css, 1, string_value='Case', with_regular_exprestion=True)  
        utillobj.verify_data_set_old('ITableData0','bgcolor','C2050450_Ds04.xlsx',"Step 08.3: Verify highlighted page1 dataset",color='navy')
        
        filterobj.filter_button_click('Clear All')
        time.sleep(5)
        filterobj.verify_filter_selection_dialog(False,'Step 08.4: Verify filter row removed',['Product Code', 'Equals', 'G100'])
        filterobj.close_filter_dialog()       
        

if __name__ == '__main__':
    unittest.main()

