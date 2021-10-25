'''
Created on Dec 29, 2017

@author: Bhagavathi

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157266
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227731
TestCase Name : Report:Verify that user is able to run a simple AHTML report
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous, ia_run,active_pivot_comment, active_filter_selection
from common.lib import utillity
from common.wftools import active_report

class C2511597_TestClass(BaseTestCase):

    def test_C2511597(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2511597'
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelanousobj =active_miscelaneous.Active_Miscelaneous(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        pivobj=active_pivot_comment.Active_Pivot_Comment(self.driver)
        actfilter = active_filter_selection.Active_Filter_Selection(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_ON_001a.fex"
        report_dataset_name="AHTML_ON_001a"
        
        """
            Step 01:Sign in to WebFOCUS as a Basic user
            http://machine:port/{alias}
            Step 02:Expand folder P292_S10032_G157266
            Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001a.fex
        """ 
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 #TCOL_0_C_0 span", synchronize_visible_element_text="Category")
        
        """
            Step 03:Verify the report is generated.
        """
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.1: Verify column heading')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 03.2:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.3: verify report data")
              
        """
            Step 04 :Select State > Pivot > (Group by) Category > (Across) Product
            Verify 'State Across Product By Category' pop up is displayed
            - Verify selected columns/data are displayed
            Verify toolbar shows:
            - Dropdown
            - Freeze icon
            - Aggregation icon
        """
        miscelanousobj.select_menu_items("ITableData0",3, "Pivot (Cross Tab)","Category","Product")
        result_obj.wait_for_property("#wall1 .arWindowBarTitle>span",1, 8, string_value='State by Product, Category')
        miscelanousobj.move_active_popup(1, '600', '0')
        
        miscelanousobj.verify_popup_appears('wall1', 'State by Product, Category', 'Step 04.1 : Verify State Across Product By Category pop up is displayed')
#         utillobj.create_pivot_data_set('piv1', Test_Case_ID+'_Ds01.xlsx')
        utillobj.verify_pivot_data_set('piv1', Test_Case_ID+'_Ds01.xlsx', 'Step 04.2 : Verify selected columns/data are displayed')
        
        """
            Step 05:Click Freeze icon displayed under Active tool bar. By default it is unlocked.
            Verify identical Freeze icon is now locked.
        """
        pivobj.click_pivot_menu_bar_items("wall1",1)
         
        """ 
            Step 06:Now go back to original report and perform Product > Filter > Equals
            Verify Filter pop up opened up on the screen.
        """
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter', 'Equals')
        result_obj.wait_for_property("#wall2 .arWindowBarTitle",1, 8, string_value='Filter Selection for Report1')
        miscelanousobj.move_active_popup(2, '600', '600')
        miscelanousobj.verify_popup_appears('wall2', 'Filter Selection for Report1', 'Step 06.1 : Verify Filter pop up opened up on the screen.')
        
        """   
            Step 07:Select Product = Espresso and click filter
        """
        actfilter.create_filter(1, 'Equals', 'small', 'wall2', value1='Espresso')
        actfilter.filter_button_click('Filter', 'wall2')
        
        """  
            Verify that report only gets filtered. Report shows all records where product=Espresso.
        """
        miscelanousobj.verify_page_summary('0','11of107records,Page1of1','Step 07.1 : Verify page summary')
#         iarun.create_table_data_set('#ITableData0', Test_Case_ID+'_Ds02.xlsx')
        iarun.verify_table_data_set('#ITableData0', Test_Case_ID+'_Ds02.xlsx', 'Step 07.2 : Verify that report only gets filtered. Report shows all records where product=Espresso.')
        utillobj.verify_pivot_data_set('piv1', Test_Case_ID+'_Ds01.xlsx', 'Step 07.3 : Verify filter not change pivot table data')
        
        """ 
            Step 08:Now go to Pivot table and unlock Freeze icon
            Verify Pivot table gets filtered with filtered query. Now Pivot table only shows record for product=Espresso.
        """
        pivobj.click_pivot_menu_bar_items('wall1', 1)
        time.sleep(3)
#         utillobj.create_pivot_data_set('piv1', Test_Case_ID+'_Ds03.xlsx')
        utillobj.verify_pivot_data_set('piv1', Test_Case_ID+'_Ds03.xlsx', 'Step 08.1 : Verify Pivot table gets filtered with filtered query. Now Pivot table only shows record for product=Espresso.')
    

if __name__ == "__main__":
    unittest.main()