'''
Created on July 27, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204916
TestCase Name =Verify that all Charts (Bar, Pie, Line, scatter)are displayed with Red color.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, ia_resultarea,visualization_ribbon,visualization_metadata,ia_styling
from common.lib import utillity


class C2204916_TestClass(BaseTestCase):

    def test_C2204916(self):
        
        Test_Case_ID="C2204916"
         
        """            
        TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        styleobj = ia_styling.IA_Style(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        """ 
            Step 01: Open IA and create a new chart using the GGSALES file.
        """
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)  
        """
            Step 02:Select Active Report as the output format.
                    Add field Product to the Horizontal axis. Add field Dollar Sales to the Vertical axis.
        """   
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        metadataobj.datatree_field_click('Product', 1, 0, 'Add To Query', 'Horizontal Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Dollar Sales', 1, 0, 'Add To Query', 'Vertical Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        resobj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        """
            Step 03:See corresponding data is displayed in the Live Preview pane.
        """ 
        resobj.verify_yaxis_title("TableChart_1", "Dollar Sales", "Step 03.1: Verify -yAxis Title")
        resobj.verify_xaxis_title("TableChart_1", "Product", "Step 03.2: Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 03.3: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 03.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 03.5: Verify  bar color")
          
        """
            Step 04:Click the Run Button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 04.1: Verify -xAxis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Dollar Sales", "Step 04.2: Verify -yAxis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 04.3: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 04.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "bar_blue", "Step 04.5: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales by Product', 'Step 04.6: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.7: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g6!mbar", expected_tooltip_list, "Step 04.10: Verify bar value")
          
        """
            Step 05:Right click on any bar on the Preview pane and select "series color".
                    Change the color to Green.click ok.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(4)
        resobj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        time.sleep(3)
        parent_css="#TableChart_1 .chartPanel g rect[class*='riser!s0!g0!mbar']"
        parent_obj=driver.find_element_by_css_selector(parent_css)
        utillobj.click_type_using_pyautogui(parent_obj, leftClick=True)
        parent_css="#FieldFilter [class*='label']"
        resobj.wait_for_property(parent_css, 1, string_value='Filter', with_regular_exprestion=True)
        time.sleep(5)
        utillobj.click_type_using_pyautogui(parent_obj, rightClick=True)
        utillobj.select_or_verify_bipop_menu('Series Color...')
        time.sleep(2)
        styleobj.set_color("green")
        """
            Step 06:Click the Run Button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 06.1: Verify -xAxis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Dollar Sales", "Step 06.2: Verify -yAxis Title")
        time.sleep(2)
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 06.3: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 06.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "green", "Step 06.5: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales by Product', 'Step 06.6: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.7: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g6!mbar", expected_tooltip_list, "Step 06.10: Verify bar value")
           
        """
            Step 07:From the Format tab, click the PIE chart icon.  Click the Run button                  
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(4)
        ribbonobj.select_ribbon_item('Format', 'pie')
        parent_css="#TableChart_1 g.chartPanel g text[class='pieLabel!g0!mpieLabel!']"
        resobj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Dollar Sales'], "Step 07.1:",same_group=True)
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 07.2: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge", "green", "Step 07.3: Verify first bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales by Product', 'Step 07.4: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.5: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 07.8: Verify number of pie")    
        expected_tooltip_list=['Product:Latte', 'Dollar Sales:10943622  (23.71%)', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s6!g0!mwedge", expected_tooltip_list, "Step 07.9: Verify bar value") 
        
        """
            Step 08:From the Format tab, click the Line chart icon. Click the Run button.          
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(4)
        ribbonobj.select_ribbon_item('Format', 'line')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 07.1: Verify -xAxis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Dollar Sales", "Step 07.2: Verify -yAxis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 07.3: Verify XY labels")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0',11,'Step 07.4 : Verify number of chart risers')
        utillobj.verify_chart_color('MAINTABLE_wbody0','riser!s0!g0!mline','green','Step 07.5 : Verify chart riser color',attribute_type='stroke')
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales by Product', 'Step 07.6: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.7: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        css="#MAINTABLE_wbody0 .chartPanel"
        move=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(move, 'start')
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g6!mmarker!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(3)
        expected_tooltip_list=['Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "marker!s0!g6!mmarker!", expected_tooltip_list, "Step 04.10: Verify bar value",default_move=True)
        """
            Step 08:Right click on any point of the Line in the Preview pane and select "series color".
                    Change the color to Yellow. Click OK to the Color panel change.
                    From the Format tab, click the Area chart icon.Click the Run button.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(4)
        resobj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        time.sleep(3)
        parent_css="#TableChart_1 .chartPanel g path[class*='riser!s0!g0!mline'][stroke]"
        parent_obj=driver.find_element_by_css_selector(parent_css)
        parent_css="#TableChart_1 .chartPanel g path[class*='riser!s0!g0!mline'][stroke]"
        parent_obj=driver.find_element_by_css_selector(parent_css)
        utillobj.click_type_using_pyautogui(parent_obj, leftClick=True,x_offset=5)
#         parent_css="#FieldFilter [class*='label']"
#         resobj.wait_for_property(parent_css, 1, string_value='Filter', with_regular_exprestion=True)
        time.sleep(5)
        utillobj.click_type_using_pyautogui(parent_obj, rightClick=True,x_offset=5)
        utillobj.select_or_verify_bipop_menu('Series Color...')
        time.sleep(2)
        styleobj.set_color("yellow")
        time.sleep(5)
        ribbonobj.select_ribbon_item('Format', 'area')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 08.1: Verify -xAxis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Dollar Sales", "Step 08.2: Verify -yAxis Title")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 08.3: Verify XY labels")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0',11,'Step 08.4 : Verify number of chart risers')
        utillobj.verify_chart_color('MAINTABLE_wbody0','riser!s0!g0!marea!','yellow','Step 08.5 : Verify chart riser color')
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales by Product', 'Step 08.6: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.7: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        css="#MAINTABLE_wbody0 .chartPanel"
        move=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(move, 'start')
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g6!mmarker!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(3)
        expected_tooltip_list=['Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "marker!s0!g6!mmarker", expected_tooltip_list, "Step 07.10: Verify bar value",default_move=True)
        """
            Step 09:From the Format tab, click the Scatter chart icon.
                    Click the Run button.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(4)
        ribbonobj.select_ribbon_item('Format', 'scatter')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 09.1: Verify -xAxis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Dollar Sales", "Step 09.2: Verify -yAxis Title")
        time.sleep(2)
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 09.3: Verify XY labels")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0',10,'Step 09.4 : Verify number of chart risers')
        utillobj.verify_chart_color('MAINTABLE_wbody0','riser!s0!g6!mmarker','yellow','Step 09.5 : Verify chart riser color',attribute_type='stroke')
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales by Product', 'Step 09.6: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.7: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g6!mmarker!", expected_tooltip_list, "Step 09.10: Verify bar value")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step8', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
if __name__ == '__main__':
    unittest.main()  
        
        
        