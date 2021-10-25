'''
Created on May 31, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5852713
TestCase Name = Verify Created, Modified and Accessed dates
'''

import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage, visualization_ribbon, vfour_miscelaneous
from common.wftools import login
from common.lib import utillity, core_utility
from common.wftools import visualization


class C5852713_TestClass(BaseTestCase):

    def test_C5852713(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        vis_obj = visualization.Visualization(self.driver)
        vis_ribobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        vfour_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        dev_user_name = utillobj.parseinitfile('mrid')
        proj_id = str(project_id)
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        sub_folder="{0}->InfoAssist->Reports".format(proj_id)
        data_folder="ibisamp"
        master_file_name='car'
        file_name="Dates test"
        
        
        """ Step 1: Login to WebFOCUS as a Developer
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: From the new Home Page click on Content from side bar
        """
        wf_mainobj.select_left_panel('Content')
           
        """ Step 3: Open P242_S10674_G171304/InfoAssist/Reports folder
        """
        wf_mainobj.expand_repository_folders(sub_folder)
           
        """ Step 4: Click Report in Action Bar
                    Click ibisamp folder in left pane
                    Click car in right pane
                    Click Open
        """
        wf_mainobj.select_ribbon_button('Report')
        vis_obj.switch_to_new_window()
        utillobj.select_masterfile_in_open_dialog_(data_folder, master_file_name)
        utillobj.synchronize_with_visble_text("#TableChart_1 [style*='font']", 'Draganddropfieldsontothecanvasorintothequerypanetobeginbuildingyourreport.', 290)
           
        """ Step 5: Double click COUNTRY
                    Double click SALES
        """
        vis_obj.double_click_on_datetree_item('COUNTRY', 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 6, 190)
        vis_obj.double_click_on_datetree_item('SALES', 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 12, 190)
           
        """ Step 6: Click Save button
                    Title: Dates test
                    Click Save 
                    Close InfoAssist
        """
        wf_mainobj.current_time()
        vis_obj.save_visualization_from_top_toolbar(file_name)
        vis_ribobj.select_visualization_application_menu_item('exit')
        core_utilobj.switch_to_previous_window(window_close=False)
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
          
        """ Step 7: Right click 'Dates test' and click Properties
                    Verify Created, Modified and Accessed dates are the same.
                    Verify current date appears.
        """
        wf_mainobj.select_repository_folder_item_context_menu(file_name, 'Properties')
        created_date=wf_mainobj.get_property_created_modified_accessed_time('Created', '7')
        modified_date=wf_mainobj.get_property_created_modified_accessed_time('Modified', '7.1')
        accessed_date=wf_mainobj.get_property_created_modified_accessed_time('Accessed', '7.2')
        all_same=False
        if created_date == modified_date == accessed_date:
            all_same=True
        utillobj.asequal(all_same, True, "Step 7.3: Verify Created, Modified and Accessed dates are the same.")
        base_status=wf_mainobj.verify_property_created_modified_accessed_time(dev_user_name, '7.4', created_date)
        utillobj.asequal(base_status, True, "Step 7.4.1: Verify current date appears in Created")
        base_status1=wf_mainobj.verify_property_created_modified_accessed_time(dev_user_name, '7.5', modified_date)
        utillobj.asequal(base_status1, True, "Step 7.5.1: Verify current date appears in Modified")
        base_status2=wf_mainobj.verify_property_created_modified_accessed_time(dev_user_name, '7.6', accessed_date)
        utillobj.asequal(base_status2, True, "Step 7.6.1: Verify current date appears in Accessed")
          
        """ Step 8: Close Properties panel
        """
        wf_mainobj.close_property_dialog()
         
        """ Step 9: Right click 'Dates test' and click Edit
        """
        wf_mainobj.select_repository_folder_item_context_menu(file_name, 'Edit')
        vis_obj.switch_to_new_window()
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 12, 290)
         
        """ Step 10: Modify as follows:
                     Double click RETAIL_COST
        """
        vis_obj.double_click_on_datetree_item('RETAIL_COST', 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 18, 190)
         
        """ Step 11: Click Save button
                     Click OK in message box "Report saved successfully"
                     Close InfoAssist
        """
        wf_mainobj.current_time()
        vis_obj.select_item_in_top_toolbar('save')
        utillobj.click_dialog_button("div[id^='BiDialog']", 'OK')
        vfour_misobj.synchronize_until_element_disappear("div[id^='BiDialog'] .active", 0, 190)
        vis_ribobj.select_visualization_application_menu_item('exit')
        core_utilobj.switch_to_previous_window(window_close=False)
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        time.sleep(9)
        
        """ Step 12: Right click 'Dates test' and click Properties
                     Verify Modified and Accessed changed and do not differ from each other.
                     Verify Created is unchanged.
        """
        wf_mainobj.select_repository_folder_item_context_menu(file_name, 'Properties')
        created_date1=wf_mainobj.get_property_created_modified_accessed_time('Created', '12')
        modified_date1=wf_mainobj.get_property_created_modified_accessed_time('Modified', '12.1')
        accessed_date1=wf_mainobj.get_property_created_modified_accessed_time('Accessed', '12.2')
        all_same=False
        if modified_date1 == accessed_date1:
            all_same=True
        utillobj.asequal(all_same, True, "Step 12.3: Verify Modified and Accessed do not differ from each other.")
        base_status1=wf_mainobj.verify_property_created_modified_accessed_time(dev_user_name, '12.4', modified_date1)
        utillobj.asequal(base_status1, True, "Step 12.4.1: Verify Modified is changed")
        base_status2=wf_mainobj.verify_property_created_modified_accessed_time(dev_user_name, '12.5', accessed_date1)
        utillobj.asequal(base_status2, True, "Step 12.5.1: Verify Accessed is changed")
        created_date_status=False
        if created_date==created_date1:
            created_date_status=True
        utillobj.asequal(created_date_status, True, "Step 12.6: Verify Created is unchanged.")
        """ Step 13: Close Properties pane
        """
        wf_mainobj.close_property_dialog()
        time.sleep(60)
        
        """ Step 14: Right click 'Dates test' and click Edit
                     Close InfoAssist
        """
        wf_mainobj.current_time()
        wf_mainobj.select_repository_folder_item_context_menu(file_name, 'Edit')
        vis_obj.switch_to_new_window()
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 18, 190)
        vis_ribobj.select_visualization_application_menu_item('exit')
        core_utilobj.switch_to_previous_window(window_close=False)
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 15: Right click 'Dates test' and click Properties
                     Verify Accessed changed.
                     Verify Created and Modified are unchanged.
        """
        wf_mainobj.select_repository_folder_item_context_menu(file_name, 'Properties')
        created_date2=wf_mainobj.get_property_created_modified_accessed_time('Created', '15')
        modified_date2=wf_mainobj.get_property_created_modified_accessed_time('Modified', '15.1')
        accessed_date2=wf_mainobj.get_property_created_modified_accessed_time('Accessed', '15.2')
        acc_date_status=False
        if accessed_date1 != accessed_date2:
            acc_date_status=True
        utillobj.asequal(acc_date_status, True, "Step 15.3: Verify Accessed changed.")
        base_status2=wf_mainobj.verify_property_created_modified_accessed_time(dev_user_name, '15.4', accessed_date2)
        utillobj.asequal(base_status2, True, "Step 15.4.1: Verify Accessed is changed")
        created_date_status=False
        if created_date==created_date2 and modified_date1==modified_date2:
            cre_and_mod_date_status=True
        utillobj.asequal(cre_and_mod_date_status, True, "Step 15.5: Verify Created and Modified are unchanged..")
        
        """ Step 16: Close Properties pane
                     Delete 'Dates test'
        """
        wf_mainobj.close_property_dialog()
        
        """ Step 17: Sign out
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()