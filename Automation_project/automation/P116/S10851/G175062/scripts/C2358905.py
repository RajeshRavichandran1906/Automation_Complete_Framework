'''
Created on Feb 14, 2018

@author: BM13368
Testcase_Name : 
Testcase_ID :
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous, ia_run, active_filter_selection, wf_legacymainpage
from common.lib import utillity

class C2358905_TestClass(BaseTestCase):

    def test_C2358905(self):
        
        """ TESTCASE VARIABLES """
        Test_Case_ID = "C2358905"
        document_fex='Globalfilter'
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
            Step 1:Create a new Document for the GGSALES file.
            From the insert menu icon, add a text box to the canvas.
            Change the text content to "Global Filter for mixed Components(Report & Chart)".
        """    
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10851_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 75)
        vis_ribbon.select_ribbon_item('Insert', 'text_box')
        utillobj.synchronize_with_number_of_element("#theCanvas #Text_1", 1, 15)
          
        vis_ribbon.resizing_document_component('0.25', '4.60')
        ia_resultobj.enter_text_in_Textbox('Text_1', "Global Filter for mixed Components(Report & Chart)")
          
        """    Expect to see the following Text Box on the canvas.    """
        ia_resultobj.verify_text_in_Textbox('#Text_1', 'Global Filter for mixed Components(Report & Chart)', "Step 01:01: Verify textbox value")
             
        """ 
            Step 2:From the insert menu icon, add a Report to the canvas, Page 1.
            Position the Report under the Text Box.
            Select Category and Product ID fields.
            Expect to see the Category, Product ID Report added beneath the Text Box.
        """    
        vis_ribbon.select_ribbon_item('Insert', 'report')
        time.sleep(5)
        ia_resultobj.drag_drop_document_component('#Text_1', '#TableChart_1', 0, 85, target_drop_point='bottom_middle')
        vis_metadata.datatree_field_click('Category', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(4)"
        utillobj.synchronize_with_visble_text(element_css, 'Category', 25)
          
        vis_metadata.datatree_field_click('Product ID', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(5)"
        utillobj.synchronize_with_visble_text(element_css, 'Product ID', 25)
          
        coln_list = ['Category', 'Product ID']
        vis_resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 02:01: Verify Category, Product, Unit Sales report.")   
           
        """   
            Step 3:Click the PAGE icon in the upper left to add Page 2 to the canvas.
        """    
        ia_resultobj.select_or_verify_document_page_menu("New Page")
        time.sleep(5)
           
        """    Expect to see Page 2 appear on the canvas, replacing Page 1    """
        page_elem=self.driver.find_element_by_css_selector("#iaPagesMenuBtn").text
        utillobj.asequal('Page 2', page_elem, "Step 03:01: Verify page2 is added in the canvas")    
              
        """   Step 4:From the insert menu icon, add a Vertical Bar Chart to the canvas, Page 2.    """
        vis_ribbon.select_ribbon_item('Insert', 'chart')
        utillobj.synchronize_with_number_of_element("#TableChart_2 svg g.chartPanel rect[class*='riser']", 25, 25)
              
        """    
            Step 5:Select Category, Product, Unit Sales and Dollar Sales fields.
            Move the Bar Chart slightly upwards to see the entire Preview image.
        """
        vis_metadata.datatree_field_click('Category', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(8)"
        utillobj.synchronize_with_visble_text(element_css, 'Category', 25)
          
        vis_metadata.datatree_field_click('Product', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(9)"
        utillobj.synchronize_with_visble_text(element_css, 'Product', 25)
          
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(7)"
        utillobj.synchronize_with_visble_text(element_css, 'UnitSales', 25)
          
        vis_metadata.datatree_field_click('Dollar Sales', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(8)"
        utillobj.synchronize_with_visble_text(element_css, 'DollarSales', 25)
          
        """    Expect to see the following Bar Chart template on the canvas.    """
        vis_resultobj.verify_xaxis_title("TableChart_2", 'Category : Product', "Step 05:01: Verify X-axis Title")
        vis_resultobj.verify_number_of_riser("TableChart_2", 1, 4, 'Step 05:02: Verify the total number of risers displayed on live-preview Chart')
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        vis_resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, 'Step 05:03: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar", "bar_blue", "Step 05:04: Verify first bar color")
          
        """    
            Step 6:Click the PAGE icon in the upper left to add Page 3 to the canvas.
            Insert a Chart into the canvas.
        """    
        ia_resultobj.select_or_verify_document_page_menu("New Page", default_page_name='Page 2')
        time.sleep(5)
        page_elem=self.driver.find_element_by_css_selector("#iaPagesMenuBtn").text
        utillobj.asequal('Page 3', page_elem, "Step 06:01: Verify page3 is added in the canvas")
        vis_ribbon.select_ribbon_item('Insert', 'chart')
        utillobj.synchronize_with_number_of_element("#TableChart_3 svg g.chartPanel rect[class*='riser']", 25, 25)
          
        """    Expect to see Page 3 appear on the canvas, showing the default Bar Chart.    """
        vis_resultobj.verify_number_of_riser("TableChart_3", 1, 25, 'Step 06:02: Verify the total number of risers displayed on live-preview Chart')   
          
        """    
            Step 7:Make sure that the Bar Chart is selected, as indicated by the lines around the image.
            Change the Bar Chart to a PIE by clicking the Format option, selecting Chart Types, then PIE and add Category, Unite Sales and Dollar Sales fields.
        """    
        vis_ribbon.select_ribbon_item("Format", "Pie")
        utillobj.synchronize_with_number_of_element("#TableChart_3 svg g.chartPanel text[class^='pieLabel']", 5, 35)
        vis_metadata.datatree_field_click('Category', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(8)"
        utillobj.synchronize_with_visble_text(element_css, 'Category', 25)
          
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(7)"
        utillobj.synchronize_with_visble_text(element_css, 'UnitSales', 25)
          
        vis_metadata.datatree_field_click('Dollar Sales', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(8)"
        utillobj.synchronize_with_visble_text(element_css, 'DollarSales', 25)
              
        """    Expect to see the Chart preview on Page 3 as a PIEs.    """
        vis_resultobj.verify_pie_label_in_single_group(['Unit Sales','Dollar Sales'], "#TableChart_3", "svg g.chartPanel text[class^='pieLabel']", "Step 07:01:Verify pie labels")
        vis_resultobj.verify_number_of_pie_segment("#TableChart_3", 1, 2, "Step 07:02:Verify number of pie chart")
        vis_resultobj.verify_legends(['Category', 'Coffee'], "#TableChart_3", msg="Step 07:03:Verify pie chart legends")
          
        """    Step 8:Save the document as Globalfilter.fex and close dashboard    """
        vis_ribbon.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(document_fex)
        utillobj.infoassist_api_logout()
#         utillobj.synchronize_with_visble_text("#SignonbtnLogin", "Sign in", 60)
        time.sleep(4)    
              
        """    
            Step 9:Open saved Globalfilter.Fex using the Text Editor.
            Change the Keyword/value pair SHOW_GLOBALFILTER=OFF to SHOW_GLOBALFILTER=ON.
            Save and execute.
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        legacy_obj.select_repository_folder_item_menu('P116->S10851_2', document_fex, 'Edit With...->Text Editor')
        parent_css='[id="menu_button_search"]'
        utillobj.synchronize_with_number_of_element(parent_css, 1, 60)
          
        search_obj=self.driver.find_element_by_css_selector("#bipEditor #menu_bar [id='menu_button_search']")
        utillobj.default_click(search_obj)
        time.sleep(0.50)
        utillobj.select_or_verify_bipop_menu('Find')
        element=self.driver.find_element_by_css_selector("#findText")
        utillobj.default_click(element)
        time.sleep(0.50)
          
#         pyautogui.typewrite(text_string, interval=0.2, pause=5)
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
        
        """    Expect to see the following Dashboard with Text Box and Report on Page 1.    """
        utillobj.active_run_fex_api_login(document_fex+".fex", 'S10851_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("[id^='LOBJText'] table > tbody > tr", 1, 75)
        expected_value = ['Global Filter for mixed Components(Report & Chart)']
        ia_run_obj.verify_document_objects("[id^='LOBJText']", 'textbox', 'Step 09:00: Verify "Global Filter for Document containing Reports" enterd in textbox.', expected_value_list=expected_value)
        ia_run_obj.create_table_data_set("#ITableData0", Test_Case_ID+'_DS01.xlsx')
        ia_run_obj.verify_table_data_set('#ITableData0', Test_Case_ID+'_DS01.xlsx', 'Step 09:01: Verify Active Report data which is displayed in Page1')
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 09:02: Verify report page summary')
            
        """   
            Step 10:Select Page 2, then Page 3.
            Expect to see the Bar Chart on Page 2.
        """ 
        ia_run_obj.select_active_document_page_layout_menu('Page 2')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']",20,45)
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Category : Product', "Step 10:02: Verify X-axis Title")
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 20, 'Step 10:03: Verify the total number of risers displayed on live-preview Chart')
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        expected_xval_list=['Coffee : Ca...', 'Coffee : Es...', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croi...', 'Food : Scone']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, 'Step 10:04: X and Y axis labels')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "bar_blue", "Step 10:05: Verify first bar color")
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 10:06: Verify Chart toolbar")
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 10:07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 10:08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        miscobj.verify_chart_title("MAINTABLE_wbody1_ft","Unit Sales, Dollar Sales BY Category, Product", "Step 10:09: Verify chart title ")
        vis_resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Unit Sales','Dollar Sales'], "Step 10:10: Verifychart legend")
        
        """  Expect to see the PIE Charts on Page 3. """
        ia_run_obj.select_active_document_page_layout_menu('Page 3')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody2_f svg g [class='pieLabel!g1!mpieLabel!']", "Dollar Sales", 25)
        
        miscobj.verify_chart_title("MAINTABLE_wbody2_ft","Unit Sales, Dollar Sales BY Category", "Step 10:11: Verify chart title ")
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g0!mwedge!", "bar_blue", "Step 10:12: Verify first bar color")  
        vis_resultobj.verify_pie_label_in_single_group(['Unit Sales', 'Dollar Sales'], "#MAINTABLE_wbody2", "svg g.chartPanel text[class^='pieLabel']", "Step 10:13: Verify pie labels")
        vis_resultobj.verify_number_of_pie_segments("MAINTABLE_wbody2", 1, 6, "Step 10:14:Verify number of pie chart")
        vis_resultobj.verify_legends(['Category','Coffee', 'Food','Gifts'], "#MAINTABLE_wbody2", msg="Step 10:15:Verify pie chart legends")
        miscobj.verify_chart_title("MAINTABLE_wbody2_ft","Unit Sales, Dollar Sales BY Category", "Step 10:16: Verify chart title ")
            
        """    
            Step 11:Switch back to Page 1 and click the Filter icon and move the filter window to right side which report not overlapped.
            Expect to see the following Filter menu appear with Page 1.
        """
        ia_run_obj.select_active_document_page_layout_menu('Page 1')
        utillobj.synchronize_with_number_of_element("[id^='LOBJText'] table > tbody > tr", 1, 20)
        
        filter_elem=self.driver.find_element_by_css_selector("table[id='iLayTB$'] .arDashboardBarGlobalButton")
        utillobj.default_click(filter_elem)
        utillobj.synchronize_with_number_of_element("#wall1 #wtop1", 1, 15)
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 11:01: Verify Filter that the selection menu appears:")
        miscobj.move_active_popup('1', '550', '100')
        time.sleep(5)
            
        """ 
            Step 12:Click the Add Condition, select the Category field, the select Coffee & Gifts from the drop down list.
            Expect to see the following Filter menu.
        """    
        filterselectionobj.add_global_condition_field('Category', parent_menu_css='0_globalop_x__0')
        filterselectionobj.create_filter(1,'Equals',value1='Coffee', value2='Gifts')
        time.sleep(3)
        expected_menu_list=['Coffee', 'Gifts']
        filterselectionobj.verify_value_selection(1, expected_menu_list, "Step 12:01: Verify global filter values")
          
        """ 
            Step 13:Click the Filter button.
            Expect to see the Report on Page 1 display only Coffee & Gifts.
        """    
        filterselectionobj.filter_button_click('Filter')
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", 'Category', 20)
        ia_run_obj.verify_table_data_set('#ITableData0', Test_Case_ID+'_DS02.xlsx', 'Step 13:01: Verify Activr Report displays')
        miscobj.verify_page_summary(0, '7of10records,Page1of1', 'Step 13:02: Verify report page summary')
            
        """ 
            Step 14:Select Page 2, then Page 3.
            Expect to see only Coffee and Gifts on the Bar Chart.
            Expect to see only Coffee and Gifts in the slices on both PIEs.
        """    

        ia_run_obj.select_active_document_page_layout_menu('Page 2')
        
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']",14, 45)
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Category : Product', "Step 14:01: Verify X-axis Title")
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 14, 'Step 14:02: Verify the total number of risers displayed on live-preview Chart')
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M']
        expected_xval_list=['Coffee : Ca...', 'Coffee : Es...', 'Coffee : Latte', 'Gifts : Coff...']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, 'Step 14:03: X and Y axis labels')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar", "bar_blue", "Step 14:04: Verify first bar color")
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 14:06: Verify Chart toolbar")
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 14:07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 14:08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        miscobj.verify_chart_title("MAINTABLE_wbody1_ft","Unit Sales, Dollar Sales BY Category, Product", "Step 14:09: Verify chart title ")
        vis_resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Unit Sales','Dollar Sales'], "Step 14:10: Verifychart legend") 
        
        """   
            Step 15:Click the 'x' on the Filter menu to close.
            switch back to the Report on Page 1.
            Expect to see the Filter menu disappear and Page 1 display all three Categories and their Products again.
        """
        ia_run_obj.select_active_document_page_layout_menu('Page 3')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody2_ft tbody", 1, 25)
        
        miscobj.verify_chart_title("MAINTABLE_wbody2_ft","Unit Sales, Dollar Sales BY Category", "Step 15:01: Verify chart title ")
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g0!mwedge!", "bar_blue", "Step 15:02: Verify first bar color")  
        vis_resultobj.verify_pie_label_in_single_group(['Unit Sales','Dollar Sales'], "#MAINTABLE_wbody2", "svg g.chartPanel text[class^='pieLabel']", "Step 15:03: Verify pie labels")
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 0, "Step 15:04: Verify number of pie chart")
        vis_resultobj.verify_legends(['Category','Coffee', 'Gifts'], "#MAINTABLE_wbody2", msg="Step 15:05: Verify pie chart legends")
        miscobj.verify_chart_title("MAINTABLE_wbody2_ft","Unit Sales, Dollar Sales BY Category", "Step 15:06: Verify chart title ")

        filterselectionobj.close_filter_dialog("wall1")
        time.sleep(4)
        utillobj.verify_object_visible("#wall1 #FiltTable1", False, "Step 15:08: Filter menu removed from the filter dialog")


if __name__ == "__main__":
    unittest.main()