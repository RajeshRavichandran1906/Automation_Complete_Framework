'''
Created on 15-Nov-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324255
TestCase Name = Duplicate_testing
'''

import unittest, time
from common.lib import utillity
from common.pages import wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324255_TestClass(BaseTestCase):

    def test_C2324255(self):
        
        workspace = "Workspaces"
        
        utiliobj=utillity.UtillityMethods(self.driver)
        mainpage = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        project_id=utiliobj.parseinitfile('project_id')
        suite_id=utiliobj.parseinitfile('suite_id')
        
        '''
        Step 01 : Sign into WebFOCUS home page as Developer User
                  Navigate URL to http://environment name:port/alias/legacyhome
        '''
        utiliobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css = "#PortalResourcevBOX table tr td"
        utiliobj.synchronize_with_visble_text(parent_css, workspace, mainpage.home_page_long_timesleep)
        
        '''
        Step 02 : Expand P292 ->S10117 -> 'BIP_V4_Portal' folder
        Step 03 : Right Click on 'IA_Chart1' and choose Duplicate
                  Verify 2 versions of that report with the copy having _1 appended to it.    
        '''
        folder_path=project_id+'->'+suite_id
        mainpage.select_repository_menu(folder_path+'->BIP_V4_Portal->IA_Chart1','Duplicate')
        utiliobj.synchronize_with_visble_text('#PortalResourcevBOX table', 'IA_Chart1_1', mainpage.home_page_long_timesleep)
        mainpage.verify_repositery_item(folder_path+'->BIP_V4_Portal','IA_Chart1_1', msg='03.00')
        mainpage.verify_repositery_item(folder_path+'->BIP_V4_Portal','IA_Chart1', msg='03.01')
         
        '''
        Step 04: Sign Out from WebFOCUS
        '''
        time.sleep(1)
         
if __name__=='__main__' :
    unittest.main()