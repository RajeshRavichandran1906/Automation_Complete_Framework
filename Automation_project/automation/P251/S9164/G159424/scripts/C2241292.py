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
from common.lib.global_variables import Global_variables

class C2241292_TestClass(BaseTestCase):

    def test_C2241292(self):
        
        utils=utillity.UtillityMethods(self.driver)
        core_utils=core_utility.CoreUtillityMethods(self.driver)
        chart_obj=chart.Chart(self.driver)
        g_var = Global_variables()
        Expected_tooltip_value=['Product Category:Media Player', 'Revenue:$246,073,059.36']
        group_id = core_utils.parseinitfile('group_id')
        
        
        """
        Step 1:Launch the IA API with Chart (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP251_S9164%2FG159435&tool=chart&master=baseapp/wf_retail_lite
        """
        
        chart_obj.invoke_chart_tool_using_api("baseapp/wf_retail_lite")
        chart_obj.wait_for_number_of_element(".chartPanel .risers rect",25,chart_obj.chart_long_timesleep)
 
        """
        Step 2:Select "Format" > "Chart Types" > "Line".
        """
        chart_obj.select_ia_ribbon_item('Format', 'Line')
        chart_obj.wait_for_number_of_element(".groupPanel [class='risers'] path",5,chart_obj.chart_long_timesleep)

        """
        Step 3:Double click "Revenue","Product,Category".
        The following chart is displayed.
        """
        chart_obj.double_click_on_datetree_item("Revenue",1)
        chart_obj.wait_for_visible_text("#queryTreeColumn", "Revenue", chart_obj.chart_long_timesleep)
        chart_obj.double_click_on_datetree_item("Product,Category",1)
        chart_obj.wait_for_visible_text("#queryTreeColumn", "Product,Category", chart_obj.chart_long_timesleep)
        
        """
        Step 4:Highlight "Revenue" in the Query pane.
        "Drill Down" icon (in "Links" grouping) is enabled.
        """
        chart_obj.select_field_under_query_tree("Revenue",1)
        chart_obj.wait_for_visible_text("#FieldDrillDown","Drill Down",chart_obj.chart_long_timesleep)

        """
        Step 5:Click "Drill Down" icon.
        "Drill Down - Revenue" window is displayed.
        """
        chart_obj.select_ia_ribbon_item("Field","drilldown")
        chart_obj.wait_for_visible_text("#rBtnUrl","Web Page",chart_obj.chart_long_timesleep)
        
        """
        Step 6:Select "Web Page" radio button.
        """
        """
        Step 7:Set URL = "http://www.espn.com".
        """
        """
        Step 8:Click "OK".
        """
        chart_obj.create_drilldown_report("webpage", url_value="http://www.espn.com", click_ok=True)

        """
        Step 9:Click "Run".
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()

        """Step 10:Hover over any datapoint on the Line chart.
        Marker and the tooltip is displayed.
        """
        core_utils.python_move_to_element(utils.validate_and_get_webdriver_object('#jschart_HOLD_0', 'chart'))
        time.sleep(5)
        chart_obj.select_or_verify_marker_tooltip_in_run_window("marker!s0!g3!mmarker!",verify_tooltip_list=Expected_tooltip_value,msg="Step 10",parent_css="#jschart_HOLD_0")
        
        """
        Step 11:Click on any marker.
        It launches a new browser going to ESPN homepage.
        """
        chart_obj.click_on_marker("#jschart_HOLD_0","marker!s0!g3!mmarker")
        core_utils.switch_to_new_window()
        actual_title=self.driver.title
        utils.asequal("ESPN: Serving fans. Anytime. Anywhere.",actual_title,"Step 11.1 verify the It launches a new browser going to ESPN homepage ")

        """
        Step 12:Click "IA" > "Save As" > "C2241292" > "Save".
        """

        core_utils.switch_to_previous_window()
        chart_obj.save_as_from_application_menu_item(g_var.current_test_case, group_id)
        time.sleep(3)
 
        """
        Step 13:Logout using API
        http://domain:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
        """
        Step 14:Restore the C2241292.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        """
        chart_obj.edit_fex_using_api_url(None, fex_name=g_var.current_test_case)
        chart_obj.verify_x_axis_title_in_preview(['Product Category'],msg="Step:14.1")
        chart_obj.verify_y_axis_title_in_preview(["Revenue"],msg="Step:14.2")
        chart_obj.verify_number_of_risers(".risers path", 1,1,"Step:14.3")
        
        """
        Step 15:Logout using API
        http://domain:port/alias/service/wf_security_logout.jsp
        """
        
 
if __name__ == '__main__':
    unittest.main() 




        
