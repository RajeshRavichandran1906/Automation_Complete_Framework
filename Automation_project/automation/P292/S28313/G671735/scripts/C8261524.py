'''
Created on Nov 8, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261524
Testcase Name : Create Portal
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.wftools import designer_portal
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261524_TestClass(BaseTestCase):

    def test_C8261524(self):
        """
        TESTCASE VARIABLES
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        portal_obj=designer_portal.Portal(self.driver)
         
        folder_name='P292_S19901'
        group_name='G513445'
        title_name='Portal for Context Menu Testing1'
        
        """
        Step 1:Sign into WebFOCUS Home Page as Admin User
        
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        time.sleep(5)
        main_page_obj.select_content_from_sidebar()  #Its written when poratl is selected its keep on loading on clicking content so its content is not selected since its written twice
        time.sleep(5)
        
        """
        Step 2:Click Content View from the side bar > Click on Domains from the resource tree
        """
        util_obj.wait_for_page_loads(main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, "Folders", main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder('Domains')
 
        """
        Step 3:If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
        """
        main_page_obj.expand_repository_folder('{0}'.format(folder_name))
        main_page_obj.expand_repository_folder('{0}'.format(group_name))
        util_obj.wait_for_page_loads(10)
 
        """
        Step 4:Click on 'Designer' category button > click on 'Portal'
        """
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
                
        """
        Step 5:Enter Title as "Portal for Context Menu Testing1" > Click 'Create'
        Verify 'Portal for Context Menu ...' appear as a folder with the grayed dotter line around the rectangular box (which means it is unpublished).
        """
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=title_name)
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.synchronize_with_visble_text(".content-box.ibx-widget .files-box", title_name, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_folders_in_grid_view([title_name], 'asin', "Step 5: Verify 'Portal for Context Menu ...' appear as a folder.")
        main_page_obj.verify_folder_icon_in_content_area(title_name, 'portal', '5.1', verify_color_name='grey')
        main_page_obj.verify_content_area_folder_publish_or_unpublish(title_name, 'unpublish', "Step 5.2: Verify folder is Unpublished")
        
        """
        Step 6:Right click on 'Portal for Context Menu Testing1' > Publish
        Verify that 'Portal for Context Menu T...' gets published and there is no greyed dotted line outside the folder
        """
        main_page_obj.right_click_folder_item_and_select_menu(title_name,'Publish', '{0}->{1}'.format(folder_name, group_name))
        util_obj.synchronize_with_visble_text(".content-box.ibx-widget .files-box", title_name, main_page_obj.home_page_medium_timesleep)
        time.sleep(20)
        main_page_obj.verify_content_area_folder_publish_or_unpublish(title_name, 'publish', "Step 6: Verify folder is published")
        main_page_obj.verify_folder_icon_in_content_area(title_name, 'portal', '6.1', verify_color_name='lochmara')
        time.sleep(2)
        """
        Step 7:In the banner link, click on the top right username > Click Sign Out.
        """    
        main_page_obj.signout_from_username_dropdown_menu()


if __name__ == '__main__':
    unittest.main()