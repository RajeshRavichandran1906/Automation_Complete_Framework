'''
Created on Nov 19, 2018

@author: Robert

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/C742430
TestCase Name = Verify simple prompt
'''

import unittest, time
from common.wftools import report
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity

class C6742430_TestClass(BaseTestCase):

    def test_C6742430(self):
        
        """Testcase variables"""
        Test_Case_ID = "C6742430"
        report_obj=report.Report(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        #ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        
        field_css="div[class='autop-amper-ctrl-container'] div[class^='autop-amper']"
        medium_wait=60
        coln_list = ['Product', '', 'Category', 'Revenue']
        filterdialog_css = "#dlgWhere [class*='active'] [class*='caption'] [class*='bi-label']"
        
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
        Step 04: Select Parameter in Type dropdown and select Dynamic radio button and check "Select multiple values at run time" and click OK and OK.
        """ 
        
        report_obj.select_filter_type('Parameter')
        report_obj.select_filter_parameter_type('Dynamic')
        report_obj.select_filter_parameter_checkbox(ParamMultiple=True)
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
        Step 06.1. Verify dropdown is visible and All Values is selected.
        """ 
        time.sleep(2)
        
        report_obj.select_field_filter_values_dropdown_in_auto_prompt('Product Subcategory')
        utillobj.verify_element_text('.ui-radio-on', 'All Values', 'Step 6.1. Verify All Values is selected default')
        
        """
        Step 07. Click Select Values
        Step 07.1. Verify Search and available values are enabled.
        """
        report_obj.select_radio_button_in_auto_prompt_values('Select Values')
        
        search_box_elem=utillobj.validate_and_get_webdriver_object("#av_search", 'search_box')
        search_box_state=utillobj.get_element_attribute(search_box_elem, 'class')
        utillobj.as_notin('ui-state-disabled',search_box_state, 'Step 7. Verify Search is enabled')
        
        available_box_elem=utillobj.validate_and_get_webdriver_object(".autop-sav-values-container","available_box")
        available_box_state=utillobj.get_element_attribute(available_box_elem, 'class')
        utillobj.as_notin('ui-state-disabled',available_box_state, 'Step 7. Verify Available values are enabled')
                                                                    
        """
        Step 08. Enter 'S' in Search box.
        Step 08.1. Verify only matching values are visible.
        """
        report_obj.enter_value_search_textbox_popup_in_auto_prompt('S')
        expected_value_list=['Smartphone', 'Speaker Kits', 'Standard', 'Streaming']
        report_obj.verify_input_type_field_filter_values_in_auto_prompt(expected_value_list, 'Step8. Verify only matching values are displayed for text S')
        
        """
        Step 09. Click "All" in control.
        Step 09.1.Verify all available values are selected.
        """
        report_obj.select_value_button_in_auto_prompt('All')
        expected_value_list=['Smartphone', 'Speaker Kits', 'Standard', 'Streaming']
        
        report_obj.verify_field_filter_values_checked_property_in_auto_prompt(expected_value_list, 'Step 9. Verify field filter values are checked', 'checked')
        
        """
        Step 10. Click "None" in control.
        Step 10.1. Verify selected values are unchecked.
        """
        report_obj.select_value_button_in_auto_prompt('None')
        expected_value_list=['Smartphone', 'Speaker Kits', 'Standard', 'Streaming']
        
        report_obj.verify_field_filter_values_checked_property_in_auto_prompt(expected_value_list, 'Step 10. Verify field filter values are un-checked', 'unchecked')
        report_obj.select_auto_prompt_value_back_button()
        
        """
        Step 11. Click Run with filter values.
        Step 11.1. Verify report run successfully.
        """
        
        report_obj.run_auto_prompt_report()
        
        utillobj.switch_to_frame(pause=5,frame_css='.autop-wf-output')
        utillobj.synchronize_with_number_of_element("body > table > tbody td", 18, 30)
        report_obj.verify_table_data_set('body table', Test_Case_ID+'_Ds02.xlsx', 'Step 7. Verify output')
        #         iarun.create_table_data_set("table[summary= 'Summary']", Test_Case_ID+'_Ds02.xlsx')
        
        """
        Step 12: Logout WF using API: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """ 
        
if __name__ == '__main__':
    unittest.main()
