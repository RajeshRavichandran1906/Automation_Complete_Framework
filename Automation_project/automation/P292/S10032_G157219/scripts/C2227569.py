'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227569
TestCase Name = Verify Parameters can be edit and delete
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class C2227569_TestClass(BaseTestCase):

    def test_C2227569(self):
        driver = self.driver
        driver.implicitly_wait(40)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """ 
        Step01: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227568.fex&tool=report
        Step02: Right mouse click > "Edit With..." > InfoAssist+.
        """
        utillobj.infoassist_api_edit('C2227568', 'report', 'S10032_ia_1', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)  
        time.sleep(8)      
           
        """
        Step03: Select "CURR_SAL" > "Links" > "Drilldown".    
        """
        coln_list = ['EMP_ID','LAST_NAME','CURR_SAL']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 03: Verify Column titles ")
        time.sleep(2) 
        metaobj.querytree_field_click("CURR_SAL", 1, 0)
        time.sleep(2)   
        ribbonobj.select_ribbon_item('Field', 'DrillDown')
        time.sleep(4)
        ia_ribbonobj.create_drilldown_report("report", verify_default_drilldown_type=True)
        
        """
        Step04: Click on the 2nd button (Edit Parameter).
        Step05: Change "Parameter Name" from "DEPARTMENT" to "DEPT".
        Step06: Click "OK".
        """
        browser_type=utillobj.parseinitfile('browser')
        if browser_type == 'Chrome':
            ia_ribbonobj.create_drilldown_report("report",set_ampersand='edit')
            time.sleep(1)
            elem=driver.find_element_by_css_selector("#drillDownParmPopup #paramValueName")
            action1 = ActionChains(driver)
            action1.move_to_element_with_offset(elem, 25, 8).click().perform()
            del action1
            time.sleep(1)
        ia_ribbonobj.create_drilldown_report("report",set_ampersand='edit',name_input='DEPT', popup_close='ok')
        
        """
        Step07: Verify "Name" has been updated to "DEPT".
        """
        ia_ribbonobj.create_drilldown_report("report", verify_input_text=['DEPT','MIS'])
         
        """
        Step08: Click on the 3rd button (Remove parameter).
        Step09: Verify Parameters Name/Value has been deleted and "Edit/Delete Parameter" buttons disabled.
        Step10: Click "Cancel".
        """
        ia_ribbonobj.create_drilldown_report("report",set_ampersand='remove')
        ia_ribbonobj.create_drilldown_report("report", verify_input_text=[],verify_enabled_parameter_icons=['add'], click_cancel='yes')
        
        """
        Step11: Click "Drilldown" button
        Step12: Verify that parameters are restored.
        Step13: Click "OK" to dismiss drilldown window
        Step14: Logout
        """
        time.sleep(2)   
        ribbonobj.select_ribbon_item('Field', 'DrillDown')
        time.sleep(4)
        ia_ribbonobj.create_drilldown_report("report", verify_default_drilldown_type=True)
        ia_ribbonobj.create_drilldown_report("report", verify_enabled_parameter_icons = ['add','edit','remove'], verify_input_text=['DEPARTMENT','MIS'], click_ok='yes')
        
        
if __name__ == '__main__':
    unittest.main()
    