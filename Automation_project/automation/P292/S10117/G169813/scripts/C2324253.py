'''
Created on 15-Nov-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324253
TestCase Name = Cut_Paste_testing
'''

import unittest, time
from common.lib import utillity
from common.pages import wf_legacymainpage, visualization_resultarea
from common.lib.basetestcase import BaseTestCase

class C2324253_TestClass(BaseTestCase):

    def test_C2324253(self):
        workspace = "Workspaces"
        utiliobj=utillity.UtillityMethods(self.driver)
        mainpage = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        project_id=utiliobj.parseinitfile('project_id')
        suite_id=utiliobj.parseinitfile('suite_id')
        
        '''
        Step 01 : Sign into WebFOCUS home page as Developer User
                  Navigate URL to http://environment_name:port/alias/legacyhome
        '''
        utiliobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep, string_value=workspace, with_regular_exprestion=True)
        time.sleep(1)
        
        '''
        Step 02 : Expand P292 domain , right click on 'S10117' folder and choose New --> Folder.
        Step 03 : Enter 'Tree Functionality Testing' then click the OK button.
        '''
        folder_path=project_id+'->'+suite_id
        mainpage.create_folder(folder_path, 'Tree Functionality Testing')
        time.sleep(5)
          
        '''
        Step 03.1 : Verify the folder appears.
        '''
        mainpage.verify_repositery_item(folder_path,'Tree Functionality Testing', msg="03.01")
        mainpage.verify_folder_status(folder_path+'->Tree Functionality Testing', status='unpublished')
          
        '''
        Step 04 : Right Click on the 'Tree Functionality Testing folder' and choose Publish.
        '''
        mainpage.select_repository_menu(folder_path+'->Tree Functionality Testing','Publish')
        time.sleep(4)
        mainpage.verify_folder_status(folder_path+'->Tree Functionality Testing', status='published')
        
        '''
        Step 05 : Open the 'BIP_V4_Portal' sub-folder under P292 domain ->S10117 folder.
        Step 06 : Right Click on 'Test images' document and choose Cut.
        '''
        self.driver.refresh()
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep, string_value=workspace, with_regular_exprestion=True)
        time.sleep(1)
        mainpage.select_repository_menu(folder_path+'->BIP_V4_Portal->Test images','Cut')
        
        '''
        Step 07 : Right click on the 'BIP_V4_Portal' folder created in this suite and see if the paste option is enabled
                  In HomePage, verify that it is NOT enabled and is greyed out
                  In Legacyhome page, verify Paste option is enabled
        '''
        mainpage.verify_repository_menu_enabled(folder_path+'->BIP_V4_Portal','Paste Ctrl+V', enabled=True)
        
        '''
        Step 08 : Right Click on 'Tree Functionality Testing' folder and choose Paste
        Verify that the tree refreshed and that folder is now expanded
        '''
        mainpage.select_repository_menu(folder_path+'->Tree Functionality Testing','Paste')
        mainpage.verify_repositery_item(folder_path+'->Tree Functionality Testing','Test images',item_exit=True, msg="08.00")
        self.driver.refresh()
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep, string_value=workspace, with_regular_exprestion=True)
        time.sleep(1)
        mainpage.verify_repositery_item(folder_path+'->BIP_V4_Portal','Test images',item_exit=False, msg="08.01")
        
        '''
        Step 09 : Sign Out from WebFOCUS. 
        '''
        
        
if __name__=='__main__' :
    unittest.main()