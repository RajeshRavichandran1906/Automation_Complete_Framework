'''
Created on January 4, 2019

@author: Varun
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5832067
Testcase Name : Verify 3D Connected Series Area are displaying with surface walls
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility
from common.lib import utillity
from common.wftools import active_chart
from selenium.webdriver.support.color import Color

class C5832067_TestClass(BaseTestCase):

    def test_C5832067(self):
        """
            TESTCASE Functions Object
        """
        active_chart_obj=active_chart.Active_Chart(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        """
        Test case css
        """
        blue_riser_css = "#MAINTABLE_wbody0_f path[class=\"riser!s0!g0!mbar!\"]"
        green_riser_css = "#MAINTABLE_wbody0_f path[class=\"riser!s1!g0!mbar!\"]"
        run_window_css = "#MAINTABLE_wbody0_f"
        wall_css = "#MAINTABLE_wbody0_f g  g  path[d]:first-child"
        
        """
        Test case variables
        """
        project = core_util_obj.parseinitfile('project_id')
        group = core_util_obj.parseinitfile('group_id')
        suite = core_util_obj.parseinitfile('suite_id')
        folder_path = '{0}_{1}/{2}'.format(project,suite,group)
        x_axis_labels = ['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        y_axis_labels = ['0', '2,000,000', '4,000,000', '6,000,000', '8,000,000', '10,000,000', '12,000,000']
        z_axis_labels = ['Dollar Sales', 'Unit Sales']
        
        """
        Step 1: Sign in to Webfocus
        http://machine:port/{alias}
        Step 2: Execute attached 3D Connected Series Area.fex using following URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS18035&BIP_item=3D_Connected_Series_Area.fex
        """
        active_chart_obj.run_fex_using_api_url(folder_path, '3D_Connected_Series_Area', mrid='mrid', mrpass='mrpass')
        
        """
        Step 3: Verify the 3D bars are displaying properly.
        Expect to see 3D Bars displaying with surface walls
        """
        active_chart_obj.verify_x_axis_label_in_run_window(x_axis_labels, parent_css=run_window_css, msg='Step 3.1: Verify the x axis labels')
        active_chart_obj.verify_y_axis_label_in_run_window(y_axis_labels, parent_css=run_window_css, msg='Step 3.2: Verify y axis labels')
        active_chart_obj.verify_z_axis_label_in_run_window(z_axis_labels, parent_css=run_window_css, msg='Step 3.3: Verify z axis labels')
        blue_risers = util_obj.validate_and_get_webdriver_objects(blue_riser_css, 'blue-riser')
        actual_color = Color.from_string(util_obj.get_element_css_propery(blue_risers[-1], 'fill')).rgba
        expected_color = util_obj.color_picker('bar_blue', 'rgba')
        util_obj.asequal(actual_color, expected_color, 'Step 3.4: Verify the blue coloured riser')
        green_risers = util_obj.validate_and_get_webdriver_objects(green_riser_css, 'green-riser')
        actual_color = Color.from_string(util_obj.get_element_css_propery(green_risers[-1], 'fill')).rgba
        expected_color = util_obj.color_picker('pale_green', 'rgba')
        util_obj.asequal( actual_color, expected_color, 'Step 3.5: Verify the green coloured riser')
        active_chart_obj.verify_legends_in_run_window(z_axis_labels, parent_css=run_window_css, msg='Step 3.6: Verify the legends')
        wall_elements = util_obj.validate_and_get_webdriver_objects(wall_css, "walls")
        util_obj.verify_visible_elements(wall_elements, 10, 'Step 3.7: Verify the walls visible')
        
        """
        Step 4: Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()