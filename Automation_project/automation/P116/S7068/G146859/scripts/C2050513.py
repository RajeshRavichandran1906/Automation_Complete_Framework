'''
Created on Jul 28, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050513
Test case Name = Verify Rollup values using numeric field as the Rollup column.
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import time,unittest
from selenium.webdriver import ActionChains

class C2050513_TestClass(BaseTestCase):

    def test_C2050513(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050513'
        """
        Step 01: Execute the AR-RP-141CA.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-141CA.fex", "S7068", 'mrid', 'mrpass')
        active_misobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01: Execute AR-RP-141CA.fex verify Page Summary 1000of1000")
        
        """
        Step 02: For column Order Number INTEGER, select Rollup from the drop down option list.
        Select Order Number INTEGER as the Rollup column.
        Expect to see Group by (X)(SUM) which indicates a Total amount will be produced
        """  
#         time.sleep(5)      
        option='Group By (X)(SUM)'
#         active_misobj.verify_menu_items('ITableData0', 0, "Rollup",option,"Step 02: Expect to see Group By (X)(SUM) which indicates a Count value will be produced.",all_items='no')
        active_misobj.select_menu_items('ITableData0', 0, "Rollup","Order Number INTEGER")
        
        """Select Order Number INTEGER as the Rollup column."""
        column=['Order Number INTEGER','Order Number INTEGER']
        active_misobj.verify_column_heading('ITableData1',column, "Step 02: Expect to see two columns for Order Number INTEGER")
        """Expect to see two columns, 1000 rows, because all values are unique.
        Each value has a Count(column 2) that equals the INTEGER value."""
        active_misobj.verify_page_summary(1, "1000of1000records,Page1of18", "Step 02: Verify Page Summary 1000of1000")
        utillobj.verify_data_set('ITableData1','I1r', "C2050513_Ds01.xlsx","Step 02: Verify data set of Order Number INTEGER")
        time.sleep(4)
        active_misobj.close_popup_dialog("1")
        
        """
        Step 03: Select ALPHA Store Code as the Rollup column.
        """
        active_misobj.select_menu_items('ITableData0', 0 ,"Rollup","ALPHA Store Code")
        
        """Expect to see two columns, 12 rows, one for each unique Store Code. 
        The second column contains a sum of INTEGER to the Store Code level. 
        First six rows should have values 41220, 42570, 42965, 45255, 46605 & 47955."""
        column_alpha=['ALPHA Store Code','Order Number INTEGER']
        active_misobj.verify_column_heading('ITableData2',column_alpha, "Step 03: Expect to see two columns for ALPHA Store Code")

        active_misobj.verify_page_summary(2, "12of12records,Page1of1", "Step 03: Verify Page Summary 12of12")
        utillobj.verify_data_set('ITableData2','I2r',"C2050513_Ds02.xlsx","Step 03: Verify dat set for ALPHA Store Code")
        time.sleep(2)
        active_misobj.close_popup_dialog("1")
        
        """
        Step 04: Select Date YYMD as the Rollup column.
        """
        active_misobj.select_menu_items('ITableData0', 0, "Rollup","Date YYMD")
        
        """Expect to see two columns, 6 rows, one for each unique YYMD date. 
        The second column contains a sum of INTEGER to the YYMD level. 
        Values should be 16290, 48690, 81090, 113490, 145890 & 95050."""
        column_yymd=['Date YYMD','Order Number INTEGER']
        active_misobj.verify_column_heading('ITableData3',column_yymd, "Step 04: Expect to see two columns for YYMD")

        active_misobj.verify_page_summary(3, "6of6records,Page1of1", "Step 04: Verify Page Summary 6of6")
        utillobj.verify_data_set("ITableData3",'I3r', "C2050513_Ds03.xlsx","Step 04: Verify data set for YYMD")
        time.sleep(2)
        active_misobj.close_popup_dialog("1")
        
        """
        Step 05: Select Date MDYY as the Rollup column.
        """
        active_misobj.select_menu_items('ITableData0', 0, "Rollup","Date MDYY")
        
        """Expect to see two columns, 6 rows, one for each unique MDYY date. 
        The second column contains a sum of INTEGER to the MDYY level. Values the same as YYMD."""
        column_mdyy=['Date MDYY','Order Number INTEGER']
        active_misobj.verify_column_heading('ITableData4',column_mdyy, "Step 05: Expect to see two columns for MDYY")
        
        active_misobj.verify_page_summary(4, "6of6records,Page1of1", "Step 05: Verify Page Summary 6of6")
        utillobj.verify_data_set("ITableData4",'I4r', "C2050513_Ds04.xlsx","Step 05: Verify data set for MDYY")
        time.sleep(2)
        active_misobj.close_popup_dialog("1")
        
        """
        Step 06: Select Date DMYY as the Rollup column.
        """
        active_misobj.select_menu_items('ITableData0', 0, "Rollup","Date DMYY")
        
        """Expect to see two columns, 6 rows, one for each unique DMYY date. 
        The second column contains a sum of INTEGER to the DMYY level. 
        Values the same as YYMD."""
        column_dmyy=['Date DMYY','Order Number INTEGER']
        active_misobj.verify_column_heading('ITableData5',column_dmyy, "Step 06: Expect to see two columns for DMYY")
                
        active_misobj.verify_page_summary(5, "6of6records,Page1of1", "Step 06: Verify Page Summary 6of6")
        utillobj.verify_data_set("ITableData5",'I5r', "C2050513_Ds05.xlsx","Step 06: Verify data set for DMYY")
        time.sleep(2)
        active_misobj.close_popup_dialog("1")
        
        """
        Step 07: Select Date D10.2 Unit Price as the Rollup column.
        """
        active_misobj.select_menu_items('ITableData0', 0, "Rollup","D10.2 Unit Price")
        
        """Expect to see two columns, 10 rows, one for each unique D10.2 Unit Price value.
        The second column containing a sum of INTEGER to the D10.2 Unit Price level. 
        The first 5 rows should have values 42216, 49561, 67193, 74368 & 41377."""
        column_unit_price=['D10.2 Unit Price','Order Number INTEGER']
        active_misobj.verify_column_heading('ITableData6',column_unit_price, "Step 07: Expect to see two columns for D10.2 Unit Price")

        active_misobj.verify_page_summary(6, "10of10records,Page1of1", "Step 07: Verify Page Summary 10of10")
        utillobj.verify_data_set("ITableData6",'I6r',"C2050513_Ds06.xlsx","Step 07: Verify data set for D10.2 Unit Price")
        time.sleep(2)
        active_misobj.close_popup_dialog("1")
        
        """
        Step 08: Select P9.2M Unit Price as the Rollup column.
        """
        active_misobj.select_menu_items('ITableData0', 0, "Rollup","P9.2M Unit Price")
        
        """Expect to see two columns"""
        column_p = ["P9.2M Unit Price",'Order Number INTEGER']
        active_misobj.verify_column_heading('ITableData7',column_p, "Step 08: Expect to see two columns for P9.2M Unit Price")
        
        active_misobj.verify_page_summary(7, "677of677records,Page1of12", "Step 08: Verify Page Summary 677of677")
        utillobj.verify_data_set("ITableData7",'I7r',"C2050513_Ds07.xlsx","Step 08: Verify data set for P9.2M Unit Price")
        time.sleep(2)
        active_misobj.close_popup_dialog("1")
        
        """
        Step 09: Select Date DATETIME HYYMDSA as the Rollup column.
        """
        active_misobj.select_menu_items('ITableData0', 0, "Rollup","DATETIME HYYMDSA")
        
        """Expect to see two columns, 4 rows, one for each unique DATETIME value. 
        The second column containing a sum of INTEGER to the DATETIME HYYMDSA level. 
        Values should be 15, 40, 65 & 500380."""
        column_datetime=["DATETIME HYYMDSA","Order Number INTEGER"]
        active_misobj.verify_column_heading('ITableData8',column_datetime, "Step 09: Expect to see two columns for DATETIME HYYMDSA")
        
        
        active_misobj.verify_page_summary(8, "4of4records,Page1of1", "Step 09: Verify Page Summary 4of4")
        utillobj.verify_data_set("ITableData8",'I8r',"C2050513_Ds08.xlsx","Step 09: Verify data set for DATETIME HYYMDSA")
        time.sleep(2)
        active_misobj.close_popup_dialog("1")
        
        """
        Step 10: End the Filter panel in preparation for the next field in the GROUP.
        Make sure the report is positioned at Page 1.
        """        
        active_misobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 10: Verify Page Summary 1000of1000")
        
if __name__ == '__main__':
    unittest.main()      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        