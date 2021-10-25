'''
Created on 05-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227545
TestCase Name = Verify available Auto Link Targets on two different columns
'''
import unittest
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_run, ia_ribbon
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods  
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report

class C2227545_TestClass(BaseTestCase):

    def test_C2227545(self):
        
        Test_Case_ID = "C2227545"
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj = CoreUtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        report = Report(self.driver)
        query_css = "#queryTreeWindow"
        
        """    
            Step 01 :Launch the IA API with CAR, Report mode
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(1)", 'Report(car)', expire_time=190)
         
        """    
            Step 02 : Double click "CAR", "RETAIL_COST".    
        """
        metaobj.datatree_field_click("CAR", 2, 1)
        report.wait_for_visible_text(query_css, "CAR")
        
        metaobj.datatree_field_click("RETAIL_COST", 2, 1)
        report.wait_for_visible_text(query_css, "RETAIL_COST")
        
        coln_list = ['CAR', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 02.01: Verify column titles")
       
        """    
            Step 03 : Drag and drop "CAR" to Filter Pane    
        """
        metaobj.drag_drop_data_tree_items_to_filter("CAR", 1)
        report.wait_for_visible_text("#dlgWhere_btnCancel", "Cancel")
       
        """    
            Step 04 : Double-click <Value>, select Type "Parameter", click ok, ok    
        """
        ia_ribbonobj.create_parameter_filter_condition('Simple', 'Simple')
        utillobj.synchronize_with_visble_text('#qbFilterBox', 'Equal', 30)
        metaobj.verify_filter_pane_field('CAR Equal to Simple Parameter (Name: CAR)', 1, "Step 04.01")
        
        """    
            Step 05 : Select Format Tab -> Click "Auto Link Target" 
        """
        ribbonobj.select_ribbon_item("Format", "Auto_Link_Target")
        utillobj.synchronize_with_number_of_element("[id^='FormatTargetAutoLink'][class*='checked ']", 1, expire_time=4)
        
        """    
            Step 06 : Click "IA" > "Save" > Enter "Title:" = "AUTOLINK_TARGET02", click "Save".    
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        report.wait_for_visible_text("#IbfsOpenFileDialog7_btnCancel", "Cancel")
        utillobj.ibfs_save_as("AUTOLINK_TARGET02")
        utillobj.synchronize_until_element_disappear("#IbfsOpenFileDialog7_btnCancel", report.home_page_short_timesleep)
         
        """    
            Step 07 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        utillobj.infoassist_api_logout()
        
        """    
            Step 08 : Launch the IA API with CAR, Report mode :    
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(1)", 'Report(car)', expire_time=190)
        
        """    
            Step 09 : Double click "CAR","MODEL","SALES"  
        """
        metaobj.datatree_field_click("CAR", 2, 1)
        report.wait_for_visible_text(query_css, "CAR")
        
        metaobj.datatree_field_click("MODEL", 2, 1)
        report.wait_for_visible_text(query_css, "MODEL")
        
        metaobj.datatree_field_click("SALES", 2, 1)
        report.wait_for_visible_text(query_css, "SALES")
        
        """    
            Step 10 : Select "Format" > "Enable Auto Linking" 
        """
        ribbonobj.select_ribbon_item("Format", "Enable_Auto_Linking")
        utillobj.synchronize_with_number_of_element("[id^='FormatEnableAutoLink'][class*='checked']", 1, expire_time=45)
        
        """    
            Step 11 : Click "IA" > "Save" > Enter "Title:" = "C2227545", click "Save".    
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        report.wait_for_visible_text("#IbfsOpenFileDialog7_btnCancel", "Cancel")
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.synchronize_until_element_disappear("#IbfsOpenFileDialog7_btnCancel", report.home_page_short_timesleep)
        
        """    
            Step 12 : Click "Run".    
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=1)
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(1)>td:nth-child(1)", 'CAR', expire_time=90)
        
        """  
            Step 13 : Verify output with hyperlinks on both "CAR", "MODEL".    
        """
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227545_Ds01.xlsx", "Step 13.01: verify data set")
        iarun.verify_autolink("table[summary='Summary']","ALFA ROMEO",2,1,10,"Step 13.02: Verify Auto Drill applied in CAR")
        iarun.verify_autolink("table[summary= 'Summary']", "2000 4 DOOR BERLINA", 2,2,18,"Step 13.03: Verify Auto Drill applied in MODEL")
        
        """    
            Step 14 : Click value "2002 2 DOOR", verify ONLY "AUTOLINK_TARGET01" fex is listed
            Step 15 : Hover over and select "AUTOLINK_TARGET01" -> Verify output 
        """     
        iarun.select_report_autolink_tooltip("table[summary= 'Summary']", 6,2, "Auto Links->AUTOLINK_TARGET01")
        utillobj.switch_to_default_content()
        core_utillobj.switch_to_new_window()
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(1)>td:nth-child(1)", 'CAR', expire_time=45)
         
        """
            Verify output
        """
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227545_Ds02.xlsx", "Step 15.01: verify Output")
        
        """    
            Step 16 : Close output window 
        """
        core_utillobj.switch_to_previous_window()
        utillobj.switch_to_frame(pause=3)

        """  
            Step 17 : Click value "BMW" in the initial output window, verify ONLY "AUTOLINK_TARGET02" is listed    
            Step 18 : Hover over and select "AUTOLINK_TARGET02" -> Verify output 
        """
        iarun.select_report_autolink_tooltip("table[summary= 'Summary']", 6,1, "Auto Links->AUTOLINK_TARGET02")
        utillobj.switch_to_default_content()
        core_utillobj.switch_to_new_window()
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(1)>td:nth-child(1)", 'CAR', expire_time=45)
        
        """
            Verify output
        """
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227545_Ds03.xlsx", "Step 18.01: verify Output")
        
        """    
            Step 19 : Close output window    
        """
        core_utillobj.switch_to_previous_window()
        
        """ 
            Step 20 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp 
        """
        #Page will logout at end of the base test class
        
if __name__ == '__main__':
    unittest.main()