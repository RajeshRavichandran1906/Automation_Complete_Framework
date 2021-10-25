'''
Created on Feb 14, 2018

@author: Robert/Updated by : Bhagavathi 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10851
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/C2510988
TestCase Name = Create a chart using report and chart using multi-page Document
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, ia_resultarea, visualization_ribbon, active_miscelaneous, ia_run
from common.lib import utillity

class C2510988_TestClass(BaseTestCase):

    def test_C2510988(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2510988'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        
        """    1. Create a new Document and select 'GGSales' as master file, and change output format as Active report/APDF    """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10851_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", "Document", 75)
         
        """    1.1. Add text box from insert menu change the text content to "Create a Multi-page Dashboard Page one".    """
        ribbonobj.select_ribbon_item("Insert", "text_box")
        utillobj.synchronize_with_number_of_element("#Text_1", 1, 20, 1)
        ribbonobj.resizing_document_component('0.3', '5.65')
        ia_resultobj.enter_text_in_Textbox('Text_1', "Create a Multi-page Dashboard Page one")
        ia_resultobj.drag_drop_document_component('#Text_1', '#theCanvas',0,0, target_drop_point='top_middle')
        
        """    "2. Select Category, Product,Unit Sales to get a report    """
        """    "2.1. Expect to see the following report with text box    """
        ribbonobj.select_ribbon_item('Insert', 'report')
        utillobj.synchronize_with_number_of_element('#TableChart_1', 1, 25)
        ia_resultobj.drag_drop_document_component('#TableChart_1', '#theCanvas', 185, -220, target_drop_point='left')
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, expire_time=15)  
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 5, expire_time=15)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        parent_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 20,1)
        coln_list = ['Category', 'Product','Unit Sales']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 02:01: Verify Category, Product, Unit Sales report.")
#         ia_resultobj.create_report_data_set('TableChart_1 ', 2, 3, Test_Case_ID+'_Ds01.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 3, Test_Case_ID+'_Ds01.xlsx', 'Step 02:02 Verify Preview report dataset')
         
        """    3. Select 'Insert > Chart' and then add 'PRODUCT to Xaxis', and 'UNITSALES to Measure(Sum)    """
        ribbonobj.select_ribbon_item("Insert", "Chart")
        element_css="#TableChart_2 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 25, 60)
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 [class='xaxisOrdinal-title']", "Product", 15)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 [class='yaxis-title']", "Unit Sales", 15)
        ia_resultobj.drag_drop_document_component('#TableChart_2', '#TableChart_1', 275, -115, target_drop_point='right')
         
        """    3.1. Expect to see the following report, chart and text box control in the live preview    """
        ia_resultobj.verify_text_in_Textbox('#Text_1', "Create a Multi-page Dashboard Page one", 'Step 3.1a. Verify Textbox message')
        coln_list=["Category", "Product", "Unit Sales"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 03:01: Verify column titles")
#         ia_resultobj.create_report_data_set('TableChart_1 ', 1, 3, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 01:02: Verify Preview report dataset')
        resultobj.verify_number_of_riser("TableChart_2", 1, 2, 'Step 3.1b: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        xaxis_value="Product"
        yaxis_value="Unit Sales"
        resultobj.verify_riser_chart_XY_labels('TableChart_2', expected_xval_list, expected_yval_list, 'Step 3.1c: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar!", "bar_blue1", "Step 3.1d: Verify bar color")
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 3.1e(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 3.2d(ii): Verify Y-Axis Title")
           
        """    4. to add another page select Insert tab, in the Pages group Page 2, is inserted after the current page, and appears on the canvas        """
        ia_resultobj.select_or_verify_document_page_menu('New Page')
         
        """    4.1. Expect to see the following page2 has added in the canvas with an empty page    """
        ia_resultobj.verify_current_document_page_name('Page 2', 'Step 4.1. Verify current document page is page 2')
         
        """    5. Add text box from insert menu change the text content to "Create a Multi-page Dashboard Page Two"    """
        ribbonobj.select_ribbon_item("Insert", "text_box")
        utillobj.synchronize_with_number_of_element("#Text_2", 1, 20)
        ribbonobj.resizing_document_component('0.3', '5.65')
        ia_resultobj.enter_text_in_Textbox('Text_2', "Create a Multi-page Dashboard Page Two")
        ia_resultobj.drag_drop_document_component('#Text_2', "#theCanvas",0, 0, target_drop_point='top_middle') 
         
        """    "6. Repeat steps 3 - 5 until your document is complete with 2nd page.    """
        ribbonobj.select_ribbon_item('Insert', 'report')
        utillobj.synchronize_with_number_of_element('#TableChart_3', 1, 25)
        ia_resultobj.drag_drop_document_component('#TableChart_3', '#theCanvas', 185, -220, target_drop_point='left')
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_3 div[class^='x']", 2, expire_time=15)  
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_3 div[class^='x']", 5, expire_time=15)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        parent_css="#TableChart_3 div[class^='x']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 20,1)
        coln_list = ['Category', 'Product','Unit Sales']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_3", coln_list, "Step 06:01: Verify Category, Product, Unit Sales report.")
#         ia_resultobj.create_report_data_set('TableChart_3 ', 2, 3, Test_Case_ID+'_Ds01.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_3', 2, 3, Test_Case_ID+'_Ds01.xlsx', 'Step 06:02 Verify Preview report dataset')
        
        """Insert chart """
        ribbonobj.select_ribbon_item('Insert', 'chart')
        element_css="#TableChart_4 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 25, 60)
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_4 [class='xaxisOrdinal-title']", "Category", 15)
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_4 [class='xaxisOrdinal-title']", "Category : Product", 15)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_4 [class='yaxis-title']", "Unit Sales", 15)
        ia_resultobj.drag_drop_document_component('#TableChart_4', '#TableChart_3', 275, -115, target_drop_point='right')   
        
        """    "6.1. Verify that Page 2 added with text box,report and chart and able to execute with out any error    """
        ia_resultobj.verify_text_in_Textbox('#Text_2', "Create a Multi-page Dashboard Page Two", 'Step 6.1a. Verify Textbox message')
        coln_list=["Category", "Product", "Unit Sales"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_3", coln_list, "Step 06:01:01: Verify column titles")
#         ia_resultobj.create_report_data_set('TableChart_3 ', 2, 3, Test_Case_ID+"_Ds02.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_3', 2, 3, Test_Case_ID+'_Ds02.xlsx', 'Step 06:01:02: Verify Preview report dataset')
        resultobj.verify_number_of_riser("TableChart_4", 1, 2, 'Step 6.1b: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['Coffee : Capuccino', 'Coffee : Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        xaxis_value="Category : Product"
        yaxis_value="Unit Sales"
        resultobj.verify_riser_chart_XY_labels('TableChart_4', expected_xval_list, expected_yval_list, 'Step 6.1c: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_4", "riser!s0!g0!mbar!", "bar_blue1", "Step 6.1d: Verify bar color")
#         resultobj.verify_xaxis_title("TableChart_4", xaxis_value, "Step 6.1e(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_4", yaxis_value, "Step 6.2d(ii): Verify Y-Axis Title")
         
        """    "7. To Navigate between pages, open the Page menu by clicking the Page icon at the top of the canvas    """
        page_elem=self.driver.find_element_by_css_selector("#iaPagesMenuBtn").text
        utillobj.asequal('Page 2', page_elem, "Step 07: Verify page2 is the deault page in the canvas")
        ia_resultobj.select_or_verify_document_page_menu('Page 1', default_page_name='Page 2',verify='true', expected_popup_list=['Page 1', 'Page 2', 'New Page', 'Page Options...'],msg='Step 07:01: Verify popup menu' )
         
        """    "7.1. Verify that in live preview report canvas able to navigate between page    """
        ia_resultobj.verify_text_in_Textbox('#Text_1', "Create a Multi-page Dashboard Page one", 'Step 7.1a. Verify Textbox message')
        utillobj.verify_object_visible("#TableChart_1", True, 'Step 7.1. Verify Report exists')
        utillobj.verify_object_visible("#TableChart_2", True, 'Step 7.1. Verify Chart exists')
         
        """    "8. Save and close the report(Note: Report should be save as AHTML as AR-AD-072a.fex,AFLEX as AR-AD-072b.fex and APDF as AR-AD-072c.fex)    """
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """    "8.1. Verify that Mulit-Page document output should have the following options Layout tab,Page1 and Page2 option and able to navigate the output from Page 1 to Page 2 with out any error.    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(css, 1, 45)
        utillobj.switch_to_frame(pause=1)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1", 1, 30)
        exp_list=['Layouts','Page 1','Page 2']
        ia_runobj.verify_active_document_page_layout_menu("table[id='iLayTB$']", exp_list, 'Step 8. Verify the Layout menu')
        print ("----------Verifying Page 1 contents----------")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", "Unit Sales", "Step 8:01: Verify -yAxis Title")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", "Product", "Step 8:02: Verify -xAxis Title")
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grin...', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 8:03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 10, 'Step 08:21: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "bar_blue", "Step 8:04: Verify  bar color")
        miscobj.verify_chart_title('MAINTABLE_wbody1_ft', 'Unit Sales by Product', 'Step 8:05: Verify Chart Title')
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step 8:06: Verify Chart toolbar")
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step 10:07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step 8:08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        '''Verifying the report'''
        miscobj.verify_page_summary(0, '10of10records,Page1of1', "Step 8:10: Verify the Run Report Heading")
        column_list=['Category', 'Product','Unit Sales']
        miscobj.verify_column_heading('ITableData0', column_list, "Step 8:11: Verify the Run Report column heading")
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID +'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID +'_Ds03.xlsx', "Step 8:12: Verify entire Data set in Run Report on Page 1") 
        
        '''verify the text'''
        expected_list=['Create a Multi-page Dashboard Page one']
        msg='Step 8. Verify text in page 1'
        ia_runobj.verify_added_text_in_textbox(expected_list, msg=msg)
        ia_runobj.select_active_document_page_layout_menu('Page 2')
        
        print ("----------Verifying Page 2 contents----------")
        utillobj.synchronize_with_number_of_element("#ITableData2", 1, 20)
        resultobj.verify_yaxis_title("MAINTABLE_wbody3", "Unit Sales", "Step 8:01: Verify -yAxis Title")
        resultobj.verify_xaxis_title("MAINTABLE_wbody3", "Category : Product", "Step 8:02: Verify -xAxis Title")
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        expected_xval_list=['Coffee : Ca...', 'Coffee : Es...', 'Coffee : Latte', 'Food : Biscotti']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody3", expected_xval_list, expected_yval_list, "Step 8:03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody3", 1, 10, 'Step 08:21: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody3", "riser!s0!g2!mbar!", "bar_blue", "Step 8:04: Verify  bar color")
        miscobj.verify_chart_title('MAINTABLE_wbody3_ft', 'Unit Sales by Category, Product', 'Step 8:05: Verify Chart Title')
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu3', ['More Options','Advanced Chart','Original Chart'],"Step 8:06: Verify Chart toolbar")
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu3', ['Aggregation'],"Step 8:07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscobj.verify_arChartToolbar('MAINTABLE_wmenu3', ['Sum'],"Step 8:08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        '''Verifying the report'''
        miscobj.verify_page_summary(2, '10of10records,Page1of1', "Step 8:10: Verify the Run Report Heading")
        column_list=['Category', 'Product','Unit Sales']
        miscobj.verify_column_heading('ITableData2', column_list, "Step 8:11: Verify the Run Report column heading")
#         utillobj.create_data_set('ITableData2','I2r', Test_Case_ID +'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData2','I2r',Test_Case_ID +'_Ds04.xlsx', "Step 8:12: Verify entire Data set in Run Report on Page 1") 
        
        '''verify the text'''
        expected_list=['Create a Multi-page Dashboard Page Two']
        msg='Step 8. Verify text in page 2'
        ia_runobj.verify_added_text_in_textbox(expected_list, msg=msg)
        
if __name__ == '__main__':
    unittest.main()