'''
Created on Jun 11, 2018

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2020965
TestCase Name =  Workflow:Natural Disasters test scenario 
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_properties
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2020965_TestClass(BaseTestCase):

    def test_C2020965(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2020965'
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=idis&master=baseapp/natural_disasterfoc
        """
        utillobj.infoassist_api_login('idis','baseapp/natural_disasterfoc','P292/S10032_esrimap_2', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
          
        """
        Step 02: Select "Home" > "Visual" > "Change" (dropdown) > "ESRI Map: Bubble".
        """
        ribbonobj.change_chart_type("bubble_map")
        time.sleep(5)
        
        """
        Step 03: Drag "State" to "Location - Layer".
        """
        metaobj.drag_drop_data_tree_items_to_query_tree_('Dimensions->State', 1, 'Layer',0)
        
        """
        Step 04: Verify "Map State" window is displayed.
        Step 05: Select "Geographic Role" (drop down) > "US State"
        Step 06: Click "OK"
        """
        parent_css='#geoRoleCancelBtn'
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        set_geo_role_obj=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[id$='GeoRoleBox'][style*='left'] div[id^='BiButton']")
        utillobj.click_on_screen(set_geo_role_obj, 'middle', click_type=0)
        time.sleep(2)
        menu_items=self.driver.find_elements_by_css_selector("div[id^='BiPopup'][style*='inherit'] div[id^='BiComboBoxItem']")
        actual_popup_list=[el.text.strip() for el in menu_items]
        utillobj.default_click(menu_items[actual_popup_list.index('US State')], mouse_duration=1)
        time.sleep(1)
        self.driver.find_element_by_css_selector("#geoRoleOkBtn").click()
#         wfmapobj.set_geo_role(role_name='US State', btn_click='Ok')
        
        """
        Step 07: Verify the following map is displayed.
        """
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 43, 30)
        metaobj.verify_query_pane_field('Layer', 'State', 1, "Step07.a(i): Verify query pane Car under the Horizontal axis bucket")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 43, 'Step 07.b: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker!", "bar_blue", "Step 07.c(i) Verify first bar color")
        time.sleep(5)
        
        """
        Step 08: Drag "Fatalities" to Marker - Size.
        """
        metaobj.drag_drop_data_tree_items_to_query_tree_('Measures->Fatalities', 1, 'Size',0)
        parent_css="#MAINTABLE_wbody1 text[class*='legend-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
#         metaobj.drag_drop_data_tree_items_to_query_tree('Sale,Quarter', 1, 'Columns', 0)
        
        """
        Step 09: Drag "Type" to Marker - Color.
        """
        metaobj.drag_drop_data_tree_items_to_query_tree_('Dimensions->Type', 1, 'Color',0)
        
        """
        Step 10: Verify the following map is displayed.
        """
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 68, 30)
        parent_css="#MAINTABLE_wbody1 .legend text"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 30)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 68, 'Step 10.b: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g16!mmarker!", "dark_green", "Step 10.c(i) Verify first bar color")
        legend=['Type', 'Earthquake', 'Hurricane', 'Tornado', 'Wildfire', 'Fatalities', '1,956', '978']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step10:d(i) Verify legend Title")
        time.sleep(5)
        
        """
        Step 11: Drag "Type" to the "Filter" pane.
        """
        metaobj.drag_drop_data_tree_items_to_filter('Dimensions->Type', 1)
        
        """
        Step 12: Uncheck "Show Prompt" checkbox on "Filter for Type" window.
        Step 13: Click "OK"
        """
        parent_css="#avFilterOkBtn"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        metaobj.create_visualization_filters('alpha', ['ShowPrompt', True])
        time.sleep(2)
        
        """
        Step 14: Verify "Type" has been placed onto the "Filter" pane.
        """
        parent_css="#avFilterOkBtn"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        metaobj.verify_filter_pane_field('Type',1,"Step 14: Verify 'Sale,Month Name' appears in filter pane")
        
        """
        Step 15: Click the "Pan" button and use the left mouse button to select few bubbles (near Florida region) to lasso (filter) a few data.
        Step 16: Click the "Filter Chart" option.
        """        
        pan_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1 div[class^='SelectionButton UIButton toggleModePan']")
        utillobj.click_on_screen(pan_css, coordinate_type='middle', click_type=0)
        time.sleep(3)
        riser="#MAINTABLE_wbody1 circle[class*='riser!s2!g16!mmarker!']"
        utillobj.synchronize_with_number_of_element(riser, 1, 30)
        
        source=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 circle[class*='riser!s2!g16!mmarker!']")
        target=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 circle[class*='riser!s1!g2!mmarker!']")
        
        utillobj.drag_to_using_pyautogui(source, target,sx_offset=-25,tx_offset=55,sy_offset=-25,ty_offset=25)
#         menu=['21 points', 'Filter Chart', 'Exclude from Chart']
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        time.sleep(5)
#         utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_2',mrid='mrid',mrpass='mrpass')

        """
        Step 17: Verify map is updated to show Florida region with different Types of disasters.
        """
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 25, 30)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 25, 'Step 17.b: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g8!mmarker!", "dark_green", "Step 17.c(i) Verify first bar color")
        legend=['Type', 'Earthquake', 'Hurricane', 'Tornado', 'Wildfire', 'Fatalities', '1,956', '978']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step17:c Verify legends Title")
        
        """
        Step 18: Verify the following filters displayed in the "Filter" pane.
        """
        time.sleep(3)
        metaobj.verify_filter_pane_field('Type' ,1, "Step 18.a: ")
        metaobj.verify_filter_pane_field('STATE and TYPE' ,2, "Step 18.b: ")
        
        """
        Step 19: Hover over any bubble and verify that tooltip is displaying proper information.
        """
        time.sleep(5)
        expected_tooltip=['State:MO', 'Fatalities:215', 'Type:Tornado', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s2!g8!mmarker!", expected_tooltip, "Step19: verify the default tooltip values")       
        
        """
        Step 20: Highlight the new filter, right mouse click and delete them.
        """
        time.sleep(5)
        metaobj.filter_tree_field_click('STATE and TYPE', 1, 1,"Delete")
        
        """
        Step 21: Highlight "Type" in "Filter" pane > Right mouse click > "Show Prompt".
        """
        metaobj.filter_tree_field_click("Type", 1, 1, "Show Prompt")
        
        """
        Step 22: Verify "Type" prompt is showing in the rightmost area of the canvas.
        """
        propertyobj.select_or_verify_show_prompt_item('1', '[All]',verify=True, verify_type=True,msg="Step 22:Verify prompt [All] is checked")
        time.sleep(5)
        
        """
        Step 23: In "Type" prompt, select "Hurricane","Tornado".
        """
        propertyobj.select_or_verify_show_prompt_item('1', 'Hurricane')
        time.sleep(2)
        propertyobj.select_or_verify_show_prompt_item('1', 'Tornado')
        time.sleep(2)
        
        """
        Step 24: Verify the following map is displayed.
        """
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 43, 30)
        propertyobj.select_or_verify_show_prompt_item('1', 'Hurricane',verify=True, verify_type=True,msg="Step 24a:Verify prompt Hurricane is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Tornado',verify=True, verify_type=True,msg="Step 24b:Verify prompt Tornado is checked")
        metaobj.verify_filter_pane_field('Type',1,"Step24.c:Verify Filter pane")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 43, 'Step24.d: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mmarker!", "bar_blue", "Step 24.e: Verify first bar color")
        legend=['Type', 'Hurricane', 'Tornado', 'Fatalities', '1,956', '978']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 24.f Verify legends Title")
        
        """
        Step 25: Select "Home" > "Insert" > "Grid".
        """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Grid')
        
        """
        Step 26: Double click "Fatalities", "Type"
        """
        metaobj.datatree_field_click("Measures->Fatalities", 2, 1)
        parent_css="#MAINTABLE_wbody2 .colHeaderScroll text"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        metaobj.datatree_field_click("Dimensions->Type", 2, 1)
        parent_css="#MAINTABLE_wbody2 .rowTitle text"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 27: Verify the following is displayed for "Grid" Query pane.
        """
        metaobj.verify_query_pane_field('Rows',"Type",1,"Step 27.a")
        metaobj.verify_query_pane_field('Measure',"Fatalities",1,"Step 27.b")
        
        """
        Step 28: Verify the following is displayed.
        """
        heading = ['Type', 'Fatalities']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody2',heading, 'Step 28.a: Verify column titles')
        row_val=['Hurricane', '2713']
        resultobj.verify_grid_row_val('MAINTABLE_wbody2',row_val,'Step 28.b: verify grid 1st row value')
                  
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 43, 30)
        metaobj.verify_filter_pane_field('Type',1,"Step 28.c:Verify Filter pane")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 43, 'Step 28.d: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mmarker!", "bar_blue", "Step 28.e: Verify first bar color")
        legend=['Type', 'Hurricane', 'Tornado', 'Fatalities', '1,956', '978']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 28.f Verify legends Title")
        propertyobj.select_or_verify_show_prompt_item('1', 'Hurricane',verify=True, verify_type=True,msg="Step 28.g:Verify prompt Hurricane is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Tornado',verify=True, verify_type=True,msg="Step 28.h:Verify prompt Tornado is checked")
        
        """
        Step 29: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
        """
        Step 30: Verify the following is displayed.
        """
        parent_css="#MAINTABLE_wbody2 .colHeaderScroll text"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        parent_css="#MAINTABLE_wbody2 .rowTitle text"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        heading = ['Type', 'Fatalities']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody2',heading, 'Step 30.a: Verify column titles')
        row_val=['Hurricane', '2713']
        resultobj.verify_grid_row_val('MAINTABLE_wbody2',row_val,'Step 30.b: verify grid 1st row value')
                  
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 43, 30)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 43, 'Step 30.d: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mmarker!", "bar_blue", "Step 30.e: Verify first bar color")
        legend=['Type', 'Hurricane', 'Tornado', 'Fatalities', '1,956', '978']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 30.f Verify legends Title")
        propertyobj.select_or_verify_show_prompt_item('1', 'Hurricane',verify=True, verify_type=True,msg="Step 30.g:Verify prompt Hurricane is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Tornado',verify=True, verify_type=True,msg="Step 30.h:Verify prompt Tornado is checked")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2020965_Actual_step30', image_type='actual',x=1, y=1, w=-1, h=-1)
                             
        """
        Step 31: Dismiss the "Run" window.
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1) 
       
        """
        Step 32: Click "IA" > "Save" > "C2020965" > "Save"
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
                   
        """
        Step 33: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
               
        """
        Step 34: Reopen fex using IA API: http://machine:port/alias/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2020965.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_4',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
                  
        """
        Step 35: Verify the following is displayed.
        """
        parent_css="#MAINTABLE_wbody2 .colHeaderScroll text"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        parent_css="#MAINTABLE_wbody2 .rowTitle text"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        heading = ['Type', 'Fatalities']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody2',heading, 'Step 35.a: Verify column titles')
        row_val=['Hurricane', '2713']
        resultobj.verify_grid_row_val('MAINTABLE_wbody2',row_val,'Step 35.b: verify grid 1st row value')
                  
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 43, 30)
        metaobj.verify_filter_pane_field('Type',1,"Step 35.c:Verify Filter pane")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 43, 'Step 35.d: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mmarker!", "bar_blue", "Step 35.e: Verify first bar color")
        legend=['Type', 'Hurricane', 'Tornado', 'Fatalities', '1,956', '978']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 35.f Verify legends Title")
        propertyobj.select_or_verify_show_prompt_item('1', 'Hurricane',verify=True, verify_type=True,msg="Step 35.g:Verify prompt Hurricane is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Tornado',verify=True, verify_type=True,msg="Step 35.h:Verify prompt Tornado is checked")
        
        """
        Step 36: Logout: http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()