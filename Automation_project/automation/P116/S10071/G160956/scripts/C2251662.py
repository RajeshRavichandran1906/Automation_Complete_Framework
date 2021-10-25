'''
Created on Jan 31, 2018

@author: BM13368
TestCase id : http://172.19.2.180/testrail/index.php?/cases/view/2251662
TestCaseName : Style headings and footings in the report output for the selected heading or footing
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous, ia_styling, ia_run
from common.lib import utillity

class C2251662_TestClass(BaseTestCase):

    def test_C2251662(self):
        
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2251662'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        """
            Step 01:Launch IA to develop a Document.
            Select 'GGSales' as master file, and change output format as Active report.
            Select Category, Product,Unit Sales to get a report
        """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10071_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 60)
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, 25)
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 5, 25)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 8, 25)
        """
            Expect to see the following report with two BY fields and single measure field.
        """
        coln_list = ["Category", "Product", "Unit Sales"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 01:01: Verify column titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 2, 3, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 01:02: Verify Preview report dataset')
        """ 
            Step 02:Now, select Drop down button from 'Insert' tab
        """
        ribbonobj.select_ribbon_item("Insert", "Drop_down")
        ribbonobj.repositioning_document_component('6.00', '1.4')
        """     
            Step 03:Right click on Drop down button and select properties then assign UNIT SALES in 'Field',
        """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1','Properties')
        
        source={'select_field':'Unit Sales'}
        resultobj.customize_active_dashboard_properties(source=source, msg="Step 03:01:", btn_type='ok')
        time.sleep(3)
        ia_resultobj.verify_active_dashboard_prompts("dropdown", "#Prompt_1", ['[All]'], "Step 03:01:Verify dropdown value")
        """
            Step 04:Select the report in canvas
        """
        report_css_elem=self.driver.find_element_by_css_selector("#TableChart_1")
        utillobj.click_on_screen(report_css_elem, "middle", click_type=0)
        time.sleep(2)
        """ 
            Step 05:From Home tab, in the Report group, click on Style icon. now you can see Report Style dialog box window
        """
        ribbonobj.select_ribbon_item("Home", "Style")
        utillobj.synchronize_with_number_of_element("#styleDlg [class*='active'] [class*='window'][class*='caption']", 1, 25)
         
        """ 
            Step 06:Set the following option Font type verdana and size to 10 select Bold/Italic/Underline option , set to left Align ment, set the Font color to Green and Background color to orange
        """
        ia_stylingobj.set_report_style(font_name='VERDANA', font_size='10', bold=True, italic=True, underline=True, left_justify=True, text_color='lime', background_color='coral', btn_apply=True, btn_ok=True)
        time.sleep(1)     
        """ 
            Step 07:Home tab in the Report group, click on Header & Footer option Report Header Type the text as Report Header and Arial and size to 10 select Bold/Italic/Underline option , set to center align ment, set the Font color to Maroon and Background color to silver
            Expect to see the following Header and Footer dialog window,
        """
        ia_stylingobj.create_header_footer('ribbon','Report Header', 'Report Header', font_name='ARIAL', font_size='10', italic=True, underline=True, center_justify=True, text_color='maroon', background_color='light_gray')
        time.sleep(1)
        """
            Step 08:In the same Header & Footer window, click on Report Footer tab and type the text as Report Footer and Arial and size to 10 select Bold/Italic/Underline option , set to center align ment, set the Font color to Maroon and Background color to silver
        """
        ia_stylingobj.create_header_footer('frame', 'Report Footer', 'Report Footer', font_name='ARIAL', font_size='10', center_justify=True, text_color='maroon', background_color='light_gray', btn_apply=True, btn_ok=True)
        time.sleep(4)
        
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=1, bg_color='light_gray', msg='Step 08:01:Verify report background color')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='maroon', bold=True, italic=True, text_value='Report Header', msg='Step 08:02:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 4, cell_no=11, bg_color='light_gray', msg='Step 08:03: Report Footer background color')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='maroon', bold=True, italic=True, text_value='Report Footer', msg='Step 08:04:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 1, bg_cell_no=4, bg_color='coral', font_color='lime', font_name='VERDANA',text_value='Category', font_size='10pt', bold=True, italic=True, underline=True, msg='Step 08:05: ')
             
        """ 
            Step 09:Save and run the report
        """
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 09:01: Verify the Report Heading')
        column_list=['Category', 'Product', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', column_list, "Step 09:02: Verify the Run Report column heading")
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID +'_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID +'_Ds02.xlsx', "Step 09:03: Verify entire Data set in Run Report on Page 1")
        
        """
            Verify the report styling and report Header and Footer applied correclty as applied in the step 7,8 and 9
        """
        ia_runobj.verify_table_cell_property("#ITableData0", 1, 1, bg_color='light_gray', text_value='Report Header', msg='Step 09:01:')
        ia_runobj.verify_table_cell_property("#ITableData0", 2, 1, bg_color='coral', text_value='Category', msg='Step 09:02:')
        ia_runobj.verify_table_cell_property("#ITableData0", 13, 1, bg_color='light_gray', text_value='Report Footer', msg='Step 09:03:')
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_1", value_list=['[All]', '186534', '189217', '190081', '190695', '308986', '333414', '360570', '421377', '630054', '878063'], msg="Step 09:04:Verify the dropdown values", expected_default_selected_value='[All]', default_selection_msg="Step 09:05:Verify the default value has selected as All")

if __name__ == "__main__":
    unittest.main()