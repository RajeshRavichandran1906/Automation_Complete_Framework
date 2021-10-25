'''
Created on Jan 09, 2018

@author: Praveen Ramkumar

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2234948
TestCase Name = Verify Tag Cloud in others tab under Format menu.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,ia_ribbon
from common.lib import utillity

class C2234948_TestClass(BaseTestCase):

    def test_C2234948(self):
        
        Test_Case_ID="C2234948"
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
            Step 01:Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES and From Home tab Select Active Report as Output file format.
        """  
        
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 .chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(4)
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 .chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        
        """
            Step 02:Select Format > Other->HTML5
            Step 03:From Select a chart pop up choose 'Tag Cloud' and click OK.
        """ 
        
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('html5', 'html5_tagCloud',4, ok_btn_click=True)
        time.sleep(3)
        
        """
            Step 04:Add fields Product ID and add Unit Sales
        """
        
        metadataobj.datatree_field_click('Product ID', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resobj.wait_for_property(parent_css, 1, string_value='ProductID', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(6) td"
        resobj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        
        """
            Step 05:Click run.
        """    
            
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Unit Sales by Product ID", "Step 05.1 : Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.2: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.3: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.4: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mtag!", "bar_blue", "Step 05.5: Verify  riser color")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 9, 'Step 05.6: Verify Number of riser')
        
        """
            Step 06:Click run.
        """
        
        expected_tooltip_list=['Product ID:G100', 'Unit Sales:360570', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g6!mtag!", expected_tooltip_list, "Step 06.1: Verify bar value")
        time.sleep(2)
        utillobj.switch_to_default_content(pause=2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
                
if __name__ == '__main__':
    unittest.main()