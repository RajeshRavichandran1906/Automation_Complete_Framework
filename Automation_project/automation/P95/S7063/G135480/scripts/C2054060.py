'''
Created on December 31, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7063&group_by=cases:section_id&group_id=135480&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2054060
TestCase Name = Chart Filtering/Exclusion using sorted Bar Measures. (ACT-522).
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.wftools.active_report import Active_Report
from common.wftools.visualization import Visualization
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods

class C2054060_TestClass(BaseTestCase):

    def test_C2054060(self):
        
        """
        TESTCASE Object's
        """
        active_chart_obj = Active_Chart(self.driver)
        active_rpt_obj = Active_Report(self.driver)
        visual_obj = Visualization(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        util_obj = UtillityMethods(self.driver)
        PARENT_CSS = "#MAINTABLE_wbody0_fmg g.chartPanel"
        page_load_css= PARENT_CSS + " text[class*='xaxisOrdinal-labels!g2!mgroupLabel']"
        W_GERMANY_CSS = PARENT_CSS + " rect[class*='riser!s0!g0!mbar']"
        ITALY_CSS = PARENT_CSS + " rect[class*='riser!s0!g1!mbar']"
        ENGLAND_CSS = PARENT_CSS + " rect[class*='riser!s0!g2!mbar']"
        JAPAN_CSS = PARENT_CSS + " rect[class*='riser!s0!g3!mbar']"
        FRANCE_CSS = PARENT_CSS + " rect[class*='riser!s0!g4!mbar']"
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        
        """
        Step 1: Sign in to WebFOCUS as a basic user
                http://machine:port/{alias}
        """
        """
        Step 2: Run the existing fex using the below API link
                http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P95_S7063/G135480&BIP_item=ACT522.fex
                Expect to see the following Bar chart, sorted by Descending Total Retail_Cost, with Countries along the X-Axis.
        """
        active_rpt_obj.run_active_report_using_api('ACT522.fex', column_css=page_load_css, synchronize_visible_element_text='ENGLAND', repository_path=folder_path)
        active_chart_obj.verify_x_axis_title_in_run_window(['COUNTRY'], msg='Step 2')
        active_chart_obj.verify_y_axis_title_in_run_window(['RETAIL_COST'], msg='Step 2.1')
        active_chart_obj.verify_chart_title('RETAIL_COST by COUNTRY', msg='Step 2.2', parent_css='#MAINTABLE_wbody0_fmg')
        active_chart_obj.verify_x_axis_label_in_run_window(['W GERMANY', 'ITALY', 'ENGLAND', 'JAPAN', 'FRANCE'], msg='Step 2.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K'], msg='Step 2.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, msg='Step 2.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(W_GERMANY_CSS, 'cerulean_blue', msg='Step 2.6')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 2.7', parent_css='#MAINTABLE_wmenu0')
        
        """
        Step 3: Left click the first Bar representing 'W GERMANY' and select Filter Chart.
                Expect to see only the Bar for W GERMANY in the Chart.
        """
        source_element = util_obj.validate_and_get_webdriver_object(W_GERMANY_CSS, 'W_GERMANY RISER')
        target_element = source_element
        visual_obj.create_lasso(source_element, target_element, source_xoffset=-15, source_yoffset=-19, target_xoffset=19, target_yoffset=19)
        visual_obj.select_lasso_tooltip('Filter Chart')
        util_obj.synchronize_until_element_disappear(page_load_css, 45)
        active_chart_obj.verify_x_axis_title_in_run_window(['COUNTRY'], msg='Step 3')
        active_chart_obj.verify_y_axis_title_in_run_window(['RETAIL_COST'], msg='Step 3.1')
        active_chart_obj.verify_chart_title('RETAIL_COST by COUNTRY', msg='Step 3.2', parent_css='#MAINTABLE_wbody0_fmg')
        active_chart_obj.verify_x_axis_label_in_run_window(['W GERMANY'], msg='Step 3.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K', '80K'], msg='Step 3.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 2, msg='Step 3.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(W_GERMANY_CSS, 'cerulean_blue', msg='Step 3.6')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 3.7', parent_css='#MAINTABLE_wmenu0')
        
        """
        Step 4: Click the remove filter button in the list of icons at the top. 
                Left click and drag a box around the last two Bars, for JAPAN and FRANCE, select Filter Chart.
                Expect to see original Char with all 5 Bars.
                Then, expect to see only two Bars for JAPAN and FRANCE.
        """
        active_chart_obj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 8)
        util_obj.synchronize_with_visble_text(page_load_css, 'ENGLAND', 45)
        active_chart_obj.verify_x_axis_title_in_run_window(['COUNTRY'], msg='Step 4')
        active_chart_obj.verify_y_axis_title_in_run_window(['RETAIL_COST'], msg='Step 4.1')
        active_chart_obj.verify_chart_title('RETAIL_COST by COUNTRY', msg='Step 4.2', parent_css='#MAINTABLE_wbody0_fmg')
        active_chart_obj.verify_x_axis_label_in_run_window(['W GERMANY', 'ITALY', 'ENGLAND', 'JAPAN', 'FRANCE'], msg='Step 4.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K'], msg='Step 4.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, msg='Step 4.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(W_GERMANY_CSS, 'cerulean_blue', msg='Step 4.6')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 4.7', parent_css='#MAINTABLE_wmenu0')
        source_element = util_obj.validate_and_get_webdriver_object(JAPAN_CSS, 'JAPAN RISER')
        target_element = util_obj.validate_and_get_webdriver_object(FRANCE_CSS, 'FRANCE RISER')
        visual_obj.create_lasso(source_element, target_element, source_xoffset=-9, source_yoffset=-9, target_xoffset=9, target_yoffset=9)
        visual_obj.select_lasso_tooltip('Filter Chart')
        util_obj.synchronize_until_element_disappear(page_load_css, 45)
        active_chart_obj.verify_x_axis_title_in_run_window(['COUNTRY'], msg='Step 4.8')
        active_chart_obj.verify_y_axis_title_in_run_window(['RETAIL_COST'], msg='Step 4.9')
        active_chart_obj.verify_chart_title('RETAIL_COST by COUNTRY', msg='Step 4.10', parent_css='#MAINTABLE_wbody0_fmg')
        active_chart_obj.verify_x_axis_label_in_run_window(['JAPAN', 'FRANCE'], msg='Step 4.11')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '1,000', '2,000', '3,000', '4,000', '5,000', '6,000', '7,000'], msg='Step 4.12')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 4, msg='Step 4.13')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(W_GERMANY_CSS, 'cerulean_blue', msg='Step 4.14')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 4.15', parent_css='#MAINTABLE_wmenu0')
        
        """
        Step 5: Click the remove filter button in the list of icons at the top. 
                Left click the second Bar for ITALY and select Exclude from Chart.
                Expect to see original Char with all 5 Bars.
                Expect to see the Bar Chart with the column for ITALY removed.
        """
        active_chart_obj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 8)
        util_obj.synchronize_with_visble_text(page_load_css, 'ENGLAND', 45)
        active_chart_obj.verify_x_axis_title_in_run_window(['COUNTRY'], msg='Step 5')
        active_chart_obj.verify_y_axis_title_in_run_window(['RETAIL_COST'], msg='Step 5.1')
        active_chart_obj.verify_chart_title('RETAIL_COST by COUNTRY', msg='Step 5.2', parent_css='#MAINTABLE_wbody0_fmg')
        active_chart_obj.verify_x_axis_label_in_run_window(['W GERMANY', 'ITALY', 'ENGLAND', 'JAPAN', 'FRANCE'], msg='Step 5.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K'], msg='Step 5.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, msg='Step 5.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(W_GERMANY_CSS, 'cerulean_blue', msg='Step 5.6')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 5.7', parent_css='#MAINTABLE_wmenu0')
        source_element = util_obj.validate_and_get_webdriver_object(ITALY_CSS, 'ITALY RISER')
        target_element = source_element
        visual_obj.create_lasso(source_element, target_element, source_xoffset=-15, source_yoffset=-19, target_xoffset=19, target_yoffset=19)
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        util_obj.synchronize_until_element_disappear(FRANCE_CSS, 45)
        active_chart_obj.verify_x_axis_title_in_run_window(['COUNTRY'], msg='Step 5.8')
        active_chart_obj.verify_y_axis_title_in_run_window(['RETAIL_COST'], msg='Step 5.9')
        active_chart_obj.verify_chart_title('RETAIL_COST by COUNTRY', msg='Step 5.10', parent_css='#MAINTABLE_wbody0_fmg')
        active_chart_obj.verify_x_axis_label_in_run_window(['W GERMANY', 'ENGLAND', 'JAPAN', 'FRANCE'], msg='Step 5.11')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K'], msg='Step 5.12')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 8, msg='Step 5.13')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(W_GERMANY_CSS, 'cerulean_blue', msg='Step 5.14')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 5.15', parent_css='#MAINTABLE_wmenu0')
        
        """
        Step 6: Click the remove filter button in the list of icons at the top. 
                Left click and drag a box around the third & fourth Bars, for ENGLAND & JAPAN, select Exclude from Chart.
                Expect to see the Bar Chart with the columns for ENGLAND & JAPAN removed.
        """
        active_chart_obj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 8)
        util_obj.synchronize_with_visble_text(page_load_css, 'ENGLAND', 45)
        active_chart_obj.verify_x_axis_title_in_run_window(['COUNTRY'], msg='Step 6')
        active_chart_obj.verify_y_axis_title_in_run_window(['RETAIL_COST'], msg='Step 6.1')
        active_chart_obj.verify_chart_title('RETAIL_COST by COUNTRY', msg='Step 6.2', parent_css='#MAINTABLE_wbody0_fmg')
        active_chart_obj.verify_x_axis_label_in_run_window(['W GERMANY', 'ITALY', 'ENGLAND', 'JAPAN', 'FRANCE'], msg='Step 6.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K'], msg='Step 6.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, msg='Step 6.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(W_GERMANY_CSS, 'cerulean_blue', msg='Step 6.6')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 6.7', parent_css='#MAINTABLE_wmenu0')
        source_element = util_obj.validate_and_get_webdriver_object(ENGLAND_CSS, 'ENGLAND RISER')
        target_element = util_obj.validate_and_get_webdriver_object(JAPAN_CSS, 'JAPAN RISER')
        visual_obj.create_lasso(source_element, target_element, source_xoffset=-9, source_yoffset=-9, target_xoffset=9, target_yoffset=9)
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        util_obj.synchronize_until_element_disappear(JAPAN_CSS, 45)
        active_chart_obj.verify_x_axis_title_in_run_window(['COUNTRY'], msg='Step 6.8')
        active_chart_obj.verify_y_axis_title_in_run_window(['RETAIL_COST'], msg='Step 6.9')
        active_chart_obj.verify_chart_title('RETAIL_COST by COUNTRY', msg='Step 6.10', parent_css='#MAINTABLE_wbody0_fmg')
        active_chart_obj.verify_x_axis_label_in_run_window(['W GERMANY', 'ITALY', 'FRANCE'], msg='Step 6.11')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K'], msg='Step 6.12')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 6, msg='Step 6.13')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(W_GERMANY_CSS, 'cerulean_blue', msg='Step 6.14')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 6.15', parent_css='#MAINTABLE_wmenu0')
        
        """
        Step 7: Logout: http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()