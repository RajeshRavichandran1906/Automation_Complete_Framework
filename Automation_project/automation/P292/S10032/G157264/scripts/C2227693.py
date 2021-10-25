'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227693
'''
import unittest, time
from selenium.webdriver.common.by import By
from common.lib import utillity,core_utility
from common.lib.basetestcase import BaseTestCase
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon

class C2227693_TestClass(BaseTestCase):
    
    def test_C2227693(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227693'
        expected_list=['PIN','LASTNAME', 'FIRSTNAME','MIDINITIAL','DIV']
        expected_xval_list=['ADAMS', 'ADDAMS', 'ANDERSON', 'BELLA', 'CASSANOVA', 'CASTALANETTA', 'CHISOLM', 'CONRAD', 'CONTI', 'CVEK', 'DONATELLO', 'DUBOIS', 'ELLNER', 'FERNSTEIN', 'GORDON', 'GOTLIEB', 'GRAFF', 'HIRSCHMAN', 'KASHMAN', 'LASTRA', 'LEWIS', 'LIEBER', 'LOPEZ', 'MARTIN', 'MEDINA', 'MORAN', 'NOZAWA', 'OLSON', 'PATEL', 'PULASKI', 'PUMA', 'ROSENTHAL', 'RUSSO', 'SANCHEZ', 'SO', 'SOPENA', 'VALINO', 'WANG', 'WHITE']
        expected_yval_list=['0', '30K', '60K', '90K', '120K', '150K']
        
        """
            CLASS OBJECTS
        """
        driver = self.driver #Driver reference object created
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
           http://machine:port/ibi_apps/ia?tool=idis&master=ibisamp/empdata&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2F    """
        
        utillobj.infoassist_api_login('idis','ibisamp/empdata','P292/S10032_visual_3', 'mrid', 'mrpass')        
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
        utillobj.asequal(expected_list, actual_list, "Step 03.01: Verify 'empdata' fields list is showing on the 'Join' window")
        
        """    4. Click "Add New".    """
        """    5. Select "training" master file.    """
        """    6. Click "Open".    """
        ia_ribbonobj.create_join("ibisamp","training", new_join=False)
        
        """    7. Verify the 'red arrow' appears joined by "PIN".    """
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 07.01: Verify join created successfully")
        
        """    8. Click "OK".    """
        join_btn=driver.find_element_by_css_selector("#dlgJoin_btnOK img")
        core_utils.left_click(join_btn)
        time.sleep(5)
        
        """    9. Verify "EXPENSES" have been added to the Data pane.    """
        metaobj.verify_data_pane_field("Measures/Properties","EXPENSES", 2, "Step 09.01: Verify 'EXPENSES' have been added to the Data pane")
        
        """    10. Double click "LASTNAME","SALARY","EXPENSES".    """
        metaobj.datatree_field_click("LASTNAME", 2, 1)
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'LASTNAME', 30)
        metaobj.datatree_field_click("SALARY", 2, 1)
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'SALARY', 30)
        metaobj.datatree_field_click("EXPENSES", 2, 1)
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'EXPENSES', 30)
        
        """    11. Verify the following chart is displayed.    """
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']", 67, 30)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'LASTNAME', "Step 11.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['SALARY','EXPENSES'], "Step 11.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 67, 'Step 11.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "lochmara", "Step 11.05: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g15!mbar!", "pale_green", "Step 11.06: Verify first bar color")
        time.sleep(1)
        
        """    12. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utils.switch_to_new_window()
        
        """    13. Verify the following chart is displayed in the "Run" window.    """
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']", 67, 30)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'LASTNAME', "Step 13.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['SALARY','EXPENSES'], "Step 13.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 13.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 67, 'Step 13.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g22!mbar!", "lochmara", "Step 13.05: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g1!mbar!", "pale_green", "Step 13.06: Verify first bar color")
        time.sleep(5)
        
        """    14. Dismiss the "Run" window.    """
        core_utils.switch_to_previous_window()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """    15. Click "IA" > "Save" > "C2160103" > "Save".    """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    16. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """    17. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2160103.fex&tool=idis    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'LASTNAME', 30)
        
        """    18. Verify Data Pane displays correct fields (including the JOIN fields).    """
        metaobj.verify_data_pane_field("Dimensions","DEPT", 6, "Step 18.01: Verify Data pane field - EMPDATA DEPT")
        metaobj.verify_data_pane_field("Dimensions","COURSECODE", 12, "Step 18.02: Verify Data pane field - TRAINING COURSECODE")
        metaobj.verify_data_pane_field("Measures/Properties","SALARY", 1, "Step 18.03: Verify Data pane field - EMPDATA SALARY")
        metaobj.verify_data_pane_field("Measures/Properties","EXPENSES", 2, "Step 18.04: Verify Data pane field - TRAINING EXPENSES")
        
        """    19. Verify the following chart is displayed.    """
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']", 67, 30)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'LASTNAME', "Step 19.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['SALARY','EXPENSES'], "Step 19.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 19.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 67, 'Step 19.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g19!mbar!", "lochmara", "Step 19.05: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g15!mbar!", "pale_green", "Step 19.06: Verify first bar color")
        time.sleep(5)

    """    20. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """               
        
if __name__ == '__main__':
    unittest.main()