'''
Created on 06-Jan-2017

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222795
TestCase Name = Verify multiple Traffic Light conditions with different styling, then remove each conditional one at a time
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2222795_TestClass(BaseTestCase):

    def test_C2222795(self):
        
        Test_Case_ID = "C2222795"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        
        """ 2. Double click COUNTRY, CAR, DEALER_COST        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        
        
        """ 3. Click on COUNTRY field in Canvas, then Display button from Field tab (If display group not expanded in Field tab )        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 3: Verify Canvas column titles ")
        time.sleep(2)
        ia_resultobj.select_field_on_canvas("TableChart_1", 1)
        
        
        """ 4. Display tab expands -> Click on Traffic Lights            """
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        
        
        """ 5. Select dropdown arrow and choose "Equal to"                                   """
        """ 6. Select the other dropdown arrow and enter value = "ENGLAND" and click "Ok"    """
        time.sleep(2)
        ia_stylingobj.traffic_light_verify_condition_row(1, field_name='COUNTRY', relation_name='Equal to', Field_Value_txt=' ')
        time.sleep(2)
        ia_stylingobj.traffic_light_create_new(1, relation_name='Equal to', filter_type='Constant', value_box_input='ENGLAND')
        
        
        """ 7. Now click on Style tab Make changes Bold, Font size-12, Italics, Underline, Justification - center, Text Color - RED , BG Color - YELLOW        """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, font_size='12', italic=True, underline=True, center_justify=True, text_color='red', background_color='yellow')
        time.sleep(2)
        
        
        """ 8. Now click on ""New"" option from Traffic Light Condition window        """
        ia_stylingobj.traffic_light_toolbar_select('New', 2)
        
        
        """ 9. Click on values dropdown menu            """
        """ 10. Type value: FRANCE -> Click "OK"        """
        time.sleep(2)
        ia_stylingobj.traffic_light_verify_condition_row(2, field_name='COUNTRY', relation_name='Equal to', Field_Value_txt=' ')
        time.sleep(2)
        ia_stylingobj.traffic_light_create_new(2, relation_name='Equal to', filter_type='Constant', value_box_input='FRANCE')
        
        
        """ 11. Now click on Style tab Make changes Bold, Font size-12, Italics, Underline, Justification - center, Text Color - BLUE , BG Color - YELLOW        """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 2, bold=True, font_size='12', italic=True, underline=True, center_justify=True, text_color='blue', background_color='yellow')
        time.sleep(2)
        
        
        """ 12. Now click on ""New"" option from Traffic Light Condition window        """
        ia_stylingobj.traffic_light_toolbar_select('New', 3)
        
        
        """ 13. Click on values dropdown menu            """
        """ 14. Type value: JAPAN -> Click" OK"          """
        time.sleep(2)
        ia_stylingobj.traffic_light_verify_condition_row(3, field_name='COUNTRY', relation_name='Equal to', Field_Value_txt=' ')
        time.sleep(2)
        ia_stylingobj.traffic_light_create_new(3, relation_name='Equal to', filter_type='Constant', value_box_input='JAPAN')
        
        
        """ 15. Now click on Style tab Make changes Bold, Font size-12, Italics, Underline, Justification - center, Text Color - GREEN , BG Color - YELLOW    """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 3, bold=True, font_size='12', italic=True, underline=True, center_justify=True, text_color='green', background_color='yellow')
        time.sleep(2)
        
        
        """ 16. Click Apply then OK            """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 16: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, "C2222778_Ds01.xlsx", 'Step 16.1: Verify report dataset ')
        
        
        """ 17. Verify Preview                """
        ia_resultobj.verify_report_cell_property("TableChart_1", 4, bg_cell_no=1, bg_color='yellow', bold=True, font_size='12pt', italic=True, underline=True, text_align='center', font_color='red', text_value='ENGLAND', msg='Step 17:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 11, bg_cell_no=2, bg_color='yellow', bold=True, font_size='12pt', italic=True, underline=True, text_align='center', font_color='blue', text_value='FRANCE', msg='Step 17.1:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 19, bg_cell_no=3, bg_color='yellow', bold=True, font_size='12pt', italic=True, underline=True, text_align='center', font_color='green', text_value='JAPAN', msg='Step 17.2:')
        
        
        """ 18. Click Field-Country tab -> Traffic lights        """
        time.sleep(2)
        ia_resultobj.select_field_on_canvas("TableChart_1", 1)
        time.sleep(3)
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        
        """ 19. Click "Delete"                            """
        ia_stylingobj.traffic_light_toolbar_select('Delete', 3)
        time.sleep(5)
        
        
        """ 20. Verify the last added TL condition is deleted Ensure that TL conditions are able to remove    """
        time.sleep(2)
        ia_stylingobj.traffic_light_verify_condition_row(2, total_row=2)
        time.sleep(2)
        
        """ 21. Click "Delete" again                            """
        ia_stylingobj.traffic_light_toolbar_select('Delete', 2)
        time.sleep(5)
        
        
        """ 22. Verify the second added TL condition is deleted Ensure that TL conditions are able to remove            """
        time.sleep(2)
        ia_stylingobj.traffic_light_verify_condition_row(1, total_row=1)
        time.sleep(2)
        
        """ 23. Click "Delete" again Verify all the added TL condtions are deleted ia_stylingobj.traffic_light_toolbar_select('Delete')                      """
        ia_stylingobj.traffic_light_toolbar_select('Delete', 1)
        time.sleep(5)
        ia_stylingobj.traffic_light_verify_condition_row(0, total_row=0)
        time.sleep(2)
        
        
        """ 24. Click "OK" and verify Preview                        """
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(7)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        ia_resultobj.verify_report_cell_property("TableChart_1", 4, font_size='9pt', font_color='gray8', text_value='ENGLAND', msg='Step 24:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 11, font_size='9pt', font_color='gray8', text_value='FRANCE', msg='Step 24.1:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 19, font_size='9pt', font_color='gray8', text_value='JAPAN', msg='Step 24.2:')
        
        
        
        """ 25. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp         """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("ia"+Test_Case_ID)
        time.sleep(2)


        
if __name__ == '__main__':
    unittest.main()