'''
Developed By  : KK14897
Developed Date: 11-DEC-2018


Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6185736
TestCase Name = Enabling Path Enforcement in Document

'''
import unittest, time
from common.wftools import report
from common.lib.basetestcase import BaseTestCase

class C6185736_TestClass(BaseTestCase):
    
    def test_C6185736(self):
        
        report_obj=report.Report(self.driver)
        
        """    
            Step 01 : Create new report with employee using API call:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/employee&item=IBFS:/WFC/Repository/P292_S11397/G458325.
        """
        MASTER_FILE_NAME="ibisamp/employee"
        report_obj.invoke_ia_tool_using_new_api_login(tool='report', master=MASTER_FILE_NAME)
        
        """    
            Step 02 : Drag BANK_NAME into the Across in Query panel.
        """
        report_obj.drag_field_from_data_tree_to_query_pane("BANK_NAME", 1, "Across", 1)
        report_obj.wait_for_visible_text('#queryTreeColumn', 'BANK_NAME')
        
        """    
            Step 03 :Mouse hover data icon present in top of the Data panel.
            Verify tool tip appears as "Enable Path Enforcement".
        """
        
        report_obj.verify_datapane_toggle_button_tooltip_in_enablemode()
        
        """    
            Step 04 : Click data icon. 
            Verify fields which are not matching the path of the added field are grayed out in the Data panel   
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(5)
        report_obj.verify_grayedout_field_in_data_pane("Dimensions", "DAT_INC", 9, msg="Step 04.00: Verify Greayed out in Dimensions")        
       
        """    
            Step 05 : Double click DEPARTMENT and CURR_SAL.
            Verify able to add fields which are not grayed out.
        """
        report_obj.double_click_on_datetree_item("DEPARTMENT", 1)
        report_obj.wait_for_visible_text('#queryTreeColumn', 'DEPARTMENT')
        report_obj.double_click_on_datetree_item("CURR_SAL", 1)
        report_obj.wait_for_visible_text('#queryTreeColumn', 'CURR_SAL')
        report_obj.verify_field_in_querypane("By", "DEPARTMENT", 1, msg="Step 05.01:Verify fields added in query pane")
        
        """    
            Step 06 : Double click SKILLS and SALARY. 
            Verify unable to add fields which are grayed out.   
        """
        report_obj.double_click_on_datetree_item("SKILLS", 1)
        report_obj.double_click_on_datetree_item("SALARY", 1)
        report_obj.verify_all_fields_in_query_pane(['Report (employee)', 'Sum', 'CURR_SAL', 'By', 'DEPARTMENT', 'Across', 'BANK_NAME'], msg="Step 06.00 :Verify fields added in query pane")
        
        """    
            Step 07 : Replace BANK_NAME into the Across with EFFECT_DATE.   
            Verify fields which are not matching the path are still in grayed out state.   
        """
        report_obj.right_click_on_field_under_query_tree("BANK_NAME", 1, "Delete")
        report_obj.drag_field_from_data_tree_to_query_pane("EFFECT_DATE", 1, "Across", 1)
        report_obj.wait_for_visible_text('#queryTreeColumn', 'EFFECT_DATE')
        report_obj.verify_grayedout_field_in_data_pane("Dimensions", "DAT_INC", 9, msg="Step 07.01: Verify Greayed out in Dimensions")        

        """    
            Step 08 : Click data icon.   
            Verify all grayed fields in data panel are back to normal. 
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(5)
        report_obj.verify_grayedout_field_in_data_pane("Dimensions", "DAT_INC", 9, msg="Step 08.01: Verify grayed field in data panel is back to normal",color_to_verify='black')        
        
        """    
            Step 09 : Click Save in toolbar.
            Step 10 : Enter "C6185736" in Title.
            Step 11 : Click Save.    
        """
        report_obj.save_report_from_toptoolbar()
        report_obj.save_file_in_save_dialog('C6185736')
        
        """    
            Step 12 :Logout of the IA API using the following URL.
            http://machine:port/alias/service/wf_security_logout.jsp   
        """
        report_obj.api_logout()
        
        
if __name__ == '__main__':
    unittest.main()