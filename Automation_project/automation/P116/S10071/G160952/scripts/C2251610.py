'''
Created on Jan 22, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251610
TestCase Name = Verify that one active filter control can be applied to multiple reports
'''

import unittest, time, keyboard
from common.lib import utillity
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, active_miscelaneous, visualization_resultarea, ia_run
from common.lib.basetestcase import BaseTestCase

class C2251610_TestClass(BaseTestCase):

    def test_C2251610(self):
        """
        TESTCASE VARIABLES
        """
        test_case_id = 'C2251610'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        active_mis_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)

        """ 
        Step 01: Launch IA to develop a new Document.
        Select 'GGSales' as master file, and change output format as Active report.
        Select Product and Unit Slaes fields to create one report
        """
        utillobj.infoassist_api_login('document', 'ibisamp/ggsales', 'S10071_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 65)
        vis_ribbon.switch_ia_tab('Home')
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 1: Verify output format as Active report.")
          
        vis_metadata.datatree_field_click('Product', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 3,20)
         
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 6,20)
          
        coln_list = ["Product", "Unit Sales"]
        vis_resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1 ", coln_list, "Step 1.1: Verify report1 titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 2, 2, 'C2251610_Ds01.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 2, 'C2251610_Ds01.xlsx', 'Step 1.2: Verify Preview report dataset')
         
        """ 
        Step 02: Click over the white space in the document area to create another report. Select Category and Unit Sales fields.
        Verify that reports does not overlap each other.
        """ 
        parent_elem=driver.find_element_by_css_selector("#TableChart_1")
        utillobj.click_on_screen(parent_elem, 'right', click_type=0, x_offset=10) 
         
        vis_metadata.datatree_field_click('Category', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_2 div[class^='x']", 2,20)
         
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_2 div[class^='x']", 4,20)
         
        ia_resultobj.drag_drop_document_component('#TableChart_2', '#TableChart_1', 85, 0)
         
        coln_list = ["Category", "Unit Sales"]
        vis_resultobj.verify_report_titles_on_preview(2, 2, "TableChart_2", coln_list, "Step 2.1: Verify report2 titles")
#         ia_resultobj.create_report_data_set('TableChart_2', 1, 2, 'C2251610_Ds02.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_2', 1, 2, 'C2251610_Ds02.xlsx', 'Step 2.2: Verify Preview report dataset')
          
        """
        Step 03: Now select Text from insert tab.
        """
        vis_ribbon.select_ribbon_item("Insert", "Text")
        utillobj.synchronize_with_number_of_element('#Prompt_1', 1, 25)
        ia_resultobj.drag_drop_document_component('#Prompt_1', '#TableChart_2', 85, 0)
        time.sleep(5) 
        """ 
        Step 04: Right click on Text prompt and select 'Properties'
        """
        vis_resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        
        """ 
        Step 05: Select Report as Report 1. Now assign field as Unit Sales.
        Make sure Category is set to Equal to and Include All is already checked.
        Step 06: Move Report2 from Candidate Reports to Targets.
        Step 07: Select OK
        """
        ComboBox_1_source = {'select_report':'Report1', 'select_field':'Unit Sales', 'verify_condition':'Equal to', 'verify_includeall':True}
        ComboBox_1_target = {'select_candidate_report':'Report2', 'add_to_target':True}
        vis_resultobj.customize_active_dashboard_properties(source=ComboBox_1_source, targets=ComboBox_1_target, msg="Step 05.") 
         
        """ 
        Step 08: Run the report. Enter input as '190695' in text box.
        """
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 95)
        utillobj.switch_to_frame(pause=3)
        utillobj.synchronize_with_number_of_element("#ITableData0 #TCOL_0_C_0 span", 1, 45)
        
        active_mis_obj.verify_page_summary(0, '10of10records,Page1of1', "Step 08: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds03.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds03.xlsx', " Step 08.1: Verify Category, Product, Region, State, Unit Sales report generated at run time.")
        
        active_mis_obj.verify_page_summary(1, '3of3records,Page1of1', "Step 08.2: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData1', 'I1r0', test_case_id + '_Ds04.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r0', test_case_id + '_Ds04.xlsx', " Step 08.3: Verify Category, Product, Region, State, Unit Sales report generated at run time.")
        
        element=self.driver.find_element_by_css_selector('#PROMPT_1_cs input')
        exec("element.clear()")
        exec("element.send_keys('190695')")
        time.sleep(3)
        keyboard.send('enter')
        time.sleep(5)
          
#         ia_runobj.select_active_dashboard_prompts('text', "#PROMPT_1_cs", ['190695'])
         
        """ 
        Step 09: Hit enter key.
        Verify Both the reports should change according to the input given in text box.
        """
        ia_runobj.verify_active_dashboard_prompts('text', '#PROMPT_1_cs', ['190695'], "Step 09: Verify Both the reports should change according to the input given in text box.")
        
        utillobj.synchronize_with_number_of_element("#ITableData0 #TCOL_0_C_0 span", 1, 45)
        active_mis_obj.verify_page_summary(0, '1of10records,Page1of1', "Step 09.1: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds05.xlsx', " Step 09.2: Verify Category, Product, Region, State, Unit Sales report generated at run time.")
         
        active_mis_obj.verify_page_summary(1, '0of3records,Page1of1', "Step 09.3: Verify page summary of Category, Product, Region, State, Unit Sales report.")
        
        """ 
        Step 10: Same way enter input as '927880' in text box and hit enter key.
        Verify Both the reports should change according to the input given in text box.
        """
        ia_runobj.select_active_dashboard_prompts('text', "#PROMPT_1_cs", ['927880'])
        ia_runobj.verify_active_dashboard_prompts('text', '#PROMPT_1_cs', ['927880'], "Step 10: Verify Both the reports should change according to the input given in text box.")
        utillobj.synchronize_with_number_of_element("#ITableData0 #TCOL_0_C_0 span", 1, 45)
        active_mis_obj.verify_page_summary(0, '0of10records,Page1of1', "Step 10.1: Verify page summary of Category, Product, Region, State, Unit Sales report.")
         
        active_mis_obj.verify_page_summary(1, '1of3records,Page1of1', "Step 10.2: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData1', 'I1r0', test_case_id + '_Ds06.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r0', test_case_id + '_Ds06.xlsx', " Step 10.3: Verify Category, Product, Region, State, Unit Sales report generated at run time.")
        
        utillobj.switch_to_default_content(pause=1)
        
        
if __name__ == '__main__':
    unittest.main()