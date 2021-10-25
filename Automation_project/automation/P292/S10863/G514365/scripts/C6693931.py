'''
Created on Sep 12, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6693931
TestCase Name = Verify simple prompt
'''

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, ia_run
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C6693931_TestClass(BaseTestCase):

    def test_C6693931(self):
        
        """Testcase variables"""
        Test_Case_ID = "C6693931"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
         
        table_css="#TableChart_1"
        filterdialog_css = "#dlgWhere [class*='active'] [class*='caption'] [class*='bi-label']"
        parent_css="#applicationButton img"
        field_css="div[class='autop-amper-ctrl-container'] div[class^='autop-amper']"
        
        coln_list = ['ProductCategory', 'Revenue']
        expected_text = 'Create a filtering condition'
        field_name='Product Category'
        input_text="Computers"
        synchronize_time=50
        sleep_time=[2,3,4,5]
                
        """
        Step 01: Create new IA report using WF_retail_lite
        http://machine:port/alias/ia?is508=false&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10117%2FG456746&tool=report&master=baseapp/wf_retail_lite
        """
        utillobj.invoke_infoassist_api_login('report','baseapp/wf_retail_lite','P292_S10863/G514365', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(table_css, 1, synchronize_time)
         
        """
        Step 02: Double click "Product,Category" and "Revenue" fields.
        """
        time.sleep(sleep_time[2]) 
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(sleep_time[2]) 
        metaobj.datatree_field_click("Revenue", 2, 1)
         
        """
        Step 02.1: Verify the following report is displayed.
        """
        time.sleep(sleep_time[2])
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 02.1: Verify column titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 7,2, Test_Case_ID+'_Ds01.xlsx',no_of_cells=4)
        ia_resultobj.verify_report_data_set('TableChart_1', 7,2, Test_Case_ID+'_Ds01.xlsx',"Step 02.2: Verify report data set",no_of_cells=4) 
         
        """
        Step 03. Drag "Product,Category" field into the Filter pane.
        """        
        metaobj.drag_drop_data_tree_items_to_filter("Product,Category", 1)
        time.sleep(sleep_time[2]) 
         
        """
        Step 03.1: Verify Create a filtering condition window opens.
        """   
        utillobj.synchronize_with_number_of_element(filterdialog_css, 1, synchronize_time)
        utillobj.verify_object_visible(filterdialog_css, True, 'Step 03.1: Verify Create a filtering condition window appears.')
        utillobj.verify_element_text(filterdialog_css, expected_text, 'Step 03.2: Verify Create a filtering condition window title.')
         
        """
        Step 04: Select Type dropdown and select Parameter and click OK and OK.
        """ 
        ia_ribbonobj.create_parameter_filter_condition('simple', None)
        time.sleep(sleep_time[3])
        
        """
        Step 05: Click Run in toolbar.
        """ 
        utillobj.synchronize_with_number_of_element(parent_css, 1, synchronize_time)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(sleep_time[3])
        utillobj.switch_to_frame(pause=4)
        time.sleep(sleep_time[2])
        
        """
        Step 05.1: Verify Autoprompt window appears with simple filter prompt.
        """ 
        utillobj.synchronize_with_number_of_element(field_css, 1, synchronize_time)
        utillobj.verify_object_visible(field_css, True, 'Step 5.1: Verify Autoprompt window appears with simple filter prompt')
        
        """
        Step 06: Enter "Computers" in Product Category: and click Run with filter values.
        """ 
        time.sleep(2)
        iarun.enter_text_in_amper_value_inputbox(field_name, input_text)
        time.sleep(sleep_time[3])
        iarun.select_amper_menu('Run')
        time.sleep(sleep_time[3])
        WebDriverWait(self.driver, synchronize_time).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[name="wfOutput"]')))
        
        """
        Step 06.1: Verify results displayed without error in Autoprompt window.
        """ 
        time.sleep(sleep_time[2])
#         iarun.create_table_data_set("table[summary= 'Summary']", Test_Case_ID+'_Ds02.xlsx')
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_Case_ID+'_Ds02.xlsx', "Step 06: verify data set")
        
        """
        Step 07: Logout WF using API: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """ 
        time.sleep(sleep_time[2])
        
if __name__ == '__main__':
    unittest.main()