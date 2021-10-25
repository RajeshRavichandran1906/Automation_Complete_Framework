'''
Created on Jul 27, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050518
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest
import time

class C2050518_TestClass(BaseTestCase):

    def test_C2050518(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050518'
        """
            Step 01: Execute the AR-RP-141CA.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-141CA.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01: Execute the AR-RP-141CA.fex")
        columns1=['Order Number INTEGER','ALPHA Store Code','Date YYMD','Date MDYY','Date DMYY','D10.2 Unit Price','P9.2M Unit Price', 'DATETIME HYYMDSA']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 01: Verify all columns listed on the report')

        
        """
            Step 02: For column D10.2 Unit Price, select Rollup from the drop down option list.
            Select Order Number INTEGER as the Rollup column
        """
        option='Group By (X)(SUM)'
        miscelanousobj.verify_menu_items('ITableData0', 5, "Rollup",option,"Step 02: Expect to see Group by (X)(SUM) which indicates a Count value will be produced.",all_items='no')
        
        miscelanousobj.select_menu_items('ITableData0', "5", "Rollup","Order Number INTEGER")
        
        """Expect to see two columns"""
        column=['Order Number INTEGER','D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData1',column, "Step 02: Expect to see two columns")
        """Expect to see 1000 rows"""
        miscelanousobj.verify_page_summary(1, "1000of1000records,Page1of18", "Step 02: Expect to see 1000 rows")
        
        """Each value has a D10.2 Unit Price has the value from the detail row.."""
        utillobj.verify_data_set("ITableData1", "I1r","C2050518_Ds01.xlsx","Step 02: Verify table")
        time.sleep(4)
        miscelanousobj.close_popup_dialog("1")
        
        """
            Step 03: Select ALPHA Store Code as the Rollup column.
        """
        miscelanousobj.select_menu_items('ITableData0', "5", "Rollup","ALPHA Store Code")
        
        """Expect to see two columns"""
        coulumn_alpha=['ALPHA Store Code','D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData2',coulumn_alpha, "Step 03: Expect to see two columns")
        
        """Expect to see 12 rows"""
        miscelanousobj.verify_page_summary(2, "12of12records,Page1of1", "Step 03: Expect to see 12 rows")
        
        """The second column contains a Sum of D10.2 Unit Price to the Store Code level. 
        First six rows should have values 5,226.00, 5,226.00, 5,299.00, 5,358.00, 5,388.00 & 5,358.00"""
        utillobj.verify_data_set("ITableData2", "I2r","C2050518_Ds02.xlsx","Step 03: Verify table")
        time.sleep(4)
        miscelanousobj.close_popup_dialog("1")
        
        """
            Step 04: Select Date YYMD as the Rollup column.
        """
        miscelanousobj.select_menu_items('ITableData0', "5", "Rollup","Date YYMD")
        
        """Expect to see two columns"""
        column_yymd=['Date YYMD','D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData3',column_yymd, "Step 04: Expect to see two columns")
        
        """Expect to see 6 rows"""
        miscelanousobj.verify_page_summary(3, "6of6records,Page1of1", "Step 04: Expect to see 6 rows")
        
        """The second column contains a Sum of D10.2 Unit Price to the YYMD level.
        Values should be 10,698.00 for the first 5 rows and 6,013.00 for the last row."""
        utillobj.verify_data_set("ITableData3", "I3r","C2050518_Ds03.xlsx","Step 04: Verify table")
        time.sleep(4)
        miscelanousobj.close_popup_dialog("1")
        
        """
            Step 05: Select Date MDYY as the Rollup column.
        """
        
        miscelanousobj.select_menu_items('ITableData0', "5", "Rollup","Date MDYY")
        
        """Expect to see two columns"""
        column_mdyy=['Date MDYY','D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData4',column_mdyy, "Step 05: Expect to see two columns")
        
        """Expect to see 6 rows"""
        miscelanousobj.verify_page_summary(4, "6of6records,Page1of1", "Step 05: Expect to see 6 rows")
        
        """The second column contains a Sum of D10.2 Unit Price to the MDYY level. Values same as YYMD."""
        utillobj.verify_data_set("ITableData4", "I4r","C2050518_Ds04.xlsx","Step 05: Verify table")
        time.sleep(4)
        miscelanousobj.close_popup_dialog("1")
        
        """
            Step 06: Select Date DMYY as the Rollup column.
        """
        miscelanousobj.select_menu_items('ITableData0', "5", "Rollup","Date DMYY")
        
        """Expect to see two columns"""
        column_dmyy=['Date DMYY','D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData5',column_dmyy, "Step 06: Expect to see two columns")
        
        """Expect to see 6 rows"""
        miscelanousobj.verify_page_summary(5, "6of6records,Page1of1", "Step 06: Expect to see 6 rows")
        
        """The second column contains a Sum of D10.2 Unit Price to the DMYY level. Values same as YYMD"""
        utillobj.verify_data_set("ITableData5", "I5r","C2050518_Ds05.xlsx","Step 06: Verify table")
        time.sleep(4)
        miscelanousobj.close_popup_dialog("1")
        
        """
            Step 07: Select D10.2 Unit Price as the Rollup column.
        """
        miscelanousobj.select_menu_items('ITableData0', "5", "Rollup","D10.2 Unit Price")
        
        """Expect to see two columns"""
        columnd_unit_price=['D10.2 Unit Price','D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData6',columnd_unit_price, "Step 07: Expect to see two columns")
        
        """Expect to see 10 rows"""
        miscelanousobj.verify_page_summary(6, "10of10records,Page1of1", "Step 07: Expect to see 10 rows")
        
        """The second column containing a Sum of D10.2 Unit Price to the D10.2 Unit Price level. 
        The first 5 rows should have values 1,092.00, 1,683.00, 3,484.00, 4,144.00 & 4,872.00."""
        utillobj.verify_data_set("ITableData6", "I6r","C2050518_Ds06.xlsx","Step 07: Verify table")
        time.sleep(6)
        miscelanousobj.close_popup_dialog("1")
        time.sleep(3)
        """
            Step 08:Select P9.2M Unit Price as the Rollup column.
        """
        miscelanousobj.select_menu_items('ITableData0', "5", "Rollup","P9.2M Unit Price")
        
        """Expect to see two columns"""
        column_p = ["P9.2M Unit Price",'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData7',column_p, "Step 08: Expect to see two columns")
        
        """Expect to see  677 rows"""
        miscelanousobj.verify_page_summary(7, "677of677records,Page1of12", "Step 08: Expect to see 10 rows")
        
        """The second column containing a Sum of D10.2 Unit Price to the P9.2M Unit Price level. 
        Values for the first 6 rows should be 13.00, 13.00, 17.00, 26.00, 26.00 & 13.00.."""
        utillobj.verify_data_set("ITableData7", "I7r","C2050518_Ds07.xlsx","Step 08: Verify table")
        time.sleep(6)
        miscelanousobj.close_popup_dialog("1")
        time.sleep(3)
        """
            Step 09: Select Datetime DATETIME HYYMDSA as the Rollup column.
        """
        miscelanousobj.select_menu_items('ITableData0', "5", "Rollup","DATETIME HYYMDSA")
        
        """Expect to see two columns"""
        column_datetime=["DATETIME HYYMDSA","D10.2 Unit Price"]
        miscelanousobj.verify_column_heading('ITableData8',column_datetime, "Step 09: Expect to see two columns")
        """Expect to see 4 rows"""
        miscelanousobj.verify_page_summary(8, "4of4records,Page1of1", "Step 09: Expect to see 4 rows")
        
        """. The second column contains a Sum of D10.2 Unit Price to the DATETIME HYYMDSA level. Values should be 359.00, 413.00, 99.00 & 58,632.00"""
        utillobj.verify_data_set("ITableData8", "I8r","C2050518_Ds08.xlsx","Step 09: Verify table")
        time.sleep(6)
        miscelanousobj.close_popup_dialog("1")
        time.sleep(2)
        
        """
            Step 10: End the Filter panel in preparation for the next field in the GROUP.
            Make sure the report is positioned at Page 1.
        """
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 10: Expect full report to be displayed again.1000 rows")
        
if __name__ == '__main__':
    unittest.main()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        