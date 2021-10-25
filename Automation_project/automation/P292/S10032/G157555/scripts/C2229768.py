'''@author: Robert 


Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157555
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2229768'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area

import time,unittest,pyautogui,datetime
import keyboard as keys

class C2229768_TestClass(AS_BaseTestCase):
    
    def test_C2229768(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        as_panelsobj=as_panels.AS_Panels(self.driver)
        as_ribbonobj=as_ribbon.AS_Ribbon(self.driver)
        tree_path="Domains->P292_S10032_G157549"
        item="HTML_Canvas"
        as_utilobj.select_home_button()
        browser = UtillityMethods.parseinitfile(self,'browser')
        acanvas_obj=as_html_canvas_area.AS_Html_Canvas(self.driver)
        email_id="report_caster@ibi.com"
        
        '''Step 1. Navigate to the domain P292_S10032_G157549'''
        '''Step 1.1. Expand the domain P292_S10032_G157549''' 
        '''Step 2. Right click on HTML_Canvas folder->New-> HTML/Document, click Next, click Finish.''' 
        hcanvas.create_new_html_canvas_document(tree_path, item)
        
         
        '''Step 2.1. By default, 4 tabs are at the bottom of the HTML page'''
        UtillityMethods.verify_picture_using_sikuli(self, 'C2229768.png', 'Step 2. Verify 4 tabs')
         
        time.sleep(5)
        '''Step 3. Click on 'Embedded CSS' tab'''
        as_utilobj.maximize_setfocus_ui_window("App")
        as_utilobj.click_picture_using_sikuli('bottom_4_tabs.png', "280","5", "double")
         
        time.sleep(5)
         
        '''Step 4. Add the following code after .internal_default {background-color: blue;}'''
        can=automation.PaneControl(Name="about:blank")
        hcanvas.wait_for_object_exist(can, 40)
        time.sleep(45)
        can.Click(140,30)
        time.sleep(3)
        pyautogui.hotkey('ctrl','home')
        time.sleep(3)
        pyautogui.hotkey('end')
        time.sleep(3)
        pyautogui.hotkey('enter')
        time.sleep(3)
        msg="background-color: blue;"
        pyautogui.typewrite(msg)
         
        '''Step 5. Click on Properties panel, "Body" section and select 'internal_default' value from the drop down 
            listing under the 'Class identifier (CSS)' property.'''
        as_utilobj.expand_doc_pane('Properties')
         
        time.sleep(4)
         
        as_utilobj.click_picture_using_sikuli('class_css.png', "15","4", "double")
         
        time.sleep(60)
        
        automation.SendKey(automation.Keys.VK_END)
        #pyautogui.hotkey('end')
        time.sleep(3)
        automation.SendKey(automation.Keys.VK_HOME)
        #pyautogui.hotkey('home')
        time.sleep(3)
        automation.SendKeys('{Ctrl}a')
        time.sleep(3)
        automation.SendKeys('{Delete}')
        
        time.sleep(3)
        css='internal_default'
        automation.SendKeys(css)
        #pyautogui.typewrite(css)
        
        time.sleep(3) 
        automation.SendKeys('{Enter}')
        
         
        '''Step 6. Click on Design tab.'''
        as_utilobj.click_picture_using_sikuli('bottom_tab_design.png', "5","4", "double")
        time.sleep(10)
        
        '''Step 6.1. Canvas color is changed to blue.'''
        UtillityMethods.verify_picture_using_sikuli(self, 'design_blue.png', 'Step 6. Verify color changed to Blue at design time')
         
         
        '''Save report'''
        automation.TreeItemControl(Name=item).RightClick()
        time.sleep(3)
        automation.MenuItemControl(Name="Refresh Descendants").MoveCursor()
        time.sleep(3)
        automation.MenuItemControl(Name="Refresh Descendants").Click()
        time.sleep(6)
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
              
        as_utilobj.save_as_UI_dialog("C2229768")
         
        '''Step 7. Run the HTML page.'''
           
        time.sleep(6)
        
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/HTML_Canvas", "C2229768.htm")
        time.sleep(6)
        hcanvas.switch_to_window(0)
        
        hcanvas.wait_for_web_object_exist("[id='loadingiframe'][style*='none']", 1, 30, 1)
        
        '''verify runtime output color to blue'''
        UtillityMethods.verify_picture_using_sikuli(self, 'runtime_blue.png', 'Step 7. Verify color changed to Blue at runtime')
        
        
        hcanvas.close_browser_session()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
    
        
if __name__=='__main__' :
    unittest.main()
