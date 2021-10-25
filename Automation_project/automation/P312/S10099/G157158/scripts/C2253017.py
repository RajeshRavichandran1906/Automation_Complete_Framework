'''
Created on Feb 22, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10099
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253017
Test_Case Name : IA-4047:Visualization chart, tooltip shows bad data after drill down
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2253017_TestClass(BaseTestCase):

    def test_C2253017(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2253017"
        metadata_browser_query_variables__css = "#iaMetaDataBrowser td"  
        metadata_browser_css = "#iaMetaDataBrowser"    
        changed_bar_text_css="[class*='bi-component dv-caption'] div"    
        total_no_of_riser_css = "#MAINTABLE_1 rect[class^='riser']"  
        long_wait_time_in_sec = 120
        short_wait_time_in_sec = 60
        yaxis_title_css = "#MAINTABLE_wbody1_f text[class='yaxis-title']"
        xaxis_title_css = "#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']"
        toolbar_run="#topToolBar #runButton img"
        
        """
        CLASS OBJECTS
        """
        visual = visualization.Visualization(self.driver)
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,riser_color_css,total_risers,tooltip, step_num):
            visual.verify_x_axis_title(x_title, msg='Step ' + step_num + '.01:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step ' + step_num + '.02:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.03'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.04'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_1 rect', 1, total_risers, msg='Step ' + step_num + '.05:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("[class*='"+riser_color_css+"']", 'bar_blue',  msg='Step ' + step_num + '.06:'+' Verify riser color')
            visual.verify_tooltip(riser, tooltip, msg='Step ' + step_num + '.07:'+' Verify riser tooltip')
            
        """
        Step1: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        visual.wait_for_visible_text(metadata_browser_query_variables__css, 'Filters and Variables', short_wait_time_in_sec)
        
        """
        Step2: Change > Bar (side by side)
        """
        visual.change_chart_type('bar')
        visual.wait_for_visible_text(changed_bar_text_css, 'Bar1', short_wait_time_in_sec)
        
        """
        Step03: Double click Shipment Unit(s) and Sale,Year/Quarter
        """
        visual.double_click_on_datetree_item('Shipment Unit(s)', 1)
        visual.wait_for_visible_text(yaxis_title_css, "Shipment Unit(s)", 45)
        visual.double_click_on_datetree_item('Sale,Year/Quarter', 1)
        visual.wait_for_visible_text(xaxis_title_css, "SaleYear/Quarter", 45)
        
        """
        Step04: Verify x and Y axis labels 2013 Q1:8,687
        Step05: Verify tooltip values.
        """
        no_of_riser=20
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec) 
        
        x_title=['Sale Year/Quarter']
        y_title=['Shipment Unit(s)']
        expected_xaxis_labels=['2012 Q1', '2012 Q2', '2012 Q3', '2012 Q4', '2013 Q1']
        expected_yaxis_labels=['0', '30K', '60K', '90K', '120K', '150K']
        Argentina_riser="riser!s0!g4!mbar"
        Argentina_tooltip=['Sale Year/Quarter:2013 Q1', 'Shipment Unit(s):8,687', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to Sale Year/Month']
        step_num='05'
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels, Argentina_riser, Argentina_riser, no_of_riser,Argentina_tooltip, step_num)        
        
        """
        Step06: Drag "Product,Category" to Color bucket
        Step07: Drag "Days,Delayed" to Size bucket
        Step08: Verify query pane
        """
        visual.wait_for_number_of_element(metadata_browser_css, 1, short_wait_time_in_sec)
        visual.drag_field_from_data_tree_to_query_pane("Product,Category", 1, "Color", 1)
        visual.verify_field_listed_under_querytree('Color BY', "Product,Category", 1, "Step 06.01: Verify Product Category added to Color")
        
        visual.wait_for_number_of_element(metadata_browser_css, 1, short_wait_time_in_sec)
        visual.drag_field_from_data_tree_to_query_pane("Days,Delayed", 1, "Size", 1)
        visual.verify_field_listed_under_querytree('Size', "Days,Delayed", 1, "Step 07.01: Verify Days Delayed added to Size")
        
        """
        Step09: Verify tooltip values for 2013 Q1.
        """
        no_of_riser=140
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
        q12013_riser_css="riser!s4!g4!mbar"       
        q12013_tooltip=['Sale Year/Quarter:2013 Q1', 'Shipment Unit(s):2,886', 'Days Delayed:1,495', 'Product Category:Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        visual.verify_tooltip(q12013_riser_css,q12013_tooltip,msg='Step 09.01: Verify q12013_riser_ tooltip', element_location='middle')
        
        """
        Step10: Right click Days,Delayed > More > Aggregation > Maximum
        Step11: Verify query pane
        Step12: Hover on 2013 Q1 and verify Days,Delayed changed to MAX Days Delayed in tooltip
        """
        visual.wait_for_number_of_element(metadata_browser_css, 1, short_wait_time_in_sec)
        visual.right_click_on_field_under_query_tree("Days,Delayed", 1, "More->Aggregation Functions->Maximum")
        Max_days_delayed_css="#queryTreeColumn tr:nth-Child(14) td"
        visual.wait_for_visible_text(Max_days_delayed_css, "MAX.Days,Delayed", short_wait_time_in_sec)
        visual.verify_field_listed_under_querytree('Size', "MAX.Days,Delayed", 1, "Step 11.01: Verify MAX Days Delayed in query pane")
        q12013_tooltip=['Sale Year/Quarter:2013 Q1', 'Shipment Unit(s):2,886', 'MAX Days Delayed:6', 'Product Category:Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        visual.verify_tooltip(q12013_riser_css,q12013_tooltip,msg='Step 12.01: Verify q12013_riser_ tooltip')
       
        """
        Step13: Click Run in the toolbar
        Step14: Hover on a bar and select drill down on product Subcategory
        """
        visual.wait_for_number_of_element(toolbar_run, 1, short_wait_time_in_sec)
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        no_of_riser=140
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
        q12013_riser_css="riser!s4!g4!mbar"
        visual.select_tooltip(q12013_riser_css, "Drill down to->Product Subcategory", move_to_tooltip=True)
        
        """
        Step15: Verify legend changed to Product SubCategory
        Step16: Close the output window
        """   
        no_of_riser=4
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
        legend=['Product Subcategory', 'Home Theater Systems', 'Receivers', 'Speaker Kits', 'iPod Docking Station']
        visual.verify_legends(legend, msg="Step15: Verify legend changed to Product Subcategory")      
        
        visual.switch_to_previous_window()
                 
        """
        Step17: Click "Save" in the toolbar > Type C2253017 > Click "Save" in the Save As dialog
        Step18: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        no_of_riser=140
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
        visual.save_as_visualization_from_menubar(Test_Case_ID)
#         visual.logout_visualization_using_api()

if __name__ == '__main__':
    unittest.main()        