'''
Developed By  : KK14897
Developed Date: 10-DEC-2018

Development in Progress

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6246600
TestCase Name = Enabling Path Enforcement in Document

'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import report,visualization

class C6246600_TestClass(BaseTestCase):
    
    def test_C6246600(self):
        
        report_obj=report.Report(self.driver)
        vis_obj=visualization.Visualization(self.driver)
        
        """    
            Step 01 : Create new report with employee using API call:
        """
        MASTER_FILE_NAME="ibisamp/employee"
        report_obj.invoke_ia_tool_using_new_api_login(master=MASTER_FILE_NAME)
        
        """    
            Step 02 : Add BANK_NAME into By.
        """
        report_obj.double_click_on_datetree_item("BANK_NAME", 1)
        
        """    
            Step 03 :Mouse hover data icon present in top of the Data panel.
        """
        
        report_obj.verify_datapane_toggle_button_tooltip_in_enablemode()
        
        """    
            Step 04 : Click data icon.    
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(3)
        report_obj.verify_grayedout_field_in_data_pane("Dimensions", "DAT_INC", 9, msg="Step 04.01 : Verify Greayed out in Dimensions")        
        report_obj.verify_grayedout_field_in_data_pane("Measures/Properties", "PCT_INC", 5, msg="Step 04.02 : Verify Greayed out in Measures")
        
        """    
            Step 05 : Click Save in toolbar.
            Step 06 : Enter "C6246600" in Title.
            Step 07 : Click Save.    
        """
        vis_obj.save_visualization_from_top_toolbar("C6246600")
#         report_obj.save_file_in_save_dialog("C6246600")
        
        """    
            Step 08 :Logout of the IA API using the following URL.
            http://machine:port/alias/service/wf_security_logout.jsp   
        """
        report_obj.api_logout()
        
        """    
            Step 09 :Reopen saved fex:
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S11397%2FG458325%2FC6246600.fex   
        """
        report_obj.edit_fex_using_api_url(folder_name="P292_S11397/G458325", fex_name="C6246600", mrid="mrid", mrpass="mrpass")
        report_obj.wait_for_visible_text('#iaMetaDataBox', "DAT_INC")
        report_obj.verify_grayedout_field_in_data_pane("Dimensions", "DAT_INC", 9, msg="Step 09.01 : Verify Greayed out in Dimensions")        
        report_obj.verify_grayedout_field_in_data_pane("Measures/Properties", "PCT_INC", 5, msg="Step 09.02 : Verify Greayed out in Measures")
        
        """    
            Step 10 : Mouse hover data icon present in top of the Data panel.    
        """
        report_obj.verify_datapane_toggle_button_tooltip_in_disablemode()
        
        """    
            Step 11 : Click data icon.    
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(3)
        report_obj.verify_grayedout_field_in_data_pane("Dimensions", "DAT_INC", 9, msg="Step 11.01 : Verify Greayed out in Dimensions",color_to_verify='black')        
        report_obj.verify_grayedout_field_in_data_pane("Measures/Properties", "PCT_INC", 5, msg="Step 11.02 : Verify Greayed out in Measures",color_to_verify='black')
        
        """    
            Step 12 : Click Save.    
        """
        report_obj.save_report_from_toptoolbar()
        report_obj.click_any_bibutton_in_dialog("div[id^='BiDialog']", "OK")
       
        """    
            Step 13 :Logout of the IA API using the following URL.
            http://machine:port/alias/service/wf_security_logout.jsp   
        """
        report_obj.api_logout()
        
        """    
            Step 14 :Reopen saved fex:
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S11397%2FG458325%2FC6246600.fex   
        """
        report_obj.edit_fex_using_api_url(folder_name="P292_S11397/G458325",fex_name="C6246600", mrid="mrid", mrpass="mrpass")
        report_obj.wait_for_visible_text('#iaMetaDataBox', "DAT_INC")
        report_obj.verify_grayedout_field_in_data_pane("Dimensions", "DAT_INC", 9, msg="Step 14.01 : Verify Greayed out in Dimensions",color_to_verify='black')        
        report_obj.verify_grayedout_field_in_data_pane("Measures/Properties", "PCT_INC", 5, msg="Step 14.02 : Verify Greayed out in Measures",color_to_verify='black')
        
        """    
            Step 15 :Logout of the IA API using the following URL.
            http://machine:port/alias/service/wf_security_logout.jsp   
        """
        report_obj.api_logout()
        
        
if __name__ == '__main__':
    unittest.main()