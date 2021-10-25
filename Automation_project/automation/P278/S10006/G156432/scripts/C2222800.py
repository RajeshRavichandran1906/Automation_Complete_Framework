'''
Created on 17-Jan-2017

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222800
TestCase Name = Verify Traffic Lights on a Define based on another BY field
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_styling, ia_run, define_compute
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class C2222800_TestClass(BaseTestCase):

    def test_C2222800(self):
        
        Test_Case_ID = "C2222800"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        def_comp = define_compute.Define_Compute(self.driver)
        define_field_path = 'Measures/Properties->Define_1'
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        
        """ 2. Double click COUNTRY, CAR, DEALER_COST            """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        
        
        """ 3. Click on Data Tab -> Detail (Define)                                                  """
        """ 4. Select the fifth option (fx) - Functions -> Character -> Edit (string, 'mask')        """
        def_comp.invoke_define_compute_dialog('define')
        time.sleep(5)
        fun_click=driver.find_element_by_css_selector('#btnFunctionsBox img')
        utillobj.default_left_click(object_locator=fun_click)
        time.sleep(5)
        parent_css="[class*='active'] #rightPane #functionsTree table[class*='tree-view-table']"
        resultobj.wait_for_property(parent_css, 1)
        
        """ 5. Select the second option (view fields in business order) to get display the fields    """
        """ 6. Select string in Edit text and Double click "COUNTRY" and select mask in Edit text and Click $9$9$    """
#         parent_table_element = "div[id='meta-data'][class*='tree-view'] table"
        time.sleep(12)
        prodedure_path = "Character->EDIT ( string, 'mask' )"
        utillobj.seletct_tree_view_plus_node(parent_css, prodedure_path, 1)
        time.sleep(5)
        textarea=driver.find_element_by_css_selector("div[id^='BiVBox'] textarea[id='ftext']")
        expected_text_value="EDIT ( string, 'mask' )"
        actual_text=textarea.get_attribute('value').strip()
        if expected_text_value == actual_text:
            actual_text_value=True
            utillobj.asequal(True,actual_text_value,"Step 6: Verify text value in text area ")
        textarea.clear()
        time.sleep(3)
        textarea.click()
        time.sleep(5)
        ActionChains(driver).send_keys("EDIT (  CAR.ORIGIN.COUNTRY , '$9$9$' ) ").perform()
        time.sleep(5)
         
         
        """ 7. Type A40 in Format tab        """
        """ 8. Click "Ok"                    """
        type_format='A40'
        field_format = self.driver.find_element_by_id("fformat")
        field_format.clear()
        time.sleep(3)
        field_format.click()
        time.sleep(3)
        ActionChains(driver).send_keys(type_format).perform()
        time.sleep(3)
        def_comp.close_define_compute_dialog('ok')
        time.sleep(10)
        metaobj.verify_data_pane_field('Dimensions', 'Define_1', 7, "Step 8: ")        
         
         
        """ 9. Double click on "Define_1"            """
        metaobj.datatree_field_click(define_field_path, 2, 1)
        time.sleep(4)
         
         
        """ 10. Click on "Define_1" field in Canvas, then Display button from Field tab (If display group not expanded in Field tab )    """
        ia_resultobj.select_field_on_canvas("TableChart_1", 3)
         
         
        """ 11. Display tab expands -> Click on Traffic Lights        """
        time.sleep(2)
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
         
         
        """ 12. Click on Define_1 drop down menu and select CAR        """
        """ 13. Select the other dropdown arrow and enter value = "DATSUN" and click "Ok"    """
        time.sleep(2)
        ia_stylingobj.traffic_light_create_new(1, field_name='CAR', filter_type='Constant', value_box_input='DATSUN')
         
         
        """ 14. Now click on Style tab Make changes Bold, Font size-12, Text Color-BLUE            """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, font_size='12', text_color='blue')
        time.sleep(2)
         
         
        """ 15. Click "Apply" and "Ok"            """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
         
         
        """ 16. Verify the preview with applied TL condition            """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'Define_1', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 16: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 16.1: Verify Canvas report dataset ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 28, bold=True, font_size='12pt', font_color='blue', text_value='AA', msg='Step 16.2:')
         
         
        """ 17. Click "Run"                """
        ribbonobj.select_top_toolbar_item('toolbar_run')
         
         
        """ 18. Verify that TL condition is applied with styling for define field        """
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx", 'Step 18: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 8, 3, bold=True, font_size='12pt', font_color='blue', text_value='AA', msg='Step 18.1:')
         
         
        """ 19. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        self.driver.switch_to_default_content()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("ia"+Test_Case_ID)
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()