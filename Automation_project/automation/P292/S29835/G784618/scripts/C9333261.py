'''
Created on August 9, 2019

@author: vishnu_priya

Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9333261
TestCase Name : Calculate DEFINE
'''
import unittest
from common.wftools import login
from common.wftools.designer_chart import Designer_Chart
from common.locators.designer_chart_locators import DesignerChart as dc_locators
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools import wf_mainpage
from common.locators import wf_mainpage_locators
from common.wftools.text_editor import wf_texteditor

class C9333261_TestClass(BaseTestCase):

    def test_C9333261(self):
        """
            CLASS OBJECTS 
        """
        designer_chart_obj=Designer_Chart(self.driver)
        utils=UtillityMethods(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        login_obj = login.Login(self.driver)
        Core_utils = CoreUtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        text_editor = wf_texteditor(self.driver)
        
        Project_id = Core_utils.parseinitfile('project_id')
        Suite_id   =  Core_utils.parseinitfile('suite_id')
        group_id  =  Core_utils.parseinitfile('group_id')
        repository_folder = Project_id+'_'+Suite_id+'->'+group_id
        
        
        
        """
            TESTCASE ID Variable 
        """
        calculator_edit_value ="WF_RETAIL_LITE.WF_RETAIL_SALES.DISCOUNT_US *250 - WF_RETAIL_LITE.WF_RETAIL_SALES.GROSS_PROFIT_US /2"
        aggregation_css = ".calculate-type-action-check.ibx-widget-disabled"
        expected_text_line_list_1 = ["DEFINE FILE baseapp/wf_retail_lite"]
        expected_text_line_list_2 = ["DISCOUNT_US_1/D20.2M=WF_RETAIL_LITE.WF_RETAIL_SALES.DISCOUNT_US *250 - WF_RETAIL_LITE.WF_RETAIL_SALES.GROSS_PROFIT_US /2;"]
        expected_text_line_list_3 = ["END"]                        
        
        """
        Step 01: Launch the IA API with Chart (edit the domain, port and alias of the URL - do not use the URL as is):
        http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29835%2FG730863%2F&master=baseapp%2Fwf_retail_lite&tool=chart
        Designer chart GUI opens.
        """
        designer_chart_obj.invoke_designer_chart_using_api("baseapp/wf_retail_lite", mrid='mrid', mrpass='mrpass')
        utils.synchronize_until_element_is_visible(dc_locators.MEASURES_FIELD_AREA_CSS,designer_chart_obj.chart_long_timesleep)
          
        """
        Step 02:Right click Measures field "Discount" > select "New Calculation =..."
        """
        designer_chart_obj.right_click_on_measures_field('Sales->Discount','New calculation...')
        utils.synchronize_until_element_is_visible(".wfc-calculator-container",designer_chart_obj.chart_long_timesleep)
          
        """
        Step 02.01:Calculator opens and displays Discount field on the canvas.
        """
        designer_chart_obj.verify_dialog_box_in_calculation('"Discount"',msg= 'Step 02.01 Calculator opens and displays Discount field')
          
        """
        Step 03:Delete the exisiting Discount and add the following formula as shown below:
          
        WF_RETAIL_LITE.WF_RETAIL_SALES.DISCOUNT_US *250 - WF_RETAIL_LITE.WF_RETAIL_SALES.GROSS_PROFIT_US /2
          
        "Calculate after aggregation" button is OFF and not accessible for change."
        """
        designer_chart_obj.edit_calculation_dialog_editor(calculator_edit_value)
        utils.verify_object_visible(aggregation_css,True,msg ="Step 03:Calculate after aggregation button is OFF and not accessible for change.")  
          
        """
        Step 04:Click Ok.
        """
  
        designer_chart_obj.click_button_on_calculation('OK')
  
   
        """
        Step 5:DISCOUNT_US_1 field is added to the tree under Measures (bottom).
        """
          
        designer_chart_obj.verify_fields_in_measures(['DISCOUNT_US_1'], msg='Step 05:01DISCOUNT_US_1 field is added to the tree under Measures',compare_type='asin',field_path ='Sales->DISCOUNT_US_1')
  
  
        """
        Step 6:Click Save and Enter title as "C9333261" > Save
        """
        designer_chart_obj.save_as_from_application_menu('C9333261')
          
        """
        Step 7:Logout using API:
        http://machine:port/alias/service/wf_security_logout.jsp.
        """
        designer_chart_obj.api_logout()
 
        """
        Step 8:Right click C9333261.fex > Edit with Text Editor.
        Following syntex is added to the fex:
        DEFINE FILE baseapp/wf_retail_lite
        DISCOUNT_US_1/D20.2M=WF_RETAIL_LITE.WF_RETAIL_SALES.DISCOUNT_US *250 - WF_RETAIL_LITE.WF_RETAIL_SALES.GROSS_PROFIT_US /2;
        END
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        utils.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, 'C9333261', main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu("C9333261",'Edit with text editor')
        Core_utils.switch_to_new_window()
        text_editor.verify_line_in_texteditor(expected_text_line_list_1,'Step:08.01',comparison_type='asin')
        text_editor.verify_line_in_texteditor(expected_text_line_list_2,'Step:08.02',comparison_type='asin')
        text_editor.verify_line_in_texteditor(expected_text_line_list_3,'Step:08.03',comparison_type='asin')
        Core_utils.switch_to_previous_window()
        
        """
        Step 9:Logout using API:
        http://machine:port/alias/service/wf_security_logout.jsp.
        """

 

 



if __name__ == '__main__':
    unittest.main()