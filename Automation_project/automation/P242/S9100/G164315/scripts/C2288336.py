'''@author: Adithyaa AK 


Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288336'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time, unittest
from common.lib import as_utility
import keyboard as keys

class C2288336_TestClass(AS_BaseTestCase):
    def test_C2288336(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Configured Environments->Data Servers->EDASERVE->Applications
                    Right click Applications and select New Application Directory 
                    Type 'validate', hit Enter'''
            
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                            
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
             
        tree_path="Data Servers->EDASERVE->Applications"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(6)
             
        as_utilobj.select_component_by_right_click(right_click_folder="Applications",click="New Application Directory")
        time.sleep(3)
             
        keys.write("validate")
        time.sleep(2)
        keys.press('enter')
                 
        as_utilobj.Verify_Element("validate","Step 01: Verified New application appears in the tree",available=True)
        time.sleep(1)
                 
        '''Step 02: Right click application folder validate and select New Application Directory. Leave default name 'newapp'.
                    Hit Enter'''
                           
        as_utilobj.select_component_by_right_click(right_click_folder="validate",click="New",click_sub_menu="Application Directory")
        time.sleep(3)
           
        keys.press('enter')
        time.sleep(1)   
          
        as_utilobj.Verify_Element("newapp","Step 02: Verified 'newapp' Sub application folder shows in the tree under 'validate' folder",available=True)
        time.sleep(1)
                
        '''Step 03: Right click newapp sub application and select New->Report
                    Navigate to ibisamp, select car.mas
                    Click Finish'''
                  
        as_utilobj.select_component_by_right_click(right_click_folder="newapp",click="New",click_sub_menu="Report")
        time.sleep(3)
                           
        as_utilobj.select_file_in_dialogs("Finish",tree_path="ibisamp",select_file="car.mas")
        time.sleep(6)
                   
        as_utilobj.verify_active_tool("App Studio - report1.fex*","Step 03: Verified Report canvas opens without error.")
        time.sleep(1)
                  
        '''Step 04: Double click on COUNTRY and DEALER_COST
                    Click Run in QAT toolbar
                    Close WebFOCUS Report tab
                    Close report1.fex
                    Click Yes to App Studio saving prompt'''
            
        as_utilobj.click_element_using_ui(tree_item="COUNTRY")      
        time.sleep(2)
            
        as_utilobj.click_element_using_ui(tree_item="DEALER_COST")      
        time.sleep(2)
           
        as_utilobj.click_element_using_ui(split_button="Run")      
        time.sleep(8)
                 
        as_utilobj.Verify_Browser_Content("IEFrame","Step 04: Verified DataServer - ",item_list=['COUNTRY','ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY','DEALER_COST','37,853','4,631','41,235','5,512','54,563'],browser_close=True)
        time.sleep(10)
                
        as_utilobj.close_canvas_item()
        time.sleep(3)
                          
        as_utilobj.select_any_dialog("Yes")
        time.sleep(3)
                 
        '''Step 05: Type c2288336 for File name, click OK
                    Right c2288336 and select Run
                    Close WebFOCUS Report tab'''
        
        as_utilobj.select_any_dialog("OK",rename_file="c2288336")      
        time.sleep(2)
              
        tree_path="newapp"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
            
        as_utilobj.select_component_by_right_click(right_click_item="c2288336.fex",click="Run")
        time.sleep(3)
                 
        as_utilobj.Verify_Browser_Content("IEFrame","Step 05: Verified DataServer - ",item_list=['COUNTRY','ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY','DEALER_COST','37,853','4,631','41,235','5,512','54,563'],browser_close=True)
        time.sleep(10)
                        
        '''Step 06: In Environments Tree, Configured Environments->Domains->Public
                    Right click on Public and select New->Folder
                    Type NewPublic, hit Enter 
                    Right click NewPublic sub application and select New->Report
                    Navigate to ibisamp, select car.mas
                    Click Finish'''
                
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                            
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                 
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Folder")    
        time.sleep(1)
             
        keys.write("NewPublic")
        time.sleep(1)     
        keys.press("enter")
        time.sleep(3)
                    
        as_utilobj.select_component_by_right_click(right_click_folder="NewPublic",click="New",click_sub_menu="Report")
        time.sleep(1)
                  
        as_utilobj.select_file_in_dialogs("Finish",tree_path="ibisamp",select_file="car.mas")
        time.sleep(6)
              
        '''Step 07: Double click on COUNTRY and DEALER_COST
                    Click Run in QAT toolbar
                    Close WebFOCUS Report tab
                    Close report1.fex
                    Click Yes to App Studio saving prompt'''
              
        as_utilobj.click_element_using_ui(tree_item="COUNTRY")      
        time.sleep(2)
          
        as_utilobj.click_element_using_ui(tree_item="DEALER_COST")      
        time.sleep(2)
          
        as_utilobj.click_element_using_ui(split_button="Run")      
        time.sleep(10)
                
        as_utilobj.Verify_Browser_Content("IEFrame","Step 07: Verified Report under Domain - ",item_list=['COUNTRY','ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY','DEALER_COST','37,853','4,631','41,235','5,512','54,563'],browser_close=True)
        time.sleep(6)
             
        as_utilobj.close_canvas_item()
        time.sleep(3)
                          
        as_utilobj.select_any_dialog("Yes")
        time.sleep(2)
                 
        '''Step 08: Type c2288336 for File name, click OK
                    Right c2288336 and select Run
                    Close WebFOCUS Report tab'''
         
        as_utilobj.select_any_dialog("OK",rename_file="c2288336")      
        time.sleep(3)
              
        as_utilobj.click_element_using_ui(tree_item="NewPublic")      
        time.sleep(3)
            
        as_utilobj.select_component_by_right_click(right_click_item="c2288336",click="Run")
        time.sleep(8)
               
        as_utilobj.Verify_Browser_Content("IEFrame","Step 08: Verified Report under Domain - ",item_list=['COUNTRY','ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY','DEALER_COST','37,853','4,631','41,235','5,512','54,563'],browser_close=True)
        time.sleep(3)
          
        '''Created Folders need to be deleted for reason of next run'''
         
        as_utilobj.select_component_by_right_click(right_click_folder="NewPublic",click="Delete")
        time.sleep(2)
         
        as_utilobj.select_any_dialog("Yes")
        time.sleep(2) 
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
              
        tree_path="Data Servers->EDASERVE->Applications->validate"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_folder="validate",click="Delete")
        time.sleep(2)
         
        as_utilobj.select_any_dialog("Yes")
        time.sleep(2) 
         
        print("Created folders are deleted for reason of nextrun")
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()