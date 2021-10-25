'''
Created on September 10, 2018
@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227609
'''
import time
import unittest
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization
from common.pages import visualization_resultarea, visualization_ribbon,ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators

class C6670551_TestClass(BaseTestCase):
    
    def test_C6670551(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C6670551'
        query_tree_css = '#queryTreeWindow'
        
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        visualization = Visualization(self.driver)
        
        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
           
        """
        Step02: Select "Home" > "Visual" > "Change" (dropdown) > "Map".
        Step03: Set "Territory" = "World".
        Step04: Click "OK".
        """
        ribbonobj.change_chart_type('map')
        time.sleep(3)
        ribbonobj.select_map('choropleth',teritory='World',btn_click='ok')
        time.sleep(3) 
        parent_css="div.leaflet-control-scale-line"
        resultobj.wait_for_property(parent_css,2)      
           
        """
        Step03: Locate and double click "Customer,Country,ISO-3166,Code", under Customer Dimension
        Step04: Verify "Location Type" dialog box displayed.
        Step05: Set "Geographic Role" = "iso_a2 (...)".
        Step06: Click "OK".
        """
        visualization.double_click_on_datetree_item("Customer,Country,ISO-3166,Code", 1)
        visualization.wait_for_visible_text(query_tree_css, "Customer,Country,ISO-3166,Code")
        
        css="#locTypeOkBtn"
        cap="div[id^='QbDialog'] [class*='active'] [class*='caption'] [class*='bi-label']"
        utillobj.verify_popup(css, "Step04: Verify dialog box displayed")
        a=self.driver.find_elements_by_css_selector(cap)
        utillobj.asequal(a[len(a)-1].text,"Location Type", "StepX: Verify Caption text in popup")
        combo_btn=self.driver.find_element_by_css_selector("div[id^='QbDialog'] #geoRoleComboBox div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_btn,"iso_a2 (AD, AE, AF)")
        time.sleep(2)
        btn_css="div[id*='locTypeOkBtn'] div[class=bi-button-label]"
        self.driver.find_element_by_css_selector(btn_css).click()
        time.sleep(2)
          
        """
        Step09: Double-click "Gross Profit" from Sales
        """
        visualization.double_click_on_datetree_item("Gross Profit", 1)
        visualization.wait_for_visible_text(query_tree_css, "Gross Profit")
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 42)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
           
        """
        Step10: Verify Preview
        Step11: Hover over Brazil > Verify menu
        """
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",42, 'Step10.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mstate", "burnt_sienna", "Step10.c(i) Verify first bar color")
        legend=['Gross Profit', '0M', '23.5M', '47M', '70.5M', '94M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step10:d(i) Verify legend Title")
        expected_tooltip=['Customer Country ISO-3166 Code:BR', 'Gross Profit:$11,022,235.68', 'Filter Chart', 'Exclude from Chart']
        visualization.verify_tooltip("riser!s0!g4!mstate", expected_tooltip, "Step 11 : verify the default tooltip values")
        time.sleep(5)
        
        """
        Step12: Select "Filter Chart" > Verify Preview
        """ 
        visualization.select_tooltip("riser!s0!g4!mstate", "Filter Chart")
        parent_css2="#MAINTABLE_wbody1 [class*='riser!s']"
        resultobj.wait_for_property(parent_css2,1)
            
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",1, 'Step12.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mstate", "persian_red", "Step12.c(i) Verify first bar color")
        legend=['Gross Profit', '11,022.2K', '11,146.2K', '11,270.2K', '11,394.2K', '11,518.2K']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step12:d(i) Verify legend Title")
        
        """
        Step13: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        time.sleep(10) 
                 
        """
        Step14: Hover over Brazil > Verify menu
        """
        parent_css2="#MAINTABLE_wbody1 [class*='riser!s']"
        resultobj.wait_for_property(parent_css2,1)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",1, 'Step14.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mstate", "persian_red", "Step14.c(i) Verify first bar color")
        legend=['Gross Profit', '11,022.2K', '11,146.2K', '11,270.2K', '11,394.2K', '11,518.2K']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step14:d(i) Verify legend Title")
            
        """
        Step15: Close the output window
        Step16: Click Save in thetoolbar, Save as "C2158150" > Click Save
        """
        self.driver.close()
        utillobj.switch_to_window(0)

        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
            
        """
        Step17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
    
        """
        Step19: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158150.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_2',mrid='mrid',mrpass='mrpass')
             
        """
        Step20: Verify canvas
        """
        parent_css2="#MAINTABLE_wbody1 [class*='riser!s']"
        resultobj.wait_for_property(parent_css2,1)
            
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",1, 'Step20.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mstate", "persian_red", "Step20.c(i) Verify first bar color")
        legend=['Gross Profit', '11,022.2K', '11,146.2K', '11,270.2K', '11,394.2K', '11,518.2K']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step20:d(i) Verify legend Title")
                   
if __name__ == '__main__':
    unittest.main()
