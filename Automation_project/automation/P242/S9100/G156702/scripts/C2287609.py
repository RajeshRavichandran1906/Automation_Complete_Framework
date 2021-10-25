'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287609'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys
import keyboard as v_keys

class C2287609_TestClass(AS_BaseTestCase):
    def test_C2287609(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        file_path="Data Servers->EDASERVE->Applications->ibisamp"
        cargraph_file="cargraph.fex"
        select_folders=["File cargraph.fex components"]
        click_items=["Run complete procedure","Optional Parameters","Report","Native Canvas","Source","OK","Yes","No","Open"]
        browser="IEFrame"
        write=["-DEFAULT FORMAT = HTML","SUMMARY","SUM"]
        key_pattern=['down','down','right']
        key_press="enter"
        offset_values=[381,137,-52,170,84,95,295,155,303,174,388,114]
        sleep=[1,2,3,4,5,6,7,8,9] 
        
        '''Testcase verification'''

        verify_images=["step2_C2287609.png"]
        verify_msg_1="skip Msg"
        verify_msg_2="Step 03: Verify browser opens with graph in HTML format"
        verify_msg_3="Step 05: Verify error parsing request been displayed"
        verify_msg_4="Step 07: Verify browser opens with graph in HTML format"
        verify_browser_pane="Powered by WebFOCUS - Internet Explorer"
        verify_dialog="Error parsing report request"
        
        '''Testscript'''
    
        as_utilobj.select_home_button()
         
        '''Step 01: Navigate to Data Servers>EDASERVE>Applications>ibisamp 
                    Double click on cargraph.fex
                    Click on X next to Report tab'''
            
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
                                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
                           
        as_utilobj.select_tree_view_pane_item(file_path) 
        time.sleep(sleep[3])
        
        as_utilobj.select_component_by_right_click(right_click_item=cargraph_file,click=click_items[8])
        time.sleep(sleep[3])    
         
        as_utilobj.select_home_button(move_x=offset_values[0],move_y=offset_values[1])
        time.sleep(sleep[2])
           
        '''Step 02: Click on Procedure View panel
                    Right-click the top level folder and select "Run complete procedure"
                    Close the browser page'''
            
        as_utilobj.select_home_button(move_x=offset_values[2],move_y=offset_values[3])
        time.sleep(sleep[0])
                
        as_utilobj.select_component_by_right_click(right_click_folder=select_folders[0],click=click_items[0])
        time.sleep(sleep[3])
            
        as_utilobj.verify_picture_using_sikuli(verify_images[0],verify_msg_2)
            
        as_utilobj.Verify_Browser_Content(browser,verify_msg_1,browser_close=True)
          
        '''Step 03: Click on Procedure View panel
                    Double-click the Optional Parameters component 
                    Change PDF to HTML
                    Right-click top level folder and select Run complete procedure
                    Close the Browser page'''
           
        as_utilobj.select_home_button(move_x=offset_values[2],move_y=offset_values[3])
        time.sleep(sleep[0])
           
        as_utilobj.double_click_element_using_offset(offset_values[4],offset_values[5]) 
        time.sleep(sleep[1])
           
        as_utilobj.select_home_button(move_x=offset_values[6],move_y=offset_values[7])
        time.sleep(sleep[0])
         
        v_keys.write(write[0])
        time.sleep(sleep[0])
   
        as_utilobj.select_home_button(move_x=offset_values[2],move_y=offset_values[3])
        time.sleep(sleep[0])
           
        as_utilobj.select_component_by_right_click(right_click_folder=select_folders[0],click=click_items[0])
        time.sleep(sleep[3])
           
        as_utilobj.Verify_Browser_Content(browser,verify_msg_2,verify_pane=verify_browser_pane,browser_close=True)
        time.sleep(sleep[1])    
          
        '''Step 04: Click on Procedure View panel
                    Right-click the Report component and select Open with... | Native Canvas
                    Click the Source tab at the bottom of the Report component'''
          
        as_utilobj.select_home_button(move_x=offset_values[2],move_y=offset_values[3])
        time.sleep(sleep[0])
      
        as_utilobj.select_component_by_right_click(right_click_item=click_items[2],send_keys=key_pattern,click=click_items[3])
        time.sleep(sleep[0])
          
        as_utilobj.click_element_using_ui(tab_item=click_items[4])
          
        '''Step 05: Change SUM to SUMMARY
                    Click on Procedure View panel
                    Right-click top level folder and select Run complete procedure'''
          
        as_utilobj.select_home_button(move_x=offset_values[8],move_y=offset_values[9])
          
        v_keys.write(write[1])
 
        keys.hotkey(key_press)
        time.sleep(sleep[0])
          
        as_utilobj.select_home_button(move_x=offset_values[2],move_y=offset_values[3])
        time.sleep(sleep[0])
           
        as_utilobj.select_component_by_right_click(right_click_folder=select_folders[0],click=click_items[0])
        time.sleep(sleep[3])
          
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_3)
          
        '''Step 06: Click OK on the Error parsing error request window'''
          
        as_utilobj.select_any_dialog(click_items[5])
          
        '''Step 07: Click Yes on message box
                    Close the browser page
                    Change SUMMARY to SUM'''
          
        as_utilobj.select_any_dialog(click_items[6])
        time.sleep(sleep[1])
          
        as_utilobj.Verify_Browser_Content(browser,verify_msg_4,verify_pane=verify_browser_pane,browser_close=True)
        time.sleep(sleep[1]) 
          
        as_utilobj.select_home_button(move_x=offset_values[8],move_y=offset_values[9])
         
        v_keys.write(write[2])
        time.sleep(sleep[0])
        keys.hotkey(key_press)
        time.sleep(sleep[0])
         
        '''Step 08: Close cargraph.fex by clicking X on the tab
                    Select No at save changes prompt
                    In Environments Tree, right-click cargraph.fex and select Run
                    Close the browser page'''
         
        as_utilobj.close_canvas_item()
        time.sleep(1)
         
        as_utilobj.select_any_dialog(click_items[7])
        time.sleep(sleep[1])
        
if __name__=='__main__' :
    unittest.main()