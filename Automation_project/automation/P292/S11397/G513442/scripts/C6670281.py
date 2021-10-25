'''
Created on September 20,2018

@author: Varun

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/11397
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6670281
TestCase Name = Alphanumeric Filter with Define field
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.pages import core_metadata

class C6670281_TestClass(BaseTestCase):

    def test_C6670281(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C6670281'
        x_axis_css = "#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        y_axis_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        expected_xval_list=["Accessories", "Camcorder", "Computers","Stereo Systems"]
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K','300K','350K','400K']
        xaxis_value="Product"
        
        visual_obj = visualization.Visualization(self.driver)
        coreobj = core_metadata.CoreMetaData(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        visual_obj.invoke_visualization_using_api('baseapp/wf_retail_lite')       
        
        """
        Step 02:Double-click "Days,Delayed" and "Shipment,Unit(s)", located under Shipment Measures
        """
        visual_obj.double_click_on_datetree_item("Days,Delayed", 1)
        visual_obj.wait_for_number_of_element(y_axis_css, 10, 120)
        visual_obj.double_click_on_datetree_item("Shipment Unit(s)", 1)
        visual_obj.wait_for_number_of_element(y_axis_css, 6, 120)
        
        """
        Step 03: Select Calculation > Detail (Define) in the Home Tab ribbon
        """
        visual_obj.select_ribbon_item("Home", 'calculation->Detail (Define)')
        dialog_box_css="div[id^=fldCreator]"
        visual_obj.wait_for_number_of_element(dialog_box_css, 4, 150)
        
        """
        Step 04: Type "Product" for Field name, change Format to A40V
        Step 05: Expand Product Dimension > Double click "Product,Category"
        """ 
        visual_obj.enter_define_compute_parameter("Product", "A40V", "Product,Category", 1)
        
        """
        Step 06:Click OK
        """
        visual_obj.close_define_compute_dialog("ok")
        
        """
        Step 07: Verify Define field "Product" appears in the Data pane
        """
        coreobj.expand_data_field_section('Product->Product')
        visual_obj.verify_field_listed_under_datatree("Product", "Product", 5, "Step 7a: Verify 'Product' is displayed in the data pane")
         
        """
        Step 08: Double click "Product" to add field to Canvas
        """
        visual_obj.double_click_on_datetree_item("Product->Product->Product", 3)
        visual_obj.wait_for_number_of_element(y_axis_css, 9, 120)
         
        """
        Step 09: Drag and drop "Product" from Data pane into the Filter pane
        """
        visual_obj.drag_and_drop_from_data_tree_to_filter('Product->Product->Product', 3) 
        ok_button_css = "div[id^=QbDialog] div[id^=avFilterOk]"
        visual_obj.wait_for_number_of_element(ok_button_css,1,120)
              
        """
        Step 10: Verify Filter dialog
        """
        item_list=['[All]', 'Accessories','Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_filter_field_values(item_list, verify_type='true')
         
        """
        Step 11: Uncheck "[All]"
        """
        visual_obj.select_filter_field_values(["[All]"])
        visual_obj.wait_for_number_of_element(ok_button_css,1,120)
        
        """    
        Step 12: Select "Accessories", "Camcorder", "Computers" and "Stereo Systems"
        Step 13: Click ok
        """
        visual_obj.select_filter_field_values(expected_xval_list,Ok_button=True)
         
        """
        Step 14: Verify Canvas
        """
        visual_obj.wait_for_number_of_element(x_axis_css, 4, 120)
        visual_obj.verify_item_checked_status_in_show_prompt_table("[All]", checked_status=False, msg="14.a: Verify that All is unchecked")
        for i in expected_xval_list:
            visual_obj.verify_item_checked_status_in_show_prompt_table(i, msg="step 14b: verify the show prompt checked items")
        visual_obj.verify_x_axis_label(expected_xval_list,  msg="Step14:c Verify x-axis label")
        visual_obj.verify_y_axis_label(expected_yval_list,  msg="Step14:d Verify x-axis label")
        visual_obj.verify_x_axis_title([xaxis_value],  msg="Step14:e Verify X-Axis Title")
        visual_obj.verify_number_of_risers("#MAINTABLE_wbody1_f rect[class^=riser]", 1, 8, msg="Step 14.f Verify the total number of risers displayed on preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g1!mbar\"]", "bar_blue", msg="Step 14.g Verify the bar colour")
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g2!mbar\"]", "lochmara", msg="Step 14.h Verify the bar colour")

        """
        Step15: Click Run
        """
        visual_obj.run_visualization_from_toptoolbar()
        visual_obj.switch_to_new_window()
           
        """
        Step16: Verify output
        """
        visual_obj.wait_for_number_of_element(x_axis_css, 4, 120)
        visual_obj.verify_x_axis_label(expected_xval_list,  msg="Step16:a Verify x-axis label")
        visual_obj.verify_y_axis_label(expected_yval_list,  msg="Step16:b Verify x-axis label")
        visual_obj.verify_x_axis_title([xaxis_value],  msg="Step16:c Verify X-Axis Title")
        visual_obj.verify_number_of_risers("#MAINTABLE_wbody1_f rect[class^=riser]", 1, 8, msg="Step 16.d Verify the total number of risers displayed on preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g1!mbar\"]", "bar_blue", msg="Step 16.e Verify the bar colour")
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g2!mbar\"]", "lochmara", msg="Step 16.f Verify the bar colour")
        for item in expected_xval_list:
            visual_obj.verify_item_checked_status_in_show_prompt_table(item,parent_prompt_css="#PROMPT_1_cs", msg="step 16g: verify the show prompt checked items")
           
        """
        Step17: Close output window
        """
        visual_obj.switch_to_previous_window()
        visual_obj.wait_for_number_of_element("#applicationButton img", 1, 120)
        
        """
        Step18: Click Save in the toolbar
        Step19: Save as "C6670281" > Click Save
        """
        visual_obj.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step20: Logout: http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual_obj.logout_visualization_using_api()
        
        """
        Step21: Reopen fex using IA API: http://machine:port/alias/ia?item=IBFS%3A%2FWFC%2FRepository%2FS11397%2FC6670281.fex
        """
        visual_obj.edit_visualization_using_api(Test_Case_ID)
        visual_obj.wait_for_number_of_element("#applicationButton img", 1, 120)
        
        """
        Step22: Verify Canvas
        """
        visual_obj.wait_for_number_of_element(x_axis_css, 4, 120)
        visual_obj.verify_x_axis_label(expected_xval_list,  msg="Step22:a Verify x-axis label")
        visual_obj.verify_y_axis_label(expected_yval_list,  msg="Step22:b Verify x-axis label")
        visual_obj.verify_x_axis_title([xaxis_value],  msg="Step22:c Verify X-Axis Title")
        visual_obj.verify_number_of_risers("#MAINTABLE_wbody1_f rect[class^=riser]", 1, 8, msg="Step 22.d Verify the total number of risers displayed on preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g1!mbar\"]", "bar_blue", msg="Step 22.e Verify the bar colour")
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g2!mbar\"]", "lochmara", msg="Step 22.f Verify the bar colour")
        for item in expected_xval_list:
            visual_obj.verify_item_checked_status_in_show_prompt_table(item, msg="step 22g: verify the show prompt checked items") 
        
        """
        Step23: Logout: http://machine:port/alias/service/wf_security_logout.jsp
        """ 
         

if __name__ == '__main__':
    unittest.main()