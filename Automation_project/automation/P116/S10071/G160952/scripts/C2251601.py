'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251601
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous
from common.lib import utillity

class C2251601_TestClass(BaseTestCase):

    def test_C2251601(self):
        
        """ TESTCASE VARIABLES """
        
        Test_Case_ID = 'C2251601'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    1. Open IA and create a new document.
        Select 'GGSales' as master file, and change output format as Active report.
        Add fields Category, Product ID, Product, State, Unit Sales & Dollar Sales to the report.
        Select 'Drop Down' from 'Insert' tab.    """
        
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10071_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 60)
        
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, 15)
           
        metaobj.datatree_field_click("Product ID", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 5, 15)
        
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 8, 15)
           
        metaobj.datatree_field_click("State", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 28, 15)
        
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 48, 15)
        
        metaobj.datatree_field_click("Dollar Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 68, 15)
               
        ribbonobj.select_ribbon_item("Insert", "Drop_down")
        
        """    2. Move Drop Down box to the right of the report. Right click on 'Drop down' box and select 'Properties' from canvas    """
        
        ia_resultobj.drag_drop_document_component("#Prompt_1", "#TableChart_1", 230, 0)
        resultobj.choose_right_click_menu_item_for_prompt("#Prompt_1", "Properties")
        
        """    3. Verify active dashboard properties window appears. Verify Report feld shows 'Report1' by default    """
        """    4. Add Unit Sales to Field    """
        """    5. Verify condition is 'Equal to' and check "All" check box. Now click OK.    """
        
        source={'select_field':'Unit Sales', 'verify_condition':'Equal to', 'verify_includeall':True}
        targets ={'verify_target_name':['Report1']}
        resultobj.customize_active_dashboard_properties(source=source, targets=targets, msg="Step 3:", btn_type='ok')
  
        
        """    6. Run the report. In the dropdown "All" option is selected by default. Verify report is filtered according to selection.    """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 40)
        utillobj.switch_to_frame()
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(2) td:nth-child(2)", "C141", 25)
        miscobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 06a: Verify the Report Heading')
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 06b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251601_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251601_Ds01.xlsx', 'Step 06c: Verify data.')
        list1=['[All]', '12386', '12904', '13147', '13691', '14382', '14568', '14614']
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_1", value_list=list1, msg='Step 6.c : Verify dropdown box values', expected_default_selected_value='[All]', default_selection_msg='Step 6.d : Verify [All] is selected as default in dropdown box')
        
        """    7. In the dropdown select "12386" option. Verify report is filtered according to selection.    """
        
        utillobj.select_dropdown("#combobox_dsPROMPT_1", 'visible_text', '12386')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(2) td:nth-child(2)", "C144", 10)
        miscobj.verify_page_summary(0, '1of107records,Page1of1', 'Step 07a: Verify the Report Heading')
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 07b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251601_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251601_Ds02.xlsx', 'Step 07c: Verify data.')
        
        """    8. In the dropdown select "15785" option. Verify report is filtered according to selection.    """
        utillobj.select_dropdown("#combobox_dsPROMPT_1", 'visible_text', '15785')
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_1", expected_default_selected_value='15785', default_selection_msg="Step 08:Verify the default value")
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(2) td:nth-child(2)", "G121", 10)
        miscobj.verify_page_summary(0, '1of107records,Page1of1', 'Step 08a: Verify the Report Heading')
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 08b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251601_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251601_Ds03.xlsx', 'Step 08c: Verify data.')
        
        """    9. In the dropdown select "141403" option. Verify report is filtered according to selection.    """
        utillobj.select_dropdown("#combobox_dsPROMPT_1", 'visible_text', '141403')
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_1", expected_default_selected_value='141403', default_selection_msg="Step 09:Verify the default value")
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(2) td:nth-child(2)", "C142", 10)
        miscobj.verify_page_summary(0, '1of107records,Page1of1', 'Step 09a: Verify the Report Heading')
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 09b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251601_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251601_Ds04.xlsx', 'Step 09c: Verify data.')
        
        """    10. Close the active dashboard runtime by clicking 'X'    """
        utillobj.switch_to_default_content()
        time.sleep(3)
        resultobj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        
        """    11. Make sure user is on Document canvas    """
        coln_list = ['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        resultobj.verify_report_titles_on_preview(6, 6, "TableChart_1 ", coln_list, "Step 11a: Verify column titles")
        #ia_resultobj.create_report_data_set('TableChart_1 ', 18, 6, 'C2251601_Ds05.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1 ', 18, 6, 'C2251601_Ds05.xlsx', 'Step 01b: Verify Preview report dataset')
        
        """    12. Right click on 'Drop down' box and select 'Properties' from canvas    """
        resultobj.choose_right_click_menu_item_for_prompt("#Prompt_1", "Properties")
        
        """    13. Click "Include All' again and check off checkbox    """
        resultobj.customize_active_dashboard_properties(source={'select_includeall':True, 'verify_includeall':False}, msg="Step:13:")
        
        """    14. Click OK and run the dashboard. Verify Drop Down prompt shows "12386" option as first value    """

        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 40)
        utillobj.switch_to_frame()
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(2) td:nth-child(2)", "C144", 25)
        miscobj.verify_page_summary(0, '1of107records,Page1of1', 'Step 14a: Verify the Report Heading')
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 14b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251601_Ds02.xlsx', 'Step 14c: Verify data.')
        
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_1", expected_default_selected_value='12386', default_selection_msg="Step 09:Verify the default value")
        utillobj.switch_to_default_content()
        
        
        """   Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()