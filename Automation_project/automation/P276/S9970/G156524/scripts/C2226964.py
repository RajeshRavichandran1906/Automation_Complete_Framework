'''
Created on 13-Mar-2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226964
TestCase Name = Test that a non-hierarchy field used as a sorting field will not be active for Drill down
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, ia_run, active_miscelaneous, ia_ribbon
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2226964_TestClass(BaseTestCase):
    
    def test_C2226964(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2226964"
        Test_Case_ID = Test_ID+"_"+browser_type
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_until_element_is_visible("#TableChart_1", 190)
        
        """    2. Drag Product,Category (Product > Product > Product,Category) into the filter pane 
                > Click Type drop down and select Parameter > Click Dynamic radio button 
                > Check off the "Select multiple values at runtime" option.
                Click OK twice to close the dialogues    
        """
        metaobj.drag_drop_data_tree_items_to_filter('Product,Category', 1)
        utillobj.synchronize_until_element_is_visible("#dlgWhere #dlgWhereWhereTree table tr:nth-child(2) span[class*='selected']>span>span", 190)
        condition_elem=utillobj.validate_and_get_webdriver_objects("#dlgWhere #dlgWhereWhereTree table tr:nth-child(2) span[class*='selected']>span>span", 'Filter dialog')
        core_util_obj.python_left_click(condition_elem[-1])
        time.sleep(5)
        core_util_obj.python_doubble_click(condition_elem[-1])
        time.sleep(3)
        utillobj.synchronize_with_number_of_element("[id^='InlineControlValue']>div[id^='BiButton']", 1, 90)
        btn_obj = utillobj.validate_and_get_webdriver_object("[id^='InlineControlValue']>div[id^='BiButton']", 'drop down')
        core_util_obj.left_click(btn_obj)
        utillobj.synchronize_with_visble_text("#dlgWhereValue_tbuttonGetValue", 'Get Values', 180)
        time.sleep(2)
        utillobj.select_combobox_item('id_wv_combo_type', 'Parameter')
        time.sleep(3)
        value_box = utillobj.validate_and_get_webdriver_object("#dlgWhereValue_rbParamDynamic input", 'Input box')
        core_util_obj.left_click(value_box)
        time.sleep(3)
        core_util_obj.left_click(utillobj.validate_and_get_webdriver_object("#dlgWhereValue_chkParamMultiple", 'Multiple'))
        time.sleep(3)
        elem1 = utillobj.validate_and_get_webdriver_object("#wndWhereValuePopup_btnOK img", 'Ok button')
        core_util_obj.left_click(elem1)
        time.sleep(3)
        ia_ribbonobj.close_filter_dialog()
        time.sleep(6)
        
        """    3. Click Format tab > Autodrill button     """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(4)
         
        """    4. Click Run    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_util_obj.switch_to_frame()
        time.sleep(3)
        
        """    5. From the Auto Prompt screen select Computers, Media Player and Stereo systems    """
        iarun.select_amper_value('Product Category', ['Computers','Media Player','Stereo Systems'],False)
        time.sleep(3)
        
        """    6. Click the run button from the Auto Prompt panel    """
        iarun.select_amper_menu('Run')
        time.sleep(20)
        core_util_obj.switch_to_frame(frame_css='iframe[name="wfOutput"]')
        core_util_obj.switch_to_frame(frame_css='iframe[src]')
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 06a: verify Auto Drill, drill down data set", desired_no_of_rows=15)
        time.sleep(5)
        
        """    7. Click on North America and Select "Drill down to Store Business Sub Region"     """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",8,1,'Drill down to Store Business Sub Region')
        time.sleep(10)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 07a: Verify that Autoprompt does not re-prompt on drill down", desired_no_of_rows=15)
        core_util_obj.switch_to_default_content()
        core_util_obj.switch_to_frame()
        time.sleep(2)
        core_util_obj.switch_to_frame(frame_css='iframe[name="wfOutput"]')
        core_util_obj.switch_to_frame(frame_css='iframe[src]')
        
        """    8. Click on Canada and select "Restore Original"    """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",5,1,'Restore Original')
        time.sleep(10)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 08a: verify Auto Drill, drill down data set", desired_no_of_rows=15)
        core_util_obj.switch_to_default_content()
        
        """    9. Click IA > Save As> Type C2226964a > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_a")
        time.sleep(5)
        
        """    10. Right click on the filter and select Exclude    """
        metaobj.filter_tree_field_click("Product,Category Equal to Multiselect Dynamic Parameter (Name: PRODUCT_CATEGORY, Field: PRODUCT_CATEGORY in WF_RETAIL_LITE) Sort Ascending", 1, 1, "Exclude")
        time.sleep(10)
        
        """    11. Click RUN. You should not be prompted and the entire report should appear without any filtering    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", "Step 11a: verify Auto Drill, drill down data set", desired_no_of_rows=15)
        time.sleep(5)
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        
        """    12. Open saved fex. Do NOT save the last changes if prompted: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226964a.fex&tool=report    """
        ribbonobj.select_tool_menu_item('menu_close')
        time.sleep(8)
        core_util_obj.left_click(utillobj.validate_and_get_webdriver_object("#saveAllDlg #btnNo", 'No button'))
        time.sleep(8)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID + "_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        """    13. Click format tab and Verify that Auto Drill is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled = utillobj.get_element_attribute(utillobj.validate_and_get_webdriver_object("#FormatAutoDrill", 'Auto Dirll'), 'disabled')                
        utillobj.asequal(disabled, None, "Step 13a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
        
        """    14. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(20)
        
        """    15. Click Run    """
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(10)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        
        """    16. From the Auto Prompt screen select Computers, Media Player and Stereo systems    """
        iarun.select_amper_value('Product Category', ['Computers','Media Player','Stereo Systems'],False)
        time.sleep(3)
        
        """    17. Click the run button from the Auto Prompt panel    """
        iarun.select_amper_menu('Run')
        time.sleep(20)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[name="wfOutput"]')
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '12of12records,Page1of1', 'Step 17a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 17b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', 'Step 17c: Verify the report data ')
        utillobj.switch_to_default_content(3)
        utillobj.switch_to_frame(1)
        time.sleep(2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[name="wfOutput"]')
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        
        """    18. Click on North America and Select "Drill down to Store Business Sub Region"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 3, 0, 'Drill down to Store Business Sub Region')
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '24of24records,Page1of1', 'Step 18a: Verify the Report Records')
        column_list=['Store Business Sub Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 18b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx', 'Step 18c: Verify the report data ')
        utillobj.switch_to_default_content(3)
        
        """    19. Click IA > Save As> Type C2226964b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_b")
        time.sleep(5)
        
        """    20. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226964b.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID + "_b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_until_element_is_visible('#TableChart_1', 190)
        time.sleep(8)
         
        """    21. Click format tab and see Autodrill button should be active    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled = utillobj.get_element_attribute(utillobj.validate_and_get_webdriver_object("#FormatAutoDrill", 'Dill down'), 'disabled')                
        utillobj.asequal(disabled, None, "Step 21a: Active_Report - Verify Autodrill button should be active")
                
        """    22. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()
