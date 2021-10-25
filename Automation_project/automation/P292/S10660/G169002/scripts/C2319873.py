"""-------------------------------------------------------------------------------------------
Created on July 23, 2019
@author: Vishnu_priya

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/2319873
Test Case Title =  Test Hover for the Resource Selector Tabs
-----------------------------------------------------------------------------------------------"""
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools import page_designer
from common.wftools import wf_mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods

class C2319873_TestClass(BaseTestCase):

    def test_C2319873(self):
        
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
            STEP 3 : Expand 'P292_S10660' domain;
            Click on 'G192932' folder and choose Page action tile from under designer category.
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
            STEP 5: Hover the Containers tab.
            Verify that you see the "Containers" tooltip
        """
        pd_design.verify_tooltip_carousel_items("Containers","Step 5: Verify that you see the 'Containers' tooltip")
       
                
        """
            STEP 6:Hover the Content tab.
            Verify that you see the "Content" tooltip
        """
        
        pd_design.verify_tooltip_carousel_items("Content", "Step 6: Verify that you see the 'Content' tooltip")
        
        """
            STEP 7:Hover the Controls tab.
            Verify that you see the "Controls" tooltip
        """
        
        pd_design.verify_tooltip_carousel_items("Controls","Step 7: Verify that you see the 'Controls' tooltip")
        
        
        """
        STEP 8: Click the Containers tab in the resource selector.
        """
        pd_design.select_option_from_carousel_items('Containers')
        
        """
        STEP 9:Click Containers tab and drag Panel, Tab, Carousel and Accordion containers onto the page canvas next to each other and drag the Grid under the Panel 1.
        """
        pd_design.drag_container_item_to_blank_canvas('Panel',1)
        utils.synchronize_with_number_of_element(container_css,1,main_page.chart_long_timesleep)
        pd_design.drag_container_item_to_blank_canvas("Tab",4)
        utils.synchronize_with_number_of_element(container_css,2,main_page.chart_long_timesleep)
        pd_design.drag_container_item_to_blank_canvas("Carousel",7)
        utils.synchronize_with_number_of_element(container_css,3,main_page.chart_long_timesleep)
        pd_design.drag_container_item_to_blank_canvas("Accordion",10)
        utils.synchronize_with_number_of_element(container_css,4,main_page.chart_long_timesleep)
        pd_design.drag_basic_container_to_canvas_container("Grid","Panel 1",location='bottom_left')
        utils.synchronize_with_number_of_element(container_css,5,main_page.chart_long_timesleep)
        pd_design.verify_containers_title(['Panel 1', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5'],"Step 8:Verify all containers are added without error")
        
        """
        STEP 10: Hover over the Maximize and Options icon in each panel
        """
        """
        STEP 10:01 Verify that you see Maximize and Options tooltips
        """
        panel_options =["Panel 1","Panel 2","Panel 3","Panel 4","Panel 5"]
        for x in panel_options:
            pd_design.verify_tooltip_for_container_options(x,"Maximize","Step 10.01 verify the {0} panel having maximize".format(x))
            pd_design.verify_tooltip_for_container_options(x,"Options","Step 10.01 verify the {0} panel having options panel".format(x))
        

        """
        STEP 11: Click the options icon in all the container.
        """
        """
        STEP 11:01 Verify that you get a message stating that "This feature is only enabled at runtime or in the preview mode."
        """
        Expected_message="This feature is only enabled at runtime or in the preview mode."
        panel_options =["Panel 1","Panel 2","Panel 3","Panel 4","Panel 5"]
        for x in panel_options:
            pd_design.click_options_verify_message(x,Expected_message,"Step 11.1:  Verify that you get a message {0} panel".format(x))
        
        time.sleep(2)
        """
        STEP 12: Close designer
        """
        pd_design.close_page_designer_without_save_page()
 
        """
        STEP 13 : Sign out WF
        """
        core_utils.switch_to_previous_window(window_close=False)
        main_page.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()