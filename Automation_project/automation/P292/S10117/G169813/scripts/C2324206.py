'''
Created on Sep 1, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324206
TestCase Name = Upload Resources : Upload Document type with .vbs extension 
'''

import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_legacymainpage
from common.lib import utillity


class C2324206_TestClass(BaseTestCase):

    def test_C2324206(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        workspace = "Workspaces"
        utillobj = utillity.UtillityMethods(self.driver)
        wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        project_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        folder_path = project_id+'->'+suite_id
        
        """
        Step 01: Sign in as WF Developer
        """
        utillobj.invoke_legacyhomepage('mrid03', 'mrpass03')
        parent_css="#bipTreePanel tbody tr:nth-child(1)> td"
        utillobj.synchronize_with_visble_text(parent_css, workspace, 190)        

        """
        Step 02: Right Click on 'BIP_V4_Portal' and choose Upload
        Step 03: Choose Document
        """
        wf_mainobj.select_repository_menu(folder_path+'->BIP_V4_Portal', 'Upload->Document')
        time.sleep(5)
        
        """
        Step 04: Click Browse and navigate to \ibirisc2\bipgqashare\Images_and_Things and choose any vbs file (ie. Upload.vbs)
        Step 05: Click Upload button
        """
        uload_item_list =['Upload.vbs']
        wf_mainobj.upload_repository_document_and_image(uload_item_list)
        time.sleep(5)
        
        """
        Verify that you get an error message for uploading the .vbs file
        """
        parent_css= "div[id^='BiDialog'][class*='bi-component']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 120)
        css="div[id^='BiDialog'][class*='bi-component'] [class*='active']  [class*='caption'] [class*='bi-label']"
        text_css="div[id^='BiDialog'][class*='bi-component'] [class*='active'] div[id^='BiOptionPane']"
        text = 'Upload Failed. The following file type(s) not allowed:\n\nUpload.vbs\nOK'
        utillobj.verify_popup(css, "Step 05.1: Verify that you get an error message for uploading the .vbs file", caption_css=text_css, caption_text=text)
        time.sleep(3)
        
        """close dialog"""
        utillobj.click_dialog_button("div[id^='BiDialog'][class*='bi-component']", "OK")
        time.sleep(3)
        close_btn = driver.find_element_by_css_selector("#dlgBipUpload #btnDone div[class*='bi-button-label']")
        utillobj.click_on_screen(close_btn, 'middle')
        utillobj.default_click(obj_locator=close_btn, click_option=0)
        
        """
        Step 06: Sign Out from WebFOCUS
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()