'''
Created on Jan 18, 2018.
@author: Niranjan.
'''
import unittest
import time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.pages import ia_resultarea, ia_run
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon 


class C2251606_TestClass(BaseTestCase):

    def test_C2251606(self):
        driver = self.driver
        miscobj = active_miscelaneous.Active_Miscelaneous(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)  
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        ia_runobj = ia_run.IA_Run(driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(driver)
        utillobj = utillity.UtillityMethods(self.driver)
        """ 
        Step 1: Launch IA to develop a new Document.
        Select 'GGSales' as master file, and change output format as Active report
        Select Category, Product,Unit Sales to get a report
        """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10071_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 60)
        active_format_btn_css="#HomeFormatType img[src*='active_reports_32']"
        utillobj.verify_element_visiblty(element_css=active_format_btn_css, msg='Step 1.0: Verify if the active report output fromat is selected by default.')
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 1.1: Verify output format as Active report.")
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, 20)
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 5, 20)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 8, 20)
        coln_list = ["Category", "Product", "Unit Sales"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1 ", coln_list, "Step 1.1: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1 ', 2, 3, 'C2251606_Ds01.xlsx', 'Step 1.2: Verify Preview report dataset')
        
        """
        2. Now, select List box and insert into the dashbaord
        """
        ribbonobj.select_ribbon_item("Insert", "List")
        utillobj.synchronize_with_number_of_element("#Prompt_1", 1, 35)
        ribbonobj.repositioning_document_component('5', '1')
        
        """
        3. Right click on each control and assign Unit sales in property of list box. Make sure Condition=Equal to and Include All is checked.
        4. Click Ok. Document will show the prompt with assigned values.
        """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        source={'select_field':'Unit Sales', 'verify_condition':'Equal to', 'includeall':'no'}
        resultobj.customize_active_dashboard_properties(source=source, msg='Step 3', btn_type='ok')
        list_box_values=['[All]', '66', '67', '68', '69']
        msg="Step 4.1: List box is shown with some assigned valued on canvas."
        ia_resultobj.verify_active_dashboard_prompts('listbox','#Prompt_1', list_box_values,msg)
        
        """
        5. Click Check box from 'Insert' tab and insert into the dashboard
        """
        ribbonobj.select_ribbon_item("Insert", "Checkbox")
        utillobj.synchronize_with_number_of_element("#Prompt_2", 1, 35)
        ribbonobj.repositioning_document_component('5', '3')
        
        """
        6. Right click on each control and assign Category in property of Check box. Make sure Condition=Equal to and Include All is checked.
        7. Click Ok. Document will show the prompt with assigned values.
        """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_2', 'Properties')
        source={'select_field':'Category', 'verify_condition':'Equal to', 'includeall':'no'}
        resultobj.customize_active_dashboard_properties(source=source, msg='Step 3', btn_type='ok')
        time.sleep(5)
        check_box_values=['[All]', 'Coffee', 'Food', 'Gifts']
        msg="Step 7.1: Check box is shown with some assigned valued on canvas."
        ia_resultobj.verify_active_dashboard_prompts('checkbox', '#Prompt_2', check_box_values, msg)
        
        """
        8. Click run.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 160)
        utillobj.switch_to_frame()
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 8.1: Verify the Report Heading')
        column_list=["Category", "Product", "Unit Sales"]
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 8.2: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251606_Ds02.xlsx', 'Step 8.2: Verify table data after Run.')
        
        """
        9. Select multiple options in List box, note that output is changed according to selection.
        Choose 190695 and 308986 values from List box and notice that report is filtered according to selection
        """
        ia_runobj.select_active_dashboard_prompts('listbox','#PROMPT_1_cs', ['190695', '308986'])
        time.sleep(4)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251606_Ds03.xlsx', 'Step 8.2: Verify table data after selecting multiple values in list box.')
        """
        10. Select multiple options in Check box, note that output is changed according to selection.
        Choose Coffee and Food values from Check box and notice that report is filtered according to selection
        """
        ia_runobj.select_active_dashboard_prompts('checkbox','#PROMPT_2_cs', ['Coffee', 'Food'])
        time.sleep(4)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251606_Ds04.xlsx', 'Step 8.2: Verify table data after selecting multiple values in check box.')
        utillobj.switch_to_default_content(pause=3)

if __name__ == '__main__':
    unittest.main()