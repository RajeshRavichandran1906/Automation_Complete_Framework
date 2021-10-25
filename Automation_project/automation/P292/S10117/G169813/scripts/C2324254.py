'''
Created on 15-Nov-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324254
TestCase Name = Copy_Paste_testing
'''

import unittest, time
from common.lib import utillity, core_utility
from common.pages import wf_legacymainpage, visualization_resultarea
from common.lib.basetestcase import BaseTestCase

class C2324254_TestClass(BaseTestCase):

    def test_C2324254(self):
        workspace = "Workspaces"
        utiliobj=utillity.UtillityMethods(self.driver)
        coreutil_obj = core_utility.CoreUtillityMethods(self.driver)
        mainpage = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        project_id=utiliobj.parseinitfile('project_id')
        suite_id=utiliobj.parseinitfile('suite_id')
        
        '''
        Step 01 : Sign into WebFOCUS home page as Developer User
                  Navigate URL to http://environment name:port/alias/legacyhome
        '''
        utiliobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep, string_value=workspace, with_regular_exprestion=True)
        time.sleep(1)
        
        '''
        Step 02 : Expand P292 -> S10117 > BIP_V4_Portal ,Right Click on cd7 and choose Copy
        '''
        folder_path=project_id+'->'+suite_id
        mainpage.select_repository_menu(folder_path+'->BIP_V4_Portal->cd7','Copy')
        time.sleep(5)
          
        '''
        Step 03 : Right click on 'Tree Functionality Testing' folder and choose Paste
                  Verify that the report is now under that folder
        '''
        mainpage.select_repository_menu(folder_path+'->Tree Functionality Testing','Paste')
        time.sleep(4)
        mainpage.verify_repositery_item(folder_path+'->Tree Functionality Testing','cd7',item_exit=True, msg="03.00")
        
        '''
        Step 04 : Right Click on cd7 under 'BIP_V4_Portal' folder created in this suite and choose Copy
        '''
        self.driver.refresh()
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep, string_value=workspace, with_regular_exprestion=True)
        time.sleep(1)
        mainpage.select_repository_menu(folder_path+'->BIP_V4_Portal->cd7','Copy')
        
        '''
        Step 05 : Right Click on 'BIP_V4_Portal' folder created in this suite and choose Paste
        Verify duplicate version of the content is created under folder.
        '''
        mainpage.select_repository_menu(folder_path+'->BIP_V4_Portal','Paste')
        time.sleep(2)
        mainpage.verify_repositery_item(folder_path+'->BIP_V4_Portal','cd7_1',item_exit=True, msg="05.00")
        
        '''
        Step 06 : Right click on cd7 under 'Tree functionality testing' folder and choose Copy
        '''
        self.driver.refresh()
        parent_css = "#PortalResourcevBOX table tr td"
        resultobj.wait_for_property(parent_css, 1, expire_time=resultobj.home_page_long_timesleep, string_value=workspace, with_regular_exprestion=True)
        time.sleep(1)
        mainpage.select_repository_menu(folder_path+'->Tree Functionality Testing->cd7','Copy')
        
        '''
        Step 07: Right click on 'BIP_V4_Portal' folder created in this suite and choose Paste 
        '''
        mainpage.select_repository_menu(folder_path+'->BIP_V4_Portal','Paste')
        time.sleep(3)
        
        '''
        Step 07.1 : Verify the information window
        '''
        css="#pasteDialog #progbar>div[class*='bi-progress-bar']"
        cap_css="#pasteDialog div[class*='window-caption'] div[class^='bi-label']"
        cap_txt='Copy/Cut/Move/Paste'
        pop_css="#pasteDialog #procErrorText"
        pop_txt='Item already exists'
        utiliobj.verify_popup(css,'Step 07.01: Verify the information window', caption_css=cap_css, caption_text=cap_txt, popup_text_css=pop_css, popup_text=pop_txt)
        
        '''
        Step 08 : Click on Create New
        '''
        coreutil_obj.left_click(self.driver.find_element_by_css_selector("#pasteDialog #btnRename"))
        time.sleep(3)
        
        '''
        Step 08.1 : Verify version 2 of cd7
        '''
        mainpage.verify_repositery_item(folder_path+'->BIP_V4_Portal','cd7_2',item_exit=True, msg="08.01")
        
if __name__=='__main__' :
    unittest.main()