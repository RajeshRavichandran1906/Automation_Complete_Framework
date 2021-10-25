'''
Created on Jul 4, 2019

@author: Aftab
Test rail link: http://172.19.2.180/testrail/index.php?/cases/view/5852639
Test case name: Add Page to Portal

'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.pages import vfour_portal_canvas,vfour_portal_ribbon,vfour_portal_properties
import time
from common.wftools.page_designer import Run
from common.pages import page_designer_miscelaneous

class C5852639_TestClass(BaseTestCase):

    def test_C5852639(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        portal_canvas = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_ribbon = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        page_designer_run_obj = Run(self.driver)
        miscellaneous_obj=page_designer_miscelaneous.PageDesignerMiscelaneous(self.driver)
        
        """
            TESTCASE CSS
        """
        project_id  = core_util_obj.parseinitfile('project_id')
        suite_id    = core_util_obj.parseinitfile('suite_id')
        group_id    = core_util_obj.parseinitfile('group_id')
        repository_folder = '{0}_{1}/{2}'.format(project_id, suite_id, group_id) 
        expected_tablet_size = [(600, 960)]
        expected_mobile_size = ['Panel 2', 'Panel 3', 'Panel 4', 'Panel 5']    
        panel5_data_expected_data = ['Panel 5 Category: Store Type:']
        expected_panel_list = ['Category Sales', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5', 'Panel 6']   
        
        '''
        Step 1 : Login WF as domain developer
        '''
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
                 
        '''
        Step 2 : Click on the portal side bar
        '''
        main_page_obj.select_portals_from_sidebar()
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Retail Samples', main_page_obj.home_page_long_timesleep)
       
        '''
        Step 3 : Right click on 'Retail samples' portal and choose Edit
        '''
        main_page_obj.right_click_folder_item_and_select_menu('Retail Samples', context_menu_item_path='Edit', item_name_index = 2)
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible('div[id*="BipAddButton"]', main_page_obj.home_page_long_timesleep)
        
        '''
        Step 4 : Click on Add a new page icon and select 1 Column page;
                 Enter title as "Show On" and click open
        '''
        portal_canvas.add_page('1 Column', Page_title='Show On', page_verify=False)
    
        '''
        Step 5 : Click F8 to open resource tree;
                 Drag and drop 'Show on' page from under P292_S11397' domain -> 'G435308' folder
        '''  
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        util_obj.synchronize_with_visble_text('#bipResourcesPanel #treeView table>tbody>tr','Workspaces',10)
        item_name = repository_folder + '/' + 'Show on'
        portal_canvas.dragdrop_repository_item_to_canvas(item_name.replace('/', '->'), 'column', 1)
         
        '''
        Step 6 : Click on Height drop down from under properties section;
                 Change the height to 'Auto'
        '''
        portal_properties.edit_input_control('panel', 'Height', input_control='combobox', combobox_input = 'Auto')
        
        '''
        Step 7 : Click on Title bar under properties panel and Check 'Hide title bar' checkbox
        '''
        portal_properties.select_property_tab('Title')
        time.sleep(1)
        portal_properties.edit_input_control('panel', 'Hide Title Bar', 'checkbox', checkbox_input='check',msg="Step 7.1")
         
        '''
        Step 8 : Save and exit portal
        '''
        core_util_obj.switch_to_default_content()
        portal_ribbon.bip_save_and_exit("Yes")
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_number_of_element(locator_obj.content_area_css,1, main_page_obj.home_page_medium_timesleep)
        
        '''
        Step 9 : Right click on 'Retail samples' portal and choose Run
        '''
        main_page_obj.right_click_folder_item_and_select_menu('Retail Samples', context_menu_item_path='Run', item_name_index = 2)
        core_util_obj.switch_to_new_window()
         
        '''
        Step 10 : Shrink the browser to tablet size
        '''
        util_obj.set_browser_window_size(600, 960)
        time.sleep(10)
        core_util_obj.switch_to_frame(frame_css='iframe[class*="iframe "]')
        
        '''
        Step 10.01 : Verify panel 6 will not show, other panels appears as below
        '''
        page_designer_run_obj.verify_containers_title(['Category Sales', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5'], 'Step 10.01: Verify panel 6 will not show, other panels appears as below')
        actual_win_size = self.driver.get_window_size()
        actual_tablet_size = actual_win_size['width'],actual_win_size['height']
        util_obj.as_List_equal([actual_tablet_size], expected_tablet_size, 'Step 10.02: Verify window size')
        
        '''
        Step 11 : Shrink the browser to mobile size
        '''
        util_obj.set_browser_window_size(412, 732)
        time.sleep(10)
        
        '''
        Step 11.01 : Verify both Panel1 and panel6 will not show, other panels appears as below
        '''
        page_designer_run_obj.verify_containers_title(expected_mobile_size, 'Step 11.01: Verify both Panel1 and panel6 will not show, other panels appears as below')
        actual_win_size = self.driver.get_window_size()
        actual_range = range(412,520)
        actual_status = actual_win_size['width'] in actual_range
        util_obj.asequal(actual_status, True, 'Step 11.02: Verify window size')
        
        '''
        Step 12 : Resize the browser back to its original maxed state
        '''
        self.driver.maximize_window()
        
        '''
        Step 12.01 : Verify all panels appear as below as this is simulating the desktop
        '''
        page_designer_run_obj.verify_filter_control_labels(['Product Model:', 'Region:', 'From:', 'To:'], 'Step 12.01: Verify all panels appear as below as this is simulating the desktop')
        page_designer_run_obj.verify_containers_title(expected_panel_list, 'Step 12.02: Verify all panels appear as below as this is simulating the desktop')
        panel5_grid_obj = miscellaneous_obj.get_pd_container_object('Panel 5')
        panel5_data = panel5_grid_obj.text.replace('\n', ' ')
        util_obj.as_List_equal(panel5_data_expected_data, [panel5_data],"Step 12.03: Verify all panels appear as below as this is simulating the desktop")
        
        '''
        Step 13 : Close the portal
        '''
        core_util_obj.switch_to_default_content()
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element(locator_obj.content_area_css,1, main_page_obj.home_page_medium_timesleep)
                 
        '''
        Step 14 : Signout WF
        '''
        main_page_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()