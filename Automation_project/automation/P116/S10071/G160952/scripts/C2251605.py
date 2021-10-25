'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251605
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, active_miscelaneous, ia_run
from common.lib import utillity

class C2251605_TestClass(BaseTestCase):

    def test_C2251605(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2251605'
        insert_fex='C2251605a'
#         driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        oFolder=utillobj.parseinitfile('suite_id')
        
        """    1. Launch IA to develop a Report
        Select 'GGSales' as master file, and change output format as HTML
        Add Category, Product ID, and Unit Sales    """
        utillobj.infoassist_api_login('report','ibisamp/ggsales','P116/S10071_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1 [align='justify']", "Draganddropfieldsontothecanvasorintothequerypanetobeginbuildingyourreport.", 65)
        metaobj.datatree_field_click("Category", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 2, expire_time=60)    
        metaobj.datatree_field_click("Product ID", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 5, expire_time=60)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 8, expire_time=60)
        coln_list = ['Category', 'Product ID', 'Unit Sales']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1 ", coln_list, "Step 01a: Verify column titles")
        
        """    2. Save the report and run the report (Note: Report should be save as AHTML.001)    """
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(insert_fex)
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 65)
        utillobj.switch_to_frame()
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2251605_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2251605_Ds01.xlsx", "Step 02a: verify data set")
        utillobj.switch_to_default_content()
        time.sleep(2)
        
        """    3. Exit from report screen.    """
        utillobj.wf_logout()
        
        """    4. Launch IA to develop a new Document.        
        Select 'GGSales' as master file, and change output format as Active report.
        Select 'Existing Report' from 'insert' tab    """
        
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10071_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("iaCanvasCaptionLabel", 'Document', 85)
        ribbonobj.select_ribbon_item("Insert", "Existing_Report")
        open_dialog_file_name="#IbfsOpenFileDialog7_cbFileName"
        utillobj.synchronize_with_number_of_element(open_dialog_file_name, 1, 45)
        
        """    5. Load the saved AHTML.001 report    """
        utillobj.select_masterfile_in_open_dialog(oFolder, insert_fex)
        coln_list = ['Category', 'Product ID', 'Unit Sales']
        resultobj.verify_report_titles_on_preview(3, 3, "IncludeTable_1 ", coln_list, "Step 03a: Verify column titles")
        
        """    6. Select 'List' from 'insert' tab    """
        ribbonobj.select_ribbon_item("Insert", "List")
        utillobj.synchronize_with_number_of_element("#Prompt_1", 1, 25)
        ribbonobj.repositioning_document_component('8', '1')
        
        """    7. Right click on list box and select properties    """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        
        """    8. Select Product ID in field. Make sure Include All is not checked. Select 'OK'.    """
        
        source_dict={'select_field':'Product ID', 'select_includeall':True}
        resultobj.customize_active_dashboard_properties(source=source_dict, msg='Step 05(ii)')
    
        """    9. Run the report    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 65)
        utillobj.switch_to_frame()
        miscobj.verify_page_summary(0, '1of10records,Page1of1', 'Step 09a: Verify the Report Heading')
        column_list=['Category', 'Product ID', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 09b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251605_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251605_Ds02.xlsx', 'Step 09c: Verify data.')
        
        """    10. Choose C144 value and notice that report is filtered according to selection    """
        iarun.select_active_dashboard_prompts('listbox', "#list_dPROMPT_1", ['C144'])
#         utillobj.asequal(True, False, "Step 10: a,c has been failed due to JIRA -*-*-*-*- ACT-204 -*-*-*-*-")
        miscobj.verify_page_summary(0, '1of10records,Page1of1', 'Step 10a: Verify the Report Heading')
        column_list=['Category', 'Product ID', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 10b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251605_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251605_Ds03.xlsx', 'Step 10c: Verify data.')
        utillobj.switch_to_default_content()
        time.sleep(3)
        
        """    11. Save the report as AHTML as AR-AD-003a.fex    """
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """   Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()