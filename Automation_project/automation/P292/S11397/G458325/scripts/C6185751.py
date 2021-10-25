'''
Developed By  : KK14897
Developed Date: 04-DEC-2018

Development in Progress

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6185751
TestCase Name = Enabling Path Enforcement in Visualization

'''
import unittest, time
from common.wftools import report
from common.lib.basetestcase import BaseTestCase

class C6185751_TestClass(BaseTestCase):
    
    def test_C6185751(self):
        
        """
            Class objects
        """
        report_obj=report.Report(self.driver)
        
        """
            Testcase variables
        """
        querytree_css = "#queryTreeWindow"
        MASTER_FILE_NAME="ibisamp/employee"
        
        """    
            Step 01 : Create new report with employee using API call:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/employee&item=IBFS:/WFC/Repository/P292_S11397/G458325.
        """
        report_obj.invoke_ia_tool_using_new_api_login(master=MASTER_FILE_NAME)
        
        """    
            Step 02 : Double click BANK_NAME.
        """
        report_obj.double_click_on_datetree_item("BANK_NAME", 1)
        report_obj.wait_for_visible_text(querytree_css, "BANK_NAME")
        
        """    
            Step 03 :Mouse hover data icon present in top of the Data panel.
        """
        
        report_obj.verify_datapane_toggle_button_tooltip_in_enablemode()
        
        """    
            Step 04 : Click data icon.    
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(3)
        report_obj.verify_grayedout_field_in_data_pane("Dimensions", "DAT_INC", 9, msg="Step 04.01: Verify Greayed out in Dimensions")        
        report_obj.verify_grayedout_field_in_data_pane("Measures/Properties", "PCT_INC", 5, msg="Step 04.02: Verify Greayed out in Measures")
        
        """    
            Step 05 : Add CURR_SAL to Vertical Axis.    
        """
        report_obj.double_click_on_datetree_item("CURR_SAL", 1)
        report_obj.wait_for_visible_text(querytree_css, "CURR_SAL")
        
        """    
            Step 06 : Double click "PAY_DATE" field.  
            Verify no changes takes place unable to add grayed out field.  
        """
        report_obj.double_click_on_datetree_item("PAY_DATE", 1)
        report_obj.verify_all_fields_in_query_pane(['Report (employee)', 'Sum', 'CURR_SAL', 'By', 'BANK_NAME', 'Across'],'Step 06.01: Verify unable to add Greayed out field')
               
        """    
            Step 07 : Mouse hover data icon present in top of the Data panel.    
        """
        report_obj.verify_datapane_toggle_button_tooltip_in_disablemode()
        
        """    
            Step 08 : Click data icon.    
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(4)
        report_obj.verify_grayedout_field_in_data_pane("Dimensions", "DAT_INC", 9, msg="Step 08.01: Verify Greayed out in Dimensions",color_to_verify='black')        
        report_obj.verify_grayedout_field_in_data_pane("Measures/Properties", "PCT_INC", 5, msg="Step 08.02: Verify Greayed out in Measures",color_to_verify='black')
        """    
            Step 09 : Click Save in toolbar.
            Step 10 : Enter "C6185751" in Title.
            Step 11 : Click Save.    
        """
        report_obj.save_report_from_toptoolbar()
        report_obj.save_file_in_save_dialog('C6185751')
        
        """    
            Step 12 :Logout of the IA API using the following URL.
            http://machine:port/alias/service/wf_security_logout.jsp   
        """
        
if __name__ == '__main__':
    unittest.main()