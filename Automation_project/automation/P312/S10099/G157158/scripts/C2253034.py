'''
Created on Feb 14, 2018

@author: Robert

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253034
TestCase Name = Vis: Filter, Drilldown and Exclude Chart with 2 By's in Preview returns incorrect output
'''

import unittest
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.pages.core_metadata import CoreMetaData
from common.lib.global_variables import Global_variables

class C2253034_TestClass(BaseTestCase):

    def test_C2253034(self):
        
        """
        CLASS & OBJECTS
        """
        coremeta = CoreMetaData(self.driver)
        visual = visualization.Visualization(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2253034'
        position=1
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/WF_RETAIL_LITE
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
         
        """
        Step 02. Double click "Revenue" and "Product,SubCategory".
        """
        field_name='Revenue'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 1, 30)
        field_name="Product,Subcategory"
        visual.double_click_on_datetree_item(field_name,position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 21, 30)
         
        """
        Step 02.00. Verify label values
        """
        x_axis_title=['Product Subcategory']
        visual.verify_x_axis_title(x_axis_title, msg='Step 02.01')
        y_axis_title=['Revenue']
        visual.verify_y_axis_title(y_axis_title, msg='Step 02.02')
        expected_xaxis_label=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 02.03')
        expected_yaxis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 02.04')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 21, msg='Step 02.05')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 02.06 ')
         
        """
        Step 03. Hover over "Blu Ray" bar.
        Verify the tool tip:
        """
        expected_tooltip_list=['Product Subcategory:Blu Ray', 'Revenue:$232,884,116.13', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 03.01 : Verify Tooltip') 
         
        """
        Step 04. Add "Product,Category" to Horizontal axis.
        """
        coremeta.collapse_data_field_section('Filters and Variables')
        field_name='Product,Category'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#queryTreeWindow"
        visual.wait_for_visible_text(parent_css, visble_element_text='Product,Category', time_out=50)
        
        """
        Step 04.00 Verify vertical and horizontal axis labels:
        """
        visual.wait_for_visible_text('[class*="labels!g0!mgroupLabel!"]','Blu Ray :', time_out=50)
        if Global_variables.browser_name == 'chrome':
            expected_xaxis_label=['Blu Ray : Media Pl...', 'Boom Box : Stere...', 'CRT TV : Televisions', 'Charger : Accesso...', 'DVD Players : Me...']
        else:
            expected_xaxis_label=['Blu Ray : Media Player', 'Boom Box : Stereo S...', 'CRT TV : Televisions', 'Charger : Accessories', 'DVD Players : Media...']
        visual.verify_x_axis_label(expected_xaxis_label,xyz_axis_label_length=5, msg='Step 04.01')
        expected_yaxis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 04.02')
        
        """
        Step 05. Verify query pane
        """
        visual.verify_field_listed_under_querytree('Vertical Axis', 'Revenue', position, "Step 05.01 ")
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Category', position+1, "Step 05.02 ")
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Subcategory', position, "Step 05.03 ")       
        
        """
        Step 06. Hover over on "Blu Ray:Media Player" and Select Filter Chart.
        """
        visual.select_tooltip('riser!s0!g0!mbar!', "Filter Chart") 
         
        """
        Step 06.00. Verify query added to filter pane
        """
        parent_css="#MAINTABLE_wbody1 [class^='riser!']"
        visual.wait_for_number_of_element(parent_css, 1, 10)
        visual.verify_field_in_filterbox('PRODUCT_SUBCATEG and PRODUCT_CATEGORY', position, "Step 06.01 ")
                 
        """
        Step 07. Verify filtered bar riser value
        """
        parent_css= "#MAINTABLE_wbody1_f text[class^='xaxis'][class$='title']"
        visual.wait_for_visible_text(parent_css, 'Product Subcategory : Product Category')
        x_axis_title=['Product Subcategory : Product Category']
        visual.verify_x_axis_title(x_axis_title, msg='Step 07.01')
        y_axis_title=['Revenue']
        visual.verify_y_axis_title(y_axis_title, msg='Step 07.02')
        expected_xaxis_label=['Blu Ray : Media Player']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 07.03')
        expected_yaxis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 07.04')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 1, msg='Step 07.05')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 07.06 ')
         
        """
        Step 08. Hover over on "Blu Ray: Media Player" and Select Drill down to > Model.
        """
        visual.select_tooltip('riser!s0!g0!mbar!', "Drill down to->Model")
       
        """
        Step 08.00. Verify it lists the models of "Blu Ray: Media Player":
        """
        parent_css="#MAINTABLE_wbody1 [class^='riser!']"
        visual.wait_for_number_of_element(parent_css, 21, 160)
        x_axis_title=['Model : Product Category']
        visual.verify_x_axis_title(x_axis_title, msg='Step 08.01')
        y_axis_title=['Revenue']
        visual.verify_y_axis_title(y_axis_title, msg='Step 08.02')
        expected_xaxis_label=['JVC XV-BP1 : Media Player', 'JVC XV-BP10 : Media Player', 'JVC XV-BP11 : Media Player', 'Panasonic DMP-BD30 : Media Pla...', 'Panasonic DMP-BD60 : Media Pla...', 'Panasonic DMP-BD70V : Media Pl...', 'Panasonic DMP-BD80 : Media Pla...', 'Pioneer BDP-120 : Media Player', 'Pioneer BDP-320 : Media Player', 'Pioneer BDP-330 : Media Player', 'Pioneer BDP-51 : Media Player', 'SAMSUNG BD-C6500 : Media Pla...', 'SHARP BD-HP70U : Media Player', 'Samsung BD-C5500 : Media Player', 'Samsung BD-P1600 : Media Player', 'Samsung BD-P3600 : Media Player', 'Sharp BD-HP24U : Media Player', 'Sony BDP-S360 : Media Player', 'Sony BDP-S370 : Media Player', 'Sony BDP-S470 : Media Player', 'Sony BDP-S570 : Media Player']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 08.03', xyz_axis_label_length=2) #label getting change in browser hence using below 
        expected_yaxis_label=['0', '4M', '8M', '12M', '16M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 08.04')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 08.05 ')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 21, msg='Step 08.06')
        
        
        """
        Step 9. Hover over first bar "JVC XV-BP1:Media Player" and Select Exclude from chart.
        """
        visual.select_tooltip('riser!s0!g0!mbar!', "Exclude from Chart")
        
        """
        Step 9.00: Verify output in preview:
        """
        parent_css="#MAINTABLE_wbody1 [class^='riser!']"
        visual.wait_for_number_of_element(parent_css, 20, 40)
        x_axis_title=['Model : Product Category']
        visual.verify_x_axis_title(x_axis_title, msg='Step 09.01')
        y_axis_title=['Revenue']
        visual.verify_y_axis_title(y_axis_title, msg='Step 09.02')
        expected_xaxis_label=['JVC XV-BP10 : Media Player', 'JVC XV-BP11 : Media Player', 'Panasonic DMP-BD30 : Media Pla...', 'Panasonic DMP-BD60 : Media Pla...', 'Panasonic DMP-BD70V : Media Pl...', 'Panasonic DMP-BD80 : Media Pla...', 'Pioneer BDP-120 : Media Player', 'Pioneer BDP-320 : Media Player', 'Pioneer BDP-330 : Media Player', 'Pioneer BDP-51 : Media Player', 'SAMSUNG BD-C6500 : Media Pla...', 'SHARP BD-HP70U : Media Player', 'Samsung BD-C5500 : Media Player', 'Samsung BD-P1600 : Media Player', 'Samsung BD-P3600 : Media Player', 'Sharp BD-HP24U : Media Player', 'Sony BDP-S360 : Media Player', 'Sony BDP-S370 : Media Player', 'Sony BDP-S470 : Media Player', 'Sony BDP-S570 : Media Player']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 09.03', xyz_axis_label_length=2)
        expected_yaxis_label=['0', '4M', '8M', '12M', '16M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 09.04')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 09.05 ')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 20, msg='Step 09.06')
        
        """
        Step 10. Verify query added to filter pane
        """        
        visual.verify_field_in_filterbox('PRODUCT_SUBCATEG and PRODUCT_CATEGORY', position, "Step 10.01 ")
        
        visual.verify_field_in_filterbox('MODEL and PRODUCT_CATEGORY', position+1, "Step 10.02 ")
        
        """
        Step 11: Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Step 12: Verify output at runtime. 
        """
        parent_css="#MAINTABLE_wbody1 text[class^='xaxisOrdinal-title']"
        visual.wait_for_visible_text(parent_css, visble_element_text='Model : Product Category', time_out=50)
        visual.verify_x_axis_title(['Model : Product Category'], msg='Step 12.01')
        visual.verify_y_axis_title(['Revenue'], msg='Step 12.02')
        expected_xaxis_label=['JVC XV-BP10 : Media Player', 'JVC XV-BP11 : Media Player', 'Panasonic DMP-BD30 : Media Pla...', 'Panasonic DMP-BD60 : Media Pla...', 'Panasonic DMP-BD70V : Media Pl...', 'Panasonic DMP-BD80 : Media Pla...', 'Pioneer BDP-120 : Media Player', 'Pioneer BDP-320 : Media Player', 'Pioneer BDP-330 : Media Player', 'Pioneer BDP-51 : Media Player', 'SAMSUNG BD-C6500 : Media Pla...', 'SHARP BD-HP70U : Media Player', 'Samsung BD-C5500 : Media Player', 'Samsung BD-P1600 : Media Player', 'Samsung BD-P3600 : Media Player', 'Sharp BD-HP24U : Media Player', 'Sony BDP-S360 : Media Player', 'Sony BDP-S370 : Media Player', 'Sony BDP-S470 : Media Player', 'Sony BDP-S570 : Media Player']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 12.03', xyz_axis_label_length=2)
        expected_yaxis_label=['0', '4M', '8M', '12M', '16M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 12.04')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 20, msg='Step 12.05')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g12!mbar!']", "bar_blue", msg='Step 12.06 ')
        visual.switch_to_previous_window()
        
        """
        Step 13: Click "Save" in the toolbar > Type C2253034 > Click "Save" in the Save As dialog
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 14: Logout of the IA API using the following URL: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
                
if __name__ == '__main__':
    unittest.main()