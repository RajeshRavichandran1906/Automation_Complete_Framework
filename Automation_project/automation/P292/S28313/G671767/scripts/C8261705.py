"""-----------------------------------------------------------------
Author : Prabhakaran
Automate : 09-August-2019
-----------------------------------------------------------------"""

from common.wftools.login import Login
from common.wftools import designer_portal
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.core_utility import CoreUtillityMethods
import time

class C8261705_TestClass(BaseTestCase):
    
    def test_C8261705(self):
        
        """
        CLASS OBJECTS
        """
        loginpage = Login(self.driver)
        homepage =  Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        coreutils = CoreUtillityMethods(self.driver)
        portal = designer_portal.Two_Level_Side(self.driver)
        page_template = designer_portal.New_Page_Template_Window(self.driver)
        
        """
            STEP 01 : Sign in to WebFOCUS as Admin user
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        time.sleep(15) #this is required for giving time to load
        utils.wait_for_page_loads(homepage.home_page_long_timesleep)
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text(".toolbar", "Workspaces", homepage.home_page_short_timesleep)
        
        """
            STEP 02 : Expand the domain from the tree and click on 'P292_S19901_G520454'
        """
        homepage.expand_repository_folder("P292_S19901_G520454")
        
        """
            STEP 03 : Right click on 'V5 Portal Share' > Run
        """
        homepage.select_repository_folder_context_menu("V5 Portal Share", "Run")
        coreutils.switch_to_new_window()
        utils.synchronize_with_visble_text(".pvd-portal-title", "V5 Portal Share", homepage.home_page_medium_timesleep)
        
        """
            STEP 04 : Click on + Sign from the sidebar
            Verify 'New Page' dialog appears with 'Link to an existing page' and 'four templates'
        """
        portal.click_on_plus_icon_under_the_folder_in_left_sidebar("My Pages")
        utils.synchronize_with_visble_text(".pop-top", "New Page", homepage.home_page_short_timesleep)
        
        """
            STEP 05 : Select 'Link to an existing page'
            Verify Selection browser window opens
        """
        page_template.click_on_link_to_an_existing_page_button()
        utils.synchronize_with_visble_text(".pop-top", "Select", homepage.home_page_short_timesleep)
        
        """
            STEP 06 : Navigate to Retail Samples domain > InfoApps folder > select 'Sales Dashboard (Filtered)' page > Click on Select button
            Verify 'Sales Dashboard (Filtere...' appear in the sidebar and 'Retail Sales Dashboard' appear as a title in the canvas.
            Also, verify that it does not display share icon in the personal page toolbar
        """
        homepage.resource_dialog().click_crumb_item("Workspaces")
        homepage.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->InfoApps", "Sales Dashboard (Filtered)")
        homepage.resource_dialog().click_button("Select")
        utils.synchronize_with_visble_text(".pd-page-title", "Retail Sales Dashboard", homepage.home_page_long_timesleep)
        utils.synchronize_until_element_is_visible("div[title='Show filters']", homepage.home_page_long_timesleep)
        portal.verify_page_header_all_buttons(['Refresh', 'Show filters', 'Delete'], "Step 06.01 : Verify page header icons")
        
        """
            STEP 07 : Close the portal run window
        """
        coreutils.switch_to_previous_window()
        
        """
            STEP 08 : In the banner link, click on the top right username > Click Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()