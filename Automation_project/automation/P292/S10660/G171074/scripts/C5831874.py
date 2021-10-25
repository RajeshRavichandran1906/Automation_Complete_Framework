'''
Created on Jul 2, 2018

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5831874
Test case Name =  Change Filter Operator from Range to Less than
'''

import unittest
from common.lib import utillity, core_utility
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, visualization_properties
from common.lib.basetestcase import BaseTestCase

class C5831874_TestClass(BaseTestCase):

    def test_C5831874(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C5831874'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)

        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_1', 'mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']", metaobj.chart_long_timesleep)
        
        """
        Step 02: Double click "Revenue,Local Currency", located under Sales Measures
        """
        metaobj.datatree_field_click('Revenue,Local Currency', 2, 1)
         
        """
        Step 03: Drag and drop "Revenue,Local Currency" into the Filter pane
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, metaobj.chart_long_timesleep)
        metaobj.drag_drop_data_tree_items_to_filter('Revenue,Local Currency', 1) 
         
        """
        Step 04: Click "Operator" dropdown box > Select "Less than or equal to"
        Step 05: Verify dialog
        Step 06: Click OK
        """
        utillobj.synchronize_until_element_is_visible("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']", metaobj.chart_long_timesleep)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Less than or equal to'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 06.00: Verify dialog') 
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),5114060,"Step 06.01: Verify dialog") 
        metaobj.verify_visualization_filters('numeric',['Aggregation','(None)','true'],['By','(None)','true'],['Operator','Less than or equal to','false'],['Sort','Ascending','true'],['ShowPrompt','true'],msg="Step 06.02:")
        metaobj.create_visualization_filters('numeric')
        utillobj.synchronize_until_element_disappear("#avFilterOkBtn", metaobj.chart_long_timesleep)
         
        """
        Step 07: Double click "Product,Subcategory" from Product Dimension
        """
        metaobj.datatree_field_click('Product,Subcategory', 2, 1)
         
        """
        Step 08: Drag and drop "Revenue,Local Currency" into the Size bucket
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 21, metaobj.chart_long_timesleep)
        metaobj.drag_drop_data_tree_items_to_query_tree('Revenue,Local Currency', 1, 'Size', 0)
         
        """
        Step 09: Verify Canvas
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, metaobj.chart_long_timesleep)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',5114060.62,'float',msg="Step 09.00: Verify filter prompt range max values")
        metaobj.verify_filter_pane_field('Revenue,Local Currency',1,"Step 09.01")
        xaxis_value="Product Subcategory"
        yaxis_value="Revenue Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 09.02: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 09.03: Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '0.3B', '0.6B', '0.9B', '1.2B']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09.04: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 09.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue1", "Step 09.06: Verify first bar color")
        
        """
        Step 10: Edit Prompt value > Drag slider handle to the right at value 2030.82 (or approximate)
        """
        utillobj.synchronize_until_element_is_visible("#ar_Prompt_1 span[id$='s_min'", metaobj.chart_long_timesleep)
        propertyobj.move_slider_measure('#ar_Prompt_1','min', 'left', 1, 'float')
        
        """
        Step11: Verify Canvas
        """
        slider_min=4091250.77
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',slider_min,'float',msg="Step 11.00: Verify filter prompt range min values")
        metaobj.verify_filter_pane_field('Revenue,Local Currency',1,"Step 11.01")
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 21, metaobj.chart_long_timesleep)
        xaxis_value="Product Subcategory"
        yaxis_value="Revenue Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 11.02: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 11.03: Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '0.3B', '0.6B', '0.9B', '1.2B']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11.04: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 11.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue1", "Step 11.06: Verify first bar color")
        
        """
        Step 12: Right click "Revenue,Local Currency" filter in the Filter pane > Edit
        Step 13: Verify dialog
        Step 14: Click Cancel
        """
        metaobj.filter_tree_field_click('Revenue,Local Currency',1,1,'Edit...')
        utillobj.synchronize_until_element_is_visible("#avfToValue input", metaobj.chart_long_timesleep)
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.as_GE(float(d['float_value']),slider_min, "Step 14.00: Verify range from dialog")
        metaobj.verify_visualization_filters('numeric',['Aggregation','(None)','false'],['By','Product,Subcategory','true'],['Operator','Less than or equal to','false'],
                                             ['Sort','Ascending','true'],['ShowPrompt','true'],msg="Step 14.01:")
        metaobj.create_visualization_filters('numeric',ok=False)
        utillobj.synchronize_until_element_disappear("#avFilterCancelBtn", metaobj.chart_long_timesleep)
           
        """
        Step15: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utilobj.switch_to_new_window()
           
        """
        Step 16: Verify output
        """
        riser_css="#MAINTABLE_wbody1 rect[class*='riser!s0!g0!mbar']"
        utillobj.synchronize_until_element_is_visible(riser_css, metaobj.chart_long_timesleep)
        xaxis_value="Product Subcategory"
        yaxis_value="Revenue Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16.00: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 16.01: Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '0.3B', '0.6B', '0.9B', '1.2B']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16.02: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 16.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue1", "Step 16.04: Verify first bar color")
           
        """
        Step 17: Close output window
        """
        core_utilobj.switch_to_previous_window()
        parent_css= "#applicationButton img"
        utillobj.synchronize_until_element_is_visible(parent_css, metaobj.chart_long_timesleep)
            
        """
        Step 18: Click Save in the toolbar > Save as "C5831874" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", metaobj.chart_long_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID)
           
        """
        Step 19: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
             
        """
        Step 20: Restore the fex using API
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC5831874.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_1',mrid='mrid',mrpass='mrpass')
            
        """
        Step 21: Verify Canvas
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 21, metaobj.chart_long_timesleep)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',slider_min,'float',msg="Step 21.00: Verify filter prompt range min values")
        metaobj.verify_filter_pane_field('Revenue,Local Currency',1,"Step 21.01")
        xaxis_value="Product Subcategory"
        yaxis_value="Revenue Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 21.02: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 21.03: Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '0.3B', '0.6B', '0.9B', '1.2B']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 21.04: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 21.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue1", "Step 21.06: Verify first bar color")
          
        """
        Step 22: Logout using API: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()