'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287613'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui

class C2287613_TestClass(AS_BaseTestCase):
    def test_C2287613(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
          
        '''Step 01: Public Domains, right click->New Procedure
                    Click on Procedure View panel, right-click the top-level folder and select New ...>Dialogue Mngr> DM If'''
             
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                      
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)     
      
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Procedure")
        time.sleep(5)
              
        as_utilobj.select_home_button(move_x=-52,move_y=170)
                                 
        tree_path="File Procedure1 components"
        as_utilobj.select_tree_view_pane_item(tree_path)
        time.sleep(2)
              
        as_utilobj.select_component_by_right_click(right_click_item="Comment",send_keys=['down','right'],click="Dialogue Mngr",click_sub_menu="DM If")
        time.sleep(8)
                  
        '''Step 02: Close the procedure view tab'''
             
        as_utilobj.select_home_button(move_x=482,move_y=137)
        time.sleep(2)
             
        as_utilobj.Verify_Current_Dialog_Closes("Save As","Step 02: Verified - There must be no error message since no changes were made")
                         
        '''Step 03: Click on Procedure View panel, right-click the top-level folder and select New ...>Dialogue Mngr> DM If
                    Change the Label value on the -IF (first line) to NEXTAREA
                    Close the DM If tab'''
                         
        as_utilobj.select_home_button(move_x=-52,move_y=170)
    
        tree_path="File Procedure1 components"
        as_utilobj.select_tree_view_pane_item(tree_path)
        time.sleep(3)
            
        as_utilobj.select_component_by_right_click(right_click_item="Comment",send_keys=['down','right'],click="Dialogue Mngr",click_sub_menu="DM If")
        time.sleep(5)
                 
        as_utilobj.select_home_button()
            
        as_utilobj.double_click_element_using_offset(1170,440)
        time.sleep(1)
            
        pyautogui.typewrite(('NEXTAREA'), interval=0.25)
        time.sleep(2)
        pyautogui.press(['enter','enter'])
        time.sleep(2) 
                 
        as_utilobj.select_home_button(move_x=482,move_y=137)
            
        as_utilobj.Verify_Current_Dialog_Opens("App Studio","Step 03: Verified - There must be a error message 'Please enter a valid conditional expression!'")
                 
        '''Step 04: Click OK to close the error message
                    Delete NEXTAREA from the label using the space bar
                    Click OK
                    Close the DM If tab'''
         
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
            
        as_utilobj.select_home_button()
        time.sleep(1)
        as_utilobj.double_click_element_using_offset(1170,440)
        time.sleep(1)
            
        pyautogui.press('space')
                     
        as_utilobj.select_home_button(move_x=482,move_y=137) 
        time.sleep(2)
            
        as_utilobj.Verify_Current_Dialog_Opens("App Studio","Step 04: Verified - There must be a error message 'Please enter a valid conditional expression!'")
                        
        as_utilobj.select_any_dialog("OK")
                   
        as_utilobj.select_home_button()
        time.sleep(1)
        as_utilobj.double_click_element_using_offset(1170,440)
        time.sleep(2)
                 
        pyautogui.press('del')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(2)
             
        as_utilobj.select_home_button(move_x=482,move_y=137) 
        time.sleep(2)
                        
        '''Step 05: Click on Procedure View panel, right-click the top-level folder and select New ...>Dialogue Mngr>DM Goto 
                    Close DM Goto tab'''
            
        as_utilobj.select_home_button(move_x=-52,move_y=170) 
        time.sleep(2)
            
        as_utilobj.select_component_by_right_click(right_click_item="Comment",send_keys=['down','right'],click="Dialogue Mngr",click_sub_menu="DM Goto")
        time.sleep(5)
                          
        as_utilobj.select_home_button()
        time.sleep(1)
            
        as_utilobj.Verify_Element("DM Goto","Step 05: Verified - DM-GOTO Editor been displayed",available=True)
        time.sleep(3)
                           
        as_utilobj.select_home_button(move_x=482,move_y=137) 
        time.sleep(2)
              
        '''Step 06: Click on Procedure View panel, right-click the top-level folder and select New ...>Dialogue Mngr>DM Label
                    Close DM Label tab'''
                      
        as_utilobj.select_home_button(move_x=-52,move_y=170) 
        time.sleep(2)
                      
        as_utilobj.select_component_by_right_click(right_click_item="Comment",send_keys=['down','right'],click="Dialogue Mngr",click_sub_menu="DM Label")
        time.sleep(5)
                 
        as_utilobj.select_home_button()
        time.sleep(1)
            
        as_utilobj.Verify_Element("DM Label","Step 06: Verified - DM Label Editor been displayed",available=True)
               
        as_utilobj.select_home_button(move_x=483,move_y=137)              
        time.sleep(2)
           
        '''Step 07: Click on Procedure View panel, right-click the top-level folder and select New ...>Dialogue Mngr>DM Repeat 
                    Change the first line's FOR value to x, hit Enter
                    Close DM Repeat tab
                    Click OK'''
         
        as_utilobj.select_home_button(move_x=-52,move_y=170)              
        time.sleep(2)
                 
        as_utilobj.select_component_by_right_click(right_click_item="Comment",send_keys=['down','right'],click="Dialogue Mngr",click_sub_menu="DM Repeat")
        time.sleep(5)
        
        as_utilobj.Verify_Element("DM Repeat","Step 07: Verified - DM Repeat Editor been displayed",available=True)  
        time.sleep(1)
         
        as_utilobj.select_home_button()
        time.sleep(1)
        
        as_utilobj.double_click_element_using_offset(1445,472)
        time.sleep(1)
        
        pyautogui.typewrite('x')
        pyautogui.press("enter")
        time.sleep(2)
        
        as_utilobj.select_home_button(move_x=482,move_y=137)
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Opens("App Studio","Step 08: Verified - There must be a error message 'Please enter a valid conditional expression!'")   
        time.sleep(1)
        
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
         
        '''Step 08: Highlight the FOR value x
                    Hit the Delete key
                    Hit Enter
                    Close DM Repeat tab'''
         
        as_utilobj.select_home_button()
        time.sleep(1)
        
        as_utilobj.double_click_element_using_offset(1445,472)
        time.sleep(1)
        pyautogui.press("delete")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(2)
         
        '''Step 08: Close DM Repeat tab
                    Click on Procedure View panel, right-click the top-level folder and select New ...>Dialogue Mngr>Dialogue Mngr
                    Close Dialogue Mngr tab
                    Close Procedure1 tab'''
         
        as_utilobj.select_home_button(move_x=482,move_y=137)
        time.sleep(1)
        
        as_utilobj.select_home_button(move_x=-52,move_y=170) 
        time.sleep(1)
                 
        as_utilobj.select_component_by_right_click(right_click_item="Comment",send_keys=['down','right'],click="Dialogue Mngr",click_sub_menu="Dialogue Mngr")
        time.sleep(5)
         
        as_utilobj.select_home_button(move_x=515,move_y=137) 
        time.sleep(3)
        
        as_utilobj.close_canvas_item() 
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()    