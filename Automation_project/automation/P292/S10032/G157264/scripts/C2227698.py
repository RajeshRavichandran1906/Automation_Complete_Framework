'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227698
'''
import unittest, time
from common.lib.global_variables import Global_variables
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity, core_utility
from selenium.webdriver.common.by import By

class C2227698_TestClass(BaseTestCase):
    
    def test_C2227698(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227698'
        expected_xval_list = ['2011', '2012', '2013', '2014', '2015', '2016']
#         expected_xval_list=['2016', '2017', '2018', '2019', '2020', '2021']
        expected_yval_list=['0', '0.4B', '0.8B', '1.2B','1.6B', '2B', '2.4B']
        oLegends=['Cost of Goods Local Currency','Cost of Goods']
        
        """
            CLASS OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        coreutillobj = core_utility.CoreUtillityMethods(self.driver)
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
              
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
              
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """    2. Drag "Cost of Goods,Local Currency" to Vertical Axis.    """
        metaobj.drag_drop_data_tree_items_to_query_tree("Cost of Goods,Local Currency", 1, 'Vertical Axis', 0)
        time.sleep(8)
        
        """    3. Drag "Cost of Goods" to Vertical Axis.    """
        metaobj.drag_drop_data_tree_items_to_query_tree("Cost of Goods", 1, 'Vertical Axis', 1)
        time.sleep(8)
        
        if Global_variables.browser_name == 'ie' : 
            canvas_obj = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f")
            coreutillobj.python_left_click(canvas_obj, 'top_left')
            time.sleep(5)
        
        """    4. Drag "Sale,Year" to Horizontal Axis.    """
        metaobj.drag_drop_data_tree_items_to_query_tree("Sale,Year", 1, 'Horizontal Axis', 0)
        time.sleep(8)
        
        """    5. Select "Format" > "Theme" > "Legacy Templates"    """
        ribbonobj.select_ribbon_item('Format','Theme')
                                     
        """    6. Select "ENBlue_Dark.sty" > Click "Open".    """
        #ribbonobj.select_theme('Legacy Templates', 'ENBlue_Dark.sty')
        theme_library='Legacy Templates'
        theme_library_xpath="//div[@id='paneIbfsExplorer_scTree']//td[contains(text(), '" + theme_library + "')]/img"
        lib_ele = self.driver.find_element_by_xpath(theme_library_xpath)
        coreutillobj.python_left_click(lib_ele)
#         utillobj.default_left_click(self, object_locator=lib_ele)
        parent_css="#paneIbfsExplorer_exList > div.bi-tree-view-body-content > table > tbody > tr:nth-child(10)"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.select_item_from_ibfs_explorer_list('ENBlue_Dark.sty')
        
        """    7. Verify that selected theme is applied.    """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 12)
        time.sleep(15)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Sale Year', "Step 07.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", oLegends, "Step 07.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 07.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 6, 'Step 07.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "san_marino", "Step 07.05: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!", "deep_lilac", "Step 07.06: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "background", "endeavour", "Step 07.07: Verify Outer background chart color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "chartFrame", "black", "Step 07.08: Verify inner chart frame color")
        time.sleep(1)
        
        """    8. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(10) 
        
        """    9. Verify the output has the same selected theme.    """
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Sale Year', "Step 09.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", oLegends, "Step 09.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 6, 'Step 09.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g5!mbar!", "san_marino", "Step 09.05: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g4!mbar!", "deep_lilac", "Step 09.06: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "background", "endeavour", "Step 09.07: Verify Outer background chart color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "chartFrame", "black", "Step 09.08: Verify inner chart frame color")
        time.sleep(5)
        
        """    10. Close the output window    """
        time.sleep(5)
        self.driver.close()
        time.sleep(3)
        utillobj.switch_to_window(0)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """    11. Click "Save" > Save as "C2160092" > click "Save"    """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    12. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """    13. Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2160092.fex&tool=idis        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(20)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    14. Verify Preview    """
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Sale Year', "Step 14.01: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", oLegends, "Step 14.02: Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 14.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 6, 'Step 14.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "san_marino", "Step 14.05: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g4!mbar!", "deep_lilac", "Step 14.06: Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "background", "endeavour", "Step 14.07: Verify Outer background chart color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "chartFrame", "black", "Step 14.08: Verify inner chart frame color")
        time.sleep(3)
     
        """    15. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()