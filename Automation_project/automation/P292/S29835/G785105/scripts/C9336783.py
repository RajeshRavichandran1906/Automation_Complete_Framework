'''
Created on Sep 11, 2019

@author: Niranjan
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9336783
TestCase Name = Document:Verify the creation of a Document with multiple Reports
'''

from common.wftools.report import Report
from common.wftools.active_report import Active_Report
from common.wftools.document import Document
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.pages.ia_miscelaneous import IA_Miscelaneous
import unittest
from common.lib import global_variables

class C9336783_TestClass(BaseTestCase):

    def test_C9336783(self):
    
        """
            CLASS OBJECTS
        """
        driver=self.driver
        report_ = Report(self.driver)
        utils = UtillityMethods(self.driver)
        act_report = Active_Report(self.driver)
        doc = Document(self.driver)
        misc = IA_Miscelaneous(self.driver)
        glob_var=global_variables.Global_variables
        
        
        """  Step 1 : Invoke following api url as below
                http://machine:port/{alias}/ia?tool=document&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10032_G157266%2F    
            Step 01.00: Verify output format as Html Analytic Report."""
        misc.invoke_ia_tool_using_api_(tool='document', master='baseapp/wf_retail_lite', mrid = 'mrid', mrpass = 'mrpass', folder_path= 'P292_S10032_G157266')
        utils.synchronize_with_visble_text("#iaCanvasContainer", "Document", misc.chart_long_timesleep)
        doc.wait_for_number_of_element("#iaMetaDataBox [id^='BiGroupBoxTitle']", 1, misc.home_page_long_timesleep)
        utils.wait_for_page_loads(misc.home_page_long_timesleep)
        output_format = self.driver.find_element_by_css_selector('#HomeFormatType').get_attribute('text')
        utils.asequal(output_format, 'HTML Analytic Document', 'Step 01.00: Verify output format as Html Analytic Report')
        
        """  Step 2: Double click Quantity,Sold from the Sales group under Measures   """
        report_.double_click_on_datetree_item('Quantity,Sold')
        utils.wait_for_page_loads(20)
        report_.wait_for_visible_text('#queryTreeWindow', 'Quantity,Sold')
        
        """   Step 3: Double click Product,Category from the Product group under Dimensions.  
              Step 03.00: Expect to see the first report component on the canvas. """
        report_.double_click_on_datetree_item('Product,Category')
        utils.wait_for_page_loads(20)
        report_.wait_for_visible_text('#queryTreeWindow', 'Product,Category')
#         report_.create_acrossreport_data_set_in_preview("TableChart_1", 2, 2, 7, 2, "C9336783_DS01.xlsx")
        report_.verify_across_report_data_set_in_preview("TableChart_1", 2, 2, 7, 2, "C9336783_DS01.xlsx", "Step 03.00: Verify first report")
              
        """   Step 4: Click Insert tab from the tool bar and click Report icon.    """
        report_.select_ia_ribbon_item('Insert', 'report')
        
        """  Step 5: Drag the new report to the right of the first report.  """
        doc.drag_drop_document_component( '#TableChart_2', '#TableChart_1', 200, 0)
        
        """  Step 6: Double click Gross Profit from the Sales group under Measures.  """
        report_.double_click_on_datetree_item('Gross Profit')
        report_.wait_for_visible_text('#queryTreeWindow', 'Gross Profit')
        
        """  Step 7: Double click Product,Category and Product,Subcategory from the Product group under Dimensions.  
        Step 07.00: Expect to see two Reports on the canvas. """
               
        report_.double_click_on_datetree_item('Product,Category')
        report_.wait_for_visible_text('#queryTreeWindow', 'Product,Category')
        if glob_var.browser_name == 'firefox':
            a=driver.find_element_by_xpath("//div[contains(@id,'QbMetaDataTree')]//td [normalize-space()='Product,Subcategory']")
            a.location_once_scrolled_into_view
            
        report_.double_click_on_datetree_item('Product,Subcategory')
        report_.wait_for_visible_text('#queryTreeWindow', 'Product,Subcategory', 60)
        
        #report_.create_acrossreport_data_set_in_preview("TableChart_2", 3, 3, 10, 3, "C9336783_DS02.xlsx")
        report_.verify_across_report_data_set_in_preview("TableChart_2", 3, 3, 10, 3, "C9336783_DS02.xlsx", "Step 07.00: Verify second report")
        
        """  Step 8: Click Run.  
        Step 08.00: Expect to see two Active Reports in the Document.
                         Expect to see 7 records on the first report and 21 records on the second report."""
        
        report_.run_report_from_toptoolbar()
        report_.switch_to_frame()
        report_.wait_for_visible_text('#MAINTABLE_wbody0 table[class="arGridBar"]', '7 of 7 records, Page 1 of 1')
        act_report.verify_column_heading('ITableData0', ['ProductCategory', 'QuantitySold'], msg = 'Step 08.00: Verify column heading of first active report')
        act_report.verify_column_heading('ITableData1', ['ProductCategory', 'ProductSubcategory', 'GrossProfit'], msg = 'Step 08.01: Verify column heading of second active report')
        summary_ele = self.driver.find_element_by_css_selector('#MAINTABLE_wbody0 table[class="arGridBar"]')
        summary = summary_ele.text
        utils.asequal(summary, '7 of 7 records, Page 1 of 1', 'Step 08.02: Verify 7 records on the first active report')
        summary_ele = self.driver.find_element_by_css_selector('#MAINTABLE_wbody1 table[class="arGridBar"]')
        summary = summary_ele.text
        utils.asequal(summary, '21 of 21 records, Page 1 of 1', 'Step 08.03: Verify 21 records on the second active report')
#         act_report.create_active_report_dataset('C9336783_DS03.xlsx', table_css='#ITableData0', desired_no_of_rows=7, starting_rownum=1)
        act_report.verify_active_report_dataset('C9336783_DS03.xlsx', table_css='#ITableData0', desired_no_of_rows=7, starting_rownum=1, msg= 'Step 08.04 : Verify first active report')
#         act_report.create_active_report_dataset('C9336783_DS04.xlsx', table_css='#ITableData1', desired_no_of_rows=7, starting_rownum=1)
        act_report.verify_active_report_dataset('C9336783_DS04.xlsx', table_css='#ITableData1', desired_no_of_rows=7, starting_rownum=1, msg= 'Step 08.05 : Verify second active report')
        
        """  Step 9. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()