'''
Created on December 27, 2017

@author: Praveen Ramkumar/Updated by :Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227733
TestCase Name = Report-Pivot: Verify that the Pivot Table can contain multiple sort fields and those fields may be moved.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, active_pivot_comment
from common.lib import utillity
from common.wftools import active_report

class C2227733_TestClass(BaseTestCase):

    def test_C2227733(self):
        
        """
            TESTCASE VARIABLES
        """
    
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
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
             Step 04: Select Dollar Sales > Pivot > (Group by) State > (Across) Product ID
        """
        
        miscelanousobj.select_menu_items("ITableData0",5, "Pivot (Cross Tab)","State","Product ID")
        
        """
             Verify 'Dollar Sales By Product ID, State' is displayed for the Report Heading.
        """
        miscelanousobj.verify_popup_appears('wall1', 'Dollar Sales by Product ID, State', 'Step 06.1:Verify Unit Sales By Category, Product appears as the Report Heading.')
#         utillobj.create_pivot_data_set('piv1', 'C2227733_Ds01.xlsx')
        utillobj.verify_pivot_data_set('piv1', 'C2227733_Ds01.xlsx','Step 04.1: Verify pivot data')
        pivobj.verify_pivot_menu('wall1', 'Step 04.2 Verify pivot toolbar menus')
        utillobj.verify_object_visible("#wall1 #LINKIMG1_-1",True, 'Step 04.3: Freeze icon Visible')
        pivobj.veryfy_pivot_table_title('piv1', 'DollarSalesbyProductID,State', 'Step 04.4: Verify pivot Title')
        
        """
             Step 05: From the drop down menu, select the Add (Y) option and select the Unit Sales field.
        """
        
        pivobj.create_new_item('wall1', 0, 'Add (Y)->Unit Sales')
        
        """
             Verify that the Report now shows Unit Sales in place of Dollar Sales, as the Pivot (Cross Tab) option only allows a single Measure field.
        """
        pivobj.veryfy_pivot_table_title('piv1', 'UnitSalesbyProductID,State', 'Step 05.1: Verify pivot Title')
#         utillobj.create_pivot_data_set('piv1', 'C2227733_Ds02.xlsx')
        utillobj.verify_pivot_data_set('piv1', 'C2227733_Ds02.xlsx','Step 05.2: Verify pivot data')
        pivobj.verify_pivot_menu('wall1', 'Step 05.3: Verify pivot toolbar menus')
        utillobj.verify_object_visible("#wall1 #LINKIMG1_-1",True, 'Step 05.4: Freeze icon Visible')
        
        """
             Step 06: From the drop down menu, select the Group By (X) option and select the Category field.                
        """
        pivobj.create_new_item('wall1', 1, 'Group By (X)->Category')
        
        """
            Verify that the report heading displays now as: Unit Sales By Product ID, State, Category.
        """
        pivobj.veryfy_pivot_table_title('piv1', 'UnitSalesbyProductID,State,Category', 'Step 06.1: Verify pivot Title')
#         utillobj.create_pivot_data_set('piv1', 'C2227733_Ds03.xlsx')
        utillobj.verify_pivot_data_set('piv1', 'C2227733_Ds03.xlsx','Step 06.2: Verify pivot data')
        pivobj.verify_pivot_menu('wall1', 'Step 06.3: Verify pivot toolbar menus')
        utillobj.verify_object_visible("#wall1 #LINKIMG1_-1",True, 'Step 06.4: Freeze icon Visible')
        
        """
             Step 07: Using the controls for Category, click the up arrow key.
             Verify that the report heading displays now as: Unit Sales By Category, Product ID, State.
            Also verify that the Category field has been moved to the Across area and now resides under the Product ID field.                
        """
        pivobj.click_groupby_across_button("piv1", 2, 2, 1)
#         utillobj.create_pivot_data_set('piv1', 'C2227733_Ds04.xlsx')
        utillobj.verify_pivot_data_set('piv1', 'C2227733_Ds04.xlsx','Step 07.1: Verify pivot data')
        pivobj.veryfy_pivot_table_title('piv1', 'UnitSalesbyProductID,Category,State', 'Step 07.2: Verify pivot Title')
        
        """
             Step 08: Using the controls for Product ID, click the down arrow.
             Verify that the State has been demoted below the Across for Category.                
        """
        pivobj.click_groupby_across_button("piv1", 1, 2, 3)
#         utillobj.create_pivot_data_set('piv1', 'C2227733_Ds05.xlsx')
        utillobj.verify_pivot_data_set('piv1', 'C2227733_Ds05.xlsx','Step 08.1: Verify pivot data')
        pivobj.veryfy_pivot_table_title('piv1', 'UnitSalesbyCategory,ProductID,State', 'Step 08.2: Verify pivot Title')
        
        """
             Step 09: Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp              
        """
        
if __name__ == "__main__":
    unittest.main()