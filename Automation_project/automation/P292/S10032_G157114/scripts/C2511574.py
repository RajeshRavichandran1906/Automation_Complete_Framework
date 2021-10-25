'''
Created on December 14, 2017

@author: Prabhakaran/ Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227785
TestCase Name = Report-Filter: Verify user can use Filter menu options under each column (Equals, Not Equal & Greater Than)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous,active_filter_selection, ia_run
from common.lib import utillity
from common.wftools import active_report

class C2511574_TestClass(BaseTestCase):

    def test_C2511574(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2511574'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        actfilter = active_filter_selection.Active_Filter_Selection(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_ON_001a.fex"
        report_dataset_name="AHTML_ON_001a"
        
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 : Expand folder P292_S10032_G157266 Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AR-AHTML-001.fex
            Step 03 : Execute the AR-AHTML-001.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        
        """
            Step 03.1 : Verify outpu
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 03.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.2: verify report data")
         
        """
            Step 04 : Select State > Filter and Verify Filter menu shows all the filter options mentioned in the Test Description.
        """
        expected_list=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0',3,'Filter',expected_list,'Step 04.1 : Verify Filter menu shows all the filter options mentioned in the Test Description')
         
        """
            Step 05 : Select Filter > Equals
        """
        miscelanousobj.select_menu_items('ITableData0',3,'Filter','Equals')
         
        """
            Step 05.1 : Verify Filter that the selection menu appears:
        """
        miscelanousobj.verify_popup_appears('wall1','Filter Selection','Step 05.1 : Verify Filter that the selection menu appears')
         
        """
            Step 06 : Click dropdown next to <Value> for State column and Verify all the values (11 States) under State column are listed.
        """
        expected_menu_list=['CA','CT','FL','GA','IL','MA','MO','NY','TN','TX','WA']
        actfilter.verify_filter_values_menu_list(1, expected_menu_list,'Step 06.1 : Verify all the values (11 States) under State column are listed')
         
        """
            Step 07 : Select "IL " value in this test and click Filter button
        """
        actfilter.create_filter(1, 'Equals',value1='IL')
        actfilter.filter_button_click('Filter')
        resultobj.wait_for_property("#ITableData0>tbody>tr",10,10)
         
        """
            Step 07.1 : Verify that report returns 9 of 107 records that has "IL " state values in the output. 
        """
        miscelanousobj.verify_page_summary('0','9of107records,Page1of1','Step 07.1 : Verify page summary')
        #iarun.create_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_01.xlsx')
        iarun.verify_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_01.xlsx','Step 07.2 : Verify that report returns 9 of 107 records that has "IL " state values in the output')
         
        """
            Step 08 : Close Filter selection pop up
        """
        miscelanousobj.close_popup_dialog('1')
        resultobj.wait_for_property("#ITableData0>tbody>tr",58,10)
         
        """
            Step 08.1 : Verify report is restored in original format.
        """
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 08:01: verify report data")
          
        """
            Step 09 : Select State > Filter > Not Equal
        """
        miscelanousobj.select_menu_items('ITableData0',3,'Filter','Not equal')
         
        """
            Step 9.1 : Verify Filter selection pop up is opened
        """
        miscelanousobj.verify_popup_appears('wall1','Filter Selection','Step 09.1 : Verify Filter selection pop up is opened')
         
        """
            Step 10 : Select "MO" value in this test and click Filter button
        """
        actfilter.create_filter(1,'Not equal',value1='MO')
        actfilter.filter_button_click('Filter')
        time.sleep(3)
         
        """
            Step 10.1 : Verify that report returns 98 of 107 records based on other state values in the output.
        """
        miscelanousobj.verify_page_summary('0','98of107records,Page1of2','Step 10.1 : Verify that report returns 98 of 107 records')
        #iarun.create_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_02.xlsx')
        iarun.verify_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_02.xlsx','Step 10.2 : Verify filtered data values')
         
        """
            Step 11 : Close Filter selection pop up
        """
        miscelanousobj.close_popup_dialog('1')
        time.sleep(3)
         
        """
            Step 11.1 : Verify report is restored in original format.
        """
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 11.1 : Verify report is restored in original format")
         
        """
            Step 12 : Select Unit Sales > Filter > Greater Than
        """
        miscelanousobj.select_menu_items('ITableData0',4,'Filter','Greater than')
         
        """
            Step 12.1 : Verify Filter selection pop up is opened
        """
        miscelanousobj.verify_popup_appears('wall1','Filter Selection','Step 12.1 : Verify Filter selection pop up is opened')
         
        """
            Step 13 : Click dropdown next to <Value> for Unit Sales column
            Verify another pop up box appears with Unit Sales values to select values from.
            Step 14 : Select value = "27100" and click Filter
        """
        actfilter.create_filter(1,'Greater than','large',value1='27100')
        actfilter.filter_button_click('Filter')
        time.sleep(3)
         
        """
            Step 14.1 : Verify report returns 54 of 107 records that have Unit Sales value greater than "27100". 
        """
        miscelanousobj.verify_page_summary('0','54of107records,Page1of1','Step 14.1 : Verify report returns 54 of 107 records')
        #iarun.create_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_03.xlsx')
        iarun.verify_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_03.xlsx','Step 14.2 : Verify Unit Sales value greater than "27100"')
         
        """
            Step 15 : Close Filter selection pop up
        """
        miscelanousobj.close_popup_dialog('1')
        time.sleep(3)
         
        """
            Step 15.1 : Verify report is restored in original format.
        """
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 15.1: verify reportis restored in original format")
        
        """
            Step 16 : Select Unit Sales > Filter > Greater Than or equal to. Then click the dropdown for Unit Sales Filter values and select 27100. Click the Filter button
        """
        miscelanousobj.select_menu_items('ITableData0',4,'Filter','Greater than or equal to')
        miscelanousobj.verify_popup_appears('wall1','Filter Selection','Step 16.1 : Verify Filter selection pop up is opened')
        actfilter.create_filter(1,'Greater than or equal to','large',value1='27100')
        actfilter.filter_button_click('Filter')
        time.sleep(3)
        
        """
            Step 16.1 : Verify report returns 55 of 107 records that have Unit Sales value greater than "27100".
        """
        miscelanousobj.verify_page_summary('0','55of107records,Page1of1','Step 16.1 : Verify report returns 55 of 107 records')
        #iarun.create_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_04.xlsx')
        iarun.verify_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_04.xlsx','Step 16.2 : Unit Sales value greater than "27100')
        
        """
            Step 17 : Dismiss the window and logout. http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__=='__main__' :
    unittest.main()