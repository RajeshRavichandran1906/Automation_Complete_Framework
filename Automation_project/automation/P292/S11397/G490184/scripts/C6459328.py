'''
Created on June 24,2019

@author: Vpriya

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/11397&group_by=cases:section_id&group_id=490184&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6459328
TestCase Name = Verify that List or View Modes are remembered
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.wftools import page_designer
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C6459328_TestClass(BaseTestCase):

    def test_C6459328(self):
        
        """
        TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        content_css=wf_mainpage_locators.WfMainPageLocators.CONTENT_CSS
        content_box_css=wf_mainpage_locators.WfMainPageLocators.content_area_css
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

        
        """ Step 4: Click toggle button.
        Verify content area shows in list view.
        """
        wfmain_obj.select_list_view()
        wfmain_obj.verify_items_in_list_view(["Explorer Widget page"],"asin","Step 4.1 verify the explorer widget in list view")
        page_designer_obj.switch_to_default_page()

        """
        Step 5:Close the 'Explorer widget' page run window.
        Verify content area displayed in Grid View
        """
        wfmain_obj_run.close()
        wfmain_obj_run.switch_to_default_content()
        wfmain_obj.verify_items_in_grid_view(["Explorer Widget page"], "asin","Step 5.1 verify the explorer widget in grid view")
        
        """Step 6:Refresh browser
        Verify content area shows in list view.
        """
        self.driver.refresh()
        utillobj.synchronize_with_visble_text(content_box_css, "Explorer Widget page", wfmain_obj.chart_long_timesleep)
        wfmain_obj.verify_items_in_list_view(["Explorer Widget page"],"asin","Step 6.1 verify the explorer widget in list view")
      
        """
        Step 7:Expand 'P292_S11397' domain -> 'G490184' folder;
        Double click on 'Explorer Widget page'
        Verify still content area shows in list view.
        """
        wfmain_obj.expand_repository_folder("P292_S11397->G490183")
        utillobj.synchronize_with_visble_text(content_box_css, "Explorer Widget page", wfmain_obj.chart_long_timesleep)
        wfmain_obj.double_click_content_item_in_list_view("Explorer Widget page")
        wfmain_obj_run.switch_to_frame()
        page_designer_obj.switch_to_container_frame("Panel 1")
        
        """
        Step 8:Click toggle button.
        Verify content area is back to grid view.
        """
        wfmain_obj.select_grid_view()
        wfmain_obj.verify_items_in_grid_view(["Explorer Widget page"], "asin","Step 8.1 verify the explorer widget in grid view")
        
        """
        Step 9:Close the 'Explorer widget' page run window.
        Verify still content area shows in list view.
        """
        page_designer_obj.switch_to_default_page()
        wfmain_obj_run.close()
        wfmain_obj_run.switch_to_default_content()
        wfmain_obj.verify_items_in_list_view(["Explorer Widget page"],"asin","Step 9.1 verify the explorer widget in list view")
        
        """Step 10:Refresh the browser.
        Verify content area is changed to grid view.
        """
        self.driver.refresh()
        utillobj.synchronize_with_visble_text(content_box_css, "Explorer Widget page", wfmain_obj.chart_long_timesleep)
        wfmain_obj.verify_items_in_grid_view(["Explorer Widget page"], "asin","Step 10.1 verify the explorer widget in grid view")
        
        """
        Step 11:In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        