'''@author: Robert 


Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157555
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2229784'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area

import time,unittest,pyautogui,datetime
import keyboard as keys

class C2229784_TestClass(AS_BaseTestCase):
    
    def test_C2229784(self):
        
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
        automation.TabItemControl(Name="Home").Click()
        stat=automation.TreeItemControl(Name=item).Exists(5,2)
        if stat==True:
            automation.TreeItemControl(Name=item).ScrollIntoView()
            time.sleep(8)
            automation.TreeItemControl(Name=item).RightClick()
            time.sleep(3)
            automation.MenuItemControl(Name="New").Click()
            time.sleep(3)
            automation.MenuItemControl(Name="HTML/Document").DoubleClick()
        else:
            hcanvas.select_UI_item_using_right_click_menu(tree_path, item, "New->HTML/Document")
       
        '''Step 2. Right click on HTML_Canvas folder->New-> HTML/Document, click Next, click Finish.'''  
        button_control=automation.ButtonControl(Name='Next >')
        hcanvas.click_on_UI_element(button_control)
                  
        button_control=automation.ButtonControl(Name='Finish')
        hcanvas.wait_for_object_exist(button_control, 30)
        hcanvas.click_on_UI_element(button_control)
                  
        pane_control=automation.PaneControl(Name="HtmlPage")
        hcanvas.wait_for_object_exist(pane_control, 30)
             
        '''Step 3.1. Click on Report component and draw a container on canvas'''
        '''Step 3.2. Right click on report container and select "Reference existing procedure"'''
                    
        acanvas_obj.drag_drop_on_canvas('Components', 'Report', 50, 50, 450, 650)
        time.sleep(5)
        '''Step 3. Click Report and draw a container in the canvas.'''
        '''Step '3.1. Right click within the report container and select "Import existing report"'''
        automation.PaneControl(Name="HtmlPage").RightClick(180,180)
               
        menu_item=automation.MenuItemControl(Name="Reference existing procedure")
        hcanvas.wait_for_object_exist(menu_item, 20)
        menu_item.MoveCursor()
        time.sleep(3)
        hcanvas.click_on_UI_element(menu_item)
               
        win_control=automation.WindowControl(Name="Open File")
            
        '''Step 3.3. Double click on  160526009.fex'''
           
        hcanvas.wait_for_object_exist(win_control, 30)
        time.sleep(3)
        automation.TextControl(Name="160526009.fex").DoubleClick(40,10)
        
        rep=automation.PaneControl(Name="WebFOCUS Report")
        
        hcanvas.wait_for_object_exist(rep, 30)
        hcanvas.verify_object_exist(rep, True, 'Step 3. Verify Report added to canvas')
        
        cell=automation.DataItemControl(Name="PAGE 1")
        hcanvas.verify_object_exist(cell, True, 'Step 3. Verify Content inside the added report to canvas')
        time.sleep(4)
         
        '''Save the report'''
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
                  
        as_utilobj.save_as_UI_dialog("C2229784")
          
          
        '''Step 4. Click Run'''
         
        
        time.sleep(6)
        
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/HTML_Canvas", "C2229784.htm")
        time.sleep(6)
        
        
        hcanvas.wait_for_web_object_exist("#report1", 1, 40, 1)
        
        '''Verifying the report in frame1'''
         
        #hcanvas.create_web_table_data("html body table tbody tr", "C2229784_Ds01.xlsx")
        hcanvas.verify_web_table_data("html body table tbody tr", "C2229784_Ds01.xlsx", 'Step 6.1 Verify Report1 in iframe')
        
        '''Step 5. Close the browser page, close and save the HTML page'''
        
        hcanvas.close_browser_session()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
    
        
if __name__=='__main__' :
    unittest.main()

