'''
Created on July 13, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2318028
TestCase Name =Verify Bubble Chart in others tab under Format menu.

'''
import unittest
# from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon,ia_ribbon
from common.lib import utillity

class C2318028_TestClass(BaseTestCase):

    def test_C2318028(self):
       
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID="C2318028"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
            
        """
        Step 01 : Right click on folder created in IA and create a new Chart using the GGSALES file. From Home tab Select Active Report as Output file format.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        element_css="#TableChart_1 g.chartPanel g text"
        utillobj.synchronize_with_number_of_element(element_css, 11, 20)
        
        ribbonobj.change_output_format_type('active_report')
        element_css="#HomeTab #HomeFormatType [class='bi-button-label']"
        utillobj.synchronize_with_visble_text(element_css, 'ActiveReport', 20)
        
        """
        Step 02 : Add fields Product, Unit Sales, Dollar Sales.
        """
        metadataobj.datatree_field_click('Product', 2, 1)
        element_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'Product', 20)
        
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        element_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(element_css, 'UnitSales', 20)
        
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)
        element_css="#TableChart_1 .legend text"
        utillobj.synchronize_with_number_of_element(element_css, 2, 20)
        
        """
        Verify Preview panel
        """
        result_obj.verify_xaxis_title("TableChart_1",'Product', "Step 02.1 : Verify X-Axis Title")
        expected_xval_list=['Capuccino','Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M','3.5M','4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 02.2 :')
        result_obj.verify_riser_legends('TableChart_1',['Unit Sales','Dollar Sales'], 'Step 02.3 : Verify chart legends label')
        result_obj.verify_number_of_riser('TableChart_1', 1, 4, 'Step 02.4 : Verify number of risers')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 02.5 : Verify bar color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mbar!', 'bar_green', 'Step 02.6 : Verify bar color')
        
        """
        Step 03 : Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        element_css="#MAINTABLE_wbody0_f g.chartPanel g text"
        utillobj.synchronize_with_number_of_element(element_css, 18, 20)
        
        """
        Expect to see the following Bar Chart.
        """
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Product', 'Step 03.1 : Verify Chart Title')
        result_obj.verify_xaxis_title('MAINTABLE_wbody0','Product', "Step 03.2 : Verify X-Axis Title")
        expected_xval_list=['Biscotti','Capuccino','Coffee Grinder','Coffee Pot','Croissant','Espresso','Latte','Mug','Scone','Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03.3 :')
        result_obj.verify_riser_legends('MAINTABLE_wbody0',['Unit Sales','Dollar Sales'], 'Step 03.4 : Verify chart legends label')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step 03.5 : Verify number of risers')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', 'lochmara', 'Step 03.6 : Verify bar color')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s1!g0!mbar!', 'pale_green', 'Step 03.7 : Verify bar color')
#         expected_tooltip1=['Product:  Biscotti', 'Unit Sales:  421377', 'Filter Chart', 'Exclude from Chart']
#         expected_tooltip2=['Product:  Biscotti', 'Dollar Sales:  5263317', 'Filter Chart', 'Exclude from Chart']
#         miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s0!g0!mbar!',expected_tooltip1,'Step 03.8 : Verify chart tooltip value')
#         miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s1!g0!mbar!',expected_tooltip2,'Step 03.9 : Verify chart tooptip value')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.10 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.11 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.12 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        utillobj.switch_to_default_content(pause=1)
        
        """
        Step 04 : Select Format > Other.From Select a chart pop up choose Bubble Chart.Click OK.
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('x_y_plots', 'x_y_plots_bubble', 3, ok_btn_click=True)
        element_css="#TableChart_1 g.chartPanel g text"
        utillobj.synchronize_with_number_of_element(element_css, 12, 20)
        
        """
        Expect to see the Clustered bar chart converted into the Preview pane for Bubble Chart.
        """
        result_obj.verify_xaxis_title('TableChart_1','Product', "Step 04.1 : Verify X-Axis Title")
        result_obj.verify_yaxis_title('TableChart_1','Unit Sales', "Step 04.2 : Verify Y-Axis Title")
        expected_xval_list=['Capuccino','Espresso']
        expected_yval_list=['0', '50K' ,'100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 04.3 :')
        result_obj.verify_number_of_circle('TableChart_1', 0, 3, 'Step 04.4 : Verify number of circles')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mmarker!', 'bar_blue1', 'Step 04.5 : Verify bar color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g1!mmarker!', 'bar_blue1', 'Step 04.6 : Verify bar color')
        
        """
        Step 05 : Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        element_css="#MAINTABLE_wbody0_f g.chartPanel g text"
        utillobj.synchronize_with_number_of_element(element_css, 18, 20)
        
        """
        Expect to see the following Bubble Chart.
        """
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Product', 'Step 05.1 : Verify Chart Title')
        result_obj.verify_xaxis_title('MAINTABLE_wbody0','Product', "Step 05.2 : Verify X-Axis Title")
        result_obj.verify_yaxis_title('MAINTABLE_wbody0','Unit Sales', "Step 05.2 : Verify Y-Axis Title")
        expected_xval_list=['Biscotti','Capuccino','Coffee Grinder','Coffee Pot','Croissant','Espresso','Latte','Mug','Scone','Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05.3 :')
        result_obj.verify_number_of_circle('MAINTABLE_wbody0', 0, 11, 'Step 05.4 : Verify number of circles')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g4!mmarker!', 'lochmara', 'Step 05.5 : Verify bar color')
        #expected_tooltip=['Product:  Croissant', 'Unit Sales:  630054', 'Dollar Sales:  7749902', 'Filter Chart', 'Exclude from Chart']
        #miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s0!g4!mmarker!',expected_tooltip,'Step 05.6 : Verify chart tooltip value')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.7 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.8 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.9 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        utillobj.switch_to_default_content(pause=1)
        
#         """
#         Save Chart      
#         """
#         ele=driver.find_element_by_css_selector("#resultArea")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step03', image_type='actual',x=1, y=1, w=-1, h=-1)
#         ribbonobj.select_tool_menu_item('menu_save_as')
#         utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__=='__main__' :
    unittest.main()