'''
@author: Adithyaa AK

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667307'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C6667307_TestClass(AS_BaseTestCase):
    def test_C6667307(self):
        
        '''Creating Object Instance'''
        
        driver = self.driver 
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
           
        '''Step 01a: Right-click Domains>ContextMenu and select New | Procedure
                    In Procedure View panel, right-click the top-level folder and select New...| Define'''
                  
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                        
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                               
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
                   
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Procedure")
        time.sleep(2)
      
        as_utilobj.select_home_button(move_x=-52,move_y=170)
        time.sleep(1)
                 
        as_utilobj.select_component_by_right_click(right_click_folder="Comment",click="New ...",click_sub_menu="Define")
        time.sleep(2)
                    
        '''Step 02: Enlarge the Select Data Source window by grabbing at the bottom
            Click ibisamp'''
               
        as_utilobj.verify_dialog_properties("Select Data Source",1755,835,resize_verification_msg="Step 02: Verify the file property fields Size, Type, Last Modified and Location gets larger with the dialog for DEFINE")
        time.sleep(1)    
                                          
        '''Step 03: Resize the Select Data Source window smaller
                    Click Cancel'''
       
        as_utilobj.verify_dialog_properties("Select Data Source",1000,835,verification_msg="Step 03: Verify the file property fields Size, Type, Last Modified and Location gets smaller with the dialog for DEFINE")
        time.sleep(1) 
               
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)     
                        
        '''Step 04: In Procedure View panel, right-click the top-level folder and select New...| Join
                    Enlarge the Select Data Source window by grabbing at the bottom
                    Click ibisamp'''
               
        as_utilobj.select_home_button(move_x=-52,move_y=170)
        time.sleep(1)
                 
        as_utilobj.select_component_by_right_click(right_click_folder="Comment",click="New ...",click_sub_menu="Join")
        time.sleep(2)
               
        as_utilobj.click_element_using_ui(tree_item_select="ibisamp")
               
        as_utilobj.verify_dialog_properties("Select Data Source",1755,835,resize_verification_msg="Step 04: Verify the file property fields Size, Type, Last Modified and Location move with the dialog for JOIN")
        time.sleep(1) 
                                    
        '''Step 05: Resize the Select Data Source window smaller
                    Click Cancel'''
                  
        as_utilobj.verify_dialog_properties("Select Data Source",1000,835,verification_msg="Step 05: Verify the file property fields Size, Type, Last Modified and Location gets smaller with the dialog for JOIN")
        time.sleep(1) 
               
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)   
              
        '''Step 06a: In Procedure View panel, right-click the top-level folder and select New...| Use (click Browse... to show the Open File window
            Navigate to Data Servers>EDASERVE>Applications>ibisamp'''
      
        as_utilobj.select_home_button(move_x=-52,move_y=170)
        time.sleep(1)
                
        as_utilobj.select_component_by_right_click(right_click_folder="Comment",click="New ...",click_sub_menu="Use")
        time.sleep(2)
             
        as_utilobj.select_home_button(move_x=1102,move_y=538)
                 
        '''Step 06b: Enlarge the Select Data Source window by grabbing at the bottom
            Resize the Select Data Source window smaller'''
              
        as_utilobj.verify_dialog_properties("Open File",1755,835,resize_verification_msg="Step 06b: Verify the file property fields Size, Type, Last Modified and Location move with the dialog for Use")
        time.sleep(1) 
                                          
        '''Step 06c: Resize the Select Data Source window smaller
                     Click Cancel'''
                  
        as_utilobj.verify_dialog_properties("Open File",1400,835,verification_msg="Step 06c: Verify the file property fields Size, Type, Last Modified and Location gets smaller with the dialog for USE")
        time.sleep(1) 
               
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)  
             
        as_utilobj.select_home_button(move_x=493,move_y=138)
        time.sleep(1)               
            
        '''Step 07a: In Procedure View panel, right-click the top-level folder and select New...| Allocation'''
                 
        as_utilobj.select_home_button(move_x=-52,move_y=170)
        time.sleep(1)
                
        as_utilobj.select_component_by_right_click(right_click_folder="Comment",click="New ...",click_sub_menu="Allocation")
        time.sleep(2)
                 
        '''Step 07b: Click Next
                    Type AS2498 for Logical Name, click Next
                    Click Next
                    Click ibisamp, click Next
                    Click .... in Filename window'''
                 
        as_utilobj.click_element_using_ui(button_item=True,id="12324")
              
        as_utilobj.click_element_using_ui(edit_element=True,id="50012",write="AS2498")
      
        as_utilobj.click_element_using_ui(button_item=True,id="12324")
              
        as_utilobj.click_element_using_ui(button_item=True,id="12324")
             
        as_utilobj.select_home_button(move_x=896,move_y=576)
                
        as_utilobj.click_element_using_ui(button_item=True,id="12324")
              
        as_utilobj.click_element_using_ui(button_item=True,id="50023") 
             
        '''Step 07c: Navigate to Data Servers>EDASERVE>Applications> double click on caster
                    Enlarge the Select Data Source window by grabbing at the bottom'''
             
        as_utilobj.verify_dialog_properties("Open File",1755,835,resize_verification_msg="Step 07c: Verify the file property fields Size, Type, Last Modified and Location gets larger with the dialog for Allocation")
        time.sleep(1) 
             
        '''Step 07d: Resize the Select Data Source window smaller
                    Click Cancel'''
             
        as_utilobj.verify_dialog_properties("Open File",1400,835,verification_msg="Step 07d: Verify the file property fields Size, Type, Last Modified and Location gets smaller with the dialog for Allocation")
        time.sleep(1) 
               
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1) 
             
        as_utilobj.select_home_button(move_x=493,move_y=138)
        time.sleep(1)
             
        '''Step 08: In Procedure View panel, right-click the top-level folder and select New...| Execute
                    Click Cancel'''
            
        as_utilobj.select_home_button(move_x=-52,move_y=170)
        time.sleep(1)
              
        as_utilobj.select_component_by_right_click(right_click_folder="Comment",click="New ...",click_sub_menu="Execute")
        time.sleep(2)
            
        as_utilobj.verify_dialog_properties("Open File",1755,835,resize_verification_msg="Step 08a: Verify the file property fields Size, Type, Last Modified and Location gets larger with the dialog for Execute")
        time.sleep(1) 
            
        as_utilobj.verify_dialog_properties("Open File",1400,835,verification_msg="Step 08b: Verify the file property fields Size, Type, Last Modified and Location gets smaller with the dialog for Execute")
        time.sleep(1) 
             
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
            
        '''Step 09: In Procedure View panel, right-click the top-level folder and select New...| HTMLForm | Referenced
                    Navigate to CC - AppStudio->AS Files
                    Enlarge the Select Data Source window by the right side of the window
                    Resize the Select Data Source window smaller
                    Click Cancel'''
            
        as_utilobj.select_home_button(move_x=-52,move_y=170)
              
        as_utilobj.select_component_by_right_click(right_click_folder="Comment",send_keys=['down','right'],click="HtmlForm",click_sub_menu="Referenced")
        time.sleep(2)
            
        as_utilobj.verify_dialog_properties("Open File",1755,835,resize_verification_msg="Step 09a: Verify the file property fields Size, Type, Last Modified and Location gets larger with the dialog for Referenced")
        time.sleep(1) 
            
        as_utilobj.verify_dialog_properties("Open File",1400,835,verification_msg="Step 09b: Verify the file property fields Size, Type, Last Modified and Location gets smaller with the dialog for Referenced")
        time.sleep(1) 
             
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
            
        '''Step 10: In Procedure View panel, right-click the top-level folder and select New...| Include
                    Navigate to CC - AppStudio->AS Files
                    Enlarge the Select Data Source window by the right side of the window
                    Resize the Select Data Source window smaller
                    Click Cancel''' 
            
        as_utilobj.select_home_button(move_x=-52,move_y=170)
              
        as_utilobj.select_component_by_right_click(right_click_folder="Comment",click="New ...",click_sub_menu="Include")
        time.sleep(2)
            
        as_utilobj.verify_dialog_properties("Open File",1755,835,resize_verification_msg="Step 10a: Verify the file property fields Size, Type, Last Modified and Location gets larger with the dialog for Include")
        time.sleep(1) 
            
        as_utilobj.verify_dialog_properties("Open File",1400,835,verification_msg="Step 10b: Verify the file property fields Size, Type, Last Modified and Location gets smaller with the dialog for Include")
        time.sleep(1) 
             
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
          
        '''Step 11: In Procedure View panel, right-click the top-level folder and select New...| Match
                    Navigate to Data Servers>EDASERVE>Applications> double click on caster
                    Enlarge the Select Data Source window by the right side of the window
                    Resize the Select Data Source window smaller
                    Click Cancel'''
           
        as_utilobj.select_home_button(move_x=-52,move_y=170)
             
        as_utilobj.select_component_by_right_click(right_click_folder="Comment",click="New ...",click_sub_menu="Match")
        time.sleep(2)
           
        as_utilobj.verify_dialog_properties("Select Data Source",1755,835,resize_verification_msg="Step 11a: Verify the file property fields Size, Type, Last Modified and Location move with the dialog for Match")
        time.sleep(1) 
                
        as_utilobj.verify_dialog_properties("Select Data Source",1000,835,verification_msg="Step 11b: Verify the file property fields Size, Type, Last Modified and Location gets smaller with the dialog for Match")
        time.sleep(1) 
            
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1) 
                  
        '''Step 12: Click AS menu->Save
                Enlarge the Save As window by the right side of the window
                Resize the Save As window smaller
                Click Cancel'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(1)
 
        as_utilobj.select_application_menu_options(send_keys=['down','down'])
        time.sleep(2)
         
        as_utilobj.verify_dialog_properties("Save As",1755,835,resize_verification_msg="Step 12a: Verify the file property fields Size, Type, Last Modified and Location move with the save as dialog for procedure")
        time.sleep(1) 
              
        as_utilobj.verify_dialog_properties("Save As",1000,835,verification_msg="Step 12b: Verify the file property fields Size, Type, Last Modified and Location gets smaller with the save as dialog for procedure")
        time.sleep(1) 
          
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1) 
         
        '''Step 13: Close Procedure1
                    Click No for "Do you want to save the changes to file Procedure1"'''
         
        as_utilobj.close_canvas_item()
        time.sleep(3) 
         
        as_utilobj.select_any_dialog("No")
        time.sleep(1)
  
        '''Step 14: Right-click Domains>ContextMenu and select New | Report
                    Click on ibisamp->car.mas
                    Click OK
                    Click AS menu->Save
                    Type as2948 for File name'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Report")
        time.sleep(2)
        
        as_utilobj.select_file_in_dialogs("OK",tree_path="ibisamp",select_file="car.mas")
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(2)
        
        as_utilobj.select_application_menu_options(send_keys=['down','down'])
        time.sleep(1)
        
        as_utilobj.verify_dialog_properties("Save As",1755,835,resize_verification_msg="Step 14a: Verify the file property fields Size, Type, Last Modified and Location move with the save as dialog for Report")
        time.sleep(1) 
             
        '''Step 15: Resize the Save As window
                    Click Cancel
                    Close Report1'''
        
        as_utilobj.verify_dialog_properties("Save As",1000,835,verification_msg="Step 14b: Verify the file property fields Size, Type, Last Modified and Location gets smaller with the save as dialog for Report")
        time.sleep(1) 
         
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        as_utilobj.select_home_button(move_x=364,move_y=114)
        time.sleep(1)

if __name__=='__main__' :
    unittest.main()