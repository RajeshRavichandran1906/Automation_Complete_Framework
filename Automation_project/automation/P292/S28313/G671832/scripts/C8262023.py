'''
Created on September 17, 2019

@author: AA14564.
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262023
TestCase Name = PCT.CNT as aggregation option for dimension (char) fields in IA+
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer_chart import Designer_Chart
from common.lib import utillity
from common.lib import core_utility
from common.wftools import chart
from common.pages.wf_mainpage import Wf_Mainpage
from common.locators.designer_chart_locators import DesignerChart as dc_locators
from common.lib.global_variables import Global_variables

class C8262023_TestClass(BaseTestCase):
    
    def test_C8262023(self):
        """
        TESTCASE VARIABLES
        """
        
        utillobj = utillity.UtillityMethods(self.driver)
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        chart_obj = chart.Chart(self.driver)
        wf_main_page = Wf_Mainpage(self.driver)
        designer_chart_obj=Designer_Chart(self.driver)
        g_var = Global_variables
        
        step1=""" Step 1: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                http://domain.com:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774&tool=chart&master=baseapp/wf_retail_lite
        """
        designer_chart_obj.invoke_designer_chart_using_api("baseapp/wf_retail_lite")
        utillobj.synchronize_until_element_is_visible(dc_locators.DIMENSIONS_FIELD_AREA_CSS, designer_chart_obj.chart_long_timesleep)
        utillobj.capture_screenshot('01.00', step1)
  
        step2=""" Step 2: Double click "Product, Category" to Horizontal axis
        """
        designer_chart_obj.double_click_on_dimension_field('Product->Product->Product,Category')
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box", "Product,Category", designer_chart_obj.home_page_long_timesleep)
        utillobj.capture_screenshot('02.00', step2)
        
        step3=""" Step 3: Right click "Model" > select "Add as measure"
        """
        designer_chart_obj.right_click_on_dimensions_field('Model', context_menu_item_path='Add as measure')
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box", "CNT.Model", designer_chart_obj.home_page_long_timesleep)
        utillobj.capture_screenshot('03.00', step3)
        
        step4=""" Step 4: Verify in query pane Vertical axis CNT prefix added to "Model" field and displayed same in preview
                Expected to see "CNT.Model"
        """
        designer_chart_obj.verify_values_in_querybucket('Vertical', ['CNT.Model'], 'Step 04.00: Verify in query pane Vertical axis CNT prefix added to "Model" field.')
        utillobj.synchronize_until_element_is_visible("[id*='chartpreview_fdmId'] [class*='riser!s0!g0!mbar']", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg='Step 04.01')
        designer_chart_obj.verify_y_axis_label_in_preview(['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50'], msg='Step 04.02')
        designer_chart_obj.verify_x_axis_title_in_preview(['Product Category'], msg='Step 04.03')
        designer_chart_obj.verify_y_axis_title_in_preview(['CNT Model'], msg='Step 04.04')
        utillobj.capture_screenshot('04.00', step4)
    
        step5=""" Step 5: Right click on "CNT.Model" > Aggregate
        """
        designer_chart_obj.select_query_bucket_field_context_menu('Vertical', 'CNT.Model', 'Aggregate', click_type=None)
        utillobj.capture_screenshot('05.00', step5)
           
        step6=""" Step 6: Verify the list of options
                Count (selected by default)
                Count Distinct
                Percent of Count
        """
        designer_chart_obj.verify_query_bucket_field_context_menu(['Count', 'Count distinct', 'Percent', 'Percent of count'], 'Step 06.00: Verify the list of options "Count, Count Distinct, Percent of Count"', comparision_type='asin')
        designer_chart_obj.verify_query_bucket_field_option_in_context_menu_checked(['Count'], 'Step 06.01: Verify the list of options "Count (selected by default)"')
        utillobj.capture_screenshot('06.00', step6)
           
        step7=""" Step 7: Click "Percent of Count" option
        """
        wf_main_page.select_context_menu_item('Percent of count')
        utillobj.capture_screenshot('07.00', step7)
         
        step8=""" Step 8: Verify query pane and preview updated with "PCT.CNT.Model" aggregation function
        """
        designer_chart_obj.verify_values_in_querybucket('Vertical', ['PCT.CNT.Model'], 'Step 08.00: Verify query pane and preview updated with "PCT.CNT.Model" aggregation function.')
        utillobj.synchronize_with_visble_text("[id*='chartpreview'] .yaxis-title", 'PCT.CNT MODEL', designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg='Step 08.01')
        designer_chart_obj.verify_y_axis_label_in_preview(['0', '5', '10', '15', '20', '25', '30'], msg='Step 08.02')
        designer_chart_obj.verify_x_axis_title_in_preview(['Product Category'], msg='Step 08.03')
        designer_chart_obj.verify_y_axis_title_in_preview(['PCT.CNT MODEL'], msg='Step 08.04')
        designer_chart_obj.verify_number_of_risers("[id*='chartpreview'] .risers rect", 1, 7, msg='Step 08.05')
        utillobj.capture_screenshot('08.00', step8)
         
        step9=""" Step 9: Right Click "PCT.CNT.Model" > Aggregate
        """
        designer_chart_obj.select_query_bucket_field_context_menu('Vertical', 'PCT.CNT.Model', 'Aggregate', click_type=None)
        utillobj.capture_screenshot('09.00', step9)
         
        step10="""
        Step 10: Verify "Percent of Count" option is selected
        """
        designer_chart_obj.verify_query_bucket_field_option_in_context_menu_checked(['Percent of count'], 'Step 10.01: Verify "Percent of Count" option is selected.')
        utillobj.capture_screenshot('10.00', step10)
         
        step11=""" Step 11: Click Run
        """
        designer_chart_obj.click_toolbar_item("preview")
        utillobj.capture_screenshot('11.00', step11)
         
        step12=""" Step 12: Hover on "Media Player " riser
        """
        core_utill_obj.switch_to_frame("iframe[src*='TableChart_1']")
        utillobj.synchronize_until_element_is_visible("#jschart_HOLD_0 [class='riser!s0!g2!mbar!']", designer_chart_obj.home_page_long_timesleep)
        utillobj.capture_screenshot('12.00', step12, expected_image_verify=True)
         
        step13=""" Step 13: Verify the tool tip value
        """
        chart_obj.verify_tooltip_in_run_window('riser!s0!g3!mbar', ['Product Category:Media Player', 'PCT.CNT MODEL:27'], msg="Step 13.00 : Verify 'Media Player ' riser tool tip value.")
        utillobj.capture_screenshot('13.00', step13)
         
        step14=""" Step 14: Click Save in the toolbar > Save as "C8262023" > Click Save
        """
        core_utill_obj.switch_to_default_content()
        designer_chart_obj.go_back_to_design_from_preview()
        designer_chart_obj.save_as_from_application_menu(g_var.current_test_case)
        utillobj.capture_screenshot('14.00', step14)
        
        step15=""" Step 15: Logout using API
                    http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
        utillobj.capture_screenshot('15.00', step15)
         
        step16=""" Step 16: Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
                    http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%2Fc8262023.fex
        """
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api(g_var.current_test_case.lower()+'.fex', tool='workbook')
        utillobj.capture_screenshot('16.00', step16)
         
        step17=""" Step 17: Verify restored successfully
        """
        utillobj.synchronize_until_element_is_visible("[id*='chartpreview'] .risers rect", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg='Step 17.01')
        designer_chart_obj.verify_y_axis_label_in_preview(['0', '5', '10', '15', '20', '25', '30'], msg='Step 17.02')
        designer_chart_obj.verify_x_axis_title_in_preview(['Product Category'], msg='Step 17.03')
        designer_chart_obj.verify_y_axis_title_in_preview(['PCT.CNT MODEL'], msg='Step 17.04')
        designer_chart_obj.verify_number_of_risers("[id*='chartpreview'] .risers rect", 1, 7, msg='Step 17.05')
        utillobj.capture_screenshot('17.00', step17)
        
        step18=""" Step 18: Right Click "PCT.CNT.Product, Category" >Aggregate
        """
        designer_chart_obj.select_query_bucket_field_context_menu('Vertical', 'PCT.CNT.Model', 'Aggregate', click_type=None)
        utillobj.capture_screenshot('18.00', step18)
        
        step19=""" Step 19: Verify "Percent of Count" option is selected
        """
        designer_chart_obj.verify_query_bucket_field_option_in_context_menu_checked(['Percent of count'], 'Step 19.01: Verify "Percent of Count" option is selected.')
        utillobj.capture_screenshot('19.00', step19)
        
        step20=""" Step 20: Logout using API
                    http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(2)
        utillobj.capture_screenshot('20.00', step20)
 
    if __name__ == "__main__":
        unittest.main()