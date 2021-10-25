'''
Created on May 20, 2019

@author: varun
Testcase Name : Verify filters can be added to filter toolbar
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261860
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.locators.designer_chart_locators import DesignerChart as dc_locators
from common.pages import designer_metadata
from common.lib import core_utility
from common.lib import utillity

class C8261860_TestClass(BaseTestCase):
    
    def test_C8261860(self):
        """
        Test case objects
        """
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        designer_meta_obj = designer_metadata.Designer_Metadata(self.driver)
        
        """
        Step 1: Launch the API to create new Designer Chart with the CAR file
        http://machine:port/ibi_apps/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%
        2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api('baseapp/wf_retail_lite')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        
        """
        Step 2: Click on Variables tab
        """
        designer_chart_obj.select_fields_or_variables_in_datapane('Variables')
        
        """
        Step 3: Expand Filters and Variables, drag Accessories to the Filter toolbar
        """
        designer_chart_obj.drag_variables_to_filter_bar('Filters and Variables->Accessories')
        designer_chart_obj.verify_filter_shelf([['Accessories','All']], "Step 3.1: Verify the filter bucket")
        
        """
        Step 4: Drag Web Store to the Filter toolbar
        """
        designer_chart_obj.drag_variables_to_filter_bar('Web Store')
        designer_chart_obj.verify_filter_shelf([['Accessories','All'], ['Web Store','All']], "Step 4.1: Verify the filter bucket")
        
        """
        Step 5: Try to drag from the Filters and Variables Store Name to a bucket, this should show a red circle with a line through when hovering over the buckets to drop it into
        """
        source_obj = designer_meta_obj.get_recursive_tree_object(['Store Name'], dc_locators.VARIABLES_CSS, 0)
        source_axis = core_util_obj.get_web_element_coordinate(source_obj)
        target_obj = util_obj.validate_and_get_webdriver_object("rect.eventCatcher", 'rect')
        target_axis = core_util_obj.get_web_element_coordinate(target_obj, yoffset=-200)
        designer_chart_obj.verify_drag_drop_with_warning_logo(source_axis['x'], source_axis['y'], target_axis['x'], target_axis['y'], target_obj, 'Step 5.1: Verify warning logo is visible')
        
        """
        Step 6: Click Application menu > Close > click No.
        """
        designer_chart_obj.close_designer_chart_from_application_menu()
        
        """
        Step 7: Sign out using API:
        http://machine:port/alias/service/wf_security_logout.jsp.
        """

        
if __name__ == '__main__':
    unittest.main()