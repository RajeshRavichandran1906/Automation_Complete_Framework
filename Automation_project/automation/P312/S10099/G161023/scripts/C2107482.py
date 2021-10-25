'''
Created on May'12, 2016
@author: Kiruthika

Test Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2107482&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case Description : IA-4596:Vis: Filter on other chart doesn't retain the Filter values "Less Than & Greater than or Equal to" in another Grid
'''
import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea
from common.locators import visualization_resultarea_locators
from common.lib import utillity


class C2107482_TestClass(BaseTestCase):

    def test_C2107482(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2107482'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_4', 'mrid', 'mrpass')
            
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
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
        Step 02: Double click Product Category and Revenue.
        """
        time.sleep(5)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(2)
        """
        Step 03: Verify x and y axis labels
        """
        parent_css1="#MAINTABLE_wbody1 svg g.risers >g>rect"
        resultobj.wait_for_property(parent_css1,7)

        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 03a: Verify the total number of risers displayed on Run Chart')
        
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 03b: X annd Y axis Scales Values has changed or NOT')
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 03:c(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 03:c(ii) Verify Y-Axis Title")
        
        """
        Step 04: Add Product SubCategory to Color.
        """
        metaobj.datatree_field_click('Product,Subcategory',1,1,'Add To Query','Color')
        time.sleep(8)
       
        """
        Step 05: Verify color label, first two and last two values of Bar.
        """
        riser1=(By.CSS_SELECTOR,"#MAINTABLE_wbody1 [class*='riser!s8!g0!mbar']")
        utillobj._validate_page(riser1)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s8!g0!mbar", "dark_green1", "Step 05.c(i) Verify first bar color")
        
        riser2=(By.CSS_SELECTOR,"#MAINTABLE_wbody1 [class*='riser!s0!g3!mbar']")
        utillobj._validate_page(riser2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar", "bar_blue", "Step 05.c(ii) Verify second bar color")
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 05:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 05:d(ii) Verify Y-Axis Title")
        
        parent_css2="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css2,22)
        a=['Product Subcategory', 'Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        resultobj.verify_riser_legends("MAINTABLE_1", a, "Step 05.e: Verify Color legends")
        
        parent_css3="#MAINTABLE_wbody1 svg g.risers >g>rect"
        resultobj.wait_for_property(parent_css3,25)
#         resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 05: Verify the total number of risers displayed on Run Chart')
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 25, 'Step 05: Verify the total number of risers displayed on Run Chart', custom_css="svg g.risers >g>rect")
        
        """
        Step 06: Insert Grid.
        """
        ribbonobj.select_ribbon_item('Home', 'Insert', opt='Grid')
        time.sleep(5)
        
        """
        Step 07: Add Sale Quarter, Product Category and Revenue.
        """
        metaobj.datatree_field_click('Sale,Quarter',2,1)
        time.sleep(3)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Revenue', 2, 1)
        
        """
        Step 08: Verify field labels in grid.
        """
        parent_css4=(By.CSS_SELECTOR,"#TableChart_2 .tablePanel g[class^='colHeader'] text")
        utillobj._validate_page(parent_css4)
        list2 = ['Sale Quarter', 'Product Category', 'Revenue']
        time.sleep(4)
        resultobj.verify_grid_column_heading('TableChart_2',list2, 'Step 08: Verify field labels in grid')
        
        """
        Step 09: Verify 1st two and last two row values in grid.
        """
        time.sleep(20)
        row1 = ['1', 'Accessories', '$31,676,924.79']
        resultobj.verify_grid_row_val('TableChart_2', row1,"Step 09: Verify 1st grid row value")
        
        """
        Step 10: Add Sale Quarter to Filter and change the Range to Less Than or equal to 2. Click ok.
        """
        metaobj.datatree_field_click('Sale,Quarter',1,1,'Filter')
        time.sleep(8)
        
        select_combobox_item_av('avOperatorComboBox', 'Equal to')
        metaobj.create_visualization_filters('alpha')
        time.sleep(6)
       
        """
        Step 11: Verify query added to filter pane.
        """
        filter_icon=(By.CSS_SELECTOR,"#qbFilterBox table>tbody>tr>td>img")
        utillobj._validate_page(filter_icon)
        metaobj.verify_filter_pane_field("Sale,Quarter",1, "Step 11: Verify query added to filter pane")
        
        """
        Step 12: Verify Sale quarter values in grid
        """
        riser3=(By.CSS_SELECTOR,"#MAINTABLE_1 [class*='riser!s0!g3!mbar']")
        utillobj._validate_page(riser3)
        
        time.sleep(25)
        row1 = ['1', 'Accessories', '$31,676,924.79']
        resultobj.verify_grid_row_val('TableChart_2', row1,"Step 12: Verify 1st grid row value")
        time.sleep(8)
        
        """
        Step 13: Hover on "Media Player" in bar chart and select filter chart.
        """
        time.sleep(10)
        resultobj.select_default_tooltip_menu("MAINTABLE_1", "riser!s0!g3!mbar", "Filter Chart")
        
        """
        Step 14: Verify Media player value filtered in bar chart
        """
        time.sleep(10)
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(10)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 14a: Verify the total number of risers displayed on Preview Chart')
        
        x_val_list=['Media Player']
        y_val_list=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 14b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 14.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 14:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 14:d(ii) Verify Y-Axis Title")
        
        """
        Step 15: Verify grid output in preview.
        """
        raiser="[class*='row0']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(8)
        row2 = ['1', 'Media Player', '$57,255,724.90']
        resultobj.verify_grid_row_val('TableChart_2', row2,"Step 15: Verify 1st grid row value") 
        time.sleep(15)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2107482_Actual_step15', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 16: Click "Save" in the toolbar > Type C2107482 > Click "Save" in the Save As dialog
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(6)

if __name__ == '__main__':
    unittest.main()

