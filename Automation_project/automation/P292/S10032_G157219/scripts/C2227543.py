'''
Created on 26-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227543
TestCase Name = Verify convert report to chart 
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227543_TestClass(BaseTestCase):

    def test_C2227543(self):        
        Test_Case_ID = "C2227543"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)

        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        chart_type_css="#TableChart_1"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
         
        """    2. Double click "CAR", "DEALER_COST".    """
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        time.sleep(4)        
        
        """    3. verify the following report is displayed    """
        coln_list = ['CAR', 'DEALER_COST',]
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 03: Verify column titles")
        time.sleep(4)
        ia_resultobj.create_report_data_set("TableChart_1", 10, 2, "C2227543_Ds01.xlsx")
        
        """    4. Select "Format" > Chart (on Destination Grouping).    """     
        ribbonobj.select_ribbon_item("Format", "Chart")
        elem1=(By.CSS_SELECTOR, "#TableChart_1 rect[class^='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1)
        time.sleep(2)
        
        """    5. Verify the Report is converted to a Chart.    """
        resultobj.verify_number_of_riser("TableChart_1", 1, 10, 'Step 05a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 05b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue1", "Step 05c(i): Verify first bar color")
        xaxis_value="CAR"
        yaxis_value="DEALER_COST"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 05d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 05d(ii): Verify Y-Axis Title")
        
        """    6. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe-"]')))
        time.sleep(3)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(3)
        driver.switch_to.default_content()
        time.sleep(4)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2227543_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        iframe=driver.find_element_by_css_selector("iframe[id^='ReportIframe-']")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        
        """    7. Verify the chart is displayed on the Run output window.    """
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 10, 'Step 07a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 07b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue1", "Step 07c(i): Verify first bar color")
        xaxis_value="CAR"
        yaxis_value="DEALER_COST"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 05d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 05d(ii): Verify Y-Axis Title")
        expected_tooltip=['CAR:ALFA ROMEO', 'DEALER_COST:16,235']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g0!mbar",expected_tooltip, "Step 07e: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr+5)
        driver.switch_to.default_content()
        time.sleep(2)
                
        """    8. Click Save button in the toolbar > "C2227543" > click Save    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    9. Click "IA" > Exit    """
        ribbonobj.select_tool_menu_item('menu_exit')
        
        """    10. Verify Save Prompt is displayed    """
        bol=driver.find_element_by_css_selector("#saveAllDlg #saveChangesLabel").text=="Save Changes to 'Report1'?"
        utillobj.asequal(True, bol, "Step 10a: Verify Save Prompt displayed")
        
        """    11. Click "No" to dismiss the prompt.    """
        driver.find_element_by_css_selector("#saveAllDlg #btnNo").click()    
        time.sleep(8)
        
        """    12. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()


        
    