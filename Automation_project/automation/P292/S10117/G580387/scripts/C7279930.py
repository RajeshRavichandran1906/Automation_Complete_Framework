'''
Created on Jun 15, 2019

@author: Sudhan/Pearlson Joyal

Test Case : http://172.19.2.180/testrail/index.php?/cases/view/7279930
TestCase Name : Auto Drill with Group created from a hierarchy field prior to setting Auto Drill
'''
import unittest,time
from common.wftools import report
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods

class C7279930_TestClass(BaseTestCase):

    def test_C7279930(self):
        """
            CLASS OBJECTS 
        """
        report_obj = report.Report(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
       
        """
            TESTCASE Variables
        """
        querypane_css = "#queryBoxColumn"
        format_css = "#FormatTab"
        case_id = "C7279930"
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        DATA_SET_NAME2 = case_id + '_DataSet_02.xlsx'
        
        """
        STEP 1 : Reopen the saved fex using API link:
                 http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/IA-Shell.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url("IA-Shell")
        report_obj.wait_for_visible_text("#TableChart_1", "Sale")   
      
        """      
        STEP 2 : Right click 'Store Business Region' in the canvas and Click 'Create Group...' option.
        """
        report_obj.select_preview_report_context_menu(25, "Create Group...")
        report_obj.wait_for_visible_text("#dynaGrpsCancelBtn", "Cancel")
      
        """
        STEP 3 : Enter 'BUSINESS_GROUP' in Field Textbox and Multi-Select 'North America' and 'South America'.
        """
        report_obj.group_dialog().enter_values_in_field_textbox("BUSINESS_GROUP")
        report_obj.group_dialog().select_multiple_fields(['North America','South America'])
        
        """
        STEP 4 : Click 'Group' and Click 'OK' button.
        """      
        report_obj.group_dialog().click_group_button()
        time.sleep(3) #added time for group to be processed
        report_obj.group_dialog().click_ok_button()
             
        """
        5 : Right click "BUSINESS_GROUP" in the Canvas and Click "Change Title" option..
        """
        report_obj.select_preview_report_context_menu(25, "Change Title...")
        report_obj.wait_for_visible_text("div[id^='BiOptionPane']", "Cancel")
                 
        """
        6 : Enter "Store,Business,Group" and Click "OK" button.
        """
        title_textbox = self.driver.find_element_by_css_selector("[id^='BiDialog'] input.bi-text-field")
        title_textbox.clear()
        title_textbox.send_keys("Store,Business,Group")
        click_button = self.driver.find_element_by_xpath("//div[contains(@id, 'BiDialog')]//div[normalize-space() = 'OK']")
        core_utils.left_click(click_button)
         
        """
        7 : Click "Format tab" and Click "Auto Drill"option.
        """
        report_obj.wait_for_visible_text("#FormatTab_tabButton", "Format")
        report_obj.select_ia_ribbon_item('Format','auto_drill')
        report_obj.wait_for_visible_text(format_css, "Features")
        
        """
        8 : Click "Run" in toolbar.
        """
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        report_obj.wait_for_number_of_element("iframe[src*='contentDrill']",1)
        report_obj.switch_to_frame("iframe[src*='contentDrill']")
        report_obj.wait_for_visible_text("table[summary='Summary']>tbody>tr:nth-child(1)", "Sale,Year",120)
        
        """
        8.01 : Check the following Output.
        """
        #report_obj.create_html_report_dataset(DATA_SET_NAME1)
        report_obj.verify_html_report_dataset(DATA_SET_NAME1,"Step 8.01 : verify report data")
        
        """
        9 : Click on "North America" and "South America" Group.
        9.01 : Check "Drill down to Store Business Region" is displayed.
        10 : Click "Drill down to Store Business Region".
        """
        expected_tooltip = ["Drill down to Store Business Region"]
        msg = "Step 10.01 : Click Drill down to Store Business Region"
        report_obj.select_report_autolink_tooltip_runtime("table[summary='Summary']", 12, 1,"Drill down to Store Business Region", verify_tooltip=expected_tooltip, msg=msg, verify_type="asin")
        report_obj.wait_for_visible_text("table[summary]>tbody>tr:nth-child(1)", "North America and South America")
    
        """
        10.01 : Check the Breadcrumb and following Output.
        """
#         report_obj.create_html_report_dataset(DATA_SET_NAME2)
        report_obj.verify_html_report_dataset(DATA_SET_NAME2,"Step 10.01 : verify report data")
        
        """
        11 : Click on "North America".
        11.01 : Check both "Drill up to Store Business Group" and "Drill down to Store Business Sub Region" are displayed.
        """
        expected_tooltip = ["Go up to Store Business Group", "Drill down to Store Business Sub Region"]
        msg = "STEP 11.01 : Check both 'Drill up to Store Business Group' and 'Drill down to Store Business Sub Region' are displayed."
        report_obj.select_report_autolink_tooltip_runtime("table[summary='Summary']", 5, 1,"Drill down to Store Business Sub Region", verify_tooltip= expected_tooltip, msg=msg, verify_type="asin" )
        report_obj.wait_for_visible_text("table[summary]>tbody>tr:nth-child(1)", "North America")       
        
        """
        12 : Click "IA" menu and Select "Save As" option.
        13 : Enter "C7279930" in Title textbox and Click "Save" button.
        """
        report_obj.switch_to_default_content()
        report_obj.save_as_from_application_menu_item(case_id)
         
        """
        14 : Logout
             http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
         
        """
        15 : Reopen the saved fex using API link
             http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/C7279930.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(case_id)
        report_obj.wait_for_visible_text(querypane_css,"Product,Category")   
         
        """
        16 : Click "Format tab".
        """
        report_obj.switch_ia_ribbon_tab('Format')
        report_obj.wait_for_visible_text(format_css, "Features")
        
        """
        16.01: Check" Auto Drill" is still selected.
        """
        report_obj.verify_ribbon_item_selected("format_auto_drill", "16.01")
        
        """
        17 : Logout
             http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()