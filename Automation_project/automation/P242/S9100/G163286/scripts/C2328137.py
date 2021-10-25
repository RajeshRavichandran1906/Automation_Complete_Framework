'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2328137'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators

class C2328137_TestClass(AS_BaseTestCase):
    def test_C2328137(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        configured_environments="Configured Environments"
        expand_till_folder="Domains->S9100"
        select_domains="Domains"
        select_folder="S9100"
        expand_till_ibisamp="Data Servers->EDASERVE->Applications->ibisamp"
        select_data_server="Data Servers"
        select_edaserve="EDASERVE"
        select_applications="Applications"
        select_ibisamp="ibisamp"
        select_master_file="carinst2.fex"
        sleep=[1,2,3,4,5,6,7,8,9,10,11] 
        run_drop_down=[25,10]
        
        '''Testcase verification'''
        
        verify_run_dropdown="step10_C2328137.png"
        verify_msg_1="Step 01: Verify Run icon in the Quick Access Tool bar is disabled"
        verify_msg_2="Step 02: Verify Run icon in the Quick Access Tool bar is disabled"
        verify_msg_3="Step 03: Verify Run icon in the Quick Access Tool bar is disabled"
        verify_msg_4="Step 04: Verify Run icon in the Quick Access Tool bar is disabled"
        verify_msg_5="Step 05: Verify Run icon in the Quick Access Tool bar is disabled"
        verify_msg_6="Step 06: Verify Run icon in the Quick Access Tool bar is disabled"
        verify_msg_7="Step 07: Verify Run icon in the Quick Access Tool bar is disabled"
        verify_msg_8="Step 08: Verify Run icon in the Quick Access Tool bar is enabled"
        verify_msg_9="Step 09: Verify drop down menu expands"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
         
        '''Step 01: Click Configured Environments in the Environments Tree panel'''
           
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
                       
        as_utilobj.select_tree_view_pane_item(configured_environments) 
        time.sleep(sleep[2])
           
        as_utilobj.verify_element_using_ui(verify_msg_1,split_button_item=locators.run_splitbutton,disabled=True)
        time.sleep(sleep[1])
           
        as_utilobj.select_tree_view_pane_item(configured_environments) 
        time.sleep(sleep[2])
           
        '''Step 02: Click Domains'''
           
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
           
        as_utilobj.select_tree_view_pane_item(expand_till_folder) 
        time.sleep(sleep[2])
          
        as_utilobj.select_file(tree_item=select_domains)
        time.sleep(sleep[2])
           
        as_utilobj.verify_element_using_ui(verify_msg_2,split_button_item=locators.run_splitbutton,disabled=True)
        time.sleep(sleep[1])
           
        '''Step 03: Click any folder under domains'''
          
        as_utilobj.select_file(tree_item=select_folder)
        time.sleep(sleep[2]) 
           
        as_utilobj.verify_element_using_ui(verify_msg_3,split_button_item=locators.run_splitbutton,disabled=True)
        time.sleep(sleep[1]) 
           
        '''Step 04 & 05: Select Data servers'''
           
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[3])
           
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[4])
           
        as_utilobj.select_tree_view_pane_item(expand_till_ibisamp) 
        time.sleep(sleep[2])
          
        as_utilobj.select_file(tree_item=select_data_server) 
        time.sleep(sleep[2])
           
        as_utilobj.verify_element_using_ui(verify_msg_4,split_button_item=locators.run_splitbutton,disabled=True)
        time.sleep(sleep[1]) 
           
        '''Step 06: Expand Data Servers and select EDASERVE'''
          
        as_utilobj.select_file(tree_item=select_edaserve) 
        time.sleep(sleep[2]) 
           
        as_utilobj.verify_element_using_ui(verify_msg_5,split_button_item=locators.run_splitbutton,disabled=True)
        time.sleep(sleep[1]) 
           
        '''Step 07: Expand EDASERVE and select Applications'''
          
        as_utilobj.select_file(tree_item=select_applications) 
        time.sleep(sleep[2]) 
  
        as_utilobj.verify_element_using_ui(verify_msg_6,split_button_item=locators.run_splitbutton,disabled=True)
        time.sleep(sleep[1]) 
           
        '''Step 08: Expand Applications and select ibisamp'''
          
        as_utilobj.select_file(tree_item=select_ibisamp) 
        time.sleep(sleep[2]) 
          
        as_utilobj.verify_element_using_ui(verify_msg_7,split_button_item=locators.run_splitbutton,disabled=True)
        time.sleep(sleep[1]) 
           
        '''Step 09: Expand ibisamp and select carinst2.fex
                    Double click on carinst2.fex'''
         
        as_utilobj.select_tree_view_pane_item(select_master_file)
        time.sleep(12)
         
        as_utilobj.verify_element_using_ui(verify_msg_8,split_button_item=locators.run_splitbutton,enabled=True)
        time.sleep(sleep[1]) 
         
        '''Step 10: Click on drop down arrow next to the Run icon
                    Close carinst2.fex tab
                    Click No to App Studio saving prompt message'''
        
        as_utilobj.click_element_using_ui(split_button_with_offset=locators.run_splitbutton,x=run_drop_down[0],y=run_drop_down[1])
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli(verify_run_dropdown,verify_msg_9)
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)

if __name__=='__main__' :
    unittest.main() 