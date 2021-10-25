'''
Created on Feb 08, 2018

@author: Sowmiya
TestSuite Name : 8202 New Features and product changes for existing functionality 
TestSuite ID : http://172.19.2.180/testrail/index.php?/suites/view/10664&group_by=cases:section_id&group_order=asc&group_id=173783
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2349047
TestCase Name: Group added to drill hierarchy when not in query
'''
import unittest
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, core_metadata

class C2253024_TestClass(BaseTestCase):

    def test_C2253024(self):
        
        """
        TESTCASE VARIABLES
        """
        position=1
        Test_Case_ID = 'C2253024'
        
        """
        Class & Objects
        """
        visual = visualization.Visualization(self.driver)
        core_meta = core_metadata.CoreMetaData(self.driver)
        resultobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        
        
        def verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, total_risers, stepno):        
            visual.verify_x_axis_title(x_axis_title, msg='Step '+stepno+'.01')
            visual.verify_y_axis_title(y_axis_title, msg='Step '+stepno+'.02')
            visual.verify_x_axis_label(x_axis_label, xyz_axis_label_length=10, msg='Step '+stepno+'.03')
            visual.verify_y_axis_label(y_axis_label, msg='Step '+stepno+'.04')
            visual.verify_number_of_risers("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 1, total_risers, msg='Step '+stepno+'.05')
            visual.verify_chart_color_using_get_css_property("rect[class='"+riser_css+"']", color_name, msg='Step '+stepno+'.06')
            visual.verify_tooltip(riser_css, tooltip_list, msg='Step '+stepno+'.07 : Verify tooltip')
    
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """      
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02 : Double click "Quantity,Sold" & "Store,Business,Region".
        """
        visual.double_click_on_datetree_item('Quantity,Sold', position)
        visual.wait_for_number_of_element("#TableChart_1 rect[class^='riser']", 1)
        core_meta.collapse_data_field_section('Filters and Variables')
        visual.double_click_on_datetree_item('Store,Business,Region', position)
        visual.wait_for_number_of_element("#TableChart_1 rect[class^='riser']", 4)
        
        """
        Step 03 : Verify label values
        Step 04 : Verify bar riser values
        """
        x_axis_title=['Store Business Region']
        y_axis_title=['Quantity Sold']
        x_axis_label=['EMEA', 'North America', 'Oceania', 'South America']
        y_axis_label=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        color_name='bar_blue'
        tooltip_list=['Store Business Region:EMEA', 'Quantity Sold:1,404,540', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store Business Sub Region']
        riser_css='riser!s0!g0!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, 4, '03')
        
        """
        Step 05 : Drag "Store,Business,Region" to Color bucket
        """
        visual.drag_field_from_data_tree_to_query_pane('Store,Business,Region', position, 'Color' ,position)
       
        """
        Step 06 : Verify query pane
        """
        visual.verify_field_listed_under_querytree('Color BY', 'Store,Business,Region', position, msg='Step 06.01')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Store,Business,Region', position, msg='Step 06.02')
        visual.verify_field_listed_under_querytree('Vertical Axis', 'Quantity,Sold', position, msg='Step 06.03')
        
        """
        Step 07 : Hover over a column(EMEA) and select Drill down on the top "Store,Business,Sub Region"
        """
        #visual.select_tooltip('riser!s0!g0!mbar!', 'Drill down to->Store Business Sub Region')
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', 'riser!s0!g0!mbar!', 'Drill down to->Store Business Sub Region')
        visual.wait_for_number_of_element("#TableChart_1 rect[class^='riser']", 3)

        """
        Step 08 : Verify query added to filter pane
        """
        visual.verify_field_in_filterbox('BUSINESS_REGION and BUSINESS_REGION', position, msg='Step 08.01 : Verify filter tree')
        
        """
        Step 09 : Verify filtered bar values (preview shows one column for region and stacked sub regions.)
        """
        x_axis_title=['Store Business Region']
        y_axis_title=['Quantity Sold']
        x_axis_label=['EMEA']
        y_axis_label=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        color_name='dark_green'
        tooltip_list=['Store Business Region:EMEA', 'Quantity Sold:1,317,153', 'Store Business Sub Region:Europe', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Region', 'Drill down to']
        riser_css='riser!s2!g0!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, 3, '09')
         
        expected_legend_list=['Store Business Sub Region', 'Africa', 'Asia', 'Europe']
        visual.verify_legends(expected_legend_list,"#TableChart_1", msg='Step 09.08 : ')
        
        """
        Step 10 : Right click filter > Delete.
        """
        visual.right_click_on_field_in_filterbox('BUSINESS_REGION and BUSINESS_REGION', position, 'Delete')
        visual.wait_for_number_of_element("#TableChart_1 rect[class^='riser']", 14)
        
        """
        Step 11 : Verify no queries display in filter pane
        """
        visual.verify_field_in_filterbox(None, position)
       
        """
        Step 12 : Right click "Store,Business,Sub Region" in Color bucket > Delete.
        """
        
        visual.right_click_on_field_under_query_tree('Store,Business,Sub Region', position, 'Delete')
        visual.wait_for_number_of_element("#TableChart_1 rect[class^='riser']", 4)
        
        """
        Step 13 : Verify query pane (Subregion should not display)
        """
        expcted_items =['Bar Stacked1', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Quantity,Sold', 'Horizontal Axis', 'Store,Business,Region', 'Marker', 'Color BY', 'Size', 'Tooltip']
        visual.verify_all_fields_in_query_pane(expcted_items, msg='Step 13.00 : Verify sub region not in query pane')
        
        """
        Step 14 : Drag "Store,Business,Region" to Color bucket.
        """
        visual.drag_field_from_data_tree_to_query_pane('Store,Business,Region', position, 'Color BY')
        visual.wait_for_number_of_element("#TableChart_1 rect[class^='riser']", 4)
        
        """
        Step 15 : Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element("#MAINTABLE_1 rect[class^='riser']", 4)
        
        """
        Step 16 : Verify output
        """
        x_axis_title=['Store Business Region']
        y_axis_title=['Quantity Sold']
        x_axis_label=['EMEA', 'North America', 'Oceania', 'South America']
        y_axis_label=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        color_name='bar_blue'
        riser_css='riser!s0!g0!mbar!'
        visual.verify_x_axis_title(x_axis_title, msg='Step 16.01')
        visual.verify_y_axis_title(y_axis_title, msg='Step 16.02')
        visual.verify_x_axis_label(x_axis_label, xyz_axis_label_length=10, msg='Step 16.03')
        visual.verify_y_axis_label(y_axis_label, msg='Step 16.04')
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 1, 4, msg='Step 16.05')
        visual.verify_chart_color_using_get_css_property("rect[class='"+riser_css+"']", color_name, msg='Step 16.06')
        expected_legend_list=['Store Business Region', 'EMEA', 'North America', 'Oceania', 'South America']
        visual.verify_legends(expected_legend_list,"#MAINTABLE_1", msg='Step 16.07 : ')     
        
        """
        Step 17 : Close the output window
        """
        visual.switch_to_previous_window()
        
        """
        Step 18 : Click "Save" in the toolbar > Type C2141377 > Click "Save" in the Save As dialog
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 19 : Logout of the IA API using the following URL. 
                    http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
if __name__ == '__main__':
    unittest.main() 