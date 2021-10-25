'''
Created on Feb 7, 2018

@author: BM13368
TestCase ID :http://172.19.2.180/testrail/index.php?/cases/view/2251723
TestCase Name : Add Global filter in a Document of reports (GRMERGE=ADVANCED).
'''
import unittest, time, keyboard
from common.lib import utillity
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, visualization_resultarea, wf_legacymainpage, active_miscelaneous, ia_run, active_filter_selection
from common.lib.basetestcase import BaseTestCase

class C2251723_TestClass(BaseTestCase):

    def test_C2251723(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2251723'
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        legacy_obj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_run_obj=ia_run.IA_Run(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        
        """
        Step 1:Create a new Document using the ggsales file.
        Select Active Report as the Output Format.
        From the Insert icon, add a Text Box with the text "Global Filter for Document containing Reports".
        """
        utillobj.infoassist_api_login('document', 'ibisamp/ggsales', 'S10071_4', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 80)
          
        """
        From the Insert icon, add a Text Box with the text "Global Filter for Document containing Reports" .
        """
        vis_ribbon.select_ribbon_item('Insert', 'text_box')
        vis_resultobj.wait_for_property("#theCanvas #Text_1", 1, 35)
        vis_ribbon.resizing_document_component('0.25', '3.60')
        
        ia_resultobj.enter_text_in_Textbox('Text_1', "Global Filter for Document containing Reports")
        time.sleep(2)
          
        """
        Expect to see the following Document canvas with the Text Box added.
        """
        ia_resultobj.verify_text_in_Textbox('#Text_1', 'Global Filter for Document containing Reports', "Step 01:01: Verify textbox value")
          
        """
        Step 2:Select Category, Product and Unit Sales to get a report.
        Move the Report preview underneath and centered below the Text Box.
        """
        vis_ribbon.select_ribbon_item('Insert', 'report')
        time.sleep(5)
        ia_resultobj.drag_drop_document_component('#Text_1', '#TableChart_1', 0, 50, target_drop_point='bottom_middle')
        
        vis_metadata.datatree_field_click('Category', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(4)"
        utillobj.synchronize_with_visble_text(element_css, 'Category', 25)
        vis_metadata.datatree_field_click('Product', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(5)"
        utillobj.synchronize_with_visble_text(element_css, 'Product', 25)
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(3)"
        utillobj.synchronize_with_visble_text(element_css, 'UnitSales', 25)
        coln_list = ['Category', 'Product', 'Unit Sales']
        vis_resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 2.1: Verify Category, Product, Unit Sales report.")
        
        """
        Step 3:Click the Page icon in the upper left to add a new Page.
        Insert a Report on Page 2 of the Document canvas.
        """
        ia_resultobj.select_or_verify_document_page_menu("New Page")
        time.sleep(3)
        vis_ribbon.select_ribbon_item('Insert', 'report')
        time.sleep(5)
          
        """
        Step 4:Select fields Category, Product and Dollar Sales for the report on Page 2.
        Click the run button the check both reports.
        """
        vis_metadata.datatree_field_click('Category', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(4)"
        utillobj.synchronize_with_visble_text(element_css, 'Category', 25)
        vis_metadata.datatree_field_click('Product', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(5)"
        utillobj.synchronize_with_visble_text(element_css, 'Product', 25)
        vis_metadata.datatree_field_click('Dollar Sales', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(3)"
        utillobj.synchronize_with_visble_text(element_css, 'DollarSales', 25)
        coln_list = ['Category', 'Product', 'Dollar Sales']
        vis_resultobj.verify_report_titles_on_preview(3, 3, "TableChart_2", coln_list, "Step 4.2: Verify Category, Product, Unit Sales report.")
          
        """
        Step 5:Save and run the report. Close the report
        """
        vis_ribbon.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
        Run the report
        """
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
         
        """
        Step 6:Edit the report in Text Editor and change the keyword/value pair from SHOW_GLOBALFILTER=OFF to SHOW_GLOBALFILTER=ON.
        Save the report and close the text editor.
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        legacy_obj.select_repository_folder_item_menu('P116->S10071_4', Test_Case_ID, 'Edit With...->Text Editor')
        parent_css='[id="menu_button_search"]'
        utillobj.synchronize_with_number_of_element(parent_css, 1, 75)
         
        search_obj=self.driver.find_element_by_css_selector("#bipEditor #menu_bar [id='menu_button_search']")
        utillobj.default_click(search_obj)
#         utillobj.click_on_screen(search_obj, coordinate_type='middle', click_type=0)
        time.sleep(0.50)
        utillobj.select_or_verify_bipop_menu('Find')
        element=self.driver.find_element_by_css_selector("#findText")
        utillobj.default_click(element)
#         utillobj.click_on_screen(elem, coordinate_type='middle', click_type=0)
        time.sleep(0.50)
        exec("element.clear()")
        exec("element.send_keys('SHOW_GLOBALFILTER=OFF')")
#         pyautogui.typewrite(text_string, interval=0.2, pause=5)

        find_btn_elem=self.driver.find_element_by_css_selector("#btnFind")
        utillobj.default_click(find_btn_elem)
#         utillobj.click_on_screen(find_btn_elem, coordinate_type='middle', click_type=0)
        time.sleep(0.50)
        element=self.driver.find_element_by_css_selector("#replaceText")
        utillobj.default_click(element)
#         utillobj.click_on_screen(elem, coordinate_type='middle', click_type=0)
        time.sleep(0.50)
        exec("element.clear()")
        exec("element.send_keys('SHOW_GLOBALFILTER=ON')")
#         keyboard.send('enter')
#         pyautogui.typewrite(text_string, interval=0.2, pause=5)
         
        elem=self.driver.find_element_by_css_selector("#btnReplaceAll")
#         utillobj.click_on_screen(elem, coordinate_type='middle', click_type=0)
        utillobj.default_click(elem)
        time.sleep(2)
         
        legacy_obj.click_text_editor_ribbon_button('Save')
        file_elem=self.driver.find_element_by_css_selector("#menu_button_file")
#         utillobj.click_on_screen(file_elem, coordinate_type='middle', click_type=0)
        utillobj.default_click(file_elem)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Close')
         
        utillobj.infoassist_api_logout()
        time.sleep(3)
        """
        Step 7:Execute each Document Fex.
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", 'S10071_4', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", 'Category', 30)
        
        ia_run_obj.verify_table_data_set('#ITableData0', Test_Case_ID+'_DS01.xlsx', 'Step 07.1 : Verify Activr Report displays')
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 07.2 : Verify report page summary')
        
        select_css = "#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']"
        self.driver.find_element_by_css_selector(select_css).click()
        utillobj.synchronize_with_visble_text("#ITableData1 #TCOL_1_C_0 span", 'Category', 30)
        
        ia_run_obj.verify_table_data_set('#ITableData1', Test_Case_ID+'_DS02.xlsx', 'Step 07.3 : Verify Activr Report displays')
        miscobj.verify_page_summary(1, '10of10records,Page1of1', 'Step 07.3 : Verify report page summary')
        
        """
        Step 8:Tap the Global Filter icon to apply a filter to the dashboard.
        Expect to see the Global Filter menu panel appear.
        Verify that the buttons appear for: Operator:, Add Condition, Filter, Highlight and Clear functions.
        """
        select_css = "#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']"
        self.driver.find_element_by_css_selector(select_css).click()
        time.sleep(8)
        filter_elem=self.driver.find_element_by_css_selector("table[id='iLayTB$'] .arDashboardBarGlobalButton")
        utillobj.default_click(filter_elem)
#         utillobj.click_on_screen(filter_elem, "middle", click_type=0)
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 08.1: Verify Filter that the selection menu appears:")
        miscobj.move_active_popup('1', '350', '120')
        time.sleep(5)
       
        """
        Step 9:Tap the Add Condition button, then select Category as the Filter field.
        From the value drop down, select Food.
        Expect to see the following Filter selection screen.
        """
        filterselectionobj.add_global_condition_field('Category', parent_menu_css='0_globalop_x__0')
        filterselectionobj.create_filter(1,'Equals',value1='Food')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        """
        Step 10:Click the Filter button to apply the Global Filter to the Document.
        Expect to see the following Reports.
        """
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", 'Category', 30)
        
        ia_run_obj.verify_table_data_set('#ITableData0', Test_Case_ID+'_DS03.xlsx', 'Step 10.1 : Verify Activr Report displays')
        miscobj.verify_page_summary(0, '3of10records,Page1of1', 'Step 10.2 : Verify report page summary')
        
        """
        Step 11:Click on Clear All button.
        Expect to see the Filters removed from the Filter menu and the report on Page 1 back to 3 Category/Product.
        """
        filterselectionobj.filter_button_click('Clear All')
        utillobj.verify_object_visible("#FiltTable1 .arFilterItem", False, "Step 11:Filter menu removed from the filter dialog")
         
        """
        Step 12:Click on the Global Filter x button to close the filter menu.
        Expect to see the menu removed and the same report original report.
        """
        filterselectionobj.close_filter_dialog()
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", 'Category', 30)
        ia_run_obj.verify_table_data_set('#ITableData0', Test_Case_ID+'_DS01.xlsx', 'Step 12.1 : Verify Activr Report displays')
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 12.2 : Verify report page summary')

if __name__ == "__main__":
    unittest.main()