'''
Created on January 3, 2019

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313005
TestCase Name = AHTML: StreamGraph ColorBy chart Filtering/Exclusions.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.wftools import chart
from common.lib import base
from common.wftools import active_chart
from common.wftools import visualization


class C2313005_TestClass(BaseTestCase):

    def test_C2313005(self):
        
        """
        Test case objects
        """
        visual_obj = visualization.Visualization(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        chart_obj = chart.Chart(self.driver)
        base_obj = base.BasePage(self.driver)
        active_chart_obj = active_chart.Active_Chart(self.driver)
        
        """
        Test case CSS
        """
        x_axis_labels = "#MAINTABLE_wbody0 text[class^='xaxis']"
        
        """
        Test case variables
        """
        x_label_list = ['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        alfa_excluded_x_list = ['AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        alfa_audi_removed_list = ['BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        three_car_list = ['PEUGEOT', 'TOYOTA', 'TRIUMPH']
        bmw_removed_x_list = ['AUDI', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        legend_list = ['DEALER_COST:ENGLAND', 'RETAIL_COST:ENGLAND', 'DEALER_COST:FRANCE', 'RETAIL_COST:FRANCE', 'DEALER_COST:ITALY', 'RETAIL_COST:ITALY', 
                       'DEALER_COST:JAPAN', 'RETAIL_COST:JAPAN', 'DEALER_COST:W GERMANY', 'RETAIL_COST:W GERMANY']
        streamcolor_title = 'DEALER_COST, RETAIL_COST by COUNTRY, CAR'
        alfa_tooltip = ['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'COUNTRY:ITALY', 'Filter Chart', 'Exclude from Chart']
        
        """
        Step 1:Open FEX:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FStreamColorBy.fex&tool=Chart
        Click the Run button.
        Expect to see the following Active Streamgraph.
        """
        chart_obj.invoke_chart_in_edit_mode_using_api('StreamColorBy')
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(x_axis_labels, 11, base_obj.chart_medium_timesleep)
        chart_obj.verify_x_axis_label_in_run_window(x_label_list, parent_css='#MAINTABLE_wbody0_f',msg='Step 1.1: Verify the X axis')
        chart_obj.verify_legends_in_run_window(legend_list,parent_css='#MAINTABLE_wbody0_f', msg='Step 1.2: Verify the legends')
        active_chart_obj.verify_chart_title(streamcolor_title, 'Step 1.3: Verify title',parent_css='#MAINTABLE_wbody0_fmg')
        
        """
        Step 2: Hover over the lower area(red) for Alfa Romeo.
        Expect to see the following Tooltip information.
        """
        chart_obj.verify_tooltip_in_run_window("marker!s4!g0!mmarker!", alfa_tooltip, 'Step 2.1: Verify tooltip values',parent_css="#MAINTABLE_wbody0", use_marker_enable=True)
        
        """
        Step 3: Select the Exclude from Chart option.
        Expect to see the following Active Streamgraph, with Alfa Romeo excluded.
        """
        chart_obj.select_tooltip_in_run_window("marker!s4!g0!mmarker!", 'Exclude from Chart', parent_css="#MAINTABLE_wbody0", use_marker_enable=True)
        chart_obj.wait_for_number_of_element(x_axis_labels, 10, base_obj.chart_medium_timesleep)
        chart_obj.verify_x_axis_label_in_run_window(alfa_excluded_x_list, parent_css='#MAINTABLE_wbody0_f',msg='Step 3.1: Verify the Alfa Romeo is excluded')
        
        """
        Step 4: Hover over the upper area(light orange) for BMW.
        Select the Exclude from Chart option.
        Expect to see the following Active Streamgraph, with Alfa Romeo and BMW excluded.
        """
        chart_obj.select_tooltip_in_run_window("marker!s9!g1!mmarker!", 'Exclude from Chart', parent_css="#MAINTABLE_wbody0", use_marker_enable=True)
        chart_obj.wait_for_number_of_element(x_axis_labels, 9, base_obj.chart_medium_timesleep)
        chart_obj.verify_x_axis_label_in_run_window(bmw_removed_x_list, parent_css='#MAINTABLE_wbody0_f',msg='Step 4.1: Verify the Alfa romeo and BMW are excluded')
        
        """
        Step 5: Hover over the lower area(light green) for Audi and click the Remove Filter option.
        Expect to see the Filter removed and all CARs restored.
        """
        chart_obj.select_tooltip_in_run_window("marker!s8!g0!mmarker!", 'Remove Filter', parent_css="#MAINTABLE_wbody0", use_marker_enable=True)
        chart_obj.wait_for_number_of_element(x_axis_labels, 11, base_obj.chart_medium_timesleep)
        chart_obj.verify_x_axis_label_in_run_window(x_label_list, parent_css='#MAINTABLE_wbody0_f',msg='Step 5.1: Verify all cars available')
        
        """
        Step 6: Left click and draw a box that touches Alfa Romeo and Audi.
        Expect to see the following box around Alfa Romeo and Audi.
        """
        source_element = util_obj.validate_and_get_webdriver_object("#MAINTABLE_wbody0_f circle[class='marker!s0!g0!mmarker!']",'source')
        target_element = util_obj.validate_and_get_webdriver_object("#MAINTABLE_wbody0_f circle[class='marker!s9!g1!mmarker!']",'target')
        visual_obj.create_marker_lasso(source_element, target_element, source_xoffset=-20, source_yoffset=20, target_xoffset=20, target_yoffset=-20,  enable_marker=True)
        
        """
        Step 7: Select the Exclude from Chart option.
        Expect to see both Alfa Romeo and Audi removed.
        """
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        chart_obj.wait_for_number_of_element(x_axis_labels, 9, base_obj.chart_medium_timesleep)
        chart_obj.verify_x_axis_label_in_run_window(alfa_audi_removed_list, parent_css='#MAINTABLE_wbody0_f',msg='Step 7.1: Verify the Alfa romeo and Audi are excluded')
        
        """
        Step 8: Hover over the lower area(blue) for BMW and select the Remove Filter option.
        Expect to see the Filter removed and all CARs restored.
        """
        chart_obj.select_tooltip_in_run_window("marker!s8!g0!mmarker!", 'Remove Filter', parent_css="#MAINTABLE_wbody0", use_marker_enable=True)
        chart_obj.wait_for_number_of_element(x_axis_labels, 11, base_obj.chart_medium_timesleep)
        chart_obj.verify_x_axis_label_in_run_window(x_label_list, parent_css='#MAINTABLE_wbody0_f',msg='Step 8.1: Verify all cars available')
        
        """
        Step 9: Left click and draw a box that touches Peugeot, Toyota and Triumph.
        Select the Filter Chart option.
        Expect to see only data for Peugeot, Toyota & Triumph.
        """
        source_element = util_obj.validate_and_get_webdriver_object("#MAINTABLE_wbody0_f circle[class='marker!s0!g7!mmarker!']",'source')
        target_element = util_obj.validate_and_get_webdriver_object("#MAINTABLE_wbody0_f circle[class='marker!s1!g9!mmarker!']",'target')
        visual_obj.create_marker_lasso(source_element, target_element, source_xoffset=-20, source_yoffset=20, target_xoffset=50, target_yoffset=-50,  enable_marker=True)
        visual_obj.select_lasso_tooltip('Filter Chart')
        chart_obj.wait_for_number_of_element(x_axis_labels, 4, base_obj.chart_medium_timesleep)
        chart_obj.verify_x_axis_label_in_run_window(three_car_list, parent_css='#MAINTABLE_wbody0_f',msg='Step 9.1: Verify only 3 cars are present')
        
        """
        Step 10: Hover over the lower area(blue) for Peugeot and select the Remove Filter option.
        Launch Designer Workbook based on Reporting Object
        """
        chart_obj.select_tooltip_in_run_window("marker!s0!g0!mmarker!", 'Remove Filter', parent_css="#MAINTABLE_wbody0", use_marker_enable=True)
        chart_obj.wait_for_number_of_element(x_axis_labels, 11, base_obj.chart_medium_timesleep)
        chart_obj.verify_x_axis_label_in_run_window(x_label_list, parent_css='#MAINTABLE_wbody0_f',msg='Step 10.1: Verify all cars available')
        
        """
        Step 11: Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()        
