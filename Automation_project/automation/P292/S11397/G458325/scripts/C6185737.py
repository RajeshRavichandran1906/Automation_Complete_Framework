'''
Developed By  : Vishnu_priya
Developed Date: 17/9/2019
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6185737
TestCase Name = Gray out fields using verb objects in Sum sorting field
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import report,visualization
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods

class C6185737_TestClass(BaseTestCase):
    
    def test_C6185737(self):
        
        report_obj=report.Report(self.driver)
        vis_obj=visualization.Visualization(self.driver)
        utill_obj = UtillityMethods(self.driver)
        core_utils= CoreUtillityMethods(self.driver)
        
        step1="""    
        Step 01:Launch the API to create new Report with EMPLOYEE.
        http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/employee&item=IBFS:/WFC/Repository/P292_S11397/G458325.
        """
        
        MASTER_FILE_NAME="ibisamp/employee"
        report_obj.invoke_ia_tool_using_new_api_login(tool='report', master=MASTER_FILE_NAME)
        utill_obj.capture_screenshot("01.01", step1)
        
        step2= """
        Step 02:Click "View tab" and Click "LIST".
        """
        report_obj.select_ia_ribbon_item("View", "List_tab")
        utill_obj.capture_screenshot("02.01", step2)
        
        step3 = """    
            Step 03 : Drag and drop "JOB_DESC" from Data pane into "Sum" in Query pane..
        """
        source = self.driver.find_element_by_css_selector("div[id*=QbMetaDataTree] .bi-tree-view-body-content>table>tbody>tr:nth-child(18)")
        target=self.driver.find_element_by_css_selector("#queryTreeColumn .bi-tree-view-body-content>table>tbody>tr:nth-child(2)")
        utill_obj.drag_drop_using_uisoup(source,target,cord_type='start')
        utill_obj.capture_screenshot("03.01", step3)
        
        Step4 = """    
            Step 04 :Mouse hover data icon present in top of the Data panel.
            Check the tool tip appears as "Enable Path Enforcement".
        """
        
        report_obj.verify_datapane_toggle_button_tooltip_in_enablemode()
        utill_obj.capture_screenshot("04.01", Step4)
        
        Step5 ="""    
            Step 05 : Click data icon.
            Check fields which are not matching the path of the added field are not accessible in the Data pane.
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(5)
        report_obj.verify_grayedout_field_in_data_pane_list_view("TYPE","TYPE",Stepno="05:01")
        report_obj.verify_grayedout_field_in_data_pane_list_view("ADDRESS_LN1","ADDRESS_LN1",Stepno="05:02")
        report_obj.verify_grayedout_field_in_data_pane_list_view("ADDRESS_LN2","ADDRESS_LN2",Stepno="05:03")
        report_obj.verify_grayedout_field_in_data_pane_list_view("GROSS","GROSS",Stepno="05:04")
        utill_obj.capture_screenshot("05.01", Step5,True)
        
        Step6 ="""
            Step 06:Drag and Drop "BANK_CODE" in Sum bucket (Replace "JOB_DESC").
            Check only field which are matching the path of the data source are accessible other fields are grayed out.
        """
        source = self.driver.find_element_by_css_selector("div[id*=QbMetaDataTree] .bi-tree-view-body-content>table>tbody>tr:nth-child(28)")
        target=self.driver.find_element_by_css_selector("#queryTreeColumn .bi-tree-view-body-content>table>tbody>tr:nth-child(3)")
        utill_obj.drag_drop_using_uisoup(source,target,cord_type='start')
        report_obj.verify_grayedout_field_in_data_pane_list_view("DAT_INC","DAT_INC",Stepno="06:01")
        report_obj.verify_grayedout_field_in_data_pane_list_view("JOBCODE","JOBCODE",Stepno="06:02")
        utill_obj.capture_screenshot("06.01", Step6,True)
        
        Step7 ="""
        Step07: Click "Data" icon.
        Check the fields in data pane are back to normal.
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(5)
        report_obj.verify_grayedout_field_in_data_pane_list_view("TYPE","TYPE",Stepno="07:01",color_to_verify='black')
        report_obj.verify_grayedout_field_in_data_pane_list_view("ADDRESS_LN1","ADDRESS_LN1",Stepno="07:02",color_to_verify='black')
        report_obj.verify_grayedout_field_in_data_pane_list_view("ADDRESS_LN2","ADDRESS_LN2",Stepno="07:03",color_to_verify='black')
        report_obj.verify_grayedout_field_in_data_pane_list_view("GROSS","GROSS",Stepno="07:04",color_to_verify='black')
        utill_obj.capture_screenshot("07.01", Step7,True)
        
        Step8 = """
        Step 08:Double click "CURR_JOBCODE" in Data pane.
        """
        source = self.driver.find_element_by_css_selector("div[id*=QbMetaDataTree] .bi-tree-view-body-content>table>tbody>tr:nth-child(6)")
        core_utils.double_click(source)
        utill_obj.capture_screenshot("08.01", Step8)
        
        Step9 ="""
        Step 09: Drag and drop "SKILLS" from Data pane into "Across" bucket in Query pane.
        """
        source = self.driver.find_element_by_css_selector("div[id*=QbMetaDataTree] .bi-tree-view-body-content>table>tbody>tr:nth-child(28)")
        target=self.driver.find_element_by_css_selector("#queryTreeColumn .bi-tree-view-body-content>table>tbody>tr:nth-child(6)")
        utill_obj.drag_drop_using_uisoup(source,target,cord_type='start')
        utill_obj.capture_screenshot("09.01", Step9)
        
        Step10 = """
        Step 10:Click data icon.
        Check Data pane and Query pane.
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(5)
        report_obj.verify_grayedout_field_in_data_pane_list_view("DAT_INC","DAT_INC",Stepno="10:01")
        report_obj.verify_grayedout_field_in_data_pane_list_view("JOBCODE","JOBCODE",Stepno="10:02")
        report_obj.verify_grayedout_field_in_data_pane_list_view("TYPE","TYPE",Stepno="10:03")
        report_obj.verify_grayedout_field_in_data_pane_list_view("ADDRESS_LN1","ADDRESS_LN1",Stepno="10:04")
        report_obj.verify_grayedout_field_in_data_pane_list_view("ADDRESS_LN2","ADDRESS_LN2",Stepno="10:05")
        report_obj.verify_grayedout_field_in_data_pane_list_view("GROSS","GROSS",Stepno="10:06")
        utill_obj.capture_screenshot("10.01", Step10)
        
        Step11 = """
        Step 11:Click on data icon
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(5)
        utill_obj.capture_screenshot("11.01", Step11)
        
        Step12 ="""    
        Step 12 :Click "Save" in toolbar Enter "C6185737" and Click "Save" button.   
        """
        vis_obj.save_visualization_from_top_toolbar("C6185736")
        utill_obj.capture_screenshot("12.01", Step12)
        
        """    
        Step 13 :Logout of the IA API using the following URL.
        http://machine:port/alias/service/wf_security_logout.jsp   
        """
        report_obj.api_logout()
        
        
if __name__ == '__main__':
    unittest.main()