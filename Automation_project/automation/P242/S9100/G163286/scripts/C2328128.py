'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2328128'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2328128_TestClass(AS_BaseTestCase):
    def test_C2328128(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
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
        
        '''Testcase verification'''
        
        verify_button_enable="Open..."
        verify_msg_1="Step 01: Verify Open is enabled on selecting configured environments"
        verify_msg_2="Step 02: Verify Open is enabled on selecting domains"
        verify_msg_3="Step 03: Verify Open is enabled on selecting folder"
        verify_msg_4="Step 04: Verify Open is enabled on selecting data server folder"
        verify_msg_5="Step 05: Verify Open is enabled on selecting EDASERVE"
        verify_msg_6="Step 06: Verify Open is enabled on selecting Applications"
        verify_msg_7="Step 07: Verify Open is enabled on selecting ibisamp"
        verify_msg_8="Step 08: Verify Open is enabled on selecting master file"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click Configured Environments in the Environments Tree panel'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
                     
        as_utilobj.select_tree_view_pane_item(configured_environments) 
        time.sleep(sleep[2])
         
        as_utilobj.verify_element_using_ui(verify_msg_1,button_item=verify_button_enable,enabled=True)
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
         
        as_utilobj.verify_element_using_ui(verify_msg_2,button_item=verify_button_enable,enabled=True)
        time.sleep(sleep[1])
         
        '''Step 03: Click any folder under domains'''
        
        as_utilobj.select_file(tree_item=select_folder)
        time.sleep(sleep[2]) 
         
        as_utilobj.verify_element_using_ui(verify_msg_3,button_item=verify_button_enable,enabled=True)
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
         
        as_utilobj.verify_element_using_ui(verify_msg_4,button_item=verify_button_enable,enabled=True)
        time.sleep(sleep[1]) 
         
        '''Step 06: Expand Data Servers and select EDASERVE'''
        
        as_utilobj.select_file(tree_item=select_edaserve) 
        time.sleep(sleep[2]) 
         
        as_utilobj.verify_element_using_ui(verify_msg_5,button_item=verify_button_enable,enabled=True)
        time.sleep(sleep[1]) 
         
        '''Step 07: Expand EDASERVE and select Applications'''
        
        as_utilobj.select_file(tree_item=select_applications) 
        time.sleep(sleep[2]) 

        as_utilobj.verify_element_using_ui(verify_msg_6,button_item=verify_button_enable,enabled=True)
        time.sleep(sleep[1]) 
         
        '''Step 08: Expand Applications and select ibisamp'''
        
        as_utilobj.select_file(tree_item=select_ibisamp) 
        time.sleep(sleep[2]) 
        
        as_utilobj.verify_element_using_ui(verify_msg_7,button_item=verify_button_enable,enabled=True)
        time.sleep(sleep[1]) 
         
        '''Step 09: Expand ibisamp and select carinst2.fex'''
        
        as_utilobj.select_file(tree_item=select_master_file)
        time.sleep(sleep[2])
         
        as_utilobj.verify_element_using_ui(verify_msg_8,button_item=verify_button_enable,enabled=True)
        time.sleep(sleep[1]) 
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
        
if __name__=='__main__' :
    unittest.main() 