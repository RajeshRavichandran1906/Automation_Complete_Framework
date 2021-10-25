'''
Created on Jan 14, 2019

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251734 
TestCase_Name : AHTML: Multi-sorted Compound Component Document, one Filter at a time.
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.wftools import chart, visualization
from common.lib import utillity, core_utility
from common.lib.global_variables import Global_variables

class C2251734_TestClass(BaseTestCase):
    
    def test_C2251734(self):
            
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        coreutillityobject = core_utility.CoreUtillityMethods(self.driver)
        active_chart = Active_Chart(self.driver)
        chart_obj = chart.Chart(self.driver)
        visual_obj = visualization.Visualization(self.driver)
        
        """
        COMMON VARIABLES
        """
        MEDIUM_WAIT_TIME = 60
        barchart_parent_css="MAINTABLE_wbody0"
        piechart1_parent_css="MAINTABLE_wbody1"
        piechart2_parent_css="MAINTABLE_wbody2"
        fex_name="BS_Dashboard"
        folder_name='P116/S10071_5'
        
        def verify_tooltip(parent_css, riser_css, expected_tooltip_list, msg, element_location='middle', xoffset=0):
            x=Global_variables.current_working_area_browser_x
            y=Global_variables.current_working_area_browser_y
            coreutillityobject.move_mouse_to_offset(x_offset=x, y_offset=y)
            tooltip_elem=self.driver.find_element_by_css_selector("#"+parent_css+" [class*='"+riser_css+"']")
            coreutillityobject.python_move_to_element(tooltip_elem, element_location=element_location, xoffset=xoffset, yoffset=0)
            tooltip_css="span[id*='tdgchart-tooltip'][style*='visible']"
            tooltip_obj=utillobj.validate_and_get_webdriver_object(tooltip_css, 'tooltip is visible')
            raw_tooltip_list=tooltip_obj.text.replace(u'\xa0\n', '').replace(u'\xa0', ' ').split('\n')
            actual_list=utillobj.get_actual_tooltip_list(raw_tooltip_list)
            utillobj.asequal(expected_tooltip_list, actual_list, msg)
        
        """
        Step 01: Execute the attached Document Fex - BS_Dashboard.
        """
        active_chart.run_fex_using_api_url(folder_name, fex_name, 'mrid', 'mrpass', run_chart_css="#"+barchart_parent_css+" rect[class*='riser!'][class*='mbar!']", no_of_element=25, wait_time=MEDIUM_WAIT_TIME)
        
        """ 
        Step 01.1: Expect to see the following three component Dashboard, with a Bar Chart and two PIEs.
        """ 
        "---a. Bar chart1---"
        expected_x_axis_title_list=['Country : Product Type']
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#'+barchart_parent_css, msg="Step 01.1: Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity']
        active_chart.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css='#'+barchart_parent_css, msg="Step 01.2: Verify y_axis title at runtime")
        expected_x_axis_label_list=['Canada/Audio', 'Canada/Ca...', 'Canada/Ca...', 'Canada/Office', 'Canada/Video', 'France/Audio', 'France/Ca...', 'France/Ca...', 'France/Office']
        active_chart.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css='#'+barchart_parent_css, xyz_axis_label_length=8, msg='Step 01.3')
        active_chart.verify_y_axis_label_in_run_window(['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K'], parent_css='#'+barchart_parent_css, msg='Step 01.4')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class^='riser!s0!g0!mbar!']", 'cerulean_blue', parent_css='#'+barchart_parent_css, msg='Step 01.5')
        active_chart.verify_chart_title('Quantity by Country, Product Type', msg='Step 01.6', parent_css='#'+barchart_parent_css)
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 01.7', parent_css='#MAINTABLE_wmenu0')
        chart_obj.verify_number_of_chart_segment(barchart_parent_css, 25, msg='Step 01.8: Verify number of bar risers', custom_css="[class*='riser!'][class*='mbar!']")
        
        "---b. Pie chart1---"
        expected_x_axis_title_list=['Quantity']
        active_chart.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#'+piechart1_parent_css, x_or_y_axis_title_css="text[class*='pieLabel!']", msg="Step 01.9: Verify Pie chart1 title at runtime")
        expected_x_axis_label_list=['11%', '4%', '5%', '4%', '75%']
        active_chart.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css='#'+piechart1_parent_css, xyz_axis_label_css="text[class*='dataLabels!']", msg='Step 01.10')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class^='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css='#'+piechart1_parent_css, msg='Step 01.11')
        active_chart.verify_chart_title('Quantity by Country,', msg='Step 01.12', parent_css='#'+piechart1_parent_css)
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 01.13', parent_css='#MAINTABLE_wmenu1')
        expected_legend_list=['Canada', 'France', 'Germany', 'Spain', 'United States']
        active_chart.verify_legends_in_run_window(expected_legend_list, parent_css='#'+piechart1_parent_css, msg='Step 01.14: Verify legends in pie chart1')
        chart_obj.verify_number_of_chart_segment(piechart1_parent_css, 5, msg='Step 01.15: Verify number of bar risers', custom_css="[class*='riser!'][class*='mwedge!']")
        
        "---c. Pie chart2---"
        expected_x_axis_title_list=['Quantity']
        active_chart.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#'+piechart2_parent_css, x_or_y_axis_title_css="text[class*='pieLabel!']", msg="Step 01.16: Verify Pie chart1 title at runtime")
        expected_x_axis_label_list=['38%', '16%', '17%', '11%', '18%']
        active_chart.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css='#'+piechart2_parent_css, xyz_axis_label_css="text[class*='dataLabels!']", msg='Step 01.17')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class^='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css='#'+piechart2_parent_css, msg='Step 01.18')
        active_chart.verify_chart_title('Quantity by Product Type,', msg='Step 01.19', parent_css='#'+piechart2_parent_css)
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 01.20', parent_css='#MAINTABLE_wmenu1')
        expected_legend_list=['Audio', 'Camcorders', 'Cameras', 'Office', 'Video']
        active_chart.verify_legends_in_run_window(expected_legend_list, parent_css='#'+piechart2_parent_css, msg='Step 01.21: Verify legends in pie chart2')
        chart_obj.verify_number_of_chart_segment(piechart2_parent_css, 5, msg='Step 01.22: Verify number of bar risers', custom_css="[class*='riser!'][class*='mwedge!']")
        
        """
        Step 02: Using the Bar Chart, left-click and grab the last 5 bars, representing all of the United States.
        """
        source_element=utillobj.validate_and_get_webdriver_object("#MAINTABLE_wbody0 rect[class*='riser!s0!g20!mbar!']", 'United States source riser bar')
        target_element=utillobj.validate_and_get_webdriver_object("#MAINTABLE_wbody0 rect[class*='riser!s0!g24!mbar!']", 'United States target riser bar')
        visual_obj.create_lasso(source_element, target_element)
         
        """
        Step 02.1: Expect to see the Filter menu appear on the right-hand side over the bars for United States.
        """
        item_list=['5 points', 'Filter Chart', 'Exclude from Chart']
        chart_obj.verify_lasso_filter(item_list, msg='Step 02.1: Expect to see the Filter menu')
         
        """
        Step 03: Click the Exclude from Chart button.
        """
        chart_obj.select_lasso_filter(select_item='Exclude from Chart')
         
        """ 
        Step 03.1: Expect to see the following dashboard, with the United States removed from the Bar Chart and the bottom left PIE
        """ 
        "---a. Bar chart1---"
        active_chart.wait_for_number_of_element(element_css="#"+barchart_parent_css+" rect[class*='riser!'][class*='mbar!']", expected_number=20, time_out=MEDIUM_WAIT_TIME)
        expected_x_axis_title_list=['Country : Product Type']
        active_chart.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#'+barchart_parent_css, msg="Step 03.1: Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity']
        active_chart.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css='#'+barchart_parent_css, msg="Step 03.2: Verify y_axis title at runtime")
        expected_x_axis_label_list=['Canada/Audio', 'Canada/Ca...', 'Canada/Ca...', 'Canada/Office', 'Canada/Video', 'France/Audio', 'France/Ca...', 'France/Ca...', 'France/Office']
        active_chart.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css='#'+barchart_parent_css, xyz_axis_label_length=8, msg='Step 03.3')
        active_chart.verify_y_axis_label_in_run_window(['0', '20K', '40K', '60K', '80K', '100K', '120K'], parent_css='#'+barchart_parent_css, msg='Step 03.4')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class^='riser!s0!g0!mbar!']", 'cerulean_blue', parent_css='#'+barchart_parent_css, msg='Step 03.5')
        active_chart.verify_chart_title('Quantity by Country, Product Type', msg='Step 03.6', parent_css='#'+barchart_parent_css)
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 03.7', parent_css='#MAINTABLE_wmenu0')
        chart_obj.verify_number_of_chart_segment(barchart_parent_css, 20, msg='Step 03.8: Verify number of bar risers', custom_css="[class*='riser!'][class*='mbar!']")
         
        "---b. Pie chart1---"
        active_chart.wait_for_number_of_element(element_css="#"+piechart1_parent_css+" path[class*='riser!'][class*='mwedge!']", expected_number=4, time_out=MEDIUM_WAIT_TIME)
        expected_x_axis_title_list=['Quantity']
        active_chart.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#'+piechart1_parent_css, x_or_y_axis_title_css="text[class*='pieLabel!']", msg="Step 03.9: Verify Pie chart1 title at runtime")
        expected_x_axis_label_list=['45%', '17%', '21%', '18%']
        active_chart.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css='#'+piechart1_parent_css, xyz_axis_label_css="text[class*='dataLabels!']", msg='Step 03.10')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class^='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css='#'+piechart1_parent_css, msg='Step 03.11')
        active_chart.verify_chart_title('Quantity by Country,', msg='Step 03.12', parent_css='#'+piechart1_parent_css)
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 03.13', parent_css='#MAINTABLE_wmenu1')
        expected_legend_list=['Canada', 'France', 'Germany', 'Spain']
        active_chart.verify_legends_in_run_window(expected_legend_list, parent_css='#'+piechart1_parent_css, msg='Step 03.14: Verify legends in pie chart1')
        chart_obj.verify_number_of_chart_segment(piechart1_parent_css, 4, msg='Step 03.15: Verify number of bar risers', custom_css="[class*='riser!'][class*='mwedge!']")
         
        "---c. Pie chart2---"
        active_chart.wait_for_number_of_element(element_css="#"+piechart2_parent_css+" path[class*='riser!'][class*='mwedge!']", expected_number=5, time_out=MEDIUM_WAIT_TIME)
        expected_x_axis_title_list=['Quantity']
        active_chart.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#'+piechart2_parent_css, x_or_y_axis_title_css="text[class*='pieLabel!']", msg="Step 03.16: Verify Pie chart1 title at runtime")
        expected_x_axis_label_list=['38%', '16%', '16%', '12%', '18%']
        active_chart.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css='#'+piechart2_parent_css, xyz_axis_label_css="text[class*='dataLabels!']", msg='Step 03.17')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class^='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css='#'+piechart2_parent_css, msg='Step 03.18')
        active_chart.verify_chart_title('Quantity by Product Type,', msg='Step 03.19', parent_css='#'+piechart2_parent_css)
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 03.20', parent_css='#MAINTABLE_wmenu1')
        expected_legend_list=['Audio', 'Camcorders', 'Cameras', 'Office', 'Video']
        active_chart.verify_legends_in_run_window(expected_legend_list, parent_css='#'+piechart2_parent_css, msg='Step 03.21: Verify legends in pie chart2')
        chart_obj.verify_number_of_chart_segment(piechart2_parent_css, 5, msg='Step 03.22: Verify number of bar risers', custom_css="[class*='riser!'][class*='mwedge!']")
         
        """
        Step 04: To prove that the bottom right PIE has also changed, hover the slice for Audio.
        Step 04.1: Expect to see the filtered value of 218K appear.
        """
        verify_tooltip(piechart2_parent_css, riser_css='riser!s0!g0!mwedge!', expected_tooltip_list=['Audio:218K (37.74%)'], msg='Step 04.1: Expect to see the filtered value of 218K appear.')
         
        """ 
        Step 05: Remove the filter by clicking on the Filter icon at the top of the Bar Chart. Then hover the Audio slice again.
        """ 
        active_chart.click_chart_menu_bar_items(window_id='MAINTABLE_wmenu0', item_index=8)
         
        """ 
        Step 05.1: Expect to see the original Charts re-displayed.
        """ 
        "---a. Bar chart1---"
        active_chart.wait_for_number_of_element(element_css="#"+barchart_parent_css+" rect[class*='riser!'][class*='mbar!']", expected_number=25, time_out=MEDIUM_WAIT_TIME)
        expected_x_axis_title_list=['Country : Product Type']
        active_chart.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#'+barchart_parent_css, msg="Step 05.1: Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity']
        active_chart.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css='#'+barchart_parent_css, msg="Step 05.2: Verify y_axis title at runtime")
        expected_x_axis_label_list=['Canada/Audio', 'Canada/Ca...', 'Canada/Ca...', 'Canada/Office', 'Canada/Video', 'France/Audio', 'France/Ca...', 'France/Ca...', 'France/Office']
        active_chart.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css='#'+barchart_parent_css, xyz_axis_label_length=8, msg='Step 05.3')
        active_chart.verify_y_axis_label_in_run_window(['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K'], parent_css='#'+barchart_parent_css, msg='Step 05.4')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class^='riser!s0!g0!mbar!']", 'cerulean_blue', parent_css='#'+barchart_parent_css, msg='Step 05.5')
        active_chart.verify_chart_title('Quantity by Country, Product Type', msg='Step 05.6', parent_css='#'+barchart_parent_css)
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 05.7', parent_css='#MAINTABLE_wmenu0')
        chart_obj.verify_number_of_chart_segment(barchart_parent_css, 25, msg='Step 05.8: Verify number of bar risers', custom_css="[class*='riser!'][class*='mbar!']")
         
        "---b. Pie chart1---"
        active_chart.wait_for_number_of_element(element_css="#"+piechart1_parent_css+" path[class*='riser!'][class*='mwedge!']", expected_number=5, time_out=MEDIUM_WAIT_TIME)
        expected_x_axis_title_list=['Quantity']
        active_chart.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#'+piechart1_parent_css, x_or_y_axis_title_css="text[class*='pieLabel!']", msg="Step 05.9: Verify Pie chart1 title at runtime")
        expected_x_axis_label_list=['11%', '4%', '5%', '4%', '75%']
        active_chart.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css='#'+piechart1_parent_css, xyz_axis_label_css="text[class*='dataLabels!']", msg='Step 05.10')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class^='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css='#'+piechart1_parent_css, msg='Step 05.11')
        active_chart.verify_chart_title('Quantity by Country,', msg='Step 05.12', parent_css='#'+piechart1_parent_css)
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 05.13', parent_css='#MAINTABLE_wmenu1')
        expected_legend_list=['Canada', 'France', 'Germany', 'Spain', 'United States']
        active_chart.verify_legends_in_run_window(expected_legend_list, parent_css='#'+piechart1_parent_css, msg='Step 05.14: Verify legends in pie chart1')
        chart_obj.verify_number_of_chart_segment(piechart1_parent_css, 5, msg='Step 05.15: Verify number of bar risers', custom_css="[class*='riser!'][class*='mwedge!']")
         
        "---c. Pie chart2---"
        expected_x_axis_title_list=['Quantity']
        active_chart.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#'+piechart2_parent_css, x_or_y_axis_title_css="text[class*='pieLabel!']", msg="Step 05.16: Verify Pie chart1 title at runtime")
        expected_x_axis_label_list=['38%', '16%', '17%', '11%', '18%']
        active_chart.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css='#'+piechart2_parent_css, xyz_axis_label_css="text[class*='dataLabels!']", msg='Step 05.17')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class^='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css='#'+piechart2_parent_css, msg='Step 05.18')
        active_chart.verify_chart_title('Quantity by Product Type,', msg='Step 05.19', parent_css='#'+piechart2_parent_css)
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 05.20', parent_css='#MAINTABLE_wmenu1')
        expected_legend_list=['Audio', 'Camcorders', 'Cameras', 'Office', 'Video']
        active_chart.verify_legends_in_run_window(expected_legend_list, parent_css='#'+piechart2_parent_css, msg='Step 05.21: Verify legends in pie chart2')
        chart_obj.verify_number_of_chart_segment(piechart2_parent_css, 5, msg='Step 05.22: Verify number of bar risers', custom_css="[class*='riser!'][class*='mwedge!']")
         
        """
        Step 05.2: Also expect to see the full value for Audio, now at 863K, the difference being the value for the United States
        """
        verify_tooltip(piechart2_parent_css, riser_css='riser!s0!g0!mwedge!', expected_tooltip_list=['Audio:863K (37.73%)'], msg='Step 05.22: Expect to see the full value for Audio, now at 863K.')
        time.sleep(5)
        
        """
        Step 06: Using the bottom left PIE, click the slick for Canada, then click the Exclude from Chart option.
        """
        source_element=utillobj.validate_and_get_webdriver_object("#MAINTABLE_wbody1 path[class^='riser!s0!g0!mwedge!']", 'Canada pie segment')
        utillobj.click_on_screen(source_element, coordinate_type='middle', click_type=0)
        chart_obj.select_lasso_filter(select_item='Exclude from Chart')
        
        """ 
        Step 06.1: Expect to see the following dashboard, with Canada removed from the Bar Chart and the bottom left PIE.
        """ 
        "---a. Bar chart1---"
        active_chart.wait_for_number_of_element(element_css="#"+barchart_parent_css+" rect[class*='riser!'][class*='mbar!']", expected_number=20, time_out=MEDIUM_WAIT_TIME)
        expected_x_axis_title_list=['Country : Product Type']
        active_chart.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#'+barchart_parent_css, msg="Step 06.1: Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity']
        active_chart.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css='#'+barchart_parent_css, msg="Step 06.2: Verify y_axis title at runtime")
        expected_x_axis_label_list=['France/Audio', 'France/Ca...', 'France/Ca...', 'France/Office', 'France/Video', 'Germany/A...', 'Germany/C...', 'Germany/C...', 'Germany/Of...']
        active_chart.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css='#'+barchart_parent_css, xyz_axis_label_length=8, msg='Step 06.3')
        active_chart.verify_y_axis_label_in_run_window(['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K'], parent_css='#'+barchart_parent_css, msg='Step 06.4')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class^='riser!s0!g0!mbar!']", 'cerulean_blue', parent_css='#'+barchart_parent_css, msg='Step 06.5')
        active_chart.verify_chart_title('Quantity by Country, Product Type', msg='Step 06.6', parent_css='#'+barchart_parent_css)
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 06.7', parent_css='#MAINTABLE_wmenu0')
        chart_obj.verify_number_of_chart_segment(barchart_parent_css, 20, msg='Step 06.8: Verify number of bar risers', custom_css="[class*='riser!'][class*='mbar!']")
        
        "---b. Pie chart1---"
        active_chart.wait_for_number_of_element(element_css="#"+piechart1_parent_css+" path[class*='riser!'][class*='mwedge!']", expected_number=4, time_out=MEDIUM_WAIT_TIME)
        expected_x_axis_title_list=['Quantity']
        active_chart.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#'+piechart1_parent_css, x_or_y_axis_title_css="text[class*='pieLabel!']", msg="Step 06.9: Verify Pie chart1 title at runtime")
        expected_x_axis_label_list=['5%', '6%', '5%', '84%']
        active_chart.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css='#'+piechart1_parent_css, xyz_axis_label_css="text[class*='dataLabels!']", msg='Step 06.10')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class^='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css='#'+piechart1_parent_css, msg='Step 06.11')
        active_chart.verify_chart_title('Quantity by Country,', msg='Step 06.12', parent_css='#'+piechart1_parent_css)
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 06.13', parent_css='#MAINTABLE_wmenu1')
        expected_legend_list=['France', 'Germany', 'Spain', 'United States']
        active_chart.verify_legends_in_run_window(expected_legend_list, parent_css='#'+piechart1_parent_css, msg='Step 06.14: Verify legends in pie chart1')
        chart_obj.verify_number_of_chart_segment(piechart1_parent_css, 4, msg='Step 06.15: Verify number of bar risers', custom_css="[class*='riser!'][class*='mwedge!']")
        
        "---c. Pie chart2---"
        active_chart.wait_for_number_of_element(element_css="#"+piechart2_parent_css+" path[class*='riser!'][class*='mwedge!']", expected_number=5, time_out=MEDIUM_WAIT_TIME)
        expected_x_axis_title_list=['Quantity']
        active_chart.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#'+piechart2_parent_css, x_or_y_axis_title_css="text[class*='pieLabel!']", msg="Step 06.16: Verify Pie chart1 title at runtime")
        expected_x_axis_label_list=['38%', '16%', '17%', '12%', '18%']
        active_chart.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css='#'+piechart2_parent_css, xyz_axis_label_css="text[class*='dataLabels!']", msg='Step 06.17')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class^='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css='#'+piechart2_parent_css, msg='Step 06.18')
        active_chart.verify_chart_title('Quantity by Product Type,', msg='Step 06.19', parent_css='#'+piechart2_parent_css)
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 06.20', parent_css='#MAINTABLE_wmenu1')
        expected_legend_list=['Audio', 'Camcorders', 'Cameras', 'Office', 'Video']
        active_chart.verify_legends_in_run_window(expected_legend_list, parent_css='#'+piechart2_parent_css, msg='Step 06.21: Verify legends in pie chart2')
        chart_obj.verify_number_of_chart_segment(piechart2_parent_css, 5, msg='Step 06.22: Verify number of bar risers', custom_css="[class*='riser!'][class*='mwedge!']")
        
        """
        Step 07: To prove that the bottom right PIE has also changed, hover the slice for Audio.
        Expect to see the filtered value of 765K appear.
        """
        verify_tooltip(piechart2_parent_css, riser_css='riser!s0!g0!mwedge!', expected_tooltip_list=['Audio:765K (37.71%)'], msg='Step 07: Expect to see the filtered value of 765K appear.')
        
        """ 
        Step 08: Remove the filter by clicking on the Filter icon for the bottom left PIE.
        Using the bottom right PIE, click the slice for Audio, then click the Exclude from Chart option.
        """ 
        active_chart.click_chart_menu_bar_items(window_id='MAINTABLE_wmenu1', item_index=8)
        active_chart.wait_for_number_of_element(element_css="#"+barchart_parent_css+" rect[class*='riser!'][class*='mbar!']", expected_number=25, time_out=MEDIUM_WAIT_TIME)
        source_element=utillobj.validate_and_get_webdriver_object("#MAINTABLE_wbody2 path[class^='riser!s0!g0!mwedge!']", 'Audio pie segment')
        utillobj.click_on_screen(source_element, coordinate_type='middle', click_type=0)
        chart_obj.select_lasso_filter(select_item='Exclude from Chart')
        
        """ 
        Step 08.1: Expect to see the following dashboard, with Audio for each Country removed from the Bar Chart and the slice for Audio from the bottom right PIE.
        """ 
        "---a. Bar chart1---"
        active_chart.wait_for_number_of_element(element_css="#"+barchart_parent_css+" rect[class*='riser!'][class*='mbar!']", expected_number=20, time_out=MEDIUM_WAIT_TIME)
        expected_x_axis_title_list=['Country : Product Type']
        active_chart.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#'+barchart_parent_css, msg="Step 08.1: Verify x_axis title at runtime")
        expected_y_axis_title_list=['Quantity']
        active_chart.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css='#'+barchart_parent_css, msg="Step 08.2: Verify y_axis title at runtime")
        expected_x_axis_label_list=['Canada/Ca...', 'Canada/Ca...', 'Canada/Office', 'Canada/Video', 'France/Ca...', 'France/Ca...', 'France/Office', 'France/Video', 'Germany/C...']
        active_chart.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css='#'+barchart_parent_css, xyz_axis_label_length=8, msg='Step 08.3')
        active_chart.verify_y_axis_label_in_run_window(['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K'], parent_css='#'+barchart_parent_css, msg='Step 08.4')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class^='riser!s0!g0!mbar!']", 'cerulean_blue', parent_css='#'+barchart_parent_css, msg='Step 08.5')
        active_chart.verify_chart_title('Quantity by Country, Product Type', msg='Step 08.6', parent_css='#'+barchart_parent_css)
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 08.7', parent_css='#MAINTABLE_wmenu0')
        chart_obj.verify_number_of_chart_segment(barchart_parent_css, 20, msg='Step 08.8: Verify number of bar risers', custom_css="[class*='riser!'][class*='mbar!']")
        
        "---b. Pie chart1---"
        active_chart.wait_for_number_of_element(element_css="#"+piechart1_parent_css+" path[class*='riser!'][class*='mwedge!']", expected_number=5, time_out=MEDIUM_WAIT_TIME)
        expected_x_axis_title_list=['Quantity']
        active_chart.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#'+piechart1_parent_css, x_or_y_axis_title_css="text[class*='pieLabel!']", msg="Step 08.9: Verify Pie chart1 title at runtime")
        expected_x_axis_label_list=['11%', '4%', '5%', '5%', '75%']
        active_chart.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css='#'+piechart1_parent_css, xyz_axis_label_css="text[class*='dataLabels!']", msg='Step 08.10')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class^='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css='#'+piechart1_parent_css, msg='Step 08.11')
        active_chart.verify_chart_title('Quantity by Country,', msg='Step 08.12', parent_css='#'+piechart1_parent_css)
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 08.13', parent_css='#MAINTABLE_wmenu1')
        expected_legend_list=['Canada', 'France', 'Germany', 'Spain', 'United States']
        active_chart.verify_legends_in_run_window(expected_legend_list, parent_css='#'+piechart1_parent_css, msg='Step 08.14: Verify legends in pie chart1')
        chart_obj.verify_number_of_chart_segment(piechart1_parent_css, 5, msg='Step 08.15: Verify number of bar risers', custom_css="[class*='riser!'][class*='mwedge!']")
        
        "---c. Pie chart2---"
        active_chart.wait_for_number_of_element(element_css="#"+piechart2_parent_css+" path[class*='riser!'][class*='mwedge!']", expected_number=4, time_out=MEDIUM_WAIT_TIME)
        expected_x_axis_title_list=['Quantity']
        active_chart.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css='#'+piechart2_parent_css, x_or_y_axis_title_css="text[class*='pieLabel!']", msg="Step 08.16: Verify Pie chart1 title at runtime")
        expected_x_axis_label_list=['26%', '27%', '18%', '29%']
        active_chart.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css='#'+piechart2_parent_css, xyz_axis_label_css="text[class*='dataLabels!']", msg='Step 08.17')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class^='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css='#'+piechart2_parent_css, msg='Step 08.18')
        active_chart.verify_chart_title('Quantity by Product Type,', msg='Step 08.19', parent_css='#'+piechart2_parent_css)
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 08.20', parent_css='#MAINTABLE_wmenu1')
        expected_legend_list=['Camcorders', 'Cameras', 'Office', 'Video']
        active_chart.verify_legends_in_run_window(expected_legend_list, parent_css='#'+piechart2_parent_css, msg='Step 08.21: Verify legends in pie chart2')
        chart_obj.verify_number_of_chart_segment(piechart2_parent_css, 4, msg='Step 08.22: Verify number of bar risers', custom_css="[class*='riser!'][class*='mwedge!']")
        
        """
        Step 09: Using the bottom left PIE, hover the slice for Spain.
        Expect to see the filtered value of 65,189 appear.
        """
        verify_tooltip(piechart1_parent_css, riser_css='riser!s3!g0!mwedge!', expected_tooltip_list=['Spain:65,189 (4.58%)'], msg='Step 09: Expect to see the filtered value of 65,189 appear.', element_location='middle_right', xoffset=-5)
        
        """ 
        Step 10: Remove the filter by clicking on the Filter icon for the bottom right PIE.
        Using the bottom left PIE, again hover the slice for Spain.
        """ 
        active_chart.click_chart_menu_bar_items(window_id='MAINTABLE_wmenu1', item_index=8)
        active_chart.wait_for_number_of_element(element_css="#"+barchart_parent_css+" rect[class*='riser!'][class*='mbar!']", expected_number=25, time_out=MEDIUM_WAIT_TIME)
        
        """
        Step 10.1: Expect to see the full volume for Spain at 101K.
        """
        verify_tooltip(piechart1_parent_css, riser_css='riser!s3!g0!mwedge!', expected_tooltip_list=['Spain:101K (4.43%)'], msg='Step 10.1: Expect to see the full volume for Spain at 101K.')
        
if __name__ == "__main__":
    unittest.main()