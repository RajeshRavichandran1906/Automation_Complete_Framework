'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10863&group_by=cases:section_id&group_order=asc&group_id=435421
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5853189'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area
import time,unittest
import keyboard as keys
import pyautogui

class C5853189_TestClass(AS_BaseTestCase):
    
    def test_C5853189(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        tree_path="Domains->P292_S10032_G157549->API"
        item="HTML_Canvas"
        as_utilobj.select_home_button()
        browser = UtillityMethods.parseinitfile(self,'browser')
        acanvas_obj=as_html_canvas_area.AS_Html_Canvas(self.driver)
        as_ribbon_obj= as_ribbon.AS_Ribbon(self.driver)
        
        '''Step 1. Navigate to the domain P292_S10032_G157549'''
        '''Step 1.1. Expand the domain P292_S10032_G157549'''
        '''Step 2. Right click on HTML_Canvas folder-> New-> HTML/Document, click Next, click Finish'''
          
        hcanvas.create_new_html_canvas_document(tree_path, item)
         
        '''Step 2.1. Click on Report component and draw a container on canvas'''
         
        acanvas_obj.drag_drop_on_canvas('Components', 'Report', 50, 50, 520, 520)
        time.sleep(5)
        '''Step 3. Right click within report container, select "Reference existing procedure"'''
        '''Step 3.1. Double click on as3653.fex'''
        hcanvas.use_existing_fex_on_canvas_component_by_context_menu('reference', 'HTML_Canvas', 'as3653.fex', 150, 150)
        
         
         
        'Verify the Design Pane'
        pane_control=automation.PaneControl(Name="WebFOCUS Active Report")
        hcanvas.wait_for_object_exist(pane_control, 45)
        time.sleep(5)
        hcanvas.verify_object_exist(pane_control, True, 'Step 2. Verify Active report Pane exists in design time')
        hcanvas.verify_total_no_of_child_objects(pane_control, 1, 'Step 2. Verify Total no of objects inside Pane')
         
        hcanvas.refresh_tree(item)
         
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
          
        as_utilobj.save_as_UI_dialog("C5853189.htm")
         
        '''Step 4. Click on Utilities tab, click Chrome'''
        '''Step 4.1. Check if the scrollbar available during output'''

        as_ribbon_obj.click_ribbon_item('Utilities', 'chrome')
         
         
        dataitem=automation.DataItemControl(Name="NAME")
        hcanvas.wait_for_object_exist(dataitem, 60)
          
        btn=automation.PaneControl(Name="HtmlPage - Google Chrome")
        btn.Click()
        time.sleep(4)
         
         
        time.sleep(10)
        as_utilobj.verify_picture_using_sikuli('C5853189_chrome', 'Step 4. Verify scrollbar in Chrome')
         
        btn.Click()
        pyautogui.hotkey('alt','F4')
         
        '''Step 5. Close the browser page, click on IE'''
        '''Step 5.1. Check if the scrollbar available during output'''
        as_ribbon_obj.click_ribbon_item('Utilities', 'ie')
        dataitem=automation.DataItemControl(Name="NAME")
        hcanvas.wait_for_object_exist(dataitem, 60)
        time.sleep(40)
        automation.WindowControl(Name="HtmlPage - Internet Explorer").Maximize()
         
        time.sleep(10)
        as_utilobj.verify_picture_using_sikuli('C5853189_ie', 'Step 5. Verify scrollbar in IE')
        automation.WindowControl(Name="HtmlPage - Internet Explorer").Close()
         
        '''Step 6. Close the browser page, click on FireFox'''
        '''Step 6.1. Check if the scrollbar available during output'''
        as_ribbon_obj.click_ribbon_item('Utilities', 'firefox')
        dataitem=automation.DataItemControl(Name="NAME")
        hcanvas.wait_for_object_exist(dataitem, 60)
        time.sleep(40)
        automation.WindowControl(Name="HtmlPage - Mozilla Firefox").Maximize()
        time.sleep(10)
        as_utilobj.verify_picture_using_sikuli('C5853189_firefox', 'Step 6. Verify scrollbar in FF')
        automation.WindowControl(Name="HtmlPage - Mozilla Firefox").Close()

        '''Step 7. Close the browser page, click on Edage'''
        '''Step 7.1. Close the browser page, click on FireFox'''
        time.sleep(5)
        stat=automation.ButtonControl(Name="Edge").IsEnabled
        
        if stat==1:
            as_ribbon_obj.click_ribbon_item('Utilities', 'edge')
            dataitem=automation.DataItemControl(Name="NAME")
            hcanvas.wait_for_object_exist(dataitem, 60)
            time.sleep(40)
            automation.WindowControl(ClassName="ApplicationFrameWindow").Click()
            time.sleep(10)
            as_utilobj.verify_picture_using_sikuli('C5853189_edge', 'Step 7. Verify scrollbar in Edge')
            pyautogui.hotkey('alt','F4')
        else:
            print ("Edge browser is not enabled from Utilities tab")
        '''Step 8. Close the browser page, close and save the HTML page.'''

        
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
        
if __name__=='__main__' :
    unittest.main()
