'''
Created on September 24, 2019

@author: AA14564.
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262024
TestCase Name = Create Datagrid Chart
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer_chart import Designer_Chart
from common.lib import utillity
from common.lib import core_utility
from common.locators.designer_chart_locators import DesignerChart as dc_locators
from common.lib.global_variables import Global_variables

class C8262024_TestClass(BaseTestCase):
    
    def test_C8262024(self):
        """
        TESTCASE VARIABLES
        """
        
        utillobj = utillity.UtillityMethods(self.driver)
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        designer_chart_obj=Designer_Chart(self.driver)
        g_var = Global_variables
        
        
        step1=""" Step 1: Launch the IA API with Chart (edit the domain, port and alias of the URL - do not use the URL as is):
                http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api("baseapp/wf_retail_lite")
        utillobj.synchronize_until_element_is_visible(dc_locators.DIMENSIONS_FIELD_AREA_CSS, designer_chart_obj.chart_long_timesleep)
        utillobj.capture_screenshot('01.00', step1)
   
        step2=""" Step 2: Select "DataGrid" from chart picker component.
        """
        designer_chart_obj.select_chart_from_chart_picker('datagrid')
        utillobj.synchronize_with_visble_text("[id*='chartpreview'] .title", "Drag fields here to create grid", designer_chart_obj.home_page_long_timesleep)
        utillobj.capture_screenshot('02.00', step2)
         
        step3=""" Step 3: Double click Product,Category
                Product Category is added to Rows bucket and shows in preview as first column.
        """
        designer_chart_obj.double_click_on_dimension_field('Product->Product->Product,Category')
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box", "Product,Category", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_values_in_querybucket('Row', ['Product,Category'], 'Step 03.00: Verify Product Category is added to Rows bucket.')
        utillobj.synchronize_with_visble_text("[id*='chartpreview'] .rowHeader", 'Accessories', designer_chart_obj.home_page_long_timesleep)
        grid_data = utillobj.validate_and_get_webdriver_object("[id*='chartpreview'] .rowHeader", 'grid data').text.strip().replace(' ','').split('\n')
        expected_data_list = ['Accessories', 'Camcorder', 'Computers', 'MediaPlayer', 'StereoSystems', 'Televisions', 'VideoProduction']
        utillobj.as_List_equal(expected_data_list, grid_data, 'Step 03.01: Verify Product Category shows in preview as first column.')
        utillobj.capture_screenshot('03.00', step3, expected_image_verify=True)
         
        step4=""" Step 4: Double click Cost of Goods, Discount, Gross Profit and Revenue
                All measures are added to Measures bucket and show as additional columns in preview.
        """
        designer_chart_obj.double_click_on_measures_field('Sales->Cost of Goods')
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box", "Cost of Goods", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.double_click_on_measures_field('Discount')
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box", "Discount", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.double_click_on_measures_field('Gross Profit')
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box", "Gross Profit", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.double_click_on_measures_field('Revenue')
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box", "Revenue", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_values_in_querybucket('Measure', ['Cost of Goods', 'Discount', 'Gross Profit', 'Revenue'], 'Step 04.00: Verify Product Category is added to Rows bucket.')
        utillobj.synchronize_with_visble_text("[id*='chartpreview'] .rowHeader", 'Accessories', designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_data_grid_set(str(g_var.current_test_case) + '_step_04', '04.01')
        utillobj.capture_screenshot('04.00', step4, expected_image_verify=True)
     
        step5=""" Step 5: Click More > Select "AutoDrill"
        """
        designer_chart_obj.select_more_option('AutoDrill')
        utillobj.capture_screenshot('05.00', step5)
            
        step6=""" Step 6: Click Preview icon from the toolbar.
                    Chart displayed in preview mode.
        """
        designer_chart_obj.click_toolbar_item("preview")
        utillobj.capture_screenshot('06.00', step6)
            
        step7=""" Step 7: Hover "Cost of Goods" value from Accessories.
        """
        core_utill_obj.switch_to_frame("iframe[src*='TableChart_1']")
        core_utill_obj.switch_to_frame("iframe[src*='contentDrill']")
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 .tablePanel", '$89,753,898.00', designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_data_grid_set(str(g_var.current_test_case) + '_step_04', '07.00')
        expected_tooltip_list = ['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Drill down to Product Subcategory']
        designer_chart_obj.verify_data_grid_tooltip('$89,753,898.00', expected_tooltip_list, 'Step 07.01: Verify Accessories tooltip value.')
        utillobj.capture_screenshot('07.00', step7, expected_image_verify=True)
          
        step8=""" Step 8: Hover blue icon from the center of the chart > click Return button.
        """
        core_utill_obj.switch_to_default_content()
        designer_chart_obj.go_back_to_design_from_preview()
        utillobj.capture_screenshot('08.00', step8)
          
        step9=""" Step 9: Click Save in the toolbar > Enter Title as "C8262024" > Click Save
        """
        designer_chart_obj.save_as_from_application_menu(g_var.current_test_case)
        utillobj.capture_screenshot('09.00', step9)
          
        step10="""
        Step 10: Logout using API
                http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
        utillobj.capture_screenshot('10.00', step10)
         
        step11=""" Step 11: Run the fex from domain tree using API (edit the domain, port and alias of the URL - do not use the URL as is):
                http://machine:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S28313%252FG671774%252F&BIP_item=c8262024.fex
        """
        designer_chart_obj.run_designer_chart_using_api(g_var.current_test_case.lower())
        core_utill_obj.switch_to_frame("iframe[src*='contentDrill']")
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 .tablePanel", '$89,753,898.00', designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_data_grid_set(str(g_var.current_test_case) + '_step_04', '11.00')
        utillobj.capture_screenshot('11.00', step11, expected_image_verify=True)
         
        step12=""" Step 12: Logout using API
                    http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
        utillobj.capture_screenshot('12.00', step12)
         
        step13=""" Step 13: Restore the C8262024.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
                http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%2Fc8262024.fex
        """
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api(g_var.current_test_case.lower()+'.fex', tool='workbook')
        utillobj.synchronize_with_visble_text("[id*='chartpreview'] .rowHeader", 'Accessories', designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_data_grid_set(str(g_var.current_test_case) + '_step_04', '13.00')
        utillobj.capture_screenshot('13.00', step13, expected_image_verify=True)
         
        step14=""" Step 14: Logout using API
                    http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
        utillobj.capture_screenshot('14.00', step14)
        
 
    if __name__ == "__main__":
        unittest.main()