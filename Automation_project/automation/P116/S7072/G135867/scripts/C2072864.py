'''
Created on Aug 5, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2072864
Test Case name = AHTML: Cannot change the font color of the current row(ACT-645).
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, ia_run
from common.lib import utillity
from selenium.webdriver.common.action_chains import ActionChains


class C2072864_TestClass(BaseTestCase):

    def test_C2072864(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2072864'
        """
            Step 01: Execute the attached repro - ACT-645.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_mis= active_miscelaneous.Active_Miscelaneous(self.driver)
        run_obj=ia_run.IA_Run(self.driver)
        browser=utillobj.parseinitfile('browser')
        utillobj.active_run_fex_api_login("ACT-645.fex", "S7072", 'mrid', 'mrpass')
#         utillobj.switch_to_frame(pause=2)
        active_mis.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Verify Page Summary of ACT-645.fex")
        active_mis.verify_column_heading('ITableData0', ['COUNTRY','CAR','MODEL','SALES','DEALER_COST','RETAIL_COST'], "Step 01.2: Verify Column heading of ACT-645.fex")
        utillobj.verify_data_set('ITableData0','I0r','ACT-645.xlsx', "Step 01.3: Verify ACT-645.fex dataset")
         
        """
        Step 02: Hover over the cell containing Alfa Romeo.
        Expect to see a the row highlighted in Red with White text.
        """
#         time.sleep(9)
        hover_ele=self.driver.find_element_by_css_selector("table[id='ITableData0'] > tbody > tr:nth-child(7) > td:nth-child(2)")
        if browser=='Firefox':
            utillity.UtillityMethods.click_type_using_pyautogui(self, hover_ele)
        else:
            ActionChains(self.driver).move_to_element(hover_ele).perform()
        ''' "These line of code help full whenever we want to extract value through regular expression"
        actual_text_color=alpha_romeo.get_attribute("style")
        print(actual_text_color)
        r,g,b = map(int, re.search(r'color:*[A-Za-z]\((\d+),\s*(\d+),\s*(\d+)\)', actual_text_color).groups())
        print('{:X}{:X}{:X}'.format(r, g, b))
        utillity.UtillityMethods.asin(self, actual_text_color, expected_text_color, "Step 02.2: Verify highlighted row text colour is White")'''
        
        run_obj.verify_table_cell_property("table[id='ITableData0']", 7, 2, bg_color='red', font_color='white', msg="Step 02: Verify highlighted row")
         
        """
        Step 03: Left-click the cell and select Highlight Value.
        """
        active_mis.select_field_menu_items('ITableData0', 5, 1,'Highlight Value')
        element=driver.find_element_by_css_selector("#IWindowBody0 .arGridBar")
        utillobj.click_type_using_pyautogui(element)
        
        """Expect to see all three rows for Alfa Romeo, highlighted in Green, with normal Black text."""
        utillobj.verify_data_set_old('ITableData0','bgcolor',Test_Case_ID+'_Ds01.xlsx',"Step 03: Verify dataset highlighted with green color", color='green')
          
        """
        Step 4: Hover over the cell for Audi.
        Expect to see the row highlighted in Red with White text.
        Expect to still see the three Green rows for Alfa Romeo
        """
        hover_obj=self.driver.find_element_by_css_selector("table[id='ITableData0'] > tbody > tr:nth-child(13) > td:nth-child(2)")
        if browser=='IE':
            ActionChains(self.driver).move_to_element(hover_obj).perform()
        else:
            utillobj.click_type_using_pyautogui(hover_obj)
        utillobj.synchronize_with_number_of_element("table[id='ITableData0'] > tbody > tr:nth-child(13) > td[style*='rgb']:nth-child(2)", 1, 5)
        run_obj.verify_table_cell_property("table[id='ITableData0']", 13, 2, bg_color='red', font_color='white', msg="Step 04: Verify highlighted row")
            

        """
        Step 05: Left-click Audi and select Highlight Row.
        """
        active_mis.select_field_menu_items('ITableData0', 11, 1,'Highlight Row')
        element=driver.find_element_by_css_selector("#IWindowBody0 .arGridBar")
        utillobj.click_type_using_pyautogui(element)
        
        """Expect to see the single row for Audi highlighted in Green."""
        utillobj.verify_data_set_old('ITableData0','bgcolor',Test_Case_ID+'_Ds02.xlsx',"Step 05.2: Verify ALFA ROMEO dataset highlighted with green color", color='green')
         
        """
        Step 06: Left-click in any cell on the report and select Unhighlight all.
        """
        active_mis.select_field_menu_items('ITableData0', 11, 1,'Unhighlight All')
        """Expect to see the Highlighling for both the Alfa Romeo and Audi removed.
        The report should appear as it did in step 1."""
        active_mis.verify_cell_property('ITableData0', 11, 1,'AUDI', 'Step 06.1: Verify row "AUDI" highlighted in transparent with black text.', text_color='black', bg_color='transparent')
        active_mis.verify_cell_property('ITableData0', 5, 1,'ALFA ROMEO', 'Step 06.2: Verify row "ALFA ROMEO" highlighted in transparent with black text.', text_color='black', bg_color='transparent')
        
if __name__ == '__main__':
    unittest.main()