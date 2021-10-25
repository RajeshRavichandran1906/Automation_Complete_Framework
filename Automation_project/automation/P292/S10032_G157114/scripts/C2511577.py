'''
Created on Dec 16, 2017

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2227788
TestCase Name : Report-Filter: Verify that filter option Equal works for multiple selection values.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous,active_filter_selection
from common.lib import utillity
from common.wftools import active_report

class C2511577_TestClass(BaseTestCase):

    def test_C2511577(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2511577'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        actfilter = active_filter_selection.Active_Filter_Selection(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_ON_001a.fex"
        report_dataset_name="AHTML_ON_001a"
        
        """
            Step 01:Sign in to WebFOCUS as a Basic user
            http://machine:port/{alias}
            Step 02:http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AR-AHTML-001.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        """ 
            Step 03:Verify the report is generated.
        """
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03:01: Verify column heading')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 03:02:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.3: verify report data")
                
        """ 
            Step 04:Select State > Filter > Equals
            Select "CA ", "MA", "NY" values in this test
            Verify all the values under selected column are listed.
        """
        miscelanousobj.select_menu_items('ITableData0',3,'Filter','Equals')
        miscelanousobj.verify_popup_appears('wall1','Filter Selection','Step 04:01: Verify Filter that the selection menu appears')
        expected_menu_list=['CA','CT','FL','GA','IL','MA','MO','NY','TN','TX','WA']
        actfilter.verify_filter_values_menu_list(1, expected_menu_list,'Step 04:02: Verify all the values (11 States) under State column are listed')
        actfilter.create_filter(1, 'Equals',value1='CA', value2='MA', value3='NY')
        
        """ 
            Step 05:Click the Filter button.
            Verify State value Filter selection menu appears.
            Verify that report returns 30 of 107 records based on "CA ", "MA", "NY" state values in the output.
        """
        actfilter.filter_button_click('Filter')
        resultobj.wait_for_property("#ITableData0>tbody>tr",31,10)
        miscelanousobj.verify_page_summary('0','30of107records,Page1of1','Step 05:01: Verify page summary')
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds02.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds02.xlsx", "Step 05:01: CacheOFF_ahtml_off_001 fex data verification")
        """ 
            Step 06:Close Filter selection pop up
            Verify report is restored in original format.
        """
        miscelanousobj.close_popup_dialog('1')
        parent_css="#IWindowBody0 span[title='Move to Top'] img"
        resultobj.wait_for_property(parent_css, 1)
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 06:01: Verify column heading')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 06:02:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01.xlsx", "Step 06:3: CacheOFF_ahtml_off_001 fex data verification", desired_no_of_rows=20)
        
        """
            Step 07:Select Dollar Sales > Filter > Equals
            Select 158995, 204897 & 409466 as values
            Verify all the values under selected column are listed.
        """
        miscelanousobj.select_menu_items('ITableData0',5,'Filter','Equals')
        miscelanousobj.verify_popup_appears('wall1','Filter Selection','Step 07:01: Verify Filter that the selection menu appears')
        actfilter.create_filter(1, 'Equals', 'large', value1='158995', value2='204897', value3='409466')
               
        """ 
            Step 08:Click the Filter button.
            Expect to see three records, one each for 158995, 204897 & 409466.
        """
        actfilter.filter_button_click('Filter')
        resultobj.wait_for_property("#ITableData0>tbody>tr",4,10)
        miscelanousobj.verify_page_summary('0','3of107records,Page1of1','Step 08:01: Verify report returns 3 of 107 records')
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds03.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds03.xlsx", "Step 08:02: CacheOFF_ahtml_off_001 fex data verification")
        
        """ 
            Step 09:Dismiss the window and logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()