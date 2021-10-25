'''
Created on JUN 13, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2318031
TestCase Name = Verify 3D Surface in others tab under Format menu.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,ia_ribbon
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2318031_TestClass(BaseTestCase):

    def test_C2318031(self):
        
        Test_Case_ID="C2318031"
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
            Step 01: Right click on folder created in IA and create a new Chart using the GGSALES file.From Home tab Select Active Report as Output file format.
        """    
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 .chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(4)  
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 .chartPanel"
        resobj.wait_for_property(parent_css, 1)
        """
            Step 02:Add fields Product, Dollar Sales, Unit Sales.
        """
        metadataobj.datatree_field_click('Product', 2, 0)
        parent_css="#TableChart_1 g text[class='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Dollar Sales',2, 0)
        parent_css="#TableChart_1 g text[class='yaxis-title']"
        resobj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales',2, 0)
        parent_css="#TableChart_1 g text[class='legend-labels!s1!']"
        resobj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        time.sleep(2)
        resobj.verify_xaxis_title("TableChart_1", "Product", "Step 02.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 02.2: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 4, 'Step 02.3: Verify the total number of risers displayed on preview')
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 02.4: Verify  bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "bar_green", "Step 02.5: Verify  bar color")
        legend=["Dollar Sales","Unit Sales",]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 02.6: Verify Y-Axis legend")
        """
            Step 03: Click the Run button.
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 03.1: Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 03.2: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 03.3: Verify the total number of risers displayed on preview')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 03.4: Verify  bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mbar!", "pale_green", "Step 03.5: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales, Unit Sales BY Product', 'Step 03.6: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.7: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        expected_tooltip_list=['Product:Latte', 'Dollar Sales:10943622', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g6!mbar!", expected_tooltip_list, "Step 03.10: Verify bar value")
        time.sleep(2)
        expected_tooltip_list=['Product:Latte', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g6!mbar!", expected_tooltip_list, "Step 03.11: Verify bar value")
         
        """
            Step 04:Select Format > Other.From Select a chart pop up choose 3D Surface. Click OK.
            Commas added to the Expected Y values as per updated from Jagadeesh and comments from CHART-1618
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(1)
        ribbonobj.select_ribbon_item('Format', 'Other')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resobj._validate_page(elem1)
        ia_ribbobj.select_other_chart_type('threed', 'threed_surface', 13, ok_btn_click=True)
        time.sleep(3)
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '500,000', '1,000,000', '1,500,000', '2,000,000', '2,500,000', '3,000,000', '3,500,000', '4,000,000']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 04.1: Verify XY labels", z_expected_labels=["Dollar Sales","Unit Sales"], )
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 04.2:verify number of 3D segment', custom_css="svg g>path[class^='riser']")
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "bar_green", "Step 04.3: Verify  bar color")
        legend=["Dollar Sales","Unit Sales"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 04.4: Verify Y-Axis legend")
        """
            Step 05: Click the Run button.
            Commas added to the Expected Y values as per updated from Jagadeesh and comments from CHART-1618
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(2)
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '2,000,000', '4,000,000', '6,000,000', '8,000,000', '10,000,000','12,000,000']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 05.1: Verify XY labels", z_expected_labels=["Dollar Sales","Unit Sales"])
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 9,'Step 05.2:verify number of 3D segment', custom_css="svg g>path[class^='riser']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 3,'Step 05.3:verify 3D chart  wall', custom_css=".chartPanel path[d^='M'][stroke-width='1'][fill]")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mbar!", "pale_green", "Step 05.6: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Dollar Sales, Unit Sales BY Product', 'Step 05.7: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 05.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.9: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        miscelaneous_obj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s1!g0!mbar!',['421,377'], "Step 05.11:verify 3D surface tooltip")
        legend=["Dollar Sales","Unit Sales"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.12: Verify Y-Axis legend")
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