'''
Created on Oct 10, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324205
TestCase Name = Upload Resources : Upload Documents of different types (extensions)
'''

import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_legacymainpage
from common.lib import utillity


class C2324205_TestClass(BaseTestCase):

    def test_C2324205(self):
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        folder_path = project_id+'->'+suite_id
        
        """ Step 1: Sign in as WF Developer
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css="#bipTreePanel tbody tr:nth-child(1)> td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, wf_mainobj.home_page_long_timesleep)
        
        """ Step 2: Right Click on 'BIP_V4_Portal' and choose Upload.
            Step 3: Choose Document.
        """
        wf_mainobj.select_repository_menu(folder_path+'->BIP_V4_Portal', 'Upload->Document')
        utillobj.synchronize_until_element_is_visible("#dlgBipUpload [class*='active'] input[name^='fileName']", wf_mainobj.home_page_long_timesleep)
        
        """ Step 4: Click Browse and navigate to \ibirisc2\bipgqashare\Images_and_Things and choose any xml file (ie. RC_parms.xml)
            Step 5: Click Browse and navigate to \ibirisc2\bipgqashare\Images_and_Things and choose any txt file (ie. test_info.txt)
            Step 6: Click Upload button
                    Click the OK button
        """
        uload_item_list =['RC_Parms.xml', 'test_info.txt']
        wf_mainobj.upload_repository_document_and_image(uload_item_list, ok=True, popup_text='Document(s) uploaded successfully to:\nIBFS:/WFC/Repository/'+project_id+'/'+suite_id+'/BIP_V4_Portal\nOK')
        utillobj.synchronize_until_element_disappear("#dlgBipUpload [class*='active'] input[name^='fileName']", wf_mainobj.home_page_long_timesleep)
        
        """ Step 7: Verify the 2 documents appear under the 'P292->S10117' > 'BIP_V4_Portal' folder
        """
        wf_mainobj.select_repository_menu(workspace, 'Refresh')
        utillobj.synchronize_with_visble_text(parent_css, workspace, wf_mainobj.home_page_long_timesleep)
        wf_mainobj.verify_repositery_item(folder_path+'->BIP_V4_Portal->RC_Parms', 'RC_Parms', msg='7')
        wf_mainobj.verify_repositery_item(folder_path+'->BIP_V4_Portal->test_info', 'test_info', msg='7.1')
        
        """ Step 8: Sign Out from WebFOCUS
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()