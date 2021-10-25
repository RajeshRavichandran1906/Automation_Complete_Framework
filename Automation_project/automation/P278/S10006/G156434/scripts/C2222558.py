'''
Created on 29-NOV-2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222558
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2222558_TestClass(BaseTestCase):

    def test_C2222558(self):
        
        Test_Case_ID = "C2222558"
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
        Step 04: Click Font Color > Select Magenta
        Step 05: Click Apply and Click OK
        """ 
        ia_styobj.set_report_style(text_color='magenta',btn_apply='btn_apply', btn_ok='btn_ok')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 06.1: Verify Canvas column titles After Apply Style")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, "C2222564_Ds01.xlsx", 'Step 06.2: Verify report dataset After Apply Style')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5,text_color='magenta', text_value='ENGLAND', msg='Step 05: Verify cell property')
        
        """
        Step 06: Again Click Style in Report section and Click Font Color > Select Black
        Step 07: Click Apply
        """
        ribbonobj.select_ribbon_item('Home', 'style')
        ia_styobj.set_report_style(background_color='black', btn_apply='btn_apply', btn_ok='btn_ok')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5,bg_cell_no=5,bg_color='black', text_value='ENGLAND', msg='Step 07: Verify cell property')
        
        """ 
        Step 08. Logout: 'http://machine:port/ibi_apps/service/wf_security_logout.jsp'        
        """
#         time.sleep(2)
#         utillobj.infoassist_api_logout()
              
       
if __name__ == '__main__':
    unittest.main()