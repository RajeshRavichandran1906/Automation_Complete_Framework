'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227723
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity

class C2227723_TestClass(BaseTestCase):
    def test_C2227723(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227723'
        bar=['Sale Quarter:3', 'Revenue:$252,441,794.52', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to Sale Month']
        expected_xval_list=['1','2','3','4']
        expected_yval_list=['0', '50M','100M', '150M', '200M', '250M', '300M', '350M']
        expected_xval_list1=[]
        expected_yval_list1=['0', '0.2B','0.4B', '0.6B', '0.8B', '1B', '1.2B']
        expected_yval_list2=['0', '0.3B','0.6B', '0.9B', '1.2B', '1.5B']
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
              
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """    2. Double click "Revenue"    """
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(8)
        
        """    3. Expand "Sales_Related" > "Trasaction Date, Simple" > double click "Sale,Quarter"    """
        metaobj.datatree_field_click("Sale,Quarter", 2, 1)
        time.sleep(8)
        
        """    4. Verify the following chart is displayed.    """
        time.sleep(5)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar!", bar, "Step 04: Verify bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Sale Quarter', "Step 04:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 04:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 04:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 04.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "lochmara", "Step 04.c: Verify first bar color")
        time.sleep(5)
        
        """    5. Click "Undo" twice    """
        for i in range(2):
            ribbonobj.select_top_toolbar_item('toolbar_undo')
            time.sleep(8)
        
        """    6. Verify the following chart is displayed.    """
        def_chart=driver.find_element_by_css_selector("#TableChart_1 svg>g>text.title").text.strip()
        utillobj.asequal("Drop Measures or Sorts into the Query Pane", def_chart, "Step 07a: Verify the default Chart displayed on Preview")
        
        """    7. Click "Redo".    """
        ribbonobj.select_top_toolbar_item('toolbar_redo')
        time.sleep(8)
        
        """    8. Verify the following chart is displayed.    """
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 08:a(i) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list1, expected_yval_list1, "Step 08:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "lochmara", "Step 08.c: Verify first bar color")
        time.sleep(5)
        
        """    9. Double click "Gross Profit".    """
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        time.sleep(8)
        
        """    10. Verify the following chart is displayed.    """
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Revenue','Gross Profit'], "Step 10:a(i) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list1, expected_yval_list2, "Step 10:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 1, 'Step 10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "lochmara", "Step 10.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!", "pale_green", "Step 10.c(ii): Verify first bar color")
        time.sleep(5)
        
        """    11. Click "Undo" Twice    """
        for i in range(2):
            print(i)
            ribbonobj.select_top_toolbar_item('toolbar_undo')
            time.sleep(8)
            
        """    12. Verify "Undo" button is disabled.    """
        disabled =self.driver.find_element_by_css_selector("#undoButton").get_attribute('disabled')                
        utillobj.asequal(disabled, 'true', "Step 12a: Verify 'Undo' button is disabled")
        time.sleep(4)
        
        """    13. Verify the following chart is displayed.    """
        def_chart=driver.find_element_by_css_selector("#TableChart_1 svg>g>text.title").text.strip()
        utillobj.asequal("Drop Measures or Sorts into the Query Pane", def_chart, "Step 13a: Verify the default Chart displayed on Preview")
        ele=driver.find_element_by_css_selector("#TableChart_1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step13', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    14. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()

