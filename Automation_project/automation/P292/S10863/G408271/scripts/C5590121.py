'''
Created on Apr 25, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5590121
TestCase Name = Verify multi-select Dynamic Filter
'''

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, ia_run
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C5590121_TestClass(BaseTestCase):

    def test_C5590121(self):
        
        Test_Case_ID = "C5590121"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
                
        """
        1. Launch the IA API with CAR, Report mode:
        """
        utillobj.invoke_infoassist_api_login('report','ibisamp/car','P292_S10863/G408271', 'mrid', 'mrpass')
        elem1="#TableChart_1"
        utillobj.synchronize_with_number_of_element(elem1, 1, 30)
        time.sleep(10)
        
        """
        2. Drag/drop COUNTRY field to Filter Pane.
        """     
        metaobj.drag_drop_data_tree_items_to_filter("COUNTRY", 1)   
        time.sleep(1)

        """
        3. Double-click <Value>, Select Type = "Parameter".
        4. Select "Dynamic" radio button.
        5. Check off "Select multiple values at runtime"
        6. Click "OK" (2x).
        """
        ia_ribbonobj.create_parameter_filter_condition('Dynamic', ['COUNTRY'],ParamMultiple=True)
        
        """
        7. Verify filter is created.
        """
        metaobj.verify_filter_pane_field('COUNTRY Equal to Multiselect Dynamic Parameter (Name: COUNTRY, Field: COUNTRY in CAR) Sort Ascending', 1, "Step 07: Verify the filter pane")
       
        """
        8. Add fields "COUNTRY", "SALES".
        """
        time.sleep(2)
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4) 
        metaobj.datatree_field_click("SALES", 2, 1)
        time.sleep(4)
        coln_list = ['COUNTRY', 'SALES']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 08: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 5,2,'C5590121_Ds01.xlsx',"Step 08: Verify report data set")        
        
        """
        09. Click "Run".
        """ 
        elem1="#applicationButton img"
        utillobj.synchronize_with_number_of_element(elem1, 1, 30)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        
        """
        10. Click the "All Values" dropdown menu > check off "ENGLAND" and "ITALY"
        """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        iarun.verify_default_amper_value('COUNTRY','All Values',"Step 10: Verify Defualt amper value All Values in run window")
        iarun.select_amper_value('COUNTRY', ['ENGLAND','ITALY'],False)
        
        """
        11. Click "Run" in the AutoPrompt window
        """        
        time.sleep(4)
        iarun.select_amper_menu('Run')
        
        """
        12. Verify it generated the following output.
        """        
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[name="wfOutput"]')))
        time.sleep(4)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C5590121_Ds02.xlsx", "Step 12: verify data set")
        
        """
        13. Click "IA" > Save > "C2071376" > click Save
        """
        driver.switch_to.default_content()
        elem1="#applicationButton img"
        utillobj.synchronize_with_number_of_element(elem1, 1, 30)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
         
        """
        14. Logout
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
         
        """
        15. Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2227516.fex&tool=report
        """
        elem1="input[id=SignonUserName]"
        utillobj.synchronize_with_number_of_element(elem1, 1, 30)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit_(Test_Case_ID, 'report', 'P292_S10863/G408271')
        elem1="#TableChart_1"
        utillobj.synchronize_with_number_of_element(elem1, 1, 30)
         
        """
        16. Verify Filter
        """
        metaobj.verify_filter_pane_field('COUNTRY Equal to Multiselect Dynamic Parameter (Name: COUNTRY, Field: COUNTRY in CAR) Sort Ascending', 1, "Step 16: Verify the filter pane")
        time.sleep(4)
        ia_resultobj.verify_report_data_set('TableChart_1', 5,2,'C5590121_Ds03.xlsx',"Step 16: Verify report data set")        
          
        """
        17. Logout:
        """
        utillobj.infoassist_api_logout()
         
if __name__ == '__main__':
    unittest.main()