'''
Created on Feb 15, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253014
Test_Case Name : IA-4360:BUE: Drill up after drill down removes options from child filter prompt
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.pages import core_metadata
import time
from common.lib.global_variables import Global_variables

class C2253014_TestClass(BaseTestCase):

    def test_C2253014(self):
        
        Test_Case_ID = "C2253014"
        metadata_browser_css="#iaMetaDataBrowser"        
        total_no_of_riser_css="#MAINTABLE_1 rect[class^='riser']"  
        wait_time_in_sec=120
        yaxis_title_css="#MAINTABLE_wbody1_f text[class='yaxis-title']"
        xaxis_title_css="#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']"
        
        visual = visualization.Visualization(self.driver)
        metadataobj = core_metadata.CoreMetaData(self.driver)
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,total_risers,step_num,tooltip=None):
            visual.verify_x_axis_title(x_title, msg='Step' + step_num + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step' + step_num + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_1 rect', 1, total_risers, msg='Step' + step_num + '.5:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class*='"+riser+"']", 'lochmara',  msg='Step' + step_num + '.6:'+' Verify riser color')
            if tooltip != None:
                visual.verify_tooltip(riser,tooltip,msg='Step' + step_num + '.7:'+' Verify riser tooltip')
            
        """
        Step1: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        visual.wait_for_number_of_element(metadata_browser_css, 1)
         
        """
        Step02: Double click 'Gross Profit' and 'Product,Subcategory'.
        """
        time.sleep(5)
        metadataobj.collapse_data_field_section("Filters and Variables")
        time.sleep(5)
        visual.double_click_on_datetree_item('Gross Profit', 1)
        visual.wait_for_visible_text(yaxis_title_css, "GrossProfit", 45)
        visual.double_click_on_datetree_item('Product,Subcategory', 1)
        visual.wait_for_visible_text(xaxis_title_css, "ProductSubcategory", 45)
         
        """
        Step03: Verify label values
        Step04: Verify query pane
        Step05: Verify first and last 3 bar riser values (Product Subcategory:Gross Profit)
        """
        no_of_riser=21
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec) 
        visual.verify_field_listed_under_querytree('Vertical Axis', 'Gross Profit', 1, "Step04.1: Verify Gross Profit in Query Pane")  
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Subcategory', 1, "Step04.2: Verify Product Subcategory in Query Pane") 
         
        x_title=['Product Subcategory']
        y_title=['Gross Profit']
        expected_xaxis_labels=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable']
        expected_yaxis_labels=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        Blu_ray_riser="riser!s0!g0!mbar"
        Blu_ray_tooltip=['Product Subcategory:Blu Ray', 'Gross Profit:$51,771,195.13', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        step_num='05.1'
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Blu_ray_riser,no_of_riser, step_num)        
         
        Boom_Box_riser="riser!s0!g1!mbar"
        Boom_Box_tooltip=['Product Subcategory:Boom Box', 'Gross Profit:$546,423.99', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        CRT_TV_riser="riser!s0!g2!mbar"
        CRT_TV_tooltip=['Product Subcategory:CRT TV', 'Gross Profit:$602,419.65', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        Universal_Remote_Controls_riser="riser!s0!g18!mbar"
        Universal_Remote_Controls_tooltip=['Product Subcategory:Universal Remote Controls', 'Gross Profit:$13,361,292.65', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        Video_Editing_riser="riser!s0!g19!mbar"
        Video_Editing_tooltip=['Product Subcategory:Video Editing', 'Gross Profit:$17,947,619.62', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        iPod_Docking_Stationy_riser="riser!s0!g20!mbar"
        iPod_Docking_Stationy_tooltip=['Product Subcategory:iPod Docking Station', 'Gross Profit:$15,328,473.06', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        visual.verify_tooltip(Boom_Box_riser,Boom_Box_tooltip,msg='Step05.2.1 Verify Boom_Box_riser tooltip')
        visual.verify_tooltip(CRT_TV_riser,CRT_TV_tooltip,msg='Step05.2.2 Verify CRT_TV_riser tooltip')
        visual.verify_tooltip(Universal_Remote_Controls_riser,Universal_Remote_Controls_tooltip,msg='Step05.2.3 Verify Universal_Remote_Controls_riser tooltip')
        visual.verify_tooltip(Video_Editing_riser,Video_Editing_tooltip,msg='Step05.2.4 Verify Video_Editing_riser tooltip')
        visual.verify_tooltip(iPod_Docking_Stationy_riser,iPod_Docking_Stationy_tooltip,msg='Step05.2.5 Verify iPod_Docking_Stationy_riser tooltip')
         
        """
        Step06: Drag 'Product,Category' to filter, leave defaults > OK
        """
        visual.wait_for_number_of_element(metadata_browser_css, 1)
        visual.drag_and_drop_from_data_tree_to_filter('Product,Category', 1)
        visual.wait_for_number_of_element("#avFilterOkBtn", 1)
        visual.close_filter_dialog('ok')
         
        """
        Step07: Verify query added to filter pane
        Step08: Drag 'Product,Subcategory' to filter, leave defaults > OK.
        Step09: Verify query added to filter pane
        """
        visual.verify_field_in_filterbox('Product,Category', 1, "Step07: Verify Product Category added to Filter pane")
#         visual.drag_and_drop_from_data_tree_to_filter('Product,Subcategory', 2)
        visual.wait_for_number_of_element(metadata_browser_css, 1)
        visual.drag_and_drop_from_data_tree_to_filter('Product,Subcategory', 1)
#         visual.right_click_on_field_under_query_tree('Product,Subcategory', 1, "Filter Values...")
        visual.wait_for_number_of_element("#avFilterOkBtn", 1)
        visual.close_filter_dialog('ok')
        visual.verify_field_in_filterbox('Product,Subcategory', 2, "Step09: Verify Product Subcategory added to Filter pane")
        no_of_riser=21
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        
        """
        Step10: Click Run in the visualization
        Step11: Hover over Tablet > "Drill Down to Model".
        Step12: Verify horizontal axis label value
        Step13: Verify Tablet model values display in output
        """
        visual.run_visualization_from_toptoolbar()
        count=1
        while True:
            if count==90:
                break
            total_window=len(self.driver.window_handles)
            if total_window>0:
                break
            else:
                count+=1
                continue
            time.sleep(1)
        visual.switch_to_new_window()
        if Global_variables.browser_name == 'edge':
            Global_variables.current_working_area_browser_y = 76
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        tablet_riser_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(tablet_riser_css, 21)
        tablet_riser_css='riser!s0!g17!mbar!'
        visual.select_tooltip(tablet_riser_css, 'Drill down to Model')
        
        no_of_riser=10
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec) 
        x_title=['Model']
        y_title=['Gross Profit']
        expected_xaxis_labels=['GLXYT10716', 'GLXYT10732', 'GLXYT3B', 'GLXYT3W', 'GLXYT70']
        expected_yaxis_labels=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        GLXYT70_riser="riser!s0!g4!mbar"
        GLXYT70_tooltip=['Model:GLXYT70', 'Gross Profit:$380,445.49', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Subcategory']
        step_num="13"
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,GLXYT70_riser,no_of_riser,step_num, tooltip=GLXYT70_tooltip)        
        
        """
        Step14: On resultant chart, hover over (GLXYT70) bar > Drill Up.
        Step15: Verify output
        Step16: Dismiss run window
        """
        #MAINTABLE_wbody1 rect[class^='riser!s']
        GLXYT70_riser_css="#MAINTABLE_wbody1 rect[class^='riser!s0!g4!mbar']"
        visual.wait_for_number_of_element(GLXYT70_riser_css, 1)
        GLXYT70_riser_css1='riser!s0!g4!mbar'
        visual.select_tooltip(GLXYT70_riser_css1, 'Drill up to Product Subcategory')
        
        no_of_riser=21
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec) 
        
        x_title=['Product Subcategory']
        y_title=['Gross Profit']
        expected_xaxis_labels=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', ]
        expected_yaxis_labels=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        Blu_ray_riser="riser!s0!g0!mbar"
        Blu_ray_tooltip=['Product Subcategory:Blu Ray', 'Gross Profit:$51,771,195.13', 'Filter Chart', 'Exclude from Chart', 'Undo Filter', 'Remove Filter', 'Drill up to Product Category', 'Drill down to Model']
        step_num="15"
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Blu_ray_riser,no_of_riser,step_num, tooltip=Blu_ray_tooltip)        
        visual.switch_to_previous_window()
         
        """
        Step17: Click "Save" in the toolbar > Type C2141213 > Click "Save" in the Save As dialog
        Step18: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        no_of_riser=21
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        visual.save_visualization_from_top_toolbar(Test_Case_ID)
#         visual.logout_visualization_using_api()

if __name__ == '__main__':
    unittest.main()        
