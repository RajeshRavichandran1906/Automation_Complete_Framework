'''
Created on Jan 24, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10851
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2358897
TestCase Name = Create a document using report and chart using multi-page Document
'''

import unittest,time,pyautogui
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, ia_miscelaneous, active_miscelaneous, visualization_resultarea, ia_run

class C2358897_TestClass(BaseTestCase):

    def test_C2358897(self):
        
        """
        TESTCASE VARIABLES
        """
        test_case_id = 'C2358897'
        
        """
        TESTCASE OBJECTS
        """
        driver = self.driver
        miscelaneousobject = ia_miscelaneous.IA_Miscelaneous(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        active_mis_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_runobj=ia_run.IA_Run(driver)

        """ 
        Step 01: Create a new document and select 'GGSales' as master file, 
        """
        miscelaneousobject.invoke_ia_tool_using_api_('document', 'ibisamp/ggsales', 'mrid', 'mrpass', 'P116/S10851_1')
#         utillobj.infoassist_api_login('document', 'ibisamp/ggsales', 'S10851_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 190)
        vis_ribbon.switch_ia_tab('Home')
        
        """ 
        Step 02: Add text box from insert menu change the text content to "Create a Multi-page Dashboard Page one" .
        """
        vis_ribbon.select_ribbon_item("Insert", "Text_Box")
        utillobj.synchronize_with_number_of_element("#Text_1", 1, 25)
        vis_ribbon.switch_ia_tab('Layout')
        height = self.driver.find_element_by_css_selector("input[id*='Height']")
        height.clear()
        height.send_keys('0.5')
        pyautogui.press('enter')
        time.sleep(5)
        width = self.driver.find_element_by_css_selector("input[id*='Width']")
        width.clear()
        width.send_keys('3.5')
        pyautogui.press('enter')
#         vis_ribbon.resizing_document_component('0.5', '3.5')
        time.sleep(3)
        ia_resultobj.enter_text_in_Textbox('Text_1', "Create a Multi-page Dashboard Page one")
        
        """ 
        Step 03: Select Category, Product,Unit Sales to get a report
        """
        time.sleep(3)
        vis_metadata.datatree_field_click('Category', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(4)"
        utillobj.synchronize_with_visble_text(element_css, 'Category', 25)
            
        vis_metadata.datatree_field_click('Product', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(5)"
        utillobj.synchronize_with_visble_text(element_css, 'Product', 25)
        
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(3)"
        utillobj.synchronize_with_visble_text(element_css, 'UnitSales', 25)
        
        ia_resultobj.drag_drop_document_component('#TableChart_1', '#Text_1', 0, 40,  target_drop_point='bottom_middle')
        time.sleep(5)
        
        """ 
        Step 04: Select 'Insert > Chart' then add 'PRODUCT to Xaxis', and 'UNITSALES to Measure(Sum)
        """
        vis_ribbon.select_ribbon_item("Insert", "Chart")
        utillobj.synchronize_with_number_of_element("#TableChart_2", 1, 25)
        
        vis_metadata.datatree_field_click('Product', 2, 0)
        parent_css="#TableChart_2 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 2, 25)
         
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        parent_css="#TableChart_2 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 25)
        
        ia_resultobj.drag_drop_document_component('#TableChart_2', '#TableChart_1', 300, 0)
        time.sleep(5)
        
        """ 
        Verify that Page 1 added with text box,report and chart and able to execute with out any error
        """
        ia_resultobj.verify_text_in_Textbox('#Text_1', 'Create a Multi-page Dashboard Page one', "Step 04.01: Verify text in textbox")
        
        coln_list = ["Category", "Product", "Unit Sales"]
        vis_resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1 ", coln_list, "Step 04.02: Verify report1 titles")
        
        xaxis_value="Product"
        vis_resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 04.03: Verify X-Axis Title")
        yaxis_value="Unit Sales"
        vis_resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 04.04: Verify y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        vis_resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step 04.05: Verify XY labels")
        vis_resultobj.verify_number_of_riser("TableChart_2", 1, 2, 'Step 04.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar", "bar_blue", "Step 04.07: Verify first bar color")
        time.sleep(5)
        
        """ 
        Step 05: To add another page select Insert tab, in the Pages group Page 2, is inserted after the current page, and appears on the canvas
        """
        vis_ribbon.select_ribbon_item("Insert", "Page")
        parent_css="#iaPagesMenuBtn div[class='bi-button-label']"
        vis_resultobj.wait_for_property(parent_css, 1, 25, string_value='Page 2')
        exp_page_text = 'Page 2'
        elem_css = driver.find_element_by_css_selector("#iaPagesMenuBtn div[class='bi-button-label']")
        act_page_text = elem_css.text.strip()
        utillobj.asequal(act_page_text, exp_page_text,  "Step 05.00: Verify Page 2 appears on the canvas")
        
        """ 
        Step 06: Add text box from insert menu change the text content to "Create a Multi-page Document Page Two"
        """
        vis_ribbon.select_ribbon_item("Insert", "Text_Box")
        utillobj.synchronize_with_number_of_element("#Text_2", 1, 25)
        vis_ribbon.resizing_document_component('0.5', '3.5')
        time.sleep(3)
        ia_resultobj.enter_text_in_Textbox('Text_2', "Create a Multi-page Document Page Two")
        
        """ 
        Step 07: Repeat steps 3 and 4 until your document is complete with 2nd page.
        """
        vis_metadata.datatree_field_click('Category', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(4)"
        utillobj.synchronize_with_visble_text(element_css, 'Category', 25)
            
        vis_metadata.datatree_field_click('Product', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(5)"
        utillobj.synchronize_with_visble_text(element_css, 'Product', 25)
        
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(3)"
        utillobj.synchronize_with_visble_text(element_css, 'UnitSales', 25)
        
        ia_resultobj.drag_drop_document_component('#TableChart_3', '#Text_2', 0, 40,  target_drop_point='bottom_middle')
        time.sleep(5)
        
        vis_ribbon.select_ribbon_item("Insert", "Chart")
        utillobj.synchronize_with_number_of_element("#TableChart_4", 1, 25)
        
        vis_metadata.datatree_field_click('Product', 2, 0)
        parent_css="#TableChart_4 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 2, 25)
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        parent_css="#TableChart_4 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 25)
        ia_resultobj.drag_drop_document_component('#TableChart_4', '#TableChart_3', 300, 0)
        time.sleep(5)
        
        ia_resultobj.verify_text_in_Textbox('#Text_2', 'Create a Multi-page Document Page Two', "Step 07.01: Verify text in textbox")
        
        coln_list = ["Category", "Product", "Unit Sales"]
        vis_resultobj.verify_report_titles_on_preview(3, 3, "TableChart_3", coln_list, "Step 07.02: Verify report1 titles")
        
        xaxis_value="Product"
        vis_resultobj.verify_xaxis_title("TableChart_4", xaxis_value, "Step 07.03: Verify X-Axis Title")
        yaxis_value="Unit Sales"
        vis_resultobj.verify_yaxis_title("TableChart_4", yaxis_value, "Step 07.04: Verify y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        vis_resultobj.verify_riser_chart_XY_labels("TableChart_4", expected_xval_list, expected_yval_list, "Step 07.05: Verify XY labels")
        vis_resultobj.verify_number_of_riser("TableChart_4", 1, 2, 'Step 07.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_4", "riser!s0!g0!mbar", "bar_blue", "Step 07.07: Verify first bar color")
        
        """ 
        Step 08: To navigate between pages, open the Page menu by clicking the Page icon at the top of the canvas
        """
        ia_resultobj.select_or_verify_document_page_menu('Page 1', default_page_name='Page 2', verify='true',expected_popup_list=['Page 1', 'Page 2', 'New Page', 'Page Options...'], msg='Step 08.00: Verify popup menu')
        
        """ 
        Step 09: Save and run the report
        """
        time.sleep(5)
        vis_ribbon.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(test_case_id)
        time.sleep(3)
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=3)
        
        """ 
        Verify that Mulit-Page document output should have the following options Layout tab,Page1 and Page2 option and able to navigate the output from Page 1 to Page 2 with out any error.
        """
        
        ia_runobj.select_active_document_page_layout_menu('Page 1')
        
        active_mis_obj.verify_page_summary(0, '10of10records,Page1of1', "Step 09.01: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds01.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds01.xlsx', " Step 09.02: Verify report at run time.", desired_no_of_rows=10)
        
        expected_text = ['Create a Multi-page Dashboard Page one']
        msg="Step 09.03: Verify text in textbox"
        ia_runobj.verify_added_text_in_textbox(expected_text, msg=msg)
        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, 25)
        xaxis_value="Product"
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 09.03 Verify X-Axis Title")
        yaxis_value="Unit Sales"
        vis_resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 09.04 Verify y-Axis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09.05: Verify XY labels")
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 10, 'Step 09.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 09.07: Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody1","Unit Sales by Product", "Step 09.08 : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 09.09: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 09.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 09.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        ia_runobj.select_active_document_page_layout_menu('Page 2')
        
        active_mis_obj.verify_page_summary(2, '10of10records,Page1of1', "Step 09.12: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData2', 'I2r', test_case_id + '_Ds02.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData2', 'I2r', test_case_id + '_Ds02.xlsx', " Step 09.13: Verify report at run time.", desired_no_of_rows=10)
        
        expected_text = ['Create a Multi-page Document Page Two']
        msg="Step 09.14: Verify text in textbox"
        ia_runobj.verify_added_text_in_textbox(expected_text, msg=msg)
        
        parent_css="#MAINTABLE_wbody3 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, 25)
        
        xaxis_value="Product"
        yaxis_value="Unit Sales"
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody3", xaxis_value, "Step 09.15: Verify X-Axis Title")
        vis_resultobj.verify_yaxis_title("MAINTABLE_wbody3", yaxis_value, "Step 09.16: Verify y-Axis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody3", expected_xval_list, expected_yval_list, "Step 09.17: Verify XY labels")
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody3", 1, 10, 'Step 09.18: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody3", "riser!s0!g0!mbar", "bar_blue", "Step 09.19: Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody3","Unit Sales by Product", "Step 09.20: Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu3', ['More Options','Advanced Chart','Original Chart'],"Step 09.21: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu3', ['Aggregation'],"Step 09.22: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu3', ['Sum'],"Step 09.23: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        

if __name__ == '__main__':
    unittest.main()