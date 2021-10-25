'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287533'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys

class C2287533_TestClass(AS_BaseTestCase):
    def test_C2287533(self): 
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()

        '''Step 01: In Environments Tree, navigate to Web Applications->ibisamp
                    Right-click ibisamp -> New | HTML Page<!--comment-->
                    Type in the editorl
                    <!-- comment -->'''
                  
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                         
        tree_path="Web Applications->ibisamp"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
                   
        as_utilobj.select_component_by_right_click(right_click_folder="ibisamp",click="New",click_sub_menu="HTML Page")
        time.sleep(2)
                  
        keys.typewrite("<!-- comment -->")
        time.sleep(1)
                           
        '''Step 02: Click on the AS menu, click Close
                    Click Yes to save file
                    Click Cancel
                    Close Edit HtmlPage1, click No to save changes prompt'''
    
        as_utilobj.close_canvas_item()
        time.sleep(1)
                 
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
                
        as_utilobj.Verify_Element("EDASERVE Applications","Step 02: Verified - The only visible folder must be 'ibisamp",unavailable=True)
        time.sleep(2)
                    
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
                        
        as_utilobj.select_any_dialog("No")
        time.sleep(2)
                    
        '''Step 03: Right-click ibisamp -> New | Javascript File
                    Type on a new line in the editor:
                    //
                    Close JavaScriptFile1.js by clicking on X
                    Select Yes to save changes'''
                       
        as_utilobj.select_component_by_right_click(right_click_folder="ibisamp",click="New",click_sub_menu="JavaScript File")
        time.sleep(2)
              
        as_utilobj.select_home_button(move_x=961,move_y=640)
                      
        keys.typewrite("//")
        time.sleep(1)
    
        as_utilobj.close_canvas_item()
        time.sleep(3)
                
        as_utilobj.Verify_Element("EDASERVE Applications","Step 03: Verify the only visible folder is 'ibisamp' for Javascript save as dialog",unavailable=True)
        time.sleep(3)
                         
        '''Step 04: Click Cancel
                 Close JavaScriptFile1.js tab , click No to save changes prompt'''
                       
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(2)
            
        as_utilobj.close_canvas_item()
        time.sleep(3)
                        
        as_utilobj.select_any_dialog("No")
        time.sleep(2)
                 
        '''Step 05: In Environments Tree, navigate to localhost->Data Servers->EDASERVE->Applications->baseapp
                    Right-click baseapp->New | Procedure
                    Type TABLE FILE CAR on line 2
                    Click on the AS menu, click Close'''
           
#         as_utilobj.logout_conf_env(webfocus_environment=True)
#         time.sleep(7)
#    
#         tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"local_environment")
#         as_utilobj.select_tree_view_pane_item(tree_path) 
#         time.sleep(3)
#                       
#         as_utilobj.select_tree_view_pane_item("Data Servers->EDASERVE->Applications") 
#         time.sleep(5)
#                 
#         as_utilobj.select_component_by_right_click(right_click_folder="baseapp",click="New",click_sub_menu="Procedure")
#         time.sleep(3)
#           
#         as_utilobj.select_home_button(move_x=940,move_y=570)
#         time.sleep(1)
#           
#         keys.typewrite("TABLE FILE CAR")
#         time.sleep(1)
#           
#         as_utilobj.select_component_by_right_click(right_click_folder="baseapp",click="Refresh Descendants")
#         time.sleep(4)
#              
#         automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
#         time.sleep(2)
#         automation.SendKey(automation.Keys.VK_F, waitTime=3)
#         time.sleep(2)
#         automation.SendKey(automation.Keys.VK_C, waitTime=3)
#         time.sleep(2)
#                  
#         '''Step 06: Select Yes at the save prompt
#                 Click Cancel 
#                 Close the Procedure1.fex tab, click No to save changes prompt'''
#           
#         as_utilobj.select_any_dialog("Yes") 
#         time.sleep(1)       
#            
#         as_utilobj.Verify_Element("EDASERVE Applications","Step 06: Verify the only visible folder is 'baseapp' for save as dialog for procedure in localhost",unavailable=True)
#         time.sleep(2)
#                    
#         as_utilobj.select_any_dialog("Cancel")
#         time.sleep(1)
#          
#         as_utilobj.select_component_by_right_click(right_click_folder="baseapp",click="Refresh Descendants")
#         time.sleep(5)
#                  
#         automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
#         time.sleep(2)
#         automation.SendKey(automation.Keys.VK_F, waitTime=3)
#         time.sleep(2)
#         automation.SendKey(automation.Keys.VK_C, waitTime=3)
#         time.sleep(2) 
#   
#         as_utilobj.select_any_dialog("No") 
#         time.sleep(2)        
#   
#         as_utilobj.logout_conf_env(local_environment=True)
#         time.sleep(3) 
         
        '''Step 07: In Environments Tree, navigate to Domains > Public 
                    Right-click Public -> New | Text Document
                    Type TABLE FILE CAR on line 1
                    Close Edit Text1.txt by clicking on X'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
         
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                     
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
               
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Text Document")
        time.sleep(2)
        
        keys.typewrite("TABLE FILE CAR")
        time.sleep(3)

        as_utilobj.close_canvas_item()
        time.sleep(3)
           
        '''Step 08: Select Yes to save the file
                    Click Cancel
                    Close Edit Text1.txt tab, click No to save changes prompt'''
         
        as_utilobj.select_any_dialog("Yes")   
        time.sleep(3)     
           
        as_utilobj.Verify_Element("EDASERVE Applications","Step 08: Verify the only visible folder is 'AS-Framework' for save as dialog for text document",unavailable=True)
        time.sleep(2)
                   
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
       
        as_utilobj.close_canvas_item()
        time.sleep(3)
  
        as_utilobj.select_any_dialog("No")
        time.sleep(1)         
        
        '''Step 09: Right-click Public folder-> New | Collaborative Portal
                    Click OK
                    Click Create on the Add Page window 
                    Click BIP menu, click Exit
                    Select No to save changes prompt'''
                       
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Collaborative Portal")
        time.sleep(5)
        
        as_utilobj.Verify_Element("EDASERVE Applications","Step 09: Verify the only visible folder is 'AS-Framework' for save as dialog for Collaborative Portal",unavailable=True)
        time.sleep(2)
                   
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(2)
                 
if __name__=='__main__' :
    unittest.main() 