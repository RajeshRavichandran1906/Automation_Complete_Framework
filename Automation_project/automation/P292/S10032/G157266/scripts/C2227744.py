'''
Created on Jan 25, 2018
@author: KS13172/Updated by :Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227744
TestCase Name = Report Other: Verify that data on an Accordion report can be expanded and compressed of its detail.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity, core_utility
from common.wftools import active_report

class C2227744_TestClass(BaseTestCase):

    def test_C2227744(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227744'
        fex_name ="Accordion.fex"
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj=core_utility.CoreUtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        
        """
        Step 01 : Sign in to WebFOCUS as a basic user
        Step 02 :Expand folder P292_S10032_G157266
                http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=Accordion.fex
        Step03: Verify the report is generated.Verify Active Report is displayed with collapse sign(+) under Category column.
        """
        
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 #TCOL_0_C_0 span", synchronize_visible_element_text="Category")
#         utillobj.create_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 03: Verify the accordion report")
                
        """
        Step04: Click the plus sign(+) next to the Coffee sort column.
        Verify that the Category for Coffee has expanded and now shows its values of:
        C141, C142 & C144, all of which also have + signs next to their values.
        """
        plus=self.driver.find_element_by_css_selector("td[id^='I0r0'] span[onclick*='expand']")
        core_utillobj.left_click(plus)
#         utillobj.create_data_set('ITableData0','I0r',Test_Case_ID+'_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds02.xlsx',"Step 04: Verify the Category Coffee expanded report")
         
        """
        Step05: Click the plus sign(+) next to the C142 value.
        Verify that the Product ID has expanded for C142 and now shows its value of:
        Latte.
        """
        plus=self.driver.find_element_by_css_selector("td[id^='I0r11'] span[onclick*='expand']")
        core_utillobj.left_click(plus)
#         utillobj.create_data_set('ITableData0','I0r',Test_Case_ID+'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds03.xlsx',"Step 05: Verify the C142 expanded report")
         
        """
        Step06: Click the plus sign(+) next to the Latte.
        Verify that the Product ID has expanded for Latte and now shows its lowest level of 11 states, starting with CA and ending with WA.
        """
        plus=self.driver.find_element_by_css_selector("td[id^='I0r11.1C2'] span[onclick*='expand']")
        core_utillobj.left_click(plus)
#         utillobj.create_data_set('ITableData0','I0r',Test_Case_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds04.xlsx',"Step 06: Verify the Latte expanded report")
         
        """
        Step07: Click Category > Accordion > Expand all option
        Verify that all Categories, Product IDs, Products have been expanded to the State level, showing Unit Sales & Dollar Sales.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Accordion','Expand All')   
#         utillobj.create_data_set('ITableData0','I0r',Test_Case_ID+'_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds05.xlsx',"Step 07: Verify the report after Expand All")
         
        """
        Step 08: Click Category > Accordion > Collapse All option
        Expect to see the original collapsed report, showing only the Categories of Coffee, Food & Gifts.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Accordion','Collapse All')        
#         utillobj.create_data_set('ITableData0','I0r',Test_Case_ID+'_Ds06.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds06.xlsx',"Step 08: Verify the report after Collapse All")
       
if __name__ == '__main__':
    unittest.main()

