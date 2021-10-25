'''
Created on 05-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227544
TestCase Name = Enable Auto Link and verify available Auto Link Targets from IA and repository tree
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_run, ia_ribbon, wf_legacymainpage
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods  
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report

class C2227544_TestClass(BaseTestCase):

    def test_C2227544(self):
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj = CoreUtillityMethods(self.driver)    
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        legacyobj=wf_legacymainpage.Wf_Legacymainpage(self.driver)
        report = Report(self.driver)
        
        """
            Step 01 : Launch the IA API with CAR, Report mode: http://machine:port/ibi_apps/ia?tool=report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS7385%2F
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(1)", 'Report(car)', expire_time=190)
            
        """
            Step 02 : Double click "CAR","MODEL","DEALER_COST".
        """
        for item in ["CAR", "MODEL", "DEALER_COST"]:
            metaobj.datatree_field_click(item,2,1)
            utillobj.synchronize_with_visble_text("#queryTreeColumn", item, metaobj.chart_medium_timesleep)
        coln_list = ["CAR", "MODEL", "DEALER_COST"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 02a: Verify column titles")
          
        """
            Step 03 : Drag "CAR" to the Filter pane.
        """
        metaobj.drag_drop_data_tree_items_to_filter("CAR", 1)
        report.wait_for_visible_text("#dlgWhere_btnCancel", "Cancel")
             
        """
            Step 04 : Double click "<Value>", set "Type:" = "Parameter", click "OK" (2x).
        """
        ia_ribbonobj.create_parameter_filter_condition('Simple', 'Simple')
             
        """
            Step 05 : Drag "MODEL" to the Filter pane.
        """
        metaobj.drag_drop_data_tree_items_to_filter("MODEL", 1)
        report.wait_for_visible_text("#dlgWhere_btnCancel", "Cancel")
         
        """
            Step 06 : Double-click <Value>, select Type "Parameter", click ok, ok    
        """
        ia_ribbonobj.create_parameter_filter_condition('Simple', 'Simple',rownum=3)
        report.wait_for_number_of_element("#qbFilterBox table>tbody>tr", 2, 30)
        metaobj.verify_filter_pane_field('CAR Equal to Simple Parameter (Name: CAR)', 1, "Step 06a")
        metaobj.verify_filter_pane_field('MODEL Equal to Simple Parameter (Name: MODEL)', 2, "Step 06b")
             
        """    
            Step 07 : Select Format Tab -> Click "Auto Link Target"    
        """
        ribbonobj.select_ribbon_item("Format", "Auto_Link_Target")
             
        """    
            Step 08 : Click "IA" > "Save" > Enter "Title:" = "AUTOLINK_TARGET01", click "Save".    
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        report.wait_for_visible_text("#IbfsOpenFileDialog7_btnCancel", "Cancel")
        utillobj.ibfs_save_as("AUTOLINK_TARGET01")
            
        """    
            Step 09 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp   
        """
        utillobj.infoassist_api_logout()
            
        """    
            Step 10 : Launch the IA API with WF_RETAIL_LITE, Chart mode:    
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(1)", 'Report(car)', expire_time=15)
            
        """    
            Step 11 : Double click "CAR","MODEL","SALES"    
        """
        for item in ["CAR", "MODEL", "SALES"]:
            metaobj.datatree_field_click(item,2,1)
            utillobj.synchronize_with_visble_text("#queryTreeColumn", item, metaobj.chart_medium_timesleep)
            
        """    
            Step 12 : Select "Format" > "Enable Auto Linking".    
        """
        ribbonobj.select_ribbon_item("Format", "Enable_Auto_Linking")
            
        """    
            Step 13 : Click "IA" > "Save" > Enter "Title:" = "AUTOLINK_SOURCE01", click "Save".    
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as("AUTOLINK_SOURCE01")
             
        """    
            Step 14 : Click "Run".    
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utillobj.switch_to_frame()
            
        """    
            Step 15 : Verify output with hyperlinks on field "MODEL" ONLY    
        """
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(1)>td:nth-child(1)", 'CAR', expire_time=90)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227544_Ds01.xlsx", "Step 15a: verify data set")
        iarun.verify_autolink("table[summary= 'Summary']", "2000 GT VELOCE", 3,2,18,"Step 15")
            
        """   
            Step 16 : Click value "2002 2 DOOR", verify "AUTOLINK_TARGET01" fex is listed    
            Step 17 : Hover over and select "AUTOLINK_TARGET01"
        """
        iarun.select_report_autolink_tooltip("table[summary= 'Summary']", 6,2, "Auto Links->AUTOLINK_TARGET01")
        core_utillobj.switch_to_default_content()
        core_utillobj.switch_to_new_window()
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(1)>td:nth-child(1)", 'CAR', expire_time=10)
             
        """    
            Step 18 : Verify output.    
        """
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227544_Ds02.xlsx", "Step 18a: verify Output")
        core_utillobj.switch_to_previous_window()
           
        """    
            Step 19 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        utillobj.infoassist_api_logout()
      
        """    
            Step 20 : Logon to WF: http://machine:port/{alias}/legacyhome and expand Repository folder > "S7385"
            Step 21 : Highlight "AUTOLINK_SOURCE01" > Right mouse click > "Properties" > Verify "Enable Auto Linking" checkbox is enabled > click "Cancel".
        """
        utillobj.invoke_legacyhomepage('mrid', 'mrpass')
        elem1="#bipTreePanel #treeView"
        utillobj.synchronize_with_number_of_element(elem1, 1, 190)
        project_id=utillobj.parseinitfile('project_id')
        folder = utillobj.parseinitfile('suite_id')
        legacyobj.select_repository_menu(project_id+"_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)->" + folder + "->" + "AUTOLINK_SOURCE01", "Properties")
        legacyobj.select_or_verify_properties_flaglist('enable_auto_link',check=True, msg='Step 21a: verify Enable Auto Linking checkbox is enabled')
        cancel_btn=driver.find_element_by_css_selector("#btnCancel img")
        core_utillobj.left_click(cancel_btn)
         
        """   
            Step 22 : Highlight "AUTOLINK_TARGET01" > Right mouse click > "Properties" > Verify "Auto Link Target" checkbox is enabled > click "Cancel".    
        """
        legacyobj.select_repository_menu('AUTOLINK_TARGET01', 'Properties')
        legacyobj.select_or_verify_properties_flaglist('auto_link_target',check=True, msg='Step 22a: verify auto_link_target checkbox is enabled')
        cancel_btn=driver.find_element_by_css_selector("#btnCancel img")
        core_utillobj.left_click(cancel_btn)
         
        """    
            Step 23 : Highlight "AUTOLINK_SOURCE01" > Right mouse click > "Run".    
        """
        legacyobj.select_repository_menu(project_id+"_S10032_G157398 (Folder Name is P292 - Remain as is due to HTML pages)->" + folder + "->" + "AUTOLINK_SOURCE01", 'Run')
        core_utillobj.switch_to_new_window()
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(1)>td:nth-child(1)", 'CAR', expire_time=10)
        
        """    
            Step 24 : Verify output with hyperlinks on field "MODEL" ONLY.    
        """
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227544_Ds01.xlsx", "Step 24a: verify data set")
        iarun.verify_autolink("table[summary= 'Summary']", "2000 GT VELOCE", 3,2,18,"Step 24")
        core_utillobj.update_current_working_area_browser_specification() 
        
        """ 
            Step 25 : Click value "2002 2 DOOR", verify "AUTOLINK_TARGET01" fex is listed
            Step 26 : Hover over and select "AUTOLINK_TARGET01".    
        """
        iarun.select_report_autolink_tooltip("table[summary= 'Summary']", 6,2, "Auto Links->AUTOLINK_TARGET01")
        core_utillobj.switch_to_new_window()
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(2)>td:nth-child(1)", 'BMW', expire_time=20)
          
        """    
            Step 27. Verify output. 
        """
        table_css = "table[summary= 'Summary'] > tbody > tr"
        table_rows = utillobj.validate_and_get_webdriver_objects(table_css, "table")
        act_list = [el.text.strip().replace('\n',' ') for el in table_rows if el.text.strip() != '']
        exp_list = ['CAR MODEL DEALER_COST', 'BMW 2002 2 DOOR 5,800']
        utillobj.as_List_equal(act_list, exp_list, "Step 27. Verify output")
        core_utillobj.switch_to_previous_window()
        core_utillobj.switch_to_previous_window()
          
        """ 
            Step 28 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp 
        """
          
if __name__ == '__main__':
    unittest.main()