'''Created by June 28 2019

@author: vishnu_priya

Testcase link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2241292
Title :  Line Chart drilldown on a marker is working properly (HTML5)
'''

import unittest,time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart 
from common.lib import core_utility

class C2276113_TestClass(BaseTestCase):

    def test_C2276113(self):
        
        utils=utillity.UtillityMethods(self.driver)
        core_utils=core_utility.CoreUtillityMethods(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        
        """
        Step 1:Launch the IA API with Chart (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP251_S9164%2FG159435&tool=chart&master=baseapp/wf_retail_lite
        """
        
        chart_obj.invoke_chart_tool_using_api("ibisamp/car")
        chart_obj.wait_for_number_of_element(".chartPanel .risers rect",25,chart_obj.chart_long_timesleep)
 
        """
        Step 2:Select "Format" > "Chart Types" > "Line".
        """
        chart_obj.select_ia_ribbon_item('Format', 'Line')
        chart_obj.wait_for_number_of_element(".groupPanel [class='risers'] path",5,chart_obj.chart_long_timesleep)

        """
        Step 3:Double click CAR and SALES.
        Fields added into query pane and canvas updated..
        """
        chart_obj.double_click_on_datetree_item("CAR",1)
        chart_obj.wait_for_visible_text("#queryTreeColumn", "CAR", chart_obj.chart_long_timesleep)
        chart_obj.double_click_on_datetree_item("SALES",1)
        chart_obj.wait_for_visible_text("#queryTreeColumn", "SALES", chart_obj.chart_long_timesleep)
        chart_obj.verify_x_axis_title_in_preview(['CAR'] ,msg="Step:3.1")
        chart_obj.verify_y_axis_title_in_preview(['SALES'],msg="Step:3.2")
        chart_obj.verify_number_of_risers(".groupPanel .risers",1,1,msg="Step:3.3")
        chart_obj.verify_y_axis_label_in_preview(['0', '20K', '40K', '60K', '80K', '100K'],msg="Step:3.4")
        chart_obj.verify_x_axis_label_in_preview(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'],msg="Step:3.5")

        """
        Step 4:Click "Run"..
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()

        """Step 5:Hover over any datapoint on the Line chart..
        Tooltip value displayed.
        """
        core_utils.python_move_to_element(utils.validate_and_get_webdriver_object('#jschart_HOLD_0', 'chart'))
        time.sleep(5)
        chart_obj.select_or_verify_marker_tooltip_in_run_window("marker!s0!g0!mmarker!",  verify_tooltip_list=['CAR:ALFA ROMEO', 'SALES:30200'], msg="Step:5", parent_css="#jschart_HOLD_0")

 
        """
        Step 6:Logout using API
        http://domain:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
 
if __name__ == '__main__':
    unittest.main() 




        
