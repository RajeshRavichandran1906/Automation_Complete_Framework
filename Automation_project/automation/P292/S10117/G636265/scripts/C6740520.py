"""-------------------------------------------------------------------------------------------
Created on June 10, 2019
@author: Aftab/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22268763
Test Case Title =  Prompt for numeric field
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.lib import global_variables
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
import time

class C6740520_TestClass(BaseTestCase):

    def test_C6740520(self):
        
        """
            CLASS OBJECTS 
        """
        report_obj = report.Report(self.driver)
        global_var_obj = global_variables.Global_variables()
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        case_id = global_var_obj.current_test_case
        live_preview_css = "#TableChart_1"
        qwery_css = "#queryBoxColumn"
        cancel_css = "#dlgWhere_btnCancel"
        resultarea_css = "table[summary]"
        filter_css = "[id^='wndWhere'][id$='Popup']:not([style*='hidden']) #metaDataBrowser [id^='WhereMetaDataTree']>div[class='bi-tree-view-body']"
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        
        """
            STEP 1 : Create new IA report using wf_retail_lite mas file using API:
        """
        report_obj.invoke_ia_tool_using_new_api_login(master = 'baseapp/wf_retail_lite')
        report_obj.wait_for_visible_text(live_preview_css, "Drag and drop")

        """
            STEP 2 : Double click add "Product,Category" and "Revenue" fields
        """
        report_obj.double_click_on_datetree_item("Product,Category", 1)
        report_obj.wait_for_visible_text(qwery_css, "Product,Category")
        
        report_obj.double_click_on_datetree_item("Revenue", 1)
        report_obj.wait_for_visible_text(qwery_css, "Revenue")

        """
            STEP 3 : Right click on "Gross Profit" from tree and select Sort;Gross profit will be added as the second BY filed
        """
        report_obj.select_datatree_field_context_menu("Gross Profit", "Sort")
        report_obj.wait_for_visible_text(qwery_css, "Gross Profit")
        
        """
            STEP 4 : Drag "Gross Profit" field to the Filter pane
        """
        report_obj.drag_and_drop_from_data_tree_to_filter("Gross Profit", 1)
        report_obj.wait_for_visible_text(cancel_css, "Cancel")
        
        """
            STEP 5 : Select Parameter in Type drop down
        """
        report_obj.open_filter_where_value_dialog()
        report_obj.select_filter_type("Parameter")
        
        """
            STEP 6 : Select Dynamic radio button and select "Gross Profit" in field list;Click OK
        """
        report_obj.select_filter_parameter_type("Dynamic")
        time.sleep(3)
        if global_variables.Global_variables.browser_name in ['chrome', 'cr'] :
            scroll_obj = utils.validate_and_get_webdriver_object(filter_css, "Filter css")
            utils.scroll_down_on_element(scroll_obj, 5)
            time.sleep(3)
            sales_obj = utils.validate_and_get_webdriver_object("div[id^='WhereMetaDataTree']> div.bi-tree-view-body-content > table > tbody > tr:nth-child(4) img", "sales css")
            core_utils.python_left_click(sales_obj)
            utils.scroll_down_on_element(scroll_obj, 4)
            time.sleep(3)
            gross_profit_obj = self.driver.find_element_by_xpath("//div[contains(@id, 'dlgWhereValue')]//*[contains(text(), 'Gross Profit')]")
            core_utils.python_left_click(gross_profit_obj)
            time.sleep(3)
        else:
            report_obj.select_field_in_filter_tree("Measure Groups->Sales->Gross Profit", 1)
        report_obj.close_filter_where_value_popup_dialog()

        """
            STEP 7 : Click OK in filtering condition dialog
        """
        report_obj.close_filter_dialog()
 
        """
            STEP 8 : Click Run in toolbar
        """ 
        report_obj.run_report_from_toptoolbar()
        
        """
            STEP 8.01 : Verify auto prompt window appears as below
        """
        report_obj.switch_to_frame()
        report_obj.verify_selected_field_dropdown_value_in_autoprompt("Gross Profit in US Currency:", "-$2,402.40", "STEP 8.01 : Verify auto prompt window appears as below")

        """
            STEP 9 : Click Run with filter values
        """
        report_obj.run_auto_prompt_report()
        
        """
            STEP 9.01 : Verify report appears as below
        """
        report_obj.switch_to_frame("iframe[name='wfOutput']")
        report_obj.wait_for_visible_text(resultarea_css, "Revenue")
        #report_obj.create_html_report_dataset(DATA_SET_NAME1)
        report_obj.verify_html_report_dataset(DATA_SET_NAME1, "STEP 9.01 : Verify report appears as below")
        report_obj.switch_to_default_content()

        """
            STEP 10 : Close IA without saving
        """
        report_obj.close_ia_without_save()
 
        """
            STEP 11 : Logout WF using API:
        """
        report_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()
        