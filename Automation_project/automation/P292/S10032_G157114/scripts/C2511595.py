'''
Created on December 29, 2017

@author: Praveen Ramkumar/Updated by :Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227734
TestCase Name = Report-Pivot: Verify that a Pivot Report can be changed to a simple column report using the Grid Controls.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_pivot_comment
from common.lib import utillity
from common.wftools import active_report

class C2511595_TestClass(BaseTestCase):

    def test_C2511595(self):
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        pivobj=active_pivot_comment.Active_Pivot_Comment(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_ON_001a.fex"
        report_dataset_name="AHTML_ON_001a"
        Test_Case_ID="C2511595"
        
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G157266
                Execute the following URL:http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001a.fex
        """
        
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 #TCOL_0_C_0 span", synchronize_visible_element_text="Category")
        
        """
             Step 03 : Verify the report is generated.
        """
        
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 03.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.2: verify report data")
        
        """
             Step 04 : Select State > Pivot > (Group by) Category > (Across) Product
        """
        miscelanousobj.select_menu_items("ITableData0",3, "Pivot (Cross Tab)","Category","Product")
        
        """
               Verify that the report heading shows: 'State By Product, Category'.
            Also verify the report shows Count in the control bar, due to the use of State as the Measure field.
        """
        pivobj.veryfy_pivot_table_title('piv1', 'StateBYProduct,Category', 'Step 04.1: Verify pivot Title')
#         utillobj.create_pivot_data_set('piv1', 'C2227734_Ds01.xlsx')
        utillobj.verify_pivot_data_set('piv1', Test_Case_ID+'_Ds01.xlsx','Step 04.2: Verify pivot data')
        pivobj.verify_pivot_menu('wall1', 'Step 04.3: Verify pivot toolbar menus')
        utillobj.verify_object_visible("#wall1 #LINKIMG1_-1",True, 'Step 04.4: Freeze icon Visible')
        
        """
             Step 05:Using the Pivot Controls select Group By (X) and select the Product ID field.
        """
        pivobj.create_new_item('wall1', 0, 'Group By (X)->Product ID')
        
        """
             :Verify that the report heading now shows: 'State By Product, Category, Product ID'.
            Also verify that the shows Category and Product ID as By fields and Product as the Across field.
        """
        
        pivobj.veryfy_pivot_table_title('piv1', 'StateBYProduct,Category,ProductID', 'Step 05.1: Verify pivot Title')
#         utillobj.create_pivot_data_set('piv1', 'C2227734_Ds02.xlsx')
        utillobj.verify_pivot_data_set('piv1', Test_Case_ID+'_Ds02.xlsx','Step 05.2: Verify pivot data')
        pivobj.verify_pivot_menu('wall1', 'Step 05.3: Verify pivot toolbar menus')
        utillobj.verify_object_visible("#wall1 #LINKIMG1_-1",True, 'Step 05.4: Freeze icon Visible')
        
        """
             Step 06:Using the Pivot Controls for the Product Across field, click the down arrow.
        """
        pivobj.click_groupby_across_button("piv1", 1, 3, 1)
        
        """
             Verify that the Product Across field has been moved to the By sort area as the first(major) sort.
            Also verify that the By sorts appear in the order: Product, Category and Product ID.
        """
        
        pivobj.veryfy_pivot_table_title('piv1', 'StateBYProduct,Category,ProductID', 'Step 06.1: Verify pivot Title')
#         utillobj.create_pivot_data_set('piv1', 'C2227734_Ds03.xlsx')
        utillobj.verify_pivot_data_set('piv1', Test_Case_ID+'_Ds03.xlsx','Step 06.2: Verify pivot data')
        pivobj.verify_pivot_menu('wall1', 'Step 06.3: Verify pivot toolbar menus')
        utillobj.verify_object_visible("#wall1 #LINKIMG1_-1",True, 'Step 06.4: Freeze icon Visible')
        
        """
             Step 07:Using the Controls for the Product ID field, click the left-pointing arrow.
        """
        pivobj.click_groupby_across_button("piv1", 1, 3, 2)
        
        """
             Verify that the report heading has changed to:State By Product, Product ID, Category.
            Also verify that the Product ID field has now been moved to the left.
        """
        pivobj.veryfy_pivot_table_title('piv1', 'StateBYProduct,ProductID,Category', 'Step 07.1: Verify pivot Title')
#         utillobj.create_pivot_data_set('piv1', 'C2227734_Ds04.xlsx')
        utillobj.verify_pivot_data_set('piv1', Test_Case_ID+'_Ds04.xlsx','Step 07.2: Verify pivot data')
        pivobj.verify_pivot_menu('wall1', 'Step 07.3: Verify pivot toolbar menus')
        utillobj.verify_object_visible("#wall1 #LINKIMG1_-1",True, 'Step 07.4: Freeze icon Visible')
        
        """
             Step 08:Using the Controls for the Category field, click the 'X' symbol.
        """
        pivobj.click_groupby_across_button("piv1", 1, 3, 4)

        """
             Verify that the report heading now reads:State By Product, Product ID.
                Also verify that Category has been removed from the report.
        """
        pivobj.veryfy_pivot_table_title('piv1', 'StateBYProduct,ProductID', 'Step 08.1: Verify pivot Title')
#         utillobj.create_pivot_data_set('piv1', 'C2227734_Ds05.xlsx')
        utillobj.verify_pivot_data_set('piv1', Test_Case_ID+'_Ds05.xlsx','Step 08.2: Verify pivot data')
        pivobj.verify_pivot_menu('wall1', 'Step 08.3: Verify pivot toolbar menus')
        utillobj.verify_object_visible("#wall1 #LINKIMG1_-1",True, 'Step 08.4: Freeze icon Visible')

        """
             Step 09:Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
if __name__ == "__main__":
    unittest.main()
