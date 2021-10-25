'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288849'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators

class C2288849_TestClass(AS_BaseTestCase):
    def test_C2288849(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_161337="Domains->S9100->161337"
        select_active_chart="ActiveChart"
        select_document="document help"
        select_html_page="DisneyBallDog"
        select_document_help_window=['down']
        help_window="App Studio Help"
        
        '''Testcase verification'''
        
        verify_report_help_window="Building an Application Using the Home Tab"
        verify_chart_help_window="Creating Charts and Visualizations"
        verify_document_help_window="Inserting Components and Controls in a Document or Active Dashboard Using the Insert Tab"
        verify_document_help_window_for_positioning="Positioning Multi-Selected Objects in a Document or Active Dashboard Using the Positioning Tab"
        verify_html_help_window="Inserting Components in an HTML Page Using the Components Tab"
        verify_msg_1="Step 01: Verify help window invoked for creating reports"
        verify_msg_2="Step 02: Verify Help file closes"
        verify_msg_3="Step 03: Verify help window invoked for creating charts"
        verify_msg_4="Step 04: Verify Help file closes"
        verify_msg_5="Step 05: Verify help window invoked for creating documents"
        verify_msg_6="Step 06: Verify help window invoked for creating documents and positioning"
        verify_msg_7="Step 07: Verify Help file closes"
        verify_msg_8="Step 08: Verify help window invoked for creating html page"
        verify_msg_9="Step 08: Verify Help file closes"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Domains->CC - AppStudio->AS Framework
                    Double click on 161337
                    Click the Help drop down menu and select Help Topics'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
             
        as_utilobj.select_tree_view_pane_item(select_161337) 
        time.sleep(6) 
         
        as_utilobj.click_element_using_ui(split_button=locators.help_splitbutton)
        time.sleep(5)
          
        as_utilobj.verify_element_using_ui(verify_msg_1,text_item=verify_report_help_window)
        time.sleep(5)
          
        '''Step 02: Close App Studio Help window
                    Close 161337 tab'''
          
        as_utilobj.verify_element_using_ui(verify_msg_2,window_control_item=help_window,window_close=True)
        time.sleep(2)
          
        as_utilobj.close_canvas_item()
        time.sleep(3)
          
        '''Step 03: In Environments Tree, Domains->CC - AppStudio->AS Framework
                    Double click on ActiveChart
                    Click the Help drop down menu and select Help Topics'''
          
        as_utilobj.select_tree_view_pane_item(select_active_chart) 
        time.sleep(20)
          
        as_utilobj.click_element_using_ui(split_button=locators.help_splitbutton)
        time.sleep(5)
          
        as_utilobj.verify_element_using_ui(verify_msg_3,text_item=verify_chart_help_window)
        time.sleep(5)
          
        '''Step 04: Close App Studio Help window
                    Close ActiveChart tab'''
          
        as_utilobj.verify_element_using_ui(verify_msg_4,window_control_item=help_window,window_close=True)
        time.sleep(2)
          
        as_utilobj.close_canvas_item()
        time.sleep(3) 
         
        '''Step 05: In Environments Tree, Domains->CC - AppStudio->AS Framework
                    Double click on a Document1
                    Click the Help drop down menu and select Help Topics'''
         
        as_utilobj.select_tree_view_pane_item(select_document) 
        time.sleep(10)
        
        as_utilobj.click_element_using_ui(split_button_with_offset=locators.help_splitbutton,x=27,y=10,send_keys=select_document_help_window)
        time.sleep(5)
        
        as_utilobj.verify_element_using_ui(verify_msg_5,text_item=verify_document_help_window)
        time.sleep(5)

        '''Step 06: Close App Studio Help window
                    Select the container on Document Canvas
                    Click the Positioning tab 
                    Click the Help icon'''
                
        as_utilobj.click_element_using_ui(close_window=help_window)
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(tab_item=locators.positioning_tab)
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(split_button_with_offset=locators.help_splitbutton,x=27,y=10,send_keys=select_document_help_window)
        time.sleep(5)
        
        as_utilobj.verify_element_using_ui(verify_msg_6,text_item=verify_document_help_window_for_positioning)
        time.sleep(5)
        
        '''Step 07: Close App Studio Help window
                    Close a Document1 tab'''
        
        as_utilobj.verify_element_using_ui(verify_msg_7,window_control_item=help_window,window_close=True)
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(3) 
        
        '''Step 08: In Environments Tree, Domains->CC - AppStudio->AS Framework
                    Double click on DisneyBallDog
                    Click the Help drop down menu and select Help Topics.'''
        
        as_utilobj.select_tree_view_pane_item(select_html_page) 
        time.sleep(10)
        
        as_utilobj.click_element_using_ui(split_button=locators.help_splitbutton)
        time.sleep(5)
         
        as_utilobj.verify_element_using_ui(verify_msg_8,text_item=verify_html_help_window)
        time.sleep(5)
        
        '''Step 09: Close App Studio Help window
                    Close DisneyBallDog tab'''
        
        as_utilobj.verify_element_using_ui(verify_msg_9,window_control_item=help_window,window_close=True)
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
          
if __name__=='__main__' :
    unittest.main()