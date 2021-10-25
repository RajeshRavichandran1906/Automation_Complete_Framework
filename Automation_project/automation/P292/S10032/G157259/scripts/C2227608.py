'''
Created on Jun'13 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227608'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_resultarea
from common.lib import utillity
from common.lib import core_utility
from common.wftools import visualization

class C2227608_TestClass(BaseTestCase):
    
    def test_C2227608(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227608'

        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        visual_obj = visualization.Visualization(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
        elem = "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(elem, 1, metaobj.chart_long_timesleep)
           
        """
        Step02: Click "Change" dropdown > "Map"
        Step03: Select "Leaflet Bubble" > OK
        """
        ribbonobj.change_chart_type('map')
        ribbonobj.select_map('bubble')
        ribbonobj.select_map('bubble',btn_click='ok')
        parent_css="div.leaflet-control-scale-line"
        resultobj.wait_for_property(parent_css,2)
         
        """
        Step04: Double click "Store,State,Province"
        Step05: Select "state_name" from Geographic Role dropdown > OK
        Step06: Double click "Gross Profit"
        """
        metaobj.datatree_field_click("Store,State,Province", 2, 1)
        combo_btn=utillobj.validate_and_get_webdriver_object("div[id^='QbDialog'] #geoRoleComboBox div[id^='BiButton']", 'combo-box')
        utillobj.select_any_combobox_item(combo_btn,"state_name (Alabama, Alaska, Arizona)")
        btn_css="div[id*='locTypeOkBtn'] div[class=bi-button-label]"
        utillobj.validate_and_get_webdriver_object(btn_css, 'btn-css').click()
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 36)
          
        """
        Step07: Click "Pan" in the map canvas
        """        
        pan_css=utillobj.validate_and_get_webdriver_object("#MAINTABLE_wbody1 button[class^='data-selection-button leaflet-control']", 'leaflet')
        core_utillobj.left_click(pan_css)
           
        """
        Step08: Lasso "Maine", "New York", "Massachusetts" bubbles (as shown in the screenshot)
        Step09: Verify Lasso Menu
        Step10: Select "Exclude from Chart"
        Step11: Verify the map is updated
        """
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1 [class*='riser!s0!g50!mstate']", 1, metaobj.chart_medium_timesleep)
        source=utillobj.validate_and_get_webdriver_object("#MAINTABLE_wbody1 path[class*='riser!s0!g50!mstate']", 'source')
        target=utillobj.validate_and_get_webdriver_object("#MAINTABLE_wbody1 path[class*='riser!s0!g41!mstate']", 'target')
        visual_obj.create_lasso(source, target, source_xoffset=-10, source_yoffset= 20, target_xoffset=25, target_yoffset=-10)
        menu=['3 points', 'Filter Chart', 'Exclude from Chart', 'Group Store,State,Province Selection']
        visual_obj.verify_lasso_tooltip(menu, 'Step 11: Verify tooltip')
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        metaobj.verify_filter_pane_field('Store,State,Province',1,"Step11.a:Verify Filter pane")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step11.a: Verify number of bubble displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g25!mstate", "bar_blue", "Step 11.b: Verify first bar color")
        legend=['Gross Profit', 'Gross Profit', '92.2M', '46.1M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step11:c Verify legends Title")
         
        """
        Step12:Click "Run"
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utillobj.switch_to_new_window()
         
        """
        Step13: Verify the map runs in a new window
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step13.a: Verify number of bubble displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g25!mstate", "bar_blue", "Step13.b: Verify first bar color")
        legend=['Gross Profit', 'Gross Profit', '92.2M', '46.1M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step13:c Verify legends Title")
         
        """
        Step14: Click "Pan" in the map canvas
        Step15: Lasso all bubbles except Alaska and Hawaii
        Step16: Select "Filter Chart"
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        pan_css=utillobj.validate_and_get_webdriver_object("#MAINTABLE_wbody1 button[class^='data-selection-button leaflet-control']", 'leaflet')
        core_utillobj.left_click(pan_css)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1 [class*='riser!s0!g69!mstate']", 1, metaobj.chart_long_timesleep)
        source=utillobj.validate_and_get_webdriver_object("#MAINTABLE_wbody1 path[class*='riser!s0!g69!mstate']", 'source')
        target=utillobj.validate_and_get_webdriver_object("#MAINTABLE_wbody1 path[class*='riser!s0!g19!mstate']", 'target')
        visual_obj.create_lasso(source, target, source_xoffset=-30, source_yoffset= -30, target_xoffset=150, target_yoffset=100)
        visual_obj.select_lasso_tooltip('Filter Chart')
         
        """
        Step17: Verify the map is updated
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 31)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 31, 'Step17.a: Verify number of bubble displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g7!mstate", "bar_blue", "Step 17.b: Verify first bar color")
        legend=['Gross Profit', 'Gross Profit', '92.2M', '46.3M', '0.3M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step17:c Verify legends Title")
          
        """
        Step18: Click Save in the toolbar
        Step19: Save as "C2158150" > Click Save
        """
        core_utillobj.switch_to_previous_window()
        utillobj.synchronize_with_number_of_element("#applicationButton img", 1, metaobj.chart_medium_timesleep)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
          
        """
        Step20: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
         
        """
        Step21: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158150.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_2',mrid='mrid',mrpass='mrpass')
          
        """
        Step22: Verify canvas
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        metaobj.verify_filter_pane_field('Store,State,Province',1,"Step22.a:Verify Filter pane")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step22.a: Verify number of bubble displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g25!mstate", "bar_blue", "Step22.b: Verify first bar color")
        legend=['Gross Profit', 'Gross Profit', '92.2M', '46.1M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step22:c Verify legends Title")
        
if __name__ == '__main__':
    unittest.main()