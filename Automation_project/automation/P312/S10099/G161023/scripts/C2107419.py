'''
Created on May'03, 2016
@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2107419
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.pages import metadata, visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run, core_metadata
from common.locators import visualization_metadata_locators, visualization_properties_locators, visualization_resultarea_locators
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators

class C2107419_TestClass(BaseTestCase):
    
    def test_C2107419(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2107419'
        """
        Step 01: Launch the IA API with wf_retail_lite
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        core_metaobj = core_metadata.CoreMetaData(self.driver)
        propobj=visualization_properties.Visualization_Properties(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_4', 'mrid', 'mrpass')
            
        #utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','S8357', 'mrid01', 'mrpass01')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Change to Grid
        """
        ribbonobj.change_chart_type('grid')
        
        """
        Step 03:Verify bar chart is changed to table(rows and columns)
        """
        time.sleep(5)
        resultobj.verify_panel_caption_label(0, 'Grid1', 'Step 03: Verify Grid1 is displayed')  
        
        """
        Step 04: Double Click Revenue, Sale Year, Product Category
        """
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Sale,Year", 2, 1)
        time.sleep(5)
        metadataobj.collapse_data_field_section('Sales')
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(5)

        """
        Step 05: Verify column titles in the canvas.
        """
        
        WebDriverWait(self.driver, 80).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 2)
        time.sleep(5)
        parent_css1=".rowTitle text"
        resultobj.wait_for_property(parent_css1, 2)
        time.sleep(10)
        parent_css1=".colHeader text"
        resultobj.wait_for_property(parent_css1, 1)
        heading = ['Sale Year', 'Product Category', 'Revenue']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',heading, 'Step 05.1: Verify column titles')

        """
        Step 06 : Verify first and last 3 row values.
        """
        time.sleep(8)
        row_val=['2011', 'Accessories', '$5,039,297.57']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val,'Step 06.1: verify grid 1st row value')

        """
        Step 07: Add any 7 filters (Prodct category, Sale,Year, Store,Business Region, Customer,Business region,Store,Country, Customer,Country and Revenue) in filter Pane with Show prompt selected.
        """
        metaobj.datatree_field_click("Product,Category", 1, 1,"Filter")
        metaobj.create_visualization_filters('alpha')
        time.sleep(10) # time to load the page after adding filter
        metaobj.datatree_field_click("Sale,Year", 1, 1,"Filter")
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        metaobj.create_visualization_filters('numeric')
        time.sleep(10)
        metaobj.datatree_field_click("Store,Business,Region", 1, 1,"Filter")
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        metaobj.create_visualization_filters('alpha')
        time.sleep(10)
        scrollable_element_css="[id^='QbMetaDataTree']>div[class='bi-tree-view-body']"
        scroll_script_syntax='document.querySelector("{0}").scrollTop=0'.format(scrollable_element_css)
        self.driver.execute_script(scroll_script_syntax)
        time.sleep(3)
        core_metaobj.collapse_data_field_section('Filters and Variables')
        metaobj.datatree_field_click("Customer,Business,Region", 1, 1,"Filter")
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        metaobj.create_visualization_filters('alpha')
        time.sleep(10)
        metaobj.datatree_field_click("Store,Country", 1, 1,"Filter")
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        metaobj.create_visualization_filters('alpha')
        time.sleep(10)
        metaobj.datatree_field_click("Customer,Country", 1, 1,"Filter")
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        metaobj.create_visualization_filters('alpha')
        time.sleep(10)
        metaobj.datatree_field_click("Revenue", 1, 1,"Filter")
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(5)
        metaobj.create_visualization_filters('numeric',['Operator','Range'])

        """
        Step 08: verify 7 filter queries are added to filter pane.
        """
        time.sleep(15)
        metaobj.verify_filter_pane_field("Product,Category",1,'Step 08.1: Product Category added to filter pane')
        metaobj.verify_filter_pane_field("Sale,Year",2,'Step 08.2: Sale Year added to filter pane')
        metaobj.verify_filter_pane_field("Store,Business,Region",3,'Step 08.3: Store Business Region added to filter pane')
        metaobj.verify_filter_pane_field("Customer,Business,Region",4,'Step 08.4: Customer Business Region added to filter pane')
        metaobj.verify_filter_pane_field("Store,Country",5,'Step 08.5: Store Country added to filter pane')
        metaobj.verify_filter_pane_field("Customer,Country",6,'Step 08.6: Customer Country added to filter pane')
        metaobj.verify_filter_pane_field("Revenue",7,'Step 08.7: Revenue added to filter pane')
        time.sleep(5)

        """
        Step 09: Run Visualization.
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)

        """
        Step 10: Move the scroll bar and verify 7 filter prompts titles and values (first two and last two values.
        """
        raiser="div[id*='ibi$container$inner$HBOX_1']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(10)
        parent_css1=".rowTitle text"
        resultobj.wait_for_property(parent_css1, 2)
        time.sleep(10)
        parent_css1=".colHeader text"
        resultobj.wait_for_property(parent_css1, 1)
        propobj.select_or_verify_show_prompt_item(1, '[All]', True,verify_type=True,msg="Step 10.1: Verify 1st filter prompt first value [All] is checked")
        time.sleep(8)
        propobj.verify_slider_range_filter_prompts('#sliderPROMPT_2','min',2011,'int',msg="Step10: Verify filter prompt range values- min")
        propobj.verify_slider_range_filter_prompts('#sliderPROMPT_2','max',2017,'int',msg="Step10: Verify filter prompt range values- max")
        time.sleep(2)
        propobj.select_or_verify_show_prompt_item(3, '[All]', True,verify_type=True,msg="Step 10.3: Verify 3rd filter prompt first value")
        time.sleep(2)
        propobj.select_or_verify_show_prompt_item(4, '[All]', True,verify_type=True,msg="Step 10.4: Verify 4th filter prompt first value")
        time.sleep(2)
        propobj.select_or_verify_show_prompt_item(5, '[All]', True,verify_type=True,msg="Step 10.5: Verify 5th filter prompt first value")
        time.sleep(2)
        propobj.select_or_verify_show_prompt_item(6, '[All]', True,verify_type=True,msg="Step 10.6: Verify 6th filter prompt first value")
        time.sleep(2)
        propobj.verify_slider_range_filter_prompts('#sliderPROMPT_7','min',17.99,'float',msg="Step10: Verify filter prompt range values- min")
        propobj.verify_slider_range_filter_prompts('#sliderPROMPT_7','max',15999.4,'float',msg="Step10: Verify filter prompt range values- max")
        

        """
        Close the output window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)

        """
        Step 11: Click "Save" in the toolbar > Type C2107419 > Click "Save" in the Save As dialog
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        #ribbonobj.select_tool_menu_item('menu_save_as')
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()
