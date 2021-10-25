'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227693
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227693_TestClass(BaseTestCase):
    def test_C2227693(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227693'
        time_out = 30
        expected_list=['PIN','LASTNAME', 'FIRSTNAME','MIDINITIAL','DIV']
        bar1=['LASTNAME:CVEK', 'SALARY:$62,500.00', 'Filter Chart', 'Exclude from Chart']
        bar2=['LASTNAME:ADAMS', 'EXPENSES:3,400.00', 'Filter Chart', 'Exclude from Chart']
        bar3=['LASTNAME:NOZAWA', 'SALARY:$80,500.00', 'Filter Chart', 'Exclude from Chart']
        bar4=['LASTNAME:MEDINA', 'EXPENSES:3,150.00', 'Filter Chart', 'Exclude from Chart']
        bar5=['LASTNAME:SANCHEZ', 'SALARY:$83,000.00', 'Filter Chart', 'Exclude from Chart']
        bar6=['LASTNAME:WHITE', 'EXPENSES:7,000.00', 'Filter Chart', 'Exclude from Chart']
        expected_xval_list=['ADAMS', 'ADDAMS', 'ANDERSON', 'BELLA', 'CASSANOVA', 'CASTALANETTA', 'CHISOLM', 'CONRAD', 'CONTI', 'CVEK', 'DONATELLO', 'DUBOIS', 'ELLNER', 'FERNSTEIN', 'GORDON', 'GOTLIEB', 'GRAFF', 'HIRSCHMAN', 'KASHMAN', 'LASTRA', 'LEWIS', 'LIEBER', 'LOPEZ', 'MARTIN', 'MEDINA', 'MORAN', 'NOZAWA', 'OLSON', 'PATEL', 'PULASKI', 'PUMA', 'ROSENTHAL', 'RUSSO', 'SANCHEZ', 'SO', 'SOPENA', 'VALINO', 'WANG', 'WHITE']
        expected_yval_list=['0', '30K', '60K', '90K', '120K', '150K']
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        
        utillobj.infoassist_api_login('idis','new_retail/empdata','P292/S10032_visual_3', 'mrid', 'mrpass')
              
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """    2. Click "Join".    """
        ribbonobj.select_ribbon_item('Home', 'Join')
        
        """    3. Verify "empdata" fields list is showing on the "Join" window.    """
        table_css="#dlgJoin #metaDataBrowser"
        tables=self.driver.find_elements_by_css_selector(table_css)
        source_tds=tables[0].find_elements_by_css_selector("td")
        actual_list=[]
        for i in range(5):
            temp=source_tds[i].text.strip()
            actual_list.append(temp)
        utillobj.asequal(expected_list, actual_list, "Step 03: Verify 'empdata' fields list is showing on the 'Join' window")
        
        """    4. Click "Add New".    """
        """    5. Select "training" master file.    """
        """    6. Click "Open".    """
#         join_add=driver.find_element_by_css_selector("#dlgJoin #dlgJoin_btnAddMaster img")
#         utillobj.default_left_click(object_locator=join_add)
#         open_dialog_file_name="#IbfsOpenFileDialog7_cbFileName"
#         utillobj.synchronize_with_number_of_element(open_dialog_file_name, 1, time_out)
#         utillobj.select_masterfile_in_open_dialog('new_retail', 'training.mas')
        ia_ribbonobj.create_join("training", new_join=False)
        
        """    7. Verify the 'red arrow' appears joined by "PIN".    """
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 07a: Verify join created successfully")
        
        """    8. Click "OK".    """
        join_btn=driver.find_element_by_css_selector("#dlgJoin_btnOK img")
        utillobj.default_left_click(object_locator=join_btn)
        time.sleep(5)
        
        """    9. Verify "EXPENSES" have been added to the Data pane.    """
        metaobj.verify_data_pane_field("Measures/Properties","EXPENSES", 2, "Step 09a: Verify 'EXPENSES' have been added to the Data pane")
        
        """    10. Double click "LASTNAME","SALARY","EXPENSES".    """
        metaobj.datatree_field_click("LASTNAME", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("SALARY", 2, 1)
        time.sleep(6)
        metaobj.datatree_field_click("EXPENSES", 2, 1)
        time.sleep(8)  
        
        """    11. Verify the following chart is displayed.    """
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g9!mbar!", bar1, "Step 11(i): Verify Salary bar value")
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g0!mbar!", bar2, "Step 11(ii): Verify Salary bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'LASTNAME', "Step11:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['SALARY','EXPENSES'], "Step 11:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 67, 'Step 11.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 11.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g15!mbar!", "pale_green", "Step 11.c(ii): Verify first bar color")
        time.sleep(1)
        
        """    12. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(10) 
        
        """    13. Verify the following chart is displayed in the "Run" window.    """
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g26!mbar!", bar3, "Step 13(i): Verify Salary bar value")
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g24!mbar!", bar4, "Step 13(ii): Verify Salary bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'LASTNAME', "Step13:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['SALARY','EXPENSES'], "Step 13:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 13:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 67, 'Step 13.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g22!mbar!", "lochmara", "Step 13.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g1!mbar!", "pale_green", "Step 13.c(ii): Verify first bar color")
        time.sleep(5)
        
        """    14. Dismiss the "Run" window.    """
        time.sleep(5)
        self.driver.close()
        time.sleep(3)
        utillobj.switch_to_window(0)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """    15. Click "IA" > "Save" > "C2160103" > "Save".    """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    16. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """    17. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2160103.fex&tool=idis    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(20)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    18. Verify Data Pane displays correct fields (including the JOIN fields).    """
        metaobj.verify_data_pane_field("Dimensions","DEPT", 6, "Step 18a: Verify Data pane field - EMPDATA DEPT")
        metaobj.verify_data_pane_field("Dimensions","COURSECODE", 12, "Step 18b: Verify Data pane field - TRAINING COURSECODE")
        metaobj.verify_data_pane_field("Measures/Properties","SALARY", 1, "Step 18c: Verify Data pane field - EMPDATA SALARY")
        metaobj.verify_data_pane_field("Measures/Properties","EXPENSES", 2, "Step 18d: Verify Data pane field - TRAINING EXPENSES")
        
        """    19. Verify the following chart is displayed.    """
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g33!mbar!", bar5, "Step 19(i): Verify Salary bar value")
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g38!mbar!", bar6, "Step 19(ii): Verify Salary bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'LASTNAME', "Step19:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['SALARY','EXPENSES'], "Step 19:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 19:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 67, 'Step 19.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g19!mbar!", "lochmara", "Step 19.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g15!mbar!", "pale_green", "Step 19.c(ii): Verify first bar color")
        time.sleep(5)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step18', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    20. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
                     
        
if __name__ == '__main__':
    unittest.main()

