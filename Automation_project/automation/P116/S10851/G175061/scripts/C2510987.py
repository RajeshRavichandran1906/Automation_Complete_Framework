'''
Created on Feb 06, 2018

@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10851
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251712
TestCase Name = Create a chart using multi-page Document
'''

import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, visualization_resultarea, active_miscelaneous, ia_run
from common.lib.basetestcase import BaseTestCase

class C2510987_TestClass(BaseTestCase):

    def test_C2510987(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2510987'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        
        """
        Step 01: Create a new document and select 'GGSales' as master file, and change output format as Active report/APDF
        Add text box from insert menu and change the text content to "Create a Chart Multi-page Document Page 1"
        """
                
        utillobj.infoassist_api_login('document', 'ibisamp/ggsales', 'S10851_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 65)
        
        vis_ribbon.switch_ia_tab('Home')
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 01: Verify output format as Active report.")
        
        vis_ribbon.select_ribbon_item("Insert", "Text_Box")
        time.sleep(2)
        vis_ribbon.resizing_document_component('0.5', '3.5')
        time.sleep(1)
        utillobj.synchronize_with_number_of_element("#Text_1", 1, 25) 
        ia_resultobj.enter_text_in_Textbox('Text_1', "Create a Chart Multi-page Document Page 1")
        
        """
           Step 02:Select 'Insert >Chart then add 'Category to Xaxis', and 'UNITSALES to Measure(Sum)
        """
        vis_ribbon.select_ribbon_item("Insert", "chart")
        element_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 25, 60)
        
        vis_ribbon.repositioning_document_component('2.00', '2.00')
        time.sleep(3)
        vis_metadata.datatree_field_click('Category', 2, 0)
        parent_css="#TableChart_1 [class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'Category', 20)
        
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        parent_css="#TableChart_1 [class='yaxis-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'UnitSales', 20)
        
        """
           Step 03:Select Check box from 'Insert' tab,right click on check box and assign "Category" in property of Check box from chart1
        """
        
        vis_ribbon.select_ribbon_item("Insert", "checkbox")
        utillobj.synchronize_with_number_of_element("#Prompt_1", 1, 20)
        
        vis_ribbon.repositioning_document_component('8.00', '2.00')
        time.sleep(3)
        vis_resultobj.choose_right_click_menu_item_for_prompt("#Prompt_1",'Properties')
        
        source={'select_field':'Category'}
        vis_resultobj.customize_active_dashboard_properties(source=source, msg="Step 03:01:", btn_type='ok')
        time.sleep(3)       
        
        """
           Step 04:To add another page select Insert tab, in the Pages group Page 2, is inserted after the current page, and appears on the canvas
        """
        
        vis_ribbon.select_ribbon_item("Insert", "Page")
        parent_css="#iaPagesMenuBtn div[class='bi-button-label']"
        utillobj.synchronize_with_visble_text(parent_css, 'Page 2', 25)
        
        exp_page_text = 'Page 2'
        elem_css = driver.find_element_by_css_selector("#iaPagesMenuBtn div[class='bi-button-label']")
        act_page_text = elem_css.text.strip()
        print(act_page_text)
        utillobj.asequal(act_page_text, exp_page_text,  "Step 04: Verify Page 2 appears on the canvas")
        
        """
           Step 05:Add text box from insert menu change the text content to "Create a Chart Multi-page Document Page 2"
        """
        
        vis_ribbon.select_ribbon_item("Insert", "Text_Box")
        utillobj.synchronize_with_number_of_element("#Text_2", 1, 25)
        
        vis_ribbon.resizing_document_component('0.5', '3.5')
        time.sleep(1)
        utillobj.synchronize_with_number_of_element("#Text_2", 1, 25) 
        ia_resultobj.enter_text_in_Textbox('Text_2', "Create a Chart Multi-page Document Page 2")
        
        """
           Step 06:Select 'Insert >Chart then add 'Product to Xaxis', and 'BUDGET DOLLARS to Measure(Sum)
        """
        
        vis_ribbon.select_ribbon_item("Insert", "chart")
        element_css="#TableChart_2 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 25, 60)
        
        vis_ribbon.repositioning_document_component('2.00', '2.00')
        time.sleep(2)
        vis_metadata.datatree_field_click('Product', 2, 0)
        parent_css="#TableChart_2 [class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'Product', 20)
        
        vis_metadata.datatree_field_click('Budget Dollars', 2, 0)
        parent_css="#TableChart_2 [class='yaxis-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'BudgetDollars', 25)
        
        """
           Step 07:Select Radio button from 'Insert' tab,right click on Radio button and assign "Product" in property of Radio button from chart2
            Step 08:Check "Include All" option, and select 'OK'. Run the report
        """
        
        vis_ribbon.select_ribbon_item("Insert", "radio_button")
        utillobj.synchronize_with_number_of_element("#Prompt_2", 1, 25)
        
        vis_ribbon.repositioning_document_component('8.00', '2.00')
        time.sleep(2)
        vis_resultobj.choose_right_click_menu_item_for_prompt("#Prompt_2",'Properties')
        
        source={'select_report':'Chart2','select_field':'Product','verify_includeall':True}
        vis_resultobj.customize_active_dashboard_properties(source=source, msg="Step 07:01:", btn_type='ok')
        
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 25)
        utillobj.switch_to_frame(pause=2)
        
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0 [class='xaxisOrdinal-title']", "Category", 35)
        
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales BY Category", "Step 08.1 : Verify chart title ")
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval1_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 08.2: Verify XY labels",x_axis_label_length=2)
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 3, 'Step 08.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g1!mbar!", "bar_blue", "Step 08.4: Verify  riser color")
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody0","Category","Step 08.5: Verify Xaxis title")
        vis_resultobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 08.6: Verify yaxis title")
        
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.8: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        ia_runobj.select_active_document_page_layout_menu('Page 2')           
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody1_ft","Budget Dollars BY Product", "Step 08.10: Verify chart title ")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grin...', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval1_list=['0', '3M', '6M', '9M', '12M']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval1_list, "Step 08.11: Verify XY labels",x_axis_label_length=2)
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 10, 'Step 08.12: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g6!mbar!", "bar_blue", "Step 08.13: Verify  riser color")
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody1","Product","Step 08.14: Verify Xaxis title")
        vis_resultobj.verify_yaxis_title("MAINTABLE_wbody1", "Budget Dollars", "Step 08.15: Verify yaxis title")
        
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 08.17: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 08.18: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 08.19: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
            Step 09:Save and close the report 
           Step 10:From IA run the saved fex
            Verify that chart with Mulit-Page document output should have the following options Layout tab,Page1 and Page2 option and able to navigate the output from Page 1 to Page 2 with out any error.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        vis_ribbon.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        utillobj.synchronize_with_number_of_element("#SignonbtnLogin", 1, 35)
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", 'S10851_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0 [class='xaxisOrdinal-title']", "Category", 65)
        
        ia_runobj.select_active_document_page_layout_menu('Page 1') 
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales BY Category", "Step 09.1 : Verify chart title ")
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval1_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 09.2: Verify XY labels",x_axis_label_length=2)
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 3, 'Step 09.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g1!mbar!", "bar_blue", "Step 09.4: Verify  riser color")
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody0","Category","Step 09.5: Verify Xaxis title")
        vis_resultobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 09.6: Verify yaxis title")
        
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.8: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)

        ia_runobj.select_active_document_page_layout_menu('Page 2')            
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody1_ft","Budget Dollars BY Product", "Step 09.1a: Verify chart title ")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grin...', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval1_list=['0', '3M', '6M', '9M', '12M']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval1_list, "Step 09.2a: Verify XY labels",x_axis_label_length=2)
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 10, 'Step 09.3a: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g6!mbar!", "bar_blue", "Step 09.4a: Verify  riser color")
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody1","Product","Step 09.5a: Verify Xaxis title")
        vis_resultobj.verify_yaxis_title("MAINTABLE_wbody1", "Budget Dollars", "Step 09.6a: Verify yaxis title")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 09.8a: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 09.9a: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 09.10a: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        
if __name__ == "__main__":
    unittest.main()
        
