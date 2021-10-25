'''
Created on Jan 31, 2018

@author: BM13368
TestSuite ID:http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2251708
TestCase Name :Verify that user can import an already created report to the document
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, active_miscelaneous,visualization_resultarea,ia_run
from common.lib.basetestcase import BaseTestCase

class C2251708_TestClass(BaseTestCase):

    def test_C2251708(self):
        """
        TESTCASE VARIABLES
        """
        Report_fex='AHTML.001'
        Test_Case_ID = 'C2251708'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        resultobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)

        """
            Step 01:Create New> Report via IA tool.
            Select 'GGSales' as master file, and select format of a report as Active report.
            Add Category Product ID, Unit Sales
        """
        utillobj.infoassist_api_login('report','ibisamp/ggsales','P116/S10071_4', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1", 1, 85)
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, 35)
        metaobj.datatree_field_click("Product ID", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 5, 35)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 8, 35)
        column_list=['Category', 'Product ID', 'Unit Sales']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", column_list, "Step 01:01: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 3, Test_Case_ID+"_Ds00.xlsx", 'Step 01:02: Verify Preview report dataset')
        
        """ 
            Step 02:Save the report and run the report (Note: Report should be save as AHTML.001)
        """
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Report_fex)
        utillobj.infoassist_api_logout()
        utillobj.synchronize_with_number_of_element("#dlgAlreadySignon", 1, 35)
        
        """ 
            Step 03:Launch IA to develop a Document.
            Select 'GGSales' as master file, and make sure format of the report is Active report.
            Select 'Existing Report' from 'insert' tab
        """
        utillobj.infoassist_api_login('Document','ibisamp/ggsales','P116/S10071_4', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 80)
        ribbonobj.select_ribbon_item("Insert", "Existing_Report")
         
        """
            Step 04:Select the saved AHTML.001 report and click Ok.
            Verify preview shows the existing report.
        """
        utillobj.select_masterfile_in_open_dialog('S10071_4', Report_fex)
        utillobj.synchronize_with_number_of_element("#IncludeTable_1 div[class^='x']", 8, 50)
        column_list=['Category', 'Product ID', 'Unit Sales']
        resultobj.verify_report_titles_on_preview(3, 3, "IncludeTable_1", column_list, "Step 04:01: Verify column titles")
        ia_resultobj.verify_report_data_set('IncludeTable_1', 2, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 04:02: Verify Preview report dataset')
        """ 
            Step 05:Select 'List' from 'insert' tab
        """
        ribbonobj.select_ribbon_item("Insert", "list")
        ribbonobj.repositioning_document_component('6.00', '1.4')
        ia_resultobj.verify_active_dashboard_prompts("listbox", "#Prompt_1", ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5'], "Step 05:01:Verify dropdown value")
        """ 
            Step 06:Right click on list box and select properties. Select field as Product ID
            Step 07:Click 'OK', and Run the report
        """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1','Properties')
        utillobj.synchronize_with_number_of_element("#adpPropertiesDlg [class*='active'] [class*='window'][class*='caption']", 1, 15)
        source={'select_field':'Product ID'}
        resultobj.customize_active_dashboard_properties(source=source, msg="Step 06:01:", btn_type='ok')
        time.sleep(3)
        ia_resultobj.verify_active_dashboard_prompts("listbox", "#Prompt_1", ['[All]', 'C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121'], "Step 07:01:Verify listbox values")
        """ 
            Step 08:Select 'C141' and verify that only 1 record for that value is returned.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 25)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        ia_runobj.verify_active_dashboard_prompts('listbox', "#PROMPT_1_cs", ['[All]', 'C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121'], "Step 08:01:Verify list of values in the list box")
        ia_runobj.select_active_dashboard_prompts('listbox','#PROMPT_1_cs', ['C141'])
        miscobj.verify_page_summary(0, '1of10records,Page1of1', 'Step 08:02: Verify the Report Heading')
        column_list=['Category', 'Product ID', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', column_list, "Step 08:03: Verify the Run Report column heading")
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID +'_Ds02.xlsx', "Step 08:04: Verify entire Data set in Run Report on Page 1")

if __name__ == "__main__":
    unittest.main()