'''
Created on Jul 26, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050520
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2050520_TestClass(BaseTestCase):

    def test_C2050520(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        Step 01: 
        Execute the AR-RP-001.fex
        
        """
        utillobj.active_run_fex_api_login("AR-RP-141CA.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01.1: Execute the AR-RP-141CA.fex")
        columns=['Order Number INTEGER', 'ALPHA Store Code', 'Date YYMD', 'Date MDYY', 'Date DMYY', 'D10.2 Unit Price', 'P9.2M Unit Price', 'DATETIME HYYMDSA']
        miscelanousobj.verify_column_heading('ITableData0', columns, 'Step 01.2: Verify column heading')
        """
        Step 02: 
        Execute AR-RP-141CA to produce the mixed field output report.
        For column DATETIME HYYMDSA, select Rollup from the drop down option list.
        Select Order Number INTEGER as the Rollup column.
        Expected:
        Expect to see Group by (X)(COU) which indicates a Count value will be produced.
        Expect to see two columns, 1000 rows, because all values of INTEGER are unique. Each value has a DATETIME HYYMDSA Count of 1
        """
        miscelanousobj.verify_menu_items('ITableData0', 7, 'Rollup', 'Group By (X)(COU)', "Step 02.1: Expect to see Group by (X)(COU) which indicates a Count value will be produced.", all_items='no')
        miscelanousobj.select_menu_items('ITableData0', 7, 'Rollup','Order Number INTEGER')
        miscelanousobj.verify_column_heading('wall1', ['Order Number INTEGER', 'DATETIME HYYMDSA'], 'Step 02.2: Expect to see two columns')
        miscelanousobj.verify_page_summary(1, '1000of1000records,Page1of18', 'Step 02.3: Expect to see 1000 rows in the heading')
        utillobj.verify_data_set('ITableData1', 'I1r', 'C2050520_Ds01.xlsx', 'Step 02.4: Verify Each value has a DATETIME HYYMDSA Count of 1')
        miscelanousobj.close_popup_dialog('1')
        
        """
        Step 03: Select ALPHA Store Code as the Rollup column.
        Expect to see two columns, 12 rows, one for each unique Store Code. 
        The second column contains a Count of field HYYMDSA to the Store Code level. 
        First six rows should have values 90, 90, 89, 90, 90 & 90.
        """
        miscelanousobj.select_menu_items('ITableData0', 7, 'Rollup','ALPHA Store Code')
        miscelanousobj.verify_page_summary(2, '12of12records,Page1of1', 'Step 03.1: Expect to see 12 rows, one for each unique Store Code')
        miscelanousobj.verify_column_heading('wall1', ['ALPHA Store Code', 'DATETIME HYYMDSA'], 'Step 03.2: Expect to see two columns')
        utillobj.verify_data_set('ITableData2', 'I2r', 'C2050520_Ds02.xlsx', 'Step 03.3: Verify second column contains a Count of field HYYMDSA to the Store Code level')
        miscelanousobj.close_popup_dialog('1')
        
        """
        Step 04: Select Date YYMD as the Rollup column.
        Expect to see two columns, 6 rows, one for each unique YYMD date. 
        The second column contains a Count of field HYYMDSA to the YYMD level. 
        Values should 180, 180, 180, 180, 180 & 100.
        """
        miscelanousobj.select_menu_items('ITableData0', 7, 'Rollup','Date YYMD')
        miscelanousobj.verify_page_summary(3, '6of6records,Page1of1', 'Step 04.1: Expect to see 6 rows, one for each unique YYMD date')
        miscelanousobj.verify_column_heading('wall1', ['Date YYMD', 'DATETIME HYYMDSA'], 'Step 04.2: Expect to see two columns')
        utillobj.verify_data_set('ITableData3', 'I3r', 'C2050520_Ds03.xlsx', 'Step 04.3: Verify second column contains a Count of field HYYMDSA to the YYMD level')
        miscelanousobj.close_popup_dialog('1')
        
        """
        Step 05: Select Date MDYY as the Rollup column.
        Expect to see two columns, 6 rows, one for each unique MDYY date. 
        The second column contains a Count of field HYYMDSA to the MDYY level. 
        Values same as YYMD.
        """
        miscelanousobj.select_menu_items('ITableData0', 7, 'Rollup','Date MDYY')
        miscelanousobj.verify_page_summary(4, '6of6records,Page1of1', 'Step 05.1: Expect to see 6 rows, one for each unique MDYY date')
        miscelanousobj.verify_column_heading('wall1', ['Date MDYY', 'DATETIME HYYMDSA'], 'Step 05.2: Expect to see two columns')
        utillobj.verify_data_set('ITableData4', 'I4r', 'C2050520_Ds04.xlsx', 'Step 05.3: Verify second column contains a Count of field HYYMDSA to the MDYY level')
        miscelanousobj.close_popup_dialog('1')
        
        """
        Step 06: Select Date DMYY as the Rollup column.
        Expect to see two columns, 6 rows, one for each unique DMYY date. 
        The second column contains a Count of field HYYMDSA to the DMYY level. Values same as YYMD.
        """
        miscelanousobj.select_menu_items('ITableData0', 7, 'Rollup','Date DMYY')
        miscelanousobj.verify_page_summary(5, '6of6records,Page1of1', 'Step 06.1: Expect to see 6 rows, one for each unique DMYY date')
        miscelanousobj.verify_column_heading('wall1', ['Date DMYY', 'DATETIME HYYMDSA'], 'Step 06.2: Expect to see two columns')
        utillobj.verify_data_set('ITableData5', 'I5r', 'C2050520_Ds05.xlsx', 'Step 06.3: Verify second column contains a Count of field HYYMDSA to the DMYY level')
        miscelanousobj.close_popup_dialog('1')
        
        """
        STEp 07: Select D10.2 Unit Price as the Rollup column.
        Expect to see two columns, 10 rows, one for each unique Unit Price value. 
        The second column contains a Count of field HYYMDSA to the D10.2 level. 
        The first 5 rows should have values 84, 99, 134, 148 & 84.
        """
        miscelanousobj.select_menu_items('ITableData0', 7, 'Rollup','D10.2 Unit Price')
        miscelanousobj.verify_page_summary(6, '10of10records,Page1of1', 'Step 07.1: Expect to see 10 rows, one for each unique D10.2 Unit Price')
        miscelanousobj.verify_column_heading('wall1', ['D10.2 Unit Price', 'DATETIME HYYMDSA'], 'Step 07.2: Expect to see two columns')
        utillobj.verify_data_set('ITableData6', 'I6r', 'C2050520_Ds06.xlsx', 'Step 07.3: Verify second column contains a Count of field HYYMDSA to the D10.2 level')
        miscelanousobj.close_popup_dialog('1')
        
        
        """
        Step 08: Select P9.2M Unit Price as the Rollup column.
        Expect to see two columns, 677 rows, one for each P9.2M Unit Price value. 
        The second column containing a Count of field HYYMDSA to the P9.2M level. 
        All rows will have a Count of one, except for $59.00, &74.00, $75.00 & $84.00. Page down to verify these.
        """
        miscelanousobj.select_menu_items('ITableData0', 7, 'Rollup','P9.2M Unit Price')
        miscelanousobj.verify_page_summary(7, '677of677records,Page1of12', 'Step 08.1: Expect to see 677 rows, one for each unique P9.2M Unit Price')
        miscelanousobj.verify_column_heading('wall1', ['P9.2M Unit Price', 'DATETIME HYYMDSA'], 'Step 08.2: Expect to see two columns')
        utillobj.verify_data_set('ITableData7', 'I7r', 'C2050520_Ds07.xlsx', 'Step 08.3: Verify second column contains a Count of field HYYMDSA to the P9.2M level')
        miscelanousobj.close_popup_dialog('1')
        
        
        """
        STep 09: Select Datetime DATETIME HYYMDSA as the Rollup column.
        Expect to see two columns, 4 rows, one for each unique DATETIME value. 
        The second column contains a Count of field HYYMDSA to the DATETIME HYYMDSA level. 
        Values should be 5, 5, 5, & 985.
        """
        miscelanousobj.select_menu_items('ITableData0', 7, 'Rollup','DATETIME HYYMDSA')
        miscelanousobj.verify_page_summary(8, '4of4records,Page1of1', 'Step 09.1: Expect to see 4 rows, one for each unique DATETIME HYYMDSA')
        miscelanousobj.verify_column_heading('wall1', ['DATETIME HYYMDSA', 'DATETIME HYYMDSA'], 'Step 09.2: Expect to see two columns')
        utillobj.verify_data_set('ITableData8', 'I8r', 'C2050520_Ds08.xlsx', 'Step 09.3: Verify second column contains a Count of field HYYMDSA to the DATETIME HYYMDSA level')
        miscelanousobj.close_popup_dialog('1')
        
        """
        Step 10: End the Filter panel in preparation for the next field in the GROUP.
        Make sure the report is positioned at Page 1.
        Expect full report to be displayed again.1000 rows
        """
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 10: Expect full report to be displayed again.1000 rows")
        
        
if __name__ == '__main__':
    unittest.main()         
        
        
        
        
        
