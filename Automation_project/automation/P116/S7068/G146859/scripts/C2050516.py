'''
Created on Jul 28, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050516
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import unittest
import time

class C2050516_TestClass(BaseTestCase):

    def test_C2050516(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050516'
        """
            Step 01: Execute the AR-RP-141CA.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-141CA.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01: Execute the AR-RP-141CA.fex")
        """
            Step 02: Execute AR-RP-141CA to produce the mixed field output report.
            For column Date MDYY, select Rollup from the drop down option list.
            Select Order Number INTEGER as the Rollup column.
        """
        
        
        option='Group By (X)(COU)'
        miscelanousobj.verify_menu_items('ITableData0', 3, "Rollup",option,"Step 02: Expect to see Group by (X)(COU) which indicates a Count value will be produced.",all_items='no')
        
        miscelanousobj.select_menu_items('ITableData0', "3", "Rollup","Order Number INTEGER")
        
        """Expect to see two columns"""
        column=['Order Number INTEGER','Date MDYY']
        miscelanousobj.verify_column_heading('ITableData1',column, "Step 02: Expect to see two columns")
        """Expect to see 1000 rows"""
        miscelanousobj.verify_page_summary(1, "1000of1000records,Page1of18", "Step 02: Expect to see 1000 rows")
        
        """Expect to see two columns, 1000 rows, because all values of INTEGER are unique. Each value has an Date MDYY Count of 1."""
        
        utillobj.verify_popup_data_set("wall1", "ITableData1", "C2050516_Ds01.xlsx","Step 02: Verify table")
        #utillobj.create_popup_data_set("wall1", "ITableData1", "C2050516_Ds01.xlsx")
        miscelanousobj.close_popup_dialog("1")
        
        """
            Step 03: Select ALPHA Store Code as the Rollup column..
        """
        miscelanousobj.select_menu_items('ITableData0', "3", "Rollup","ALPHA Store Code")
        
        """Expect to see two columns"""
        coulumn_alpha=['ALPHA Store Code','Date MDYY']
        miscelanousobj.verify_column_heading('ITableData2',coulumn_alpha, "Step 03: Expect to see two columns")
        
        """Expect to see 12 rows"""
        miscelanousobj.verify_page_summary(2, "12of12records,Page1of1", "Step 03: Expect to see 12 rows")
        
        """Expect to see two columns, 12 rows, one for each unique Store Code. The second column contains a Count of Date MDYY to the Store Code level. 
        First six rows should have values 90, 90, 89, 90, 90 & 90."""
        
        
        utillobj.verify_popup_data_set("wall1", "ITableData2", "C2050516_Ds02.xlsx","Step 03: Verify table")
        #utillobj.create_popup_data_set("wall1", "ITableData2", "C2050516_Ds02.xlsx")
        miscelanousobj.close_popup_dialog("1")
        
        """
            Step 04: Select Date YYMD as the Rollup column.
        """
        miscelanousobj.select_menu_items('ITableData0', "3", "Rollup","Date YYMD")
        
        """Expect to see two columns"""
        column_yymd=['Date YYMD','Date MDYY']
        miscelanousobj.verify_column_heading('ITableData3',column_yymd, "Step 04: Expect to see two columns")
        
        """Expect to see 6 rows"""
        miscelanousobj.verify_page_summary(3, "6of6records,Page1of1", "Step 04: Expect to see 6 rows")
        
        """Expect to see two columns, 6 rows, one for each unique YYMD date. The second column contains a Count of Date MDYY to the YYMD level.
         Values should 180, 180, 180, 180, 180 & 100.."""
        utillobj.verify_popup_data_set("wall1", "ITableData3", "C2050516_Ds03.xlsx","Step 04: Verify table")
        #utillobj.create_popup_data_set("wall1", "ITableData3", "C2050516_Ds03.xlsx")
        miscelanousobj.close_popup_dialog("1")
        time.sleep(3)#conditional wait for make ready do the action
        """
            Step 05: Select Date MDYY as the Rollup column.
        """
        miscelanousobj.select_menu_items('ITableData0', "3", "Rollup","Date MDYY")
        
        """Expect to see two columns"""
        column_mdyy=['Date MDYY','Date MDYY']
        miscelanousobj.verify_column_heading('ITableData4',column_mdyy, "Step 05: Expect to see two columns")
        
        """Expect to see 6 rows"""
        miscelanousobj.verify_page_summary(4, "6of6records,Page1of1", "Step 05: Expect to see 6 rows")
        
        """Expect to see two columns, 6 rows, one for each unique MDYY date.
         The second column contains a Count of Date MDYY to the MDYY level. Values same as YYMD."""
        utillobj.verify_popup_data_set("wall1", "ITableData4", "C2050516_Ds04.xlsx","Step 05: Verify table")
        
        #utillobj.create_popup_data_set("wall1", "ITableData4", "C2050516_Ds04.xlsx")
        
        miscelanousobj.close_popup_dialog("1")
        time.sleep(3)#conditional wait for make ready do the action
        
        """
            Step 06: Select Date DMYY as the Rollup column.
        """
        miscelanousobj.select_menu_items('ITableData0', "3", "Rollup","Date DMYY")
        
        """Expect to see two columns"""
        column_dmyy=['Date DMYY','Date MDYY']
        miscelanousobj.verify_column_heading('ITableData5',column_dmyy, "Step 06: Expect to see two columns")
        
        """Expect to see 6 rows"""
        miscelanousobj.verify_page_summary(5, "6of6records,Page1of1", "Step 06: Expect to see 6 rows")
        
        """Expect to see two columns, 6 rows, one for each unique DMYY date.
            The second column contains a Count of Date MDYY to the DMYY level. Values same as YYMD."""
        utillobj.verify_popup_data_set("wall1", "ITableData5", "C2050516_Ds05.xlsx","Step 06: Verify table")
        
        #utillobj.create_popup_data_set("wall1", "ITableData5", "C2050516_Ds05.xlsx")
        
        miscelanousobj.close_popup_dialog("1")
        
        time.sleep(3)#conditional wait for make ready do the action
        
        """
            Step 07: Select D10.2 Unit Price as the Rollup column.
        """
        miscelanousobj.select_menu_items('ITableData0', "3", "Rollup","D10.2 Unit Price")
        
        """Expect to see two columns"""
        columnd_unit_price=['D10.2 Unit Price','Date MDYY']
        miscelanousobj.verify_column_heading('ITableData6',columnd_unit_price, "Step 07: Expect to see two columns")
        
        """Expect to see 10 rows"""
        miscelanousobj.verify_page_summary(6, "10of10records,Page1of1", "Step 07: Expect to see 10 rows")
        
        """Expect to see two columns, 10 rows, one for each Unit Price value. The second column containing a Count of Date MDYY to the D10.2 Unit Price level.
         The first 5 rows should have values 84, 99, 134, 148 & 84."""
         
        utillobj.verify_popup_data_set("wall1", "ITableData6", "C2050516_Ds06.xlsx","Step 07: Verify table")
        #utillobj.create_popup_data_set("wall1", "ITableData6", "C2050516_Ds06.xlsx")
        miscelanousobj.close_popup_dialog("1")
        
        time.sleep(3)#conditional wait for make ready do the action
        
        """
            Step 08: Select P9.2M Unit Price as the Rollup column.
        """
        miscelanousobj.select_menu_items('ITableData0', "3", "Rollup","P9.2M Unit Price")
        
        """Expect to see two columns"""
        column_p = ["P9.2M Unit Price",'Date MDYY']
        miscelanousobj.verify_column_heading('ITableData7',column_p, "Step 08: Expect to see two columns")
        
        """Expect to see  677 rows"""
        miscelanousobj.verify_page_summary(7, "677of677records,Page1of12", "Step 08: Expect to see 10 rows")
        
        """Expect to see two columns, 677 rows, one for each P9.2M Unit Price value. The second column containing a Count of Date MDYY to the P9.2M Unit Price level.
         All rows will have a Count of one, except for $59.00, &74.00, $75.00 & $84.00. Page down to verify these."""
        utillobj.verify_popup_data_set("wall1", "ITableData7", "C2050516_Ds07.xlsx","Step 08: Verify table")
        
        #utillobj.create_popup_data_set("wall1", "ITableData7", "C2050516_Ds07.xlsx")
        
        miscelanousobj.close_popup_dialog("1")
        time.sleep(3)#conditional wait for make ready do the action
        
        """
            Step 09: Select Datetime DATETIME HYYMDSA as the Rollup column.
        """
        miscelanousobj.select_menu_items('ITableData0', "3", "Rollup","DATETIME HYYMDSA")
        
        """Expect to see two columns"""
        column_datetime=["DATETIME HYYMDSA",'Date MDYY']
        miscelanousobj.verify_column_heading('ITableData8',column_datetime, "Step 09: Expect to see two columns")
        
        """Expect to see 4 rows"""
        miscelanousobj.verify_page_summary(8, "4of4records,Page1of1", "Step 09: Expect to see 4 rows")
        
        """Expect to see two columns, 4 rows, one for each unique DATETIME value.
        The second column contains a Count of Date MDYY to the DATETIME HYYMDSA level.
        Values should be 5, 5, 5, & 985."""
        utillobj.verify_popup_data_set("wall1", "ITableData8", "C2050516_Ds08.xlsx","Step 09: Verify table")
        #utillobj.create_popup_data_set("wall1", "ITableData8", "C2050516_Ds08.xlsx")
        miscelanousobj.close_popup_dialog("1")
        time.sleep(3)#conditional wait for make ready do the action
        
        """
            Step 10: End the Filter panel in preparation for the next field in the GROUP.
            Make sure the report is positioned at Page 1.
        """
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 10: Expect full report to be displayed again.1000 rows")
        
if __name__ == '__main__':
    unittest.main()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
