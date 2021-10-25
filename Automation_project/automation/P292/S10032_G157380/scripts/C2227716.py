'''
Created on Jun 14, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227716
'''

import unittest, time, re
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, wf_mainpage, wf_legacymainpage
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227716_TestClass(BaseTestCase):

    def test_C2227716(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227716'
        
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        wf_legacymainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        
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
        Step04: Highlight "Product,Category" (in Query pane) > Right mouse click > "Delete"
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
        time.sleep(2)
        metaobj.querytree_field_click("Product,Category", 1, 1,'Delete')
        time.sleep(2)
        metaobj.verify_query_pane_field('Rows',"Columns",1,"Step04: Verify Product Category removed")
       
        """
        Step05: Drag "Product,Category" to Rows
        Step06: Double click "Revenue"
        Step07: Drag "Gross Profit" to "Measure"
        """
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 1, 1,'Add To Query','Rows')
        time.sleep(4)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Gross Profit", 1, 1,'Add To Query','Measure')
        time.sleep(4)
        metaobj.verify_query_pane_field('Rows',"Product,Category",1,"Step07: Verify Rows")
        metaobj.verify_query_pane_field('Measure',"Revenue",1,"Step07: Verify Revenue in measure")
        metaobj.verify_query_pane_field('Measure',"Gross Profit",2,"Step07: Verify Gross Profit in measure")
        time.sleep(4)
        parent_css1=".rowTitle text"
        resultobj.wait_for_property(parent_css1,1)
        parent_css1=".colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 2)
         
        """
        Step08: Verify the following is displayed
        """
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 12)
        time.sleep(5)
        resultobj.verify_number_of_riser("TableChart_1", 1, 12, 'Step08: Verify the total number of risers in Bar Stacked1')
        parent_css="#TableChart_2 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 14)
        time.sleep(5)
        heading = ['Product Category', 'Revenue','Gross Profit']
        resultobj.verify_grid_column_heading('TableChart_2',heading, 'Step08.1: Verify column titles')
        row_val=['Accessories', '$129,608,338.53','$39,854,440.53']
        resultobj.verify_grid_row_val('TableChart_2',row_val,'Step08.2: verify grid 1st row value')
        expected_tooltip=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("TableChart_2","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step08.d: verify the default tooltip values")
         
        """
        Step09: Click "IA" > "Save" > "C2160087" > "Save"
        """        
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
                       
        """
        Step10: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step11: Log on to WF:
        Step12: Highlight "C2160087" > Right mouse click > Verify Edit options
        Step13: Select Edit With... > InfoAssist+
        """
        utillobj.invoke_webfocu('mrid','mrpass')
        time.sleep(10)
        prid=utillobj.parseinitfile('project_id')
        suid=utillobj.parseinitfile('suite_id')
        node=utillobj.parseinitfile('nodeid')
        if bool(re.match('wfinst.*',node)):
            wf_mainobj.select_repository_folder_item_menu(prid+'->'+suid,'C2227716', 'Edit')
        else:
            wf_legacymainobj.select_repository_menu(prid+'->'+suid+'->C2227716', 'Edit With...')
            time.sleep(5)
            utillobj.select_or_verify_bipop_menu('InfoAssist+')
        time.sleep(5)
        utillobj.switch_to_window(1)
        time.sleep(15)   
        
        """
        Step14: Verify the following is displayed.
        """
        time.sleep(4)
        parent_css1=".rowTitle text"
        resultobj.wait_for_property(parent_css1,1)
        parent_css1=".colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 2)
        metaobj.verify_query_pane_field('Rows',"Product,Category",1,"Step14: Verify Rows")
        metaobj.verify_query_pane_field('Measure',"Revenue",1,"Step14: Verify Revenue in measure")
        metaobj.verify_query_pane_field('Measure',"Gross Profit",2,"Step14: Verify Gross Profit in measure")
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 12)
        time.sleep(5)
        resultobj.verify_number_of_riser("TableChart_1", 1, 12, 'Step14: Verify the total number of risers in Bar Stacked1')
        parent_css="#TableChart_2 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 14)
        time.sleep(5)
        heading = ['Product Category', 'Revenue','Gross Profit']
        resultobj.verify_grid_column_heading('TableChart_2',heading, 'Step14.1: Verify column titles')
        row_val=['Accessories', '$129,608,338.53','$39,854,440.53']
        resultobj.verify_grid_row_val('TableChart_2',row_val,'Step14.2: verify grid 1st row value')
        expected_tooltip=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("TableChart_2","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step14.d: verify the default tooltip values")
 

if __name__ == '__main__':
    unittest.main()