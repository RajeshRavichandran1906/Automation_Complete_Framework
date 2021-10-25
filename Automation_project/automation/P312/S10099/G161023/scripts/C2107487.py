'''
Created on June8, 2016
@author: Kiruthika

Test Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2107487&group_by=cases:section_id&group_id=146864&group_order=asc
TestCase Name : IA-4550:BUE: Cannot filter if value contains special character
'''
import unittest
import time
from selenium.webdriver import ActionChains
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.pages import core_metadata


class C2107487_TestClass(BaseTestCase):

    def test_C2107487(self):
        driver = self.driver #Driver reference object created
        
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2107487'
        core_meta_obj = core_metadata.CoreMetaData(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/customer_data','P312/S10099_4', 'mrid', 'mrpass')
            
        #utillobj.infoassist_api_login('idis','baseapp/customer_data','S8357', 'mrid01', 'mrpass01')
        element_css="#resultArea svg>g.chartPanel rect[class*='riser!']"
        utillobj.synchronize_with_number_of_element(element_css, 12, 60)
        
        """
        Step 02: Add "Number of Days Since Contact" to Vertical axis
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Measure Groups->Sheet1->Number of Days Since Contact', 1, 'Vertical Axis', 0)
        
        """
        Step 04: Add "Sales Rep" to horizontal axis
        """
        time.sleep(5)
        core_meta_obj.collapse_data_field_section('Measure Groups')
        metaobj.drag_drop_data_tree_items_to_query_tree('Dimensions->Sheet1->Sales->Sales Rep', 1, 'Horizontal Axis', 0)
        
        """
        Step 05: Verify x and Y axis labels
        """
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(parent_css1, 'Number of Days Since Contact', 90, 1)
        
        xaxis_value="Sales Rep"
        yaxis_value="Number of Days Since Contact"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 05:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 05:d(ii) Verify Y-Axis Title")
        
        """
        Step 06: Verify first and last 2 bar values
        """
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 33, 'Step 06: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Andy Florez', 'Bill Arkell', 'Bill Kotraba', 'Brant Hubbard', 'Chris Braun', 'Craig Clark', 'Curtis Drever', 'Dan Haug']
        expected_yval_list=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500', '4,000', '4,500']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 06b: X and Y axis Labels -')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 06.c Verify first bar color")
        time.sleep(8)
        tooltip_list=['Sales Rep:Bill Arkell', 'Number of Days Since Contact:187', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sales Branch']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g1!mbar', tooltip_list, "Step 06: Verify first bar values")
        
        """
        Step 07: Hover over "Mark O'Mara" > Filter chart
        """
        
        time.sleep(5)
        
        move = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        browser=utillobj.parseinitfile('browser')
        
        if browser=='Firefox' :
            utillobj.click_type_using_pyautogui(move,move=True)
        else :
            action = ActionChains(driver)
            action.move_to_element_with_offset(move,1,1).perform()
        
        time.sleep(5)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g21!mbar","Filter Chart")
        """
        Step 08: verify query added to the filter pane
        """
        metaobj.verify_filter_pane_field('Sales Rep',1,"Step 08: verify query added to filter pane.")
        """
        Step 09: Verify "Mark O'Mara" value alone is displayed in preview.
        """
        
        time.sleep(3)
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css1, 1)
        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1,1,"Step 09: Verify 1 bar displayed in preview - ")
        expected_xval_list=["Mark O'Mara"]
        expected_yval_list=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500', '4,000', '4,500']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 09b: X annd Y axis Labels -')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 09.c Verify first bar color")
        xaxis_value="Sales Rep"
        yaxis_value="Number of Days Since Contact"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 09:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 09:d(ii) Verify Y-Axis Title")
        time.sleep(8)
        tooltip_list=["Sales Rep:Mark O'Mara", 'Number of Days Since Contact:4059', 'Drill up to Sales Branch']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar', tooltip_list, "Step 09: Verify 'Mark O'Mara' in first bar ")
        time.sleep(15)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2107487_Actual_step09', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 10: Click "Save" in the toolbar > Type C2107487 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()

