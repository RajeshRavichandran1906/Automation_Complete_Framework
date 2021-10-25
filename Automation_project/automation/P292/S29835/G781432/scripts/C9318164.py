'''
Created on May 28, 2019

@author: Vpriya
Testcase Name : Show as Value
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/9318164
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.locators.designer_chart_locators import DesignerInsight as dc_locators
from common.lib import utillity
from common.lib import core_utility
from common.lib.global_variables  import Global_variables
from common.wftools import wf_mainpage
from common.wftools import login


class C9318164_TestClass(BaseTestCase):
    
    def test_C9318164(self):
        
        """
        Testcase case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        Global_variables_obj=Global_variables()
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        wf_mainpage_obj=wf_mainpage.Wf_Mainpage(self.driver)
        login_obj=login.Login(self.driver)
        
        
        """
        Testcase variables
        """
        
        Testcase_ID=Global_variables_obj.current_test_case
        
        """
        Testcase Css
        """
        Text_editor_css=".wf-ace-text-editor .ace_content"
        expected_text_content=['DEFINE FILE ibisamp/car','DEALER_COST_BIN_1/D7=FLOOR(CAR.BODY.DEALER_COST/100)*100;']
        Expected_X_label_list=['ENGLAND : 4,200', 'ENGLAND : 7,400', 'ENGLAND : 11,100', 'ENGLAND : 14,900', 'FRANCE : 4,600', 'ITALY : 4,900', 'ITALY : 5,600', 'ITALY : 25,000', 'JAPAN : 2,600', 'JAPAN : 2,800', 'W GERMANY : 5,000', 
         'W GERMANY : 5,800', 'W GERMANY : 6,000', 'W GERMANY : 8,300', 'W GERMANY : 8,400', 'W GERMANY : 10,000', 'W GERMANY : 11,000']
        Expected_Y_label_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K', '50K']
        Expected_x_title_list=['COUNTRY : DEALER_COST_BIN_1']
        Expected_y_title_list=['SALES']
        Run_parent_css="#jschart_HOLD_0"

        
        
        """
        Step 1: Launch the API to create new Designer Chart with the Car file
        http://machine:port/{alias}/designer?&item=IBFS:/WFC/Repository/P292_S29835/G730863&master=ibisamp/car&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api("ibisamp/car")
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
  
        """
        Step 2:Under Measures > expand Comp > Carrec > Body under Data panel
        """
        """
        Step 3:Right click on DEALER_COST > Select "Bin Values"
        """
        designer_chart_obj.right_click_on_measures_field("COMP->CARREC->BODY->DEALER_COST","Bin values")
        utill_obj.synchronize_until_element_is_visible(".bin-values-dlg-menu-item .wfc-binvalues-box", designer_chart_obj.chart_long_timesleep)
 

        """
        Step 4:Click the Value button
        """
        designer_chart_obj.edit_bin_values_in_measures(show_as="Value")
        
        """
        Step 5:Click OK
        Verify a field "DEALER_COST_BIN_1" added to the BODY segment of the Dimensions group.
        """
        designer_chart_obj.verify_element_added_in_dimensions("Step:5.1 Verify a field DEALER_COST_BIN_1" ,"COMP->CARREC->BODY->DEALER_COST_BIN_1","DEALER_COST_BIN_1")

        """
        Step 6:Double click "Country", "DEALER_COST_BIN_1" and "Sales"

        Verify the following canvas and Query panel
        """
        designer_chart_obj.double_click_on_dimension_field("COUNTRY")
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "COUNTRY", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_dimension_field("DEALER_COST_BIN_1")
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "DEALER_COST_BIN_1", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field("COMP->CARREC->BODY->SALES")
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "SALES", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(Expected_X_label_list,msg="Step 06:01 verify the x axis label")
        designer_chart_obj.verify_y_axis_label_in_preview(Expected_Y_label_list,msg="Step 06:02 verify the y axis label")
        designer_chart_obj.verify_x_axis_title_in_preview(Expected_x_title_list,msg="Step 06:03 verify the x_title_list")
        designer_chart_obj.verify_y_axis_title_in_preview(Expected_y_title_list,msg="Step 06:04 verify the y_title_list")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s0!g9!mbar!"]', 'bar_blue', msg="Step 06:05 verify the chart colour")
        designer_chart_obj.verify_number_of_risers("rect[class^='riser!']", 1, 17, "Step 06:06 verify the number of risers")
        

        """
        Step 7:Click Save and Enter title as "C9318164" > Save
        """
        designer_chart_obj.save_designer_chart_from_toolbar(Testcase_ID)

 
        """
        Step 8:Logout using API:
        http://machine:port/alias/service/wf_security_logout.jsp.
        """
         
        designer_chart_obj.api_logout()
        
         
        """
        Step 9:Right click the saved fex and Edit with Text Editor.
        
        Verify the following syntax
        
        DEFINE FILE ibisamp/car
        DEALER_COST_BIN_1/D7=FLOOR(CAR.BODY.DEALER_COST/100)*100;
        END
        """
        
        login_obj.invoke_home_page('mrid','mrpass')
        wf_mainpage_obj.expand_repository_folder("Domains->P292_S29835->G730863")
        wf_mainpage_obj.right_click_folder_item_and_select_menu(Testcase_ID,"Edit with text editor")
        core_utility_obj.switch_to_new_window()
        utill_obj.synchronize_until_element_is_visible(".wf-ace-text-editor .ace_content",designer_chart_obj.home_page_long_timesleep)
        text_editor_elem=utill_obj.validate_and_get_webdriver_object(Text_editor_css,"text_editor_css")
        text_content=text_editor_elem.text.split("\n")
        actual_text_content=[x.strip() for x in text_content]
        utill_obj.verify_list_values(expected_text_content, actual_text_content, msg="Step:09.1 ", assert_type="asin")
        
        
        """
        Step 10:Logout using API:
        http://machine:port/alias/service/wf_security_logout.jsp.
        """
        
        designer_chart_obj.api_logout()
        
         
        """
        Step 11:Restore the saved Chart Designer using API link.
        
        http://machine:port/alias/designer?&item=IBFS:/WFC/Repository/P292_S29835/G730863/c9318164.fex
        
        Verify restore successful with Bin field
        """
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api(Testcase_ID.lower())
        utill_obj.synchronize_with_number_of_element("[class*='xaxisOrdinal-labels!']",17,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(Expected_X_label_list,msg="Step 11:01 verify the x axis label")
        designer_chart_obj.verify_y_axis_label_in_preview(Expected_Y_label_list,msg="Step 11:02 verify the y axis label")
        designer_chart_obj.verify_x_axis_title_in_preview(Expected_x_title_list,msg="Step 11:03 verify the x_title_list")
        designer_chart_obj.verify_y_axis_title_in_preview(Expected_y_title_list,msg="Step 11:04 verify the y_title_list")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s0!g9!mbar!"]', 'bar_blue', msg="Step 11:05 verify the chart colour")
        designer_chart_obj.verify_number_of_risers("rect[class^='riser!']", 1, 17, "Step 11:06 verify the number of risers")
        

        """
        Step 12:Click Preview
        
        Verify output
        """
        
        designer_chart_obj.click_toolbar_item("Preview")
        core_utility_obj.switch_to_frame(dc_locators.INSIGHT_PREVIEW_FRAME)
        utill_obj.synchronize_until_element_is_visible(Run_parent_css,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(Expected_X_label_list,parent_css="#jschart_HOLD_0",msg="Step 06:01 verify the x axis label")
        designer_chart_obj.verify_y_axis_label_in_preview(Expected_Y_label_list,parent_css="#jschart_HOLD_0",msg="Step 06:02 verify the y axis label")
        designer_chart_obj.verify_x_axis_title_in_preview(Expected_x_title_list,parent_css="#jschart_HOLD_0",msg="Step 06:03 verify the x_title_list")
        designer_chart_obj.verify_y_axis_title_in_preview(Expected_y_title_list,parent_css="#jschart_HOLD_0",msg="Step 06:04 verify the y_title_list")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s0!g9!mbar!"]', 'bar_blue', parent_css="#jschart_HOLD_0",msg="Step 06:05 verify the chart colour")
        designer_chart_obj.verify_number_of_risers("#jschart_HOLD_0 rect[class^='riser!']", 1, 17, "Step 06:06 verify the number of risers")
        core_utility_obj.switch_to_default_content()
        designer_chart_obj.go_back_to_design_from_preview()
        
        
        """
        Step 13:Logout using API:
        
        http://machine:port/alias/service/wf_security_logout.jsp.
        """


 
       
if __name__ == '__main__':
    unittest.main()