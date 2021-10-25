'''
Created on MAY 10,2017 

@author: pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Testcase = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2203706
TestCase Name = AHTML:CHART/DEFAULT:Legends sligthly displayed over labels (142614)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest,time
from common.pages import visualization_resultarea,active_miscelaneous


class C2203706_TestClass(BaseTestCase):

    def test_C2203706(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        
 
        """ 
        Step 1:Create a AHTML simple report by run the C2203706.fex in text editor       
        """
        utillobj.active_run_fex_api_login("C2203706.fex", "S7074", 'mrid', 'mrpass')
        time.sleep(3)
        
        """ 
        Step 2:Check Legend fields (DEALER_COST and RETAIL_COST) are displayed properly  
        """
        parent_css="div [id='MAINTABLE_wmenu0']"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(1)
        xaxis_value="COUNTRY"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0_f", xaxis_value, "Step 2:a(i) Verify X-Axis Title")
        legend=["DEALER_COST", "RETAIL_COST"]
        result_obj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 2:a(ii) Verify Y-Axis Title")
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        result_obj.verify_riser_chart_XY_labels("MAINTABLE_wbody0_f", expected_xval_list, expected_yval_list, "Step 2:b Verify XY labels")
        result_obj.verify_number_of_riser("MAINTABLE_wbody0_f", 1, 10, 'Step 2.c: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "bar_blue", "Step 2:d: Verify first bar color")
        time.sleep(1)
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s1!g0!mbar!", "pale_green", "Step 2:e: Verify Second bar color")
        time.sleep(5)
         
        bar=['COUNTRY:ITALY', 'DEALER_COST:41,235', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g2!mbar!", bar, "Step 2:f: Verify bar value",x_offset=0,y_offset=-10)
         
        bar=['COUNTRY:ITALY', 'RETAIL_COST:51,065', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s1!g2!mbar!", bar, "Step 2:g: Verify bar value",x_offset=0,y_offset=-10)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by COUNTRY', 'Step 2:h: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 2:i: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 2:j: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 2:k: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        

if __name__ == "__main__":
    unittest.main()       