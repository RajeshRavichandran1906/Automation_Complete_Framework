'''
Created on Jul 12, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2204883
TestCase Name = Verify user is able to export chart to Word document

'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea,active_chart_rollup
from common.lib import utillity


class C2204883_TestClass(BaseTestCase):

    def test_C2204883(self):
        
        """
        TESTCASE VARIABLES
        """
        
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        act_chart=active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        """
        Step 01 : Execute attached fex "Chart_AHTML.fex" in IA.
        """
        utillobj.active_run_fex_api_login("Chart_AHTML.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody0_f .risers rect[class^='riser!']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, 65)
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft','Unit Sales by Category, Product','Step 01.1 : Verify Chart Title')
        result_obj.verify_xaxis_title('MAINTABLE_wbody0','Category : Product', 'Step 01:1 Verify X-Axis Title')
        result_obj.verify_yaxis_title('MAINTABLE_wbody0','Unit Sales', 'Step 01:2 Verify Y-Axis Title')
        expected_xval_list=['Coffee/Capuccino','Coffee/Espresso','Coffee/Latte','Food/Biscotti','Food/Croissant','Food/Scone','Gifts/Coffee Grinder','Gifts/Coffee Pot','Gifts/Mug','Gifts/Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 01.3 : ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 01.4: Verify number of risers')
        utillobj.verify_chart_color('MAINTABLE_wbody0','riser!s0!g4!mbar!', 'cerulean_blue', 'Step 01.5: Verify bar Color')
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s0!g4!mbar!',['Unit Sales, Food/Croissant: 630,054'], 'Step 01.6 : Verify Chart Tool Tip')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 01.7 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.8 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.9 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.take_monitor_screenshot('C2204883_Actual_Step_01','actual', left=0, top=60, right=0, bottom=40)
        time.sleep(4)
        
        """
        Step 02 : Click Export to > Word option from the dropdown menu
        """
        browser=utillobj.parseinitfile('browser')
        if browser=='IE' :
            act_chart.select_chartmenubar_option('MAINTABLE_wmenu0',0,'Export to->Word',0,custom_css='cpop')
            time.sleep(60)
            utillobj.take_monitor_screenshot('C2204883_Actual_Step_02', image_type='actual', left=0, top=20, right=600, bottom=40)  
            utillobj.kill_process('WINWORD')
            time.sleep(2)
        else :
            print("Export option available only in IE browser")
        
if __name__=='__main__' :
    unittest.main()