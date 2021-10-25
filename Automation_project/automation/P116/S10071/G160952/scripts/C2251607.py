'''
Created on Jan 24, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251607
TestCase Name = Verify image, text box and Check box ADPs work properly in a new report
'''

import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, active_miscelaneous, visualization_resultarea, ia_run
from common.lib.basetestcase import BaseTestCase

class C2251607_TestClass(BaseTestCase):

    def test_C2251607(self):
        """
        TESTCASE VARIABLES
        """
        test_case_id = 'C2251607'
        field_element_css="#TableChart_1 div[class^='x']"
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
        Select Category, Product, State, Product ID, Unit Sales and Dollar Sales to get a report
        """
        utillobj.infoassist_api_login('document', 'ibisamp/ggsales', 'S10071_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 60)
        vis_ribbon.switch_ia_tab('Home')
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 01: Verify output format as Active report.")
          
        vis_metadata.datatree_field_click('Category', 2, 0)
        utillobj.synchronize_with_number_of_element(field_element_css, 2, 20)
            
        vis_metadata.datatree_field_click('Product', 2, 0)
        utillobj.synchronize_with_number_of_element(field_element_css, 5, 20)
          
        vis_metadata.datatree_field_click('State', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(6)"
        utillobj.synchronize_with_visble_text(element_css, 'State', 20)
          
        vis_metadata.datatree_field_click('Product ID', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(7)"
        utillobj.synchronize_with_visble_text(element_css, 'ProductID', 20)
           
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(3)"
        utillobj.synchronize_with_visble_text(element_css, 'UnitSales', 20)
          
        vis_metadata.datatree_field_click('Dollar Sales', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(4)"
        utillobj.synchronize_with_visble_text(element_css, 'DollarSales', 20)
          
        coln_list = ["Category", "Product", "State", "Product ID", "Unit Sales", "Dollar Sales"]
        vis_resultobj.verify_report_titles_on_preview(6, 6, "TableChart_1 ", coln_list, "Step 1.1: Verify report1 titles")
         
        """ 
        Step 02: Add a image by Selecting "Image" from 'Insert' tab.
        """
        vis_ribbon.select_ribbon_item('Insert', 'image')
        utillobj.synchronize_with_visble_text("#IbfsOpenFileDialog7_btnOK div", 'Open', 45)
         
        """
        Step 03: Select "SMPLOGO1" image
        Step 04: Click Ok. Image will appear on the dashboard. Drag the image above report.
        """
        utillobj.ibfs_save_as('smplogo1')
        utillobj.synchronize_with_number_of_element("#PageItemImage_1 img[src*='config']",1,20)
        ia_resultobj.drag_drop_document_component('#PageItemImage_1', '#TableChart_1', 95, 0)
 
        """
        Step 05: Add a text by selecting "Text Box" from 'Insert' tab
        Step 06: Drag Tex box next to image.
        """
        vis_ribbon.select_ribbon_item("Insert", "Text_Box")
        utillobj.synchronize_with_number_of_element("#Text_1",1,20)
        ia_resultobj.drag_drop_document_component('#Text_1', '#PageItemImage_1', 85, 0)
         
        """ 
        Step 07: Highlight "Enter text here" text and overwrite as 'SAMPLE TEXT'
        """
        ia_resultobj.enter_text_in_Textbox('Text_1', "SAMPLE TEXT")
         
        """ 
        Step 08: Add 'Checkbox' from 'Insert' tab
        Step 09: Drag check box next to report 
        """
        vis_ribbon.select_ribbon_item("Insert", "Checkbox")
        utillobj.synchronize_with_number_of_element("#Prompt_1", 1, 25)
        ia_resultobj.drag_drop_document_component('#Prompt_1', '#PageItemImage_1', 85, 0,  target_drop_point='bottom_middle')
        time.sleep(5) 
         
        """ 
        Step 10: Right click on Check Box, and select properties
        """
        vis_resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
         
        """ 
        Step 11: Add Unit Sales to Field. Make sure Condition = Equal to and Include All is checked. 
        Step 12: Select OK
        """
        ComboBox_1_source = {'select_report':'Report1', 'select_field':'Unit Sales', 'verify_condition':'Equal to', 'verify_includeall':True}
        vis_resultobj.customize_active_dashboard_properties(source=ComboBox_1_source, msg="Step 11.")
        
        """ 
        Step 13: Run report
        """
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 60)
        utillobj.switch_to_frame(pause=3)
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", 'Category', 45)
        active_mis_obj.verify_page_summary(0, '107of107records,Page1of2', "Step 13.1: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds01.xlsx', " Step 13.2: Verify report at run time.")
        
        check=['[All]', '12386', '12904', '13147', '13691', '14382', '14568', '14614']
        check_defau='[All]'
        ia_runobj.verify_active_dashboard_prompts("check_box", "#PROMPT_1_cs", check, "Step 13.3: Verify check box IS SHOWING", default_selected_check=check_defau)
        
        expected_text = 'SAMPLE TEXT'
        actual_text = driver.find_element_by_css_selector("[id*='LOBJText']").text.strip()
        print(actual_text)
        utillobj.asequal(actual_text, expected_text,  "Step 13.3: Verify text in textbox")
        
        img_displayed=driver.find_element_by_css_selector("#orgdivouter0 #allLayoutObjects #EMBEDIMG0 img[src^='data']").is_displayed()
        utillobj.asequal(True, img_displayed, 'Step 13.5: Verify expected image appears on the document canvas')
        
        """ 
        Step 14: Choose 14382 value and notice that report is filtered according to selection. Verify Image, Text, , report and filter control should be displayed, without overlapping.
        """
        ia_runobj.select_active_dashboard_prompts('checkbox',"#PROMPT_1_cs",['14382'])
        time.sleep(8)
        
        active_mis_obj.verify_page_summary(0, '1of107records,Page1of1', "Step 14.1: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds02.xlsx', " Step 14.2: Verify report at run time.")
        
        expected_text = 'SAMPLE TEXT'
        actual_text = driver.find_element_by_css_selector("[id*='LOBJText']").text.strip()
        print(actual_text)
        utillobj.asequal(actual_text, expected_text,  "Step 14.3: Verify text in textbox")
        
        check=['[All]', '12386', '12904', '13147', '13691', '14382', '14568', '14614']
        ia_runobj.verify_active_dashboard_prompts("check_box", "#PROMPT_1_cs", check, "Step 14.4: Verify check box IS SHOWING")
        
        img_displayed=driver.find_element_by_css_selector("#orgdivouter0 #allLayoutObjects #EMBEDIMG0 img[src^='data']").is_displayed()
        utillobj.asequal(True, img_displayed, 'Step 14.5: Verify expected image appears on the document canvas')
        
        time.sleep(5)
        utillobj.switch_to_default_content(pause=1)
       
        
if __name__ == '__main__':
    unittest.main()