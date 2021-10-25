'''
Created on JUL 10, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204987
TestCase Name = AHTML:IA:JSCHART:Sort-»Limit throws error message-149217
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous
from common.lib import utillity

class C2204987_TestClass(BaseTestCase):

    def test_C2204987(self):
        
        Test_Case_ID="C2204987"
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        """
            Step 01:Launch Info Assist and create a new Chart using the CAR file.
            Select Active Report as the output format.
            
        """    
        utillobj.infoassist_api_login('Chart', 'ibisamp/car', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)  
        time.sleep(3)  
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        """
            Step 02:Add fields Car & Dealer_Cost.
    
        """  
        metadataobj.datatree_field_click('CAR', 1, 0, 'Add To Query', 'Horizontal Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1, string_value='CAR', with_regular_exprestion=True)
        metadataobj.datatree_field_click('DEALER_COST', 1, 0, 'Add To Query', 'Vertical Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        resobj.wait_for_property(parent_css, 1, string_value='DEALER_COST', with_regular_exprestion=True)
        time.sleep(3)
        resobj.verify_xaxis_title("TableChart_1", "CAR", "Step 02.1: Verify -xAxis Title")
        time.sleep(1)
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 02.2: Verify -yAxis Title")
        time.sleep(2)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 02.3: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 10, 'Step 02.4: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue1", "Step 02.5 Verify  bar color")
        """
            Step 03:Run the report    
    
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 03.1: Verify -yAxis Title")
        time.sleep(1)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 03.2: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 03.3: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 03.4: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 03.5: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST by CAR', 'Step 03.6: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.7: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g2!mbar!", expected_tooltip_list, "Step 03.10: Verify bar value")
        """
            Step 04:Right click on Bar in design area, and select Sort-> limit->5
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        resobj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        time.sleep(2)
        parent_css="#TableChart_1 [class*='riser!s0!g2!mbar!']"    
        selector = driver.find_element_by_css_selector(parent_css)
        utillobj.click_type_using_pyautogui(selector,cord_type='middle',default_move=True,leftClick=True)
        time.sleep(4)
        resobj.wait_for_property(parent_css, 1,expire_time=50)
        utillobj.click_type_using_pyautogui(selector,cord_type='middle',rightClick=True)
        utillobj.select_or_verify_bipop_menu('Sort')
        utillobj.select_or_verify_bipop_menu('Limit')
        utillobj.select_or_verify_bipop_menu('5')
        time.sleep(4)
        """
            Step 05:Click the Run button.    
    
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 05.1: Verify -yAxis Title")
        time.sleep(1)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 05.2: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['DATSUN', 'TOYOTA', 'TRIUMPH', 'PEUGEOT', 'AUDI']
        expected_yval_list=['0', '1,000', '2,000', '3,000', '4,000', '5,000', '6,000']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 05.3: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 5, 'Step 05.4: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 05.5: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST by CAR', 'Step 05.6: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.7: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['CAR:TRIUMPH', 'DEALER_COST:4,292', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g2!mbar!", expected_tooltip_list, "Step 05.10: Verify bar value")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step5', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()
