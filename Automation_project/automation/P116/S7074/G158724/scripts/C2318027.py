'''
Created on Nov 22, 2017

@author: Pavithra
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon,ia_ribbon,ia_resultarea
from common.lib import utillity

class C2318027_TestClass(BaseTestCase):

    def test_C2318027(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID="C2318027"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj=ia_ribbon.IA_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step 01 :Right click on folder created in IA and create a new Chart using the GGSALES file.
            From Home tab Select Active Report as Output file format.Screenshot:
        """
        utillobj.infoassist_api_login('Chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        element_css="#TableChart_1 g.chartPanel g text"
        utillobj.synchronize_with_number_of_element(element_css, 11, 20)
        
        ribbonobj.change_output_format_type('active_report')
        element_css="#HomeTab #HomeFormatType [class='bi-button-label']"
        utillobj.synchronize_with_visble_text(element_css, 'ActiveReport', 20)
        
        """
        Step 02 :Add fields Product, Unit Sales.Screenshot:
        """
        metadataobj.datatree_field_click("Product", 2, 0)
        element_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 2, 20)
        
        metadataobj.datatree_field_click("Unit Sales", 2, 0)
        element_css= "#TableChart_1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(element_css, 8, 20)
               
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 02.1 :Verify xy label')
        result_obj.verify_number_of_riser('TableChart_1', 1, 2, 'Step 02.2 : Verify number of preview risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 02.3 : Verify preview bar color")
        result_obj.verify_xaxis_title('TableChart_1','Product','Step 02.4 : Verify X-Axis title')
        result_obj.verify_yaxis_title('TableChart_1','Unit Sales','Step 02.5 : Verify X-Axis title')
        metadataobj.verify_query_pane_field('Horizontal Axis','Product',1,"Step 02.6: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','Unit Sales',1,"Step 02.7: Verify query pane")
         
        """
        Step 03 :Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        result_obj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)

        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales BY Product", "Step 05.1 : Verify chart title ")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.2a: Verify XY labels")
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","Product","Step 05.3 : Verify Xaxis title")
        result_obj.verify_yaxis_title('MAINTABLE_wbody0','Unit Sales','Step 02.5 : Verify X-Axis title')
        result_obj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 05.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 05.4a: Verify  riser color")
#         expected_tooltip_list=['Product:Biscotti', 'Unit Sales:421377', 'Filter Chart', 'Exclude from Chart']
#         result_obj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 05.6a: Verify bar value")       
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
          
        """
        Step 04 :Select Format > Other.From Select a chart pop up choose XY Polar Diagram.
        Click OK.Expect to see the Clustered bar chart converted into the Preview pane for XY Polar Diagram.
        """
        utillobj.switch_to_default_content(pause=3)
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('x_y_plots', 'x_y_plots_polar', 2, ok_btn_click=True)
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 16)
        expected_xval_list=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 04.1 :Verify xy label')
        result_obj.verify_yaxis_title('TableChart_1','Unit Sales','Step 04.2: Verify X-Axis title')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1',1,'Step 05.2 : Verify no of parabox chart lines',custom_css="svg g circle[class*='series!s0!g0!mmarker!")#TableChart_1 svg g circle[class*='series!s0!g0!mmarker!']
        
        """
        Step 05:Click the Run button.Expect to see the following XY Polar Diagram.AHTML output:
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        result_obj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales BY Product", "Step 05.1 : Verify chart title ")
        expected_xval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        expected_yval1_list=['0', '0.2', '0.4', '0.6', '0.8', '1', '1.2']
        result_obj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.2a: Verify XY labels")
        result_obj.verify_yaxis_title('MAINTABLE_wbody0','Unit Sales','Step 5.3 : Verify X-Axis title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 5.4 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.5: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.6: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=2)        
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step 5', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()