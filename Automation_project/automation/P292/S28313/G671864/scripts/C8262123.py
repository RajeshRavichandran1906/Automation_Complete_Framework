'''
Created on Dec 4, 2018

@author: Vpriya
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8262123
Testcase Name : Adding base pages in V5 Portal as developer user
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage,page_designer
from common.lib import utillity,core_utility

class C8262123_TestClass(BaseTestCase):
    
    def test_C8262123(self):
        """
        CLASS OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        page_designer_obj=page_designer.Design(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        
        """
        TESTCASE VARIBALE
        """
        folder_path='Domains->P292_S19901->G513510->V5 Personal Portal'
        
        """
        CSS
        """
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        blank_css= "div[class*='pd-np-list ibx-widget'] [class*='pd-np-item']:nth-child(2)"
        page_box_css="[class*='pd-page-section-grid']:nth-child(60)"
        properties_css="div[title='Properties']"
        toggle_css="div[class*='ibx-accordion-page ibx-accordion-page']"
        plus_icon_css="div[class*='ibx-label-glyph ibx-label-icon fa fa-plus-circle']"
        lock_Content_css="div[class*='pd-ps-value pd-ps-es-lock-content ibx-can-toggle '] [class*='ibx-switch-slider round']"
        
        """
            Step 1: Sign into WebFOCUS Home Page as Developers User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
 
        """
            Step 2: Expand 'P292_S19901' domain > G513510 folder > click on V5 Personal Portal.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, 45)
        main_page_obj.expand_repository_folder(folder_path)
        
        
        """
            Step 3: Click on page action bar > Choose blank template.
        """
        main_page_obj.select_action_bar_tabs_option("Page")
        core_utility_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(blank_css, 1, 20)
        page_designer_obj.select_page_designer_template("Blank")
        util_obj.synchronize_with_number_of_element(page_box_css, 1, 25)
        """
            Step 4: Click on Containers tab > drag and drop Panel container on the page canvas.
        """
        page_designer_obj.select_option_from_carousel_items('Containers')
        page_designer_obj.drag_container_item_to_blank_canvas('Panel',1)
        """
            Step 5: From the designer toolbar, click on Properties > toggle off lock content..
            Verify Panel 1 have a + sign inside
        """
        util_obj.synchronize_with_number_of_element(properties_css, 1, 20)
        page_designer_obj.click_property()
        util_obj.synchronize_with_number_of_element(toggle_css, 1,5)
        lock_elem=util_obj.validate_and_get_webdriver_object(lock_Content_css, "lock toggle css")
        core_utility_obj.python_left_click(lock_elem)
        util_obj.synchronize_with_number_of_element(plus_icon_css,1,10)
        page_designer_obj.verify_panel_add_content_displayed_in_container('Panel 1','Step 5')
        page_designer_obj.verify_panel_add_content_color_in_container('Panel 1', 'gainsboro', "step 5.1")
        
        
        """
            Step 6: Click on Save button > enter title as 'Base Page 1' > click save.
        """
        page_designer_obj.save_page_from_toolbar('Base Page 1')
        
        """
            Step 7: Click on application menu > Close..
        """
        page_designer_obj.close_page_designer_from_application_menu()
        
        """
            Step 8: Click on page action bar > Choose blank template...
        """
        core_utility_obj.switch_to_previous_window(window_close=False)
        main_page_obj.expand_repository_folder(folder_path)
        main_page_obj.select_action_bar_tabs_option("Page")
        core_utility_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(blank_css, 1, 20)
        page_designer_obj.select_page_designer_template("Blank")
        util_obj.synchronize_with_number_of_element(page_box_css, 1, 25)
        
        """
           Step 9: Click on Containers tab > drag and drop tab container on the page canvas
        """
        page_designer_obj.select_option_from_carousel_items('Containers')
        page_designer_obj.drag_container_item_to_blank_canvas('Tab',1)
        
        """
           Step 10: From the designer toolbar, click on Properties > toggle off lock content.
           Verify Panel 1 have a + sign inside
        """
        util_obj.synchronize_with_number_of_element(properties_css, 1, 20)
        page_designer_obj.click_property()
        util_obj.synchronize_with_number_of_element(toggle_css, 1,5)
        lock_elem=util_obj.validate_and_get_webdriver_object(lock_Content_css, "lock toggle css")
        core_utility_obj.python_left_click(lock_elem)
        util_obj.synchronize_with_number_of_element(plus_icon_css,1,10)
        page_designer_obj.verify_panel_add_content_displayed_in_container('Panel 1','Step 10')
        page_designer_obj.verify_panel_add_content_color_in_container('Panel 1', 'gainsboro', "step 10.1")
        
        """
           Step 11: Click on Save button > enter title as 'Base Page 2' > click save.
        """
        page_designer_obj.save_page_from_toolbar('Base Page 2')
        
        """
            Step 12: Click on application menu > Close..
        """
        page_designer_obj.close_page_designer_from_application_menu()
        
        """
            Step 13: Click on page action bar > Choose blank template...
        """
        core_utility_obj.switch_to_previous_window(window_close=False)
        main_page_obj.expand_repository_folder(folder_path)
        main_page_obj.select_action_bar_tabs_option("Page")
        core_utility_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(blank_css, 1, 20)
        page_designer_obj.select_page_designer_template("Blank")
        util_obj.synchronize_with_number_of_element(page_box_css, 1, 25)
        
        """
           Step 14: Click on Containers tab > drag and drop tab container on the page canvas
           From the designer toolbar, click on Properties > toggle off lock content.
           Verify Panel 1 have a + sign inside
        """
        page_designer_obj.select_option_from_carousel_items('Containers')
        page_designer_obj.drag_container_item_to_blank_canvas('Carousel',1)
        util_obj.synchronize_with_number_of_element(properties_css, 1, 20)
        page_designer_obj.click_property()
        util_obj.synchronize_with_number_of_element(toggle_css, 1,5)
        lock_elem=util_obj.validate_and_get_webdriver_object(lock_Content_css, "lock toggle css")
        core_utility_obj.python_left_click(lock_elem)
        util_obj.synchronize_with_number_of_element(plus_icon_css,1,10)
        page_designer_obj.verify_panel_add_content_displayed_in_container('Panel 1','Step 14')
        page_designer_obj.verify_panel_add_content_color_in_container('Panel 1', 'gainsboro', "step 14.1")
        
        """
            Step 15: Click on Save button > enter title as 'Base Page 3' > click save.
        """
        page_designer_obj.save_page_from_toolbar('Base Page 3')
        
        """
            Step 16: Click on application menu > Close..
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_utility_obj.switch_to_previous_window(window_close=False)
        main_page_obj.verify_items_in_grid_view(["Base Page 1","Base Page 2","Base Page 3"],"asin","Step 16:Verify Base Page1,2 and 3 are shown in the content area.")
        
        """
            Step 17: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
                
if __name__ == "__main__":
    unittest.main()