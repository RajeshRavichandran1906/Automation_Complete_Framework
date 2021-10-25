'''
Created on December 26, 2018

@author: AA14564
Testcase Name : Adding pages inside the folders in V5 Portal
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262144
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools import page_designer

class C8262144_TestClass(BaseTestCase):
    
    def test_C8262144(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designobj = page_designer.Design(self.driver)
        
        """
        Test case CSS
        """
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        blank_css= "div[class*='pd-np-list ibx-widget'] [class*='pd-np-item']:nth-child(2)"
        Container_css="div[title='Containers']"
        
        """
        Test case variables
        """
        portal_name = 'V5 Personal Portal_Nav-2'
        project = core_util_obj.parseinitfile('project_id')
        group = core_util_obj.parseinitfile('group_id')
        suite = core_util_obj.parseinitfile('suite_id')
        expand_respository = '{0}_{1}->{2}'.format(project,suite,group)
        folder_one = 'Folder 1'
        folder_two = 'Folder 2'
        folder_three = 'Folder 3'
        folders_text = 'Folders'
        expected_list1=['Test page 1.1', 'Test page 1.2']
        expected_list2=['Test page 2.1', 'Test page 2.2']
        expected_list3=['Test page 3.1', 'Test page 3.2']
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User.
                Click on Content tree from side bar.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """ Step 2: Expand 'P292_S19901' domain > G514402 folder > click on V5 Personal Portal_Nav-2.
        """
        main_page_obj.expand_repository_folder('Domains->{0}->{1}'.format(expand_respository, portal_name))
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_short_timesleep)
        
        """ Step 3: Double click on Folder 1. Click Page action bar > choose blank template > click on Containers tab > drag and drop Panel container on the page canvas.
        """
        main_page_obj.right_click_folder_item_and_select_menu(folder_one,click_option='double_click')
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(blank_css, 1, 20)
        page_designobj.select_page_designer_template("Blank")
        util_obj.synchronize_with_number_of_element(Container_css, 1,15)
        page_designobj.select_option_from_carousel_items('Containers')
        page_designobj.drag_container_item_to_blank_canvas('Panel',1)
    
        """ Step 4: Click on Save button > enter title as 'Test page 1.1' > click save and close the page designer.
        """
        page_designobj.save_page_from_toolbar('Test page 1.1')
        page_designobj.close_page_designer_from_application_menu()
        time.sleep(3)
        
        """ Step 5: Click Page action bar > choose blank template > click on Containers tab > drag and drop Tab container on the page canvas.
        """
        core_util_obj.switch_to_previous_window(window_close=False)
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(blank_css, 1, 20)
        page_designobj.select_page_designer_template("Blank")
        util_obj.synchronize_with_number_of_element(Container_css, 1,15)
        page_designobj.select_option_from_carousel_items('Containers')
        page_designobj.drag_container_item_to_blank_canvas('Tab',1)
        
        """ Step 6: Click on Save button > enter title as 'Test page 1.2 ' > click save and close the page designer.
                    Verify Test page 1.1 and Test page 1.2 are created and shown in the content area.
        """
        page_designobj.save_page_from_toolbar('Test page 1.2')
        page_designobj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        main_page_obj.verify_items_in_grid_view(expected_list1,'asequal',"Step 6: Verify Test page 1.1 and Test page 1.2 are created and shown in the content area")
        
        """ Step 7: Select Folder 2 in tree. Click Page action bar > choose blank template > click on Containers tab > drag and drop Panel container on the page canvas.
        """
        main_page_obj.click_repository_folder(portal_name)
        main_page_obj.right_click_folder_item_and_select_menu(folder_two,click_option='double_click')
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(blank_css, 1, 20)
        page_designobj.select_page_designer_template("Blank")
        util_obj.synchronize_with_number_of_element(Container_css, 1,15)
        page_designobj.select_option_from_carousel_items('Containers')
        page_designobj.drag_container_item_to_blank_canvas('Panel',1)
        
        """ Step 8: Click on Save button > enter title as 'Test page 2.1' > click save and close the page designer.
        """
        page_designobj.save_page_from_toolbar('Test page 2.1')
        page_designobj.close_page_designer_from_application_menu()
        time.sleep(3)
        
        """ Step 9: Click Page action bar > choose blank template > click on Containers tab > drag and drop Carousel container on the page canvas.
        """
        core_util_obj.switch_to_previous_window(window_close=False)
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(blank_css, 1, 20)
        page_designobj.select_page_designer_template("Blank")
        util_obj.synchronize_with_number_of_element(Container_css, 1,15)
        page_designobj.select_option_from_carousel_items('Containers')
        page_designobj.drag_container_item_to_blank_canvas('Carousel',1)
        
        """ Step 10: Click on Save button > enter title as 'Test page 2.2 ' > click save and close the page designer.
                    Verify Test page 2.1 and Test page 2.2 are are created and shown in the content area.
        """
        page_designobj.save_page_from_toolbar('Test page 2.2')
        page_designobj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        main_page_obj.verify_items_in_grid_view(expected_list2,'asequal',"Step 10: Verify Test page 2.1 and Test page 2.2 are created and shown in the content area")
        
        """ Step 11: Select Folder 3 in tree. Click Page action bar > choose blank template > click on Containers tab > drag and drop Accordion container on the page canvas.
        """
        main_page_obj.click_repository_folder(portal_name)
        main_page_obj.right_click_folder_item_and_select_menu(folder_three,click_option='double_click')
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(blank_css, 1, 20)
        page_designobj.select_page_designer_template("Blank")
        util_obj.synchronize_with_number_of_element(Container_css, 1,15)
        page_designobj.select_option_from_carousel_items('Containers')
        page_designobj.drag_container_item_to_blank_canvas('Accordion',1)
        
        """ Step 12: Click on Save button > enter title as 'Test page 3.1' > click save and close the page designer.
        """
        page_designobj.save_page_from_toolbar('Test page 3.1')
        page_designobj.close_page_designer_from_application_menu()
        time.sleep(3)
        core_util_obj.switch_to_previous_window(window_close=False)
        
        """ Step 13: Click Page action bar > choose blank template > click on Containers tab > drag and drop Grid container on the page canvas.
        """
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(blank_css, 1, 20)
        page_designobj.select_page_designer_template("Blank")
        util_obj.synchronize_with_number_of_element(Container_css, 1,15)
        page_designobj.select_option_from_carousel_items('Containers')
        page_designobj.drag_container_item_to_blank_canvas('Grid',1)
        
        """ Step 14: Click on Save button > enter title as 'Test page 3.2 ' > click save and close the page designer.
                    Verify Test page 3.1 and Test page 3.2 are are created and shown in the content area.
        """
        page_designobj.save_page_from_toolbar('Test page 3.2')
        page_designobj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        main_page_obj.verify_items_in_grid_view(expected_list3,'asequal',"Step 14: Verify Test page 3.1 and Test page 3.2 are created and shown in the content area")
        
        """ Step 15: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()