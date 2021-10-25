'''
Developed By  : KK14897
Developed Date: 18-DEC-2018

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6185733
TestCase Name =Gray Out Fields Not on the Path in Multi-segment FOCUS file

'''
import unittest, time
from common.wftools import report,visualization
from common.pages import visualization_metadata
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods 

class C6185733_TestClass(BaseTestCase):
    
    def test_C6185733(self):
        
        report_obj=report.Report(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        vis_obj=visualization.Visualization(self.driver)
        vis_meta_obj=visualization_metadata.Visualization_Metadata(self.driver)
        
        """    
            Step 01 : Create new report with employee using API call:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/employee&item=IBFS:/WFC/Repository/P292_S11397/G458325.
        """
        MASTER_FILE_NAME="ibisamp/employee"
        report_obj.invoke_ia_tool_using_new_api_login(tool='report', master=MASTER_FILE_NAME)
        
        """    
            Step 02 : Goto View tab and select Structured in Data Panel.
        """
        report_obj.select_ia_ribbon_item("View", "structured_tab")
        time.sleep(4)
        vis_meta_obj.verify_field_in_data_pane("EMPINFO", "LAST_NAME", 2, msg="Step 02.00 : Verify field in data pane")
        
        """    
            Step 03 :Add DATE_ATTEND from ATTNDSEG into the BY.
        """
        report_obj.double_click_on_datetree_item("ATTNDSEG->DATE_ATTEND", 1)
        
        """    
            Step 04 : Mouse hover data icon present in top of the Data panel.
        """
        report_obj.verify_datapane_toggle_button_tooltip_in_enablemode()
        
        """    
            Step 05 : Click data icon to Enable Path Enforcement.    
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(4)
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "SALARY", 3, msg="Step 05.01: Verify Greayed out in PAYINFO")        
        report_obj.verify_grayedout_field_in_data_pane("JOBSEG", "JOBCODE", 1, msg="Step 05.02: Verify Greayed out in JOBSEG")
        
        """    
            Step 06 : Double click or drag GROSS field from SALINFO into the Sum.    
        """
        report_obj.double_click_on_datetree_item("SALINFO->GROSS", 1)
        
        """    
            Step 07 : Replace DATE_ATTEND in By with BANK_NAME from FUNDTRAN segment.    
        """
        report_obj.drag_field_from_data_tree_to_query_pane("FUNDTRAN->BANK_NAME", 1, "DATE_ATTEND", 1,ele_loc="middle")
        
        '''Verify only "EMPINFO" and "FUNDTRAN" segments are accessible.'''
        report_obj.verify_grayedout_field_in_data_pane("EMPINFO", "EMP_ID", 1, msg="Step 07.01: Verify Greayed out in EMPINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("FUNDTRAN", "BANK_CODE", 2, msg="Step 07.02: Verify Greayed out in FUNDTRAN",color_to_verify="black")
        
        '''Verify other than "EMPINFO" and "FUNDTRAN" segments are not accessible.'''
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "SALARY", 3, msg="Step 07.03: Verify Greayed out in PAYINFO")        
        report_obj.verify_grayedout_field_in_data_pane("JOBSEG", "JOBCODE", 1, msg="Step 07.04: Verify Greayed out in JOBSEG")
        
        """    
            Step 08 : Mouse hover data icon present in top of the Data panel.    
        """
        report_obj.verify_datapane_toggle_button_tooltip_in_disablemode()
        
        """    
            Step 09 : Click Data icon in top of the data panel to Disable Path Enforcement.    
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(4)
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "SALARY", 3, msg="Step 09.01: Verify Greayed out in PAYINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("JOBSEG", "JOBCODE", 1, msg="Step 09.02: Verify Greayed out in JOBSEG",color_to_verify="black")
        
        """    
            Step 10 : Replace BANK_NAME in By with DAT_INC in PAYINFO segment. (Using drag and drop)    
        """
        report_obj.drag_field_from_data_tree_to_query_pane("PAYINFO->DAT_INC", 1, "BANK_NAME", 1,ele_loc="middle")
        
        """    
            Step 11 : Click data icon.    
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(4)
        
        '''Verify field names in the data panel list not along with the accessible path are grayed out'''
        report_obj.verify_grayedout_field_in_data_pane("ADDRESS", "TYPE", 1, msg="Step 11.01: Verify Greayed out in PAYINFO")        
        report_obj.verify_grayedout_field_in_data_pane("SALINFO", "PAY_DATE", 1, msg="Step 11.02: Verify Greayed out in JOBSEG")
        
        '''Only EMPINFO, FUNDTRAN, PAYINFO, JOBSEG, SECSEG and SKILLSEG segments are accessible'''
        report_obj.verify_grayedout_field_in_data_pane("EMPINFO", "EMP_ID", 1, msg="Step 11.03: Verify Greayed out in PAYINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("FUNDTRAN", "BANK_NAME", 1, msg="Step 11.04: Verify Greayed out in JOBSEG",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "SALARY", 3, msg="Step 11.05: Verify Greayed out in PAYINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("JOBSEG", "JOBCODE", 1, msg="Step 11.06: Verify Greayed out in JOBSEG",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("SECSEG", "SEC_CLEAR", 1, msg="Step 11.07: Verify Greayed out in SECSEG",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("SKILLSEG", "SKILLS", 1, msg="Step 11.08: Verify Greayed out in SKILLSEG",color_to_verify="black")
        
        """    
            Step 12 : Double click JOB_DESC in JOBSEG and delete DAT_INC in By.    
        """
        report_obj.double_click_on_datetree_item("JOBSEG->JOB_DESC", 1)
        vis_meta_obj.select_querytree_field("DAT_INC", "right", 1, context_menu_path="Delete")
        report_obj.verify_grayedout_field_in_data_pane("EMPINFO", "EMP_ID", 1, msg="Step 12.01: Verify Greayed out in EMPINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("FUNDTRAN", "BANK_NAME", 1, msg="Step 12.02: Verify Greayed out in FUNDTRAN",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "SALARY", 3, msg="Step 12.03: Verify Greayed out in PAYINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("JOBSEG", "JOBCODE", 1, msg="Step 12.04: Verify Greayed out in JOBSEG",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("SECSEG", "SEC_CLEAR", 1, msg="Step 12.05: Verify Greayed out in PAYINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("SKILLSEG", "SKILLS", 1, msg="Step 12.06: Verify Greayed out in JOBSEG",color_to_verify="black")
        
        """    
            Step 13 : Replace JOB_DESC in By with SEC_CLEAR in SECSEG segment.    
        """
        report_obj.drag_field_from_data_tree_to_query_pane("SECSEG->SEC_CLEAR", 1, "JOB_DESC", 1,ele_loc="middle")
        report_obj.verify_grayedout_field_in_data_pane("EMPINFO", "EMP_ID", 1, msg="Step 13.01: Verify Greayed out in EMPINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("FUNDTRAN", "BANK_NAME", 1, msg="Step 13.02: Verify Greayed out in FUNDTRAN",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "SALARY", 3, msg="Step 13.03: Verify Greayed out in PAYINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("JOBSEG", "JOBCODE", 1, msg="Step 13.04: Verify Greayed out in JOBSEG",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("SECSEG", "SEC_CLEAR", 1, msg="Step 13.05: Verify Greayed out in SECSEG",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("SKILLSEG", "SKILLS", 1, msg="Step 13.06: Verify Greayed out in SKILLSEG")
        
        """    
            Step 14 : Click on data icon.    
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(4)
        report_obj.verify_grayedout_field_in_data_pane("EMPINFO", "EMP_ID", 1, msg="Step 14.01: Verify Greayed out in EMPINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("FUNDTRAN", "BANK_NAME", 1, msg="Step 14.02: Verify Greayed out in FUNDTRAN",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "SALARY", 3, msg="Step 14.03: Verify Greayed out in PAYINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("JOBSEG", "JOBCODE", 1, msg="Step 14.04: Verify Greayed out in JOBSEG",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("SECSEG", "SEC_CLEAR", 1, msg="Step 14.05: Verify Greayed out in SECSEG",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("SKILLSEG", "SKILLS", 1, msg="Step 14.06: Verify Greayed out in SKILLSEG",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("ADDRESS", "TYPE", 1, msg="Step 14.05: Verify Greayed out in ADDRESS",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("SALINFO", "PAY_DATE", 1, msg="Step 14.06: Verify Greayed out in SALINFO",color_to_verify="black")
        
        """    
            Step 15 : Double click SKILLS in SKILLSEG and delete SEC_CLEAR in By.    
        """
        report_obj.double_click_on_datetree_item("SKILLSEG->SKILLS", 1)
        vis_meta_obj.select_querytree_field("SEC_CLEAR", "right", 1, context_menu_path="Delete")
        time.sleep(15)
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "DAT_INC", 1, msg="Step 15.01: Verify Greayed out in EMPINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("FUNDTRAN", "BANK_NAME", 1, msg="Step 15.02: Verify Greayed out in FUNDTRAN",color_to_verify="black")
        
        """    
            Step 16 : Click data icon.    
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(4)
        report_obj.verify_grayedout_field_in_data_pane("EMPINFO", "EMP_ID", 1, msg="Step 16.01: Verify Greayed out in EMPINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("FUNDTRAN", "BANK_NAME", 1, msg="Step 16.02: Verify Greayed out in FUNDTRAN",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "SALARY", 3, msg="Step 16.03: Verify Greayed out in PAYINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("JOBSEG", "JOBCODE", 1, msg="Step 16.04: Verify Greayed out in JOBSEG",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("SECSEG", "SEC_CLEAR", 1, msg="Step 16.05: Verify Greayed out in PAYINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("SKILLSEG", "SKILLS", 1, msg="Step 16.06: Verify Greayed out in JOBSEG",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("ADDRESS", "TYPE", 1, msg="Step 16.07: Verify Greayed out in ADDRESS")
        
        """    
            Step 17 : Click on data icon.    
        """
        report_obj.click_datapane_toggle_button()
        web_element = self.driver.find_element_by_css_selector('#resultArea')
        core_utils.python_move_to_element(web_element)
        report_obj.verify_datapane_toggle_button_tooltip_in_enablemode()
        report_obj.verify_grayedout_field_in_data_pane("EMPINFO", "EMP_ID", 1, msg="Step 17.01: Verify Greayed out in EMPINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("FUNDTRAN", "BANK_NAME", 1, msg="Step 17.02: Verify Greayed out in FUNDTRAN",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "SALARY", 3, msg="Step 17.03: Verify Greayed out in PAYINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("JOBSEG", "JOBCODE", 1, msg="Step 17.04: Verify Greayed out in JOBSEG",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("SECSEG", "SEC_CLEAR", 1, msg="Step 17.05: Verify Greayed out in SECSEG",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("SKILLSEG", "SKILLS", 1, msg="Step 17.06: Verify Greayed out in SKILLSEG",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("ADDRESS", "TYPE", 1, msg="Step 17.07: Verify Greayed out in ADDRESS",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("SALINFO", "PAY_DATE", 1, msg="Step 17.08: Verify Greayed out in SALINFO",color_to_verify="black")
        
        """    
            Step 18 : Replace SKILLS in By with TYPE in ADDRESS segment. (Using drag and drop)    
        """
        report_obj.drag_field_from_data_tree_to_query_pane("ADDRESS->TYPE", 1, "SKILLS", 1,ele_loc="middle")
        
        """    
            Step 19 : Click on data icon.    
        """
        report_obj.click_datapane_toggle_button()
        core_utils.python_move_to_element(web_element)
        report_obj.verify_datapane_toggle_button_tooltip_in_disablemode()
        report_obj.verify_grayedout_field_in_data_pane("EMPINFO", "EMP_ID", 1, msg="Step 19.01: Verify Greayed out in EMPINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("FUNDTRAN", "BANK_NAME", 1, msg="Step 19.02: Verify Greayed out in FUNDTRAN",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "SALARY", 3, msg="Step 19.04: Verify Greayed out in PAYINFO")        
        report_obj.verify_grayedout_field_in_data_pane("JOBSEG", "JOBCODE", 1, msg="Step 19.05: Verify Greayed out in JOBSEG")
        report_obj.verify_grayedout_field_in_data_pane("SECSEG", "SEC_CLEAR", 1, msg="Step 19.06: Verify Greayed out in SECSEG")        
        report_obj.verify_grayedout_field_in_data_pane("SKILLSEG", "SKILLS", 1, msg="Step 19.07: Verify Greayed out in SKILLSEG")        
        report_obj.verify_grayedout_field_in_data_pane("SALINFO", "PAY_DATE", 1, msg="Step 19.08: Verify Greayed out in SALINFO")
        
        """    
            Step 20 : Click on data icon.    
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(4)
        report_obj.verify_grayedout_field_in_data_pane("EMPINFO", "EMP_ID", 1, msg="Step 20.01: Verify Greayed out in EMPINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("FUNDTRAN", "BANK_NAME", 1, msg="Step 20.02: Verify Greayed out in FUNDTRAN",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "SALARY", 3, msg="Step 20.03: Verify Greayed out in PAYINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("JOBSEG", "JOBCODE", 1, msg="Step 20.04: Verify Greayed out in JOBSEG",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("SECSEG", "SEC_CLEAR", 1, msg="Step 20.05: Verify Greayed out in SECSEG",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("SKILLSEG", "SKILLS", 1, msg="Step 20.06: Verify Greayed out in SKILLSEG",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("ADDRESS", "TYPE", 1, msg="Step 20.07: Verify Greayed out in ADDRESS",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("SALINFO", "PAY_DATE", 1, msg="Step 20.08: Verify Greayed out in SALINFO",color_to_verify="black")
        
        """    
            Step 21 : Replace TYPE in By with PAY_DATE in SALINFO segment. (Using drag and drop)    
        """
        report_obj.collapse_datatree_field_section('FUNDTRAN') #work around for getting EMPINFO
        report_obj.drag_field_from_data_tree_to_query_pane("SALINFO->PAY_DATE", 1, "TYPE", 1,ele_loc="middle")
        report_obj.expand_datatree_field_section('FUNDTRAN')
        
        """    
            Step 22 : Click on data icon.    
        """
        report_obj.click_datapane_toggle_button()
        core_utils.python_move_to_element(web_element)
        report_obj.verify_datapane_toggle_button_tooltip_in_disablemode()
        report_obj.verify_grayedout_field_in_data_pane("EMPINFO", "EMP_ID", 1, msg="Step 22.01: Verify Greayed out in EMPINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("FUNDTRAN", "BANK_NAME", 1, msg="Step 22.02: Verify Greayed out in FUNDTRAN",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("SALINFO", "PAY_DATE", 1, msg="Step 22.03: Verify Greayed out in SALINFO",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("ADDRESS", "TYPE", 1, msg="Step 22.04: Verify Greayed out in ADDRESS")
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "SALARY", 3, msg="Step 22.05: Verify Greayed out in PAYINFO")        
        report_obj.verify_grayedout_field_in_data_pane("JOBSEG", "JOBCODE", 1, msg="Step 22.06: Verify Greayed out in JOBSEG")
        report_obj.verify_grayedout_field_in_data_pane("SECSEG", "SEC_CLEAR", 1, msg="Step 22.07: Verify Greayed out in SECSEG")        
        report_obj.verify_grayedout_field_in_data_pane("SKILLSEG", "SKILLS", 1, msg="Step 22.08: Verify Greayed out in SKILLSEG")        
        
        """    
            Step 23 : Replace PAY_DATE in By with DED_CODE in DEDUCT segment. (Using drag and drop)    
        """
        report_obj.collapse_datatree_field_section('FUNDTRAN') #work around for getting DEDUCT
        report_obj.drag_field_from_data_tree_to_query_pane("DEDUCT->DED_CODE", 1, "PAY_DATE", 1,ele_loc="middle")
        report_obj.expand_datatree_field_section('FUNDTRAN')
        time.sleep(3)
        report_obj.verify_datapane_toggle_button_tooltip_in_disablemode()
        report_obj.verify_grayedout_field_in_data_pane("FUNDTRAN", "BANK_NAME", 1, msg="Step 23.01: Verify Greayed out in FUNDTRAN",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("SALINFO", "PAY_DATE", 1, msg="Step 23.02: Verify Greayed out in SALINFO",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("ADDRESS", "TYPE", 1, msg="Step 23.04: Verify Greayed out in ADDRESS")
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "SALARY", 3, msg="Step 23.05: Verify Greayed out in PAYINFO")        
        report_obj.verify_grayedout_field_in_data_pane("JOBSEG", "JOBCODE", 1, msg="Step 23.06: Verify Greayed out in JOBSEG")
        report_obj.verify_grayedout_field_in_data_pane("SECSEG", "SEC_CLEAR", 1, msg="Step 23.07: Verify Greayed out in SECSEG")        
        report_obj.verify_grayedout_field_in_data_pane("SKILLSEG", "SKILLS", 1, msg="Step 23.08: Verify Greayed out in SKILLSEG")        
        
        """    
            Step 24 : Click on data icon.    
        """
        report_obj.click_datapane_toggle_button()
        time.sleep(4)
        report_obj.verify_grayedout_field_in_data_pane("EMPINFO", "EMP_ID", 1, msg="Step 24.01: Verify Greayed out in EMPINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("FUNDTRAN", "BANK_NAME", 1, msg="Step 24.02: Verify Greayed out in FUNDTRAN",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("SALINFO", "PAY_DATE", 1, msg="Step 24.03: Verify Greayed out in SALINFO",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("ADDRESS", "TYPE", 1, msg="Step 24.04: Verify Greayed out in ADDRESS",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "SALARY", 3, msg="Step 24.05: Verify Greayed out in PAYINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("JOBSEG", "JOBCODE", 1, msg="Step 24.06: Verify Greayed out in JOBSEG",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("SECSEG", "SEC_CLEAR", 1, msg="Step 24.07: Verify Greayed out in SECSEG",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("SKILLSEG", "SKILLS", 1, msg="Step 24.08: Verify Greayed out in SKILLSEG",color_to_verify="black")        
        
        """    
            Step 25 : Replace DED_CODE in By with COURSE_CODE in COURSEG segment. (Using drag and drop)    
        """
        report_obj.collapse_datatree_field_section('FUNDTRAN') #work around for getting COURSEG
        report_obj.drag_field_from_data_tree_to_query_pane("COURSEG->COURSE_CODE", 1, "DED_CODE", 1,ele_loc="middle")
        report_obj.expand_datatree_field_section('FUNDTRAN')
        
        """    
            Step 26 : Click data icon to ON Enforce Paths.    
        """
        report_obj.click_datapane_toggle_button()
        core_utils.python_move_to_element(web_element)
        report_obj.verify_datapane_toggle_button_tooltip_in_disablemode()
        report_obj.verify_grayedout_field_in_data_pane("EMPINFO", "EMP_ID", 1, msg="Step 26.01: Verify Greayed out in EMPINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("FUNDTRAN", "BANK_NAME", 1, msg="Step 26.02: Verify Greayed out in FUNDTRAN",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("SALINFO", "PAY_DATE", 1, msg="Step 26.03: Verify Greayed out in SALINFO")
        report_obj.verify_grayedout_field_in_data_pane("ADDRESS", "TYPE", 1, msg="Step 26.04: Verify Greayed out in ADDRESS")
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "SALARY", 3, msg="Step 26.05: Verify Greayed out in PAYINFO")        
        report_obj.verify_grayedout_field_in_data_pane("JOBSEG", "JOBCODE", 1, msg="Step 26.06: Verify Greayed out in JOBSEG")
        report_obj.verify_grayedout_field_in_data_pane("SECSEG", "SEC_CLEAR", 1, msg="Step 26.07: Verify Greayed out in SECSEG")        
        report_obj.verify_grayedout_field_in_data_pane("SKILLSEG", "SKILLS", 1, msg="Step 26.08: Verify Greayed out in SKILLSEG")        
        
        """    
            Step 27 : Replace COURSE_CODE in By with EMP_ID in the top segment (EMPINFO). (Using drag and drop)    
        """
        report_obj.drag_field_from_data_tree_to_query_pane("EMPINFO->EMP_ID", 1, "COURSE_CODE", 1,ele_loc="middle")
        report_obj.verify_grayedout_field_in_data_pane("EMPINFO", "EMP_ID", 1, msg="Step 27.01: Verify Greayed out in EMPINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("FUNDTRAN", "BANK_NAME", 1, msg="Step 27.02: Verify Greayed out in FUNDTRAN",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("SALINFO", "PAY_DATE", 1, msg="Step 27.03: Verify Greayed out in SALINFO",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("ADDRESS", "TYPE", 1, msg="Step 27.04: Verify Greayed out in ADDRESS",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("PAYINFO", "SALARY", 3, msg="Step 27.05: Verify Greayed out in PAYINFO",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("JOBSEG", "JOBCODE", 1, msg="Step 27.06: Verify Greayed out in JOBSEG",color_to_verify="black")
        report_obj.verify_grayedout_field_in_data_pane("SECSEG", "SEC_CLEAR", 1, msg="Step 27.07: Verify Greayed out in SECSEG",color_to_verify="black")        
        report_obj.verify_grayedout_field_in_data_pane("SKILLSEG", "SKILLS", 1, msg="Step 27.08: Verify Greayed out in SKILLSEG",color_to_verify="black")
        
        """    
            Step 28 : Click Save in toolbar.
            Step 29 : Enter "C6185733" in Title.
            Step 30 : Click Save.    
        """
        vis_obj.save_visualization_from_top_toolbar("C6185733")
        
        """    
            Step 31 :Logout of the IA API using the following URL.
            http://machine:port/alias/service/wf_security_logout.jsp   
        """
        report_obj.api_logout()
        
        
if __name__ == '__main__':
    unittest.main()