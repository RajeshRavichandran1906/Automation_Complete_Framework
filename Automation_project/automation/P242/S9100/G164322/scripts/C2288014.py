'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288014'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import keyboard as keys

class C2288014_TestClass(AS_BaseTestCase):
    def test_C2288014(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Click on View Options icon
                    Select 'View Items by Name' from the 'View Options' menu
                    Un-check 'Respect Sort Order Property'''
                    
        as_utilobj.click_element_using_ui(menu_item=True,name='View Options')
        time.sleep(1)
         
        as_utilobj.click_element_using_ui(menu_item=True,name='View items by Name')
        time.sleep(1)
 
        as_utilobj.verify_element_using_ui("Step 01: Verified 'View items by Name' is checked",menu_item_enabled="View items by Name")
        time.sleep(1)
          
        as_utilobj.click_element_using_ui(menu_item=True,name='View Options')
        time.sleep(1)
           
        as_utilobj.click_element_using_ui(menu_item=True,name='Respect Sort Order Property')
        time.sleep(1)
          
        '''Step 02: Navigate to CCAppStudio
                    Expand ASFramework
                    Select ActiveChart.fex
                    Click File/Folder Properties panel
                    Prefix Name with zzz, hit Enter'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                      
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
               
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
          
        as_utilobj.select_component_by_right_click(right_click_item='ActiveChart.fex',click='Properties')
        time.sleep(1)
        
        as_utilobj.select_home_button()
        
        as_utilobj.double_click_element_using_offset(1600,145)
        time.sleep(1)
        
        keys.write('zzz')
        time.sleep(1)
        
        keys.press('enter')
        time.sleep(2)
        
        as_utilobj.Verify_Element('zzzActiveChart.fex',"Step 02: Verified file been renamed in Environment Tree",available=True)
        time.sleep(2)
        
        '''Step 03: Click File/Folder Properties panel
                    Delete zzz from Name, hit Enter
                    Click on View Options icon
                    Select 'View Items by Title' from the 'View Options' menu
                    Check 'Respect Sort Order Property'''
        
        as_utilobj.select_component_by_right_click(right_click_item='zzzActiveChart.fex',click='Rename')
        time.sleep(1)
        
        keys.write("ActiveChart")
        time.sleep(1)
        
        as_utilobj.Verify_Element('ActiveChart.fex',"Step 03: Verified File Reverted back to old name",available=True)
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(menu_item=True,name='View Options')
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(menu_item=True,name='View items by Title')
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(menu_item=True,name='View Options')
        time.sleep(1)
         
        as_utilobj.click_element_using_ui(menu_item=True,name='Respect Sort Order Property')
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()  