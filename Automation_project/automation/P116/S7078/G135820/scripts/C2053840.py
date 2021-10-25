'''
Created on Aug 29, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053840
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_pivot_comment
from common.lib import utillity


class C2053840_TestClass(BaseTestCase):

    def test_C2053840(self):
        
        """
        Step 01: Execute the attached repro - AR_RP_CALCULATE.fex
                Create a new Pivot Table by selecting P9.2M Unit Price and from the drop down list,
                select Pivot(Cross Tab), move to Group BY(SUM) and select ALPHA Store Code, move to Across and select Date YYMD for the Across
        """
        
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        pivotobj=active_pivot_comment.Active_Pivot_Comment(self.driver)
        utillobj.active_run_fex_api_login("AR_RP_CALCULATE.fex", "S7078", 'mrid', 'mrpass')
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table[id='IWindowBody0'] .arGridBar table")))
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01: Execute the AR_RP_CALCULATE.fex")
        columnslist=['Order Number INTEGER', 'ALPHA Store Code', 'Date YYMD', 'Date MDYY', 'Date DMYY', 'D10.2 Unit Price', 'P9.2M Unit Price', 'Datetime HYYMDSA']
        miscelanousobj.verify_column_heading("ITableData0", columnslist, 'Step 01a: Verify all columns listed on the report')
        miscelanousobj.select_menu_items('ITableData0', "6", "Pivot (Cross Tab)","ALPHA Store Code","Date YYMD")
        utillobj.verify_pivot_data_set("piv1", "C2053840_Ds01.xlsx", "Step 01b: Expect to see a Pivot Table")
        
        """
        Step 02: From the options bar, click the third icon which says Sum and select Avg from the drop down list.
        """
        pivotobj.select_aggregate_function("wall1", 0, "Avg", True)
        utillobj.verify_pivot_data_set("piv1", "C2053840_Ds02.xlsx", "Step 02: Expect the Pivot Table to reflect Averages.")
        """
        Step 03: From the options bar, click the third icon which now says Avg and change it to Min.
        """
        pivotobj.select_aggregate_function("wall1", 1, "Min", True)
        utillobj.verify_pivot_data_set("piv1", "C2053840_Ds03.xlsx", "Step 03: Expect the Pivot Table to reflect Minimums.")
        """
        Step 04: From the options bar, click the third icon which now says Min and change it to Max.
        """
        pivotobj.select_aggregate_function("wall1", 1, "Max", True)
        utillobj.verify_pivot_data_set("piv1", "C2053840_Ds04.xlsx", "Step 04: Expect the Pivot Table to reflect Maximums.")
        """
        Step 05: From the options bar, click the third icon which now says Max and change it to Count.
        """
        pivotobj.select_aggregate_function("wall1", 1, "Count", True)
        utillobj.verify_pivot_data_set("piv1", "C2053840_Ds05.xlsx", "Step 05: Expect the Pivot Table to reflect Counts.")
        """
        Step 06: From the options bar, click the third icon which now says Count and change it to Distinct.
        """
        pivotobj.select_aggregate_function("wall1", 1, "Distinct", True)
        utillobj.verify_pivot_data_set("piv1", "C2053840_Ds06.xlsx", "Step 06: Expect the Pivot Table to reflect Distinct Counts.")
        """
        Step 07: From the options bar, click the third icon which now says Distinct and change it back to the original SUM.
        """
        pivotobj.select_aggregate_function("wall1", 1, "Sum", True)
        utillobj.verify_pivot_data_set("piv1", "C2053840_Ds01.xlsx", "Step 07: Expect the Pivot Table to reflect the original Sum totals")

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
