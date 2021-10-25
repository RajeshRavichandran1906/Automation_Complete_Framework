'''
Created on 15-Nov-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324255
TestCase Name = Duplicate_testing
'''

import unittest, time
from common.lib import utillity
from common.pages import wf_mainpage, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324255_TestClass(BaseTestCase):

    def test_C2324255(self):
        
        utiliobj=utillity.UtillityMethods(self.driver)
        if utiliobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst04','wfinst05'):
            mainpage = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            mainpage = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        project_id=utiliobj.parseinitfile('project_id')
        suite_id=utiliobj.parseinitfile('suite_id')
        
        '''
        Step 01 : Sign in as WF Developer
        '''
        utiliobj.invoke_webfocu('mrid03', 'mrpass03')
        time.sleep(4)
        
        '''
        Step 02 : Expand P292 ->S10117 -> 'BIP_V4_Portal' folder
        Step 03 : Right Click on 'IA_Chart1' and choose Duplicate
        '''
        folder_path=project_id+'->'+suite_id
        mainpage.select_repository_menu(folder_path+'->BIP_V4_Portal->IA_Chart1','Duplicate')
        time.sleep(5)
         
        '''
        Step 03.1 : Verify 2 versions of that report with the copy having _1 appended to it.
        '''
        mainpage.verify_repositery_item(folder_path+'->BIP_V4_Portal','IA_Chart1_1', msg='3.1')
        mainpage.verify_repositery_item(folder_path+'->BIP_V4_Portal','IA_Chart1', msg='3.2')
         
if __name__=='__main__' :
    unittest.main()