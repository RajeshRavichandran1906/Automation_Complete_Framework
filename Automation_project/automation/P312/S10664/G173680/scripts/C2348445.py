'''
Created on Jan 12, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348445
Test_Case Name : If bin field added to Color in BLA it is treated as the BY
Preconditions : Continue from C2348444
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea
from common.pages.ia_resultarea import IA_Resultarea
from common.wftools.visualization import Visualization

class C2348445_TestClass(BaseTestCase):

    def test_C2348445(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2348445'
        
        """   
            CLASS OBJECTS 
        """
        visual=Visualization(self.driver)
        ia_rsultobj= IA_Resultarea(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
    
        """
            Step 01 : Restore C2343111.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348444.fex
        """
        visual.edit_visualization_using_api('C2348445_Base')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f svg text[class='yaxis-title']", 'QuantitySold', 90)
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 28, visual.home_page_long_timesleep)
        
        """
            Step 01.1 : Verify preview
        """
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','columns','QUANTITY_SOLD_BIN_1 : Product Category', ['1', '2', '3', '4'], "Step 1.1: Verify Column header",1)
#         visual.verify_x_axis_title(['Product Category', 'Product Category', 'Product Category', 'Product Category'], msg='Step 01.1')
        visual.verify_y_axis_title(['Quantity Sold'], msg='Step 01.2')
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Product...', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Product...', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Product...', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Product...']
        expected_yaxis_labels=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        visual.verify_x_axis_label(expected_xaxis_labels, xyz_axis_label_length=12, msg='Step 01.3')
        visual.verify_y_axis_label(expected_yaxis_labels, msg='Step 01.4')
        visual.verify_column_label(['QUANTITY_SOLD_BIN_1 : Product Category', '1', '2', '3', '4'], msg='Step 01.5')
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f svg rect[class^='riser']", 4, 7, msg='Step 01.6')
#         visual.take_preview_snapshot(Test_Case_ID, '01')
        
        """
            Step 02 : Drag and drop "QUANTITY_SOLD_BIN_1" bin from Columns to color bucket
        """
        visual.drag_field_within_query_pane('QUANTITY_SOLD_BIN_1', 'Color')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f .legend text[class='legend-title']", 'QUANTITY_SOLD_BIN_1', 40)
        
        """
            Step 03 : Verify bin added to color bucket and preview updated
            A color legend is added with values from 1 to 4
        """
        visual.verify_x_axis_title(['Product Category'], msg='Step 03.1')
        visual.verify_y_axis_title(['Quantity Sold'], msg='Step 03.2')
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        visual.verify_x_axis_label(expected_xaxis_labels, msg='Step 03.3')
        visual.verify_y_axis_label(expected_yaxis_labels, msg='Step 03.4')
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f svg rect[class^='riser']", 4, 7, msg='Step 03.5')
        visual.verify_legends(['QUANTITY_SOLD_BIN_1', '1', '2', '3', '4'], msg='Step 03.6')
        visual.verify_chart_color_using_get_css_property("rect[class='riser!s1!g0!mbar!']", 'pale_green',  msg='Step 03.7 ')
        visual.verify_chart_color_using_get_css_property("rect[class='riser!s2!g0!mbar!']", 'med_green',  msg='Step 03.8 ')
#         visual.take_preview_snapshot(Test_Case_ID, '03')
        
        """
            Step 04 : Click view source icon to view fex code generated. "QUANTITY_SOLD_BIN_1" added as by field
            Step 05 : Close view source code window
        """
        expcted_syntax=["SUM WF_RETAIL_LITE.WF_RETAIL_SALES.QUANTITY_SOLD", "BY QUANTITY_SOLD_BIN_1", "BY WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY", "TYPE=DATA, COLUMN=N1, BUCKET=color, $", "TYPE=DATA, COLUMN=N2, BUCKET=x-axis,"]
#         visual.verify_fexcode_syntax(expcted_syntax, 'Step 04.1 : Verify fex code generated. "QUANTITY_SOLD_BIN_1" added as by field')
#         the above line makes time out error so using below function from ia_resultarea.py
        ia_rsultobj.verify_fexcode_syntax(expcted_syntax, 'Step 04.1 : Verify fex code generated. "QUANTITY_SOLD_BIN_1" added as by field')
        
        """
            Step 06 : Hover on the preview chart and verify tool tip values
        """
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f .legend text[class='legend-title']", 'QUANTITY_SOLD_BIN_1', 40)
        expected_tooltip=['Product Category:Video Production', 'Quantity Sold:5,832', 'QUANTITY_SOLD_BIN_1:4', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_tooltip("riser!s3!g6!mbar", expected_tooltip, 'Step 06.1 : Verify tooltip values')
        
        """
            Step 07 : Click change drop down > select Line
        """
        visual.change_chart_type('line')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f svg text[class='yaxis-labels!m6!']", '600K', 80)
        
        """
            Step 08 : Verify chart converted to line and following preview displayed
        """
        visual.verify_x_axis_title(['Product Category'], msg='Step 08.1')
        visual.verify_y_axis_title(['Quantity Sold'], msg='Step 08.2')
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        visual.verify_x_axis_label(expected_xaxis_labels, msg='Step 08.3')
        visual.verify_y_axis_label(expected_yaxis_labels, msg='Step 08.4')
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f svg path[class^='riser']", 1, 4, msg='Step 08.5')
        visual.verify_legends(['QUANTITY_SOLD_BIN_1', '1', '2', '3', '4'], msg='Step 08.6')
        visual.verify_chart_color_using_get_css_property("path[class='riser!s0!g0!mline!']", 'lochmara', attribute='stroke',  msg='Step 08.7 ')
        visual.verify_chart_color_using_get_css_property(" path[class='riser!s1!g0!mline!']", 'bar_green', attribute='stroke',  msg='Step 08.8 ')
        expected_tooltip=['Product Category:Accessories', 'Quantity Sold:236,127', 'QUANTITY_SOLD_BIN_1:1', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_tooltip("marker!s0!g0!mmarker", expected_tooltip, 'Step 08.9 : Verify tooltip values', use_marker_enable=True, move_to_tooltip=False)
#         visual.take_preview_snapshot(Test_Case_ID, '08')
        
        """
            Step 09 : Click IA > Save as "C2348445" > Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
            Step 10 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
            Step 11 : Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10666%2FC2348445.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f svg text[class='yaxis-labels!m6!']", '600K', 40)
        
        """
            Step 12 : Click change drop down > select Area
        """
        visual.change_chart_type('area')
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f svg .legend path[class^='legend-markers']", 4, 40)
        
        """
            Step 13 : Verify chart converted to line and following preview displayed
        """
        visual.verify_x_axis_title(['Product Category'], msg='Step 13.1')
        visual.verify_y_axis_title(['Quantity Sold'], msg='Step 13.2')
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        visual.verify_x_axis_label(expected_xaxis_labels, msg='Step 13.3')
        visual.verify_y_axis_label(expected_yaxis_labels, msg='Step 13.4')
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f svg path[class*='marea']", 1, 4, msg='Step 13.5')
        visual.verify_legends(['QUANTITY_SOLD_BIN_1', '1', '2', '3', '4'], msg='Step 13.6')
        visual.verify_chart_color_using_get_css_property("path[class='riser!s0!g0!marea!']", 'lochmara',  msg='Step 13.7 ')
        visual.verify_chart_color_using_get_css_property("path[class='riser!s1!g0!marea!']", 'bar_green',  msg='Step 13.8 ')
#         visual.take_preview_snapshot(Test_Case_ID, '13')
        
        """
            Step 14 : Click Run
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f svg text[class='yaxis-labels!m6!']", '600K', 60)
        
        """
            Step 14.1 : Verify run window output
        """
        visual.verify_x_axis_title(['Product Category'], msg='Step 14.1')
        visual.verify_y_axis_title(['Quantity Sold'], msg='Step 14.2')
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        visual.verify_x_axis_label(expected_xaxis_labels, msg='Step 14.3')
        visual.verify_y_axis_label(expected_yaxis_labels, msg='Step 14.4')
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f svg path[class*='marea']", 1, 4, msg='Step 14.5')
        visual.verify_legends(['QUANTITY_SOLD_BIN_1', '1', '2', '3', '4'], msg='Step 14.6')
        visual.verify_chart_color_using_get_css_property("path[class='riser!s0!g0!marea!']", 'lochmara',  msg='Step 14.7 ')
        visual.verify_chart_color_using_get_css_property("path[class='riser!s1!g0!marea!']", 'bar_green',  msg='Step 14.8 ')
#         visual.take_run_window_snapshot(Test_Case_ID, '14')
        
        """
            Step 15 : Hover on the run time chart and verify tool tip values
        """
        expected_tooltip=['Product Category:Accessories', 'Quantity Sold:217,060', 'QUANTITY_SOLD_BIN_1:2', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_tooltip("marker!s1!g0!mmarker", expected_tooltip, 'Step 15.1 : Verify tooltip values', use_marker_enable=True)
        
        """
            Step 16 : Dismiss run window
        """
        visual.switch_to_previous_window()
        
        """
            Step 17 : Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
            Step 18 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()

if __name__=='__main__' :
    unittest.main()