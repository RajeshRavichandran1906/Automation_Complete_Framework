'''
Created on January 24, 2019

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8357890
TestCase Name = AHTML:Cache:Webpage error when filtering with DATEs (MtYY) (ACT-383)
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.wftools.active_report import Active_Report
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods

class C8357890_TestClass(BaseTestCase):

    def test_C8357890(self):
        
        """
        TESTCASE Object's
        """
        active_chart_obj = Active_Chart(self.driver)
        active_report_obj = Active_Report(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        util_obj = UtillityMethods(self.driver)
        
        """
        Testcase CSS
        """
        PARENT_CSS = "#MAINTABLE_wbody0_fmg g.chartPanel"
        page_load_css= PARENT_CSS + " text[class*='xaxisOrdinal-labels!g0!mgroupLabel']"
        action_css = PARENT_CSS + " rect[class*='riser!s0!g0!mbar']"
        chart_title_css = '#MAINTABLE_wbody0_fmg'
        drop_down_css = '#combobox_dsPROMPT_1'
        toolbar_css = '#MAINTABLE_wmenu0'
        
        """
        Testcase Variables
        """
        fex_name = 'ACT-383_ON.fex'
        riser_type = 'rect'
        riser_color = 'cerulean_blue'
        chart_toolbar_list = ['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        x_axis_title = ['CATEGORY : Define_1 : DIRECTOR']
        y_axis_title= ['COPIES']
        chart_title = 'COPIES by CATEGORY, DIRECTOR'
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        drop_down_values = ['Jun, 1939', 'May, 1940', 'Aug, 1941', 'Nov, 1941', 'Mar, 1942', 'Jul, 1942', 'Nov, 1950', 'Jul, 1951',
                             'Jul, 1954', 'Dec, 1954', 'Jan, 1955', 'Oct, 1955', 'Nov, 1958', 'Dec, 1958', 'Jan, 1959', 'Feb, 1959',
                              'May, 1960', 'Jan, 1962', 'Sep, 1963', 'Nov, 1972', 'Jul, 1973', 'Aug, 1975', 'Apr, 1976', 'Dec, 1976',
                               'Apr, 1978', 'May, 1978', 'Mar, 1980', 'Apr, 1980', 'May, 1980', 'Jul, 1981', 'Jul, 1982', 'Sep, 1982',
                                'Mar, 1983', 'Feb, 1984', 'Nov, 1984', 'Aug, 1985', 'Aug, 1986', 'Oct, 1986', 'Nov, 1986', 'Dec, 1986',
                                 'Jan, 1987', 'Sep, 1987', 'Oct, 1987', 'Jan, 1988', 'Feb, 1988', 'Mar, 1988', 'Apr, 1988', 'May, 1988', 
                                 'Jun, 1988', 'Jul, 1988', 'Aug, 1988', 'Oct, 1988', 'Feb, 1989', 'Dec, 1989', 'Jan, 1990', 'Jun, 1990', 'Mar, 1991']
        
        """
        Step 1: Log in to WebFOCUS
        http://machine:port/{alias}
        """
        """
        Step 2: Run the existing fex using the below API link
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P116_18157/685302&BIP_item=ACT-383_ON.fex
        Verify chart is displayed with Date dropdown box without any webpage error.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=page_load_css, synchronize_visible_element_text='ACTION/VERHOVEN P.', repository_path=folder_path)
        active_chart_obj.verify_x_axis_title_in_run_window(x_axis_title, msg='Step 2')
        active_chart_obj.verify_y_axis_title_in_run_window(y_axis_title, msg='Step 2.1')
        active_chart_obj.verify_chart_title(chart_title, msg='Step 2.2', parent_css=chart_title_css)
        active_chart_obj.verify_x_axis_label_in_run_window(['ACTION/VERHOVEN P.', 'FOREIGN/SCOLA E.'], msg='Step 2.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5'], msg='Step 2.4')
        active_chart_obj.verify_number_of_risers_in_run_window(riser_type, 1, 4, msg='Step 2.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(action_css, riser_color, msg='Step 2.6')
        active_chart_obj.verify_active_chart_toolbar(chart_toolbar_list, msg='Step 2.7', parent_css=toolbar_css)
        util_obj.verify_dropdown_value(drop_down_css, drop_down_values, 'Step 2.9: Verify the dropdown value', expected_default_selected_value='Jun, 1988', default_selection_msg='Step 2.8: Verify the selected dropdown')
        
        """
        Step 3: Change the value from dropdown eg:Jan 1987
        Verify the chart is changed without any error.
        """
        util_obj.select_dropdown(drop_down_css, 'visible_text', 'Jan, 1987')
        active_chart_obj.wait_for_number_of_element("#MAINTABLE_wbody0_fmg g.chartPanel text[class^='xaxis']", 2, active_chart_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_title_in_run_window(x_axis_title, msg='Step 3')
        active_chart_obj.verify_y_axis_title_in_run_window(y_axis_title, msg='Step 3.1')
        active_chart_obj.verify_chart_title(chart_title, msg='Step 3.2', parent_css=chart_title_css)
        active_chart_obj.verify_x_axis_label_in_run_window(['MYSTERY/LUMET S.'], msg='Step 3.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '0.2', '0.4', '0.6', '0.8', '1', '1.2'], msg='Step 3.4')
        active_chart_obj.verify_number_of_risers_in_run_window(riser_type, 1, 2, msg='Step 3.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(action_css, riser_color, msg='Step 3.6')
        active_chart_obj.verify_active_chart_toolbar(chart_toolbar_list, msg='Step 3.7', parent_css=toolbar_css)
        util_obj.verify_dropdown_value(drop_down_css, drop_down_values, 'Step 3.9: Verify the dropdown value', expected_default_selected_value='Jan, 1987', default_selection_msg='Step 3.8: Verify the selected dropdown')
        
        """
        Step 4:     
        Logout:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()