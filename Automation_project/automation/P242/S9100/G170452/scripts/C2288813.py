'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288813'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2288810_TestClass(AS_BaseTestCase):
    def test_C2288813(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_domains="Domains"
        select_framework_folder="S9100"
        select_data_server="Data Servers"
        select_edaserve="EDASERVE"
        select_application_folder="Applications"
        select_baseapp="baseapp"
        select_web_applications="Web Applications"
        select_ibisamp="ibisamp"
        select_html_file="wfmstart.html"
        
        '''Testcase verification'''
        
        verify_save_as="step1_C2288813.png"
        verify_msg_1="Step 01: Verify save options is disabled on domains"
        verify_msg_2="Step 02: Verify save options is disabled on framework folder"
        verify_msg_3="Step 03: Verify save options is disabled on data servers"
        verify_msg_4="Step 04: Verify save options is disabled on edaserve"
        verify_msg_5="Step 05: Verify save options is disabled on applications"
        verify_msg_6="Step 06: Verify save options is disabled on baseapp"
        verify_msg_7="Step 07: Verify save options is disabled on web applications"
        verify_msg_8="Step 08: Verify save options is disabled on ibisamp"
        verify_msg_9="Step 09: Verify save options is disabled on wfmstart"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, select Domains
                    Click the AS logo'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                  
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                  
        as_utilobj.select_tree_view_pane_item(select_domains) 
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_save_as,verify_msg_1)
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
        
        '''Step 02: In Environments Tree, Domains
                    Select CC - AppStudio
                    Click the AS logo'''
        
        as_utilobj.select_tree_view_pane_item(select_framework_folder) 
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_save_as,verify_msg_2)
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
        
        '''Step 03: Navigate to Data Servers- and select 
                    Click the AS logo'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                  
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                  
        as_utilobj.select_tree_view_pane_item(select_data_server) 
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_save_as,verify_msg_3)
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
        
        '''Step 04: Expand Data Servers
                    Select EDASERVE
                    Click the AS logo'''
        
        as_utilobj.select_tree_view_pane_item(select_edaserve) 
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_save_as,verify_msg_4)
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
        
        '''Step 05: Expand EDASERVE
                    Select Applications folder
                    Click the AS logo'''
        
        as_utilobj.select_tree_view_pane_item(select_application_folder) 
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_save_as,verify_msg_5)
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
        
        '''Step 06: Expand Applications folder
                    Expand baseapp
                    Select profile.fex
                    Click the AS logo 
                    Collapse Data Servers'''
        
        as_utilobj.select_tree_view_pane_item(select_baseapp) 
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_save_as,verify_msg_6)
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
        
        '''Step 07: Navigate to Web Applications and select
                    Click the AS logo
                    Expand Web Applications'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                  
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                  
        as_utilobj.select_tree_view_pane_item(select_web_applications) 
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_save_as,verify_msg_7)
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
        
        '''Step 08: Select ibisamp
                    Click the AS logo
                    Expand ibisamp'''
            
        as_utilobj.select_tree_view_pane_item(select_ibisamp) 
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_save_as,verify_msg_8)
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
                    
        '''Step 09: Select wfmstart.html
                    Click the AS logo
                    Collapse Web Applications'''
        
        as_utilobj.select_file(tree_item=select_html_file) 
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_save_as,verify_msg_9)
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)  
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                            
        
if __name__=='__main__' :
    unittest.main()