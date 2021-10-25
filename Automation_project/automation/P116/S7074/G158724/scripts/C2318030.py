'''
Created on July 14, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2318030
TestCase Name = Verify 3D Connected Series Area in others tab under Format menu.

'''
import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon,ia_ribbon,ia_resultarea
from common.lib import utillity


class C2318030_TestClass(BaseTestCase):

    def test_C2318030(self):
       
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID="C2318030"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
            
        """
        Step 01 : Right click on folder created in IA and create a new Chart using the GGSALES file. From Home tab Select Active Report as Output file format.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/ggsales','P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(2)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(5)
        
        """
        Step 02 : Add fields Product, Dollar Sales, Unit Sales.
        """
        metadataobj.datatree_field_click('Product', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value="Product")
        
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value="Dollar Sales")
        
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 .legend text"
        result_obj.wait_for_property(parent_css, 2)
        time.sleep(3)
        
        """
        Verify Preview panel
        """
        result_obj.verify_xaxis_title("TableChart_1",'Product', "Step 02.1 : Verify X-Axis Title")
        expected_xval_list=['Capuccino','Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M','3.5M','4M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 02.2 :')
        result_obj.verify_riser_legends('TableChart_1',['Dollar Sales','Unit Sales'], 'Step 02.3 : Verify chart legends label')
        result_obj.verify_number_of_riser('TableChart_1', 1, 4, 'Step 02.4 : Verify number of risers')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 02.5 : Verify bar color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mbar!', 'bar_green', 'Step 02.6 : Verify bar color')
        
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
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales, Unit Sales BY Product', 'Step 03.1 : Verify Chart Title')
        result_obj.verify_xaxis_title('MAINTABLE_wbody0','Product', "Step 03.2 : Verify X-Axis Title")
        expected_xval_list=['Biscotti','Capuccino','Coffee Grinder','Coffee Pot','Croissant','Espresso','Latte','Mug','Scone','Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03.3 :')
        result_obj.verify_riser_legends('MAINTABLE_wbody0',['Dollar Sales','Unit Sales'], 'Step 03.4 : Verify chart legends label')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step 03.5 : Verify number of risers')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', 'lochmara', 'Step 03.6 : Verify bar color')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s1!g0!mbar!', 'pale_green', 'Step 03.7 : Verify bar color')
        expected_tooltip1=['Product:  Biscotti', 'Dollar Sales:  5263317', 'Filter Chart', 'Exclude from Chart']
        expected_tooltip2=['Product:  Biscotti', 'Unit Sales:  421377', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s0!g0!mbar!',expected_tooltip1,'Step 03.8 : Verify chart tooltip value')
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s1!g0!mbar!',expected_tooltip2,'Step 03.9 : Verify chart tooptip value')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.10 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.11 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.12 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        utillobj.switch_to_default_content(pause=1)
        time.sleep(3)
        
        """
        Step 04 : Select Format > Other.From Select a chart pop up choose 3D Connected Series Area .Click OK.
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('threed', 'threed_connected_series_area', 9, ok_btn_click=True)
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 13)
        time.sleep(8)
        
        """
        Expect to see the Clustered bar chart converted into the Preview pane for 3D Connected Series Area .
        Commas added to the Expected Y values as per updated from Jagadeesh and comments from CHART-1618
        """
        expected_xval_list=['Capuccino','Espresso']
        expected_yval_list=['0', '500,000', '1,000,000', '1,500,000', '2,000,000', '2,500,000', '3,000,000', '3,500,000', '4,000,000']
        expected_zval_list=['Dollar Sales','Unit Sales']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 04.1 :',z_expected_labels=expected_zval_list)
        ia_resultobj.verify_number_of_chart_segment('TableChart_1',12,'Step 04.2 : Verify no of 3D chart risers ',  custom_css="svg g>path[class^='riser']")
        result_obj.verify_riser_legends('TableChart_1',['Dollar Sales','Unit Sales'], 'Step 04.3 : Verify chart legends label')
        utillobj.verify_chart_color('TableChart_1',None, 'bar_green', 'Step 04.4 : Verify bar color',custom_css="g>path[class='riser!s1!g0!mbar!']:nth-child(6)")
        utillobj.verify_chart_color('TableChart_1',None, 'bar_blue1', 'Step 04.5 : Verify bar color',custom_css="g>path[class='riser!s0!g0!mbar!']:nth-child(6)")
        
        """
        Step 05 : Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        parent_css="#MAINTABLE_wbody0_f g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 19)
        time.sleep(3)
         
        """
        Expect to see the following 3D Connected Series Area .
        Commas added to the Expected Y values as per updated from Jagadeesh and comments from CHART-1618
        """
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales, Unit Sales BY Product', 'Step 05.1 : Verify Chart Title')
        expected_xval_list=['Biscotti','Capuccino','Coffee Grinder','Coffee Pot','Croissant','Espresso','Latte','Mug','Scone','Thermos']
        expected_yval_list=['0', '2,000,000', '4,000,000', '6,000,000', '8,000,000', '10,000,000', '12,000,000']
        expected_zval_list=['Dollar Sales','Unit Sales']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 05.2 :',z_expected_labels=expected_zval_list)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0 ',44,'Step 05.3 : Verify no of 3D chart risers',  custom_css="svg g>path[class^='riser']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0 ',3,'Step 05.4 : Verify no of 3D chart wall',  custom_css=".chartPanel path[d^='M'][stroke-width='1'][fill]")
        utillobj.verify_chart_color('MAINTABLE_wbody0 ',None, 'pale_green', 'Step 05.5 : Verify bar color',custom_css="g>path[class='riser!s1!g0!mbar!']:nth-child(22)")
        utillobj.verify_chart_color('MAINTABLE_wbody0 ',None, 'lochmara', 'Step 05.6 : Verify bar color',custom_css="g>path[class='riser!s0!g0!mbar!']:nth-child(22)")
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s0!g0!mbar!',['5,263,317'],'Step 05.7 : Verify chart tooltip value')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 05.8 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.9 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.10 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)        
        utillobj.switch_to_default_content(pause=1)
        time.sleep(3)
         
        """
        Save Chart      
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        time.sleep(10)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step_05', image_type='actual',x=1, y=1, w=-1, h=-1)
        result_obj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(4)
        
if __name__=='__main__' :
    unittest.main()