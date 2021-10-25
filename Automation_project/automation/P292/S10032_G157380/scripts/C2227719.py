'''
Created on Jun 15, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227719
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon,visualization_run,\
    ia_run,wf_mainpage
from common.locators import visualization_resultarea_locators
from common.lib import utillity
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pyautogui import click


class C2227719_TestClass(BaseTestCase):

    def test_C2227719(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227719'
        
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_runobj = visualization_run.Visualization_Run(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
           
        """
        Step02: Select "Home" > "Visual" > "Insert" (dropdown) > "Grid"
        Step03: Double click "Product,Category"
        """
        time.sleep(3)
        ribbonobj.select_ribbon_item('Home','Insert',opt='Grid')
        time.sleep(10)
        resultobj.verify_panel_caption_label(0, 'Grid1', "Step02: Verify Grid1 is displayed")
        resultobj.verify_panel_caption_label(1, 'Bar Stacked1', "Step02: Verify Bar Stacked1 is displayed")
           
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        metaobj.verify_query_pane_field('Rows',"Product,Category",1,"Step03: Verify Rows")
      
        """
        Step04: Verify that report with relevant data is displayed in the canvas area.
        """
#         utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
       
        time.sleep(4)
        parent_css1="#TableChart_2 .rowTitle text"
        resultobj.wait_for_property(parent_css1,1)
          
        time.sleep(5)
        heading = ['Product Category']
        resultobj.verify_grid_column_heading('TableChart_2',heading, 'Step04.1: Verify column titles')
        row_val=['Accessories']
        resultobj.verify_grid_row_val('TableChart_2',row_val,'Step04.2: verify grid 1st row value')
         
        """
        Step05: Select "Insert" > "Grid".
        """
        time.sleep(3)
        ribbonobj.select_ribbon_item('Home','Insert',opt='Grid')
 
        """
        Step06: Verify that the canvas has split into three and left side is empty to build the new report.
        """        
        time.sleep(10)
        resultobj.verify_panel_caption_label(0, 'Grid2', "Step06: Verify Grid2 is displayed")
        resultobj.verify_panel_caption_label(1, 'Grid1', "Step06: Verify Grid1 is displayed")
        resultobj.verify_panel_caption_label(2, 'Bar Stacked1', "Step06: Verify Bar Stacked1 is displayed")

        time.sleep(4)
        parent_css1=self.driver.find_element_by_css_selector("#TableChart_3 .rowTitle text")
        d=utillobj.get_attribute_value(parent_css1, 'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'',"Step06: Verify Grid2 is empty")
                
        """
        Step07: Select "Product,Category", "Gender", "Sale,Quarter" and "Revenue".
        """
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 2,1)
        time.sleep(4)
        metaobj.datatree_field_click("Gender", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Sale,Quarter", 2,1)
        time.sleep(4)
        metaobj.datatree_field_click("Revenue", 2,1)
        time.sleep(4)
        
        """
        Step08: Verify that those fields are displayed in the Query Pane (under Grid2 node).
        """
        metaobj.verify_query_pane_field('Grid1',"Grid2",1,"Step08: Verify Grid2")
        metaobj.verify_query_pane_field('Rows',"Product,Category",1,"Step08: Verify Rows")
        metaobj.verify_query_pane_field('Rows',"Gender",2,"Step08: Verify Rows")
        metaobj.verify_query_pane_field('Rows',"Sale,Quarter",3,"Step08: Verify Rows")
        metaobj.verify_query_pane_field('Measure',"Revenue",1,"Step08: Verify Revenue in measure")
          
        time.sleep(4)
        parent_css1="#TableChart_3 .rowTitle text"
        resultobj.wait_for_property(parent_css1,3)
        parent_css1="#TableChart_3 .colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
          
        """
        Step09: Verify that report with relevant data is displayed in the canvas area.
        """
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 12)
        time.sleep(5)
        resultobj.verify_number_of_riser("TableChart_1", 1, 12, 'Step09: Verify the total number of risers in Bar Stacked1')
          
        parent_css="#TableChart_2 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        rise=len(self.driver.find_elements_by_css_selector(parent_css))
        utillobj.asequal(rise,7,"Step09: Verify Grid1 risers")
        
        parent_css="#TableChart_3 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 56)
        rise=len(self.driver.find_elements_by_css_selector(parent_css))
        utillobj.asequal(rise,56,"Step09: Verify Grid2 risers")
          
        time.sleep(5)
        heading = ['Product Cat...','Ge...','Sale Qu...','Revenue']
        resultobj.verify_grid_column_heading('TableChart_3',heading, 'Step09.1: Verify column titles')
        row_val=['Accessories', 'F','1','$15,704,375.50']
        resultobj.verify_grid_row_val('TableChart_3',row_val,'Step09.2: verify grid 1st row value')
        expected_tooltip=['Product Category:Accessories', 'Gender:F', 'Sale Quarter:1', 'Revenue:$15,704,375.50', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("TableChart_3","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step08.d: verify the default tooltip values")
          
        """
        Step10: Click "IA" > "Save" > "C2160087" > "Save"
        """        
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
                        
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
                        
        """
        Step11: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
         
        """
        Step12: Reopen fex using IA API:
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
         
        """
        Step13: Verify the following is displayed.
        """
        time.sleep(4)
        parent_css1="#TableChart_2 .rowTitle text"
        resultobj.wait_for_property(parent_css1,1)
        
        resultobj.verify_panel_caption_label(0, 'Grid2', "Step1: Verify Grid2 is displayed")
        resultobj.verify_panel_caption_label(1, 'Grid1', "Step12: Verify Grid1 is displayed")
        resultobj.verify_panel_caption_label(2, 'Bar Stacked1', "Step12: Verify Bar Stacked1 is displayed")
          
        time.sleep(5)
        heading = ['Product Category']
        resultobj.verify_grid_column_heading('TableChart_2',heading, 'Step13.1: Verify column titles')
        row_val=['Accessories']
        resultobj.verify_grid_row_val('TableChart_2',row_val,'Step13.2: verify grid 1st row value')
        time.sleep(2)
        metaobj.verify_query_pane_field('Grid1',"Grid2",1,"Step13: Verify Grid2")
        metaobj.verify_query_pane_field('Rows',"Product,Category",1,"Step13: Verify Rows")
        metaobj.verify_query_pane_field('Rows',"Gender",2,"Step13: Verify Rows")
        metaobj.verify_query_pane_field('Rows',"Sale,Quarter",3,"Step13: Verify Rows")
        metaobj.verify_query_pane_field('Measure',"Revenue",1,"Step13: Verify Revenue in measure")
          
        time.sleep(4)
        parent_css1="#TableChart_3 .rowTitle text"
        resultobj.wait_for_property(parent_css1,3)
        parent_css1="#TableChart_3 .colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 12)
        time.sleep(5)
        resultobj.verify_number_of_riser("TableChart_1", 1, 12, 'Step13: Verify the total number of risers in Bar Stacked1')
          
        parent_css="#TableChart_2 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        rise=len(self.driver.find_elements_by_css_selector(parent_css))
        utillobj.asequal(rise,7,"Step13: Verify Grid1 risers")
        
        parent_css="#TableChart_3 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 56)
        rise=len(self.driver.find_elements_by_css_selector(parent_css))
        utillobj.asequal(rise,56,"Step13: Verify Grid2 risers")
          
        time.sleep(5)
        heading = ['Product Cat...','Ge...','Sale Qu...','Revenue']
        resultobj.verify_grid_column_heading('TableChart_3',heading, 'Step13.1: Verify column titles')
        row_val=['Accessories', 'F','1','$15,704,375.50']
        resultobj.verify_grid_row_val('TableChart_3',row_val,'Step13.2: verify grid 1st row value')
        expected_tooltip=['Product Category:Accessories', 'Gender:F', 'Sale Quarter:1', 'Revenue:$15,704,375.50', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("TableChart_3","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step13.d: verify the default tooltip values")
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()



    
     
        