"""-------------------------------------------------------------------------------------------
Created on July 01, 2019
@author: vpriya

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/6459313
Test Case Title =  Create,Edit and Run Portal Page
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage,Run
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
from common.locators import wf_mainpage_locators
from common.pages import wf_mainpage as main_pages
from common.wftools import report
from common.wftools import chart
from common.pages import visualization_resultarea, wf_legacymainpage, vfour_miscelaneous, vfour_portal_canvas, vfour_portal_ribbon, ia_resultarea
import time


class C6459313_TestClass(BaseTestCase):

    def test_C6459313(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        pd_design = Design(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        main_page_run = Run(self.driver)
        mainpage_obj = main_pages.Wf_Mainpage(self.driver)
        report_obj=report.Report(self.driver)
        chart_obj=chart.Chart(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        
        
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        
        """
            TESTCASE CSS
        """
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text" 
        explorer_css = "div[class^='file-item file-item-published']"
        
        def select_column(column_no):
            """
            Desc:- This function is used to slect coloumn default is middle in BIP file so updtaed in script level 
            """
            elem=portal_canvas.get_column_obj(column_no)
            utils.click_on_screen(elem, 'top_middle', click_type=0,y_offset=2)
        
        
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
            STEP 3 : Expand 'P292_S11397' domain -> 'G490183' folder;
            Double click on 'Explorer Widget page'
        """
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        pd_design.run_page_designer_by_double_click("Explorer Widget page")
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        
        """
        Step 4:Click on Portal Page action tile from under Other category;
        Verify Page Designer window opens in a new tab
        """
        main_page.select_action_bar_tab('Other')
        utils.synchronize_with_visble_text(locator_obj.content_area_css, 'Portal Page', main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option('Portal Page')
        core_utils.switch_to_new_window()
        
        """
        Step 5:Choose 2 Column;
        Enter title as 'Portal Page' and click Create
        """
        portal_canvas.add_page('2 Column',Page_title="Portal Page",page_verify=False)
        time.sleep(3)

        """
        Step 6:Select Column1 and click on Insert tab;
        Click on Resource Tree under Insert tab
        """
        portal_ribbon.select_ribbon_item("Insert", 'Insert_ResourceTree') 
        utils.synchronize_with_visble_text("[id^='BiLabel'][class*='bip-title-bar']",'Panel 1',30)
        portal_canvas.verify_panel_caption("Panel 1","Step 6.1")

        """
        Step 7:Select Column2 and click on Insert tab;
        Click on Portal List under Insert tab
        Verify contents are added to the columns as below
        """
        select_column(2)
        portal_ribbon.select_ribbon_item("Insert", 'Insert_PortalList') 
        time.sleep(30)

        """
        Step 8:Click Save;
        Click OK button
        """
        """
        step 9:Click on BIP application main menu;
        Select Exit.
        Verify 'Portal Page' is listed under 'G490183' folder as below
        """
        portal_ribbon.bip_save_and_exit("Yes")
        core_utils.switch_to_previous_window(window_close=False)
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        main_page.verify_items_in_grid_view(["Portal Page"],"asin","Step 12.1 Verify 'Report' is available under 'G490183' folder in content area as below")

        """
        Step 10:Double click on 'Portal Page'.
        Verify that the Page Designer opens in a design mode with two columns and their corresponding contents as below
        """
        pd_design.run_page_designer_by_double_click("Portal Page")
        core_utils.switch_to_new_window()
        select_column(1)
        portal_canvas.verify_panel_caption("Panel 1","Step 10.1")
        select_column(2)
        portal_canvas.verify_panel_caption("Panel 2","Step 10.1")
        
        """
        Step 11:Click on BIP application main menu;
        Select Exit.
        """
        
        time.sleep(5)
        core_utils.switch_to_previous_window()

 
        """
        Step 12:Close the 'Explorer widget' page run window
        Verify 'Portal Page' is listed under 'P292_S11397' domain -> 'G490183' folder in Home page
        """
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        pd_design.switch_to_default_page()
        main_page_run.close()
        main_page_run.switch_to_default_content()
        utils.synchronize_with_visble_text(content_css, "Content", 60)
        self.driver.refresh()
        utils.synchronize_with_visble_text(explorer_css, "Explorer",main_page.home_page_medium_timesleep)
        main_page.verify_items_in_grid_view(["Portal Page"],"asin","Step 12.1 Verify 'Portal Page' is available under 'G490183' folder in content area as below")

        
        """
        Step 13:Sign Out WF
        """
        main_page.signout_from_username_dropdown_menu()
 

 

 
if __name__ == '__main__':
    unittest.main() 