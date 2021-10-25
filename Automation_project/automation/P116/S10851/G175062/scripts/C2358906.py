'''
Created on May 28, 2018

@author: BM13368
TestCase_Name : Add Global filter to Document for a report and a chart (MERGE=ADVANCED).
TestCase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2358906
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous, ia_run, active_filter_selection, wf_legacymainpage
from common.lib import utillity

class C2358906_TestClass(BaseTestCase):

    def test_C2358906(self):
        
        """ TESTCASE VARIABLES """
        Test_Case_ID = "C2358906"
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_run_obj=ia_run.IA_Run(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        legacy_obj=wf_legacymainpage.Wf_Legacymainpage(self.driver)
        
        """
            Step 01:Create a new Document canvas for the GGSALES file.
            Switch the Format to Active Report.
            From the insert menu icon, add a Text Box and insert the text 
            "Global Filter for Document containing Report & Chart".
        """    
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10851_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 75)
        vis_ribbon.select_ribbon_item('Insert', 'text_box')
        utillobj.synchronize_with_number_of_element("#theCanvas #Text_1", 1, 15)
           
        vis_ribbon.resizing_document_component('0.25', '4.60')
        ia_resultobj.enter_text_in_Textbox('Text_1', "Global Filter for Document containing Report & Chart")
           
        """    Expect to see the following Text Box on the canvas.    """
        ia_resultobj.verify_text_in_Textbox('#Text_1', 'Global Filter for Document containing Report & Chart', "Step 01:01: Verify textbox value")
         
        """
            Step 02:From the insert menu icon, add a Report to the canvas below the Text Box.
            Select fields Category, Product, Unit Sales & Dollar Sales.
        """
        vis_ribbon.select_ribbon_item('Insert', 'report')
        time.sleep(5)
        ia_resultobj.drag_drop_document_component('#Text_1', '#TableChart_1', 0, 85, target_drop_point='bottom_middle')
         
        vis_metadata.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, expire_time=10)  
          
        vis_metadata.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 5, expire_time=10)
            
        vis_metadata.datatree_field_click("Unit Sales", 2, 1)
        parent_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 20,1)
         
        vis_metadata.datatree_field_click("Dollar Sales", 2, 1)
        parent_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 20,1)
         
        coln_list = ['Category', 'Product','Unit Sales', 'Dollar Sales']
        vis_resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 02:01: Verify Category, Product, Unit Sales report.")
         
        ia_resultobj.create_report_data_set('TableChart_1 ', 2, 4, Test_Case_ID+'_Ds01.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 4, Test_Case_ID+'_Ds01.xlsx', 'Step 02:02 Verify Preview report dataset')
         
         
        """
            Step 03:Step 03:Click the Page icon in the upper left to create Page 2.
            Insert a Chart.
            Expect to see the following Chart preview panel on Page 2.
        """
        ia_resultobj.select_or_verify_document_page_menu("New Page")
        time.sleep(5)
        vis_ribbon.select_ribbon_item("Insert", "Chart")
        element_css="#TableChart_2 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 25, 60)
         
        """
            Step 04:Add fields Category, Product, Budget Units & Budget Dollars to the preview.
        """
         
        vis_metadata.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 [class='xaxisOrdinal-title']", "Category", 15)
         
        vis_metadata.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 [class='xaxisOrdinal-title']", "Category : Product", 15)
            
        vis_metadata.datatree_field_click("Budget Units", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 [class='yaxis-title']", "Budget Units", 15)
         
        vis_metadata.datatree_field_click("Budget Dollars", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 [class='legend-labels!s1!']", "Budget Dollars", 15)
         
        """
        Step 05: Save the document
        """
        vis_ribbon.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        utillobj.infoassist_api_logout()
        time.sleep(5)
         
        """
        Step 06 :Open the saved Document Fex using the Text Editor.
        Change the Keyword/value pair SHOW_GLOBALFILTER=OFF to SHOW_GLOBALFILTER=ON.
        Save and execute.
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        legacy_obj.select_repository_folder_item_menu('P116->S10851_2', Test_Case_ID, 'Edit With...->Text Editor')
        parent_css='[id="menu_button_search"]'
        utillobj.synchronize_with_number_of_element(parent_css, 1, 60)
         
        search_obj=self.driver.find_element_by_css_selector("#bipEditor #menu_bar [id='menu_button_search']")
        utillobj.default_click(search_obj)
        time.sleep(0.50)
        utillobj.select_or_verify_bipop_menu('Find')
        element=self.driver.find_element_by_css_selector("#findText")
        utillobj.default_click(element)
        time.sleep(0.50)
         
        exec("element.clear()")
        exec("element.send_keys('SHOW_GLOBALFILTER=OFF')")
        find_btn_elem=self.driver.find_element_by_css_selector("#btnFind")
        utillobj.default_click(find_btn_elem)
        time.sleep(0.50)
        element=self.driver.find_element_by_css_selector("#replaceText")
        utillobj.default_click(element)
        time.sleep(0.50)
        exec("element.clear()")
        exec("element.send_keys('SHOW_GLOBALFILTER=ON')")
           
        elem=self.driver.find_element_by_css_selector("#btnReplaceAll")
        utillobj.default_click(elem)
        time.sleep(2)
           
        legacy_obj.click_text_editor_ribbon_button('Save')
        file_elem=self.driver.find_element_by_css_selector("#menu_button_file")
        utillobj.default_click(file_elem)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Close')
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
            Execute the fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", 'S10851_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("[id^='LOBJText'] table > tbody > tr", 1, 75)
        expected_value = ['Global Filter for Document containing Report & Chart']
        ia_run_obj.verify_document_objects("[id^='LOBJText']", 'textbox', 'Step 06:00: Verify "Global Filter for Document containing Reports" enterd in textbox.', expected_value_list=expected_value)
        ia_run_obj.create_table_data_set("#ITableData0", Test_Case_ID+'_DS02.xlsx')
        ia_run_obj.verify_table_data_set('#ITableData0', Test_Case_ID+'_DS02.xlsx', 'Step 06:01: Verify Active Report data which is displayed in Page1')
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 06:02: Verify report page summary')
        
        """
            Step 7:Click the Global Filter icon, select Add Condition, select Category, then from the dropdown pick 'Gifts'.
        """
        filter_elem=self.driver.find_element_by_css_selector("table[id='iLayTB$'] .arDashboardBarGlobalButton")
        utillobj.default_click(filter_elem)
        utillobj.synchronize_with_number_of_element("#wall1 #wtop1", 1, 15)
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 07:01: Verify Filter that the selection menu appears:")
        miscobj.move_active_popup('1', '600', '140')
        time.sleep(5)
        
        filterselectionobj.add_global_condition_field('Category', parent_menu_css='0_globalop_x__0')
        filterselectionobj.create_filter(1,'Equals',value1='Gifts')
        time.sleep(3)
        expected_menu_list=['Gifts']
        filterselectionobj.verify_value_selection(1, expected_menu_list, "Step 07:02: Verify global filter values")
        
        """
            Step 08 :Click the Filter button.
        """
        filterselectionobj.filter_button_click('Filter')
        
        """
            Expect to see the following Filtered Report on Page 1 contain only Gifts.
        """
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", 'Category', 20)
        ia_run_obj.create_table_data_set('#ITableData0', Test_Case_ID+'_DS03.xlsx')
        ia_run_obj.verify_table_data_set('#ITableData0', Test_Case_ID+'_DS03.xlsx', 'Step 08:01: Verify Activr Report displays')
        miscobj.verify_page_summary(0, '4of10records,Page1of1', 'Step 08:02: Verify report page summary')
        
        """
            Step 09 :Switch to Page 2.
        """
        
        ia_run_obj.select_active_document_page_layout_menu('Page 2')
        time.sleep(5)
        
        """
            Expect to see the following Filtered Chart on Page 2 contain only Gifts.
        """
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']",8, 45)
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Category : Product', "Step 09:01: Verify X-axis Title")
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 8, 'Step 09:02: Verify the total number of risers displayed on live-preview Chart')
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M']
        expected_xval_list=['Gifts : Coff...', 'Gifts : Coff...', 'Gifts : Mug', 'Gifts : The...']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, 'Step 09:03: X and Y axis labels')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar", "bar_blue", "Step 09:04: Verify first bar color")
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 09:05: Verify Chart toolbar")
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 09:06: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 09:07: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        miscobj.verify_chart_title("MAINTABLE_wbody1_ft","Budget Units, Budget Dollars BY Category, Product", "Step 09:08: Verify chart title ")
        vis_resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Budget Units','Budget Dollars'], "Step 09:09: Verifychart legend")
        
        """
            Step 10 :Switch back to Page 1.
            Click the Add Condition, select Product, change the operator to Not Equal, then from the drop-down select Thermos.
            Click the Filter button.
        """
        ia_run_obj.select_active_document_page_layout_menu('Page 1')
        t_css="div[id^='LOBJText_'] span left span"
        text1=self.driver.find_element_by_css_selector(t_css).text.strip()
        print (text1)
        utillobj.asequal(text1,"Global Filter for Document containing Report & Chart", 'Step 10.01: Verify text in page 1')
        filterselectionobj.add_global_condition_field('Product', parent_menu_css='0_globalop_0')
        filterselectionobj.create_filter(2,'Not equal',value1='Thermos')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        
        """
            Expect to see the Report on Page 1 with Thermos eliminated from the Category Gifts.
        """
        
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", 'Category', 20)
        ia_run_obj.create_table_data_set('#ITableData0', Test_Case_ID+'_DS04.xlsx')
        ia_run_obj.verify_table_data_set('#ITableData0', Test_Case_ID+'_DS04.xlsx', 'Step 10:01: Verify Activr Report displays')
        miscobj.verify_page_summary(0, '3of10records,Page1of1', 'Step 10:02: Verify report page summary')
        
        """
            Click on Clear All button and click on the Global Filter x button to close the Global Filter menu.
        """
        
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(3)
        
        """
            Expect to see Global Filter menu removed from the Chart on Page 2.
        """
        
        ia_run_obj.verify_table_data_set('#ITableData0', Test_Case_ID+'_DS02.xlsx', 'Step 06:01: Verify Active Report data which is displayed in Page1')
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 06:02: Verify report page summary')
        
        """
            Expect to see Global Filter menu removed from the Chart on Page 1.
        """
        ia_run_obj.select_active_document_page_layout_menu('Page 2')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']",20, 45)
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Category : Product', "Step 10:01: Verify X-axis Title")
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 20, 'Step 10:02: Verify the total number of risers displayed on live-preview Chart')
        expected_yval_list=['0', '3M', '6M', '9M', '12M']
        expected_xval_list=['Coffee : Ca...', 'Coffee : Es...', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croi...']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, 'Step 10:03: X and Y axis labels')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar", "bar_blue", "Step 10:04: Verify first bar color")
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 10:05: Verify Chart toolbar")
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 10:06: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 10:07: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        miscobj.verify_chart_title("MAINTABLE_wbody1_ft","Budget Units, Budget Dollars BY Category, Product", "Step 10:08: Verify chart title ")
        vis_resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Budget Units','Budget Dollars'], "Step 10:09: Verifychart legend")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()