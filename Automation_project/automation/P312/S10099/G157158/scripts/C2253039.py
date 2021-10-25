'''
Created on Feb 17, 2018
@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253039
Test_Case Name : Drill Down not working properly in Design time
'''
import unittest
from common.lib import utillity
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.pages.core_metadata import CoreMetaData

class C2253039_TestClass(BaseTestCase):

    def test_C2253039(self):
        
        Test_Case_ID = "C2253039"
        total_no_of_riser_css="#MAINTABLE_wbody1 rect[class^='riser']"  
        wait_time_in_sec=120
        
        core_meta = CoreMetaData(self.driver)
        util_obj= utillity.UtillityMethods(self.driver)
        visual = visualization.Visualization(self.driver)   
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,total_risers,tooltip, step_num):
            visual.verify_x_axis_title(x_title, msg='Step' + step_num + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step' + step_num + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step' + step_num + '.5:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class*='"+riser, 'bar_blue',  msg='Step' + step_num + '.6:'+' Verify riser color')
            visual.verify_tooltip(riser,tooltip,msg='Step' + step_num + '.7:'+' Verify riser tooltip')
            
        """
        Step1:Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/WF_RETAIL_LITE
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        util_obj.wait_for_page_loads(20)
        
        """
        Step02: Add Cost of Goods(Vertical axis) and Product,Category(horizontal-axis).
        """
        visual.double_click_on_datetree_item('Cost of Goods', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "CostofGoods", 45)
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "Product Category", 45)
        
        """
        Step03: Verify axis label values
        Step04: Verify query pane
        Step05:Hover over "Media Player" bar.

            Verify the tool tip:      
        """
        
        no_of_riser=7
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec) 
        x_title=['Product Category']
        y_title=['Cost of Goods']
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        Media_Player_riser="riser!s0!g3!mbar!"
        Media_Player_riser_riser_tooltip=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Media_Player_riser,no_of_riser,Media_Player_riser_riser_tooltip, '03.1')  
        
        visual.verify_field_listed_under_querytree('Vertical Axis', 'Cost of Goods', 1, "Step04.1: Verify Cost of Goods in Query Pane")  
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Category', 1, "Step04.2: Verify Product,Category in Query Pane")  
         
        Media_Player_riser="riser!s0!g3!mbar!"
        Media_Player_riser_riser_tooltip=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
           
        visual.verify_tooltip(Media_Player_riser,Media_Player_riser_riser_tooltip, msg='Step 05.01: Verify Media_Player_riser tooltip')
                     
        """
        Step06:Drag Product,Category to Filter bucket. Uncheck 'All' and check 'Camcorder' and click ok.
        """    
        core_meta.collapse_data_field_section('Filters and Variables')
        visual.drag_and_drop_from_data_tree_to_filter('Product,Category', 1)
        visual.wait_for_number_of_element("#avFilterOkBtn", 1)
        visual.select_filter_field_values(['[All]'], Ok_button=True)
        visual.select_filter_field_values(['Camcorder'], Ok_button=True)
       
        
        """
        Step07:Verify query added to filter pane
        """
        visual.verify_field_in_filterbox('Product,Category', 1, "Step07: Verify COUNTRY added to Filter pane")        
        
        """
        Step08:Verify output in preview.
        """
        no_of_risera=1
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_risera, wait_time_in_sec) 
        x_title=['Product Category']
        y_title=['Cost of Goods']
        expected_xaxis_labels=['Camcorder']
        expected_yaxis_labels=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        Camcorder_riser="riser!s0!g0!mbar!"
        Camcorder_riser_tooltip=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Drill down to Product Subcategory']
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Camcorder_riser,no_of_risera,Camcorder_riser_tooltip, '08.1') 
        
        """
        Step09:Hover on the bar and click Drill Down
        """
        
        Camcorder_riser="riser!s0!g0!mbar!"
        visual.select_tooltip(Camcorder_riser, 'Drill down to Product Subcategory')
        
        """
        Step10:Verify output display Camcorder subcategory values
        """
        no_of_riserb=3
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riserb, wait_time_in_sec) 
        x_title=['Product Subcategory']
        y_title=['Cost of Goods']
        expected_xaxis_labels=['Handheld','Professional','Standard']
        expected_yaxis_labels=['0', '10M', '20M', '30M', '40M', '50M','60M']
        Professional_riser="riser!s0!g1!mbar!"
        Professional_riser_tooltip=['Product Subcategory:Professional', 'Cost of Goods:$35,218,308.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Professional_riser,no_of_riserb,Professional_riser_tooltip, '10.1') 
        
        
        """
        Step11:Hover any riser(professional), click Drill Up
        """
        
        Camcorder_riser='riser!s0!g1!mbar!'
        visual.select_tooltip(Camcorder_riser, 'Drill up to Product Category')
        
        """
        Step12:Verify it display all bar values.
        """
    
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec) 
        x_title=['Product Category']
        y_title=['Cost of Goods']
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        Media_Player_riser="riser!s0!g3!mbar!"
        Media_Player_riser_riser_tooltip=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Media_Player_riser,no_of_riser,Media_Player_riser_riser_tooltip, '12.1') 
        
        """
        Step13:Click Run in the toolbar
        Step14:Verify output
        """
        visual.run_visualization_from_toptoolbar()
        util_obj.wait_for_page_loads(10)
        visual.switch_to_new_window()
        no_of_riser=7
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec) 
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec) 
        x_title=['Product Category']
        y_title=['Cost of Goods']
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        Media_Player_riser="riser!s0!g3!mbar!"
        Media_Player_riser_riser_tooltip=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Media_Player_riser,no_of_riser,Media_Player_riser_riser_tooltip, '14.1')  
        visual.take_run_window_snapshot(Test_Case_ID, '14')
        visual.switch_to_previous_window()
        """
        Step15:Click "Save" in the toolbar > Type C2141630 > Click "Save" in the Save As dialog
        Step16:Logout of the IA API using the following URL. http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)  
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()