'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227698
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227698_TestClass(BaseTestCase):
    def test_C2227698(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227698'
        bar1=['Sale Year:2014', 'Cost of Goods Local Currency:540,969,939.93', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        bar2=['Sale Year:2016', 'Cost of Goods:$325,821,316.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        expected_xval_list=['2011', '2012', '2013', '2014', '2015', '2016']
        expected_yval_list=['0', '0.4B', '0.8B', '1.2B','1.6B', '2B', '2.4B']
        oLegends=['Cost of Goods Local Currency','Cost of Goods']
        
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
        
        """    2. Drag "Cost of Goods,Local Currency" to Vertical Axis.    """
        metaobj.datatree_field_click("Cost of Goods,Local Currency", 2, 1)
        time.sleep(8)
        
        """    3. Drag "Cost of Goods" to Vertical Axis.    """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(8)
        
        """    4. Drag "Sale,Year" to Horizontal Axis.    """
        metaobj.datatree_field_click("Sale,Year", 2, 1)
        time.sleep(8)
        
        """    5. Select "Format" > "Theme" > "Legacy Templates"    """
        ribbonobj.select_ribbon_item('Format','Theme')
                                     
        """    6. Select "ENBlue_Dark.sty" > Click "Open".    """
        #ribbonobj.select_theme('Legacy Templates', 'ENBlue_Dark.sty')
        theme_library='Legacy Templates'
        theme_library_xpath="//div[@id='paneIbfsExplorer_scTree']//td[contains(text(), '" + theme_library + "')]/img"
        lib_ele = self.driver.find_element_by_xpath(theme_library_xpath)
        utillobj.default_left_click(self, object_locator=lib_ele)
        utillobj.select_item_from_ibfs_explorer_list('ENBlue_Dark.sty')
        
        """    7. Verify that selected theme is applied.    """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 12)
        time.sleep(15)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!", bar1, "Step 7(i): Verify Cost of Goods Local Currency bar value")
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g5!mbar!", bar2, "Step 7(ii): Verify Cost of Goods bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Sale Year', "Step18:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", oLegends, "Step 7:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 7:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 6, 'Step 7.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "san_marino", "Step 7.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!", "deep_lilac", "Step 7.c(ii): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "background", "endeavour", "Step 7.c(iii): Verify Outer background chart color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "chartFrame", "black", "Step 7.c(iv): Verify inner chart frame color")
        time.sleep(1)
        
        """    8. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(10) 
        
        """    9. Verify the output has the same selected theme.    """
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!", bar1, "Step 9(i): Verify Cost of Goods Local Currency bar value")
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g5!mbar!", bar2, "Step 9(ii): Verify Cost of Goods bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Sale Year', "Step 9:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", oLegends, "Step 9:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 9.a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 6, 'Step 9.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g5!mbar!", "san_marino", "Step 9.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g4!mbar!", "deep_lilac", "Step 9.c(ii): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "background", "endeavour", "Step 9.c(1ii): Verify Outer background chart color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "chartFrame", "black", "Step 9.c(iii): Verify inner chart frame color")
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
        ribbonobj.select_tool_menu_item('menu_save_as')
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
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!", bar1, "Step 14(i): Verify Cost of Goods Local Currency bar value")
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g5!mbar!", bar2, "Step 14(ii): Verify Cost of Goods bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Sale Year', "Step 14:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", oLegends, "Step 14:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 14:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 6, 'Step 14.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "san_marino", "Step 14.c(i): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g4!mbar!", "deep_lilac", "Step 14.c(ii): Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "background", "endeavour", "Step 14.c(iii): Verify Outer background chart color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "chartFrame", "black", "Step 14.c(iv): Verify inner chart frame color")
        time.sleep(5)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step14', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    15. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()

