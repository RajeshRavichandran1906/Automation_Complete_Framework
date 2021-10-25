'''
Created on Feb 17, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10099
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253015
Test_Case Name : IA-4707:Vis: Drill up after Drill down not working, throws script error
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.pages import visualization_resultarea

class C2253015_TestClass(BaseTestCase):

    def test_C2253015(self):
        
        Test_Case_ID = "C2253015"
        metadata_browser_css = "#iaMetaDataBrowser"        
        total_no_of_riser_css = "#MAINTABLE_1 rect[class^='riser']"  
        wait_time_in_sec = 120
        yaxis_title_css = "#MAINTABLE_wbody1_f text[class='yaxis-title']"
        xaxis_title_css = "#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']"
        
        visual = visualization.Visualization(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)

        """
        Step01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        visual.wait_for_number_of_element(metadata_browser_css, 1)
        
        """
        Step02: Double click Cost of Goods and Product,Category.
        """
        visual.double_click_on_datetree_item('Cost of Goods', 1)
        visual.wait_for_visible_text(yaxis_title_css, "CostofGoods", 45)
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_visible_text(xaxis_title_css, "ProductCategory", 45)
        
        """
        Step02.00: Verify label values
        """
        x_title=['Product Category']
        y_title=['Cost of Goods']
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visual.verify_x_axis_label(expected_xaxis_labels, msg= 'Step 02.01')
       
        visual.verify_y_axis_label(expected_yaxis_labels, msg= 'Step 02.02')
        
        visual.verify_x_axis_title(x_title, msg= 'Step 02.03')
        visual.verify_y_axis_title(y_title, msg= 'Step 02.04')
        
        """
        Step03: Verify query pane
        """
        no_of_riser=7
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec) 
        visual.verify_field_listed_under_querytree('Vertical Axis', 'Cost of Goods', 1, "Step 03.01: Verify Cost of Goods in Query Pane")  
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Category', 1, "Step 03.02: Verify Product Category in Query Pane") 
        
        """
        Step04: Hover on Media Player
        Verify tooltip values
        """
        no_of_riser=7
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        expected_tooltip_list =['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_tooltip('riser!s0!g3!mbar', expected_tooltip_list, msg='Step 04.01 : Verify tooltip')
        #visual.select_tooltip(Media_Player_riser_css, 'Drill down to Product Subcategory')
        
        """
        Step05: Click Drill down
        Verify horizontal axis label value changed to Product SubCategory
        """
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1','riser!s0!g3!mbar','Drill down to Product Subcategory')
        visual.wait_for_number_of_element(total_no_of_riser_css, 4, wait_time_in_sec)
        x_title=['Product Subcategory']       
        visual.verify_x_axis_title(x_title, msg= 'Step 05.01 : Verify horizontal axis label value changed to Product SubCategory')             
        
        """
        Step06: Verify query added to filter pane       
        """
        visual.verify_field_in_filterbox('Product,Category', 1, "Step 06.01")       
        
        """
        Step07: Hover on Blu Ray
        Verify tooltip
        """
        expected_tooltip_list =['Product Subcategory:Blu Ray', 'Cost of Goods:$181,112,921.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list, msg='Step 07.01 : Verify tooltip')
        #visual.select_tooltip(BluRay_riser_css, 'Drill up to Product Category')
        
        
        """
        Step08: Click Drill up
        Verify horizontal axis label is moved up to one level (Product category)
        """
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', 'riser!s0!g0!mbar', 'Drill up to Product Category')
        no_of_riser=7
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        x_title=['Product Category']
        visual.verify_x_axis_title(x_title, msg= 'Step 08.01')
        
        """
        Step09: Verify output in preview.
        """
        y_title=['Cost of Goods']
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        Accessories_riser='rect[class="riser!s0!g0!mbar!"]'
        visual.verify_x_axis_label(expected_xaxis_labels, msg= 'Step 09.01')  
        visual.verify_y_axis_label(expected_yaxis_labels, msg= 'Step 09.02')
        visual.verify_y_axis_title(y_title, msg= 'Step 09.03')
        visual.verify_chart_color_using_get_css_property(Accessories_riser, 'bar_blue', msg= 'Step 09.04')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 7, msg='Step 09.05')
        
        """
        Step10: Click Run in the toolbar
        Verify output
        """   
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element(total_no_of_riser_css, 7, wait_time_in_sec)
        x_title=['Product Category']
        y_title=['Cost of Goods']
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        Accessories_riser='rect[class="riser!s0!g0!mbar!"]'
        visual.verify_x_axis_label(expected_xaxis_labels, msg= 'Step 10.01')  
        visual.verify_y_axis_label(expected_yaxis_labels, msg= 'Step 10.02')
        visual.verify_x_axis_title(x_title, msg= 'Step 10.03')
        visual.verify_y_axis_title(y_title, msg= 'Step 10.04')
        visual.verify_chart_color_using_get_css_property(Accessories_riser, 'bar_blue', msg= 'Step 10.05')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 7, msg='Step 10.06')
        
        """
        Step11: Close the output window
        """
        visual.switch_to_previous_window()
                 
        """
        Step12: Click "Save" in the toolbar > Type C2253015  > Click "Save" in the Save As dialog
        """
        visual.wait_for_number_of_element(total_no_of_riser_css, 7, wait_time_in_sec)
        visual.save_as_visualization_from_menubar(Test_Case_ID)
                
        """
        Step13: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()