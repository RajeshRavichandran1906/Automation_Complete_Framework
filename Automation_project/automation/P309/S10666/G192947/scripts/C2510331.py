'''
Created on Jun 25, 2019

@author: Varun/Prasanth
Testcase Name : MarkerShape option "Fill" in Matrix Marker chart
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2510331

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.lib import core_utility
from common.wftools.designer_chart import Designer_Insight
from common.pages.insight_header import Insight_Header

class C2510331_TestClass(BaseTestCase):
    
    def test_C2510331(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        insight_obj=Designer_Insight(self.driver)
        insight_header_obj= Insight_Header(self.driver)
        
        """
        Test case variables
        """
        project_id=core_util_obj.parseinitfile("project_id")
        suite_id=core_util_obj.parseinitfile("suite_id")
        group_id=core_util_obj.parseinitfile("group_id")
        folder_path=project_id+"_"+suite_id+"/"+group_id
        expected_row_label_list=["COUNTRY", "ENGLAND", "FRANCE", "ITALY", "JAPAN", "W GERMANY"]
        expected_col_label_list=['BODYTYPE', 'CONVERTIBLE', 'COUPE', 'HARDTOP', 'ROADSTER', 'SEDAN', 'SALES', '0', '22K', '44K', '66.1K', '88.2K']
        
        """
        STEP 1:Launch the API to create new Chart.
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=chart&master=ibisamp/car
        """
        chart_obj.invoke_chart_tool_using_api("ibisamp/car", mrid="mrid", mrpass="mrpass", folder_path=folder_path)
        chart_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        
        """
        STEP 2 : Select Format > Run with > Insight
        """
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        chart_obj.select_ia_ribbon_item('Format', "insight")
        
        """
        STEP 3: Click Run 
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_visible_text(".main-box","Vertical Axis")
        
        """
        STEP 4: Click Chart picker drop down > Select Matrix Marker 
        """
        insight_header_obj.change_chart_type_from_chart_picker_option("Matrix")
        chart_obj.wait_for_visible_text(".main-box","Rows")
        
        """
        STEP 5: Add "COUNTRY" in ROWS bucket and "BODYTYPE" in COLUMNS bucket
        Add SALES in COLOR bucket
        """
        insight_header_obj.search_and_add_field_to_query_bucket("Rows", "COUNTRY")
        chart_obj.wait_for_visible_text(".main-box","COUNTRY")
        
        insight_header_obj.search_and_add_field_to_query_bucket("Columns", "BODYTYPE")
        chart_obj.wait_for_visible_text(".main-box","BODYTYPE")
        
        insight_header_obj.search_and_add_field_to_query_bucket("Color", "SALES")
        chart_obj.wait_for_visible_text(".main-box","SALES")
        
        """
        STEP 6: Verify following insight matrix marker chart displayed
        """
        
        insight_obj.verify_insight_querybox_text_options(['Rows', 'Columns', 'Size', 'Color'], "Step 06.01 : Verify_insight_querybox_text_options")
        insight_obj.verify_insight_optionsbox_text(['Reset', 'Swap  Axis', 'Change chart', 'Show Filter', 'Swap  Axis', 'More Options'], "Step 06.02 : Verify_insight_optionsbox_text")
        
        chart_obj.verify_rows_label_in_run_window(expected_row_label_list, ".main-box", msg="Step 06.03")
        chart_obj.verify_column_label_in_run_window(expected_col_label_list, ".main-box", msg="Step 06.04")
        chart_obj.verify_number_of_risers("#runbox_id circle[class*='riser']", 1, 9, msg="Step 06.05 : Verify circles")
        chart_obj.verify_chart_color("runbox_id", "riser!s0!g0!mmarker!r0!c0!", "persian_red", msg="Step 06.06 : Verify circle color")
        chart_obj.verify_chart_color("runbox_id", "riser!s0!g0!mmarker!r4!c4!", "elf_green", msg="Step 06.07 : Verify circle color")
        
        """
        STEP 7: Click More Options-> Marker Shape > Select SQUARE
        """
        insight_header_obj.select_or_verify_more_option_menu_item("Marker Shape", "Square", submenu=True)
        
        """
        STEP 8: Verify Marker shape changed to Square
        """
        chart_obj.wait_for_number_of_element("path[class*='riser']", 9)
        chart_obj.verify_number_of_risers("#runbox_id path[class*='riser']", 1, 9, msg="Step 08.01 : Verify Marker shape changed to Square")
        chart_obj.verify_rows_label_in_run_window(expected_row_label_list, ".main-box", msg="Step 08.02")
        chart_obj.verify_column_label_in_run_window(expected_col_label_list, ".main-box", msg="Step 08.03")
        
        
        """
        STEP 9: Click More Options-> Marker Shape > Select Fill
        """
        insight_header_obj.select_or_verify_more_option_menu_item("Marker Shape", "Fill", submenu=True)
        
        """
        STEP 10: Verify Marker shape changed to Fill
        """
        chart_obj.wait_for_number_of_element("rect[class*='riser']", 9)
        chart_obj.verify_number_of_risers("#runbox_id rect[class*='riser']", 1, 9, msg="Step 10.01 : Verify Marker shape changed to Fill")
        chart_obj.verify_rows_label_in_run_window(expected_row_label_list, ".main-box", msg="Step 10.02")
        chart_obj.verify_column_label_in_run_window(expected_col_label_list, ".main-box", msg="Step 10.03")
        
        """
        STEP 11 : Click IA > Close > click No.
        """
        chart_obj.switch_to_default_content()
        chart_obj.close_ia_without_save()
        
        """
        STEP 12 :Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
if __name__ == '__main__':
    unittest.main()
        