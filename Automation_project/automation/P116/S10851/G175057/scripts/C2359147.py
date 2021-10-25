'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2359147
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous
from common.lib import utillity

class C2359147_TestClass(BaseTestCase):

    def test_C2359147(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2359147'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        
        """    1. Launch IA to develop a Document.
        Select 'GGSales' as master file, and change output format as Active report
        Select Category, Product, and Unit Sales to get a report    """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10851_1', 'mrid', 'mrpass')
        utillobj.wait_for_page_loads(20)
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=35, string_value='Document') 
        metaobj.datatree_field_click("Category", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 2, expire_time=15)    
        metaobj.datatree_field_click("Product", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 5, expire_time=15)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 8, expire_time=15)
        
        
        """    2. Drag and drop 'Product' into Coordinated area    """
        metaobj.drag_drop_data_tree_items_to_query_tree('Product',1,'Coordinated',0,target_cord='middle')
        time.sleep(8)
        coln_list = ["Category", "Product", "Unit Sales"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1 ", coln_list, "Step 01.01: Verify column titles")
        #ia_resultobj.create_report_data_set('TableChart_1 ', 2, 3, Test_Case_ID + '_Ds01.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1 ', 2, 3, Test_Case_ID + '_Ds01.xlsx', 'Step 01.02: Verify Preview report dataset')
               
        """    3. Save and run the report    """
        """    Note that Product values are displayed as drop down in top of browser, and changing values should affect the report as per selection.    """
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame()
        miscobj.verify_page_summary(0, '1of10records,Page1of1', 'Step 03.01: Verify the Report Heading')
        column_list=['Category', 'Product', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 03.02: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID + '_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID + '_Ds02.xlsx', 'Step 03.03: Verify data.')
        verify_dd_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        list_msg="Step 03.04: Verify the list of values in drop down box"
        def_value='Biscotti'
        def_msg='Step 03.05: Verify Global FILTER is showing Biscotti'
        utillobj.verify_dropdown_value(".arDashboardMergeDropdown", value_list=verify_dd_list, msg=list_msg, expected_default_selected_value=def_value, default_selection_msg=def_msg)
        
        utillobj.select_dropdown(".arDashboardMergeDropdown","visible_text",'Latte')
        miscobj.verify_page_summary(0, '1of10records,Page1of1', 'Step 03.06: Verify the Report Heading')
        column_list=['Category', 'Product', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 03.07: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID + '_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID + '_Ds03.xlsx', 'Step 03.08: Verify data.')
        verify_dd_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        list_msg="Step 03.09: Verify the list of values in drop down box"
        def_value='Latte'
        def_msg='Step 03.10: Verify Global FILTER is showing Latte'
        utillobj.verify_dropdown_value(".arDashboardMergeDropdown", value_list=verify_dd_list, msg=list_msg, expected_default_selected_value=def_value, default_selection_msg=def_msg)
                
        """   Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()