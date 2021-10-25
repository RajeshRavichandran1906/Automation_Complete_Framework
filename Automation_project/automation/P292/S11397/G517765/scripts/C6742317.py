'''
Created on Sep 17, 2018

@author: Varun

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2319021
TestCase Name = Home Tab - Compute
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.wftools import visualization
from common.pages import define_compute

class C6742317_TestClass(BaseTestCase):
    
    def test_C6742317(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C6742317'
        
        visual_obj = visualization.Visualization(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        defcom_obj = define_compute.Define_Compute(self.driver)
        
        expected_field_value='"Cost of Goods" - "Gross Profit"'
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '30M', '60M', '90M','120M', '150M']
        y_axis_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
        
        visual_obj.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        
        """    2. Select Calculation > "Summary (Compute)".    """
        visual_obj.select_ribbon_item("Home", 'calculation->Summary (Compute)')
        dialog_box_css="div[id^=fldCreator]"
        visual_obj.wait_for_number_of_element(dialog_box_css, 4, 150)
        
        """    3. Set Field = "PROFITS".    """
        """    4. Double-click field "Cost of Goods".    """
        visual_obj.enter_define_compute_parameter("PROFITS", "D12.2", "Cost of Goods", 1)
        
        """    5. Click minus ( - ) sign.    """
        visual_obj.select_calculation_btns("minus")
        
        """    6. Double-click field "Gross Profit".    """
        defcom_obj.select_define_compute_field("Gross Profit", 1)
        
        """    7. Verify the following COMPUTE has been created in the textbox.    """
        actual_field = util_obj.validate_and_get_webdriver_object("#ftext","Element")
        actual_field_value = util_obj.get_attribute_value(actual_field,'text_value')
        util_obj.asequal(expected_field_value, actual_field_value['text_value'].strip(), "Step 7a: Verify the following COMPUTE has been created in the textbox.")

        
        """    8. Click "OK".    """
        
        visual_obj.close_define_compute_dialog("ok")
        
        """    9. Verify "PROFITS" is displayed in the Query pane and the following chart is displayed.    """
        
        visual_obj.wait_for_number_of_element(y_axis_css, 6, 120)
        visual_obj.verify_field_listed_under_querytree("Vertical Axis", "PROFITS", 1, "Step 9a: Verify 'PROFITS' is displayed in the Query pane")
        visual_obj.verify_y_axis_title(['PROFITS'],  msg="Step 9b: Verify Y-Axis Title")
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g0!mbar\"]", "lochmara", msg="Step 9c Verify the bar colour")
        
        """    10. Double click field "Product,Category".    """
        visual_obj.double_click_on_datetree_item("Product->Product->Product,Category", 1)
        risers_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        visual_obj.wait_for_number_of_element(risers_css, 7, 120)
        
        """    11. Verify the following chart is displayed.    """
        visual_obj.verify_x_axis_title(['Product Category'],  msg="Step11:a Verify X-Axis Title")
        visual_obj.verify_y_axis_title(['PROFITS'],  msg="Step11:b Verify Y-Axis Title")    
        visual_obj.verify_x_axis_label(expected_xval_list,  msg="Step11:c Verify x-axis label")
        visual_obj.verify_y_axis_label(expected_yval_list,  msg="Step11:d Verify y-axis label")
        visual_obj.verify_number_of_risers("#MAINTABLE_wbody1_f rect[class^=riser]", 1, 7, msg="Step 11.e Verify the total number of risers displayed on preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g2!mbar\"]", "lochmara", msg="Step 11.f Verify the bar colour")
        
        """    12. Click Calculation > "Detail (Define)".    """
        visual_obj.select_ribbon_item('Home','calculation->Detail (Define)')
        dialog_box_css="div[id^=fldCreator]"
        visual_obj.wait_for_number_of_element(dialog_box_css, 4, 150)
        
        """    13. Create a new define as shown:
         Field = Profits
         Format = D12.2 (default)
         Field used = "Cost of Goods" - "Gross Profit"    """
         
        visual_obj.enter_define_compute_parameter("Profits", "D12.2", "Cost of Goods", 1)
        visual_obj.select_calculation_btns("minus")
        defcom_obj.select_define_compute_field("Gross Profit", 1)
        
        """    14. Verify the following DEFINE has been created in the textbox.    """
        actual_field = util_obj.validate_and_get_webdriver_object("#ftext","text_box_element")
        actual_field_value = util_obj.get_attribute_value(actual_field,'text_value')
        util_obj.asequal(expected_field_value, actual_field_value['text_value'].strip(), "Step 14a: Verify the following COMPUTE has been created in the textbox.")
        
        """    15. Click "OK".    """
        visual_obj.close_define_compute_dialog("ok")
        
        """    16. Select "Home" > "Visual" > "Change" (dropdown) > Bar.    """
        visual_obj.change_chart_type('bar')
        parent_css= "div[class*='bi-label dv-caption-label']"
        visual_obj.wait_for_number_of_element(parent_css, 1, 120)
        
        """    17. Double click "Profits" (from Measures).    """
        visual_obj.double_click_on_datetree_item("Sales->Profits", 1)
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        visual_obj.wait_for_number_of_element(parent_css, 14, 120)
        
        """    18. Verify following chart is displayed.    """
        visual_obj.verify_x_axis_title(['Product Category'],  msg="Step18:a Verify X-Axis Title")
        visual_obj.verify_legends(['PROFITS','Profits'], msg="Step18:b Verify legends")
        visual_obj.verify_x_axis_label(expected_xval_list,  msg="Step18:c Verify x-axis label")
        visual_obj.verify_y_axis_label(expected_yval_list,  msg="Step18:d Verify y-axis label")
        visual_obj.verify_number_of_risers("#MAINTABLE_wbody1_f rect[class^=riser]", 2, 7, msg="Step 18.e Verify the total number of risers displayed on preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g2!mbar\"]", "lochmara", msg="Step 18.f Verify the bar colour")
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s1!g0!mbar\"]", "pale_green", msg="Step 18.g Verify the bar colour")
        
        """    19. Click "Run".    """
        visual_obj.run_visualization_from_toptoolbar()
        visual_obj.switch_to_new_window()
        
        """    20. Verify output is correct..    """
        visual_obj.verify_x_axis_title(['Product Category'],  msg="Step20:a Verify X-Axis Title")
        visual_obj.verify_legends(['PROFITS','Profits'], msg="Step20:b Verify legends")
        visual_obj.verify_x_axis_label(expected_xval_list,  msg="Step20:c Verify x-axis label")
        visual_obj.verify_y_axis_label(expected_yval_list,  msg="Step20:d Verify y-axis label")
        visual_obj.verify_number_of_risers("#MAINTABLE_wbody1_f rect[class^=riser]", 2, 7, msg="Step 20.e Verify the total number of risers displayed on preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g6!mbar\"]", "lochmara", msg="Step 20.f Verify the bar colour")
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s1!g5!mbar\"]", "pale_green", msg="Step 20.g Verify the bar colour")
        
        """    21. Close the output window.    """
        visual_obj.switch_to_previous_window()
        visual_obj.wait_for_number_of_element("#applicationButton img", 1, 120)
        
        """    22. Click on "IA" > Select "Save As"    """
        """    23. Save fex as "C2319021" > Click "Save"    """
        visual_obj.save_as_visualization_from_menubar(Test_Case_ID)

        """    24. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        visual_obj.logout_visualization_using_api()
        
        """    25. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2160105.fex&tool=idis    """
        visual_obj.edit_visualization_using_api(Test_Case_ID)
        visual_obj.wait_for_number_of_element("#applicationButton img", 1, 120) 
        
        """    26. Verify Computed field (PROFITS) is displayed in the Query pane.    """
        
        visual_obj.verify_field_listed_under_querytree("Vertical Axis", "PROFITS", 1, "Step 26a: Verify 'PROFITS' is displayed in the Query pane")

        """    27. Verify chart    """

        visual_obj.verify_x_axis_title(['Product Category'],  msg="Step27:a Verify X-Axis Title")
        visual_obj.verify_legends(['PROFITS','Profits'], msg="Step27:b Verify legends")
        visual_obj.verify_x_axis_label(expected_xval_list,  msg="Step27:c Verify x-axis label")
        visual_obj.verify_y_axis_label(expected_yval_list,  msg="Step27:d Verify y-axis label")
        visual_obj.verify_number_of_risers("#MAINTABLE_wbody1_f rect[class^=riser]", 2, 7, msg="Step 27.e Verify the total number of risers displayed on preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g3!mbar\"]", "lochmara", msg="Step 27.f Verify the bar colour")
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s1!g4!mbar\"]", "pale_green", msg="Step 27.g Verify the bar colour")
        
        """    28. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """     
        
if __name__ == '__main__':
    unittest.main()


