'''
Created on 16-Jan-2017

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222796
TestCase Name = Verify Define and a Compute fields with TL conditions for both columns
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_styling, define_compute
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2222796_TestClass(BaseTestCase):

    def test_C2222796(self):
        
        Test_Case_ID = "C2222796"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
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
        
        
        """ 3. Click on Data Tab -> Detail (Define)            """
        """ 4. Double click DEALER_COST and click *10 in Detail Field (Define) window        """
        """ 5. Click "Ok" and Verify the created define field added under Measures in data pane    """
        def_comp.invoke_define_compute_dialog('define')
        time.sleep(2)
        def_comp.enter_define_compute_parameter('Define_1', 'D12.2', 'DEALER_COST', 1)
        time.sleep(3)
        def_comp.select_calculation_btns('mult')
        def_comp.select_calculation_btns('one')
        def_comp.select_calculation_btns('zero')
        time.sleep(2)
        def_comp.close_define_compute_dialog('ok')
        time.sleep(10)
        metaobj.verify_data_pane_field('Measures/Properties', 'Define_1', 15, "Step 5: ")
        
        
        """6. Click on Data Tab -> Summary (Compute)            """
        """ 7. Double click RETAIL_COST and click *10 in Summary Field (Compute) window        """
        """ 8. Click "Ok" and Verify the created compute field added under Sum in query pane    """
        def_comp.invoke_define_compute_dialog('compute')
        time.sleep(2)
        def_comp.enter_define_compute_parameter('Compute_1', 'D12.2', 'RETAIL_COST', 1)
        time.sleep(3)
        def_comp.select_calculation_btns('mult')
        def_comp.select_calculation_btns('one')
        def_comp.select_calculation_btns('zero')
        time.sleep(2)
        def_comp.close_define_compute_dialog('ok')
        time.sleep(10)
        metaobj.verify_query_pane_field('Sum', 'Compute_1', 2, 'Step 8:')
        
        
        """ 9. Double click "Define_1" in Data pane            """
        time.sleep(4)
        metaobj.datatree_field_click(define_field_path, 2, 1)        
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST','Compute_1', 'Define_1']
        resultobj.verify_report_titles_on_preview(5, 5, "TableChart_1", coln_list, "Step 9: Verify Canvas column titles ")
        time.sleep(2)
        
        
        """ 10. Click on "Define_1" field in Canvas, then Display button from Field tab (If display group not expanded in Field tab )    """
        ia_resultobj.select_field_on_canvas("TableChart_1", 5)
        
        
        """ 11. Display tab expands -> Click on Traffic Lights        """
        time.sleep(2)
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        
        
        """ 12. Select dropdown arrow and choose "Equal to"            """
        """ 13. Select the other dropdown arrow and enter value = "42920" and click "Ok"    """
        time.sleep(2)
        ia_stylingobj.traffic_light_create_new(1, relation_name='Equal to', filter_type='Constant', value_box_input='42920')
        
        
        """ 14. Now click on Style tab Make changes Bold, Text Color - RED , BG Color - YELLOW        """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, text_color='red', background_color='yellow')
        time.sleep(2)
        
        
        """ 15. Click "Ok" and Ensure correct preview is reflected        """
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST','Compute_1', 'Define_1']
        resultobj.verify_report_titles_on_preview(5, 5, "TableChart_1", coln_list, "Step 15: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 5, Test_Case_ID+"_Ds01.xlsx", 'Step 15.1: Verify Canvas report dataset ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=1, bg_color='yellow', bold=True, font_color='red', text_value='42,920.00', msg='Step 15.2:')
        
        
        """ 16. Click on "Compute_1"field in Canvas, then Display button from Field tab (If display group not expanded in Field tab )        """
        ia_resultobj.select_field_on_canvas("TableChart_1", 4)
        
        
        """ 17. Display tab expands -> Click on Traffic Lights            """
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        
        
        """ 18. Select dropdown arrow and choose "Not equal to"            """
        """ 19. Select the other dropdown arrow and enter value = "31390" and click "Ok"    """
        time.sleep(2)
        ia_stylingobj.traffic_light_create_new(1, relation_name='Not equal to', filter_type='Constant', value_box_input='31390')
        time.sleep(3)
        
        
        """ 20. Now click on Style tab Make changes Bold, Text Color - BLUE , BG Color - YELLOW        """
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, text_color='blue', background_color='yellow')
        time.sleep(2)
        
        
        """ 21. Click "Ok"    """
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        
        """ 22. Verify that Define and Compute field are applied with TL        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST','Compute_1', 'Define_1']
        resultobj.verify_report_titles_on_preview(5, 5, "TableChart_1", coln_list, "Step 22: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 5, Test_Case_ID+"_Ds01.xlsx", 'Step 22.1: Verify Canvas report dataset ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 9, bg_cell_no=1, bg_color='yellow', bold=True, font_color='blue', text_value='223,690.00', msg='Step 22.2:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=4, bg_color='yellow', bold=True, font_color='red', text_value='42,920.00', msg='Step 22.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 36, bold=False, font_color='gray8', text_value='31,390.00', msg='Step 22.4:')
        
        
        """ 23. Click "IA" menu > "Save As" > "C2222796" > Click Save        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("ia"+Test_Case_ID)
        time.sleep(2)
        
        
        """ 24. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        time.sleep(2)
        driver.switch_to.default_content()
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        
        """ 25. Reopen saved FEX:
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222796.fex&tool=Report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        time.sleep(2)
        utillobj.infoassist_api_edit("ia"+Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        
        
        """ 26. Verify Preview                                """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST','Compute_1', 'Define_1']
        resultobj.verify_report_titles_on_preview(5, 5, "TableChart_1", coln_list, "Step 26: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 5, Test_Case_ID+"_Ds01.xlsx", 'Step 26.1: Verify Canvas report dataset ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 9, bg_cell_no=1, bg_color='yellow', bold=True, font_color='blue', text_value='223,690.00', msg='Step 26.2:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=4, bg_color='yellow', bold=True, font_color='red', text_value='42,920.00', msg='Step 26.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 36, bold=False, font_color='gray8', text_value='31,390.00', msg='Step 26.4:')
        
        
        """ 27. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()