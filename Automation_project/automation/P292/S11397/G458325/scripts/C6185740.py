'''
Developed By  : KK14897
Developed Date: 12-DEC-2018

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6185740
TestCase Name = Enabling Path Enforcement in Reporting Objects 

'''
import unittest ,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import report,visualization
from common.pages import wf_reporting_object
from common.lib import core_utility,utillity
from selenium.webdriver import ActionChains

class C6185740_TestClass(BaseTestCase):
    
    def test_C6185740(self):
        
        report_obj=report.Report(self.driver)
        vis_obj=visualization.Visualization(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        wfreportobj = wf_reporting_object.Wf_Reporting_Object(self.driver)
        actions = ActionChains(self.driver)
        
        """
            Testcase css
        """
        query_tree_css = "#queryTreeWindow"
    
        """    
            Step 01 : Create new report with employee using API call:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/employee&item=IBFS:/WFC/Repository/P292_S11397/G458325.
        """
        MASTER_FILE_NAME="ibisamp/employee"
        report_obj.invoke_ia_tool_using_new_api_login(tool='reportingobject', master=MASTER_FILE_NAME,report_css="#editorViewPane")
        
        """    
            Step 02 : Double click Chart in Reporting Object.
        """
        chart_obj = utillobj.validate_and_get_webdriver_object("#roTree table tbody tr:nth-child(8)", "Chart css")
        actions.double_click(chart_obj).perform()
        
        """ 
            Step 03 : Maximize ReportingObject chart window.
        """
        core_utility_obj.switch_to_new_window()
        report_obj.wait_for_visible_text("#pfjTableChart_2", "Group 0")
        
        """ 
            Step 04 : Double click DEPARTMENT and SALARY fields in data plane.
        """
        report_obj.double_click_on_datetree_item("DEPARTMENT", 1)
        report_obj.wait_for_visible_text(query_tree_css, "DEPARTMENT")
        
        report_obj.double_click_on_datetree_item("SALARY", 1)
        report_obj.wait_for_visible_text(query_tree_css, "SALARY")
        
        """    
            Step 05 : Mouse hover data icon present in top of the Data panel.
        """
        report_obj.verify_datapane_toggle_button_tooltip_in_enablemode()
        report_obj.wait_for_visible_text("#pfjTableChart_2 ", "SALARY")
        
        """    
            Step 06 : Click data icon.    
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(5) #firefox need time to avoid stale error
        report_obj.verify_grayedout_field_in_data_pane("Dimensions", "TYPE", 11, msg="Step 06.00: Verify Greayed out in Dimensions")        
#         report_obj.verify_grayedout_field_in_data_pane("Measures/Properties", "PCT_INC", 5, msg="Step 6: Verify Greayed out in Measures")
        
        """    
            Step 07 : Exit and Save.
        """
        report_obj.select_visualization_application_menu_item("exit")
        report_obj.ia_exit_save("Yes")
        core_utility_obj.switch_to_previous_window(window_close=False)
        
        """    
            Step 08 : Click Save in RO toolbar.
            Step 09 : Enter "C6185740" in Title.
            Step 10 : Click Save.
            Step 11 : Exit RO.
        """
        wfreportobj.select_top_toolbar_item("toptoolbar_save")
        utillobj.ibfs_save_as("C6185740")
        
        """    
            Step 12 : Click data icon.    
        """
        utillobj.infoassist_api_edit_("C6185740", tool="chart", folder="P292_S11397/G458325")
        report_obj.wait_for_visible_text("#pfjTableChart_2 ", "SALARY")
        report_obj.verify_grayedout_field_in_data_pane("Dimensions", "TYPE", 11, msg="Step 12.00: Verify Greayed out in Dimensions")        
#         report_obj.verify_grayedout_field_in_data_pane("Measures/Properties", "PCT_INC", 5, msg="Step 12: Verify Greayed out in Measures")

        """    
            Step 13 : Mouse hover data icon present in top of the Data panel.    
        """
        report_obj.verify_datapane_toggle_button_tooltip_in_disablemode()
        
        """    
            Step 14 : Click data icon.    
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(5) #firefox need time to avoid stale error
        report_obj.verify_grayedout_field_in_data_pane("Dimensions", "DAT_INC", 9, msg="Step 14.00: Verify Greayed out in Dimensions",color_to_verify='black')        
#         report_obj.verify_grayedout_field_in_data_pane("Measures/Properties", "PCT_INC", 5, msg="Step 14: Verify Greayed out in Measures",color_to_verify='black')

        """    
            Step 15 :Logout of the IA API using the following URL.
            http://machine:port/alias/service/wf_security_logout.jsp   
        """
        vis_obj.logout_visualization_using_api()
        
        
if __name__ == '__main__':
    unittest.main()