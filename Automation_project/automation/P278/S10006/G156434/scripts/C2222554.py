'''
Created on 30-NOV-2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222554
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators

class C2222554_TestClass(BaseTestCase):

    def test_C2222554(self):
        
        Test_Case_ID = "C2222554"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_styobj = ia_styling.IA_Style(self.driver)
        
        """
        Step 01: Launch IA Report mode
        http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        Step 02. Select "COUNTRY","CAR","DEALER_COST","RETAIL_COST".      
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        
        """ 
        Step 03. Click Style in the Report section                                   
        """
        ribbonobj.select_ribbon_item('Home', 'style')
        
        """
        Step 04: Click Italic
        Step 05: Click Cancel > Verify Preview
        """ 
        ia_styobj.set_report_style(italic=True, btn_cancel=True)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 05.1: Verify Canvas column titles After Apply Style")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, "C2222564_Ds01.xlsx", 'Step 05.2: Verify report dataset After Apply Style')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5,font_name='Arial',font_size='9pt', text_value='ENGLAND',italic=False, msg='Step 05.3: Verify cell property')
        
        """
        Step 06: Click Run > Verify runtime
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)     
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        ia_runobj.verify_table_data_set("table[summary= 'Summary']", "C2222554_Ds01.xlsx", "Step 06a: verify data set")
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2,1,font_color='gray8', text_value='ENGLAND', font_name='ARIAL', font_size='9pt',msg="Step 06: Verify cell property in run window")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        
        """    
        Step 06. Click Save in the toolbar > Save As C2222554 > click Save   
         """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
        time.sleep(5)
        
        """    
        Step 07. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp   
        """
        time.sleep(3)
        
        
if __name__ == '__main__':
    unittest.main()
        
        
        
        