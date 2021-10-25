'''
Created on 10June, 2016
@author: Kiruthika
Completed on 10Jun 2016

Test Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2108151&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case Description : IA-4539:BUE: Filter from hover tooltip doesn't work in special scenario
'''
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.pages import core_metadata

class C2108151_TestClass(BaseTestCase):

    def test_C2108151(self):
        driver = self.driver #Driver reference object created
        
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2108151'
        core_meta_obj = core_metadata.CoreMetaData(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        browser=utillobj.parseinitfile('browser')
        
        utillobj.infoassist_api_login('idis','baseapp/customer_data','P312/S10099_4', 'mrid', 'mrpass')
            
        element_css="#resultArea svg>g.chartPanel rect[class*='riser!']"
        utillobj.synchronize_with_number_of_element(element_css, 12, 60)
        """
        Step 02: Change to scatter chart.
        """
        ribbonobj.change_chart_type('scatter')
        """
        Step 03: Add Net Sales to vertical axis and Number of Days Since Contact to Horizontal axis.
        """
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree('Measure Groups->Sheet1->Number of Days Since Contact', 1, 'Vertical Axis', 0)
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree('Measure Groups->Sheet1->Net Sales', 1, 'Horizontal Axis', 0)
        
       
        """
        Step 04: Verify x and y axis labels.
        """
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(parent_css1, 'Net Sales', 90, 1)
       
        resultobj.verify_xaxis_title('MAINTABLE_wbody1_f', "Net Sales",'Step 04: Verify X title Number of Days Since Contact')
        
        resultobj.verify_yaxis_title('MAINTABLE_wbody1_f', "Number of Days Since Contact",'Step 04: Verify Y title Number of Days Since Contact')
        
        expected_xval_list=['0', '30M', '60M', '90M', '120M', '150M']
        expected_yval_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 04: X annd Y axis Label values verify')
        
        
        """
        Step 05: Add Transactions to Size.
        """
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree('Measure Groups->Sheet1->Transactions', 1, 'Size', 0)
        time.sleep(5)
         
        """
        Step 06: Add Company Name to Detail.
        """
        core_meta_obj.collapse_data_field_section('Measure Groups')
        metaobj.drag_drop_data_tree_items_to_query_tree('Dimensions->Sheet1->Company->Company Name', 1, 'Detail', 0)
        time.sleep(5)
        """
        Step 07: Add Sales Region to Color and Columns.
        """
        raiser='[class*="riser!s0!g442!mmarker"]'
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        metaobj.drag_drop_data_tree_items_to_query_tree('Dimensions->Sheet1->Sales->Sales Region', 1, 'Columns', 0)
#         metaobj.datatree_field_click('Sales Region',1,1,'Add To Query','Columns')
        time.sleep(5)
        raiser='[class*="riser!s0!g87!mmarker!r0!c0"]'
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        metaobj.drag_drop_data_tree_items_to_query_tree('Dimensions->Sheet1->Sales->Sales Region', 1, 'Color', 0)
#         metaobj.datatree_field_click('Sales Region',1,1,'Add To Query','Color')
        time.sleep(5)
        
        element_css="#TableChart_1 [class*='riser!s0!g87!mmarker!r0!c0']"
        utillobj.synchronize_with_number_of_element(element_css, 1, 60, 1)
        """ 
        Step 08: Verify query pane
        """
        metaobj.verify_query_pane_field("Columns","Sales Region", 1, "Step 08.1: Verify query pane Columns")
        metaobj.verify_query_pane_field("Vertical Axis","Number of Days Since Contact", 1, "Step 08.2: Verify query pane Vertical Axis")
        metaobj.verify_query_pane_field("Horizontal Axis","Net Sales", 1, "Step 08.3: Verify query pane Horizontal Axis")
        metaobj.verify_query_pane_field("Size","Transactions", 1, "Step 08.4: Verify query pane Size")
        metaobj.verify_query_pane_field("Detail","Company Name", 1, "Step 08.5: Verify query pane Detail")
        metaobj.verify_query_pane_field("Color BY","Sales Region", 1, "Step 08.6: Verify query pane COLOR BY")  
         
        """
        Step 09: Hover on a scatter plot and verify tooltip values
        """
        time.sleep(5)
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css1, 1)
        parent_css1="#MAINTABLE_wbody1 svg g text[class='xaxisNumeric-title']"
        resultobj.wait_for_property(parent_css1, 5)
        raiser='[class*="riser!s0!g87!mmarker!r0!c0"]'
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(5)
    
        move = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        
        if browser=='Firefox' :
            utillobj.click_type_using_pyautogui(move,move=True)
        else : 
            action = ActionChains(driver)
            action.move_to_element_with_offset(move,1,1).perform()
        
        time.sleep(5)
        a=['Sales Region:Canada', 'Net Sales:89,217.0', 'Number of Days Since Contact:38', 'Transactions:6', 'Sales Region:Canada', 'Company Name:Superior Plus Corp.', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g87!mmarker!r0!c0',a,"Step 09: Hover on a scatter plot and verify tooltip values",x_offset=0,y_offset=-9)
         
        """
        Step 10: Insert Stacked bar chart.
        """
        time.sleep(5)
        ribbonobj.select_ribbon_item('Home','Insert',opt='Chart')
        time.sleep(3)
        ribbonobj.change_chart_type('stacked_bar')
        
        """
        Step 11: Add Customer count to vertical axis and Sales Branch to horizontal axis
        """
        time.sleep(3)
        core_meta_obj.collapse_data_field_section('Dimensions')
        metaobj.drag_drop_data_tree_items_to_query_tree('Measure Groups->Sheet1->Customer Count', 1, 'Vertical Axis', 0)
#         metaobj.datatree_field_click('Customer Count',1,1,'Add To Query','Vertical Axis')
        time.sleep(5)
        core_meta_obj.collapse_data_field_section('Measure Groups')
        metaobj.drag_drop_data_tree_items_to_query_tree('Dimensions->Sheet1->Sales->Sales Branch', 1, 'Horizontal Axis', 0)
#         metaobj.datatree_field_click('Sales Branch',1,1,'Add To Query','Horizontal Axis')
        time.sleep(5)
        
        """
        Step 12: Verify x and y axis labels of stacked bar chart
        """
        move1 = driver.find_element_by_xpath("//div[contains(@id,'BoxLayoutMiniWindow')]/div/div[contains(text(),'Bar Stacked1')]")
        if browser=='Firefox' :
            utillobj.click_type_using_pyautogui(move1,move=True)
        else :
            action = ActionChains(driver)
            action.move_to_element(move).perform()
        
        parent_css1="#MAINTABLE_wbody2 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css1, 1)
        parent_css1="#MAINTABLE_wbody2 svg g text[class='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css1, 1)
         
        resultobj.verify_xaxis_title('MAINTABLE_wbody2_f', "Sales Branch",'Step 12: Verify X title Sales Branch')
        resultobj.verify_yaxis_title('MAINTABLE_wbody2_f', "Customer Count",'Step 12: Verify Y title Customer Count')
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 14, 'Step 12.b: Verify the total number of risers displayed on Run Chart') 
        expected_xval_list=['Atlanta', 'Boston', 'Canada Emerging Business', 'Canadian Central', 'Chicago', 'Cincinnati', 'Dallas', 'Detroit', 'Los Angeles']
        expected_yval_list=['0', '50', '100', '150', '200', '250', '300', '350', '400']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', expected_xval_list, expected_yval_list, 'Step 012.c: X annd Y axis Labels -')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g0!mbar", "bar_blue", "Step 12.d.c Verify first bar color")
        """
        Step 13: Add Sales Region to Color
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Dimensions->Sheet1->Sales->Sales Region', 1, 'Color', 0)
#         metaobj.datatree_field_click('Sales Region',1,1,'Add To Query','Color')
        time.sleep(5)
        """
        Step 14: Verify query pane of bar stacked chart
        """
        
        metaobj.verify_query_pane_field("Vertical Axis","Customer Count", 1, "Step 14: Verify query pane of bar stacked chart")

        """
        Step 15: Click Swap.
        """
        time.sleep(5)
        ribbonobj.select_ribbon_item('Home','Swap')
        
        """
        Step 16: Verify x and y axis labels are interchanged.
        """
        time.sleep(15)
        metaobj.verify_query_pane_field("Vertical Axis", "Sales Branch", 1,"Step 16: Verify x and y axis labels are interchanged")
        time.sleep(3)
        metaobj.verify_query_pane_field("Horizontal Axis","Customer Count", 1,"Step 16: Verify x and y axis labels are interchanged")

        """
        Step 17: Insert Grid.
        """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Grid')
        time.sleep(3)
        """
        Step 18: Add Contact First Name, Contact Last Name and Contact Phone number to rows.
        """
        metaobj.datatree_field_click('Dimensions->Sheet1->Contact->Contact First Name',2,1)
        time.sleep(3)
        metaobj.datatree_field_click('Dimensions->Sheet1->Contact->Contact Last Name',2,1)
        time.sleep(3)
        metaobj.datatree_field_click('Dimensions->Sheet1->Contact->Contact Phone Number',2,1)
        WebDriverWait(self.driver, 100).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 3)
        time.sleep(10)
#         ele=driver.find_element_by_css_selector("#iaCanvasPanel")
#         utillobj.take_screenshot(ele,'C2108151_Actual_step17', image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """
        Step 19: Maximize grid and verify titles.
        """
        resultobj.select_panel_caption_btn(0, 'maximize')
        time.sleep(8)        
        WebDriverWait(self.driver, 60).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 3)
        list01 =['Contact First Name', 'Contact Last Name', 'Contact Phone Number']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody3',list01, 'Step 19.1: Verify field titles')
        time.sleep(3)
         
        """
        Step 20: Minimize the Grid.
        """
        elem1=(By.XPATH, "//div[contains(@class,'mini-window-check')]/div/div[contains(@class,'restore-button')]")
        resultobj._validate_page(elem1)
        resultobj.select_panel_caption_btn(0, 'restore')
        
        """
        Step 21: Drag and drop Bar chart in between center and bottom position of Scatter.
        """
        time.sleep(15)
        resultobj.drag_and_drop_visualization("Bar Stacked1", "Scatter1", "bottom_most")
         
        """
        Step 22: Drag and drop Grid in between center and left of bar chart.
        """
        time.sleep(30)
        resultobj.drag_and_drop_visualization("Grid1", "Bar Stacked1", "left")
         
        """
        Step 23: Drag and drop Number of Days Since Contact to filter pane.
        """
        time.sleep(30)       
        #metaobj.datatree_field_click('Number of Days Since Contact',1,1,'Filter')
        core_meta_obj.collapse_data_field_section('Dimensions')
        metaobj.drag_drop_data_tree_items_to_filter('Measure Groups->Sheet1->Number of Days Since Contact',0)
        """
        Step 24: Change the range value From: 21 To: 74 and uncheck show prompt
        """
        metaobj.create_visualization_filters('numeric', ['From','21'],['ShowPrompt'])
        time.sleep(15)
        """
        Step 25: Verify query added to filter pane
        """
        metaobj.verify_filter_pane_field('Number of Days Since Contact',1, "Step 25: Verify query added to filter pane")
        time.sleep(10)
#         ele=driver.find_element_by_css_selector("#iaCanvasPanel")
#         utillobj.take_screenshot(ele,'C2108151_Actual_step25', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        """
        Step 26: Click Run in the toolbar
        """
        elem1=(By.ID, 'applicationButton')
        resultobj._validate_page(elem1)
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(8)
       
        """
        Step 27: Scroll down and hover over New York (green) in bar chart.
        Step 28: Verify tooltip value of NewYork
        """
        elem2=(By.CSS_SELECTOR, "div[id*='ibi$container$inner$VBOX']")
        resultobj._validate_page(elem2)
        time.sleep(10)
        a=['Sales Branch:New York', 'Customer Count:132', 'Sales Region:Eastern', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sales Region', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody2','riser!s2!g10!mbar',a,"Step 28: Verify tooltip value of NewYork")
        time.sleep(10)
        resultobj.verify_xaxis_title('MAINTABLE_wbody2', "Sales Branch",'Step 28: Verify X title Sales Branch')
        resultobj.verify_yaxis_title('MAINTABLE_wbody2', "Customer Count",'Step 28: Verify Y title Customer Count')
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 14, 'Step 28.b: Verify the total number of risers displayed on Run Chart') 
        expected_xval_list=['Atlanta', 'Boston', 'Canada Emerging Business', 'Canadian Central', 'Chicago', 'Cincinnati', 'Dallas', 'Detroit', 'Los Angeles']
        expected_yval_list=['0', '30', '60', '90', '120', '150']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', expected_xval_list, expected_yval_list, 'Step 28.c: X annd Y axis Labels -')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s2!g10!mbar", "dark_green", "Step 28.d.c Verify first bar color")
        
        """
        Step 29: Select Drilldown on Sales Rep.
        """
        elem1=(By.CSS_SELECTOR, "[id*='MAINTABLE_wbody2'] [class*='riser!s2!g10!mbar']")
        resultobj._validate_page(elem1)       
        time.sleep(10)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody2","riser!s2!g10!mbar", 'Drill down to->Sales Rep')
        
        
        """
        Step 30: Verify each riser value of bar stacked chart
        """
#         elem1=(By.CSS_SELECTOR, "[id*='MAINTABLE_wbody2']")
#         resultobj._validate_page(elem1) 
        time.sleep(8)
        resultobj.verify_xaxis_title('MAINTABLE_wbody2', "Sales Rep",'Step 30: Verify X title Sales Branch')
        resultobj.verify_yaxis_title('MAINTABLE_wbody2', "Customer Count",'Step 30: Verify Y title Customer Count')
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 3, 'Step 30.b: Verify the total number of risers displayed on Run Chart') 
        expected_xval_list=['Chris Braun', 'Jerry Duci', "Mark O'Mara"]
        expected_yval_list=['0', '20', '40', '60', '80', '100']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', expected_xval_list, expected_yval_list, 'Step 30.c: X annd Y axis Labels -')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g0!mbar", "bar_blue", "Step 30.d.c Verify first bar color")
        time.sleep(8)
        a=['Sales Rep:Chris Braun', 'Customer Count:20', 'Sales Region:Eastern', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Sales Branch', 'Drill down to Sales Branch']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody2','riser!s0!g0!mbar',a,"Step 30: Verify tooltip value of Chris Braun")
        time.sleep(15)
#         ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$VBOX']")
#         utillobj.take_screenshot(ele,'C2108151_Actual_step30', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 31: In resultant three bars, hover over Mark O'Mara (do not click) > Filter Chart in tooltip
        """
