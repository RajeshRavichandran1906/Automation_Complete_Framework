'''
Created on Jan'25, 2017
@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227530
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_ribbon, define_compute, active_miscelaneous, visualization_resultarea
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227530_TestClass(BaseTestCase):

    def test_C2227530(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2227530'
        driver = self.driver
        driver.implicitly_wait(35)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        defcomp=define_compute.Define_Compute(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result=visualization_resultarea.Visualization_Resultarea(self.driver)
        browser=utillobj.parseinitfile('browser')
        
        """ Step 01: Launch IA Document mode:- http://machine:port/ibi_apps/ia?tool=document&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032 """
        utillobj.infoassist_api_login('document','ibisamp/car','P292/S10032', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#iaCanvasPanel")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """ Step 2. Select "Insert" > "Chart". """
        ribbonobj.select_ribbon_item("Insert", "Chart")
        time.sleep(4)
        
        """ Step 3. Double click "COUNTRY". """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        
        """ Step 4. Select "Data" > "Define". """
        defcomp.invoke_define_compute_dialog('define')
        elem1=(By.CSS_SELECTOR, "#fname")
        resultobj._validate_page(elem1)
        
        """ Step 5. Enter Name = "DEFSALES". """
        """ Step 6. Double click "SALES" > "OK". """
        defcomp.enter_define_compute_parameter("DEFSALES", 'D12.2', 'SALES', 1)
        defcomp.close_define_compute_dialog('ok')
        
        """ Step 7. Double click "DEFSALES". """
        metaobj.datatree_field_click("DEFSALES", 2, 1)
        time.sleep(4)
        
        """ Step 8. Verify the following chart is displayed. """
        resultobj.verify_number_of_riser("TableChart_1", 1, 5, 'Step 08a: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 08b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue1", "Step 08c: Verify bar color")
        xaxis_value="COUNTRY"
        yaxis_value="DEFSALES"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 08d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 05d(ii): Verify Y-Axis Title")
        
        """ Step 9 : click Run """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step09_'+browser, image_type='actual',x=50, y=80, w=-150, h=-100)
        utillobj.switch_to_frame()
        #WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe"]')))
        time.sleep(8)
        
        
        """ Step 10. Verify the document is displayed. """
        msg="Step 10"
        miscelanousobj.verify_arChartToolbar("MAINTABLE_0",['More Options','Advanced Chart','Original Chart'],"Step 10a: Verify Chart toolbar")
        x_val_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        y_val_list=['0', '20K', '40K', '60K', '80K', '100K']
        result.verify_riser_chart_XY_labels('MAINTABLE_0', x_val_list, y_val_list, msg + ".b")
        expected_tooltip=['COUNTRY:  W GERMANY', 'DEFSALES:  88,190.00', 'Filter Chart', 'Exclude from Chart']
        miscelanousobj.verify_active_chart_tooltip('MAINTABLE_0', 'riser!s0!g4!mbar', expected_tooltip, msg + ".c: verify the chart tooltip with fill color")
        #driver.switch_to.default_content()
        utillobj.switch_to_default_content()
        time.sleep(2)
        
        """ Step 11 : Click "IA" > Exit > Yes. """
        ribbonobj.select_tool_menu_item('menu_close')
        time.sleep(5)
        driver.find_element_by_css_selector("#saveAllDlg #btnYes").click()
        time.sleep(5)
        
        """ Step 12 : Enter Title = "C2227528". """
        """ Step 13 : Click "Save". """
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """ Step 14: Logout. """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """ Step 15 : Reopen saved FEX: """
        time.sleep(5)
        oFolder=utillobj.parseinitfile('suite_id')
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', oFolder, mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)  
        time.sleep(10)
        
        """ Step 16 : Verify Chart on Canvas is displayed. """
        resultobj.verify_number_of_riser("TableChart_1", 1, 5, 'Step 08a: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 08b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue1", "Step 08c: Verify bar color")
        xaxis_value="COUNTRY"
        yaxis_value="DEFSALES"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 08d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 05d(ii): Verify Y-Axis Title")
        
        """ Step 17: Logout. """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()