'''
Created on Jan 02, 2018

@author: Praveen Ramkumar/Updated by :Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227732
TestCase Name = Report-Pivot: Verify Pivot Tool bar menu items operate from an Active Report.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_pivot_comment
from common.lib import utillity
from common.wftools import active_report

class C2227732_TestClass(BaseTestCase):

    def test_C2227732(self):
        
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
                Execute the following URL:http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001.fex
        """
        active_reportobj.run_active_report_using_api(fex_name,column_css="#ITableData0 #TCOL_0_C_0 span", synchronize_visible_element_text='Category')

        """
             Step 03 : Verify the report is generated.
        """
        
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 03.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.2: verify report data")
        
        """
             Step 04: Select Unit Sales > Pivot > (Group by) Product > (Across) Category
            Verify 'Unit Sales By Category, Product' appears as the Report Heading.
            Verify Grid Report shows Unit Sales sorted BY Category going down and Across Product going across the report.
            
            Also verify toolbar shows:
            - Dropdown
            - Freeze icon
            - Aggregation icon
        """
        miscelanousobj.select_menu_items("ITableData0",4, "Pivot (Cross Tab)","Product","Category")
        pivobj.veryfy_pivot_table_title('piv1', 'UnitSalesBYCategory,Product', 'Step 04.1: Verify pivot Title')
#         utillobj.create_pivot_data_set('piv1', 'C2227732_Ds02.xlsx')
        utillobj.verify_pivot_data_set('piv1', 'C2227732_Ds02.xlsx','Step 04.2: Verify pivot data')
        pivobj.verify_pivot_menu('wall1', 'Step 05.3: Verify pivot toolbar menus')
        utillobj.verify_object_visible("#wall1 #LINKIMG1_-1",True, 'Step 04.4: Freeze icon Visible')
        
        """
            Step 05: Click dropdown menu under tool bar, select Group By (X).
            Verify it shows:
            - New
            - Group By (x)
            - Add (y)
            - Export to (specific to IE browser)
            - Pivot tool
        """
        browser=utillobj.parseinitfile('browser')
        if browser == 'IE':
            exp=['New', 'Group By (X)', 'Add (Y)','Export to', 'Pivot Tool']
            pivobj.verify_new_item('wall1', 0, exp,"Step 05:verified menu tool bar")
        else:
            exp=['New', 'Group By (X)', 'Add (Y)', 'Pivot Tool']
            pivobj.verify_new_item('wall1', 0, exp,"Step 05:verified menu tool bar") 
        """
             Step 06: Select the Product ID field to be added as an additional sort.
                Verify that the report now shows an additional sort (Product ID) going down the report next to Product(name).
        """
        
        pivobj.create_new_item('wall1', 0, 'Group By (X)->Product ID')
        pivobj.veryfy_pivot_table_title('piv1', 'UnitSalesBYCategory,Product,ProductID', 'Step 06.1: Verify pivot Title')
#         utillobj.create_pivot_data_set('piv1', 'C2227732_Ds03.xlsx')
        utillobj.verify_pivot_data_set('piv1', 'C2227732_Ds03.xlsx','Step 06.2: Verify pivot data')
        pivobj.verify_pivot_menu('wall1', 'Step 06.3: Verify pivot toolbar menus')
        utillobj.verify_object_visible("#wall1 #LINKIMG1_-1",True, 'Step 06.4: Freeze icon Visible')
        
        """
             Step 07: Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == "__main__":
    unittest.main()   