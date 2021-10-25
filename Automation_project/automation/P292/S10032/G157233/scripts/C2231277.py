'''
Created on Nov 28, 2017

@author: Praveen Ramkumar
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2231277
TestCase Name = Verify restore with Choropleth Map
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib.basetestcase import BaseTestCase

class C2231277_TestClass(BaseTestCase):

    def test_C2231277(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2231277'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step 01: Launch IA Chart mode:http://machine:port/ibi_apps/ia?tool=Chart&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """      
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 02: Select Format Tab > Click "Choropleth"
        """
        ribbonobj.select_ribbon_item('Format', 'Choropleth')
        
        """
        Step 03: Verify Preview
        """
        parent_css="div[id*='pfjTableChart_1_com-esri-map'] div[class='esriControlsBR']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        elem_css = "div[id*='pfjTableChart_1_com-esri-map'] div[class='esriControlsBR']"
        utillobj.verify_object_visible(elem_css, True, "Step 03: Verify Preview")
        
        """
        Step 04:Double-click "Customer,Country"
        """
        metaobj.datatree_field_click('Customer,Country', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=15,string_value='Customer,Country', with_regular_exprestion=True)
        metaobj.verify_query_pane_field('Layer','Customer,Country',1,"Step 05.1: Verify query pane")
        
        """
        Step 05:Drag "Customer,Continent" into the Color bucket("Customer,Continent" is located under "Customer,Country" attributes)
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Customer,Continent',1, 'Color',0)
        parent_css='#queryTreeWindow tr:nth-child(7) td'
        resultobj.wait_for_property(parent_css, 1,string_value='Customer,Continent',expire_time=15)
        metaobj.verify_query_pane_field('Color BY','Customer,Continent',1,"Step 05.1: Verify query pane")
        
        """
        Step 06:Verify the Preview is updated
        """
        utillobj.verify_chart_color("TableChart_1", "riser!s5!g1!mregion!", "orange", "Step 06.1: Verify first bar color")
        legend=['Customer Continent', 'Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step 06.2: Verify legend Title")
        iaresultobj.verify_number_of_chart_segment("TableChart_1",42, 'Step 06.3: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        
        """
        Step 07:Click "Run"
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
                
        """
        Step 08:Verify the correct map is displayed at runtime
        """
        legend=['Customer Continent', 'Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 08.01: Verify legend Title")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g2!mregion!", "pale_yellow", "Step 08.02: Verify first bar color")
        time.sleep(5)
#         parent_elem=driver.find_element_by_css_selector("#jschart_HOLD_0 [class*='riser!s3!g2!mregion!']")
#         utillobj.click_on_screen(parent_elem, 'start', x_offset=85, y_offset=40)
#         time.sleep(3)
#         expected_tooltip=['Customer Country:United States', 'Customer Continent:North America']
#         resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s3!g2!mregion!",expected_tooltip, "Step 08.03: verify the default tooltip values", default_move=True)
#         time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0",42, 'Step 08.04: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
       
        """
        Step 09:Click "Save" in the toolbar > "C2231277" > click "Save"
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(8)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(8)
        
        """
        Step 10:Click "Run"
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        
        """
        Step 11:Verify output
        """
        legend=['Customer Continent', 'Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step 11.01: Verify legend Title")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g2!mregion!", "pale_yellow", "Step 11.02: Verify first bar color")
#         time.sleep(5)
#         parent_elem=driver.find_element_by_css_selector("#jschart_HOLD_0 [class*='riser!s4!g0!mregion!']")
#         utillobj.click_on_screen(parent_elem, 'start', x_offset=85, y_offset=40)
#         time.sleep(3)
#         expected_tooltip=['Customer Country:Australia', 'Customer Continent:Oceania']
#         resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s4!g0!mregion!",expected_tooltip, "Step 11.03: verify the default tooltip values", default_move=True)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0",42, 'Step 11.04: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
       
        """
        Step 12:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 13:Reopen saved FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2231277.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032_infoassist_3',mrid='mrid',mrpass='mrpass')
        time.sleep(8)
        
        """
        Step 14:Verify Preview and successful restore
        """
        iaresultobj.verify_number_of_chart_segment("TableChart_1",42, 'Step 14.2: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g2!mregion!", "pale_yellow", "Step 14.3: Verify first bar color")
        legend=['Customer Continent', 'Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step 14.4: Verify legend Title")
        
        """
        Step 15:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()        