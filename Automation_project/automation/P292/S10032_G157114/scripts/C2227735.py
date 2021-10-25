'''
Created on December 26, 2017

@author: Praveen Ramkumar/Updated by :Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227735
TestCase Name = Report-Pivot: Verify user can change the aggregation type of a Pivot Report.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import  active_miscelaneous, active_pivot_comment
from common.lib import utillity
from common.wftools import active_report

class C2227735_TestClass(BaseTestCase):

    def test_C2227735(self):
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        pivobj=active_pivot_comment.Active_Pivot_Comment(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_OFF_001a.fex"
        report_dataset_name="AHTML_OFF_001a"
        
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G157266
                Execute the following URL:http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001a.fex
        """
    
        active_reportobj.run_active_report_using_api(fex_name,column_css="#ITableData0 #TCOL_0_C_0 span", synchronize_visible_element_text='Category')
        
        """
             Step 03 : Verify the report is generated.
        """
        
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 03.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.2: verify report data")
        
        """
             Step 04 : Select Unit Sales > Pivot > (Group by) State > (Across) Product
        """
        
        miscelanousobj.select_menu_items("ITableData0",4, "Pivot (Cross Tab)","State","Product")
        
        """
             Verify that the Aggregation icon now states Count.
            Also verify that summed Unit Sales have been replaced by Counts of Unit Sales.
        """
        pivobj.select_aggregate_function("wall1",0, 'Count')
        miscelanousobj.verify_popup_appears('wall1', 'Unit Sales BY Product, State', 'Step 04.1:Verify Unit Sales By Category, Product appears as the Report Heading.')
#         utillobj.create_pivot_data_set('piv1', 'C2227735_Ds01.xlsx')
        utillobj.verify_pivot_data_set('piv1', 'C2227735_Ds01.xlsx','Step 04.2: Verify pivot data')
        pivobj.verify_pivot_menu('wall1', 'Step 04.3: Verify pivot toolbar menus')
        utillobj.verify_object_visible("#wall1 #LINKIMG1_-1",True, 'Step 04.4: Freeze icon Visible')

        
        """
             Step 05: Click Aggregation icon and select the Count option.
        """
        
        pivobj.select_aggregate_function("wall1",1, 'Count')
        
        
        """
             Verify that the Aggregation icon now states Count.
            Also verify that summed Unit Sales have been replaced by Counts of Unit Sales.
        """
#         utillobj.create_pivot_data_set('piv1', 'C2227735_Ds02.xlsx')
        utillobj.verify_pivot_data_set('piv1', 'C2227735_Ds02.xlsx','Step 05.1: Verify pivot data')
        miscelanousobj.verify_popup_appears('wall1', 'Unit Sales BY Product, State', 'Step 05.2:Verify Unit Sales By Category, Product appears as the Report Heading.')
         
        """
             Step 06: Click Aggregation icon and select the Avg option.
        """
        
        pivobj.select_aggregate_function("wall1",1, 'Avg')
        
        """
             Verify that the Aggregation icon now states Avg.
            Also verify that the counts of Unit Sales have been replaced by the Average of Unit Sales. 
            The ONLY value that has changed from the SUM version is the final Grand Total Avg, located in the bottom right, which should read: 34,476.
        """
        
#         utillobj.create_pivot_data_set('piv1', 'C2227735_Ds03.xlsx')
        utillobj.verify_pivot_data_set('piv1', 'C2227735_Ds03.xlsx','Step 06.1: Verify pivot data')
        miscelanousobj.verify_popup_appears('wall1', 'Unit Sales BY Product, State', 'Step 06.2:Verify Unit Sales By Category, Product appears as the Report Heading.')
        
        """
             Step 07: Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
      
if __name__ == '__main__':
    unittest.main()
