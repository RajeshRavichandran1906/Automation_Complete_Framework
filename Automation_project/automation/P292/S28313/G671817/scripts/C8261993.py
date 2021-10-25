'''
Created on May 20, 2019

@author: vpriya
Testcase Name : Undo/Redo work after adding a filter to the Filter Shelf
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261993
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.locators import designer_chart_locators
from common.lib import core_utility
from common.lib import utillity
import time

class C8261993_TestClass(BaseTestCase):
    
    def test_C8261993(self):
        """
        Test case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        designer_chart_loc_obj=designer_chart_locators.DesignerChart()
        utill_obj=utillity.UtillityMethods(self.driver)
        
        """
        Testcase Objects
        """
        
        Filter_css="[class^='new-filter-field']"
        
    
        """
        Step 1: Launch the API to create new Designer Chart with the CAR file
        http://machine:port/ibi_apps/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%
        2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api('ibisamp/car')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        
        """
        Step 2:Drag and drop "Country" to Filter shelf.
        """
        designer_chart_obj.drag_data_field_from_dimensions_to_filter_pane('COUNTRY')
        utill_obj.synchronize_with_visble_text(Filter_css, 'COUNTRY', designer_chart_obj.chart_long_timesleep)
        
        """
        Step 3:Click outside of the canvas.
        
        Undo button is enabled under toolbar.
        """

        spacer_elem=utill_obj.validate_and_get_webdriver_object(designer_chart_loc_obj.SPACER_CSS,"outside the canvas")
        core_utility_obj.python_left_click(spacer_elem)
        designer_chart_obj.verify_toolbar_item_enabled_disabled("undo", "Step 3", disabled="false")
 
        

        """
        Step 4:Click "Undo"
        Filter is removed from filter shelf.
        """
        designer_chart_obj.click_toolbar_item('undo')
        filter_pill_css=designer_chart_loc_obj.FILTER_BAR + " .filter-pill"
        utill_obj.synchronize_until_element_disappear(filter_pill_css,designer_chart_obj.chart_long_timesleep)
        designer_chart_obj.verify_filter_shelf([], "Step 4:verify filter shelf is empty")
        
        """
        Step 5:Click "Redo"
        Filter is added again under Filter shelf.
        """
        designer_chart_obj.click_toolbar_item('redo')
        utill_obj.synchronize_until_element_is_visible(designer_chart_loc_obj.FILTER_BAR + " .filter-pill",designer_chart_obj.chart_long_timesleep)
        designer_chart_obj.verify_filter_shelf([['COUNTRY','All']], "Step 4:verify filter shelf is empty")


        """
        Step 6:Click Application menu > Close > Click No button.        
        """
        designer_chart_obj.close_designer_chart_from_application_menu()
        
        """
        Step 7:Logout using API:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp.
        """
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()