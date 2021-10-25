'''
Created on Oct 10, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324205
TestCase Name = Upload Resources : Upload Documents of different types (extensions)
'''

import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, wf_mainpage, wf_legacymainpage
from common.lib import utillity


class C2324205_TestClass(BaseTestCase):

    def test_C2324205(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        
        """ Step 1: Sign in as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#topBannerMenuBox [id^='BiWelcomeBannerMenuButton']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="autodevuser43", with_regular_exprestion=True)
        
        """ Step 2: Right Click on 'BIP_V4_Portal' and choose Upload.
            Step 3: Choose Document.
        """
        wf_mainobj.select_repository_menu('P292->S10117->BIP_V4_Portal_upload', 'Upload->Document')
        time.sleep(5)
        
        """ Step 4: Click Browse and navigate to \ibirisc2\bipgqashare\Images_and_Things and choose any xml file (ie. RC_parms.xml)
            Step 5: Click Browse and navigate to \ibirisc2\bipgqashare\Images_and_Things and choose any txt file (ie. test_info.txt)
            Step 6: Click Upload button
                    Click the OK button
        """
        uload_item_list =['RC_Parms.xml', 'test_info.txt']
        wf_mainobj.upload_repository_document_and_image(uload_item_list, ok=True, popup_text='Document(s) uploaded successfully to:\nIBFS:/WFC/Repository/P292/S10117/BIP_V4_Portal_upload\nOK')
        time.sleep(5)
        
        """ Step 7: Verify the 2 documents appear under the 'P292->S10117' > 'BIP_V4_Portal' folder
        """
        wf_mainobj.select_repository_menu('Domains', 'Refresh')
        wf_mainobj.verify_repositery_item('P292->S10117->BIP_V4_Portal_upload', 'RC_Parms', msg='7')
        wf_mainobj.verify_repositery_item('P292->S10117->BIP_V4_Portal_upload', 'test_info', msg='7.1')
        
        """ Step 8: Sign Out from WebFOCUS
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()