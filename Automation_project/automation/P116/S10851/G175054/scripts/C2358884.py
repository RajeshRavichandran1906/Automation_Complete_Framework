'''
Created on Jan 24, 2018
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2358884
@author: Praveen Ramkumar
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_resultarea,visualization_metadata,visualization_ribbon,ia_resultarea
from common.lib import utillity

class C2358884_TestClass(BaseTestCase):

    def test_C2358884(self):
        """ TESTCASE VARIABLES """
        test_case_id ="C2358884"
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        active_mis_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
                      
        """
            Step 01:Launch IA to develop a new Document.
            Select 'GGSales' as master file, and change output format as Active report.
            Click Category, Product and Unit Sales fields to create a report
        """
        utillobj.infoassist_api_login('document','ibisamp/ggsales', 'S10851_1','mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 65)
        vis_ribbon.switch_ia_tab('Home')
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 1: Verify output format as Active report.")
                 
        vis_metadata.datatree_field_click('Category', 2, 0)
        element_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(element_css, 2, 60)
          
        vis_metadata.datatree_field_click('Product', 2, 0)
        utillobj.synchronize_with_number_of_element(element_css, 5, 60)
         
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        utillobj.synchronize_with_number_of_element(element_css, 8, 60)
         
        """
            Step 02:Select 'Insert > Chart' and drag the chart next to report.
        """
        vis_ribbon.select_ribbon_item('Insert', 'Chart')
        utillobj.synchronize_with_visble_text("[class*='legend-labels!s0!']", 'Series0', 60)
         
         
        """
            Step 03:Now double click Product from Dimensions and Unit Sales from Measures
        """
        vis_metadata.datatree_field_click('Product', 2, 0)
        chart2_xtitle_css="#TableChart_2 [class*='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(chart2_xtitle_css, 'Product', 60)
         
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        chart2_ytitle_css="#TableChart_2 [class*='yaxis-title']"
        utillobj.synchronize_with_visble_text(chart2_ytitle_css, 'UnitSales', 60)
        vis_ribbon.repositioning_document_component('5.5', '2.5')
        utillobj.synchronize_with_number_of_element("#pfjTableChart_2  [class*='riser!s0']",2,60)
         
        """
            Step 04:Select Text box from the Insert menu. Place it above report and chart in the dashboard.
        """
        vis_ribbon.select_ribbon_item('Insert', 'Text_Box')
        utillobj.synchronize_with_number_of_element("[id^='Text']",1,45)
        vis_ribbon.repositioning_document_component('5.25', '0.75')
        
        """
            Step 05:Highlight Enter Test here text inside the Text box. Replace content as "Sample text for the test case"Adjust text box size as per the content.
            Step 06:Right click on the text box and select delete option.
            Step 07:Verify that text box component deleted on Document canvas.
        """
        utillobj.synchronize_with_number_of_element("[id^='Text']",1,45)
        vis_ribbon.resizing_document_component('0.25', '2.5')
        time.sleep(1)
        utillobj.synchronize_with_number_of_element("#Text_1",1,45)
        ia_resultobj.enter_text_in_Textbox('Text_1', "Sample text for the test case")
        ia_resultobj.verify_text_in_Textbox('#Text_1', 'Sample text for the test case', "Step 05: Verify Textbox text")
        vis_resultobj.choose_right_click_menu_item_for_prompt('#Text_1', 'Delete')
        
        """
            Step 08:Run Document and verify that deleted text component is no more visible in the output..
            Step 09:Close active dashboard in run time.Right click on the report and select delete option.
            Step 10:Verify that report is deleted on Document canvas.
        """ 
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css,1,45)
        utillobj.switch_to_frame(pause=2)  
        table_data_css="#ITableData0"    
        utillobj.synchronize_with_number_of_element(table_data_css,1,45)  
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds01.xlsx', " Step 09: Verify dataset.")
        utillobj.switch_to_default_content(pause=1)
        vis_resultobj.select_panel_caption_btn(0, select_type='close', custom_css="[class*='window-caption']")
        
        vis_resultobj.choose_right_click_menu_item_for_prompt('#TableChart_1', 'Delete')
        
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval1_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        vis_resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval1_list, "Step 10.1: Verify XY labels",x_axis_label_length=2)
        vis_resultobj.verify_xaxis_title("TableChart_2", "Product", "Step 10.2a: Verify X-Axis Title") 
        vis_resultobj.verify_yaxis_title("TableChart_2", "Unit Sales", "Step 10.2b: Verify y-Axis Title")
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar!", "bar_blue1", "Step 10.3: Verify  riser color")
        vis_resultobj.verify_number_of_riser("TableChart_2", 1, 2, 'Step 10.4: Verify the total number of risers displayed on preview')
        
        """
        Step 11:Run Document and verify that deleted report is no more visible in the output.
        """
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element(frame_css,1,45)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0",1,45)       
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 11.1a: Verify X-Axis Title") 
        vis_resultobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 11.1b: Verify y-Axis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grin...', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 11.2: Verify XY labels",x_axis_label_length=2)
        active_mis_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Product', 'Step 11.4: Verify Chart Title')
        active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.5: Verify Chart toolbar")
        active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        vis_resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 11.8: Verify the total number of risers displayed on preview')
        expected_tooltip_list=['Product:Croissant', 'Unit Sales:630054', 'Filter Chart', 'Exclude from Chart']
        vis_resultobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!", expected_tooltip_list, "Step 11.9: Verify bar value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "bar_blue1", "Step 11.10: Verify  riser color")
        
        
if __name__ == "__main__":
    unittest.main() 