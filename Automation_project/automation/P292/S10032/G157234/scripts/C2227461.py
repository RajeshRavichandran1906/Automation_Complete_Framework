'''
Created on Nov 15, 2017

@author: BM13368
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_styling, ia_run
from common.lib.basetestcase import BaseTestCase


class C2227461_TestClass(BaseTestCase):

    def test_C2227461(self):
        
        """    TESTCASE VARIABLES    """
        driver= self.driver
        Test_Case_ID = 'C2227461'
        utillobj = utillity.UtillityMethods(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(driver)
        ia_resultarea_obj=ia_resultarea.IA_Resultarea(driver)
        ia_styling_obj=ia_styling.IA_Style(driver)
        ia_run_obj=ia_run.IA_Run(driver)
        """
            Step 01 : Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
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
#         ia_resultarea_obj.create_report_data_set('TableChart_1', 10, 3, 'C2227461_Ds01.xlsx', desired_no_of_rows=5)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 03:00: Verify Canvas column titles ")
        time.sleep(2)
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 10, 3, "C2227461_Ds01.xlsx", 'Step 03:01: Verify report dataset')
        """
            Step 04 : Select "DEALER_COST" in Query pane > click "Display" from "Field" tab.
        """
        metaobj.querytree_field_click('DEALER_COST', 1, 0)
        time.sleep(3)
        
        """
            Step 05 : Click "Traffic Lights" (Default = Greater than) > dropdown button > "Get Values" > "From File".
            Step 06 : Verify "Select From File..." window is displayed.
            Step 07 : Enable "Flat file or CSV" radio button.
            Step 08 : Click "Choose File" > select "Flat-File-Data-for-0027.txt" > "Open".
            Step 09 : Verify "Flat-File-Data-for-0027.txt" has been selected.
            Step 10 : Click "OK".
            Step 11 : Verify the "Values" textbox is populated with the flat file data.
            Step 12 : Select "33333" > "OK".
            Step 13 : Verify "33333" has been selected.
        """
        vis_ribbon_obj.select_ribbon_item('Field', 'trafficlights')
        time.sleep(8)
        ia_styling_obj.traffic_light_create_new(1, filter_type='Constant', getvalue_params='From File', flat_file='Flat-File-Data-for-0027.txt', browse_okBtn=True, value='3333')
        
        """
            Step 14 : Click "Style" button.
            Step 15 : Change Font size = 12, Bold, Italic, Center, Font color = Blue, Background = Green.
        """
        time.sleep(2)
        ia_styling_obj.traffic_light_toolbar_select('Style', 1, font_size='12', bold=True, italic=True, text_color='blue', background_color='lime')
        time.sleep(2)
       
        """
            Step 16 : Click "OK".
        """
        ia_styling_obj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_styling_obj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        
        """
            Step 17 : Verify the specified styling applied to "BMW" in "Live Preview".
        """
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 17:01: Verify Canvas column titles ")
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 10, 3, "C2227461_Ds01.xlsx", 'Step 17:02: Verify report dataset')
        
        """
            Step 18 : Click "Run".
        """
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(10)
        
        """
            Step 19 : Verify the specified styling applied to "BMW" in Run mode.
        """
#         ia_run_obj.create_table_data_set("table[summary='Summary']", 'C2227461_Ds02.xlsx', desired_no_of_rows=5)
        ia_run_obj.verify_table_data_set("table[summary='Summary']", "C2227461_Ds02.xlsx" , 'Step 19:01: Verify report dataset')
        ia_run_obj.verify_table_cell_property("table[summary='Summary']", 11, 3, bg_color='lime', font_color='blue', text_value='49,500', bold=True, italic=True, msg='Step 19:02:')
        
        """
            Step 20 : Dismiss the Run output window.
        """
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        
        """
            Step 21 : Click "Traffic Lights" (Default = Greater than) > dropdown button > "Get Values" > "From File".
        """
        vis_ribbon_obj.select_ribbon_item('Field', 'trafficlights')
        time.sleep(8)
        
        """
            Step 22 : Click "Choose File" > select "Excel-Data-for-0027.xlsx" > "Open".
            Step 23 : Verify "Excel-Data-for-0027.xlsx" has been selected.
            Step 24 : Verify "Excel Spreadsheet (XLS,XLSX)" radio button has been enabled.
            Step 25 : Click OK
            Step 26 : Verify the "Values" textbox is populated with the Excel (XLSX) data.
            Step 27 : Select "23232" > "OK".
            Step 28 : Verify "23232" has been selected.
        """
        ia_styling_obj.traffic_light_create_new(1, filter_type='Constant', getvalue_params='From File', flat_file='Excel-Data-for-0027.xlsx', browse_okBtn=True, value='23232')
        
        """
            Step 29 : Click "OK".
        """
        ia_styling_obj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_styling_obj.traffic_light_close_dialog('Ok')
        time.sleep(5)
        
        """
            Step 30 : Verify previously specified styling did not change and applied to "MASERATI" and "BMW" in "Live Preview".
        """
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 30:01: Verify Canvas column titles ")
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 10, 3, "C2227461_Ds01.xlsx", 'Step 30:02: Verify report dataset')
        ia_resultarea_obj.verify_report_cell_property("TableChart_1", 28, bg_cell_no=2, bg_color='lime', font_color='blue', text_value='49,500', bold=True, italic=True, msg='Step 30:03:')
        ia_resultarea_obj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=1, bg_color='lime', font_color='blue', text_value='25,000', bold=True, italic=True, msg='Step 30:04:')
        
        """
            Step 31 : Click "Run".
        """
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(10)
        
        """
            Step 32: Verify the specified styling applied to "MASERATI" and "BMW" in Run mode
        """
        ia_run_obj.verify_table_data_set("table[summary='Summary']", "C2227461_Ds02.xlsx" , 'Step 32:01: Verify report dataset')
        ia_run_obj.verify_table_cell_property("table[summary='Summary']", 11, 3, bg_color='lime', font_color='blue', text_value='49,500', bold=True, italic=True, msg='Step 32:02:')
        ia_run_obj.verify_table_cell_property("table[summary='Summary']", 7, 3, bg_color='lime', font_color='blue', text_value='25,000', bold=True, italic=True, msg='Step 32:03')
        
        """
            Step 33 : Click "IA" > "Save" > "C2227461" > Click "Save".
        """
        utillobj.switch_to_default_content(pause=2)
        time.sleep(2)
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 34 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
            Step 35 : Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227461.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_3', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
            Step 36 : Verify Preview
        """
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 36:01: Verify Canvas column titles ")
        ia_resultarea_obj.verify_report_data_set('TableChart_1', 10, 3, "C2227461_Ds01.xlsx", 'Step 36:02: Verify report dataset')
        ia_resultarea_obj.verify_report_cell_property("TableChart_1", 28, bg_cell_no=2, bg_color='lime', font_color='blue', text_value='49,500', bold=True, italic=True, msg='Step 36:03:')
        ia_resultarea_obj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=1, bg_color='lime', font_color='blue', text_value='25,000', bold=True, italic=True, msg='Step 36:04:')
        
        """
            Step 37 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()