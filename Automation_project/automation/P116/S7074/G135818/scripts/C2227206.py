'''
Created on MAY 12,2017 

@author: pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Testcase = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227206
TestCase Name = VAL:AHTML:chart:By default it displays legends (ACT-111)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest,time
from common.pages import visualization_resultarea, active_miscelaneous


class C2227206_TestClass(BaseTestCase):
    def test_C2227206(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        
        """ 
        Step 1:In Text Editor, create a new report fex; copy the attached repro_simple.fex.
        and Run the report.      
        """
        utillobj.active_run_fex_api_login("162760.fex", "S7074", 'mrid', 'mrpass')
        time.sleep(6)
        parent_css="div [id='MAINTABLE_wmenu0']"
        result_obj.wait_for_property(parent_css, 1)
        
        """ 
        Step 2:(a) Verify the run report 
        """

        result_obj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 2:a(i) Verify -yAxis Title")
        result_obj.verify_xaxis_title("MAINTABLE_wbody0_f", "Category : Product", "Step 2:a(ii) Verify -xAxis Title")
        expected_xval_list=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels("MAINTABLE_wbody0_f", expected_xval_list, expected_yval_list, "Step 2:b:Verify XY labels")
        result_obj.verify_number_of_riser("MAINTABLE_wbody0_f", 1, 10, 'Step 2:c: Verify the total number of risers displayed on preview')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "cerulean_blue", "Step 2:d: Verify  bar color")
        expected_tooltip_list=['Unit Sales, Coffee/Latte: 878,063']
        miscelaneous_obj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g2!mbar!', expected_tooltip_list, "Step 2.e: verify tooltip values")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category, Product', 'Step 2:f: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 2:g: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 2:h: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 2:i: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
       

if __name__ == "__main__":
    unittest.main()  