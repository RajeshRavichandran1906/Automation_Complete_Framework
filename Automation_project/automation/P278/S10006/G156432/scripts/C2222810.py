'''
Created on 18-Jan-2017

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222810
TestCase Name = Verify the values are retrieved from the appropriate selected field in field dropdown in TL window for "Get values"
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling,\
    ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2222810_TestClass(BaseTestCase):

    def test_C2222810(self):
        
        Test_Case_ID = "C2222810"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """ 
        Step01: Launch IA Report mode:
        http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        
        """
        Step02: Double click CAR, SEATS      
        """
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("SEATS", 2, 1)
        time.sleep(4)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['CAR', 'SEATS']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 02: Verify Column titles ")
        time.sleep(2)
        
        """
        Step03: Now Click on CAR field
        """
        ia_resultobj.select_field_on_canvas("TableChart_1", 1)
        
        """
        Step04: From Field Tab > Display group, click "Traffic Lights"
        Step05: Click on CAR drop down menu and select SEATS
        Step06: Click on Value dropdown in Traffic Lights condition dialog
        Step07: Select "Get values-> All"
        Step08: Verify the values are displayed for SEATS in Traffic Lights condition dialog
        """
        
        time.sleep(5)
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        time.sleep(1)
        ia_stylingobj.traffic_light_create_new(1, field_name='SEATS', filter_type='Constant', getvalue_params='All', verify=['2','4','5'])
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Cancel')
        
        
        
        """
        Step 09: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp     
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("ia"+Test_Case_ID)
        time.sleep(2)
        

if __name__ == '__main__':
    unittest.main()
    