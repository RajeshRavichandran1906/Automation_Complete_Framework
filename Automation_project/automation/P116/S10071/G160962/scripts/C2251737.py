'''
Created on Jan 11, 2019

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251737
TestCase_Name : AHTML:CMPD MultiLayout return to filter box only shows 2 val (136793)
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_report import Active_Report
from common.wftools.active_chart import Active_Chart
from common.wftools import chart
from common.wftools import report
from common.wftools import document
from common.lib import utillity

class C2251737_TestClass(BaseTestCase):

    def test_C2251737(self):
        
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        active_reportobj = Active_Report(self.driver)
        report_obj = report.Report(self.driver)
        active_chart = Active_Chart(self.driver)
        chart_obj = chart.Chart(self.driver)
        doc_obj=document.Document(self.driver)
        
        """
        COMMON VARIABLES
        """
        MEDIUM_WAIT_TIME = 60
        chart_parent_css="MAINTABLE_wbody0"
        report_parent_css="#ITableData1"
        fex_name="136793"
        folder_name='P116/S10071_5'
        
        """
        Step 01: Execute the attached repro - ACT-198.fex
        """
        report_obj.run_fex_using_api_url(folder_name, fex_name, 'mrid', 'mrpass', run_table_css="#"+chart_parent_css, no_of_element=1, wait_time=MEDIUM_WAIT_TIME)
        
        """ 
        Step 01.1: Verify the bar chart is displayed
        """ 
        expected_x_axis_label_list=['2000 / 12', '2001 / 01', '2001 / 02', '2001 / 03', '2001 / 04', '2001 / 05', '2001 / 06', '2001 / 07', '2001 / 08', '2001 / 09', '2001 / 10', '2001 / 11', '2001 / 12', '2002 / 01', '2002 / 02', '2002 / 03', '2002 / 04', '2002 / 05', '2002 / 06', '2002 / 07', '2002 / 08', '2002 / 09', '2002 / 10', '2002 / 11', '2002 / 12']
        active_chart.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css='#'+chart_parent_css, xyz_axis_label_css="div[title^='200']", msg='Step 01.1')
        active_chart.verify_y_axis_label_in_run_window(['0', '200 K', '400 K', '600 K', '800 K'], parent_css='#'+chart_parent_css, xyz_axis_label_css="[style*='right']", msg='Step 01.2')
        active_chart.verify_chart_color_using_get_css_property_in_preview("div[title*='13169'][style*='rect']", 'Lochmara', parent_css='#'+chart_parent_css, attribute='background-color', msg='Step 01.3')
        active_chart.verify_chart_title('Price: by YEAR, MONTH', msg='Step 01.4', parent_css='#'+chart_parent_css, title_css="div[style*='center'][onclick] div")
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 01.5', parent_css='#MAINTABLE_wmenu0')
        chart_obj.verify_number_of_chart_segment(chart_parent_css, 25, msg='Step 01.6: Verify number of bar risers', custom_css="div[title^='Price'][style*='rect']")
        
        """
        Step 02: select "2001" drop down value form page layout 1
        """
        time.sleep(3)
        utillobj.select_dropdown("[id='combobox_dsCOMBOBOX1']", 'visible_text', '2001')
        
        """ 
        Step 02.1: Verify the bar chart is displayed
        """ 
        active_chart.wait_for_number_of_element("#"+chart_parent_css+" div[title^='Price'][style*='rect']", 12, MEDIUM_WAIT_TIME)
        expected_x_axis_label_list=['2001 / 01', '2001 / 02', '2001 / 03', '2001 / 04', '2001 / 05', '2001 / 06', '2001 / 07', '2001 / 08', '2001 / 09', '2001 / 10', '2001 / 11', '2001 / 12']
        x_axis_label_css="#MAINTABLE_wbody0 div[title^='200']"
        x_axis_label_obj=utillobj.validate_and_get_webdriver_objects(x_axis_label_css, "x_axis_label_list")
        actual_x_axis_label_list=[i.text for i in x_axis_label_obj]
        utillobj.as_List_equal(expected_x_axis_label_list, actual_x_axis_label_list, "Step 02.1: Verify x_axis_label_list")
        active_chart.verify_y_axis_label_in_run_window(['0', '200 K', '400 K', '600 K', '800 K'], parent_css='#'+chart_parent_css, xyz_axis_label_css="[style*='right']", msg='Step 02.2')
        active_chart.verify_chart_color_using_get_css_property_in_preview("div[title*='180131'][style*='rect']", 'Lochmara', parent_css='#'+chart_parent_css, attribute='background-color', msg='Step 02.3')
        active_chart.verify_chart_title('Price: by YEAR, MONTH', msg='Step 02.4', parent_css='#'+chart_parent_css, title_css="div[style*='center'][onclick] div")
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 02.5', parent_css='#MAINTABLE_wmenu0')
        chart_obj.verify_number_of_chart_segment(chart_parent_css, 12, msg='Step 02.6: Verify number of bar risers', custom_css="div[title^='Price'][style*='rect']")
        utillobj.verify_dropdown_value("[id='combobox_dsCOMBOBOX1']",expected_default_selected_value='2001', default_selection_msg="Step 02.7: Expect to see the initial Combo Box value of '2001'")
        
        """
        Step 03: Select page layout 2 tab from compound report
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page layout 2')
        active_chart.wait_for_number_of_element(report_parent_css, 1, MEDIUM_WAIT_TIME)
        
        """
        Step 03.1: Verify the report is displayed
        """
        active_reportobj.verify_page_summary(1, '25of25records,Page1of2', "Step 03.1: Expect to see the following Active Report with 25 records")
        time.sleep(3)
#         active_reportobj.create_reporttable_dataset(file_name='C2251737_Ds01.xlsx', table_css=report_parent_css)
        active_reportobj.verify_active_report_dataset(file_name='C2251737_Ds01.xlsx', table_css=report_parent_css, msg='Step 03.2: Verify data set')
        
        """
        Step 04: Again select page layout 1 Tab
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page layout 1')
        active_chart.wait_for_number_of_element("#"+chart_parent_css, 1, MEDIUM_WAIT_TIME)
        
        """ 
        Step 04.1: Verify report get filtered with 2001 value
        """
        utillobj.as_List_equal(expected_x_axis_label_list, actual_x_axis_label_list, "Step 02.1: Verify x_axis_label_list")
        active_chart.verify_y_axis_label_in_run_window(['0', '200 K', '400 K', '600 K', '800 K'], parent_css='#'+chart_parent_css, xyz_axis_label_css="[style*='right']", msg='Step 02.2')
        active_chart.verify_chart_color_using_get_css_property_in_preview("div[title*='180131'][style*='rect']", 'Lochmara', parent_css='#'+chart_parent_css, attribute='background-color', msg='Step 02.3')
        active_chart.verify_chart_title('Price: by YEAR, MONTH', msg='Step 02.4', parent_css='#'+chart_parent_css, title_css="div[style*='center'][onclick] div")
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 02.5', parent_css='#MAINTABLE_wmenu0')
        chart_obj.verify_number_of_chart_segment(chart_parent_css, 12, msg='Step 02.6: Verify number of bar risers', custom_css="div[title^='Price'][style*='rect']")
        utillobj.verify_dropdown_value("[id='combobox_dsCOMBOBOX1']",expected_default_selected_value='2001', default_selection_msg="Step 02.7: Expect to see the initial Combo Box value of '2001'")
        
if __name__ == "__main__":
    unittest.main()