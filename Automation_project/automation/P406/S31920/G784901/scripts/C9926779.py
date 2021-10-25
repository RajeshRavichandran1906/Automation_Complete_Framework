import unittest
#import sys
#sys.path.append('../../')
from utility.selenium_utility import Selenium_Utility 
from utility.basetestcasedocker import BaseTestCaseDocker
from utility.locators import *

class C9926779_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C9926779_TestClass, self).__init__(driver)
    
    def test_C9926779(self):        
        
        case_id = 'C9926779'
        author = 'autoauthworkspace'
        basic_user = 'autobasworkspace'
        from_path = 'Retail Samples->Charts'
        to_path = 'My Workspace->My Content'
        fex = 'Arc - Sales by Region'
        #new_title = case_id + '_test'
        new_summary = 'Test of summary changing'
        #Step 1: Log into the paris home page
        utilobj = Selenium_Utility(self.driver)
        utilobj.login_wf(mrid=author, mrpass='')
        #Step 2: Create users to  be used for testing - Dev, Adv, Basic
        #Step 3: Click on My Workspace - verify 
        utilobj.click_my_workspace()
        utilobj.verify_fex_not_present(fex)
        #Step 4: Click on Share With Me
        utilobj.click_shared_with_me()
        utilobj.verify_fex_not_present(fex)
        #Step 5: Go to workspaces
        utilobj.click_workspaces()
        #Step 6: Copy items to My Content folder
        workspaces_iframe = utilobj.driver.find_element(*HomePageLocators.workspaces_iframe)
        utilobj.driver.switch_to.frame(workspaces_iframe)
        utilobj.copy_and_paste_fex(from_path, fex, to_path, case_id, "6")
        self.driver.switch_to.default_content()
        #Step 7: Return to paris home page
        #utilobj.go_to_paris_home_page()
        #Step 8: Click on My Workspace
        utilobj.click_my_workspace()
        #Step 8a: Verify grid view + sorted by "Modified"
        utilobj.verify_grid_view(case_id, '8')
        #utilobj.verify_sorted_last_modified(case_id, '8')
        #Step 9: Switch to list view (maintain sorting)
        utilobj.toggle_list_my_workspace()
        utilobj.verify_sorted_last_modified(case_id, '9')
        #Step 10: Right click on items and verify context menus
        utilobj.right_click_fex(fex)
        utilobj.verify_context_menu(case_id, '10')
        #Step 11: Right click item and share (verify share icon)
        try:
            #utilobj.right_click_fex(fex)
            utilobj.unshare_fex()
            utilobj.right_click_fex(fex)
        except:
            pass
        utilobj.share_fex(fex, case_id, '11')
        #Step 12: Right click and choose share with (verify share dialog)
        '''try:
            utilobj.right_click_fex(fex)
            utilobj.unshare_fex()
        except:
            pass'''
        #Step 13: Share with user
        utilobj.right_click_fex(fex)
        utilobj.unshare_fex()
        utilobj.right_click_fex(fex)
        utilobj.share_fex_with(case_id, '13', basic_user)
        #Step 14: Change properties of 2 items (summary, title)
        utilobj.right_click_fex(fex)
        utilobj.change_properties(summary=new_summary)
        utilobj.verify_properties(case_id, '14', summary=new_summary)
        #Step 15: Click out and then back to My Workspace (verify items showing properly)
        utilobj.click_shared_with_me()
        utilobj.click_my_workspace()
        utilobj.toggle_list_my_workspace()
        utilobj.verify_workspace_item(fex, case_id, '15')
        #Step 16: Duplicate item (Verify it is duplicated and listed first by Last Modified)
        #utilobj.click_my_workspace()
        #utilobj.toggle_list_my_workspace()
        utilobj.right_click_fex(fex)
        utilobj.duplicate_fex()
        utilobj.verify_duplicated_item(fex, case_id, '16')
        utilobj.verify_sorted_last_modified(case_id, '16')
        #Step 17: Log in as user that was shared
        utilobj.logout_wf()
        utilobj.login_wf(mrid=basic_user, mrpass='')
        #Step 18: Click on share with me (verify items appear)
        utilobj.click_shared_with_me()
        #utilobj.verify_shared_item(fex, case_id, '18')
        utilobj.verify_workspace_item(fex, case_id, '18')
        #Step 19: Sign out
        utilobj.logout_wf()
              
if __name__ == "__main__":   
    unittest.main()