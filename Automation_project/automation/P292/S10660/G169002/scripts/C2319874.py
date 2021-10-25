"""-------------------------------------------------------------------------------------------
Created on July 19, 2019
@author: Vishnu_priya

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2319874
Test Case Title =  Test Containers tab
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools import page_designer
from common.wftools import wf_mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods


class C2319874_TestClass(BaseTestCase):

    def test_C2319874(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = page_designer.Design(self.driver)
        main_page = wf_mainpage.Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text" 
        container_css="[data-ibx-type='pdContainer']"
        
        """
            STEP 1 : Login WF as domain developer
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        utils.synchronize_with_visble_text(content_css, "Content", 60)
        
        """
            STEP 2 : Click on Content view from side bar
        """
        main_page.select_content_from_sidebar()
 
        """
            STEP 3 : Expand 'P292_S10863' domain -> 'G192932' folder;
            Click on Page action tile from under Designer category
        """
        main_page.expand_repository_folder(repository_folder)
        main_page.select_action_bar_tab("Designer")
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text("div[class^='pd-new-page']", "Blank")
 
        """
            STEP 4 : Choose blank template
            Verify that page designer opens. 
        """
        utils.verify_object_visible("div[class^='pd-new-page']",True,"Step 04: Verify that page designer opens ")
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
        
        """
        STEP 5: Click the Containers tab in the resource selector.
        """
        pd_design.select_option_from_carousel_items('Containers')
        
        """
        STEP 5:1 Verify that there is a section titled Basic Containers
        """
        sectioned_titled=utils.validate_and_get_webdriver_object(".ibx-accordion-page-button","Basic_containers_title").text
        utils.asequal(sectioned_titled,"Basic Containers","Step:05:01 Verify that there is a section titled Basic Containers")
        
        """
        STEP 6:Verify that there is a section titled Basic Containers
        Section 1 has Panel, Tab, Carousel, Accordion
        Section 2 has Grid
        """
        containers_elem=self.driver.find_elements_by_css_selector(".ibxtool-panel-basic-containers")
        Section_1_title=containers_elem[0].text.strip().replace("\n",",")
        utils.asequal(Section_1_title,'Panel,Tab,Carousel,Accordion',"Step 6: verify section1_title")
        Section_2_title=containers_elem[1].text.strip().replace("\n",",")
        utils.asin('Grid',Section_2_title,"Step 6: verify section2_title")
        
        """
        STEP 7:Drag each container type onto the page canvas next to each other.
        """
        pd_design.drag_container_item_to_blank_canvas('Panel',1)
        utils.synchronize_with_number_of_element(container_css,1,main_page.chart_long_timesleep)
        pd_design.drag_container_item_to_blank_canvas("Tab",4)
        utils.synchronize_with_number_of_element(container_css,2,main_page.chart_long_timesleep)
        pd_design.drag_container_item_to_blank_canvas("Carousel",7)
        utils.synchronize_with_number_of_element(container_css,3,main_page.chart_long_timesleep)
        pd_design.drag_container_item_to_blank_canvas("Accordion",10)
        utils.synchronize_with_number_of_element(container_css,4,main_page.chart_long_timesleep)
        
        
        """
        STEP 8:Drag the grid under the Panel 1
        Verify all containers are added without error.
        """
        pd_design.drag_basic_container_to_canvas_container("Grid","Panel 1",location='bottom_left')
        utils.synchronize_with_number_of_element(container_css,5,main_page.chart_long_timesleep)
        pd_design.verify_containers_title(['Panel 1', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5'],"Step 8:Verify all containers are added without error")

        """
        STEP 9: Close designer
        """
        pd_design.close_page_designer_without_save_page()
 
        """
        STEP 10 : Sign out WF
        """
        core_utils.switch_to_previous_window(window_close=False)
        main_page.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()