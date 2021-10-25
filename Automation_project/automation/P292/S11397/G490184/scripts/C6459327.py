'''
Created on June 24,2019

@author: Vpriya

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/11397&group_by=cases:section_id&group_id=490184&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6459327
TestCase Name = Verify that Favorites Side View is remembered
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.wftools import page_designer
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C6459327_TestClass(BaseTestCase):

    def test_C6459327(self):
        
        """
        TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        content_css=wf_mainpage_locators.WfMainPageLocators.CONTENT_CSS
        page_designer_obj=page_designer.Design(self.driver)
        wfmain_obj_run=wf_mainpage.Run(self.driver)
        
        """ Step 1: Login WF as domain developer
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_visble_text(content_css, "Content", 60)
        
        """Step 2: Click on Content tree from side bar
        """
        wfmain_obj.select_content_from_sidebar()
        
        """
        Step 3:Expand 'P292_S11397' domain -> 'G490184' folder;
        Double click on 'Explorer Widget page'
        """
        wfmain_obj.expand_repository_folder("P292_S11397->G490183")
        page_designer_obj.run_page_designer_by_double_click("Explorer Widget page")
        wfmain_obj_run.switch_to_frame()
        page_designer_obj.switch_to_container_frame("Panel 1")

        
        """ Step 4: Expand Retail Samples -> Reports;
        Right click on "Quantity Sold By Stores" and select 'Add to Favorites'
        Verify Favorite added popup opens with a transparent green background layer as below
        """
        wfmain_obj.right_click_folder_item_and_select_menu("Quantity Sold By Stores", 'Add to Favorites',"Retail Samples->Reports")
        wfmain_obj.verify_favorites_notify_popup("Step:4")
        
        
        """
        Step 5:Click on Favorites view from the sidebar.
        Verify 'Quantity Sold By Stores' is displayed in the Favorites view as below
        """
        wfmain_obj.select_favorites_from_sidebar()
        wfmain_obj.verify_items_in_grid_view(["Quantity Sold By Stores"], "asin","Step 5.1")
        page_designer_obj.switch_to_default_page()

        """
        Step 6:Close the 'Explorer widget' page run window.
        Verify by default Content View is selected and NOT Favorites View.
        """
        wfmain_obj_run.close()
        utillobj.synchronize_until_element_is_visible(".left-main-panel-content-button-active[title*='Content view']",wfmain_obj.chart_long_timesleep)
        utillobj.verify_object_visible(".left-main-panel-content-button-active[title*='Content view']", True,"Step 6.1 verify the object is visible")
        
        """Step 7:Refresh browser
        Verify Favorites view appears and 'Quantity Sold By Stores' is available as a favorite
        """
        self.driver.refresh()
        utillobj.synchronize_until_element_is_visible(".left-main-panel-content-button-active[title*='Favorites view']",wfmain_obj.chart_long_timesleep)
        utillobj.verify_object_visible(".left-main-panel-content-button-active[title*='Favorites view']", True,"Step 7.1 verify the object is visible")
        wfmain_obj.verify_items_in_grid_view(["Quantity Sold By Stores"], "asin","Step 5.1")
        
        """Step 8:Click on Content view from side bar
        """
        wfmain_obj.select_content_from_sidebar()
        
        """
        Step 9:Expand 'P292_S11397' domain -> 'G490184' folder;
        Double click on 'Explorer Widget page'
        Verify Content View is selected and NOT Favorites View.
        """
        wfmain_obj.expand_repository_folder("P292_S11397->G490183")
        page_designer_obj.run_page_designer_by_double_click("Explorer Widget page")
        wfmain_obj_run.switch_to_frame()
        page_designer_obj.switch_to_container_frame("Panel 1")
        utillobj.verify_object_visible(".left-main-panel-content-button-active[title*='Content view']", True,"Step 9.1 verify the object is visible")
        
        """
        Step 10:Close the 'Explorer widget' page run window.
        """
        page_designer_obj.switch_to_default_page()
        wfmain_obj_run.close()
        wfmain_obj_run.switch_to_default_content()
        
        """
        Step 11:In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        