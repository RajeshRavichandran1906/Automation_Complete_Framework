'''
Created on Nov 15, 2018

@author: Robert

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/C742429
TestCase Name = Verify simple prompt
'''

import unittest, time
from common.wftools import report
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity

class C6742429_TestClass(BaseTestCase):

    def test_C6742429(self):
        
        """Testcase variables"""
        Test_Case_ID = "C6742429"
        report_obj=report.Report(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        
        field_css="div[class='autop-amper-ctrl-container'] div[class^='autop-amper']"
        medium_wait=60
        coln_list = ['Product', '', 'Category', 'Revenue']
        filterdialog_css = "#dlgWhere [class*='active'] [class*='caption'] [class*='bi-label']"
        expected_value_list=['Blu Ray', 'Boom Box', 'Charger', 'CRT TV', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'iPod Docking Station', 'Portable TV', 'Professional', 'Receivers', '', '', '', '', '', '', '']
        drop_down_list="div[class*='popup-container'][style*='max-width'] #av_grp_values"
        
        """
        Step 01: Create new IA report using WF_retail_lite
        http://machine:port/alias/ia?is508=false&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10117%2FG456746&tool=report&master=baseapp/wf_retail_lite
        """
        
        report_obj.invoke_ia_tool_using_new_api_login('report','baseapp/wf_retail_lite')
         
        """
        Step 02: Double click "Product,Category" and "Revenue" fields.
        """
        report_obj.double_click_on_datetree_item("Dimensions->Product->Product->Product,Category", 1)
        report_obj.double_click_on_datetree_item("Measure Groups->Sales->Revenue", 1)
        
         
        """
        Step 02.1: Verify the following report is displayed.
        """
        #utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 18, 60)
        utillobj.synchronize_with_visble_text("#TableChart_1 div[class^='x']:nth-of-type(5)", 'Revenue', 30, 1)
        report_obj.verify_report_column_titles_on_preview(4, 4, coln_list)
        
        """
        Step 03. Drag "Product,Category" field into the Filter pane.
        """   
        report_obj.collapse_datatree_field_section('Sales')
        report_obj.drag_and_drop_from_data_tree_to_filter('Product,Subcategory', 1)     
         
        """
        Step 03.1: Verify Create a filtering condition window opens.
        """   

        utillobj.synchronize_with_number_of_element(filterdialog_css, 1, medium_wait)
        utillobj.verify_object_visible(filterdialog_css, True, 'Step 03.1: Verify Create a filtering condition window appears.')
        
         
        """
        Step 04: Select Parameter in Type dropdown and select Dynamic raedio button and click OK and OK.
        """ 
        
        report_obj.select_filter_type('Parameter')
        report_obj.select_filter_parameter_type('Dynamic')
        report_obj.close_filter_where_value_popup_dialog()
        report_obj.close_filter_dialog()
        
        
        """
        Step 05: Click Run in toolbar.
        """ 
        report_obj.run_report_from_toptoolbar()
        utillobj.switch_to_frame(pause=4)
        
        
        """
        Step 05.1: Verify report run successfully with Autoprompt.
        """ 
        utillobj.synchronize_with_number_of_element(field_css, 1, medium_wait)
        utillobj.verify_object_visible(field_css, True, 'Step 5.1: Verify Autoprompt window appears with simple filter prompt')
        
        """
        Step 06: Click Product Subcategory: dropdown.
        Step 06.1. Verify dropdown is visible with longer list.
        """ 
        time.sleep(2)
        report_obj.select_field_filter_values_dropdown_in_auto_prompt('Product Subcategory')
        report_obj.verify_input_type_field_filter_values_in_auto_prompt(expected_value_list, 'Step 6. Verify the filter values list')
        
        """
        Step 07. Scroll down and select Smartphone in dropdown and click Run with filter values.
        """        
        web_element=utillobj.validate_and_get_webdriver_object(drop_down_list, 'List_object')
        utillobj.click_on_screen(web_element, 'middle', click_type=3)
        time.sleep(2)

        utillobj.mouse_scroll('down', 10)
        report_obj.select_input_single_field_filter_value_in_auto_prompt(['Smartphone'])
        
        
        report_obj.run_auto_prompt_report()
        
        utillobj.switch_to_frame(pause=5,frame_css='.autop-wf-output')
        #WebDriverWait(self.driver, synchronize_time).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[name="wfOutput"]')))
        
        """
        Step 07.1: Verify report run successfully.
        """ 
        report_obj.verify_table_data_set('body table', Test_Case_ID+'_Ds02.xlsx', 'Step 7. Verify output')
        #         iarun.create_table_data_set("table[summary= 'Summary']", Test_Case_ID+'_Ds02.xlsx')
        
        
        """
        Step 08: Logout WF using API: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """ 
        
if __name__ == '__main__':
    unittest.main()
