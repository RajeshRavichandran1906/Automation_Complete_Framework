'''
Created on Jan 29, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10851
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2358896
TestCase Name = Create a chart using multi-page Document
'''

import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, visualization_resultarea, active_miscelaneous, ia_run
from common.lib.basetestcase import BaseTestCase

class C2358896_TestClass(BaseTestCase):

    def test_C2358896(self):
        """
        TESTCASE VARIABLES
        """
        test_case_id = 'C2358896'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_runobj = ia_run.IA_Run(self.driver)

        """
        Step 01: Create a new Document and select 'GGSales' as master file, and make sure format of the report is Active report.
        """
        utillobj.infoassist_api_login('document', 'ibisamp/ggsales', 'S10851_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 75)
        vis_ribbon.switch_ia_tab('Home')
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 01: Verify output format as Active report.")
        
        """ 
        Add text box from insert menu and change the text content to "Create a Chart Multi-page Dashboard Page 1" .
        """
        vis_ribbon.select_ribbon_item("Insert", "Text_Box")
        utillobj.synchronize_with_number_of_element("#Text_1",1, 25)
        vis_ribbon.resizing_document_component('0.5', '3.5')
        time.sleep(3)
        ia_resultobj.enter_text_in_Textbox('Text_1', "Create a Chart Multi-page Dashboard Page 1")
        
        """ 
        Step 02: Select 'Insert > chart then add 'Category to Xaxis', and 'UNITSALES to Measure(Sum) 
        """
        vis_ribbon.select_ribbon_item("Insert", "Chart")
        utillobj.synchronize_with_number_of_element("#TableChart_1", 1, 35)
        
        vis_metadata.datatree_field_click('Category', 2, 0)
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 25)
         
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        parent_css="#TableChart_1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 25)
        
        ia_resultobj.drag_drop_document_component('#TableChart_1', '#Text_1', 0, 40,  target_drop_point='bottom_middle')
        time.sleep(5)
        
        """ 
        Expect to see the following chart with text box control
        """
        ia_resultobj.verify_text_in_Textbox('#Text_1', 'Create a Chart Multi-page Dashboard Page 1', "Step 2.1: Verify text in textbox")
        
        xaxis_value="Category"
        vis_resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 2.2:a(i) Verify X-Axis Title")
        yaxis_value="Unit Sales"
        vis_resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 2.2:a(ii) Verify y-Axis Title")
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        vis_resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 2.2:a(iii):Verify XY labels")
        vis_resultobj.verify_number_of_riser("TableChart_1", 1, 1, 'Step 2.2.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 2.2.c: Verify first bar color")
        time.sleep(5)
        
        """ 
        Step 03: Select Check box from 'Insert' tab,right click on check box and assign "Category" in property of Check box from chart1
        """
        vis_ribbon.select_ribbon_item("Insert", "Checkbox")
        utillobj.synchronize_with_number_of_element("#Prompt_1", 1, 25)
        
        ia_resultobj.drag_drop_document_component('#Prompt_1', '#TableChart_1', 85, 0)
        time.sleep(5) 
        vis_resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
         
        """ 
        Step 04: Check "Include All" option, and select 'OK'
        """
        ComboBox_1_source = {'select_report':'Chart1', 'select_field':'Category', 'verify_condition':'Equal to', 'verify_includeall':True}
        vis_resultobj.customize_active_dashboard_properties(source=ComboBox_1_source, msg="Step 04.", btn_type='ok')
#         utillobj.infoassist_api_edit(test_case_id, 'document', 'S10071_1', mrid='mrid', mrpass='mrpass') 
        time.sleep(10)  
        
        """ 
        Step 05: To add another page select Insert tab, in the Pages group Page 2, is inserted after the current page, and appears on the canvas
        """
        vis_ribbon.select_ribbon_item("Insert", "Page")
        
        parent_css="#iaPagesMenuBtn div[class='bi-button-label']"
        utillobj.synchronize_with_visble_text(parent_css, 'Page 2', 25)
        
        exp_page_text = 'Page 2'
        elem_css = driver.find_element_by_css_selector("#iaPagesMenuBtn div[class='bi-button-label']")
        act_page_text = elem_css.text.strip()
        utillobj.asequal(act_page_text, exp_page_text,  "Step 05: Verify Page 2 appears on the canvas")
        
        """ 
        Step 06: Add text box from insert menu change the text content to "Create a Chart Multi-page Dashboard Page 2"
        """
        vis_ribbon.select_ribbon_item("Insert", "Text_Box")
        utillobj.synchronize_with_number_of_element("#Text_2", 1, 20)
        vis_ribbon.resizing_document_component('0.5', '3.5')
        time.sleep(3)
        ia_resultobj.enter_text_in_Textbox('Text_2', "Create a Chart Multi-page Dashboard Page 2")
        
        """ 
        Step 07: Insert chart and add 'Product to Xaxis', and 'BUDGET DOLLARS to Measure(Sum) 
        """
        vis_ribbon.select_ribbon_item("Insert", "Chart")
        utillobj.synchronize_with_number_of_element("#TableChart_2", 1, 35)
        
        vis_metadata.datatree_field_click('Product', 2, 0)
        parent_css="#TableChart_2 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 2, 25)
         
        vis_metadata.datatree_field_click('Budget Dollars', 2, 0)
        parent_css="#TableChart_2 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 9, 25)
        
        ia_resultobj.drag_drop_document_component('#TableChart_2', '#Text_2', 0, 40,  target_drop_point='bottom_middle')
        time.sleep(5)
        
        """ 
        Step 08: Select Radio button from 'Insert' tab,right click on Radio button and assign "Product" in property of Radio button from chart2
        """
        vis_ribbon.select_ribbon_item("Insert", "Radio_Button")
        element_css='#Prompt_2'
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        ia_resultobj.drag_drop_document_component(element_css, '#TableChart_2', 85, 0)
        time.sleep(5) 
        vis_resultobj.choose_right_click_menu_item_for_prompt('#Prompt_2', 'Properties')
         
        """ 
        Step 09: Check "Include All" option, and select 'OK'
        """
        ComboBox_1_source = {'select_report':'Chart2', 'select_field':'Product', 'verify_condition':'Equal to', 'verify_includeall':True}
        prompts_select = {'select_prompts':'radiobutton_2'}
        vis_resultobj.customize_active_dashboard_properties(prompts=prompts_select, source=ComboBox_1_source, msg="Step 09.", btn_type='ok')
#         utillobj.infoassist_api_edit(test_case_id, 'document', 'S10071_1', mrid='mrid', mrpass='mrpass') 
        time.sleep(10) 
         
        ia_resultobj.verify_text_in_Textbox('#Text_2', 'Create a Chart Multi-page Dashboard Page 2', "Step 09.1: Verify text in textbox")
        
        xaxis_value="Product"
        vis_resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 9.2:a(i) Verify X-Axis Title")
        yaxis_value="Budget Dollars"
        vis_resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 9.2:a(ii) Verify y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        vis_resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step 9.2:a(iii):Verify XY labels")
        vis_resultobj.verify_number_of_riser("TableChart_2", 1, 2, 'Step 9.2.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar", "bar_blue", "Step 9.2.c: Verify first bar color")
        
        """ 
        Step 10: Save and run the report
        """
        
        vis_ribbon.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(test_case_id)
        time.sleep(3)
        
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 50)
        
        utillobj.switch_to_frame(pause=3)
        elem_css="form[name='mergeform'] table[id^='iLayTB'] [id^='iLay']"
        utillobj.synchronize_with_number_of_element(elem_css, 3, 25)
        
        """ 
        Verify that Page 1 report based on the check box selected value and Page 2 report radio button based on the selected values.
        """
        ia_runobj.select_active_document_page_layout_menu('Page 1')
        expected_text = ['Create a Chart Multi-page Dashboard Page 1']
        msg="Step 10.1: Verify text in textbox in page 1"
        ia_runobj.verify_added_text_in_textbox(expected_text, msg=msg)
        
        check=['[All]', 'Coffee', 'Food', 'Gifts']
        check_defau='[All]'
        ia_runobj.verify_active_dashboard_prompts("check_box", "#PROMPT_1_cs", check, "Step 10.2: Verify check box IS SHOWING", default_selected_check=check_defau)
        
        parent_css="#MAINTABLE_wbody0 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 5, 25)
        
        xaxis_value="Category"
        yaxis_value="Unit Sales"
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 10.3:a(i) Verify X-Axis Title")
        vis_resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 10.3:a(ii) Verify y-Axis Title")
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 10.3:a(iii):Verify XY labels")
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 3, 'Step 10.3.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar", "bar_blue", "Step 10.3.c: Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0","Unit Sales BY Category", "Step 10.3.e : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.3.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.3.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.3.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        ia_runobj.select_active_document_page_layout_menu('Page 2')
        expected_text = ['Create a Chart Multi-page Dashboard Page 2']
        msg="Step 10.1: Verify text in textbox in page2"
        ia_runobj.verify_added_text_in_textbox(expected_text, msg=msg)
        
        check=['[All]', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        check_defau='[All]'
        ia_runobj.verify_active_dashboard_prompts("radio_button", "#PROMPT_2_cs", check, "Step 10ii.2: Verify radio_button IS SHOWING", default_selected_check=check_defau)
        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 5, 25)
        
        xaxis_value="Product"
        yaxis_value="Budget Dollars"
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10ii:a(i) Verify X-Axis Title")
        vis_resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step10ii:a(ii) Verify y-Axis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '3M', '6M', '9M', '12M']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step10ii:a(iii):Verify XY labels")
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 10, 'Step10ii.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10ii.c: Verify first bar color")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody1","Budget Dollars BY Product", "Step 10ii.e : Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 10ii.f: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step10ii.g: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step10ii.h: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        

if __name__ == '__main__':
    unittest.main()