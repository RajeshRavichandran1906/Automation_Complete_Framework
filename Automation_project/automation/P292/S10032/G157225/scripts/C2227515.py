'''
Created on 24-OCT-2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227515
TestCase Name = Verify single-select Dynamic Filter using Define from master
'''
import unittest, time
from common.lib import utillity 
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, ia_run
 
class C2227515_TestClass(BaseTestCase):

    def test_C2227515(self):
        
        Test_Case_ID = "C2227515"
        
        driver = self.driver
        iarun=ia_run.IA_Run(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
                
        """
        1. Launch the IA API with CAR, Report mode:
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        2. Double click "COUNTRY", "CAR", "SALES".
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'COUNTRY', 30)
        metaobj.datatree_field_click("CAR", 2, 1)
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'CAR', 30)
        metaobj.datatree_field_click("SALES", 2, 1)
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'SALES', 30)
        parent_css="#TableChart_1 [id^='ActivePreviewItem']"
        resultobj.wait_for_property(parent_css, 6)
        coln_list = ['COUNTRY', 'CAR', 'SALES']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 02.01: Verify column titles")
        time.sleep(4)
        ia_resultobj.verify_report_data_set('TableChart_1', 10,3,'C2227515_Ds01.xlsx',"Step 02.02: Verify report data set")        
        
        """
        3. Drag "CAR" to Filter pane.
        """        
        metaobj.drag_drop_data_tree_items_to_filter("CAR", 1)
        utillobj.synchronize_with_number_of_element("#dlgWhere  #dlgWhere_btnOK", 1, 30)
        time.sleep(3)

        """
        4. Double-click <Value>, Select Type = "Parameter".
        5. Select "Static" radio button.
        6. Click "Get Values" (dropdown) > "All".
        7. Double click "AUDI", "BMW", "JAGUAR".
        8. Verify the selected values moved to "Multiple Values" area.
        9. Click "OK" (2x).
        """
        ia_ribbonobj.create_parameter_filter_condition('Static',['AUDI','BMW','JAGUAR'],getvalue_params='All')
        utillobj.synchronize_with_visble_text('#qbFilterBox table>tbody', 'CAR', 30)
        
        """
        10. Verify the following is displayed in the "Filter" pane.
        """
        metaobj.verify_filter_pane_field('CAR Equal to Static Parameter (Name: CAR, Values: AUDI, BMW, JAGUAR)', 1, "Step 10.01: Verify the filter pane")
       
        """
        11. Click "Run".
        """ 
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        
        """
        12. Verify the following autoprompt (CAR = AUDI) is displayed
        """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        iarun.verify_default_amper_value('CAR','AUDI',"Step 12.01: Verify Defualt amper value AUDI is displayed in run window")
        
        """
        13. Click the dropdown > Verify only the selected values are available
        14. Select "BMW", click "Run" in the output window.
        """
        iarun.select_amper_value('CAR', ['BMW'],False,verify_small_value_list=['AUDI','BMW','JAGUAR'])
        time.sleep(4)
        iarun.select_amper_menu('Run')
        
        """
        15. Verify the following report is displayed.
        """        
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[name="wfOutput"]')))
        time.sleep(3)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227515_Ds02.xlsx", "Step 15.01: verify data set")
        
        """
        16. Click "IA" > "Save" > "C2227515" > click Save
        """
        driver.switch_to.default_content()
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """
        17. Logout
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        18. Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2227515.fex&tool=report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.infoassist_api_edit('C2227515', 'report', 'S7385', mrid='mrid', mrpass='mrpass')
        time.sleep(15)
        
        """
        19. Verify canvas
        """
        parent_css="#TableChart_1 [id^='ActivePreviewItem']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css="#qbFilterBox table>tbody>tr img"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.verify_filter_pane_field('CAR Equal to Static Parameter (Name: CAR, Values: AUDI, BMW, JAGUAR)', 1, "Step 19.01: Verify the filter pane")
        time.sleep(4)
        ia_resultobj.verify_report_data_set('TableChart_1', 10,3, 'C2227515_Ds03.xlsx',"Step 19.02: Verify report data set")        
         
        """
        20. Logout
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()