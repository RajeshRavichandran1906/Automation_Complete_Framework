'''
Created on July 27, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2318048
TestCase Name = Verify Streamgraph Chart in others tab under Format menu.

'''
import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon,ia_ribbon,ia_resultarea
from common.lib import utillity

class C2318048_TestClass(BaseTestCase):

    def test_C2318048(self):
       
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID="C2318048"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_result=ia_resultarea.IA_Resultarea(self.driver)
            
        """
        Step 01 : Right click on folder created in IA and create a new Chart using the GGSALES file.From Home tab Select Active Report as Output file format.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(2)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(5)
        
        """
        Step 02 : Add fields Product, Unit Sales.
        """
        metadataobj.datatree_field_click('Product', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value="Product")
        
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value="Unit Sales")
        time.sleep(3)
           
        """
        Verify Preview panel
        """
        result_obj.verify_xaxis_title("TableChart_1",'Product', "Step 02.1 : Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1",'Unit Sales', "Step 02.1 : Verify X-Axis Title")
        expected_xval_list=['Capuccino','Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K','350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 02.2 :')
        result_obj.verify_number_of_riser('TableChart_1', 1, 2, 'Step 02.3 : Verify number of risers')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 02.5 : Verify chart color')
        
        """
        Step 03 : Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        parent_css="#MAINTABLE_wbody0_f g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 18)
        time.sleep(3)
        
        """
        Expect to see the following Bar Chart.
        """
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Product', 'Step 03.1 : Verify Chart Title')
        result_obj.verify_xaxis_title('MAINTABLE_wbody0','Product', "Step 03.2 : Verify X-Axis Title")
        result_obj.verify_yaxis_title('MAINTABLE_wbody0','Unit Sales', "Step 03.3 : Verify X-Axis Title")
        expected_xval_list=['Biscotti','Capuccino','Coffee Grinder','Coffee Pot','Croissant','Espresso','Latte','Mug','Scone','Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03.3 :')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 03.5 : Verify number of risers')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g4!mbar!', 'lochmara', 'Step 03.6 : Verify chart color')
        expected_tooltip=['Product:  Croissant', 'Unit Sales:  630054', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s0!g4!mbar!',expected_tooltip,'Step 03.11 : Verify chart tooptip value')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.12 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.13 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.14 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        utillobj.switch_to_default_content(pause=1)
        time.sleep(3)
        
        """
        Step 04 : Select Format > Other.Select the HTML5 series of charts.From Select a chart pop up choose Streamgraph Chart.
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('html5', 'stream_graph', 3, ok_btn_click=True)
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 3)
        time.sleep(3)
        
        """
        Expect to see the Clustered bar chart converted into the Preview pane for Streamgraph Chart.
        """
        result_obj.verify_xaxis_title("TableChart_1",'Product', "Step 04.1 : Verify X-Axis Title")
        expected_xval_list=['Capuccino','Espresso']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list,[],'Step 04.2 :')
        ia_result.verify_number_of_chart_segment('TableChart_1',1,'Step 04.3 : Verify Streamgraph path',custom_css=".chartPanel path[class^='riser']")
        utillobj.verify_chart_color('TableChart_1',None, 'bar_blue1', 'Step 04.5 : Verify chart color',custom_css=".chartPanel path[class='riser!s0!g0!marea!']",attribute_type='fill')

        
        """
        Step 05 : Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        parent_css="#MAINTABLE_wbody0_f g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(3)
          
        """
        Expect to see the following Streamgraph Chart.
        """
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Product', 'Step 05.1 : Verify Chart Title')
        expected_xval_list=['Biscotti','Capuccino','Coffee Grinder','Coffee Pot','Croissant','Espresso','Latte','Mug','Scone','Thermos']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list,[], 'Step 05.2 :')
        ia_result.verify_number_of_chart_segment('MAINTABLE_wbody0',1,'Step 04.3 : Verify Streamgraph path',custom_css=".chartPanel path[class^='riser']")
        ia_result.verify_number_of_chart_segment('MAINTABLE_wbody0',10,'Step 04.3 : Verify Streamgraph tooltip circles',custom_css=".eventPanel circle[class^='marker']")
        utillobj.verify_chart_color('MAINTABLE_wbody0',None, 'lochmara', 'Step 04.5 : Verify bar color',custom_css=".chartPanel path[class='riser!s0!g0!marea!']",attribute_type='fill')
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.click_on_screen(parent_elem, coordinate_type='start')
        marker=driver.find_element_by_css_selector("#MAINTABLE_wbody0  circle[class='marker!s0!g0!mmarker!']")
        utillobj.click_on_screen(marker,'middle',javascript_marker_enable=True,mouse_duration=2.5)
        browser=utillobj.parseinitfile('browser')
        if browser == 'IE':
            time.sleep(3)
        else:
            time.sleep(1)
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0','marker!s0!g0!mmarker!', ['Product:  Biscotti', 'Unit Sales:  421377', 'Filter Chart', 'Exclude from Chart'],'Step 05.7 : Verify chart tooltip value',default_move=True)
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.8 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.9 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.10 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        utillobj.switch_to_default_content(pause=1)
        time.sleep(3)
          
        """
        Save Chart      
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_05', image_type='actual',x=1, y=1, w=-1, h=-1)
        result_obj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(4)
         
if __name__=='__main__' :
    unittest.main()