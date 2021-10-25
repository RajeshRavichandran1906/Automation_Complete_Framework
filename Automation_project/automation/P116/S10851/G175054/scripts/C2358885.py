'''
Created on Jan 23, 2018
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2358885
@author: Praveen Ramkumar
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_resultarea,visualization_metadata,visualization_ribbon
from common.lib import utillity

class C2358885_TestClass(BaseTestCase):

    def test_C2358885(self):
        
        """ TESTCASE VARIABLES """
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        active_mis_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
                      
        step1="""
        Step 01:Create an Active Document with ggsales.mas
        Insert a chart and enter fields as Category, Product, Unit
        Sales and Dollar sales
        """
        utillobj.infoassist_api_login('document','ibisamp/ggsales', 'S10851_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 190)
        vis_ribbon.switch_ia_tab('Home')
        vis_ribbon.select_ribbon_item('Insert', 'Chart')
        utillobj.synchronize_with_visble_text("[class*='legend-labels!s0!']", 'Series0', 190)
        
        vis_metadata.datatree_field_click('Category', 2, 0)
        chart_xtitle_css="#TableChart_1 [class*='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(chart_xtitle_css, 'Category', 190)
         
        vis_metadata.datatree_field_click('Product', 2, 0)
        utillobj.synchronize_with_visble_text(chart_xtitle_css, 'Category:Product', 190)
        
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        chart_legend1_css="#TableChart_1 [class*='yaxis-title']"
        utillobj.synchronize_with_visble_text(chart_legend1_css, 'UnitSales', 190)
        
        vis_metadata.datatree_field_click('Dollar Sales', 2, 0)
        chart_legend2_css="#TableChart_1 [class*='legend-labels!s1']"
        utillobj.synchronize_with_visble_text(chart_legend2_css, 'DollarSales', 190)
        utillobj.capture_screenshot('01.01', step1)
        
        step3="""
        Step 02:From format tab, select Line as chart type
        Step 03:Click on Series tab and select Smooth line option
        """
        vis_ribbon.select_ribbon_item('Format', 'Line')
        line_css="[class*='mline']"
        utillobj.synchronize_with_number_of_element(line_css, 2, 190)
        vis_ribbon.select_ribbon_item('Series', 'smoothline')
        utillobj.capture_screenshot('03.01', step3)
        
        step5="""
        Step 04:Run the dashboard and click Line chart icon. You will see correct output of Smooth line            
        Step 05:De-select the smooth line option from series tab
        """
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css,1,190)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0",1,190)
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody0", "Category : Product", "Step 05.01: Verify X-Axis Title")  
        expected_xval_list=['Coffee : Ca...', 'Coffee : Es...', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croi...', 'Food : Scone', 'Gifts : Coff...', 'Gifts : Coff...', 'Gifts : Mug', 'Gifts : The...']
        expected_yval1_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.02: Verify XY labels")
        legend=['Unit Sales', 'Dollar Sales']
        vis_resultobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.03: Verify Y-Axis legend")
        active_mis_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category, Product', 'Step 05.04: Verify Chart Title')
        active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.05: Verify Chart toolbar")
        active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.06: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.07: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=3)
        vis_ribbon.select_ribbon_item('Format', 'Line')
        line_css="[class*='mline']"
        utillobj.synchronize_with_number_of_element(line_css, 2, 190)
        vis_ribbon.select_ribbon_item('Series', 'smoothline')
        utillobj.capture_screenshot('05.01', step5)
        
        step6="""
        Step 06:Run the Dashboard. You will see line chart run with connected format.
        """
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        frame_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(frame_css,1,190)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0",1,190)
        vis_resultobj.verify_xaxis_title("MAINTABLE_wbody0", "Category : Product", "Step 060.1: Verify X-Axis Title")  
        expected_xval_list=['Coffee : Ca...', 'Coffee : Es...', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croi...', 'Food : Scone', 'Gifts : Coff...', 'Gifts : Coff...', 'Gifts : Mug', 'Gifts : The...']
        expected_yval1_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        vis_resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 06.02: Verify XY labels")
        legend=['Unit Sales', 'Dollar Sales']
        vis_resultobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 06.03: Verify Y-Axis legend")
        active_mis_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category, Product', 'Step 06.04: Verify Chart Title')
        active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.05: Verify Chart toolbar")
        active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.06: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.07: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=3)
        utillobj.capture_screenshot('06.01', step6)
        
if __name__ == '__main__':
    unittest.main()