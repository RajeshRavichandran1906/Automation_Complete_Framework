'''
Created on December 11, 2018

@author: Vpriya
Testcase Name : Adding pages inside the folders in V5 Portal as developer user
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8262125
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.wftools import page_designer


class C8262125_TestClass(BaseTestCase):
    
    def test_C8262125(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        page_designobj = page_designer.Design(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        blank_css= "div[class*='pd-np-list ibx-widget'] [class*='pd-np-item']:nth-child(2)"
        Container_css="div[title='Containers']"
        expected_list1=['Test page 1.1', 'Test page 1.2']
        expected_list2=['Test page 2.1', 'Test page 2.2']
        expected_list3=['Test page 3.1', 'Test page 3.2']
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Expand 'P292_S19901' domain > G513510 folder > click on V5 Personal Portal.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, 45)
        main_page_obj.expand_repository_folder('Domains->P292_S19901->G513510->V5 Personal Portal')
        
        """
        Step 3: Double click on Folder 1. Click Page action bar > choose blank template.'.
        """
        main_page_obj.right_click_folder_item_and_select_menu('Folder 1',click_option='double_click')
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(blank_css, 1, 20)
        page_designobj.select_page_designer_template("Blank")
    
        
        """
        Step 4: Click on Containers tab > drag and drop Panel container on the page canvas.
        """
        util_obj.synchronize_with_number_of_element(Container_css, 1,15)
        page_designobj.select_option_from_carousel_items('Containers')
        page_designobj.drag_container_item_to_blank_canvas('Panel',1)
        
        """
        Step 5: Click on Save button > enter title as 'Test page 1.1' > click save and Click on application menu > Close..
        """
        page_designobj.save_page_from_toolbar('Test page 1.1')
        page_designobj.close_page_designer_from_application_menu()
        
        """
        Step 6: Click Page action bar > choose blank template..
        """
        time.sleep(3)
        core_util_obj.switch_to_previous_window(window_close=False)
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(blank_css, 1, 20)
        page_designobj.select_page_designer_template("Blank")
        
        """
        Step 7: Click on Containers tab > drag and drop Tab container on the page canvas..
        """
        util_obj.synchronize_with_number_of_element(Container_css, 1,15)
        page_designobj.select_option_from_carousel_items('Containers')
        page_designobj.drag_container_item_to_blank_canvas('Tab',1)
        
        """
        Step 8: Click on Save button > enter title as 'Test page 1.2 ' > click save and Click on application menu > Close
        Verify Test page 1.1 and Test page 1.2 are created and shown in the content area.
        """
        page_designobj.save_page_from_toolbar('Test page 1.2')
        page_designobj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        main_page_obj.verify_items_in_grid_view(expected_list1,'asequal',"Step 8: Verify Test page 1.1 and Test page 1.2 are created and shown in the content area")
        
        """
        Step 9: Double click on Folder 2. Click Page action bar > choose blank template.
        """
        main_page_obj.click_repository_folder('V5 Personal Portal')
        main_page_obj.right_click_folder_item_and_select_menu('Folder 2',click_option='double_click')
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(blank_css, 1, 20)
        page_designobj.select_page_designer_template("Blank")
        
        """
        Step 10: Click on Containers tab > drag and drop Panel container on the page canvas.
        """
        util_obj.synchronize_with_number_of_element(Container_css, 1,15)
        page_designobj.select_option_from_carousel_items('Containers')
        page_designobj.drag_container_item_to_blank_canvas('Panel',1)
        
        """
        Step 11: Click on Save button > enter title as 'Test page 2.1' > click save and Click on application menu > Close.
        """
        page_designobj.save_page_from_toolbar('Test page 2.1')
        page_designobj.close_page_designer_from_application_menu()
        
        """
        Step 12: Click Page action bar > choose blank template.
        """
        time.sleep(3)
        core_util_obj.switch_to_previous_window(window_close=False)
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(blank_css, 1, 20)
        page_designobj.select_page_designer_template("Blank")
        
        """
        Step 13: Click on Containers tab > drag and drop Carousel container on the page canvas.
        """
        util_obj.synchronize_with_number_of_element(Container_css, 1,15)
        page_designobj.select_option_from_carousel_items('Containers')
        page_designobj.drag_container_item_to_blank_canvas('Carousel',1)
        
        """
        Step 14: Click on Save button > enter title as 'Test page 2.2 ' > click save and Click on application menu > Close..
        Verify Test page 2.1 and Test page 2.2 are created and shown in the content area.
        """
        page_designobj.save_page_from_toolbar('Test page 2.2')
        page_designobj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        main_page_obj.verify_items_in_grid_view(expected_list2,'asequal',"Step 14: Verify Test page 2.1 and Test page 2.2 are created and shown in the content area")
        
        """
        Step 15: Double click on Folder 3. Click Page action bar > choose blank template.
        """
        main_page_obj.click_repository_folder('V5 Personal Portal')
        main_page_obj.right_click_folder_item_and_select_menu('Folder 3',click_option='double_click')
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(blank_css, 1, 20)
        page_designobj.select_page_designer_template("Blank")
        
        """
        Step 16: Click on Containers tab > drag and drop Accordion container on the page canvas.
        """
        util_obj.synchronize_with_number_of_element(Container_css, 1,15)
        page_designobj.select_option_from_carousel_items('Containers')
        page_designobj.drag_container_item_to_blank_canvas('Accordion',1)
        
        """
        Step 17: Click on Save button > enter title as 'Test page 3.1' > click save and Click on application menu > Close.
        """
        page_designobj.save_page_from_toolbar('Test page 3.1')
        page_designobj.close_page_designer_from_application_menu()
        
        """
        Step 18: Click Page action bar > choose blank template.
        """
        time.sleep(3)
        core_util_obj.switch_to_previous_window(window_close=False)
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(blank_css, 1, 20)
        page_designobj.select_page_designer_template("Blank")
        
        """
        Step 19: Click on Containers tab > drag and drop Grid container on the page canvas.
        """
        util_obj.synchronize_with_number_of_element(Container_css, 1,15)
        page_designobj.select_option_from_carousel_items('Containers')
        page_designobj.drag_container_item_to_blank_canvas('Grid',1)
        
        """
        Step 20: Click on Save button > enter title as 'Test page 3.2 ' > click save and Click on application menu > Close.
        Verify Test page 3.1 and Test page 3.2 are created and shown in the content area.
        """
        page_designobj.save_page_from_toolbar('Test page 3.2')
        page_designobj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        main_page_obj.verify_items_in_grid_view(expected_list3,'asequal',"Step 20:Verify Test page 3.1 and Test page 3.2 are created and shown in the content area")
        
        """
        Step 21: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()