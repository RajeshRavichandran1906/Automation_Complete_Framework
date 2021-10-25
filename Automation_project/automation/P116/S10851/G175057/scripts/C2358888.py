'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2358888
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, active_miscelaneous
from common.lib import utillity, core_utility
from common.lib.global_variables import Global_variables

class C2358888_TestClass(BaseTestCase):

    def test_C2358888(self):
        
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2358888'
        
        """ CLASS OBJECTS """
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
                
        """    1. Launch IA to develop a Document.
        Select 'GGSales' as master file, and change output format as Active report/APDF
        Select 'Chart' from home tab and choose Category, Product, and Unit Sales to get a chart    """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10851_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=35, string_value='Document')
        ribbonobj.select_ribbon_item("Insert", "Chart")
        utillobj.synchronize_with_number_of_element("#pfjTableChart_1", 1, resultobj.chart_medium_timesleep)
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1", "Coffee", resultobj.chart_medium_timesleep)    
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1", "Product", resultobj.chart_medium_timesleep)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1", "Unit Sales", resultobj.chart_medium_timesleep)
        utillobj.wait_for_page_loads(10)
        
        """    2. Drag and drop 'Category' into Coordinated area    """
        metaobj.drag_drop_data_tree_items_to_query_tree('Category',1,'Coordinated',0,target_cord='middle')
        time.sleep(8)
        resultobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 02.01: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 02.02: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 02.03: Verify bar color")
        xaxis_value="Category : Product"
        yaxis_value="Unit Sales"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 02.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 02.05: Verify Y-Axis Title")
        
        """    3. Save and run the report    """
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame()
        miscobj.verify_arChartToolbar("MAINTABLE_0",['More Options','Advanced Chart','Original Chart'],"Step 03.01: Verify Chart toolbar")
        x_val_list=['Coffee : Capuccino', 'Coffee : Espresso', 'Coffee : Latte']
        y_val_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_0', x_val_list, y_val_list, "Step 03.02")
        expected_tooltip=['Category:  Coffee', 'Product:  Latte', 'Unit Sales:  878063', 'Filter Chart', 'Exclude from Chart']
        miscobj.verify_active_chart_tooltip('MAINTABLE_0', 'riser!s0!g2!mbar', expected_tooltip, "Step 03.03: verify the chart tooltip with fill color")
        xaxis_value="Category : Product"
        yaxis_value="Unit Sales"
        resultobj.verify_xaxis_title("MAINTABLE_0", xaxis_value, "Step 03.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_0", yaxis_value, "Step 03.05: Verify Y-Axis Title")
        utillobj.verify_chart_color("MAINTABLE_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 03.06: Verify bar color")
        verify_dd_list=['Coffee', 'Food', 'Gifts']  
        def_value='Coffee'
        def_msg='Step 03.07: Verify Global FILTER is showing Coffee'
        list_msg="Step 03.08: Verify the list of values in drop down box"
        utillobj.verify_dropdown_value(".arDashboardMergeDropdown", value_list=verify_dd_list, msg=list_msg, expected_default_selected_value=def_value, default_selection_msg=def_msg)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        utillobj.switch_to_frame()
        
        """    4. Note that Product values are displayed as drop down in top of browser, and changing values should affect the Chart as per selection.    """
            
        def select_combo_box_item(combobox_item, combobox_dropdown_css=".arDashboardMergeDropdown"):
            '''
            Desc:- This function is used to select an item from the combobox. 
            '''
            combodropdown_elem = self.driver.find_element_by_css_selector(combobox_dropdown_css)
            core_utils.left_click(combodropdown_elem)
            menu_items=self.driver.find_elements_by_css_selector(combobox_dropdown_css+' option')
            actual_popup_list=[el.text.strip() for el in menu_items]
            print(menu_items[actual_popup_list.index(combobox_item)])
            core_utils.left_click(menu_items[actual_popup_list.index(combobox_item)],'bottom_middle')
            time.sleep(1)
        if Global_variables.browser_name=="firefox": 
            select_combo_box_item('Gifts') #passing gifts to select Food in firefox browser
        else:
            select_combo_box_item('Food')

        time.sleep(8)
        miscobj.verify_arChartToolbar("MAINTABLE_0",['More Options','Advanced Chart','Original Chart'],"Step 04.01: Verify Chart toolbar")
        x_val_list=['Food : Biscotti', 'Food : Croissant', 'Food : Scone']
        y_val_list=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_0', x_val_list, y_val_list, "Step 04.02")
        xaxis_value="Category : Product"
        yaxis_value="Unit Sales"
        resultobj.verify_xaxis_title("MAINTABLE_0", xaxis_value, "Step 04.03: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_0", yaxis_value, "Step 04.04: Verify Y-Axis Title")
        utillobj.verify_chart_color("MAINTABLE_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 04.05: Verify bar color")
        utillobj.switch_to_default_content(pause=3)
        
        """   Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()