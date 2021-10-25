'''
Created on Nov 30, 2017

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2231280
TestCase Name : Auto Prompt using Static and Dynamic filters
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_run 
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2231280_TestClass(BaseTestCase):

    def test_C2231280(self):
        
        Test_Case_ID = "C2231280"
        Test_Case_ID1 = "C2231275"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        """
            Step 1:Reopen FEX created in the precondition test case (C2231275):
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2231275.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID1, 'report', 'P292/S10032_infoassist_4', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        coln_list = ['NEWSITE', 'LASTNAME', 'COURSECODE', 'EXPENSES', 'NEWEXPENSES']
        resultobj.verify_report_titles_on_preview(5, 5, "TableChart_1", coln_list, "Step 01:01: Verify column titles")
         
        """
            Step 2:Select IA > Save As > "C2231280" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)    
        """
            Step 3:Click field EXPENSES in the Sum container > Select "Prompt" in the Field Tab ribbon
        """
        metaobj.querytree_field_click('EXPENSES', 1, 0)
        ribbonobj.select_ribbon_item('Field', 'Prompt')
        parent_css="#dlgWhere [class*='active']"
        resultobj.wait_for_property(parent_css, 1)
              
        """ 
            Step 4:Select "Dynamic" radio button
            Step 5:Check off "Select multiple values at runtime"
            Step 6:Click OK > OK
        """
        ia_ribbobj.create_parameter_filter_condition('Dynamic', ['EXPENSES'], ParamMultiple=True)
        time.sleep(2)
        metaobj.verify_filter_pane_field('EXPENSES Equal to Multiselect Dynamic Parameter (Name: EXPENSES, Field: EXPENSES in J001)', 1, "Step 06:01: Verify the filter pane")
        """ 
            Step 7:Click field NEWSITE in the Query pane > Select "Prompt" in the Field Tab ribbon
        """
        metaobj.datatree_field_click('NEWSITE', 0, 1)
        ribbonobj.select_ribbon_item('Field', 'Prompt')
        """ 
            Step 8:Verify default options (Dynamic should be disabled)
        """
        filter_prompt_css=self.driver.find_element_by_css_selector("#dlgWhereValue_rbParamDynamic")
        status=filter_prompt_css.get_property('disabled')
        utillobj.asequal(status, True, "Step 08:01: Verify Dynamic should be disabled")
           
        """ 
            Step 9:Click "Static" radio button
            Step 10:Check off "Select multiple values at runtime"
            Step 11:Click Get Values > All
            Step 12:Multi-select values from 103 E HAWTHORNE to 33 CHASE RD > Click the >> button to move selection to the right panel
            Step 13:Click OK > OK
        """ 
        ia_ribbobj.create_parameter_filter_condition('Static', ['103 E HAWTHORNE','20 E ROCKAWAY','20 ROCKAWAY','238 BEECHWOOD PLACE','265 S EASTERN BLVD','33 CHASE RD'], getvalue_params='All', ParamMultiple=True)
        time.sleep(2)
        metaobj.verify_filter_pane_field('NEWSITE Equal to Multiselect Static Parameter (Name: NEWSITE, Values: 103 E HAWTHORNE, 20 E ROCKAWAY, 20 ROCKAWAY, ...)', 2, "Step 13:02: Verify filter pane")   
           
        """     
            Step 14:Click the output location shortcut in the status bar > Select "New Window"
        """
        ia_ribbobj.select_report_output_window('New Window')
        time.sleep(4)
        """ 
            Step 15:Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
              
        """
            Step 16:Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
         
        """ 
            Step 17:Verify Auto Prompt page in new window
        """
        utillobj.switch_to_window(1)
        """ 
            Step 18:Click "All Values" dropdown > Click "Select Values" in the pop up dialog
            Step 19:Scroll down and check off values from "3,200.00" to "3,400.00" > Click the back arrow icon on top to submit selection.
        """
        ia_runobj.select_amper_value('EXPENSES', ['3,200.00','3,300.00','3,350.00','3,400.00'],Search=True)
        time.sleep(2)
           
        """ 
            Step 20:Click "NEWSITE:" dropdown > Check off values from 103 E HAWTHROME to 265 S EASTERN BLVD > Click the x icon on top to submit selection.
        """ 
        ia_runobj.select_amper_value('NEWSITE', ['103 E HAWTHORNE','20 E ROCKAWAY','20 ROCKAWAY','238 BEECHWOOD PLACE','265 S EASTERN BLVD'], False)   
        """ 
            Step 21:Click the Run icon in the Auto Prompt page
        """ 
        time.sleep(4)
        ia_runobj.select_amper_menu('Run')    
        """ 
            Step 22:Verify output > Close window
        """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[name="wfOutput"]')))
        time.sleep(4)
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds02.xlsx", "Step 22:01: Verify output at runtime using autoprompt") 
              
        """ 
            Step 23:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        driver.close()
        utillobj.switch_to_window(0)
        utillobj.infoassist_api_logout()
        """    
            Step 24:Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2231280.fex&tool=Report
        """ 
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_4', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)   
        """  
            Step 25:Verify Preview and Filter pane
        """
        coln_list = ['NEWSITE', 'LASTNAME', 'COURSECODE', 'EXPENSES', 'NEWEXPENSES']
        resultobj.verify_report_titles_on_preview(5, 5, "TableChart_1", coln_list, "Step 25:01: Verify column titles")
        metaobj.verify_filter_pane_field('EXPENSES Equal to Multiselect Dynamic Parameter (Name: EXPENSES, Field: EXPENSES in IBISAMP/TRAINING)', 1, "Step 25:01: Verify the filter pane")
        metaobj.verify_filter_pane_field('NEWSITE Equal to Multiselect Static Parameter (Name: NEWSITE, Values: 103 E HAWTHORNE, 20 E ROCKAWAY, 20 ROCKAWAY, ...)', 2, "Step 25:02: Verify filter pane")
         
        """ 
            Step 26:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    unittest.main()