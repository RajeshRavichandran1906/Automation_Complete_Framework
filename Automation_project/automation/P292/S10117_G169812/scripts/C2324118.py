'''
Created on Oct 9, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324118
TestCase Name = Upload Resources:Upload_Image_to_Repository_Folder_and_verify
'''

import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, wf_mainpage, wf_legacymainpage
from common.lib import utillity


class C2324118_TestClass(BaseTestCase):

    def test_C2324118(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2324118'
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        
        """ Step 1: Sign in as WF Developer 
                    Expand 'P292 domain->S10117',
                    Right-click on the 'BIP_V4_Portal' folder and select Upload, then select Image
                    Browse to \ibirisc2\bipgqashare\Images_and_Things
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        parent_css = "#topBannerMenuBox [id^='BiWelcomeBannerMenuButton']"
        resultobj.wait_for_property(parent_css, 1, expire_time=50, string_value="autodevuser43", with_regular_exprestion=True)
        wf_mainobj.select_repository_menu('P292->S10117->BIP_V4_Portal_upload', 'Upload->Image')
        time.sleep(5)
        
        
        """ Step 2: Upload the following images:
                    cd7.gif
                    honda_integra.gif
                    babydeer.jpg
                    Bluehills.jpg
                    Verify the uploaded image is listed under the BIP_V4_Portal folder.
        """
        uload_item_list =['cd7.gif', 'honda_integra.gif', 'babydeer.jpg', 'Bluehills.jpg']
        wf_mainobj.upload_repository_document_and_image(uload_item_list, ok=True, popup_text='Image(s) uploaded successfully to:\nIBFS:/WFC/Repository/P292/S10117/BIP_V4_Portal_upload\nOK')
        time.sleep(5)
        wf_mainobj.select_repository_menu('Domains', 'Refresh')
        wf_mainobj.verify_repositery_item('P292->S10117->BIP_V4_Portal_upload', 'cd7', msg='2')
        wf_mainobj.verify_repositery_item('P292->S10117->BIP_V4_Portal_upload', 'honda_integra', msg='2.1')
        wf_mainobj.verify_repositery_item('P292->S10117->BIP_V4_Portal_upload', 'babydeer', msg='2.2')
        wf_mainobj.verify_repositery_item('P292->S10117->BIP_V4_Portal_upload', 'Bluehills', msg='2.3')
        
        """ Step 3: Expand 'BIP_V4_Portal' folder under P292 domain ->S10117 folder,
                    Right click on all uploaded images and click View
                    Verify the uploaded images should display.
        """
        browser =  utillobj.parseinitfile('browser')
        wf_mainobj.select_repository_menu('P292->S10117->BIP_V4_Portal_upload->cd7', 'View')
        utillobj.switch_to_window(1)
        utillobj.take_browser_screenshot(Test_Case_ID+"_Actual_step3"+browser)
        driver.close()
        utillobj.switch_to_window(0)
        wf_mainobj.select_repository_menu('P292->S10117->BIP_V4_Portal_upload->honda_integra', 'View')
        utillobj.switch_to_window(1)
        utillobj.take_browser_screenshot(Test_Case_ID+"_Actual_step3_1_"+browser)
        driver.close()
        utillobj.switch_to_window(0)
        wf_mainobj.select_repository_menu('P292->S10117->BIP_V4_Portal_upload->babydeer', 'View')
        utillobj.switch_to_window(1)
        utillobj.take_browser_screenshot(Test_Case_ID+"_Actual_step3_2_"+browser)
        driver.close()
        utillobj.switch_to_window(0)
        wf_mainobj.select_repository_menu('P292->S10117->BIP_V4_Portal_upload->Bluehills', 'View')
        utillobj.switch_to_window(1)
        utillobj.take_browser_screenshot(Test_Case_ID+"_Actual_step3_3_"+browser)
        driver.close()
        utillobj.switch_to_window(0)
        
        
        """ Step 4: Run the IA document named "Test images" in the 'BIP_V4_Portal' folder.
                    Verify the document runs with no errors.
        """
        wf_mainobj.select_repository_menu('P292->S10117->BIP_V4_Portal_upload->Test_images', 'Run')
        utillobj.switch_to_window(1)
        utillobj.take_browser_screenshot(Test_Case_ID+"_Actual_step4_"+browser)
        driver.close()
        utillobj.switch_to_window(0)
        
        
        """ Step 5: Sign Out from WebFOCUS
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()