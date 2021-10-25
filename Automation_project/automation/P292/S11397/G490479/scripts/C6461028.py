'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6461028'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators
import uiautomation as automation

class C6461028_TestClass(AS_BaseTestCase):
    def test_C6461028(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()

        '''Test-Case Property Variables'''
        
        webfocus_env_path="webfocus_environment"
        key_pattern_1=['down','enter']
        key_pattern_2=['down','down','enter']
        key_pattern_3=['down','down','down','enter']
        key_pattern_4=['down','down','down','down','enter']
        key_pattern_5=['down','down','down','down','down','enter']
        key_pattern_6=['down','down','down','down','down','down','enter']
        key_pattern_7=['down','down','down','down','down','down','down','enter']
        wait_time=[0,1,2,3,4,5,6,7,8,9,10,11,12]
                
        '''Test-Case Verifications'''
        
        verify_image_1="step1_C6461028.png"
        verify_image_2="step2_C6461028.png"
        verify_image_3="step3_C6461028.png"
        verify_image_4="step4_C6461028.png"
        verify_image_5="step5_C6461028.png"
        verify_image_6="step6_C6461028.png"
        verify_image_7="step7_C6461028.png"
        
        verify_msg="Verify Browser maximised"
        verify_msg_1="Step 01: Verify the admin console for the specified environment opens in the default browser."
        verify_msg_2="Step 02: Verify the Reporting Server Console opens in IE at the Applications tab"
        verify_msg_3="Step 03: Verify the security tab invokes inside App studio"
        verify_msg_4="Step 04: Verify the WebFOCUS BI Portal opens in an IE browser and is positioned at the welcome page"
        verify_msg_5="Step 05: Verify the Deferred Report Status window opens in IE"
        verify_msg_6="Step 06: Verify Reporting Server Console for the specified environment opens in the default browser."
        verify_msg_7="Step 07: Verify Session Viewer window opens with date and time with the following"
        verify_msg_8="Verify browser closed"
        
        '''Test-Script'''
          
        as_utilobj.select_home_button()
        time.sleep(wait_time[0])
        
        '''Step 01: In Environments Tree, select a Configured Environment
                    Under WebFOCUS Administration drop down menu, click WebFOCUS Administration Console'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(wait_time[1])
            
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(wait_time[2])
                
        as_utilobj.select_tree_view_pane_item(locators.data_server) 
        time.sleep(wait_time[2])
          
        as_utilobj.click_element_using_ui(split_button=locators.wf_admin_splitbutton,send_keys=key_pattern_1)
        time.sleep(wait_time[6])
         
        as_utilobj.Verify_Browser_Content(locators.ie_browser_classname,verify_msg)
        time.sleep(wait_time[2])
          
        as_utilobj.verify_picture_using_sikuli(verify_image_1,verify_msg_1)
        time.sleep(wait_time[2])
         
        as_utilobj.Verify_Browser_Content(locators.ie_browser_classname,verify_msg_8,browser_close=True)
        time.sleep(wait_time[2])
          
        '''Step 02: Under WebFOCUS Administration drop down menu, click Reporting Server Console
                    Close the WebFOCUS nn Server tab'''
          
        as_utilobj.click_element_using_ui(split_button=locators.wf_admin_splitbutton,send_keys=key_pattern_2)
        time.sleep(wait_time[11])
         
        as_utilobj.Verify_Browser_Content(locators.ie_browser_classname,verify_msg)
        time.sleep(wait_time[2])
         
        as_utilobj.verify_picture_using_sikuli(verify_image_2,verify_msg_2)
        time.sleep(wait_time[2])
          
        as_utilobj.Verify_Browser_Content(locators.ie_browser_classname,verify_msg_8,browser_close=True)
        time.sleep(wait_time[2])
          
        '''Step 03: Under WebFOCUS Administration drop down menu, click Security Center
                    Close the Security Center (server name) tab'''
         
        as_utilobj.click_element_using_ui(split_button=locators.wf_admin_splitbutton,send_keys=key_pattern_3)
        time.sleep(wait_time[11])
         
        as_utilobj.verify_picture_using_sikuli(verify_image_3,verify_msg_3)
        time.sleep(wait_time[2])
          
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_C, waitTime=3)
        time.sleep(2)
         
        '''Step 04: Under WebFOCUS Administration drop down menu, click BI Portal
                    Close the WebFOCUS Home tab'''
         
        as_utilobj.click_element_using_ui(split_button=locators.wf_admin_splitbutton,send_keys=key_pattern_4)
        time.sleep(wait_time[11])
         
        as_utilobj.Verify_Browser_Content(locators.ie_browser_classname,verify_msg)
        time.sleep(wait_time[2])
         
        as_utilobj.verify_picture_using_sikuli(verify_image_4,verify_msg_4)
        time.sleep(wait_time[2])
          
        as_utilobj.Verify_Browser_Content(locators.ie_browser_classname,verify_msg_8,browser_close=True)
        time.sleep(wait_time[2])
        
        '''Step 05: Under WebFOCUS Administration drop down menu, click Deferred Status
                    Close the Deferred Report Status tab'''
        
        as_utilobj.click_element_using_ui(split_button=locators.wf_admin_splitbutton,send_keys=key_pattern_5)
        time.sleep(wait_time[11])
        
        as_utilobj.Verify_Browser_Content(locators.ie_browser_classname,verify_msg)
        time.sleep(wait_time[2])
        
        as_utilobj.verify_picture_using_sikuli(verify_image_5,verify_msg_5)
        time.sleep(wait_time[2])
         
        as_utilobj.Verify_Browser_Content(locators.ie_browser_classname,verify_msg_8,browser_close=True)
        time.sleep(wait_time[2])
        
        '''Step 06: Under WebFOCUS Administration drop down menu, click ReportCaster Console
                    Close the ReportCaster Status tab'''
         
        as_utilobj.click_element_using_ui(split_button=locators.wf_admin_splitbutton,send_keys=key_pattern_6)
        time.sleep(wait_time[11])
         
        as_utilobj.Verify_Browser_Content(locators.ie_browser_classname,verify_msg)
        time.sleep(wait_time[2])
         
        as_utilobj.verify_picture_using_sikuli(verify_image_6,verify_msg_6)
        time.sleep(wait_time[2])
          
        as_utilobj.Verify_Browser_Content(locators.ie_browser_classname,verify_msg_8,browser_close=True)
        time.sleep(wait_time[2])
         
        '''Step 07: Under WebFOCUS Administration drop down menu, click Session Viewer
                    Close the Session Viewer tab'''
         
        as_utilobj.click_element_using_ui(split_button=locators.wf_admin_splitbutton,send_keys=key_pattern_7)
        time.sleep(wait_time[11])
         
        as_utilobj.Verify_Browser_Content(locators.ie_browser_classname,verify_msg)
        time.sleep(wait_time[2])
         
        as_utilobj.verify_picture_using_sikuli(verify_image_7,verify_msg_7)
        time.sleep(wait_time[2])
          
        as_utilobj.Verify_Browser_Content(locators.ie_browser_classname,verify_msg_8,browser_close=True)
        time.sleep(wait_time[2])    
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(wait_time[1])   
        
if __name__=='__main__' :
    unittest.main()  