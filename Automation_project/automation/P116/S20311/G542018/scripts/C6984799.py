'''
Created on Dec 21, 2018

@author: Vpriya
Testcase ID :  http://172.19.2.180/testrail/index.php?/cases/view/6984799
Testcase Name : Verify a chart shows correct filtered output once filter via lasso applied - Area Chart
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.wftools import active_chart, chart
from common.wftools import visualization

class C6984799_TestClass(BaseTestCase):

    def test_C6984799(self):
        """
            TESTCASE Functions Object
        """
        
        utillobj = utillity.UtillityMethods(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        visual_obj=visualization.Visualization(self.driver)
        preview_parent_css="TableChart_1"
        preview_yaxis_title_css="#"+preview_parent_css+" [class='yaxis-title']"
        short_time=250
        run_exp_yaxis_label_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        run_exp_xaxis_label_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        run_exp_xaxis_title_list=['Product']
        run_exp_column_label=['Category', 'Coffee', 'Food', 'Gifts']
        source_elem_css="circle[class*='marker!s0!g1!mmarker!r0!c0!']"
        Target_elem_css="circle[class*='marker!s0!g5!mmarker!r0!c0!']"
        expected_tooltip_list=['2 points', 'Filter Chart', 'Exclude from Chart']
        expresso_css='marker!s0!g1!mmarker!r0!c0!'
        expresso_tooltip_list=['Category:Coffee', 'Product:Espresso', 'Unit Sales:308986', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        coffee_css="circle[class*='marker!s0!g3!mmarker!r0!c2!']"
        mug_css="circle[class*='marker!s0!g7!mmarker!r0!c2!']"
        filter_css="#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']"

        
        """
            Step 01 : Log in to WebFOCUS
            http://machine:port/{alias}
            Step 02 : Execute following URL to create Chart
            http://machine:port/{alias}/ia?tool=Chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS20311%2F
        """
        active_chart_obj.invoke_chart_tool_using_api('ibisamp/ggsales')
        
        """
            Step 03 : Change Output format to Active Reports
        """
        chart_obj.change_output_format_type('active_report')
        
        """
            Step 04 : From the Format tab, select Area Chart
        """
        chart_obj.select_ia_ribbon_item('Format', 'Area')
        
        """
            Step 05 : Select data from the left pane (Dimensions and Measures)
            Category - Columns
            Product - Horizontal Axis
            Unit Sales - Vertical Axis
        """
        field_name1='Category'
        field_name2='Product'
        field_name3='Unit Sales'
        preview_expected_column_header_label=['Category : Product', 'Coffee']
        chart_obj.drag_field_from_data_tree_to_query_pane(field_name1, 1, 'Columns', 1)
        
        css1="#"+preview_parent_css+" text[class='colHeader-label!']"
        chart_obj.wait_for_visible_text(css1, field_name1,short_time)
        
        chart_obj.drag_field_from_data_tree_to_query_pane(field_name2, 1, 'Horizontal Axis', 1)
        chart_obj.wait_for_visible_text(css1, 'Category : Product', short_time)
        
        chart_obj.drag_field_from_data_tree_to_query_pane(field_name3, 1, 'Vertical Axis', 1)
        chart_obj.wait_for_visible_text(preview_yaxis_title_css, field_name3, short_time)
        
        """ See corresponding data is displayed in the Live Preview pane."""
        
        exp_yaxis_title_list=['Unit Sales','Unit Sales', 'Unit Sales']
        preview_expected_label_list=['Capuccino', 'Espresso']
        preview_expected_yaxis_label_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        
        chart_obj.verify_y_axis_title_in_preview(exp_yaxis_title_list, msg="Step 04:01:")
        chart_obj.verify_column_label(preview_expected_column_header_label, "#"+preview_parent_css, msg='Step 04:02')
        chart_obj.verify_x_axis_label_in_preview(preview_expected_label_list, msg="Step 04:03")
        chart_obj.verify_y_axis_label_in_preview(preview_expected_yaxis_label_list, msg="Step 04:04:")
        """
        Step 6:Run the Area Chart.
        Verify Active Chart 'Unit Sales BY Category, Product' is displayed on canvas with selected data.
        """
        chart_obj.run_chart_from_toptoolbar()
        utillobj.switch_to_frame(pause=2)
        run_parent_css="MAINTABLE_wbody0"
        run_exp_yaxis_title="#"+run_parent_css+" .chartPanel text[class*='yaxis-title']"
        chart_obj.wait_for_visible_text(run_exp_yaxis_title, field_name3)
        
        
        expected_toolbar_menu_list=['More Options','Advanced Chart','Original Chart', 'Aggregation', 'Sum']
        run_exp_chart_title="Unit Sales BY Category, Product"
        active_menubar_css="#MAINTABLE_wmenu0"
        
        chart_obj.verify_y_axis_title_in_run_window(exp_yaxis_title_list, parent_css="#"+run_parent_css, msg="Step 05:01")
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+run_parent_css, msg="Step 05:02")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+run_parent_css, msg="Step 05:03")
        chart_obj.verify_x_axis_title_in_run_window(run_exp_xaxis_title_list, parent_css="#"+run_parent_css, msg="Step 05:04")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 05:06", parent_css=active_menubar_css)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 05:07", parent_css="#MAINTABLE_wbody0_ft")
        chart_obj.verify_column_label(run_exp_column_label, "#"+run_parent_css, msg='Step 05:08')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 [class*='marker!s0!g5!mmarker!r0!c0!']", 1, 50)
        
        
        """
            Step 07 : Left-click and drag a box around Capuccino and Espresso points in the COFFEE Category.
                    Verify context menu displays:
                    2 points
                    Filter Chart
                    Exclude from Chart
        """
        source_obj=utillobj.validate_and_get_webdriver_object(source_elem_css,"Source elem")
        target_obj=utillobj.validate_and_get_webdriver_object(Target_elem_css,"Target elem")
        visual_obj.create_marker_lasso(source_obj,target_obj,)
        visual_obj.verify_lasso_tooltip(expected_tooltip_list,"Step7.1 verify lasso context Menu")
    
        """
            Step 08 :Click Filter Chart option.
            Verify based on area selection, filtered area is displayed.
            Filet icon is also displayed in the active tool bar.
        """
        visual_obj.select_lasso_tooltip("Filter Chart")
        utillobj.verify_object_visible(filter_css,True,"Step8")
    
        """
            Step 09 :Hover on the Espresso point .
            Verify context menu displays:
            Category: Coffee
            Product: Espresso
            Unit Sales: 308,986
            Filter Chart
            Exclude from Chart
            Remove Filter
            
        """
        chart_obj.verify_tooltip_in_run_window(expresso_css, expresso_tooltip_list,"Step9.1",'#MAINTABLE_wbodyMain0', element_location='bottom_middle',use_marker_enable=True)
       
        
        """
        Step 10 :Click Remove Filter option.
        Verify original chart appears in the output.
        Make sure filter icon is not present.
        """
        chart_obj.select_tooltip_in_run_window('marker!s0!g1!mmarker!r0!c0!', 'Remove Filter', '#MAINTABLE_wbodyMain0', use_marker_enable=True)
        chart_obj.verify_y_axis_title_in_run_window(exp_yaxis_title_list, parent_css="#"+run_parent_css, msg="Step 05:01")
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+run_parent_css, msg="Step 05:02")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+run_parent_css, msg="Step 05:03")
        chart_obj.verify_x_axis_title_in_run_window(run_exp_xaxis_title_list, parent_css="#"+run_parent_css, msg="Step 05:04")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 05:06", parent_css=active_menubar_css)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 05:07", parent_css="#MAINTABLE_wbody0_ft")
        chart_obj.verify_column_label(run_exp_column_label, "#"+run_parent_css, msg='Step 05:08')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 [class*='marker!s0!g5!mmarker!r0!c0!']", 1, 50)
        utillobj.verify_object_visible(filter_css, False,"Step 10.1 object is not visible")
        
        """
        Step 11 :Left-click and drag a box around the Coffee Pot and Mug points in the GIFTS Category.
        Verify context menu displays:
        2 points
        Filter Chart
        Exclude from Chart
        """
        cofee_pot_elem=utillobj.validate_and_get_webdriver_object(coffee_css,'Cofee_css_source')
        mug_pot_elem=utillobj.validate_and_get_webdriver_object(mug_css,'Mug_css')
        visual_obj.create_marker_lasso(cofee_pot_elem,mug_pot_elem)
        visual_obj.verify_lasso_tooltip(expected_tooltip_list,"Step11.1 verify lasso context Menu")
        """
        Step 12 :Click Exclude from Chart option.
        Verify Coffee Pot and Mug points in the GIFTS Category are excluded from the chart and filter icon appears on the Active tool bar.
        """
        visual_obj.select_lasso_tooltip("Exclude from Chart")
        utillobj.verify_object_visible(filter_css,True,"Step8")
       
        """
        Step 13:Click remove filter icon from the active tool bar.
        Verify original chart appears with FOOD and GIFTS categories restored with all points. 
        Also verify that the 'Remove filter' is not present.
        """
        active_chart_obj.click_chart_menu_bar_items('MAINTABLE_wmenu0',4)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0_ft",1,45)
        utillobj.verify_object_visible(filter_css,False,"Step8")
        
        """
            Step 14 : Dismiss the window and logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()