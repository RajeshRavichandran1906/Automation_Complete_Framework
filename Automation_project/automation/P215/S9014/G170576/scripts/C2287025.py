'''
Created on Aug 23, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2287025&group_by=cases:section_id&group_order=asc&group_id=170576
Testcase Name : Verify to Run and Interact with 'Freeze DataTable'
'''
import unittest, time
from common.wftools import report
from common.lib.basetestcase import BaseTestCase
from common.lib.javascript import JavaScript
from common.lib.core_utility import CoreUtillityMethods
from common.lib import utillity

class C2287025_TestClass(BaseTestCase):

    def test_C2287025(self):
        
        driver = self.driver
        report_obj = report.Report(driver)
        utillobj=utillity.UtillityMethods(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        Test_Case_ID="C2287025"
        medium_wait= 60
        
        username= 'mrbasid'
        password= 'mrbaspass'
        fex_name='Top_10_DataTables_Freeze'
        folder_name='Retail_Samples/Portal/Responsive_Tables'
        row1_text_val="Blu Ray"
        Qty_row_val="679,495"
        exp_columns_text='Subcategory Gross Profit   Discount MSRP COGS Qty'
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        table_css="#DataTables_Table_0"
        column_header_css="#DataTables_Table_0_wrapper .dataTables_scrollHeadInner"
        row_val_css=table_css+" > tbody >tr:nth-child({0})>td:nth-child({1})"
        subcategory_column_css="#DataTables_Table_0_wrapper .DTFC_LeftHeadWrapper table thead tr>th:nth-child({0})"
        Qty_column_css=table_css+"_wrapper thead:nth-child({0})>tr:nth-child({1})>th:nth-child({2})"
        Qty_column_val_css=".dataTables_scrollBody>table>tbody>tr:nth-child({0})>td:last-child"
        no_of_rows=table_css+" > tbody >tr"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
            Step 01: Sign to Webfocus using rsadv (advanced user)
            http://machine:port/ibi_apps
            Step 02: Run the Report using the below API URL
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Responsive_Tables&BIP_item=Top_10_DataTables_Freeze.fex
        """ 
        report_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_table_css=no_of_rows, no_of_element=14)
        
        """
            Verify the background color for Subcategory
            Verify the first row value of Report output
        """
        
#         report_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx")
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", "Step 02:01: Verify Report Output")
        
        msg='Step 02:02: Verify report column headers displayed as {0} in the report'.format(exp_columns_text) 
        actual_columns_text=self.driver.find_element_by_css_selector(column_header_css).text
        utillobj.asequal(exp_columns_text, actual_columns_text, msg)
        """
            Step 03 : Resize the browser window to small size
        """
        report_obj.set_browser_window_size(x='580')
        report_obj.wait_for_visible_text(row_val_css.format(1,1), row1_text_val, medium_wait)
        
        """
            Step 04 : Scroll horizontal bar to move forward
        """
        elem1=self.driver.find_element_by_css_selector(subcategory_column_css.format(1))
        
        before_scroll_subcategory_location=CoreUtillityMethods.get_web_element_coordinate(self, elem1)
        
        elem=self.driver.find_element_by_css_selector(Qty_column_val_css.format(1))
        JavaScript.scrollIntoView(self, elem)
        time.sleep(3)
        
        """
        Verify the Subcategory Columns is freezed and it should not move, other columns are move
        """
        elem1=self.driver.find_element_by_css_selector(subcategory_column_css.format(1))
        elem2=self.driver.find_element_by_css_selector(Qty_column_css.format(1,1,7))
        
        after_scroll_subcategory_location=CoreUtillityMethods.get_web_element_coordinate(self, elem1)
        
        Qty_location=CoreUtillityMethods.get_web_element_coordinate(self, elem2)
        
        if before_scroll_subcategory_location['x'] == after_scroll_subcategory_location['x'] and after_scroll_subcategory_location['x'] < Qty_location['x']:
            utillobj.as_GE(True, False, "Step 04:01:Verify Subcategory is freezed after applied horizontal bar to move right")
        else:
            False
        
        msg='Step 04:02:Verify report text value shown {0} in the report'.format(Qty_row_val)    
        report_obj.verify_table_cell_property(1, 7,table_css=Qty_column_val_css.format(1,7), text_value=Qty_row_val, msg=msg)
            
        """
            Step 05 : Maximize the browser window
        """
        report_obj.maximize_browser()
        report_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", "Step 05:01: Verify Report Output")
        
        """
            Step 06 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
        '''Will be acheived in teardown'''


if __name__ == "__main__":
    unittest.main()