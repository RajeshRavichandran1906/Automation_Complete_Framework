'''
Created on Jan 16, 2018

@author: Robert

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251623
TestCase Name = Verify that active prompt and report are not appearing on the dashboard once removed
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib import utillity


class C2251623_TestClass(BaseTestCase):

    def test_C2251623(self):
        """ TESTCASE VARIABLES """
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        
        """    1. Launch IA to develop a Document.    """
        """    1.1. Select 'GGSales' as master file, and change output format as Active report    """
        
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10071', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 85)
        
        """    1.2. Select Category, Product,Unit Sales to get a report    """
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, 25)
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 5, 25)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 8, 25)
        
        
        """    1.2a Verify the following "Report" in Canvas    """
        coln_list=["Category", "Product", "Unit Sales"]
        
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 1.2a: Verify column titles")
        
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 3, 'C2251622_Ds01.xlsx', 'Step 1.2b: Verify Preview report dataset')
        
        """    2. Select 'Insert > Chart' and drag the chart next to report.    """
        
        ribbonobj.select_ribbon_item("Insert", "chart")
        utillobj.synchronize_with_visble_text("[class*='legend-labels!s0!']", 'Series0', 50)
        
        """    3. Now double click Product from Dimensions and Unit Sales from Measures    """
        
        metaobj.datatree_field_click("Product", 2, 1)
        chart2_xtitle_css="#TableChart_2 [class*='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(chart2_xtitle_css, 'Product', 30)
        
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        chart2_ytitle_css="#TableChart_2 [class*='yaxis-title']"
        utillobj.synchronize_with_visble_text(chart2_ytitle_css, 'UnitSales', 30)
        
        ia_resultobj.drag_drop_document_component('#TableChart_2', '#TableChart_1', 275, 0)
        
        """    4. Select Text box from the Insert menu. Place it above report and chart in the dashboard.    """
         
        ribbonobj.select_ribbon_item("Insert", "text_box")
        utillobj.synchronize_with_number_of_element("#Text_1", 1, 35) 
        ribbonobj.resizing_document_component('0.5', '5')
        ia_resultobj.drag_drop_document_component('#Text_1', '#TableChart_2', 75, -55, target_drop_point='top_middle')
         
        """    5. Highlight Enter Test here text inside the Text box. Replace content as "Sample text for the test case"    """
         
        ia_resultobj.enter_text_in_Textbox('Text_1', "Sample text for the test case")
        combo_box=driver.find_element_by_id("TableChart_1")
        utillobj.click_on_screen(combo_box, coordinate_type='start', click_type=0)
        time.sleep(4)
        '''    5.1. Adjust text box size as per the content.    '''
        '''     Verifying the contents after adding a textbox'''
         
        ia_resultobj.verify_text_in_Textbox('#Text_1', "Sample text for the test case", 'Step 5.1 Verify the text')
         
        expected_xlabel_list=['Capuccino', 'Espresso']
        expected_ylabel_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resultobj.verify_riser_chart_XY_labels('TableChart_2', expected_xlabel_list, expected_ylabel_list,'Step 5.2 : ')
        resultobj.verify_xaxis_title('TableChart_2','Product','Step 5.3 : Verify X-Axis title')
        resultobj.verify_yaxis_title('TableChart_2','Unit Sales','Step 5.4 : Verify Y-Axis title')
        resultobj.verify_number_of_riser('TableChart_2',1,2,'Step 5.5 : Verify number of chart risers')
         
        '''    6. Right click on the text box and select delete option.    '''
        
        resultobj.choose_right_click_menu_item_for_prompt('#Text_1','Delete')
         
        '''    '7. Verify that text box component deleted on Document canvas.    '''
         
        utillobj.verify_object_visible("#Text_1", False, 'Step 7.1 Verify Textbox is deleted')
        utillobj.verify_object_visible("#TableChart_1", True, 'Step 7.2 Verify Report is still there')
        utillobj.verify_object_visible("#TableChart_2", True, 'Step 7.3 Verify Chart is still there')
         
        
        '''    '8. Run Document and verify that deleted text component is no more visible in the output.    '''
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 60)
        utillobj.switch_to_frame(pause=3)
        utillobj.verify_object_visible("td[id^='LOBJText_']", False, 'Step 8.1 Verify Textbox is not visible in runtime')
        utillobj.verify_object_visible("#ITableData0", True, 'Step 8.2 Verify Report is still there')
        utillobj.verify_object_visible("#MAINTABLE_wbody1", True, 'Step 8.3 Verify Chart is still there')
         
        utillobj.switch_to_default_content(pause=3)
        
         
        '''    '9. Close active dashboard in run time.    '''
        '''    '9.1. Right click on the report and select delete option.    '''
        resultobj.select_panel_caption_btn(0, select_type='close', custom_css="[class*='active'] [class*='caption'][class*='window']")
        time.sleep(5)
        resultobj.choose_right_click_menu_item_for_prompt('#TableChart_1','Delete')

        
        '''    10. Verify that report is deleted on Document canvas.    '''
        utillobj.verify_object_visible("#Text_1", False, 'Step 10.1 Verify Textbox is not visible')
        utillobj.verify_object_visible("#TableChart_1", False, 'Step 10.2 Verify Report is deleted')
        utillobj.verify_object_visible("#TableChart_2", True, 'Step 10.3 Verify Chart is still there')
         
        '''    11. Run Document and verify that deleted report is no more visible in the output.    '''
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 60)
        utillobj.switch_to_frame(pause=3)
        utillobj.synchronize_with_number_of_element("#ITableData0 #TCOL_0_C_0 span", 1, 45)
        utillobj.verify_object_visible("td[id^='LOBJText_']", False, 'Step 11.1 Verify Textbox is not visible in runtime')
        utillobj.verify_object_visible("#ITableData0", False, 'Step 11.2 Verify Report is not visible')
        utillobj.verify_object_visible("#MAINTABLE_wbody0_f", True, 'Step 11.3 Verify Chart is still there')
#         
        expected_xlabel_list=['Biscotti', 'Capuccino', 'Coffee Grin...', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_ylabel_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0_f', expected_xlabel_list, expected_ylabel_list,'Step 11.4 : ')
        resultobj.verify_xaxis_title('MAINTABLE_wbody0_f','Product','Step 11.5 : Verify X-Axis title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody0_f','Unit Sales','Step 11.6 : Verify Y-Axis title')
        resultobj.verify_number_of_riser('MAINTABLE_wbody0_f',1,10,'Step 11.7 : Verify number of chart risers')
        
        
        utillobj.switch_to_default_content(pause=3)
        
        
if __name__ == '__main__':
    unittest.main()