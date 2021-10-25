'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2270240'''

from common.lib.as_basetestcase import AS_BaseTestCase
from common.pages import as_panels
from selenium.webdriver import ActionChains
import time,unittest
from common.lib import as_utility
import pyautogui as keys

class C2270240_TestClass(AS_BaseTestCase):
    def test_C2270240(self):
        
        '''Create instance of object '''
        driver=self.driver
        as_panels_obj= as_panels.AS_Panels(driver)
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()

        '''AS_Menu Tooltips'''
        
        as_panels_obj.Verify_Tooltip_Using_Name('Application Menu','Step 01: Verify AS_Menu Tooltip is Application Menu',move_x=4,move_y=4)
        time.sleep(1) 
        
        as_utilobj.select_home_button()
        
        as_utilobj.click_element_using_ui(button_item=True,name="Application Menu")
        time.sleep(2)
        
        as_panels_obj.Verifypanel_Tooltip(10,40,'Open (Ctrl+O)', 'Step 02: Verify AS_Menu Tooltip is Open (Ctrl+O) - Open an existing document',move_x=2,move_y=2)
        time.sleep(1)

        as_panels_obj.Verifypanel_Tooltip(10,40,'Save (Ctrl+S)', 'Step 03: Verify AS_Menu Tooltip is Save (Ctrl+S) - Save the active document.',move_x=2,move_y=2)
        time.sleep(1)
        
        as_panels_obj.Verifypanel_Tooltip(10,40,'Save As', 'Step 04: Verify AS_Menu Tooltip is Save As - Save the active document with a new name',move_x=2,move_y=2)
        time.sleep(1)

        as_panels_obj.Verifypanel_Tooltip(10,40,'Save All', 'Step 05: AS_Menu Verify Tooltip is Save All - Save all active documents',move_x=2,move_y=2)
        time.sleep(1)
        
        ''' To locate RUN and verify the tooltips'''
        
        action = ActionChains(self.driver)
        action.move_by_offset(10,40).perform()
        del action
        time.sleep(1)
        
        as_panels_obj.Verifypanel_Tooltip(2,2,'Message Viewer OFF','Step 06: Verify Run Tooltip is Message Viewer OFF',move_x=80,move_y=-160)
        time.sleep(1) 
        
        as_panels_obj.Verifypanel_Tooltip(2,2,'Message Viewer ON','Step 07: Verify Run Tooltip is Message Viewer ON - Display messages in a separate frame below the report output',move_x=2,move_y=30)
        time.sleep(1) 
        
        as_panels_obj.Verifypanel_Tooltip(2,2,'Display command lines','Step 08: Verify Run Tooltip is Display command lines - Displays messages and lines in a separate frame below the report output that are expanded and stacked for execution',move_x=2,move_y=25)
        time.sleep(1) 
        
        as_panels_obj.Verifypanel_Tooltip(2,2,'Display Dialogue Manager commands','Step 09: Verify Run Tooltip is Display Dialogue Manager commands - Displays messages and lines in a separate frame below the report output that are expanded and stacked for execution while also displaying all Dialogue Manager commands',move_x=2,move_y=20)
        time.sleep(1)
        
        as_panels_obj.Verifypanel_Tooltip(2,2,'Close','Step 10: Verify AS_Menu Tooltip is Close - Save the active documents',move_x=-130,move_y=190)
        time.sleep(1)
        
        as_panels_obj.Verifypanel_Tooltip(2,2,'Close All','Step 10: Verify AS_Menu Tooltip is Close All - Close All the active documents',move_x=2,move_y=30)
        time.sleep(1)
        
        as_panels_obj.Verifypanel_Tooltip(280,46,'Options','Step 11: Verify AS_Menu Tooltip is Options - Changes global options for this application',move_x=3,move_y=3)
        time.sleep(1)
        
        as_panels_obj.Verifypanel_Tooltip(90,5,'Exit','Step 12: Verify AS_Menu Tooltip is Exit - Quit the application; prompts to save document',move_x=3,move_y=3)
        time.sleep(1) 
        
        keys.hotkey('esc')
        time.sleep(1)
    
if __name__=='__main__' :
    unittest.main()