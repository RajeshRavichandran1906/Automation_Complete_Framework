'''
Created on Nov'28, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222574
'''
import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run, ia_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib import utillity
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.locators.loginpage_locators import LoginPageLocators

class C2222574_TestClass(BaseTestCase):

    def test_C2222574(self):
        
        """    TESTCASE VARIABLES    """
        Test_Case_ID = 'C2222574'
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver) 
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        ia_styobj = ia_styling.IA_Style(self.driver)
        
        """
        Step 01: Launch the IA API with CAR master file    
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)

        """    
        Step 02 : Select "COUNTRY","CAR","DEALER_COST","RETAIL_COST".        
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("RETAIL_COST", 2, 1)
        time.sleep(4)
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 02a: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, "C2222564_Ds01.xlsx", 'Step 02b: Verify report dataset')
        time.sleep(4)
        
        """
        Step 03: Select CAR in the Query window
        """
        metaobj.querytree_field_click('CAR', 1)
        
        """
        Step 04: Click Data + Title in the Style section
        """
        time.sleep(2)
        ribbonobj.select_ribbon_item('Field', 'dataplusstyle')
        time.sleep(2)
        
        """
        Step 05: Click Font Color > Select Magenta
        Step 06: Ok
        """
        ribbonobj.select_ribbon_item('Field', 'fontcolour')
        ia_styobj.set_color('magenta')
        
        """
        Step 07: Click Background Color > Select Cyan
        Step 08: Click OK
        """
        ribbonobj.select_ribbon_item('Field', 'fontbackcolour')
        ia_styobj.set_color('cyan')
        
        """
        Step 09: Select COMIC SANS MS as the Font Type
        """
        ribbonobj.switch_ia_tab('Field')
        utillobj.select_combobox_item("FieldFont", 'COMIC SANS MS')
        time.sleep(1)
        
        """
        Step 10: Click Drilldown in the Links Section
        """
        ribbonobj.select_ribbon_item('Field', 'drilldown')
        
        """
        Step 11: Click Web Page Radio Button > Enter URL - http://www.yahoo.com > select new window in the target dropdown
        Step 12: Click OK
        """
        ia_ribbonobj.create_drilldown_report("webpage", url_value="http://www.yahoo.com", click_ok='yes')
        ia_resultobj.verify_autolink("TableChart_1","JAGUAR",10,"Step 12a: Verify DrillDown applied in JAGUAR",link_color='magenta') 
        ia_resultobj.verify_report_cell_property("TableChart_1", 2, bg_cell_no=2,bg_color='cyan', font_color='magenta', text_value='CAR', msg='Step 12b: Verify CAR cell property')
        ia_resultobj.verify_report_cell_property("TableChart_1", 6,bg_cell_no=6, bg_color='cyan', font_color='magenta', text_value='JAGUAR', msg='Step 12c: Verify JAGUAR cell property')
                
        """
        Step 13: Click Drilldown in the Links Section
        """
        ribbonobj.select_ribbon_item('Field', 'drilldown')
        
        """
        Step 14: Click 'Delete all and exit' > Click Yes
        """
        ia_ribbonobj.create_drilldown_report("webpage",delete_all_and_exit='yes')
        time.sleep(1)
        
        """
        Step 15: Verfiy styling remains
        """
        ia_resultobj.verify_report_cell_property("TableChart_1", 2,bg_cell_no=2, bg_color='cyan', font_color='magenta', text_value='CAR', msg='Step 15a: Verify CAR cell property remains')
        ia_resultobj.verify_report_cell_property("TableChart_1", 6,bg_cell_no=6, bg_color='cyan', font_color='magenta', text_value='JAGUAR', msg='Step 15b: Verify JAGUAR cell property remains')
        
        """
        Step 16: Click Save in the toolbar > Save As C2222574 > click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
              
        """         
        step 17: Logout: 'http://machine:port/ibi_apps/service/wf_security_logout.jsp'        
        """
        time.sleep(2)
        utillobj.infoassist_api_logout()
              
        """
        Step 18. Reopen saved FEX: 
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222574.fex&tool=Report       
        """              
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(2)
        utillobj.infoassist_api_edit("se_"+Test_Case_ID, 'report', 'S10006')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)

              
        """
        Step 19: Verify restore
        """
        ia_resultobj.verify_report_cell_property("TableChart_1", 2, bg_cell_no=2, bg_color='cyan', font_color='magenta', text_value='CAR', msg='Step 19a: Verify CAR cell property remains')
        ia_resultobj.verify_report_cell_property("TableChart_1", 6, bg_cell_no=6, bg_color='cyan', font_color='magenta', text_value='JAGUAR', msg='Step 19b: Verify JAGUAR cell property remains')
        time.sleep(2)
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, "C2222564_Ds01.xlsx", 'Step 19c: Verify report dataset')
        time.sleep(4)
        
        
        
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        
        
        