#         elem1=(By.CSS_SELECTOR, "[id*='MAINTABLE_wbody2'] [class*='riser!s0!g2!mbar']")
#         resultobj._validate_page(elem1) 
        time.sleep(15)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody2","riser!s0!g2!mbar", 'Filter Chart')
        
        """
        Step 32: Verify Mark O'Mara value filtered.
        """
        elem1=(By.CSS_SELECTOR, "[id*='MAINTABLE_wbody2'] [class*='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1) 
        time.sleep(20)
        resultobj.verify_xaxis_title('MAINTABLE_wbody2', "Sales Rep",'Step 32: Verify X title Sales Branch')
        resultobj.verify_yaxis_title('MAINTABLE_wbody2', "Customer Count",'Step 32: Verify Y title Customer Count')
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 1, 'Step 32.b: Verify the total number of risers displayed on Run Chart') 
        expected_xval_list=["Mark O'Mara"]
        expected_yval_list=['0', '20', '40', '60', '80', '100']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', expected_xval_list, expected_yval_list, 'Step 32.c: X annd Y axis Labels -')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g0!mbar", "bar_blue", "Step 32.d.c Verify first bar color")
        time.sleep(8)
        a=["Sales Rep:Mark O'Mara","Customer Count:79","Sales Region:Eastern", 'Remove Filter', 'Drill up to Sales Branch', 'Drill down to Sales Branch']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody2','riser!s0!g0!mbar',a,"Step 32: Verify tooltip value of Mark O'Mara")
        time.sleep(15)
        elem2=(By.CSS_SELECTOR, "div[id*='ibi$container$inner$VBOX']")
        resultobj._validate_page(elem2) 
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$VBOX']")
        utillobj.take_screenshot(ele,'C2108151_Actual_step32', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 33: Close the output window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 34: Click "Save" in the toolbar > Type C2108151 > Click "Save" in the Save As dialog
        """
        time.sleep(2)  
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()

