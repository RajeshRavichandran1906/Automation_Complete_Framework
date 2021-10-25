'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288374'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys

class C2288374_TestClass(AS_BaseTestCase):
    def test_C2288374(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, right click on BarChart and select Duplicate
                    Right click on the highlighted BarChart file and select Properties'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                           
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_item="BarChart",send_keys=['down','down'])
        time.sleep(1)
         
        as_utilobj.Verify_Element("Duplicate","Step 01: BarChart been displayed in the duplicated file name BarChart_1.htm",available=True)
        time.sleep(2)
         
        keys.press('esc')
        time.sleep(1)
         
        '''Step 02: Double click on the highlighted BarChart file'''
         
        tree_path="BarChart"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(4)
         
        as_utilobj.verify_active_tool("App Studio - BarChart (English)","Step 02: Barchart file is opened in HTML Canvas")
        time.sleep(2)
        
        '''Step 03: Click Run
                    Close HtmlPage tab output
                    Close BarChart tab'''
        
        as_utilobj.click_element_using_ui(split_button="Run")
        time.sleep(8)
        
        as_utilobj.verify_picture_using_sikuli("step3_C2288374.png","Step 03: BarChart invoked in IE browser")
        time.sleep(6)
        
        as_utilobj.Verify_Browser_Content("IEFrame",".",browser_close=True)
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        '''Step 04: Right click on the Garden and select Copy
                    Right click on CC - AppStudio->AS Browser and select Paste'''
        
        as_utilobj.select_component_by_right_click(right_click_item='Garden',send_keys=['down'])
        time.sleep(2)
        
        as_utilobj.Verify_Element("Copy","Step 04: Garden html file been successfully pasted",available=True)
        time.sleep(1)
        
        keys.press('esc')
        time.sleep(1)
        
        '''Step 05: In Environments Tree, CC - AppStudio->AS Browser
                    Right click on Garden and select Delete 
                    Click Yes'''
        
        as_utilobj.select_component_by_right_click(right_click_item='Garden',send_keys=['down'])
        time.sleep(2)
        
        as_utilobj.Verify_Element("Delete","Step 05: Garden html file been successfully deleted",available=True)
        time.sleep(1)
        
        keys.press('esc')
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()        