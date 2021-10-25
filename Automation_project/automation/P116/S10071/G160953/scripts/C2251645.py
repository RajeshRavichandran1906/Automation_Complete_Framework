'''
Created on 17-Jan-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251645
TestCase Name = Verify that same syntax available in report and text editor
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, visualization_resultarea, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2251645_TestClass(BaseTestCase):

    def test_C2251645(self):
        """
        TESTCASE VARIABLES
        """
        test_case_id = 'C2251645'
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        legacy_obj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        
        """ Step 1: Launch IA to develop a document.
                    Select 'GGSales' as master file, and change output format as Active report. 
                    Select Category, Product ID, Product, State, Unit Sales and Dollar Sales to get a report
        """
        utillobj.infoassist_api_login('document', 'ibisamp/ggsales', 'S10071_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 95)
        vis_ribbon.switch_ia_tab('Home')
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 1: Verify output format as Active report.")
        
        vis_metadata.datatree_field_click('Category', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, 60)
        
        vis_metadata.datatree_field_click('Product ID', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 5, 60)
        
        vis_metadata.datatree_field_click('Product', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(6)"
        utillobj.synchronize_with_visble_text(element_css, 'Product', 25)
        vis_metadata.datatree_field_click('State', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(7)"
        utillobj.synchronize_with_visble_text(element_css, 'State', 25)
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(3)"
        utillobj.synchronize_with_visble_text(element_css, 'UnitSales', 25)
        vis_metadata.datatree_field_click('Dollar Sales', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(4)"
        utillobj.synchronize_with_visble_text(element_css, 'DollarSales', 2)
        
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 6, 0, 0, test_case_id + '_Ds01.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1', 2, 6, 0, 0, test_case_id + '_Ds01.xlsx', "Step 1.1: Verify Category, Product, Unit Sales report.")
             
        """ Step 2: Now, select Drop down prompt from 'Insert' tab and drag to the right of report.
        """
          
        vis_ribbon.select_ribbon_item("Insert", "Drop_down")
        utillobj.synchronize_with_number_of_element("#Prompt_1", 1, 35)
        ia_resultobj.drag_drop_document_component('#Prompt_1', '#TableChart_1', 70, 0)
            
        """ Step 3: Now, select List prompt from 'Insert' tab and drag to the right of drop down prompt.
        """
        vis_ribbon.select_ribbon_item("Insert", "List")
        utillobj.synchronize_with_number_of_element("#Prompt_2", 1, 35)
        ia_resultobj.drag_drop_document_component('#Prompt_2', '#Prompt_1', 70, 0)
            
        """ Step 4: Now, select Check box prompt from 'Insert' tab and drag to the right of List prompt.
        """
        vis_ribbon.select_ribbon_item("Insert", "Checkbox")
        utillobj.synchronize_with_number_of_element("#Prompt_3", 1, 35)
        ia_resultobj.drag_drop_document_component('#Prompt_3', '#Prompt_2', 70, 0)
          
        """ Step 5: Right click on Dropdown prompt and assign a field as follows:
                    Click ComboBox_1 --> from Field select Category
                    Click List_2 --> from Field select Product ID
                    Click CheckBox_3 --> from Field select Product
                    Make sure Condition = Equal to and Include All is checked.
        """
        """ Step 6: Select Ok.
        """
        vis_resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        ComboBox_1_source = {'select_field':'Category', 'verify_condition':'Equal to', 'verify_sort':'Ascending', 'verify_includeall':True}
        List_2_source = {'select_field':'Product ID', 'verify_condition':'Equal to', 'verify_sort':'Ascending', 'verify_includeall':True}
        CheckBox_3_source = {'select_field':'Product', 'verify_condition':'Equal to', 'verify_sort':'Ascending', 'verify_includeall':True}
        List_2_prompt = {'select_prompts':'list_2'}
        CheckBox_3_prompt = {'select_prompts':'checkbox_3'}
        vis_resultobj.customize_active_dashboard_properties(source=ComboBox_1_source, msg="Step 5.", btn_type='Apply')
        vis_resultobj.customize_active_dashboard_properties(prompts=List_2_prompt, source=List_2_source, msg="Step 5.1.", btn_type='Apply')
        vis_resultobj.customize_active_dashboard_properties(prompts=CheckBox_3_prompt, source=CheckBox_3_source, msg="Step 5.2.")
        time.sleep(1)
        ia_resultobj.verify_active_dashboard_prompts("#Prompt_1", ['[All]'], 'dropdown', "step 5.3: verify Dropdown prompt value.")
        ia_resultobj.verify_active_dashboard_prompts("#Prompt_2", ['[All]', 'C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121'], 'listbox', "step 5.4: verify listbox prompt value.")
        ia_resultobj.verify_active_dashboard_prompts("#Prompt_3", ['[All]', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos'], 'checkbox', "step 5.5: verify checkbox prompt value.")
          
        """ Step 7: Save Document as DB with prompts.fex
        """
        vis_ribbon.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as('prompts')
        utillobj.wf_logout()
        utillobj.login_wf('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#PortalResourcevBOX table tr td", 'Domains', 45)
           
        """ Step 8: Edit fex with Text Editor to check the code
                    Check code in Text editor.
        """
        legacy_obj.select_menu('P116->S10071_2->prompts', 'Edit With...->Text Editor')
        utillobj.synchronize_with_number_of_element("#bipEditor [class*='active'] #bipEditorArea", 1, 35)
        expected_syntax_list = ["OBJECT=combobox, NAME=Prompt_1, ARDATA_REPORT='TableChart_1', ARDATA_COLUMN='CATEGORY', ARFILTER_TARGET='TableChart_1,', ARFILTER_CONDITION='EQ', ARFILTER_MULTIPLE='OFF', ARFILTER_SHOWALL='ON', ARFILTER_VALUEASIS='OFF', ARFILTER_SORT='ASCENDING', ARFILTER_SHOWTITLE='', FONT='ARIAL', SIZE=9, STYLE=NORMAL, COLOR=RGB(20 20 20), POSITION=(6.15625 1.083333), DIMENSION=(1.041666 0.25)",
                                "OBJECT=list, NAME=Prompt_2, ARDATA_REPORT='TableChart_1', ARDATA_COLUMN='PCD', ARFILTER_TARGET='TableChart_1,', ARFILTER_CONDITION='EQ', ARFILTER_MULTIPLE='ON', ARFILTER_SHOWALL='ON', ARFILTER_VALUEASIS='OFF', ARFILTER_SORT='ASCENDING', ARFILTER_SHOWTITLE='', FONT='ARIAL', SIZE=9, STYLE=NORMAL, COLOR=RGB(20 20 20), POSITION=(7.479166 1.125), DIMENSION=(1.041666 1.041666)",
                                "OBJECT=checkbox, NAME=Prompt_3, ARDATA_REPORT='TableChart_1', ARDATA_COLUMN='PRODUCT', ARFILTER_TARGET='TableChart_1,', ARFILTER_CONDITION='EQ', ARFILTER_MULTIPLE='ON', ARFILTER_SHOWALL='ON', ARFILTER_VALUEASIS='OFF', ARFILTER_SORT='ASCENDING', ARFILTER_SHOWTITLE='', FONT='ARIAL', SIZE=9, STYLE=NORMAL, COLOR=RGB(20 20 20), POSITION=(8.802083 1.166666), DIMENSION=(1.041666 1.041666)"]
        texteditor_text = self.driver.find_element_by_css_selector("#bipEditor [class*='active'] #bipEditorArea").get_attribute('value')
        for syntax in expected_syntax_list :
            if syntax in texteditor_text :
                status=True
            else :
                status=False
                break
        utillity.UtillityMethods.asequal(self,True,status,"Step 8: Verify text editor syntax.")
        elem = self.driver.find_element_by_css_selector("#bipEditor [class*='active'] [class*='window'][class*='close']")
        utillobj.click_on_screen(elem, 'middle', click_type=0)
        time.sleep(2)
        utillobj.wf_logout()
         
        """ Step 9: Edit Document in IA and click View source.
                    Same syntax should be in Text editor.
        """
        utillobj.infoassist_api_edit('prompts', 'document', 'folder', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_number_of_element("#Prompt_1", 1, 95)
         
        expected_show_fex = ["OBJECT=combobox, NAME=Prompt_1, ARDATA_REPORT='TableChart_1', ARDATA_COLUMN='CATEGORY', ARFILTER_TARGET='TableChart_1,', ARFILTER_CONDITION='EQ', ARFILTER_MULTIPLE='OFF', ARFILTER_SHOWALL='ON', ARFILTER_VALUEASIS='OFF', ARFILTER_SORT='ASCENDING', FONT='ARIAL', SIZE=9, STYLE=NORMAL, COLOR=RGB(20 20 20), POSITION=(6.15625 1.083333), DIMENSION=(1.041666 0.25)",
                             "OBJECT=list, NAME=Prompt_2, ARDATA_REPORT='TableChart_1', ARDATA_COLUMN='PCD', ARFILTER_TARGET='TableChart_1,', ARFILTER_CONDITION='EQ', ARFILTER_MULTIPLE='ON', ARFILTER_SHOWALL='ON', ARFILTER_VALUEASIS='OFF', ARFILTER_SORT='ASCENDING', FONT='ARIAL', SIZE=9, STYLE=NORMAL, COLOR=RGB(20 20 20), POSITION=(7.479166 1.125), DIMENSION=(1.041666 1.041666)",
                             "OBJECT=checkbox, NAME=Prompt_3, ARDATA_REPORT='TableChart_1', ARDATA_COLUMN='PRODUCT', ARFILTER_TARGET='TableChart_1,', ARFILTER_CONDITION='EQ', ARFILTER_MULTIPLE='ON', ARFILTER_SHOWALL='ON', ARFILTER_VALUEASIS='OFF', ARFILTER_SORT='ASCENDING', FONT='ARIAL', SIZE=9, STYLE=NORMAL, COLOR=RGB(20 20 20), POSITION=(8.802083 1.166666), DIMENSION=(1.041666 1.041666)"]
        ia_resultobj.verify_fexcode_syntax(expected_show_fex, "Step 9: Verify view source")
        
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()