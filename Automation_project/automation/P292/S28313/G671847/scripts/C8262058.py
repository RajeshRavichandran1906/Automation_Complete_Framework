'''
Created on May 11, 2019

@author: varun
Test case Name : Test ESC keyboard
Test case ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262058
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import page_designer
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.locators import wf_mainpage_locators
import sys
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard as kb


class C8262058_TestClass(BaseTestCase):
    
    def test_C8262058(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        pd_obj = page_designer.Design(self.driver)
        pd_preview = page_designer.Preview(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        Test case CSS
        """
        pop_up_dialog_css = ".pop-top"
        page_designer_content_tab_css = "[class*='pd-content-tab-pag'].tpg-selected .ibx-accordion-page-button"
        
        """
        Test case variables
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        
        """
        Step 1: Login WF as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on Content View from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder('Domains')
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on 'P292_S28313' domain -> G671847 folder
        """
        main_page_obj.click_repository_folder('{0}_{1}->{2}'.format(project_id, suite_id, group_id))
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on Page action tile from under Designer category
        """
        main_page_obj.select_action_bar_tab('Designer')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Page', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Page')
        
        """
        Step 5: Choose 'Grid 2-1' template
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(pop_up_dialog_css, 'Grid 2-1', main_page_obj.home_page_medium_timesleep)
        pd_obj.select_page_designer_template('Grid 2-1')
        util_obj.synchronize_until_element_is_visible(page_designer_content_tab_css, main_page_obj.home_page_medium_timesleep)

        """
        Step 6: Click Preview button
        Verify preview mode appears
        """
        pd_obj.click_preview()
        pd_preview.verify_preview_is_displayed('Step 06.01 : Verify preview window is display')
        pd_preview.verify_page_heading_title(['Page Heading'], 'Step 06.01 : Verify page heading')
        pd_preview.verify_page_header_visible_buttons(['Refresh'], 'Step 06.03 : Verify Refresh and Filter buttons are display on page header in preview')
        pd_preview.verify_containers_title(['Panel 1', 'Panel 2', 'Panel 3'], 'Step 06.04 : Verify {0} containers display in preview'.format('panels'))
        
        """
        Step 7: Click keyboard ESC key
        Verify user is back in design mode
        """
        if sys.platform == 'linux':
            pykeyboard.tap_key(pykeyboard.escape_key)
        else:
            kb.send('esc')
        pd_obj.verify_containers_title(['Panel 1', 'Panel 2', 'Panel 3'], "Step 07.01: Verify panels in the design mode")
        
        """
        Step 8: Drag and drop 'Margin by Product category' from under Retail Samples -> Report to the panel 1
        """
        pd_obj.collapse_content_folder('G671847->P292_S28313')
        pd_obj.drag_content_item_to_container('Margin by Product Category', 'Panel 1', content_folder_path='Retail Samples->Reports')
        
        """
        Step 9: Click preview button
        Verify preview mode appears;
        Verify 'Margin by Product category' appears in Panel1
        """
        pd_obj.click_preview()
        pd_preview.verify_preview_is_displayed('Step 09.01 : Verify preview window is display')
        pd_preview.verify_page_heading_title(['Page Heading'], 'Step 09.01 : Verify page heading')
        pd_preview.verify_page_header_visible_buttons(['Refresh'], 'Step 09.03 : Verify Refresh and Filter buttons are display on page header in preview')
        pd_preview.verify_number_of_panels(3, 'Step 09.04 : Verify {0} panel display in preview'.format(3))
        pd_preview.verify_containers_title(['Margin by Product Category', 'Panel 2', 'Panel 3'], 'Step 09.05 : Verify Panel 1 has been replaced')
                                           
        """
        Step 10: Click keyboard ESC key
        Verify user is back in design mode
        """
        if sys.platform == 'linux':
            pykeyboard.tap_key(pykeyboard.escape_key)
        else:
            kb.send('esc')
        pd_obj.verify_containers_title(['Margin by Product Category', 'Panel 2', 'Panel 3'], "Step 10.01: Verify panels in the design mode")
        
        """
        Step 11: Save page as 'PD-1108' and close designer
        """
        pd_obj.save_page_from_toolbar('PD-1108')
        pd_obj.close_page_designer_from_application_menu()
        
        """
        Step 12: Signout WF
        """
        
if __name__ == '__main__':
    unittest.main()