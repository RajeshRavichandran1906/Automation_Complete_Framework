'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287581'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
import pyautogui as keys
from common.lib import as_utility
import keyboard as keys_1

class C2287581_TestClass(AS_BaseTestCase):
    def test_C2287581(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
                
        '''Step 01: From Environments Detail panel, expand Data Servers>EDASERVE>Applications 
                    Right click on baseapp and select New | Text Document
                    Type TABLE FILE CAR
                    Close Edit Text1.txt tab
                    Click Yes to App Studio prompt
                    Click OK'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                      
        as_utilobj.select_tree_view_pane_item("Data Servers->EDASERVE->Applications->ibisamp") 
        time.sleep(2)   
          
        as_utilobj.select_component_by_right_click(right_click_folder="ibisamp",click="New",click_sub_menu="Text Document")
        time.sleep(2)
        
        as_utilobj.select_home_button(move_x=800,move_y=250)
                
        keys_1.write('TABLE FILE CAR')
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)

        as_utilobj.click_element_using_ui(edit_element=True,id="1516",write="c2287581")
        time.sleep(2)
                        
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
           
        '''Step 02: Right-click on otext1.txt and select Rename
                    Type 'ZZtext1Z', hit Enter'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="ibisamp",click="Properties")
        time.sleep(1)
          
        as_utilobj.select_component_by_right_click(right_click_item_env_detail="c2287581.txt",click="Rename")
        time.sleep(1)
          
        keys_1.write('zzc2287581')
        time.sleep(1)
        
        keys.hotkey('enter')
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_item_env_detail="zzc2287581.txt",click="Properties")
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui("Step 02: Verify Filename in edaserve with upcase letter must display correctly FOR NEW FILE RENAME",list_item_exist="zzc2287581.txt",available=True) 
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_item_env_detail="zzc2287581.txt",click="Delete")
        time.sleep(3)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        '''Step 03: From Environments Detail panel, switch to View Items By Name
                    Select ibisamp, right click on carinst.fex and select Rename 
                    Type CCarinst.fex, hit Enter'''
        
        as_utilobj.select_component_by_right_click(right_click_item_env_detail="carinst.fex",click="Rename")
        time.sleep(1)
        
        keys_1.write('ccarinst')
        time.sleep(1)
        
        keys.hotkey('enter')
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_item_env_detail="ccarinst.fex",click="Properties")
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui("Step 03: Verify Filename in edaserve with upcase letter must display correctly FOR EXISTING FILE",list_item_exist="ccarinst.fex",available=True) 
        time.sleep(1)
        
        '''Step 04: Right click on CCarinst.fex and select Rename 
                    Type carinst.fex, hit Enter'''
        
        as_utilobj.select_component_by_right_click(right_click_item_env_detail="ccarinst.fex",click="Rename")
        time.sleep(1)
        
        keys_1.write('carinst')
        time.sleep(1)
        
        keys.hotkey('enter')
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_item_env_detail="ccarinst.fex",click="Properties")
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui("Step 04: Verify Filename reverted back to the old state 'carinst.fex'",list_item_exist="carinst.fex",available=True) 
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()