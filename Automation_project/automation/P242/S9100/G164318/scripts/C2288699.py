'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288699'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2288699_TestClass(AS_BaseTestCase):
    def test_C2288699(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        base_file_repository="Domains->S9100"
        expand_base_app="Web Applications->baseapp"
        baseapp="baseapp"
        ie_browser="IEFrame"
        select_ibcomposer_execute="IbComposer execute"
        select_ibcomposer_under_webapp="IbComposer_execute.htm"
        
        '''Testcase verification'''
        
        verify_report_table=['Testing API IbComposer_execute for reports','COUNTRY','CAR','MODEL','SALES','ENGLAND','JAGUAR','V12XKE AUTO']
        verify_button_list=['Display Report in New Window','Display Report in Target','Display Report in Frame']
        verify_msg_1="Step 2.1: Verify html file invoked in ie browser"
        verify_msg_2="Step 2.2: Verify table item existing : "
        verify_msg_3="Step 2.2: Verify buttons existing : "
        
                
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, navigate to Domains->CC - AppStudio->API Validation folder and Expand
                    Right click on ibComposer execute and select Copy'''
              
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                      
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
            
        as_utilobj.select_tree_view_pane_item(base_file_repository)
        time.sleep(2)
                      
        as_utilobj.select_component_by_right_click(right_click_item=select_ibcomposer_execute,click=component_locators.copy) 
        time.sleep(2)
          
        '''Step 02: Navigate to Web Applications
                    Right click on baseapp and select Paste
                    Right click on ibComposer_ execute.htm and select Run on Web Server
                    Close HtmlPage output tab 
                    Collapse Domains'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
           
        as_utilobj.select_tree_view_pane_item(expand_base_app)
        time.sleep(2)
           
        as_utilobj.select_component_by_right_click(right_click_folder=baseapp,click=component_locators.paste) 
        time.sleep(2)
           
        as_utilobj.select_component_by_right_click(right_click_folder=baseapp,click=component_locators.refresh_descendants) 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_item=select_ibcomposer_under_webapp,click=component_locators.run_on_web_server) 
        time.sleep(20)
        
        as_utilobj.Verify_Browser_Content(ie_browser,verify_msg_1)
        time.sleep(2)
        
        as_utilobj.Verify_Browser_Content(ie_browser,verify_msg_2,item_list=verify_report_table)
        time.sleep(2)
        
        as_utilobj.Verify_Browser_Content(ie_browser,verify_msg_3,button_list=verify_button_list,browser_close=True)
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_item=select_ibcomposer_under_webapp,click=component_locators.delete) 
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(2)
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()