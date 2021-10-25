'''
Created on 4th April 2018

@author: Vpriya
Testcase Name : Create Page outside the portal
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261627
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators
from common.wftools import page_designer


class C8261627_TestClass(BaseTestCase):
    
    def test_C8261627(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        page_designer_obj=page_designer.Design(self.driver)
        
        """
        Test case CSS
        """
        page_pop_up_title_css="div[data-ibx-type='pdNewPage'] div[class*='ibx-title-bar-caption']"
        icon_css="div .pd-page-canvas .material-icons"
        
        """
        Test case variables
        """
        page_pop_up_text="New Page"
        
        """
        Step 1: Login WF as wfpenadm1/owasp!@630.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 3: Expand 'V5 Domain Testing';
        Click on v5portal1 and select Page tile from action bar
        """
        main_page_obj.expand_repository_folder('V5 Domain Testing')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css,'Page',base_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Page')
        
        """
        Step 4:From New Page dialog select InfoApp 1 template.
        """
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(page_pop_up_title_css, page_pop_up_text,base_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('InfoApp 1')
                
        """
        Step 5: Click save;
        Enter 'Page_new' and click save button
        """
        util_obj.synchronize_with_number_of_element(icon_css, 2, base_obj.home_page_medium_timesleep)
        page_designer_obj.save_as_page_from_application_menu('Page_new')
        
        """
        Step 6: Close designer
        """
        core_utill_obj.switch_to_previous_window()
        
        """
        Step 7:Right click on 'Page_new' and click Publish.
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css,'Page_new',base_obj.home_page_medium_timesleep )
        main_page_obj.right_click_folder_item_and_select_menu('Page_new','Publish')
        
        """
        Verify 'Page_new' has been published
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css,'Page_new',base_obj.home_page_medium_timesleep )
        main_page_obj.verify_content_area_item_publish_or_unpublish('Page_new', 'publish', msg="Step 07.01: Verify 'Page_new' has been published")
        
        """
        Step 8:Sign out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()