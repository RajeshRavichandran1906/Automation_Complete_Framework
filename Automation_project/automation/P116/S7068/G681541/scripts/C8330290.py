'''
Created on Jan 8, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8330290
Testcase Name : AHTML: Verify Filter operators against various Alphanumeric fields(Part 3)
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.pages import active_filter_selection
from common.lib import utillity
import unittest

class C8330290_TestClass(BaseTestCase):

    def test_C8330290(self):

        """
           CLASS OBJECTS
        """ 
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        
        """
            TESTCASE VARIABLES
        """
        
        fex_name="AR-RP-141AL.fex"
        long_wait=60
        
        """
            CSS
        """
        table_css="#ITableData0"
        data_value_css=table_css+" tbody tr:nth-child(4) td:nth-child(2)"
        
        """
        Step 1:Execute AR-RP-141AL.fex from below API to produce the alphanumeric output
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P116_S7068/G146859&BIP_item=AR-RP-141AL.fex
        Expect to see the following Active Report.
        """
        utillobj.active_run_fex_api_login(fex_name, "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(data_value_css, '000001', long_wait)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 1:01: Expect to see the following Active Report. - page summary verification")

        """
        Step 2:For the following ALPHA fields, select Filter, then Equals and use these values:
        Select the Highlight option for this test.
        After each field Highlight, close the Filter panel for the next field.

        ALPHA ORDER - 000001
        ALPHA ANV - 000005 
        ALPHA TEXT - 000010
        ALPHA A80 - 000015 
        ALPHA Edit - G-104 
        ALPHA Store Code - R1020 
        ALPHA Vendor Code - V102 
        ALPHA Vendor Name - Thermo Tech, Inc

        ALPHA Product Code - G100 
        ALPHA Product Descr. - French Roast

        Verify that the report Highlights only those rows that match the selected value.
        .
        .
        .
        .
        Expect 1 row highlighted - value 000001 
        Expect 1 row highlighted - value 000005
        Expect 1 row highlighted - value 000010
        Expect 1 row highlighted - value 000015
        Expect only G-104 rows highlighted, page down to verify
        Expect only R1020 rows highlighted, page down to verify
        Expect only V102 rows highlighted, page down to verify
        Expect only Thermo Tech, Inc rows highlighted, page down to verify
        Expect only G100 rows highlighted, page down to verify
        Expect only French Roast rows highlighted, page down to verify
        """
        #Expect 1 row highlighted - value 000001
         
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals','large',value1='000001')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds01_Page1.xlsx',"Step 04: Expect 1 row highlighted - value 000001")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds01_Page1.xlsx')
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #time.sleep(3)
        #Expect 1 row highlighted - value 000005
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter", "Equals")
         
        filterselectionobj.create_filter(1, 'Equals','large', value1='000005')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
 
        #time.sleep(5)
         
         
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds02_Page1.xlsx',"Step 04 Expect 1 row highlighted - value 000005")
         
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds02_Page1.xlsx')
         
        filterselectionobj.close_filter_dialog()
        #Expect 1 row highlighted - value 000010
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals','large',value1='000010')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight') 
        #time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds03_Page1.xlsx',"Step 04 Expect 1 row highlighted - value 000010")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds03_Page1.xlsx')
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 1 row highlighted - value 000015
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals','large',value1='000015')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
 
        #time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds04_Page1.xlsx',"Step 04 Expect 1 row highlighted - value 000015")
         
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds04_Page1.xlsx')
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        # Expect only G-104 rows highlighted, page down to verify
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Equals")
        filterselectionobj.create_filter(1, 'Equals',value1='G-104')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds05_Page1.xlsx',"Step 04 Expect only G-104 rows highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds05_Page1.xlsx')
        #time.sleep(5)
         
        filterselectionobj.close_filter_dialog()
        #Expect only R1020 rows highlighted, page down to verify
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals',value1='R1020')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds06_Page1.xlsx',"Step 04 Expect only R1020 rows highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds06_Page1.xlsx')
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        # Expect only V102 rows highlighted, page down to verify
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals',value1='V102')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
         
        #time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds07_Page1.xlsx',"Step 04.1: Expect only V102 rows highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds07_Page1.xlsx')
        #time.sleep(5)
         
        filterselectionobj.close_filter_dialog()
         
         
        # Expect only Thermo Tech, Inc rows highlighted, page down to verify
         
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals',value1='ThermoTech, Inc')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
         
        #time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds08_Page1.xlsx',"Step 04 Expect only Thermo Tech, Inc rows highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds08_Page1.xlsx')
        #time.sleep(5)
         
        filterselectionobj.close_filter_dialog()
         
        # Expect only G100 rows highlighted, page down to verify
         
        miscelanousobj.select_menu_items("ITableData0", "9", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals',value1='G100')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
  
        #time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds09_Page1.xlsx',"Step 04:Expect only G100 rows highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds09_Page1.xlsx')
        #time.sleep(5)
         
        filterselectionobj.close_filter_dialog()
 
        # Expect only French Roast rows highlighted, page down to verify
         
        miscelanousobj.select_menu_items("ITableData0", "10", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals',value1='French Roast')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds10_Page1.xlsx',"Step 04 Expect only French Roast rows highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds10_Page1.xlsx')
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        

if __name__ == "__main__":
    unittest.main()