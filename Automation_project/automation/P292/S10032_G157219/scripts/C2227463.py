'''
Created on Nov 15, 2017

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2227463
TestCase Name : Verify deleting Traffic Lights condition 
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_styling, ia_run
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2227463_TestClass(BaseTestCase):

    def test_C2227463(self):
        
        """    TESTCASE VARIABLES    """
        Test_Case_ID = 'C2227463'
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
        resultobj.wait_for_property(parent_css, 2)
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
            Step 03 : Verify the following report is displayed.
        """
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 03:00: Verify Canvas column titles ")
        time.sleep(2)
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 10, 3, "C2227463_Ds01.xlsx", 'Step 03:01: Verify report dataset')
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
            Step 06 : Verify the "Traffic Light Condition" window appears (Default = "Equal to").
        """
        ia_styling_obj.traffic_light_verify_condition_row(1, relation_name='Equal to')
        """
            Step 07 : Click on dropdown button > Enter "Value" = "ENGLAND" > "OK".
        """
        ia_styling_obj.traffic_light_create_new(1, filter_type='Constant', value_box_input='ENGLAND')
        time.sleep(2)
        """
            Step 08 : Click "Style" button.
            Step 09 : Change Font size = 12, Bold, Italic, Font color = Red, Background = Yellow.
            Step 10 : Click Apply
            Step 11 : Verify that "ENGLAND" is applied with the conditional styling.
        """
        time.sleep(2)
        ia_styling_obj.traffic_light_toolbar_select('Style', 1, font_size='12', bold=True, italic=True, text_color='red', background_color='yellow')
        time.sleep(2)
        ia_styling_obj.traffic_light_verify_condition_row(1, field_name='COUNTRY', relation_name='Equal to', Field_Value_txt='ENGLAND')
         
        """
            Step 12 : Click "OK".
        """
        ia_styling_obj.traffic_light_close_dialog('Apply')
        time.sleep(3)
        ia_styling_obj.traffic_light_close_dialog('Ok')
        time.sleep(3)
         
        """
            Step 13 : Click "Run".
        """
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(10)
        """
            Step 14 : Verify that proper styling is applied to the report.
        """
        ia_run_obj.verify_table_data_set("table[summary='Summary']", "C2227463_Ds02.xlsx" , 'Step 14:01: Verify report dataset')
        ia_run_obj.verify_table_cell_property("table[summary='Summary']", 2, 1, bg_color='yellow', font_color='red', text_value='ENGLAND', bold=True, italic=True, msg='Step 14:02:')
        
        """
            Step 15 : Click "IA" > "Save" > "C2227463" > Click "Save".
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(1)
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        """
            Step 16 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        """
            Step 17 : Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227463.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_3', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(5)
        """
            Step 18 : Select "COUNTRY" in Query pane > Click "Traffic Lights".
        """
        metaobj.querytree_field_click('COUNTRY', 1, 0)
        time.sleep(3)
        vis_ribbon_obj.select_ribbon_item('Field', 'trafficlights')
        time.sleep(5)
        """
            Step 19 : Click "Delete" in the Traffic Lights dialog
        """
        ia_styling_obj.traffic_light_toolbar_select('Delete', 1)
        time.sleep(3)
        
        """
            Step 20 : Verify condition is deleted
        """
        utillobj.verify_object_visible("#trafficLightsDlg #cstyMainPane [id^='condGridRowBox']", False, 'Step 20 : Verify condition is deleted')
        """
            Step 21 : Click OK
        """
        ia_styling_obj.traffic_light_close_dialog('Ok')
        time.sleep(3)
        
        """
            Step 22 : Run > Verify no traffic lights displayed 
        """
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(10)
        ia_run_obj.verify_table_data_set("table[summary='Summary']", "C2227463_Ds02.xlsx", 'Step 22:01: Verify report dataset')
        ia_run_obj.verify_table_cell_property("table[summary='Summary']", 2, 1, font_size='9pt', font_color='gray8', text_value='ENGLAND', msg='Step 22:02:')
        
        """
            Step 23 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
if __name__ == "__main__":
    unittest.main()