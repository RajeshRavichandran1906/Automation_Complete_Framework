'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253224
TestCase Name = Bar Chart 
'''
import unittest, time
from common.lib import utillity 
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.ui import WebDriverWait
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, metadata
 
class C2253224_TestClass(BaseTestCase):
    
    def test_C2253224(self):
        
        """
        TESTCASE OBJECTS
        """
        driver = self.driver
        metadataobj = metadata.MetaData(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        TESTCASE VARIABLES
        """ 
        browser_type=utillobj.parseinitfile('browser')
        Test_Case_ID = "C2253224_"+browser_type
        elem = "#jschart_HOLD_0 span>a[href*='contentDrill']"
        
        """    1a. Launch the IA Chart API with wf_retail_lite    """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P276/S9970', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)   
        time.sleep(15)
        
        """    1b. Add fields and Click enable Autodrill button from Format Tab    """
        metaobj.datatree_field_click('Quantity,Sold', 2, 1)
        query_tree = '#queryTreeColumn'
        utillobj.synchronize_with_visble_text(query_tree, 'Quantity,Sold', 30)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        utillobj.synchronize_with_visble_text(query_tree, 'Product,Category', 30)
        metadataobj.collapse_data_field_section('Filters and Variables')
        time.sleep(2)
        metadataobj.collapse_data_field_section('Measure Groups')
        time.sleep(2)
        metaobj.datatree_field_click('Store,Business,Region', 1, 1, 'Add To Query', 'Color')
        time.sleep(8)
        ribbonobj.switch_ia_tab("Format")
        if driver.find_element_by_css_selector("#FormatAutoDrillCluster").value_of_css_property("Visibility") == 'hidden':
            autolink_altbtn=driver.find_element_by_css_selector("#FormatAutoDrillCluster_altButton img")
            utillobj.default_left_click(object_locator=autolink_altbtn)
            time.sleep(2)
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(15)
        
        """    1c. Click IA > Save As > Type C2253224 > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    2. Right click on "Bar" and choose Run from the menu    """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S9970", 'mrid', 'mrpass')
        time.sleep(25)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        br=utillobj.get_browser_height()
        utillobj.browser_x=br['browser_width']
        utillobj.browser_y=br['browser_height']
        
        time.sleep(4)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(3)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 02.01: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 28, 'Step 02.02: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 02.03: Verify first segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g1!mbar!", "bar_green", "Step 02.04: Verify second segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g1!mbar!", "pale_yellow_2", "Step 02.05: Verify fourth segment in the bar color")
        xaxis_value="Product Category"
        yaxis_value="Quantity Sold"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 02.06: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 02.07: Verify Y-Axis Title")
        time.sleep(8)
          
        """    3. Hover over the tallest bar in Stereo System (North America) and then hover over "Drill down to" and click on "Product Subcategory"    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s1!g4!mbar!', 'Drill down to->Product Subcategory')
        time.sleep(8)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 1)
        time.sleep(8)
        a =['Product Subcategory:Speaker Kits', 'Quantity Sold:139,579', 'Store Business Region:North America', 'Restore Original', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s0!g3!mbar!',a,"Step 03.01: Verify Speaker Kits tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 5, "Step 03.02: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Subcategory", "Step 03.03: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Quantity Sold", "Step 03.04: verify Y axis title")
        expected_xval_list=['Boom Box', 'Home Theater Systems', 'Receivers', 'Speaker Kits', 'iPod Docking Station']
        expected_yval_list=['0', '40K', '80K', '120K', '160K', '200K', '240K', '280K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 03.05: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue1", "Step 03.06: Verify bar color") 
        time.sleep(3)
        
        """    4. Hover over the bar for Home Theater Systems and then hover over "Drill down to" and click on Store Business Sub Region    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g1!mbar!', 'Drill down to->Store Business Sub Region')
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 2)
        time.sleep(8)
        a =['Product Subcategory:Home Theater Systems', 'Quantity Sold:23,344', 'Store Business Sub Region:Midwest', 'Restore Original', 'Drill up to', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s3!g0!mbar!',a,"Step 04.01: Verify Midwest tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 8, "Step 04.02: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Subcategory", "Step 04.03: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Quantity Sold", "Step 04.04: verify Y axis title")
        expected_xval_list=['Home Theater Systems']
        expected_yval_list=['0', '30K', '60K', '90K', '120K', '150K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 04.05: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 04.06: Verify bar color") 
        time.sleep(3)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#jschart_HOLD_0"),'C2229681_Actual_step4', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        
        """    5. Hover over the tallest bar for "West" and then hover over "Drill down to" and click on "Store Country"    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s7!g0!mbar!', 'Drill down to->Store Country')
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 3)
        time.sleep(8)
        a =['Product Subcategory:Home Theater Systems', 'Quantity Sold:135,629', 'Store Country:United States', 'Restore Original', 'Drill up to', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s0!g0!mbar!',a,"Step 05.01: Verify United States tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 1, "Step 05.02: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Subcategory", "Step 05.03: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Quantity Sold", "Step 05.04: verify Y axis title")
        expected_xval_list=['Home Theater Systems']
        expected_yval_list=['0', '40K', '80K', '120K', '160K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 05.05:')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 05.06: Verify bar color") 
        time.sleep(3)
        
        """    6. Hover over the single bar and then hover over "Drill down to" and click on "Store State Province"    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!', 'Drill down to->Store State Province')
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 4)
        time.sleep(8)
        a =['Product Subcategory:Home Theater Systems', 'Quantity Sold:122,610', 'Store State Province:Idaho', 'Restore Original', 'Drill up to', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s4!g0!mbar!',a,"Step 06.01: Verify Idaho tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 9, "Step 06.02: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Subcategory", "Step 06.03: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Quantity Sold", "Step 06.04: verify Y axis title")
        expected_xval_list=['Home Theater Systems']
        expected_yval_list=['0', '30K', '60K', '90K', '120K', '150K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 06.05: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s4!g0!mbar!", "brick_red", "Step 06.06: Verify bar color") 
        time.sleep(3)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#jschart_HOLD_0"),'C2229681_Actual_step6', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        
        """    7. Hover over the second bar from the left, for California, and then hover over "Drill down to" and click on "Store City"    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s1!g0!mbar!', 'Drill down to->Store City')
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 5)
        time.sleep(8)
        a =['Product Subcategory:Home Theater Systems', 'Quantity Sold:1,646', 'Store City:San Francisco', 'Restore Original', 'Drill up to', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s2!g0!mbar!',a,"Step 07.01: Verify San Francisco tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 3, "Step 07.02: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Subcategory", "Step 07.03: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Quantity Sold", "Step 07.04: verify Y axis title")
        expected_xval_list=['Home Theater Systems']
        expected_yval_list=['0', '400', '800', '1,200', '1,600', '2,000', '2,400', '2,800']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 07.05: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 07.06: Verify bar color") 
        time.sleep(3)
        
        """    8. Hover over the middle bar, for San Diego, and then hover over "Drill down to" and click on "Model"    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s1!g0!mbar!', 'Drill down to->Model')
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 6)
        time.sleep(8)
        a =['Model:Panasonic', 'Quantity Sold:281', 'Store City:San Diego', 'Restore Original', 'Drill up to', 'Drill down to Store Postal Code']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s0!g2!mbar!',a,"Step 08.01: Verify San Diego tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 8, "Step 08.02: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Model", "Step 08.03: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Quantity Sold", "Step 08.04: verify Y axis title")
        expected_xval_list=['LG MDD72', 'LG XD63', 'Panasonic', 'Panasonic SC-PT160', 'Pioneer HTZ-170', 'Samsung HT-Z120', 'Sharp HT-CN550', 'Sony DAV-DZ30']
        expected_yval_list=['0', '50', '100', '150', '200', '250', '300', '350', '400']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 08.05: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g6!mbar!", "bar_blue1", "Step 08.06: Verify bar color") 
        time.sleep(3)
        
        """    9. On the second row of bread crumbs, ending with "Home Theater Systems", click on the "Home" link to clear those selections.    """
        bread_crumbs=driver.find_elements_by_css_selector(elem)
        bc_list=[el.text.strip() for el in bread_crumbs]
        bread_crumbs[bc_list.index('Home',1)].click()
        time.sleep(8)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 4)
        time.sleep(8)
        a =['Product Category:Stereo Systems', 'Quantity Sold:1,646', 'Store City:San Francisco', 'Restore Original', 'Drill up to Store State Province', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s2!g0!mbar!',a,"Step 09.01: Verify San Francisco tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 3, "Step 09.02: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Category", "Step 09.03: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Quantity Sold", "Step 09.04: verify Y axis title")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '400', '800', '1,200', '1,600', '2,000', '2,400', '2,800']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 09.05: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 09.06: Verify bar color") 
        
        """    10. Hover over any bar and click on "Restore Original"    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s1!g0!mbar!', 'Restore Original')
        time.sleep(15)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 10.01: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 28, 'Step 10.02: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 10.03: Verify first segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g1!mbar!", "bar_green", "Step 10.04: Verify second segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g1!mbar!", "pale_yellow_2", "Step 10.05: Verify fourth segment in the bar color")
        xaxis_value="Product Category"
        yaxis_value="Quantity Sold"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 10.06: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 10.07: Verify Y-Axis Title")
        time.sleep(8)
         
        """    10. Close the output window.    """
        
if __name__ == '__main__':
    unittest.main()