'''
Created on 05-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227546
TestCase Name = Verify Auto Link Targets with multiple drill downs
'''
import unittest
import time
from common.pages import visualization_metadata, visualization_ribbon, ia_run, ia_ribbon, ia_resultarea
from common.lib import utillity
from common.lib import core_utility
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report

class C2227546_TestClass(BaseTestCase):

    def test_C2227546(self):
      
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj = core_utility.CoreUtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        report_obj=Report(self.driver)
        
        """    1. Reopen fex AUTOLINK_SOURCE01 using IA API:    """
        report_obj.edit_fex_using_api_url(folder_name="P292/S10032_infoassist_2", fex_name="AUTOLINK_SOURCE01", mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
         
        """    2. Select Format Tab > Verify "Enable Auto Linking" is enabled.    """
        ribbonobj.switch_ia_tab("Format")
        time.sleep(3)
        oVerify="tool-bar-button-checked" in driver.find_element_by_id("FormatEnableAutoLink").get_attribute("class")
        utillobj.asequal(True, oVerify, "Step 02a: Verify 'Enable Auto Linking' is enabled")
        
        """    3. Click field "MODEL", click "Drill Down" on the Ribbon    """
        metaobj.querytree_field_click("MODEL", 1)
        time.sleep(15)
        dd_btn=driver.find_element_by_css_selector("#FieldDrillDown img")
        core_utillobj.left_click(dd_btn)
        time.sleep(10)
        
        """    4. Click "Browse", select "AUTOLINK_TARGET01", click "Open"    """
        """    5. Remove default name in the "Description" area -> Type "Drill down to Report"    """
        ia_ribbonobj.create_drilldown_report("report", browse_file_name="AUTOLINK_TARGET01",set_description="Drill down to Report")
        
        """    6. Click "Create a new drill down" icon    """
        new_btn=driver.find_element_by_css_selector("#drillDownNew img")
        core_utillobj.left_click(new_btn)
        time.sleep(3)
        
        """    7. Click "Web Page" option, click URL input box.    """
        """    8. Type http://www.ibi.com    """
        ia_ribbonobj.create_drilldown_report("webpage", url_value="http://www.ibi.com")
        
        """    9. Click "Create a new drill down" icon    """
        new_btn=driver.find_element_by_css_selector("#drillDownNew")
        core_utillobj.left_click(new_btn)
        time.sleep(3)
        
        """    10. Click "Web Page" option, click URL input box    """
        """    11. Type http://www.google.com    """
        """    12. Click OK    """
        ia_ribbonobj.create_drilldown_report("webpage", url_value="http://www.google.com", click_ok='yes')
        
        """    13. Verify the hyperlink is applied on Live preview    """
        ia_resultobj.verify_autolink("TableChart_1","2000 4 DOOR BERLINA",18,"Step 13a: Verify Auto Drill applied in 2000 4 DOOR BERLINA") 
 
        """    14. Click "Save" > verify save message > click OK    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        report_obj.wait_for_visible_text("#IbfsOpenFileDialog7_btnCancel", "Cancel")
        utillobj.ibfs_save_as("AUTOLINK_SOURCE01_a")
        time.sleep(5)
        
        """    15. Click "Run"    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(pause=1)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227546_Ds01.xlsx", "Step 15a: verify data set")
        
        """    16. Click value "2000 GT VELOCE", verify menu for multi-drill and auto link targets    """
        iarun.verify_autolink_tooltip_values("table[summary='Summary']", 3, 2, ['Drill down to Report', 'Drill Down 2', 'Drill Down 3', 'Auto Links'], "Step 16a: Verify menu for Multi-drill and Autolink targets")
        
        """    17. Hover over Auto Links -> select the auto link target "AUTOLINK_TARGET01" -> verify output    """
        iarun.select_report_autolink_tooltip("table[summary= 'Summary']", 3,2, "Auto Links->AUTOLINK_TARGET01")
        utillobj.switch_to_default_content(pause=1)
        core_utillobj.switch_to_new_window()
        time.sleep(10)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227546_Ds02.xlsx", "Step 17b: verify Output")
        
        """    18. Close output window for selected "AUTOLINK_TARGET01" target    """
        core_utillobj.switch_to_previous_window()
        utillobj.switch_to_frame(pause=1)
      
        """    19. Click value "2002 2 DOOR" in the initial output window    """
        """    20. Select "Drill down to Report" -> verify output    """
        iarun.select_report_autolink_tooltip("table[summary= 'Summary']", 6,2, "Drill down to Report")
        utillobj.switch_to_default_content(pause=1)
        time.sleep(10)
        core_utillobj.switch_to_new_window()

        expected_plist=['Close Filter Panel', 'Reset filter values', 'Save current values', 'Run with filter values']
        plist=[]
        prompt=driver.find_elements_by_css_selector("#promptPanel div>a")
        for i in range(len(prompt)):
            plist.append(prompt[i].get_attribute("title"))
        utillobj.asequal(plist, expected_plist, "step 20a: Verify autoprompt navigation buttons")
        arprompt=driver.find_element_by_css_selector("#promptPanel > div > div > div[class^='autop-amper'] > div > div").get_attribute("title")
        utillobj.asin("CAR", arprompt, "Step 20b: verify the field name")
                
        """    21. Close the output window for the selected drill Report    """
        core_utillobj.switch_to_previous_window()
        utillobj.switch_to_frame(pause=1)
       
        """    22. Click value "2000 GT VELOCE" -> select "Drill Down3"    """
        iarun.select_report_autolink_tooltip("table[summary= 'Summary']", 6,2, "Drill Down 3")
        
        """    23. Verify google page is displayed - https://www.google.com/    """
        utillobj.switch_to_default_content(pause=1)
        core_utillobj.switch_to_new_window()
        owebpage=driver.current_url
        utillobj.asin("google", owebpage, "Step 23a: Verify Google page isdisplayed")
        
        """    24. Close the web page, close the output window    """
        core_utillobj.switch_to_previous_window()

        """    25. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
    
if __name__ == '__main__':
    unittest.main()