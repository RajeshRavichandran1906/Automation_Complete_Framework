'''
Created on January 4, 2019

@author: Varun
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5832068
Testcase Name : Verify 3D Surface are displaying with surface walls
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility
from common.lib import utillity
from common.wftools import active_chart

class C5832068_TestClass(BaseTestCase):

    def test_C5832068(self):
        """
            TESTCASE Functions Object
        """
        active_chart_obj=active_chart.Active_Chart(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        """
        Test case css
        """
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
        Step 2: Execute attached 3D Surface.fex using following URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS18035&BIP_item=3D_surface.fex
        """
        active_chart_obj.run_fex_using_api_url(folder_path, '3D_Surface', mrid='mrid', mrpass='mrpass')
        
        """
        Step 3: Verify the 3D bars are displaying properly.
        Expect to see 3D Bars displaying with surface walls
        """
        active_chart_obj.verify_x_axis_label_in_run_window(x_axis_labels, parent_css=run_window_css, msg='Step 3.1: Verify the x axis labels')
        active_chart_obj.verify_y_axis_label_in_run_window(y_axis_labels, parent_css=run_window_css, msg='Step 3.2: Verify y axis labels')
        active_chart_obj.verify_z_axis_label_in_run_window(z_axis_labels, parent_css=run_window_css, msg='Step 3.3: Verify z axis labels')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window('path[class="riser!s1!g0!mbar!"]', 'pale_green', parent_css=run_window_css, attribute='fill', msg='Step 3.4: Verify the riser colour')
        active_chart_obj.verify_legends_in_run_window(z_axis_labels, parent_css=run_window_css, msg='Step 3.5: Verify the legends')
        wall_elements = util_obj.validate_and_get_webdriver_objects(wall_css, "walls")
        util_obj.verify_visible_elements(wall_elements, 9, 'Step 3.6: Verify the walls visible')
        
        """
        Step 4: Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()