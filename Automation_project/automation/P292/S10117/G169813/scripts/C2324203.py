'''
Created on 28-Aug-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324203
TestCase Name = Portal Designer_Design Tree : Create_and_Delete_folder_from_F8_Resource_Tree
'''
import unittest, time
from common.lib import utillity
from common.lib import core_utility
from common.pages import wf_administration_console, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324203_TestClass(BaseTestCase):

    def test_C2324203(self):
        driver = self.driver 
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj = core_utility.CoreUtillityMethods(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        wf_admin_conobj = wf_administration_console.Wf_Administration_Console(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        folder_path = project_id+'->'+suite_id
        
        
        """ Step 1: Sign in as WF Administrator
        """
        utillobj.invoke_legacyhomepage('mrid', 'mrpass')
        parent_css="#bipTreePanel tbody tr:nth-child(1)> td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        
        
        """ Step 2: Click on Administration then Administration Console
        """                                             
        wf_mainpageobj.select_or_verify_top_banner_links('Administration->Administration Console')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        core_utillobj.switch_to_new_window()
        time.sleep(2)
        
        """ Step 3: Click BI Portal
                    Check the Collaborative Portal box
        """
        wf_admin_conobj.select_admin_console_tree('#console_tree_Configuration_Settings', 'Application Settings->BI Portal') 
        time.sleep(1)
        parent_css1="#idApplicationSettingsPageView"
        wf_admin_conobj.verify_bihbox(parent_css1, 'Collaborative Portal', 'checkbox', 'checked', 'Step 3: Collaborative Portal is checked.')
        
        
        """ Step 4: Click On Save button
                    Click OK
        """
        wf_admin_conobj.input_bihbox(parent_css1, 'Save', option_button='save')
        time.sleep(2)
        
        """ Step 5: Close the Administration Console
        """
        wf_admin_conobj.select_or_verify_top_toolbar_links('close')
        core_utillobj.switch_to_previous_window(window_close=False)
        
        """ Step 6: Refresh the browser
        """
        driver.refresh()
        time.sleep(2)
        
        
        """ Step 7: Right click on the 'P292_S10117' domain then select New
                    Verify that you see Collaborative Portal and Page.
                    For 8202
                    Verify that you see Collaborative Portal and Portal Page.
        """
        parent_css="#bipTreePanel tbody tr:nth-child(1)> td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        wf_mainpageobj.select_repository_menu(folder_path+'->BIP_V4_Portal', 'New', item_exit=True, expected_menu_list=['Collaborative Portal', 'Portal Page'], 
                                              msg="Step 7")
        
        
        """ Step 8: Click Administration then Administration Console
                    Click BI Portal
        """
        wf_mainpageobj.select_or_verify_top_banner_links('Administration->Administration Console')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        core_utillobj.switch_to_new_window()
        time.sleep(2)
        wf_admin_conobj.select_admin_console_tree('#console_tree_Configuration_Settings', 'Application Settings->BI Portal')   
        time.sleep(2)
        
        
        """ Step 9: Uncheck Collaborative Portal and save
                    Click OK
        """
        wf_admin_conobj.input_bihbox(parent_css1, 'Collaborative Portal', input_control='checkbox', option_button='save')
        time.sleep(2)
        
        """ Step 10: Close Administration Console and Refresh
        """
        wf_admin_conobj.select_or_verify_top_toolbar_links('close')
        core_utillobj.switch_to_previous_window(window_close=False)
        driver.refresh()
        time.sleep(2)
        
        """ Step 11: Right click on the 'P292_S10117' domain then New
                    Verify that you don't see Collaborative Portal and Page
                    For 8202
                    Verify that you don't see Collaborative Portal and Portal Page.
        """
        parent_css="#bipTreePanel tbody tr:nth-child(1)> td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        wf_mainpageobj.select_repository_menu(folder_path+'->BIP_V4_Portal', 'New', item_exit=False, expected_menu_list=['Collaborative Portal', 'Portal Page'], 
                                              msg="Step 11")
        
        """ Step 12: Click Administration then Administration Console
                     Click BI Portal
        """
        wf_mainpageobj.select_or_verify_top_banner_links('Administration->Administration Console')
        run_loop = True
        count_time=0
        while run_loop:
            if count_time == 25:
                run_loop = False
            if len(driver.window_handles) > 1:
                run_loop = False
            count_time += 1
        core_utillobj.switch_to_new_window()
        time.sleep(2)
        wf_admin_conobj.select_admin_console_tree('#console_tree_Configuration_Settings', 'Application Settings->BI Portal')   
        time.sleep(2)
        
        
        """ Step 13: Check Collaborative Portal and save
                     Click OK
        """
        wf_admin_conobj.input_bihbox(parent_css1, 'Collaborative Portal', input_control='checkbox', option_button='save')
        time.sleep(2)
                
        """ Step 14: Close Administration Console and Refresh
        """
        wf_admin_conobj.select_or_verify_top_toolbar_links('close')
        core_utillobj.switch_to_previous_window(window_close=False)
        driver.refresh()
        time.sleep(2)
        
        
        """ Step 15: Right click on the 'P292_S10117' domain then select New
                     Verify that you see Collaborative Portal and Page.
                     For 8202
                    Verify that you see Collaborative Portal and Portal Page.
        """
        parent_css="#bipTreePanel tbody tr:nth-child(1)> td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        wf_mainpageobj.select_repository_menu(folder_path+'->BIP_V4_Portal', 'New', item_exit=True, expected_menu_list=['Collaborative Portal', 'Portal Page'], 
                                              msg="Step 15")
        
        
        """ Step 16: Sign Out from WebFOCUS
        """
        time.sleep(5)
        
        

if __name__ == '__main__':
    unittest.main()