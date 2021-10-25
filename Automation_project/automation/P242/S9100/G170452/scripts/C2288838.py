'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288838'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2288838_TestClass(AS_BaseTestCase):
    def test_C2288838(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
    
        '''Testcase verification'''
        
        verify_general_category_elements="step1_C2288838.png"
        verify_report_category_elements="step2_C2288838.png"
        verify_html_category_elements="step3_C2288838.png"
        verify_document_category_elements="step4_C2288838.png"
        verify_environment_category_elements="step5_C2288838.png"
        verify_help_category_elements="step6_C2288838.png"
        verify_output_viewer_elements="step7_C2288838.png"
        verify_file_extensions_elements="step8_C2288838.png"
        
        verify_msg_1="Step 1.1: Verify Options window opens with General tab displayed by default"
        verify_msg_2="Step 1.2: Verify General tab options are available and selected"
        verify_msg_3="Step 2.1: Verify Options window for Report tab displayed"
        verify_msg_4="Step 2.2: Verify Report tab options are available and selected"
        verify_msg_5="Step 3.1: Verify Options window for html page tab displayed"
        verify_msg_6="Step 3.2: Verify html tab options are available and selected"
        verify_msg_7="Step 4.1: Verify Options window for document tab displayed"
        verify_msg_8="Step 4.2: Verify document tab options are available and selected"
        verify_msg_9="Step 5.1: Verify Options window for environment tab displayed"
        verify_msg_10="Step 5.2: Verify environment tab options are available and selected"
        verify_msg_11="Step 6.1: Verify Options window for help_configuration tab displayed"
        verify_msg_12="Step 6.2: Verify help_configuration tab options are available and selected"
        verify_msg_13="Step 7.1: Verify Options window for output viewer settings tab displayed"
        verify_msg_14="Step 7.2: Verify output viewer settings tab options are available and selected"
        verify_msg_15="Step 8.1: Verify Options window for file extensions tab displayed"
        verify_msg_16="Step 8.2: Verify file extensions tab options are available and selected"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click the AS and click Options'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_1,list_item=component_locators.general_category,selected=True)
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli(verify_general_category_elements,verify_msg_2)
        time.sleep(2)
        
        '''Step 02: From App Studio Options, click Reporting'''
        
        as_utilobj.select_element_appstudio_options(list_item=component_locators.reporting_category)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_3,list_item=component_locators.reporting_category,selected=True)
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli(verify_report_category_elements,verify_msg_4)
        time.sleep(2)
        
        '''Step 03: From App Studio Options, click HTML Page'''
        
        as_utilobj.select_element_appstudio_options(list_item=component_locators.html_category)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_5,list_item=component_locators.html_category,selected=True)
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli(verify_html_category_elements,verify_msg_6)
        time.sleep(2)
        
        '''Step 04: From App Studio Options, click Document'''
        
        as_utilobj.select_element_appstudio_options(list_item=component_locators.document_category)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_7,list_item=component_locators.document_category,selected=True)
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli(verify_document_category_elements,verify_msg_8)
        time.sleep(2)
        
        '''Step 05: From App Studio Options, click Environments'''
        
        as_utilobj.select_element_appstudio_options(list_item=component_locators.environment_category)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_9,list_item=component_locators.environment_category,selected=True)
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli(verify_environment_category_elements,verify_msg_10)
        time.sleep(2)
        
        '''Step 06: From App Studio Options, click Help Configuration'''
        
        as_utilobj.select_element_appstudio_options(list_item=component_locators.help_category)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_11,list_item=component_locators.help_category,selected=True)
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli(verify_help_category_elements,verify_msg_12)
        time.sleep(2)
        
        '''Step 07: From App Studio Options, Output Viewer Settings'''
        
        as_utilobj.select_element_appstudio_options(list_item=component_locators.output_viewer_category)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_13,list_item=component_locators.output_viewer_category,selected=True)
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli(verify_output_viewer_elements,verify_msg_14)
        time.sleep(2)
        
        '''Step 08: From App Studio Options, click File Extensions
                    Click Cancel'''
        
        as_utilobj.select_element_appstudio_options(list_item=component_locators.file_extension_category)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_15,list_item=component_locators.file_extension_category,selected=True)
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli(verify_file_extensions_elements,verify_msg_16)
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(1)
         
if __name__=='__main__' :
    unittest.main()  