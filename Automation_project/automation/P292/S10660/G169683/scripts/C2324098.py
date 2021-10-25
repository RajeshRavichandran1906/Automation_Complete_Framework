'''
Created on July 25, 2019

@author: Vpriya
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer
from common.wftools import wf_mainpage
from common.wftools.login import Login
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods


class C2324098_TestClass(BaseTestCase):

    def test_C2324098(self):
        
        """
        Testclass objects
        """
        login = Login(self.driver)
        pd_design = page_designer.Design(self.driver)
        main_page = wf_mainpage.Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text" 
        
        """
        Step 1:Login WF as domain developer;
        Click on Content view from side bar.
        """
        login.invoke_home_page('mrid', 'mrpass')
        utils.synchronize_with_visble_text(content_css, "Content", 60)
        
          
        """
        Step 2:Expand 'P292_S10660' domain;
        Click on 'G192933' folder and choose Page action tile from designer category.
        """
        main_page.select_content_from_sidebar()
        main_page.expand_repository_folder(repository_folder)
        main_page.select_action_bar_tab("Designer")
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text("div[class^='pd-new-page']", "Blank")
        
         
        """
        Step 3:Create a page with InfoApp 1 template.
        Verify Page 1 is displayed in the canvas selector.
        """
        
        utils.verify_object_visible("div[class^='pd-new-page']",True,"Step 04: Verify that page designer opens ")
        pd_design.select_page_designer_template("InfoApp 1")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
        
        
        """
        Step 4:Click on "G192933 > P292_S10660" domain to two level up;
        Navigate to Retail samples --> Portal --> Small Widgets folder.
        """
        """
        Step 5:Drag and drop Category Sales report on to the container.
        """

        pd_design.select_option_from_carousel_items("Content")
        pd_design.collapse_content_folder(group_id)
        pd_design.collapse_content_folder("{0}_{1}".format(project_id,suite_id))
        pd_design.drag_content_item_to_blank_canvas("Category Sales", 1,"Retail Samples->Portal->Small Widgets")
        utils.synchronize_until_element_is_visible("[title='Quick filter']",main_page.chart_long_timesleep)
         
        """
        Step 6:Click the toolbar icon and click Save.
        """
        """
        Step 7:Enter "C2324098" in Title and click Save.
        Verify that the Page 1 is now replaced with the new title
        """
        pd_design.save_as_page_from_application_menu("C2324098")
        pd_design.verify_page_tab_groups(['C2324098'],"Step 07.1")
        
        """
        Step 8:Click the toolbar icon and click Save as...
        Verify the new title visible in Title and Name box.
        """
        pd_design.select_option_from_application_menu("Save as...")
        main_page.verify_new_folder_title_value("C2324098","8")
         
        """
        Step 9:Enter "C2324098 New" in Title and click Save as.
        Verify the new title "C2324098 New" visible in the canvas selector.
        """
        
        main_page.click_button_on_popup_dialog("Cancel")
        pd_design.save_as_page_from_application_menu("C2324098 New")
        pd_design.verify_page_tab_groups(['C2324098 New'],"Step 09.1")
        
        """
        Step 10:Click the toolbar icon and click Open.
        """
        pd_design.select_option_from_application_menu("Open...")
        main_page.select_file_or_folder_from_resource_dialog("C2324098 New",view_type='grid_view')
        main_page.click_button_on_popup_dialog('Open')
        utils.synchronize_until_element_is_visible(".wb-page-tab-button",main_page.chart_long_timesleep)
        
 
        """
        Step 11:Select "C2324098" page and click Open.
        Verify "C2324098" is visible in the canvas selector.
        """
        pd_design.verify_page_tab_groups(['C2324098 New'],"Step:11.01")
        
        """
        Step 12:Close the page
        """ 
        """
        Step 13:Sign out WF.
        """
        core_utils.switch_to_previous_window()
        main_page.signout_from_username_dropdown_menu()

 
        
    
if __name__ == "__main__" :
    unittest.main()