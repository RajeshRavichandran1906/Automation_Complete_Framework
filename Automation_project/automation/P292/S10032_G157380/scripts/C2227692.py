'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227692
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity

class C2227692_TestClass(BaseTestCase):
    def test_C2227692(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227692'
        
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
        
        """    2. Select "Home" > "Visual" > "Insert" (dropdown) > "Grid".    """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Grid')
        time.sleep(10)

        """    3. Verify the following is displayed.    """
        def_grid=driver.find_element_by_css_selector("#TableChart_2 svg>g>text.title").text.strip()
        utillobj.asequal("Drag fields here to create grid", def_grid, "Step 03a: Verify the default Grid displayed on Preview")
        def_chart=driver.find_element_by_css_selector("#TableChart_1 svg>g>text.title").text.strip()
        utillobj.asequal("Drop Measures or Sorts into the Query Pane", def_chart, "Step 03b: Verify the default Chart displayed on Preview")
        
        """    4. Double click "Revenue","Product,Category".    """
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(8)
        
        """    5. Verify the following is displayed in the Query pane.    """
        metaobj.verify_query_pane_field('Rows', 'Product,Category', 1, "Step05a: Verify Product,Category in Rows")
        metaobj.verify_query_pane_field('Measure', 'Revenue', 1, "Step05b: Verify Revenue in Measure")
        
        """    6. Verify the following grid is displayed.    """
        heading = ['Product Category', 'Revenue',]
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',heading, 'Step 06.1: Verify column titles')
        row_val=['Accessories', '$129,608,338.53']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val,'Step 06.2: verify grid 1st row value')
        expected_tooltip=['Product Category:Televisions', 'Revenue:$78,381,132.81', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mcellFill!r5!c0!",expected_tooltip, "Step 06.3: verify the default tooltip values")
        time.sleep(5)
        
        """    7. Verify the following chart is displayed.    """
        def_chart=driver.find_element_by_css_selector("#TableChart_1 svg>g>text.title").text.strip()
        utillobj.asequal("Drop Measures or Sorts into the Query Pane", def_chart, "Step 07a: Verify the default Chart displayed on Preview")
        
        """    8. Click "Swap".    """
        ribbonobj.select_ribbon_item('Home', 'Swap')
        time.sleep(5)
        
        """    9. Verify the following is displayed in the Query pane.    """
        metaobj.verify_query_pane_field('Columns', 'Product,Category', 1, "Step09a: Verify Product,Category in Columns")
        metaobj.verify_query_pane_field('Measure', 'Revenue', 1, "Step09b: Verify Revenue in Measure")
        
        """    10. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        ele=driver.find_element_by_css_selector("#resultArea #iaCanvasPanel")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step10', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        
if __name__ == '__main__':
    unittest.main()

