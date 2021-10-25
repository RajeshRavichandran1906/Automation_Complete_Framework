'''
Created on Nov 21, 2017

@author: Prabhakaran

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2317998
TestCase Name = Verify Vertical Percent Bars in others tab under Format menu.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_ribbon
from common.lib import utillity


class C2317998_TestClass(BaseTestCase):

    def test_C2317998(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID='C2317998'
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """
            Step 01: Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES and From Home tab Select Active Report as Output file format.
        """  
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 [class='riser!s1!g2!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 75)
  
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 [class='riser!s1!g2!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 10)
        
        """
        Step 01.1 : Verify preview
        """
        expected_xval_list=['Group 1','Group 2','Group 3','Group 4']
        expected_yval_list=['0', '10', '20', '30', '40', '50']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 01.1:")
        resobj.verify_riser_legends('TableChart_1',['Series0','Series1','Series2','Series3','Series4'], 'Step 01.2: Verify Chart legends label')
        resobj.verify_number_of_riser('TableChart_1', 5,5,'Step 01.3 : Verify number of chart risers')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 01.4 : Verify chart riser color')
        
        """
            Step 02: Add fields Category, Unit Sales, Dollar Sales.
        """
        metadataobj.datatree_field_click('Category', 2, 0)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='xaxisOrdinal-title']",'Category',15)
        
        metadataobj.datatree_field_click('Unit Sales', 2, 0)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='yaxis-title']",'Unit Sales',15)
        
        metadataobj.datatree_field_click('Dollar Sales',2, 0)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='legend-labels!s1!']",'Dollar Sales',15)
        
        resobj.verify_xaxis_title("TableChart_1", "Category", "Step 02.1: Verify X axis Title")
        resobj.verify_riser_legends('TableChart_1',['Unit Sales','Dollar Sales'], 'Step 02.2: Verify Chart legends label')
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M','6M','7M']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 02.3: Verify XY axis labels")
        resobj.verify_number_of_riser('TableChart_1', 1,2,'Step 02.4 : Verify number of chart risers')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 02.5:  Verify chart riser color')
        
        """
            Step 03 : Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        
        """
            Step 03.1 : Verify output chart
        """
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft','Unit Sales, Dollar Sales by Category','Step 03.1 : Verify chart title')
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Category", "Step 03.2 : Verify X axis Title")
        resobj.verify_riser_legends('MAINTABLE_wbody0',['Unit Sales','Dollar Sales'], 'Step 03.3 : Verify Chart legends lablesList')
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 03.4 : Verify XY axis labels")
        resobj.verify_number_of_riser('MAINTABLE_wbody0', 1,6,'Step 03.5 : Verify number chart of risers')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g1!mbar!', 'bar_blue', 'Step 03.6 :  Verify chart riser Color')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.7 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.8 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]') 
        utillobj.switch_to_default_content(pause=3)
        
        """
            Step 04 :Select Format > Other.From Select a chart pop up choose 'Vertical Percent Bars'.Click OK.
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('bar', 'vertical_percent_bars', 3, ok_btn_click=True)
        time.sleep(4)
        resobj.verify_xaxis_title("pfjTableChart_1", "Category", "Step 04.1 : Verify X axis Title")
        resobj.verify_riser_legends('pfjTableChart_1',['Unit Sales','Dollar Sales'], 'Step 04.2 : Verify chart legends lablesList')
        expected_xval_list=['Coffee']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("pfjTableChart_1", expected_xval_list, expected_yval_list, "Step 04.3 : Verify XY axis labels")
        resobj.verify_number_of_riser('pfjTableChart_1', 1,2,'Step 04.4 : Verify number of chart risers')
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 04.5 :  Verify chart riser color')
         
        """
        Step 05 : Run and verify output.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 45)
        utillobj.switch_to_frame(pause=2)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Category", "Step 05.1: Verify X axis Title")
        resobj.verify_riser_legends('MAINTABLE_wbody0',['Unit Sales','Dollar Sales'], 'Step 05.2: Verify Chart legends lablesList')
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval_list=['0%', '20%', '40%', '60%', '80%', '100%']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 05.3: Verify XY axis labels")
        resobj.verify_number_of_riser('MAINTABLE_wbody0', 1,6,'Step 05.4 : Verify number chart of risers')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g1!mbar!', 'bar_blue', 'Step 05.5:  Verify chart riser Color')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.6: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]') 
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft','Unit Sales, Dollar Sales by Category','Step 05.09 : Verify chart title')
        utillobj.switch_to_default_content(pause=3)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step05', image_type='actual')
           
if __name__ == '__main__':
    unittest.main()