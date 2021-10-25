'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157549
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2036815'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods

import time,unittest
import keyboard as keys

class C2036826_TestClass(AS_BaseTestCase):
    
    def test_C2036826(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        #hcanvas_web=html_canvas.Html_Canvas(self.se_driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        tree_path="Domains->P292_S10032_G157549->API"
        item="116649AS"
        run_item="116649AS.htm"
        as_utilobj.select_home_button()
        browser = UtillityMethods.parseinitfile(self,'browser')
        
        '''Step 1. Navigate to Domains P292_S10032_G157549'''
        '''Step 1.1. Expand API folder'''
        automation.TabItemControl(Name="Home").Click()
        automation.MenuItemControl(Name="All Files").Click()
        stat=automation.TreeItemControl(Name=item).Exists(5,2)
         
        if stat==True:
            automation.TreeItemControl(Name=item).ScrollIntoView()
            time.sleep(8)
            automation.TreeItemControl(Name=item).RightClick()
            time.sleep(3)
            automation.MenuItemControl(Name="Open").Click()
        else:
            hcanvas.select_UI_item_using_right_click_menu(tree_path, item, "Open")
 
        button_control=automation.PaneControl(Name="HtmlPage").ButtonControl(AutomationId="button1")

         
        hcanvas.wait_for_object_exist(button_control, 30)
         
        '''Step 1.2. Right click on 116649AS and click Run'''
        
        'Verify the Design Pane'
        pane_control=automation.PaneControl(Name="HtmlPage")
        hcanvas.verify_object_exist(pane_control, True, 'Step 1. Verify Pane exists')
        hcanvas.verify_total_no_of_child_objects(pane_control, 4, 'Step 1. Verify Total no of objects inside Pane')
        
        list_control=automation.PaneControl(Name="HtmlPage").ListControl(AutomationId="listbox1")
        hcanvas.verify_object_exist(list_control, True, 'Step 1. Verify Listbox exists')
        
        button_control=automation.PaneControl(Name="HtmlPage").ButtonControl(AutomationId="button1")
        hcanvas.verify_object_exist(button_control, True, 'Step 1. Verify button exists')
                 
        '''run the item'''

        
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/API", run_item)
        
        '''Verify the runtime options'''
        time.sleep(4)
        
        hcanvas.wait_for_web_object_exist("[id='button1']", 1, 30, 1)
        
        hcanvas.verify_web_object_no_of_elements("[id^='button']", 1, 'Step 1.3 Verify no of buttons')
        hcanvas.verify_web_object_no_of_elements("[id^='listbox']", 1, 'Step 1.3 Verify no of listbox')
        
       
        '''Step 1.4. Clicking on the buttons sets values to the controls using the API'''
        '''Step 1.5. Multisource tree control is expanded and only top item is selected by default.'''
        '''Step 2. Click Test buttons for Calendar, Text Box, List Box, Text Area, Single Tree and Multi Tree and West will be selected for Multi Tree'''
        
        '''calendar button'''
        hcanvas.click_on_web_element("#button1")
        time.sleep(10)
        hcanvas.verify_web_object_visible("#listbox1 > option:nth-child(4):checked", True, 'Step 2.1. Verify item1 is selected')
        hcanvas.verify_web_object_visible("#listbox1 > option:nth-child(11):checked", True, 'Step 2.2. Verify item2 is selected')        
        '''Step 4. Close HtmlPage browser page'''
        
        hcanvas.close_browser_session()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
        
if __name__=='__main__' :
    unittest.main()
