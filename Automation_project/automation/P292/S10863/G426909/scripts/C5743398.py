"""-------------------------------------------------------------------------------------------
Created on July 16, 2019

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5743398
Test Case Title =  Check Settings menu
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools import page_designer
from common.wftools import wf_mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.pages.wf_mainpage import Wf_Mainpage as main

class C5743398_TestClass(BaseTestCase):

    def test_C5743398(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = page_designer.Design(self.driver)
        main_page = wf_mainpage.Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        main_obj=main(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text" 
    
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
            STEP 3 : Expand 'P292_S10863' domain -> 'G426906' folder;
            Click on Page action tile from under Designer category
        """
        main_page.expand_repository_folder(repository_folder)
        main_page.select_action_bar_tab("Designer")
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text("div[class^='pd-new-page']", "Blank")
 
        """
            STEP 4 : Choose blank template
        """
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")

        """
        STEP 5: Drag and drop 'Category Sales' from Retail Samples -> Portal -> Small widgets to the page canvas
        """
        pd_design.select_option_from_carousel_items("Content")
        pd_design.collapse_content_folder("G426906")
        pd_design.collapse_content_folder("P292_S10863")
        pd_design.drag_content_item_to_blank_canvas("Category Sales", 1, content_folder_path="Retail Samples->Portal->Small Widgets")
        
        """
        STEP 6: Click on quick filter icon
        """
        pd_design.click_quick_filter()
        utils.synchronize_until_element_is_visible('[data-ibx-type="pdFilterPanel"]',main_page.home_page_long_timesleep)
        
        """
        STEP 7: Right click on first filter control and choose 'Edit Label' menu
        """
        pd_design.verify_filter_dropdown_is_optional("Category:", "Step 07.01 :  Verify red dotted line around it")
        pd_design.select_filter_grid_cell(1, click_on_location='middle')
        pd_design.select_filter_grid_cell(1, click_on_location='middle', click_type='right')
        
        """
            STEP 7 : Expected - Verify red dotted line around it and menu appears as below
        """

        main_obj.verify_context_menu_item(['Edit label', 'Convert', 'Settings', 'Style', 'Delete control'], msg='Step 07.02')
        
        """
            STEP 08 : Click on Settings menu
        """
        main_obj.select_context_menu_item("Settings")
        
        """
            STEP 08 - Expected : Verify properties pane opens and filter control properties appears as below
        """
        pd_design.verify_setting_tabs(['General Settings', 'Control Settings', 'Data Settings', 'Parameters'], "Step 08.01 : Verify ['General Settings', 'Control Settings', 'Data Settings', 'Parameters'] tab are displayed in setting panel")
        pd_design.verify_setting_tab_properties('General Settings', ['Type=Multiple select', 'ID=FILTERPANEL', 'Classes=', 'Tooltip=', 'Global name='], "Step 08.02 : Verify general settings properties")
        pd_design.verify_setting_tab_properties('Control Settings', ['Optional=on', 'Placeholder text=Make a selection...', 'Search=off', 'Selection controls=off'], "Step 08.03 : Verify control settings properties")
        pd_design.verify_setting_tab_properties('Data Settings', ['Show All option=on', 'Display text=All', 'Default value=_FOC_NULL'], "Step 08.04 : Verify data settings properties")
        pd_design.verify_setting_parameter_tab_properties(['PRODUCT_CATEGORY (A40V)'], "Step 08.05 : Verify parameter values in setting tab")
        
        """
            STEP 9 : Close page without saving
        """
        pd_design.close_page_designer_without_save_page()
 
        """
            STEP 10 : Sign out WF
        """
        core_utils.switch_to_previous_window(window_close=False)
        
if __name__ == '__main__':
    unittest.main()