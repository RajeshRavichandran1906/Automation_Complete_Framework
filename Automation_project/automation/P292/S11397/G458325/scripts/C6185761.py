'''
Developed By  : KK14897
Developed Date: 10-DEC-2018

Development in Progress

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6185761
TestCase Name = Enabling Path Enforcement in Document

'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import report,visualization
from common.pages import ia_resultarea

class C6185761_TestClass(BaseTestCase):
    
    def test_C6185761(self):
        
        report_obj=report.Report(self.driver)
        vis_obj=visualization.Visualization(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
            Testcase css
        """
        querytree_css = "#queryTreeWindow"
        
        """    
            Step 01 : Create new report with employee using API call:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/employee&item=IBFS:/WFC/Repository/P292_S11397/G458325.
        """
        MASTER_FILE_NAME="ibisamp/employee"
        report_obj.invoke_ia_tool_using_new_api_login(tool='document', master=MASTER_FILE_NAME)
        
        """    
            Step 02 : Double click BANK_NAME and SALARY.
        """
        report_obj.double_click_on_datetree_item("BANK_NAME", 1)
        report_obj.wait_for_visible_text(querytree_css, "BANK_NAME")
        report_obj.double_click_on_datetree_item("SALARY", 1)
        report_obj.wait_for_visible_text(querytree_css, "SALARY")
        
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
            Step 05 : Click Insert tab and select Chart.    
        """
        report_obj.select_ia_ribbon_item("Insert","Chart")
        report_obj.wait_for_number_of_element("#TableChart_2 rect[class*='riser']", 25)
        
        """    
            Step 06 : Drag and place new chart next to the report.    
        """
        ia_resultobj.drag_drop_document_component('#TableChart_1', '#TableChart_2', 70, 0)
        
        """    
            Step 07 : Double click DEPARTMENT and SALARY.    
        """
        time.sleep(5)
        report_obj.double_click_on_datetree_item("DEPARTMENT", 1)
        report_obj.wait_for_visible_text(querytree_css, "DEPARTMENT")
        report_obj.double_click_on_datetree_item("SALARY", 1)
        report_obj.wait_for_visible_text(querytree_css, "SALARY")
        report_obj.verify_grayedout_field_in_data_pane("Dimensions", "TYPE", 11, msg="Step 07.01 : Verify Greayed out in Dimensions")      
        report_obj.verify_grayedout_field_in_data_pane("Measures/Properties", "GROSS", 8, msg="Step 07.02: Verify Greayed out in Measures")
        
        """    
            Step 08 : Mouse hover data icon present in top of the Data panel.    
        """
        
        report_obj.verify_datapane_toggle_button_tooltip_in_disablemode()
        
        """    
            Step 09 : Click data icon.    
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(3)
        report_obj.verify_grayedout_field_in_data_pane("Dimensions", "DAT_INC", 9, msg="Step 09.01 : Verify Greayed out in Dimensions",color_to_verify='black')        
        report_obj.verify_grayedout_field_in_data_pane("Measures/Properties", "PCT_INC", 5, msg="Step 09.02 : Verify Greayed out in Measures",color_to_verify='black')
        
        """    
            Step 10 : Click Save in toolbar.
            Step 11 : Enter "C6185761" in Title.
            Step 12 : Click Save.    
        """
        vis_obj.save_visualization_from_top_toolbar("C6185761")
        
        """    
            Step 13 :Logout of the IA API using the following URL.
            http://machine:port/alias/service/wf_security_logout.jsp   
        """
        report_obj.api_logout()
        
        
if __name__ == '__main__':
    unittest.main()