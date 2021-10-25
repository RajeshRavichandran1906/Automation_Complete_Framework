'''
Created on 03-Feb-2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227539
TestCase Name = Verify changing Document Page Color 
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, ia_styling, active_miscelaneous
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.locators.loginpage_locators import LoginPageLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2227539_TestClass(BaseTestCase):

    def test_C2227539(self):
        Test_Case_ID = 'C2227539'
        driver = self.driver
        driver.implicitly_wait(35)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        styleobj=ia_styling.IA_Style(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        browser=utillobj.parseinitfile('browser')
        
        """ 1. Launch IA Document mode:- http://machine:port/ibi_apps/ia?tool=Document&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032 """
        utillobj.infoassist_api_login('document','ibisamp/car','P292/S10032_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document')
        time.sleep(2)
        
        """ 2. Double click CAR and SALES """
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("SALES", 2, 1)
        time.sleep(5)
        coln_list = ["CAR","SALES"]
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 02a: Verify column titles")
        
        """ 3. Right-click on the Canvas space > Verify "Page Color" menu is displayed """
        source_elem = self.driver.find_element_by_css_selector("#resultArea #canvasFrame")
        canvas_width=source_elem.size['width']
        canvas_heigth=source_elem.size['height']
        action1 = ActionChains(self.driver)
        action1.move_to_element_with_offset(source_elem, canvas_width/2, canvas_heigth/2).click().perform()
        time.sleep(3)
        action1.move_to_element_with_offset(source_elem, canvas_width/2, canvas_heigth/2).context_click().perform()
        del action1
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=['Page Color'], msg='Step 03a: ')
        
        """ 4. Select "Page Color" > Select a light gray color > click OK """
        utillobj.select_or_verify_bipop_menu('Page Color')
        styleobj.set_color("light_gray")
        
        """ 5. Verify color is applied  """
        expected_bg_color=utillobj.color_picker('light_gray', 'rgba')
        actual_bg_color=Color.from_string(self.driver.find_element_by_css_selector("#resultArea #canvasFrame #theCanvas").value_of_css_property("background-color")).rgba
        utillobj.asequal(expected_bg_color, actual_bg_color , "Step 0a5: Verify background color applied in preview canvas")
        
        """ 6. Click Run """
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(5)
        utillobj.switch_to_frame()
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 06a: Verify the Report Heading')
        column_list=['CAR', 'SALES']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 06b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2227539_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2227539_Ds01.xlsx', 'Step 06c: Verify data.')
        
        """ 7. Verify background color """
        expected_bg_color=utillobj.color_picker('light_gray', 'rgba')
        actual_bg_color=Color.from_string(self.driver.find_element_by_css_selector("#orgdivouter0").value_of_css_property("background-color")).rgba
        utillobj.asequal(expected_bg_color, actual_bg_color , "Step 07a: Verify background color applied in Run report")
        elem=driver.find_element_by_css_selector("#orgdivouter0")
        utillobj.take_screenshot(elem,Test_Case_ID+'_Actual_Step07_'+browser, image_type='actual')
        utillobj.switch_to_default_content()
        time.sleep(2)
        
        """ 8. Click "Save" > save as "C2227539" > Click Save """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """ 9. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """ 10. Reopen saved FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227539.fex&tool=Document """
        oFolder=utillobj.parseinitfile('suite_id')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', oFolder, mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=20, string_value='Document')
        time.sleep(2)
        
        """ 11. Verify Canvas """
        expected_bg_color=utillobj.color_picker('light_gray', 'rgba')
        actual_bg_color=Color.from_string(self.driver.find_element_by_css_selector("#resultArea #canvasFrame #theCanvas").value_of_css_property("background-color")).rgba
        utillobj.asequal(expected_bg_color, actual_bg_color , "Step 11: Verify background color applied in preview canvas")
        coln_list = ["CAR","SALES"]
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 11a: Verify column titles")
        
        """ 12. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp """
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()