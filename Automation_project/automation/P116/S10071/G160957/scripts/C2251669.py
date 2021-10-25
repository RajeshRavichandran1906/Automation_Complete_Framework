'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251669
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, active_miscelaneous
from common.lib import utillity

class C2251669_TestClass(BaseTestCase):

    def test_C2251669(self):
        """ TESTCASE VARIABLES """
        
        Test_Case_ID = 'C2251669'
       
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)        
        
        """    1. Launch IA to develop a new Document.
        Select 'GGSales' as master file, and change output format as Active report.
        Select Category, Product,Unit Sales to get a report    """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10071', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 65) 
        
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, 20)
            
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 5, 25)
        
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 8, 25)
        
        coln_list = ['Category', 'Product', 'Unit Sales']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1 ", coln_list, "Step 01a: Verify column titles")
        
        """    2. Now, select 'Drop down' from 'Insert' tab    """
        ribbonobj.select_ribbon_item("Insert", "Drop_down")
        utillobj.synchronize_with_number_of_element("#Prompt_1", 1, 25)
        ribbonobj.repositioning_document_component('6', '1')
        
        """    3. Right click on 'Drop down' box and select properties    """
        
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        
        """    4. Add Unit Sales to Field and change 'Condition' as 'Greater than or equal to', select 'OK' .    """
        source_dict={'select_field':'Unit Sales', 'select_condition':'Greater than or equal to'}
        resultobj.customize_active_dashboard_properties(source=source_dict)
        
        """    5. Save and run the report    """
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame()
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0", 'Category', 65)
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 05a(1): Verify the Report Heading')
        column_list=['Category', 'Product', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 05b(1): Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251669_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251669_Ds01.xlsx', 'Step 05c(1): Verify data.')
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_1",expected_default_selected_value='[All]', default_selection_msg="Step 05d(1): Verify the first check box is 'All' and selected")
        
        """Choose 308986 value from drop-down and notice that report is filtered according to selection.
        Report should be filtered according to the given condition -'Not equal to'"""
        utillobj.select_dropdown('#combobox_dsPROMPT_1', 'value', '308986')
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0", 'Category', 30)
        miscobj.verify_page_summary(0, '6of10records,Page1of1', 'Step 05a(2): Verify the Report Heading')
        column_list=['Category', 'Product', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 05b(2): Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251669_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251669_Ds02.xlsx', 'Step 05c(2): Verify data.')
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_1",expected_default_selected_value='308986', default_selection_msg="Step 05d(2): Verify the first check box is '308986' and selected")
        utillobj.switch_to_default_content()
        time.sleep(3)
         
        
        """   Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()