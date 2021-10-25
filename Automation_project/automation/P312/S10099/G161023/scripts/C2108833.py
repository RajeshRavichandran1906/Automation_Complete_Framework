'''
Created on May'30, 2016
@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2108833
'''
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run
from common.lib import utillity, javascript



class C2108833_TestClass(BaseTestCase):
    

    def test_C2108833(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2108833'
        """
            Step 01: Launch the IA API with wf_retail_lite
            http://machine:port/ibi_apps/ia?tool=idis&master=retail_samples/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S8357', 'mrid', 'mrpass')
        element_css="#resultArea svg>g.chartPanel rect[class*='riser!']"
        utillobj.synchronize_with_number_of_element(element_css, 12, 60)
        time.sleep(2)
        def select_combobox_item_av(combo_id, combo_item):
            """
            Syntax: utillobj.select_combobox_item('comboSourceFields', 'Equals to')
            """
            self.driver.find_element_by_css_selector("div[id*=" + combo_id + "] div[id^='BiButton']").click()
            time.sleep(2)
            menu_items=self.driver.find_elements_by_css_selector("div[id^='BiPopup'][style*='inherit'] div[id^='BiComboBoxItem']")
            actual_popup_list=[el.text.strip() for el in menu_items]
            menu_items[actual_popup_list.index(combo_item)].click()
            time.sleep(1)
        """
            Step 02: Change to Grid
        """
        ribbonobj.change_chart_type('grid')
         
        """
            Step 03: Add Sale,Year, Sale,Month,Product Category,Store Business region,Customer Business region,Revenue,Gross profit and Cost of goods sold.
        """
        #REASON - While application gets hanging webdriver will be unable access the DOM , hence webdriver mostly will fail here soto handle this 
        #instance sleep used here. 
         
        time.sleep(7)
        metaobj.datatree_field_click("Sale,Year", 2, 1)
        metaobj.datatree_field_click("Sale,Month", 2, 1)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(5)
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 3)
        metaobj.datatree_field_click("Store,Business,Region", 2, 1)
        time.sleep(5)
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 4)
        metaobj.datatree_field_click("Customer,Business,Region", 2, 1)
        time.sleep(5) 
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 5)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(5) 
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".colHeader text")) == 1)
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        time.sleep(5)
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".colHeader text")) == 2)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(5)
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".colHeader text")) == 3)
         
        """
        Step 04:verify first and last two rows values
        """
        time.sleep(5)
        list2 =['Sale Year', 'Sale Month', 'Product Category', 'Store Business Region', 'Customer Business Region', 'Revenue', 'Gross Profit', 'Cost of Goods']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',list2, 'Step 04.1: Verify field titles')
        row_val=['2011', '1', 'Accessories', 'EMEA', 'EMEA', '$243,497.42', '$77,581.42', '$165,916.00']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val,'Step 04.2: verify grid 1st row value')
         
        """
        Step 05: Drag and drop Sale,Month to filter pane and click ok
        """
        metaobj.drag_drop_data_tree_items_to_filter("Sale,Month",0)
        metaobj.create_visualization_filters('numeric')
         
        """
        Step 06: Verify range values in filter prompt
        """
        time.sleep(5)
        parent_css="#qbFilterBox table>tbody>tr img"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox'] div[id^='slider'][class*='ui-slider']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(8)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',1,'int',msg="Step06: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',12,'int',msg="Step06: Verify filter prompt range values- max")
        
         
        """
        Step 07: Insert chart
        """
        ribbonobj.select_ribbon_item('Home', 'Insert', opt='Chart')
        time.sleep(6)
        parent_css="#TableChart_2 svg g[class='risers']"
        resultobj.wait_for_property(parent_css, 1)
         
        """
        Step 08: Change to Bubble map
        """
        ribbonobj.change_chart_type("bubble_map")
        parent_css="#TableChart_2 div[id$='zoom_slider']"
        resultobj.wait_for_property(parent_css, 1)
         
        """
        Step 09: Add Customer,Country to layer
        """
        obj_css="#resultArea div[class*='dv-mini-window-checked'] span.esriAttributionLastItem"
        utillity.UtillityMethods.synchronize_with_visble_text(self, obj_css, 'Esri', 30)
        metaobj.datatree_field_click("Customer,Country", 2, 1)
         
        """
        Step 10: Verify label value
        """
        time.sleep(12)
        parent_css="#MAINTABLE_wbody2 svg g text[class^='legend-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 90, 1)
        a=['Customer Country']
#         resultobj.verify_riser_legends("TableChart_2",a, "Step 10: Verify label value")
        elements_object=self.driver.find_elements_by_css_selector("#TableChart_2 .legend text")
        temp_list = javascript.JavaScript.get_elements_text(self, elements_object)
        utillobj.as_List_equal(a,temp_list, "Step 10: Verify label value Customer Country")
         
        """
        Step 11: Insert chart and change to bubble map
        """
        ribbonobj.select_ribbon_item('Home', 'Insert', opt='Chart')
        time.sleep(6)
        parent_css="#TableChart_3 svg g[class='risers']"
        resultobj.wait_for_property(parent_css, 1)
        ribbonobj.change_chart_type("bubble_map")
        parent_css="#TableChart_3 div[id$='zoom_slider']"
        resultobj.wait_for_property(parent_css, 1)
         
        """
        Step 12: Add Store,Country to layer.
        """
        obj_css="#resultArea div[class*='dv-mini-window-checked'] span.esriAttributionLastItem"
        utillity.UtillityMethods.synchronize_with_visble_text(self, obj_css, 'Esri', 30)
        metaobj.datatree_field_click("Store,Country", 2, 1)
        time.sleep(15)
         
        """
        Step 13: verify label value.
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody3 svg g text[class^='legend-labels']"
        resultobj.wait_for_property(parent_css, 1)
        a=['Store Country']
        elements_object=self.driver.find_elements_by_css_selector("#TableChart_3 .legend text")
        temp_list = javascript.JavaScript.get_elements_text(self, elements_object)
        utillobj.as_List_equal(a,temp_list, "Step 13: Verify label value Store Country")
#         resultobj.verify_riser_legends("TableChart_3",a, "Step 13: Verify label value")
 
        """
        Step 14: Drag and drop bubble map1 and place at bottom of the grid.
        """
        resultobj.drag_and_drop_visualization("BubbleMap1","Grid1","bottom")
        time.sleep(15)        
        elem = (By.CSS_SELECTOR,'#MAINTABLE_wbody1 g.tablePanel')
        resultobj._validate_page(elem)
        time.sleep(50)
         
        """
        Step 15: Drag and drop bubble map2 and place at right corner of bubble map1.
        """
        resultobj.drag_and_drop_visualization("BubbleMap2", "BubbleMap1","right")
        elem = (By.CSS_SELECTOR,'#MAINTABLE_wbody1 g.tablePanel')
        resultobj._validate_page(elem)
        time.sleep(50)
         
        """
        Step 16: Drag and drop Sale,Year to filter pane.
        """
        metaobj.datatree_field_click("Sale,Year", 1, 1,"Filter")
        time.sleep(15)
         
        """
        Step 17: Modify the operator to Equal to, select 2013 and click ok.
        """  
        time.sleep(4)
        l= ['[All]','2013']
        metaobj.create_visualization_filters('numeric',['Operator','Equal to'],['GridItems',l])
         
        """
        Step 18: Verify query added to filter
        """
        time.sleep(15)
        metaobj.verify_filter_pane_field("Sale,Year", 2,"Step 18: Verify Sale Year added to filter")
         
        """
        Step 19: Verify sale year column in grid has only 2013
        """
        time.sleep(6)
        c=['2...', '1', 'Acc...', 'EMEA', 'EMEA', '$588,586.44', '$178,259.44', '$410,327.00']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',c,'Step 19: Verify sale year column in grid has only 2013')
         
        """
        Step 20: Drag and drop Customer,Country to filter pane, accept default values and click ok
        """
#         utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10099_4',mrid='mrid', mrpass='mrpass')
#         elem = (By.CSS_SELECTOR,'#MAINTABLE_wbody1 g.tablePanel')
#         resultobj._validate_page(elem)
        time.sleep(3)
        metaobj.datatree_field_click("Customer,Country", 1, 1,"Filter")
        time.sleep(3)
        metaobj.create_visualization_filters('alpha')
        
        """
        Step 21: verify query added to filter pane
        """
        parent_css="#qbFilterWindow #qbFilterBox table td img"
        resultobj.wait_for_property(parent_css, 3)
        time.sleep(5)         
        metaobj.verify_filter_pane_field("Customer,Country", 3, "Step 21: verify Customer Country added to filter pane")
        
        """
        Step 22: Click on icon at right corner of Customer,Country filter prompt and select Dropdown
        """
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item(3, "United States")
        time.sleep(5)
        propertyobj.change_prompt_options("3", "Dropdown (Single Select)")

        """
        Step 23: Verify query added to filter pane.
        """
        time.sleep(3)
        metaobj.verify_filter_pane_field("Sale,Month", 1, "Step 23: Verify Sale Month added to filter pane.")
        
        """
        Step 24: Change Customer,Country value to United states
        """
        propertyobj.filter_prompt_select_drop_down("3", "United States")
        
        """
        Step 25: Verify bubble maps display only 'United States value'
        """
        time.sleep(20)
        map1_bubble=['Customer Country:United States', 'Drill down to Customer State Province']
        map2_bubble=['Store Country:United States', 'Drill down to Store State Province']

        resultobj.verify_default_tooltip_values("MAINTABLE_wbody3",  "riser!s0!g0!mmarker", map2_bubble, "Step 25: Verify bubble map2 display only 'United States value")
        time.sleep(15)
        
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2", "riser!s0!g0!mmarker", map1_bubble, "Step 25: Verify bubble map1 display only 'United States value")
        time.sleep(8)
        
        """
        Step 26: Set the slider values from:1 to :3
        """
        propertyobj.move_slider_dimension_sale_month("1",r1=1,r2=3)
        time.sleep(15)
        
        """
        Step 27: Maximise grid and verify Sale Month column values display only 1 to 3
        """
        time.sleep(10)
#         grid1 = self.driver.find_element_by_xpath("//div[contains(@id,'BoxLayoutMiniWindow')]/div/div[contains(text(),'Grid1')]")
#         action = ActionChains(self.driver)
#         action.click(grid1).perform()
        resultobj.select_panel("Grid1")
        time.sleep(3)
        resultobj.select_panel_caption_btn(0, select_type='maximize')
        time.sleep(8)
        resultobj.verify_grid_data_set('MAINTABLE_wbody1',2,'C2108833_Ds01.xlsx', "Step 27: Verify Grid 2 measure data set")
        time.sleep(15)
        resultobj.select_panel_caption_btn(0, select_type="restore")
        
        """
        Step 28: Click "Run" in the toolbar.
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        """
        Step 29: Verify output
        """
        parent_css="#MAINTABLE_wbody1 svg .tablePanel"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody2 svg g circle[class='riser!s0!g0!mmarker!']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody3 svg g circle[class='riser!s0!g0!mmarker!']"
        resultobj.wait_for_property(parent_css, 1)
        d=['2013', '1', 'Accessories', 'North America', 'North America', '$181,410.33', '$55,771.33', '$125,639.00']
        resultobj.verify_grid_row_val("MAINTABLE_wbody1", d, "Step 29: Verify sale year column in grid has only 2013")
        
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2108833_Actual_step29', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 30: Close the output window
        """
        time.sleep(2)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 32: Click "Save" in the toolbar > Type C2108833 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(6)
        
if __name__ == '__main__':
    unittest.main()