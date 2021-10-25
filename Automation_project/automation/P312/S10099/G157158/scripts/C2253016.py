'''
Created on Feb 21, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10099
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253016
Test_Case Name : IA-4688:Vis: Drilldown and Drillup on a vis with filter NE shows empty chart
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.lib import core_utility, global_variables
from common.pages import visualization_resultarea

class C2253016_TestClass(BaseTestCase):

    def test_C2253016(self):
        
        Test_Case_ID = "C2253016"
        metadata_browser_css = "#iaMetaDataBrowser"        
        total_no_of_riser_css = "#MAINTABLE_1 rect[class^='riser']"  
        wait_time_in_sec = 120
        yaxis_title_css = "#MAINTABLE_wbody1_f text[class='yaxis-title']"
        xaxis_title_css = "#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']"
        Filter_dialog_ok_button_css = "#avFilterOkBtn"
        
        visual = visualization.Visualization(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        viz_resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,riser_color_css,total_risers,tooltip, step_num):
            visual.verify_x_axis_title(x_title, msg='Step' + step_num + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step' + step_num + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_1 rect', 1, total_risers, msg='Step' + step_num + '.5:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("[class*='"+riser_color_css+"']", 'bar_blue',  msg='Step' + step_num + '.6:'+' Verify riser color')
            visual.verify_tooltip(riser,tooltip,msg='Step' + step_num + '.7:'+' Verify riser tooltip')
        
        def select_tooltip(riser_css, menu_path, parent_css='MAINTABLE_wbody1', initial_move_xy_dict=None, element_location='middle', xoffset=0, yoffset=0, use_marker_enable=False, move_to_tooltip=False):
            tooltip_elem=self.driver.find_element_by_css_selector("#"+parent_css+" [class*='"+riser_css+"']")
            viz_resobj.move_mouse_to_chart_component(tooltip_elem, initial_move_xy_dict=initial_move_xy_dict, element_location=element_location, xoffset=xoffset, yoffset=yoffset, use_marker_enable=use_marker_enable, move_to_tooltip=move_to_tooltip)
            tooltip_menu_list=menu_path.split('->')
            tooltip_css= "[id*='tdgchart-tooltip']:not([style*='hidden']) span.tdgchart-tooltip-label"
            elems=self.driver.find_elements_by_css_selector(tooltip_css)
            tooltip_item_to_be_selected=[elem for elem in elems if elem.text.strip()==tooltip_menu_list[0]][0]
            if global_variables.Global_variables.browser_name=='firefox':
                tooltip_item_to_be_selected.click()
            else:
                core_utilobj.left_click(tooltip_item_to_be_selected, element_location='middle_left', xoffset=10)
            
        """
        Step1: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        visual.wait_for_number_of_element(metadata_browser_css, 1)
        
        """
        Step02: Double click "Revenue" and "Customer Country".
        """
        visual.double_click_on_datetree_item('Revenue', 1)
        visual.wait_for_visible_text(yaxis_title_css, "Revenue", 45)
        visual.double_click_on_datetree_item('Customer,Country', 1)
        visual.wait_for_visible_text(xaxis_title_css, "CustomerCountry", 45)
        
        """
        Step03: Verify label values
        Step04: Verify query pane
        Step05: Verify first and last 3 bar riser values (CustomerCountry:Revenue)
        """
        no_of_riser=42
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec) 
        visual.verify_field_listed_under_querytree('Vertical Axis', 'Revenue', 1, "Step04.1: Verify Revenue in Query Pane")  
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Customer,Country', 1, "Step04.2: Verify Customer Country in Query Pane") 
         
        """
        Argentina:$5,291,947.92
        Australia:$2,562,553.72
        Austria:$47,386,456.91
        Turkey:$799,730.03
        United Kingdom:$55,730,572.66
        United States:$333,514,945.66
        """
        x_title=['Customer Country']
        y_title=['Revenue']
        expected_xaxis_labels=['Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Canada', 'Chile']
        expected_yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        Argentina_riser="riser!s0!g0!mbar"
        Argentina_tooltip=['Customer Country:Argentina', 'Revenue:$5,291,947.92', 'Filter Chart', 'Exclude from Chart', 'Drill up to Customer Business Sub Region', 'Drill down to Customer State Province']
        step_num='05.1'
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels, Argentina_riser, Argentina_riser, no_of_riser,Argentina_tooltip, step_num)        
        Austria_riser="riser!s0!g2!mbar"
        Austria_tooltip=['Customer Country:Austria', 'Revenue:$47,386,456.91', 'Filter Chart', 'Exclude from Chart', 'Drill up to Customer Business Sub Region', 'Drill down to Customer State Province']
        visual.verify_tooltip(Austria_riser,Austria_tooltip,msg='Step05.3" Verify Austria_riser tooltip')
        
        """
        Step06: Add Customer Country to filters and set Not Equal to United States.
        Step07: Verify query added to filter pane
        Step08: verify United States value not displayed in preview output
        """
        visual.drag_and_drop_from_data_tree_to_filter('Customer,Country', 1)
#         visual.right_click_on_datetree_item('Customer,Country', 1, 'Filter')        
        visual.wait_for_number_of_element(Filter_dialog_ok_button_css, 1, wait_time_in_sec)
        visual.select_filter_operator_combobox('alpha','Not equal to')
        select_filter_value_list=['[All]','United States']
        visual.select_filter_field_values(select_filter_value_list,True)
        filter_text_css=".arFilterButton span"
        visual.wait_for_visible_text(filter_text_css, 'Customer,Country')
         
        visual.verify_field_in_filterbox('Customer,Country', 1, "Step07: Verify query added to filter pane")
         
        no_of_riser=41
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        visual.verify_number_of_risers('#MAINTABLE_1 rect', 1, no_of_riser, msg='Step08.1:'+' Verify number of risers are 41')
        United_Kindom_riser="riser!s0!g40!mbar"
        United_Kindom_tooltip=['Customer Country:United Kingdom', 'Revenue:$55,730,572.66', 'Filter Chart', 'Exclude from Chart', 'Drill up to Customer Business Sub Region', 'Drill down to Customer State Province']
        visual.verify_tooltip(United_Kindom_riser,United_Kindom_tooltip,msg='Step08.2: Verify last riser tooltip is United Kingdom')
        
        """
        Step09: Hover on Italy and select Drilldown.
        """
        no_of_riser=41
        main_pane_css = "#MAINTABLE_wbody1"
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        Italy_riser_css='riser!s0!g20!mbar'
        main_pane_elem = self.driver.find_element_by_css_selector(main_pane_css)
        core_utilobj.python_left_click(main_pane_elem, element_location='top_left', xoffset=9, yoffset=9)
        select_tooltip(Italy_riser_css, 'Drill down to Customer State Province')
        
        """
        Step10: Verify Customer country changed to Customer State Province in horizontal axis
        Step11: Verify Italy 'State province (Abruzzi, Calabria, Umbria and Veneto) : revenue' values
        Abruzzi:$69,411.51
        Calabria:$72,365.59
        Umbria:$20,919.32
        Veneto:$478,250.95       
        """
        no_of_riser=18
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        x_title=['Customer State Province']
        y_title=['Revenue']
        expected_xaxis_labels=['Abruzzi', 'Calabria', 'Campania', 'Emilia-Romagna']
        expected_yaxis_labels=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M', '40M', '45M']
        Abruzzi_riser_css="riser!s0!g0!mbar"
        Abruzzi_riser_color_css="tinyPlaceholder!s0!g0!mbar"
        Abruzzi_tooltip=['Customer State Province:Abruzzi', 'Revenue:$69,411.51', 'Filter Chart', 'Exclude from Chart', 'Drill up to Customer Country', 'Drill down to Customer City']
        step_num='11'
        def verify_bar(x_title,y_title,x_label, y_label,riser,total_risers,tooltip, step_num):
            visual.verify_x_axis_title(x_title, msg='Step' + step_num + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step' + step_num + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_1 rect', 1, total_risers, msg='Step' + step_num + '.5:'+' Verify number of risers')
            visual.verify_tooltip(riser,tooltip,msg='Step' + step_num + '.7:'+' Verify riser tooltip')
        verify_bar(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Abruzzi_riser_css,no_of_riser,Abruzzi_tooltip, step_num)
        
        """
        Step12: Hover on "Lazio" and select drillup
        Step13: verify output in preview
        """
        Lazio_riser_css="#MAINTABLE_1 rect[class^='riser!s0!g5!mbar']"
        visual.wait_for_number_of_element(Lazio_riser_css, 1)
        Lazio_riser_css='riser!s0!g5!mbar'
        visual.select_tooltip(Lazio_riser_css, 'Drill up to Customer Country', move_to_tooltip=True)
        
        no_of_riser=42
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        x_title=['Customer Country']
        y_title=['Revenue']
        expected_xaxis_labels=['Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Canada', 'Chile']
        expected_yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        Argentina_riser="riser!s0!g0!mbar"
        Argentina_tooltip=['Customer Country:Argentina', 'Revenue:$5,291,947.92', 'Filter Chart', 'Exclude from Chart', 'Drill up to Customer Business Sub Region', 'Drill down to Customer State Province']
        step_num='13'
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Argentina_riser,Argentina_riser,no_of_riser,Argentina_tooltip, step_num)        
        
        """
        Step14: Click Run in the toolbar
        Step15: Verify output
        Step16: Close the output window
        """   
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        step_num='15'
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Argentina_riser,Argentina_riser,no_of_riser,Argentina_tooltip, step_num)        
        
        visual.take_run_window_snapshot(Test_Case_ID, '15')
        visual.switch_to_previous_window()
                 
        """
        Step17: Click "Save" in the toolbar > Type C2141213 > Click "Save" in the Save As dialog
        Step18: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        visual.save_as_visualization_from_menubar(Test_Case_ID)
#         visual.logout_visualization_using_api()

if __name__ == '__main__':
    unittest.main()        
