'''
Created on July 03, 2019.

@author: Niranjan_Das/Prasanth

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6156518
TestCase Name = Run Page In Retail samples Example
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design,Preview
from common.wftools import chart
from common.pages.ia_run import IA_Run

class C6156518_TestClass(BaseTestCase):

    def test_C6156518(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        main_page_run=wf_mainpage.Run(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        page_preview_obj=Preview(self.driver)
        chart_obj = chart.Chart(self.driver)
        ia_run_obj=IA_Run(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        repository_folder = 'Retail Samples->Portal->Advanced Features->Drill-down Target Example'
        action_tile = 'Designer'
        
        """
        Step 1: Login WF as Retail Samples domain developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 2: Expand Retail Samples -> Portal --> Advanced Features --> Drill-Down Target Example
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 3: Right click on "Drill Target Example page" and Run in new Window
        """
        main_page_obj.right_click_folder_item_and_select_menu("Drill Target Example", "Run in new window")
        
        """ 
        Step 3.01: Verify page and its panel contents appear as below
        """
        core_util_obj.switch_to_new_window()
        expected_page_heading=['Click on a Year or a Quantity Sold to See More Detailed Information']
        page_preview_obj.verify_page_heading_title(expected_page_heading, msg="Step 03.01 : Verify page heading")
        expected_visible_buttons=["Refresh"]
        page_preview_obj.verify_page_header_visible_buttons(expected_visible_buttons, msg="Step 03.02 : Verify page header visible buttons")
        expected_title_list=['1 - Summary Level Content', '3 - Details for the Selected Year and Region', '2 - Details for the Selected Year (Carousel Container)']
        page_preview_obj.verify_containers_title(expected_title_list, msg="Step 03.03 : Verify containers title")
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 4: Click 2013 in the first panel
        """
        page_designer_obj.switch_to_container_frame('1 - Summary Level Content')
        ia_run_obj.select_and_verify_drilldown_report_field("table[summary]", 1, 4)
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 4:Verify that the carousel panel changes as below
        """
        page_designer_obj.switch_to_container_frame('2 - Details for the Selected Year (Carousel Container)')
        chart_obj.verify_chart_title("2013 Monthly Shipments by Region", 'run', msg="Step 04.01 : Verify chart title")
        chart_obj.verify_y_axis_title_in_run_window(['Quantity Sold'],msg="Step 04.02")
        chart_obj.verify_x_axis_label_in_run_window(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], msg="Step 04.03")
        chart_obj.verify_y_axis_label_in_run_window(['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K'], msg="Step 04.04")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 g[class*='riser'] rect", 3, 12, msg="Step 04.05")
        chart_obj.verify_legends_in_run_window(['EMEA', 'North America', 'South America'], parent_css="#jschart_HOLD_0", msg="Step 04.06")
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 5:Click on the second slide
        """
        slide_2=util_obj.validate_and_get_webdriver_object(".grid-stack-item-content div[title='Go to slide 2 of 2']", "second slide")
        core_util_obj.left_click(slide_2)
        
        """ 
        Step 5.01:Verify slide2 and its content appears as below
        """
        page_designer_obj.switch_to_container_frame('2 - Details for the Selected Year (Carousel Container)',frame_index=2)
        chart_obj.verify_chart_title("2013 Monthly Sales by Region", 'run', msg="Step 05.01 : Verify chart title")
        chart_obj.verify_y_axis_title_in_run_window(['Revenue'],msg="Step 05.02")
        chart_obj.verify_x_axis_label_in_run_window(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], msg="Step 05.03")
        chart_obj.verify_y_axis_label_in_run_window(['0', '2M', '4M', '6M', '8M', '10M'], msg="Step 05.04")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 g[class*='riser'] path", 1, 3, msg="Step 05.05")
        chart_obj.verify_legends_in_run_window(['EMEA', 'North America', 'South America'], parent_css="#jschart_HOLD_0", msg="Step 05.06")
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 6: Click on 61,246 under North America in first panel
        """
        page_designer_obj.switch_to_container_frame('1 - Summary Level Content')
        ia_run_obj.select_and_verify_drilldown_report_field("table[summary]", 4, 3)
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 6.01: Verify that the third panel changes as below
        """
        page_designer_obj.switch_to_container_frame('3 - Details for the Selected Year and Region')
        util_obj.synchronize_until_element_is_visible("div[id*='jschart_HOLD_0_com-esri-ma'] circle",page_designer_obj.home_page_medium_timesleep)
        chart_obj.verify_number_of_risers("div[id*='jschart_HOLD_0_com-esri-ma'] circle", 1, 80, msg="Step 06.01")
        chart_obj.verify_legends_in_run_window(['Gross Profit', '0K', '198.5K', '396.9K', '595.3K', '793.7K', 'Quantity Sold', '9,286', '4,643.5', '1'], parent_css="#jschart_HOLD_0", msg="Step 05.06")
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 7: Close page
        """
        page_designer_obj.switch_to_previous_window()
        
        """ 
        Step 8: Signout WF
        """
if __name__ == '__main__':
    unittest.main()



        