'''
Created on Jan 19, 2018

@author: Robert

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251694
TestCase Name = AHTML: ARFILTER_SORT = ASCENDING\DESCENDING (ACT-197)
'''
import unittest, time
import re
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, ia_run
from common.lib import utillity

class C2251694_TestClass(BaseTestCase):

    def test_C2251694(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2251694'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        
        """    1. Execute the attached repro - 161113.fex to produce an AHTML Document with filtering controls, Maximize the report window..    """
            
        utillobj.active_run_fex_api_login('161113.fex', 'S10071_3', 'mrid', 'mrpass')
             
        resultobj.wait_for_property("#ITableData0",1,30)
         
        time.sleep(3)
         
        """    1.1. Expect to see the following AHTML Document containing a report and 4 filter windows.    """
        """    1.2. Verify that the ListBox, CheckBox, Radio button and Combo box filters all appear.    """
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 1.2a: Verify the Report Heading')
        column_list=["COUNTRY", "CAR", "MODEL", "BODYTYPE", "DEALER_COST"]
        
        
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 1.2b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251694_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251694_Ds01.xlsx', 'Step 1.2c: Verify data.')
        
        utillobj.verify_object_visible("#list_dPROMPT_1", True, 'Step 1.2d. Verify Listbox present')
        utillobj.verify_object_visible("#checkbox_dPROMPT_2", True, 'Step 1.2e. Verify Checkbox present')
        utillobj.verify_object_visible("#radiobutton_dPROMPT_3", True, 'Step 1.2f. Verify Radiobuttons present')
        utillobj.verify_object_visible("#combobox_dPROMPT_4", True, 'Step 1.2g. Verify Combobox present')
        
        exp_list=['[All]', '25,000', '14,940', '11,194', '11,000', '10,000', '8,400', '8,300', '7,427', '6,000', '5,800', '5,660', '5,063', '4,915', '4,631', '4,292', '2,886', '2,626']
        iarun.verify_active_dashboard_prompts('listbox',"#list_dPROMPT_1", exp_list, 'Step 1.2h Verify the listbox contents')
        iarun.verify_active_dashboard_prompts('checkbox',"#checkbox_dPROMPT_2", exp_list, 'Step 1.2i Verify the checkbox contents')
        iarun.verify_active_dashboard_prompts('radiobutton',"#radiobutton_dPROMPT_3", exp_list, 'Step 1.2j Verify the radiobutton contents')
        
        
        """    2. Click on the [All] value in the Combo Box filter.    """
        """    2.1. Expect to see all filter Boxes, including the Combo Box to display the lists in Descending order.    """
        
        utillobj.verify_dropdown_value("#combobox_dPROMPT_4", exp_list, 'Step 2.1 Verify the dropdown contents')
        
        """    3. In the ListBox filter, select the value 5,800.    """
        """    3.1. Expect to see only one row for    """
        """    3.2. W GERMANY/BMW/2002 2 DOOR and value 5,800.    """
        
        iarun.select_active_dashboard_prompts('listbox',"#list_dPROMPT_1", ['5,800'])
        time.sleep(6)
        
        miscelanousobj.verify_page_summary(0, '1of18records,Page1of1', 'Step 3.2a: Verify the Report Heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251694_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251694_Ds02.xlsx', 'Step 3.2b: Verify data after filter.')
  
        
if __name__=='__main__' :
    unittest.main()
        