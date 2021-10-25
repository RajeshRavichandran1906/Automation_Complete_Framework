'''
Created on September 16, 2019

@author: AA14564.
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262022
TestCase Name = Edit format of measure for tooltip
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer_chart import Designer_Chart, Designer_calculation_edit_format
from common.lib import utillity
from common.lib import core_utility
from common.wftools import chart
from common.locators.designer_chart_locators import DesignerChart as dc_locators
from common.lib.global_variables import Global_variables

class C8262022_TestClass(BaseTestCase):
    
    def test_C8262022(self):
        """
        TESTCASE VARIABLES
        """
        
        utillobj = utillity.UtillityMethods(self.driver)
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        chart_obj = chart.Chart(self.driver)
        designer_chart_obj=Designer_Chart(self.driver)
        designer_format = Designer_calculation_edit_format(self.driver)
        project_id=core_utill_obj.parseinitfile('project_id')
        suite_id = core_utill_obj.parseinitfile('suite_id')
        group_id = core_utill_obj.parseinitfile('group_id')
        folder_name = project_id+'_'+suite_id+'/'+group_id
        g_var = Global_variables
        
        step1="""
        Step 1: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                http://domain.com:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774&tool=chart&master=baseapp/wf_retail_lite
        """
        designer_chart_obj.invoke_designer_chart_using_api("baseapp/wf_retail_lite")
        utillobj.synchronize_until_element_is_visible(dc_locators.DIMENSIONS_FIELD_AREA_CSS, designer_chart_obj.chart_long_timesleep)
        utillobj.capture_screenshot('01.00', step1)
  
        step2="""
        Step 2: Double click "Product,Category", "Discount" & "Quantity,Sold"
        """
        designer_chart_obj.double_click_on_dimension_field('Product->Product->Product,Category')
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box", "Product,Category", designer_chart_obj.home_page_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('Sales->Discount')
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box", "Discount", designer_chart_obj.home_page_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('Sales->Quantity,Sold')
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box", "Quantity,Sold", designer_chart_obj.home_page_medium_timesleep)
        utillobj.capture_screenshot('02.00', step2)
        
        step3="""
        Step 3: Right click "Discount" > Format Data
        """
        designer_chart_obj.select_query_bucket_field_context_menu('Vertical', 'Discount', 'Format data', click_type=None)
        utillobj.capture_screenshot('03.00', step3)
        
        step4="""
        Step 4: Select Number Format > Type as "Floating Point "
        """
        utillobj.synchronize_with_visble_text(".pop-top", "Data type", designer_format.home_page_short_timesleep)
        designer_format.select_datatype_in_dialog('numeric')
        designer_format.select_datatype_in_numeric('decimal')
        utillobj.capture_screenshot('04.00', step4)
    
        step5="""
        Step 5: Uncheck "Show 1000 separator"
        """
        designer_format.select_checkbox_in_numeric('Show 1000 separator', 'uncheck')
        utillobj.capture_screenshot('05.00', step5)
           
        step6="""
        Step 6: Click OK.
        """
        designer_format.close_dialog('OK')
        utillobj.capture_screenshot('06.00', step6)
           
        step7="""
        Step 7: Right click Quantity,Sold > Format Data.
        """
        designer_chart_obj.select_query_bucket_field_context_menu('Vertical', 'Quantity,Sold', 'Format data', click_type=None)
        utillobj.capture_screenshot('07.00', step7)
         
        step8="""
        Step 8: Type as "Currency (local)" > Currency Symbol = Dollar ($)
        """
        utillobj.synchronize_with_visble_text(".pop-top", "Data type", designer_format.home_page_short_timesleep)
        designer_format.select_datatype_in_dialog('numeric')
        designer_format.select_datatype_in_numeric('currency')
        designer_format.select_currency_symbol_in_numeric('Dollar')
        utillobj.capture_screenshot('08.00', step8)
         
        step9="""
        Step 9: Click OK.
        """
        designer_format.close_dialog('OK')
        utillobj.capture_screenshot('09.00', step9)
         
        step10="""
        Step 10: Click Preview.
        """
        designer_chart_obj.click_toolbar_item("preview")
        utillobj.capture_screenshot('10.00', step10)
         
        step11=""" Step 11: Hover over Discount riser
                    Discount displays without commas and without dollar sign
        """
        core_utill_obj.switch_to_frame("iframe[src*='TableChart_1']")
        utillobj.synchronize_until_element_is_visible("#jschart_HOLD_0 [class='riser!s0!g2!mbar!']", designer_chart_obj.home_page_long_timesleep)
        chart_obj.verify_tooltip_in_run_window('riser!s0!g3!mbar', ['Product Category:Media Player', 'Discount:11519142.41'], msg="Step 11.00 : Verify Discount displays without commas and without dollar sign")
        utillobj.capture_screenshot('11.00', step11)
         
        step12=""" Step 12: Hover over Quantity,Sold riser
                    Quantity,Sold displays with dollar sign and 2 decimal points
        """
        chart_obj.verify_tooltip_in_run_window('riser!s1!g3!mbar', ['Product Category:Media Player', 'Quantity Sold:$771,934.00'], msg="Step 12.00 : Verify Quantity,Sold displays with dollar sign and 2 decimal points")
        utillobj.capture_screenshot('12.00', step12, expected_image_verify=True)
         
        step13=""" Step 13: Click Save in the toolbar > Save as "C8262022" > Click Save
        """
        core_utill_obj.switch_to_default_content()
        designer_chart_obj.go_back_to_design_from_preview()
        designer_chart_obj.save_as_from_application_menu(g_var.current_test_case)
        utillobj.capture_screenshot('13.00', step13)
         
        step14=""" Step 14: Logout using API
                    http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
        utillobj.capture_screenshot('14.00', step14)
        
        step15=""" Step 15: Run from bip
                    http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S28313%2FG671774&BIP_item=C8262022.fex
        """
        chart_obj.run_fex_using_api_url(folder_name, g_var.current_test_case.lower(), "mrid", "mrpass")
        utillobj.synchronize_until_element_is_visible("#jschart_HOLD_0 [class='riser!s0!g2!mbar!']", designer_chart_obj.home_page_long_timesleep)
        utillobj.capture_screenshot('15.00', step15)
        
        step16=""" Step 16: Hover over risers
        """
        chart_obj.verify_tooltip_in_run_window('riser!s0!g3!mbar', ['Product Category:Media Player', 'Discount:11519142.41'], msg="Step 16.00 : Verify Discount displays without commas and without dollar sign")
        chart_obj.verify_tooltip_in_run_window('riser!s1!g3!mbar', ['Product Category:Media Player', 'Quantity Sold:$771,934.00'], msg="Step 16.01 : Verify Quantity,Sold displays with dollar sign and 2 decimal points")
        utillobj.capture_screenshot('16.00', step16, expected_image_verify=True)
        
        step17=""" Step 17: Logout using API
                    http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(2)
        utillobj.capture_screenshot('17.00', step17)
 
    if __name__ == "__main__":
        unittest.main()