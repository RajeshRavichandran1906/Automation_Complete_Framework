'''
Created on Jan 15, 2018
TestSuite : AR14 - Active Document
TestSuite ID : http://172.19.2.180/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc&group_id=160952
TestCase ID: http://172.19.2.180/testrail/index.php?/cases/view/2251612
TestSuite Name : Verify that user is able to delete the existing dashboard controls (e.g. Drop down)
@author: BM13368
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous
from common.lib import utillity

class C2251612_TestClass(BaseTestCase):

    def test_C2251612(self):
        
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2251612'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
            Step 01:Launch IA to develop a new Document.
            Select 'GGSales' as master file, and change output format as Active report.
            Add Category Product ID,Product,State,Unit Sales,Dollar Sales to develop a report
        """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10071', 'mrid', 'mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=65, string_value='Document')
        metaobj.datatree_field_click("Category", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 2, expire_time=30)    
        metaobj.datatree_field_click("Product ID", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 5, expire_time=30)
        metaobj.datatree_field_click("Product", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 8, expire_time=30)    
        metaobj.datatree_field_click("State", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 28, expire_time=30)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 48, expire_time=30)
        metaobj.datatree_field_click("Dollar Sales", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 68, expire_time=30)
        
        coln_list = ["Category", "Product ID", "Product", "State", "Unit Sales", "Dollar Sales"]
        resultobj.verify_report_titles_on_preview(6, 6, "TableChart_1 ", coln_list, "Step 01:01: Verify column titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 18, 6, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 18, 6, Test_Case_ID+"_Ds01.xlsx", 'Step 01:02: Verify Preview report dataset')
        """ 
            Step 02:Select 'Drop Down' from 'Insert' tab and drag it to the right side.
        """
        ribbonobj.select_ribbon_item("Insert", "Drop_down")
        ribbonobj.repositioning_document_component('6.50', '1.5')
        
        """ 
            Step 03:Right click on 'Drop down' box and select 'Properties' from canvas
        """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        
        """ 
            Step 04:Verify active dashboard properties window appears.
        """
        properties_dlg="#adpPropertiesDlg [class*='active'] [class*='window'][class*='caption']"
        resultobj.wait_for_property(properties_dlg, 1, expire_time=30)
        utillobj.verify_object_visible(properties_dlg, True, "Step 04:01:Verify properties dialog is displayed")
        """     
            Step 05:Add Field as Unit Sales. Make sure Condition is set to Equal to and Include All is checked.
            Step 06:Click Ok
        """
        source_item= {'select_report':'Report1', 'select_field':'Unit Sales', 'verify_condition':'Equal to', 'verify_includeall':True}
        resultobj.customize_active_dashboard_properties(source=source_item, msg="Step 05.")
              
        """     
            Step 07:Run the Document.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 45)
        utillobj.switch_to_frame(pause=2)
        """ 
            By default, All is the selected option under dropdown.
        """
        utillobj.synchronize_with_number_of_element("#ITableData0 #TCOL_0_C_0 span", 1, 35)
        miscobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 07:01: Verify the Report Heading')
        column_list=["Category", "Product ID", "Product", "State","Unit Sales", "Dollar Sales"]
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 07:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds02.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds02.xlsx", 'Step 07:03: Verify data.')
        expected_val='[All]'
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_1", expected_default_selected_value=expected_val, default_selection_msg="Step 07:04:Verify dropdown default valueAll is selected")
        utillobj.switch_to_default_content(pause=1)
        """
            Step 08:Close the dashboard in run time.
            On canvas, right click Drop down prompt and select 'Delete' option.
            Verify no dashboard prompt is available next to report.
        """
        resultobj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        time.sleep(10)
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Delete')
        time.sleep(8)
        utillobj.verify_object_visible("#Prompt_1", False, "Step 08:01: Verify option dropdown box is not visible")
        """ 
            Step 09:Click Run.
            Verify that deleted prompt is no more available on dashboard.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 60)
        utillobj.switch_to_frame(pause=2)
        combo_box="#combobox_dsPROMPT_1"
        utillobj.verify_object_visible(combo_box, False, "Step 09:01: Verify option dropdown box is not visible")

if __name__ == "__main__":
    unittest.main()