'''
Developed By  : KK14897
Developed Date: 05-DEC-2018

Development in Progress

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6246604
TestCase Name = Enabling Path Enforcement using Chart

'''
import unittest,time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.wftools import report,visualization,chart

class C6246604_TestClass(BaseTestCase):
    
    def test_C6246604(self):
        
        chart_obj=chart.Chart(self.driver)
        report_obj=report.Report(self.driver)
        util_obj=utillity.UtillityMethods(self.driver)
        vis_obj=visualization.Visualization(self.driver)
        
        """    
            Step 01 : Create new report with employee using API call:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/employee&item=IBFS:/WFC/Repository/P292_S11397/G458325.
        """
        MASTER_FILE_NAME="ibisamp/employee"
        report_obj.invoke_ia_tool_using_new_api_login(tool="chart", master=MASTER_FILE_NAME)
        
        """    
            Step 02 : Add COURSE_CODE in Horizontal Axis.
        """
        chart_obj.double_click_on_datetree_item("COURSE_CODE", 1)
        
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
            Step 05 : Delete COURSE_CODE in Horizontal Axis.    
        """
        chart_obj.right_click_on_field_under_query_tree("COURSE_CODE", 1, "Delete")
        
        """    
            Step 06 : Right click COURSE_CODE select > Add to Query > Color.    
        """
        chart_obj.right_click_on_datetree_item("COURSE_CODE", 1, "Add To Query->Color")
        
        """    
            Step 07 : Double click BANK_NAME and CURR_SAL.    
        """
        chart_obj.double_click_on_datetree_item("BANK_NAME", 1)
        chart_obj.double_click_on_datetree_item("CURR_SAL", 1)
        util_obj.synchronize_with_number_of_element("#TableChart_1 [class*='riser!s0!g1!mbar!']", 1, 60)
        
        """    
            Step 08 : Click Save in toolbar.
            step 09 : Enter "C6246604" in Title
            step 10 : Click Save.    
        """
        vis_obj.save_visualization_from_top_toolbar("C6246604")
        
        """    
            Step 11 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp   
        """
        chart_obj.api_logout()
        
        """    
            Step 12 : Reopen saved fex:
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S11397%2FG458325%2FC6246604.fex
        """
        chart_obj.edit_fex_using_api_url(folder_name="P292_S11397/G458325", fex_name="C6246604")
        chart_obj.wait_for_visible_text('#iaMetaDataBox', "DAT_INC")
       
        """
        Verify fields not along with the accessible path are grayed out in data panel.
        """    
        report_obj.verify_grayedout_field_in_data_pane("Dimensions", "DAT_INC", 9, msg="Step 12.01: Verify Greayed out in Dimensions")        
        report_obj.verify_grayedout_field_in_data_pane("Measures/Properties", "PCT_INC", 5, msg="Step 12.02: Verify Greayed out in Measures")
        
        """    
            Step 13 : Click data icon.    
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(3)
        report_obj.verify_grayedout_field_in_data_pane("Dimensions", "DAT_INC", 9, msg="Step 13.01: Verify Greayed out in Dimensions", color_to_verify='black')        
        report_obj.verify_grayedout_field_in_data_pane("Measures/Properties", "PCT_INC", 5, msg="Step 13.02: Verify Greayed out in Measures", color_to_verify='black')
        
        """    
            Step 14 :Logout of the IA API using the following URL.
            http://machine:port/alias/service/wf_security_logout.jsp   
        """
        chart_obj.api_logout()
            
if __name__ == '__main__':
    unittest.main()