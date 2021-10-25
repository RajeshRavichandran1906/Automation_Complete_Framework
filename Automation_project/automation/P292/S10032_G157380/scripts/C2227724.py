'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227724
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity

class C2227724_TestClass(BaseTestCase):
    def test_C2227724(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227724'
        
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
        
        """    2. Select "Insert" > "Grid".    """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Grid')
        time.sleep(10)
        
        """    3. Double click "Revenue" and "Product,Category".    """
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(8)
        
        """    4. Verify the two fields are showing in the Query pane.    """
        metaobj.verify_query_pane_field('Rows', 'Product,Category', 1, "Step 04a: Verify Product,Category in Rows")
        metaobj.verify_query_pane_field('Measure', 'Revenue', 1, "Step 04b: Verify Revenue in Measure")
        
        """    5. Click "Undo".    """
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        time.sleep(8)
        
        """    6. Verify "Product,Category" has been removed from the Query pane.    """
        metaobj.verify_query_pane_field('Rows', 'Columns', 1, "Step 06a: Verify Product,Category has been removed from Rows")
        
        """    7. Verify "Revenue" is still showing on the Grid.    """
        metaobj.verify_query_pane_field('Measure', 'Revenue', 1, "Step 07a: Verify Revenue in Measure")
        heading = ['Revenue',]
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',heading, 'Step 07b: Verify column titles')
        
        """    8. Click "Redo".    """
        ribbonobj.select_top_toolbar_item('toolbar_redo')
        time.sleep(8)
        
        """    9. Verify "Product,Category" has been added back to the Query pane.    """
        metaobj.verify_query_pane_field('Rows', 'Product,Category', 1, "Step 09a: Verify Product,Category in Rows")
        metaobj.verify_query_pane_field('Measure', 'Revenue', 1, "Step 09b: Verify Revenue in Measure")
        heading = ['Product Category', 'Revenue',]
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',heading, 'Step 09c: Verify column titles')
        
        """    10. Click "Undo" 3 times    """
        for i in range(3):
            ribbonobj.select_top_toolbar_item('toolbar_undo')
            time.sleep(8)
            
        """    11. Verify "Undo" button is disabled.    """
        disabled =self.driver.find_element_by_css_selector("#undoButton").get_attribute('disabled')                
        utillobj.asequal(disabled, 'true', "Step 11a: Verify 'Undo' button is disabled")
        time.sleep(4)
        
        """    12. Verify "Grid1" canvas has been removed.    """
        try:
            def_grid=driver.find_element_by_css_selector("#TableChart_2 svg>g>text.title").text.strip()
            utillobj.asequal(True, def_grid, "Step 12a: Verify the default Grid displayed on Preview")
        except:
            utillobj.asequal(False, False, "Step 12a: Verify the default Grid1 has been removed")
            
        """    13. Verify all the data has been removed and only the default gray chart displayed.    """
        def_chart=driver.find_element_by_css_selector("#TableChart_1 svg>g>text.title").text.strip()
        utillobj.asequal("Drop Measures or Sorts into the Query Pane", def_chart, "Step 13a: Verify the default Chart displayed on Preview")
        
        """    14. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()

