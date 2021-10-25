'''
Created on Oct 9, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324118
TestCase Name = Upload Resources:Upload_Image_to_Repository_Folder_and_verify
'''

import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_legacymainpage
from common.lib import utillity,core_utility

class C2324118_TestClass(BaseTestCase):

    def test_C2324118(self):
        
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        Test_Case_ID = 'C2324118'
        utillobj = utillity.UtillityMethods(self.driver)
        coreutillobj=core_utility.CoreUtillityMethods(self.driver)
        wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        folder_path = project_id+'->'+suite_id
        
        """ Step 1: Sign in as WF Developer 
                    Expand 'P292 domain->S10117',
                    Right-click on the 'BIP_V4_Portal' folder and select Upload, then select Image
                    Browse to \ibirisc2\bipgqashare\Images_and_Things
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css="#bipTreePanel tbody tr:nth-child(1)> td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        wf_mainobj.select_repository_menu(folder_path+'->BIP_V4_Portal', 'Upload->Image')
        utillobj.synchronize_with_number_of_element("#dlgBipUpload [class*='active'][class*='window'] input[id*='FormControl'][type='file']", 5, 90)
        
        """ Step 2: Upload the following images:
                    cd7.gif
                    honda_integra.gif
                    babydeer.jpg
                    Bluehills.jpg
                    Verify the uploaded image is listed under the BIP_V4_Portal folder.
        """
        uload_item_list =['cd7.gif', 'honda_integra.gif', 'babydeer.jpg', 'Bluehills.jpg']
        wf_mainobj.upload_repository_document_and_image(uload_item_list, ok=True, popup_text='Image(s) uploaded successfully to:\nIBFS:/WFC/Repository/'+project_id+'/'+suite_id+'/BIP_V4_Portal\nOK')
        utillobj.synchronize_until_element_disappear("#dlgBipUpload [class*='active'][class*='window']", 45)
        wf_mainobj.select_repository_menu(workspace, 'Refresh')
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)
        wf_mainobj.verify_repositery_item(folder_path+'->BIP_V4_Portal->cd7', 'cd7', msg='2')
        wf_mainobj.verify_repositery_item(folder_path+'->BIP_V4_Portal->honda_integra', 'honda_integra', msg='2.1')
        wf_mainobj.verify_repositery_item(folder_path+'->BIP_V4_Portal->babydeer', 'babydeer', msg='2.2')
        wf_mainobj.verify_repositery_item(folder_path+'->BIP_V4_Portal->Bluehills', 'Bluehills', msg='2.3')
        
        """ Step 3: Expand 'BIP_V4_Portal' folder under P292 domain ->S10117 folder,
                    Right click on all uploaded images and click View
                    Verify the uploaded images should display.
        """
        wf_mainobj.select_repository_menu(folder_path+'->BIP_V4_Portal->cd7', 'View')
        coreutillobj.switch_to_new_window()
        utillobj.verify_picture_using_sikuli(Test_Case_ID+"_Base_step3.png","Step3.1:verfiy picture of cd7.gif")
        coreutillobj.switch_to_previous_window()
        wf_mainobj.select_repository_menu(folder_path+'->BIP_V4_Portal->honda_integra', 'View')
        coreutillobj.switch_to_new_window()
        utillobj.verify_picture_using_sikuli(Test_Case_ID+"_Base_step3.1.png","Step3.1:verfiy picture of honda integra")
        coreutillobj.switch_to_previous_window()
        wf_mainobj.select_repository_menu(folder_path+'->BIP_V4_Portal->babydeer', 'View')
        coreutillobj.switch_to_new_window()
        utillobj.verify_picture_using_sikuli(Test_Case_ID+"_Base_step3.2.png","Step3.1:verfiy picture of baby deer")
        coreutillobj.switch_to_previous_window()
        wf_mainobj.select_repository_menu(folder_path+'->BIP_V4_Portal->Bluehills', 'View')
        coreutillobj.switch_to_new_window()
        utillobj.verify_picture_using_sikuli(Test_Case_ID+"_Base_step3.3.png","Step3.1:verfiy picture of blue hills")
        coreutillobj.switch_to_previous_window()
        
        """ Step 4: Run the IA document named "Test images" in the 'BIP_V4_Portal' folder.
                    Verify the document runs with no errors.
        """
        wf_mainobj.select_repository_menu(folder_path+'->BIP_V4_Portal->Test images', 'Run')
        coreutillobj.switch_to_new_window()
        
        utillobj.verify_picture_using_sikuli(Test_Case_ID+"_Base_step4.png","Step4 verify all pictures")
        coreutillobj.switch_to_previous_window()
        
        """ Step 5: Sign Out from WebFOCUS
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()