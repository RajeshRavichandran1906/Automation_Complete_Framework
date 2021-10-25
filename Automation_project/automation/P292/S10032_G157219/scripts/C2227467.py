'''
Created on 17-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227467
TestCase Name = Verify create Slicer from field context menu in the Data pane
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, ia_run
from common.lib import utillity  
import time
from common.locators.loginpage_locators import LoginPageLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators

class C2227467_TestClass(BaseTestCase):

    def test_C2227467(self):
        
        Test_Case_ID = "C2227467"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        
        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        chart_type_css="#TableChart_1"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        
        """    2. Double click "COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST"    """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("RETAIL_COST", 2, 1)
        time.sleep(4)
        
        """    3. Verify the following report is displayed.    """
        coln_list = ["COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST"]
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 03a: Verify column titles") 
        #ia_resultobj.create_report_data_set("TableChart_1", 10, 4, "C2227467_Ds01.xlsx")
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 4, "C2227467_Ds01.xlsx", "Step 03b: verify data set")
        
        """    4. Select "COUNTRY" from Data pane.    """
        """    5. Right mouse click > Slicers > "New Group".    """
        metaobj.datatree_field_click("COUNTRY", 1, 1,'Slicers','New Group')
        
        """    6. Verify "COUNTRY" has been added to "Group 1"    """
        ia_ribbonobj.verify_slicer_group(1, ['Group 1', 'COUNTRY'], "Step 6a: Verify 'COUNTRY' has been added to 'Group 1'")
        
        """    7. Select "CAR" from Data pane.    """
        """    8. Right mouse click > Slicers > "Existing Group".    """
        metaobj.datatree_field_click("CAR", 1, 1,'Slicers','Existing Group')
        
        """    9. In "Add Slicers" window, click "OK"    """
        driver.find_element_by_css_selector("#addSlicerDlg #addSlicerOkBtn").click()
        
        """    10. Verify "COUNTRY" has been added to "Group 1".    """
        ia_ribbonobj.verify_slicer_group(1, ['Group 1', 'COUNTRY', '  CAR'], "Step 10a: Verify 'CAR' slicer has been added to 'Group 1'")
        
        """    11. Select COUNTRY = (ENGLAND, ITALY AND W GERMANY) by holding Ctrl key > Click "OK".    """
        list1=['ENGLAND', 'ITALY', 'W GERMANY']
        ia_ribbonobj.create_slicer(1, 'COUNTRY', list1, 'small', 'ok')
        
        """    12. Select CAR = (BMW, MASERATI) > Click "OK".    """
        list2=['BMW', 'MASERATI']
        ia_ribbonobj.create_slicer(1, 'CAR', list2, 'small', 'ok')
        
        """    13. Click "Update Preview" in the Slicers Tab ribbon > Verify Preview is refreshed    """
        ribbonobj.select_ribbon_item('Slicers', 'Update_preview')
        time.sleep(5)
        coln_list = ["COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST"]
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 13a: Verify column titles") 
#         ia_resultobj.create_report_data_set("TableChart_1", 2, 4, "C2227467_Ds02.xlsx")
        ia_resultobj.verify_report_data_set("TableChart_1", 2, 4, "C2227467_Ds02.xlsx", "Step 13b: verify data set")
        
        """    14. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        
        """    15. Verify the report is displayed.    """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227467_Ds03.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227467_Ds03.xlsx", "Step 15a: verify data set")
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    16. Click "IA" > "Save" > C2227467 > click Save.    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    17. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    18. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163511.fex&tool=document    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(2)
        
        """    19. Verify Preview    """
        coln_list = ["COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST"]
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 19a: Verify column titles") 
#         ia_resultobj.create_report_data_set("TableChart_1", 2, 4, "C2227467_Ds02.xlsx")
        ia_resultobj.verify_report_data_set("TableChart_1", 2, 4, "C2227467_Ds02.xlsx", "Step 19b: verify data set")
        
        """    20. Select Slicers Tab > Verify Slicers in the Ribbon    """
        ribbonobj.switch_ia_tab('Slicers')
        time.sleep(2)
        ia_ribbonobj.verify_slicer_group(1,  ['Group 1', 'COUNTRY', 'Multiple', ' CAR', 'Multiple'] , "Step 20a: Verify 'COUNTRY', 'CAR' slicers in 'Group 1'")
        
        """    21. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()


     