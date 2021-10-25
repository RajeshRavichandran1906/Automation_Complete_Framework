'''
Created on Sep 16, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view//2062831
'''
import unittest
from common.lib import utillity
from common.lib import core_utility
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_resultarea

class C2062831_TestClass(BaseTestCase):

    def test_C2062831(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resobj= visualization_resultarea.Visualization_Resultarea(self.driver)
        
        
        """
        Step 01. Execute the attached repro - act-593.fex
        """
        utillobj.active_run_fex_api_login("act-593.fex", "S7215", 'mrid', 'mrpass')
        """Expect to see the following Active Bar Chart."""
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0_fmg", 1, active_misobj.chart_medium_timesleep)
        
        """
        Step 02: Hover over the first Bar for ENGLAND.
        Expect to see the following Tool Tips displayed, including links for
        IBI and Google at the bottom.
        """
        active_misobj.verify_active_chart_tooltip('MAINTABLE_0',"riser!s0!g0!mbar!",['COUNTRY:  ENGLAND', 'DEALER_COST:  37,853', 'Filter Chart', 'Exclude from Chart', 'IBI', 'Google'],"Step 02.01: Verify Chart tooltip")
        utillobj.verify_chart_color('MAINTABLE_0',"riser!s0!g0!mbar!",'cerulean_blue',"Step 02.02: Verify Chart color")
        x=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        y=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_0', x, y, "Step 02.03: Verify Chart XY labels")
        title=utillobj.validate_and_get_webdriver_object("#MAINTABLE_0 #MAINTABLE_wbody0_ft tbody", 'maintable').text.strip()
        utillobj.asequal(title,'DEALER_COST by COUNTRY',"Step 02.04: Verify chart title")                
        
        """
        Step 03: Click the first link at the bottom, for IBI.
        Expand the new window. 
        Expect to see the IBI home page appear in a new window.
        """
        resobj.select_default_tooltip_menu("MAINTABLE_0","riser!s0!g0!mbar", 'IBI', wait_time=0, drilldown_menu='ibi')
        core_util_obj.switch_to_new_window()
        utillobj.asin(self.driver.title,"Data and Analytics Company | ibi","Step 03.01: Verify IBI Page title")
        utillobj.asequal(self.driver.current_url,"https://www.ibi.com/","Step 03.02: Verify IBI url")
        
        """
        Step 04: Close the IBI window,
        Click the second link at the bottom, for Google.
        Expand the new window.
        """
        core_util_obj.switch_to_previous_window()
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0","riser!s0!g0!mbar", 'Google', drilldown_menu='google')
        core_util_obj.switch_to_new_window()
        utillobj.asequal(self.driver.title,"Google","Step 04.01: Verify Google Page title")
        utillobj.asequal(self.driver.current_url,"https://www.google.com/?gws_rd=ssl","Step 04.02: Verify Google url")
        core_util_obj.switch_to_previous_window()
        
            
if __name__ == '__main__':
    unittest.main() 