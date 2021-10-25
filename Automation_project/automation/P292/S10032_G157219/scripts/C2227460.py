'''
Created on Nov 14, 2017

@author: BM13368
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_styling, ia_run
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2227460_TestClass(BaseTestCase):

    def test_C2227460(self):
        
        """    TESTCASE VARIABLES    """
        Test_Case_ID = 'C2227460'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultarea_obj=ia_resultarea.IA_Resultarea(self.driver)
        ia_styling_obj=ia_styling.IA_Style(self.driver)
        ia_run_obj=ia_run.IA_Run(self.driver)
        """
            Step 01 : Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """
            Step 02 : Double click "COUNTRY", "CAR", "DEALER_COST".
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
         
        """
            Step 03 : Verify the following report is displayed
        """
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 10, 3, "C2227460_Ds01.xlsx", 'Step 03:01: Verify report dataset')
        """
            Step 04 : Select "COUNTRY" in Query pane > click "Display" from "Field" tab (If not already expanded)
        """
        metaobj.querytree_field_click('COUNTRY', 1, 0)
        time.sleep(3)
        """
            Step 05 : Click "Traffic Lights".
        """
        vis_ribbon_obj.select_ribbon_item('Field', 'trafficlights')
        time.sleep(8)
        """
            Step 06 : Click on dropdown button > Enter "Value" = "ENGLAND" > "OK".
        """
        ia_styling_obj.traffic_light_verify_condition_row(1, field_name='COUNTRY', relation_name='Equal to', Field_Value_txt=' ')
        time.sleep(2)
        ia_styling_obj.traffic_light_create_new(1, filter_type='Constant', value_box_input='ENGLAND')
        time.sleep(2)
        """
            Step 07 : Click "Style" > Font size = 12, Font color = Red, Bold.
        """
        ia_styling_obj.traffic_light_toolbar_select('Style', 1, font_size='12', bold=True, text_color='red')
        time.sleep(2)
        """
            Step 08 : Click "New" button.
        """
        ia_styling_obj.traffic_light_toolbar_select('New', 2)
        time.sleep(2)
         
        """
            Step 09 : Click on dropdown button > Enter "Value" = "JAPAN" > "OK".
        """
        ia_styling_obj.traffic_light_create_new(2, filter_type='Constant', value_box_input='JAPAN')
        time.sleep(2)
         
        """
            Step 10 : Click "Style" > Font size = 12, Font color = Blue, Bold.
        """
        ia_styling_obj.traffic_light_toolbar_select('Style', 2, font_size='12', bold=True, text_color='blue')
        """
            Step 11 : Click "New" button.
        """
        ia_styling_obj.traffic_light_toolbar_select('New', 3)
        """
            Step 12 : Click on dropdown button > Enter "Value" = "FRANCE" > "OK".
        """
        time.sleep(2)
        ia_styling_obj.traffic_light_create_new(3, filter_type='Constant', value_box_input='FRANCE')
        time.sleep(2)
         
        """
            Step 13 : Click "Style" > Font size = 12, Font color = Green, Bold.
        """
        ia_styling_obj.traffic_light_toolbar_select('Style', 3, font_size='12', bold=True, text_color='lime')
        time.sleep(2)
        """
            Step 14 : Click "Apply".
        """
        ia_styling_obj.traffic_light_close_dialog('Apply')
        time.sleep(3)
         
        """
            Step 15 : Verify conditional styling is applied to "ENGLAND", "JAPAN" and "FRANCE"
        """
        ia_styling_obj.traffic_light_verify_preview(1, preview_font_name='Arial', preview_font_size='12', preview_bold=True, preview_text_color='red')
        ia_styling_obj.traffic_light_verify_preview(2, preview_font_name='Arial', preview_font_size='12', preview_bold=True, preview_text_color='blue')
        ia_styling_obj.traffic_light_verify_preview(3, preview_font_name='Arial', preview_font_size='12', preview_bold=True, preview_text_color='lime')
        time.sleep(1)
                 
        """
            Step 16 : Click "OK".
        """
        ia_styling_obj.traffic_light_close_dialog('Ok')
        time.sleep(3)
        
        """
            Step 17 : Click "Run".
        """
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(10)
        
        """
            Step 18 : Verify the report is displayed.
        """
        ia_run_obj.verify_table_cell_property("table[summary='Summary']", 2, 1, font_color='red', text_value='ENGLAND', font_size='12pt', bold=True, msg='Step 18:01:Verify Country cell styling')
        ia_run_obj.verify_table_cell_property("table[summary='Summary']", 5, 1, font_color='lime', text_value='FRANCE', font_size='12pt', bold=True, msg='Step 18:02:Verify FRANCE cell styling')
        ia_run_obj.verify_table_cell_property("table[summary='Summary']", 8, 1, font_color='blue', text_value='JAPAN', font_size='12pt', bold=True, msg='Step 18:03:Verify JAPAN cell styling')
        """
            Step 19 : Click "IA" > "Save".
            Step 20 : Enter Title = "C2227460".
            Step 21 : Click "Save".
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(1)
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
       
        """
            Step 22 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        """
            Step 23 : Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227460.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_3', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
        """
            Step 24 : Verify Preview
        """
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 10, 3, "C2227460_Ds01.xlsx", 'Step 24:00: Verify report dataset')
        ia_resultarea_obj.verify_report_cell_property("TableChart_1", 4, font_color='red', text_value='ENGLAND', font_size='12pt', bold=True, msg='Step 18:01:Verify Country cell styling')
        ia_resultarea_obj.verify_report_cell_property("TableChart_1", 11, font_color='lime', text_value='FRANCE', font_size='12pt', bold=True, msg='Step 18:02:Verify FRANCE cell styling')
        ia_resultarea_obj.verify_report_cell_property("TableChart_1", 19, font_color='blue', text_value='JAPAN', font_size='12pt', bold=True, msg='Step 18:03:Verify JAPAN cell styling')
        """
            Step 25 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()