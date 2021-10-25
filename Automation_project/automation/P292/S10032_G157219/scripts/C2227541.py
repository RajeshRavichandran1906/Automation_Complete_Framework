'''
Created on 10-Nov-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227541
TestCase Name = Verify styled Report then convert to Chart
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon, ia_styling
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227541_TestClass(BaseTestCase):

    def test_C2227541(self):        
        Test_Case_ID = "C2227541"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver) 
        iastylingobj=ia_styling.IA_Style(self.driver)
        
        """    1. Launch the IA API with EMPLOYEE, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/employee','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """    2. Double click "LAST_NAME", "CURR_SAL", "SALARY"    """
        metaobj.datatree_field_click("LAST_NAME", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CURR_SAL", 2, 1)
        time.sleep(4)      
        metaobj.datatree_field_click("SALARY", 2, 1)
        time.sleep(4)     
        
        """    3. verify the following report is displayed    """
        coln_list = ["LAST_NAME", "CURR_SAL", "SALARY"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 03a: Verify column titles")
#         ia_resultobj.create_report_data_set("TableChart_1", 10, 3, "C2227541_Ds001.xlsx")
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 3, "C2227541_Ds001.xlsx","Step 03a: Verify data set")
        
        """    4. Select "CURR_SAL".    """
        metaobj.querytree_field_click("CURR_SAL", 1)
        
        """    5. Click on Style from Fields Tab    """
        """    6. Change Font size = 12 , Font Color = Red, Bold, Italic.    """
        iastylingobj.set_field_style(font_size='12',bold=True,italic=True,text_color='red')
        
        """    7. Verify the "Live Preview" updated with the specified style for "CURR_SAL".    """
        ia_resultobj.verify_report_cell_property("TableChart_1", 5, font_color='red', font_size='12pt', bold=True, italic=True, msg='Step 7:')
        
        """    8. Select "Home" > click "Chart" button to convert to Chart..    """     
        ribbonobj.select_ribbon_item("Home", "Chart")
        elem1=(By.CSS_SELECTOR, "#TableChart_1 rect[class^='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1)
        time.sleep(2)
        
        """    9. Verify the Report is converted to a Chart.    """
        resultobj.verify_number_of_riser("TableChart_1", 2, 11, 'Step 09a: Verify the total number of risers displayed on preview Chart')
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 09b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue1", "Step 09c(i): Verify first bar color")
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 09d(i): Verify X-Axis Title")
        
        """    10. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2227541_Base_step10', image_type='base',x=1, y=1, w=-1, h=-1)
        iframe=driver.find_element_by_css_selector("[id^=ReportIframe-]")
        x_fr=iframe.location["x"]
        y_fr=iframe.location["y"]
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        
        """    11. Verify the chart is displayed on the Run output window.    """
        resultobj.verify_number_of_riser("jschart_HOLD_0", 2, 11, 'Step 11a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 11b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g4!mbar!", "bar_blue1", "Step 11c(i): Verify first bar color")
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 11d(i): Verify X-Axis Title")
        expected_tooltip=['LAST_NAME:IRVING', 'CURR_SAL:$26,862.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g4!mbar",expected_tooltip, "Step 11e: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr)
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    12. Click switch "Reports" shortcut in the Status bar    """
        """    13. Select "Report1" fex > verify canvas.    """
        self.driver.find_element_by_css_selector("#sbpSwitchReportPanel div[class$='drop-down-arrow']").click()
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu("Report1")
        time.sleep(8)
        coln_list = ["LAST_NAME", "CURR_SAL", "SALARY"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 13a: Verify column titles")
#         ia_resultobj.create_report_data_set("TableChart_1", 10, 2, "C2227541_Ds01.xlsx")
        time.sleep(8)
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 3, "C2227541_Ds01.xlsx", "Step 13b: Verify the report data set on preview")
        ia_resultobj.verify_report_cell_property("TableChart_1", 20, font_color='red', font_size='12pt', bold=True, italic=True, msg='Step 13c:')
        
        """    14. Save the Report fex : Click Save button in the toolbar > "C2068421" > click Save    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    15. Click "IA" > close    """
        ribbonobj.select_tool_menu_item('menu_close')
         
        """    16. Save the Chart fex : Click Save button in the toolbar > "C2068421" > click Save    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID + '_1')
        time.sleep(5)
        
        """    17. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()


        
    