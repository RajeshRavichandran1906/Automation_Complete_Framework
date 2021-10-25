'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226969
TestCase Name = Test that Auto Drill works with Group created from a hierarchy field after setting Auto Drill
'''
import unittest, time
from common.pages import ia_run, active_miscelaneous, visualization_metadata
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables
from common.wftools.report import Report

class C2235748_TestClass(BaseTestCase):
    
    def test_C2235748(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type = Global_variables.browser_name
        Test_ID="C2235748"
        Test_Case_ID = Test_ID+"_"+browser_type
        iarun=ia_run.IA_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        report_ = Report(self.driver)
        
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        
        report_.edit_fex_using_api_url("IA-Shell", folder_name= "P276/S9970")
        utillobj.wait_for_page_loads(report_.report_long_timesleep)
        utillobj.synchronize_with_visble_text("#TableChart_1", "Sale,Year", report_.report_long_timesleep)
        
        """    2. Click Format tab > Autodrill button     """
#         time.sleep(15)  # giving time to click format properly
        time.sleep(5)  # giving time to click format properly
        report_.switch_ia_ribbon_tab('Format') #click format properly
        time.sleep(10)
        report_.select_ia_ribbon_item("Format", "auto_drill")
        utillobj.synchronize_with_number_of_element("[id='FormatAutoDrill'][class*='checked']", 1, 30)
        
        """    3. Right click on Store Business Region on the canvas and select 'Create Group...'    """
        metaobj.querytree_field_click("Store,Business,Region", 1, 1, "Create Group...")
        utillobj.synchronize_with_visble_text('#dynaGrpsCancelBtn', 'Cancel', report_.report_long_timesleep)
        
        """    4. Change the Field name to "BUSINESS_GROUP". Multi select both North America and South America using CTRL key.
                Click on "Group" in the upper left of the dialog. Click OK to close the dialog.    """
        
        metaobj.create_ia_group('Group', ['North America', 'South America'], change_field_txt='BUSINESS_GROUP', close_button='ok')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(6)", "BUSINESS_GROUP", 40)
        
        """    5. Right click on BUSINESS_GROUP on the canvas and select "Change Title". Enter "Store,Business,Group" and click OK to close.    """
        metaobj.querytree_field_click("BUSINESS_GROUP", 1, 1, "Change Title...")
        utillobj.synchronize_with_visble_text("div[id*='BiDialog']", "OK", report_.report_long_timesleep)
        edit_title_css="div[id^='BiDialog'][tabindex='0']"
        edit_title_obj=self.driver.find_element_by_css_selector(edit_title_css)
        utillobj.set_text_to_textbox_using_keybord('Store,Business,Group', text_box_elem=edit_title_obj.find_element_by_css_selector("input"))
        utillobj.click_dialog_button(edit_title_css,"OK")
        time.sleep(4)
        
        """    6. Click RUN     """
        report_.run_report_from_toptoolbar()
        utillobj.wait_for_page_loads(report_.home_page_long_timesleep)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 06.01: Verify the Data set", desired_no_of_rows=15)
        
        """    7. Click on Click on North America and South America Group    """        
        """    8. Select "Drill down to Store Business Region"    """
        expected_tooltip_list = ['Drill down to Store Business Region']
        iarun.select_report_autolink_tooltip("table[summary='Summary']",12,1,'Drill down to Store Business Region', expected_tooltip_list, msg="Step 07.01: Verify the menu shows 'Drill down to Store Business Region", verify_type='asequal')
        utillobj.wait_for_page_loads(200)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 08.01: Verify Drill down to Store Business Sub Region data set", desired_no_of_rows=15)
        time.sleep(4)
        
        """    9. Click on North America.    """
        expected_tooltip_list = ['Reset', 'Go up to Store Business Group', 'Drill down to Store Business Sub Region']
        iarun.verify_autolink_tooltip_values_usng_pyautogui("table[summary='Summary']",5,1, expected_tooltip_list, "Step 09.01: Verify the menu shows 'Drill down to Store Business Region'")
        utillobj.switch_to_default_content(1)
        time.sleep(2)
        
        """    10. Click IA > Save As> Type C2235748a > click Save    """
        report_.save_as_from_application_menu_item(Test_Case_ID + "_a")
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    11. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2235748a.fex&tool=report    """
        utillobj.infoassist_api_edit(Test_Case_ID + "_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.wait_for_page_loads(report_.home_page_long_timesleep)
        utillobj.synchronize_with_visble_text("#TableChart_1", "Sale,Year", report_.report_long_timesleep)
        
        """    12. Click format tab and Verify Autodrill button is still selected    """
        time.sleep(13)  # giving time to click format properly
        report_.switch_ia_ribbon_tab('Format')
        utillobj.synchronize_with_visble_text('#FormatTab', 'Features', report_.report_short_timesleep)
        report_.verify_ribbon_item_is_enabled('format_auto_drill', '12.01')
        
        """    13. Click on HTML output format in status bar and select Active format    """
        report_.select_output_format_from_status_bar('HTML Analytic Document')
        
        """    14. Click RUN    """
        report_.run_report_from_toptoolbar()
        utillobj.wait_for_page_loads(report_.home_page_long_timesleep)
        utillobj.switch_to_frame(1)
        time.sleep(4)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '21of21records,Page1of1', 'Step 14.01: Verify the Report Records')
        column_list=['Store Business Group', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 14.02: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0okay r', Test_ID+'_Ds03.xlsx', desired_no_of_rows=15)
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', 'Step 14.03: Verify the report dataset', desired_no_of_rows=15)
        
        """    15. Click on North America and South America Group    """
        values=['Drill down to Store Business Region', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscelanousobj.verify_field_menu_items('ITableData0', 7, 0, values, "Step 15.01: Verify the menu ")
        
        """    16. Select "Drill down to Store Business Region"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7, 0, 'Drill down to Store Business Region')
        utillobj.wait_for_page_loads(180)
        miscelanousobj.verify_page_summary(0, '14of14records,Page1of1', 'Step 16.01: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 16.02: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', 'Step 16.03: Verify the report data')
        time.sleep(5)
        
        """    17. Click on North America.    """
        values=['Reset', 'Go up to Store Business Group', 'Drill down to Store Business Sub Region', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscelanousobj.verify_field_menu_items('ITableData0', 0, 0, values, "Step 17.01: Verify the menu ")
        time.sleep(4)
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        
        """    18. Click IA > Save As> Type C2235748b > click Save    """
        report_.save_as_from_application_menu_item(Test_Case_ID + "_b")
        time.sleep(4)
        
        """    19. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226964b.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID + "_b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.wait_for_page_loads(report_.report_long_timesleep)
        utillobj.synchronize_with_visble_text("#TableChart_1", "Sale,Year", report_.report_long_timesleep)
         
        """    20. Click format tab and see Autodrill button should be active    """
        time.sleep(15)  # giving time to click format properly
        report_.switch_ia_ribbon_tab('Format')
        utillobj.synchronize_with_visble_text('#FormatTab', 'Features', report_.report_short_timesleep)
        report_.verify_ribbon_item_is_enabled('format_auto_drill', '20.01')
        
        """    21. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()