'''
Created on JUN 14, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2234945
TestCase Name = Verify Pie, Ring Pie, Pie Multi, Ring Pie Multi in others tab under Format menu.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,ia_ribbon
from common.lib import utillity

class C2234945_TestClass(BaseTestCase):

    def test_C2234945(self):
        
        Test_Case_ID="C2234945"
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        """
            Step 01:Create a Chart with ggsales.mas From Home tab Select Active Report as Output file format. From Select a chart pop up choose the first option - 'Pie'.Click Ok.
        """    
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 65)
        
        ribbonobj.change_output_format_type('active_report')
        time.sleep(1)
        parent_css="#HomeTab #HomeFormatType [class='bi-button-label']"
        utillobj.synchronize_with_visble_text(parent_css, "ActiveReport", 15)
        
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('pie', 'pie', 1, ok_btn_click=True)
        
        """
            Step 02: Add fields as follows:Category under Rows, Dollar Sales under Measure, Product under Color
        """
        
        metadataobj.datatree_field_click('Category', 1, 1, 'Add To Query', 'Rows')
        parent_css="#TableChart_1 g.chartPanel g text[class='rowHeader-label!']"
        utillobj.synchronize_with_visble_text(parent_css, 'Category', 15)
        
        metadataobj.datatree_field_click('Dollar Sales', 1, 1, 'Add To Query', 'Measure')
        parent_css="#TableChart_1 [class^='pieLabel!g0']"
        utillobj.synchronize_with_visble_text(parent_css, "Dollar Sales", 15)
        
        metadataobj.datatree_field_click('Product', 1, 1, 'Add To Query', 'Color')
        parent_css="#TableChart_1 g.legend g text[class='legend-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'Product', 15)
        
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', ['Dollar Sales'], "Step 02.1:",custom_css="text[class*='pieLabel']",same_group=True) 
        expected_label_list=['Product', 'Capuccino', 'Espresso']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 02.2: Verify pie lablesList ')
        resobj.verify_visualization_row_column_header_labels('TableChart_1', 'Rows', 'Category', ['Coffee'], "Step 02.3: Verify row header and value")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge!r0!c0", "bar_blue1", "Step 02.4: Verify  bar color")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, "Step 03.8: Verify number of pie", custom_css=".chartPanel .scrollCharts path[class*='riser!']")
              
        """
            Step 03:Click run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.switch_to_frame(pause=2)
        
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Dollar Sales', 'Dollar Sales', 'Dollar Sales'], "Step 03.1:", custom_css="text[class*='pieLabel']", same_group=True)
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 03.2: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r1!c0!", "bar_blue", "Step 03.3: Verify first bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales BY Category, Product', 'Step 03.4: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.5: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 03.8: Verify number of pie", custom_css=".chartPanel .scrollCharts path[class*='riser!']")    
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'Rows', 'Category', ['Coffee', 'Food', 'Gifts'], "Step 03.10: Verify row header and value")
           
        """
            Step 04:Close the Pie chart.Back in Format > Other, select the second option - 'Ring Pie'. Click OK.
        """
        utillobj.switch_to_default_content(pause=3)
        resobj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        ribbonobj.select_ribbon_item("Format", "Other")
        ia_ribbobj.select_other_chart_type('pie', 'ring_pie', 4, ok_btn_click=True)
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', ['Dollar Sales'], "Step 04.1:",custom_css="text[class*='pieLabel']",same_group=True) 
        expected_label_list=['Product', 'Capuccino', 'Espresso']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 04.2: Verify pie lablesList ')
        resobj.verify_visualization_row_column_header_labels('TableChart_1', 'Rows', 'Category', ['Coffee'], "Step 04.3: Verify row header and value")
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', ['6.1M'], "Step 04.4:",custom_css="text[class^='totalLabel!g']",same_group=True) 
  
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge!r0!c0!", "bar_blue1", "Step 04.5: Verify first bar color")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, "Step 04.6: Verify number of pie", custom_css=".chartPanel .scrollCharts path[class*='riser!']")
        """
            Step 05: Click Run
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        utillobj.switch_to_frame(pause=2)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Dollar Sales', 'Dollar Sales', 'Dollar Sales'], "Step 05.1:",same_group=True)
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 05.2: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r1!c0!", "bar_blue", "Step 05.3: Verify first bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales BY Category, Product', 'Step 05.4: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.5: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 05.8: Verify number of pie", custom_css=".chartPanel .scrollCharts path[class*='riser!']")
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['17.2M', '17.2M', '11.7M'], "Step 05.9:",custom_css="text[class^='totalLabel!g']",same_group=True) 
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'Rows', 'Category', ['Coffee', 'Food', 'Gifts'], "Step 05.11: Verify row header and value")
        time.sleep(2)
        
        """
            Step 06:Close the Pie Multi chart. Add Unit Sales to the Measure area.Back in Format > Other, select the third option - 'Pie Multi'. Click OK.
        """
        
        utillobj.switch_to_default_content(pause=3)
        resobj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        metadataobj.datatree_field_click('Unit Sales', 1, 1, 'Add To Query', 'Measure')     
        parent_css="#TableChart_1 g.chartPanel g text[class='pieLabel!g1!mpieLabel!']"
        utillobj.synchronize_with_visble_text(parent_css, "Unit Sales", 15)
       
        ribbonobj.select_ribbon_item("Format", "Other")
        ia_ribbobj.select_other_chart_type('pie', 'pie_multi', 5, ok_btn_click=True)
        time.sleep(5)
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', ['Dollar Sales', 'Unit Sales'], "Step 06.1:",custom_css="text[class*='pieLabel']",same_group=True) 
        expected_label_list=['Product', 'Capuccino', 'Espresso']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 06.2: Verify pie lablesList ')
        resobj.verify_visualization_row_column_header_labels('TableChart_1', 'Rows', 'Category', ['Coffee'], "Step 06.3: Verify row header and value")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge!r0!c0!", "bar_blue1", "Step 06.4: Verify first bar color")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 4, "Step 06.5: Verify number of pie", custom_css=".chartPanel .scrollCharts path[class*='riser!']")
        """
            Step 07: Click Run
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        utillobj.switch_to_frame(pause=2)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Dollar Sales', 'Unit Sales','Dollar Sales', 'Unit Sales', 'Dollar Sales', 'Unit Sales'], "Step 07.1:", custom_css="text[class*='pieLabel']", same_group=True)
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 07.2: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r1!c0!", "bar_blue", "Step 07.3: Verify first bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales, Unit Sales BY Category, Product', 'Step 07.4: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.5: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 20, "Step 07.8: Verify number of pie", custom_css=".chartPanel .scrollCharts path[class*='riser!']")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'Rows', 'Category', ['Coffee', 'Food', 'Gifts'], "Step 07.10: Verify row header and value")
           
        """
            Step 08:Close the Pie Multi chart.Back in Format > Other, select the third option - 'Ring Pie Multi'.Click OK.
        """
        utillobj.switch_to_default_content(pause=3)
        resobj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
       
        ribbonobj.select_ribbon_item("Format", "Other")
        ia_ribbobj.select_other_chart_type('pie', 'pie_multi_ring', 6, ok_btn_click=True)
        time.sleep(5)
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', ['Dollar Sales', 'Unit Sales'], "Step 08.1:",custom_css="text[class*='pieLabel']",same_group=True) 
        expected_label_list=['Product', 'Capuccino', 'Espresso']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 08.2: Verify pie lablesList ')
        resobj.verify_visualization_row_column_header_labels('TableChart_1', 'Rows', 'Category', ['Coffee'], "Step 08.3: Verify row header and value")
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', ['6.1M', '483K'], "Step 04.4:",custom_css="text[class^='totalLabel!g']",same_group=True) 
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge!r0!c0!", "bar_blue1", "Step 08.5: Verify first bar color")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 4, "Step 08.6: Verify number of pie", custom_css=".chartPanel .scrollCharts path[class*='riser!']")
        
        """
            Step 09: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        parent_css="#MAINTABLE_wbody0 .chartPanel .scrollCharts path[class*='riser!']"
        utillobj.synchronize_with_number_of_element(parent_css, 20, 25)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Dollar Sales', 'Unit Sales', 'Dollar Sales', 'Unit Sales', 'Dollar Sales', 'Unit Sales'], "Step 09.1:",custom_css="text[class*='pieLabel']", same_group=True)
        expected_label_list=['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 09.2: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!r1!c0!", "bar_blue", "Step 09.3: Verify first bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales, Unit Sales BY Category, Product', 'Step 09.4: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.5: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 20, "Step 09.8: Verify number of pie", custom_css=".chartPanel .scrollCharts path[class*='riser!']")
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['17.2M', '1.4M', '17.2M', '1.4M', '11.7M', '928K'], "Step 09.9:",custom_css="text[class^='totalLabel!g']",same_group=True) 
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'Rows', 'Category', ['Coffee', 'Food', 'Gifts'], "Step 09.11: Verify row header and value")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step9', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()