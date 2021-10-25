'''@author: Robert 


Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157555
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2231085'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area

import time,unittest,pyautogui,datetime
import keyboard as keys

class C2231085_TestClass(AS_BaseTestCase):
    
    def test_C2231085(self):
        
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
        
        
        '''Step 3. In Environments Tree, set Filter to "Other Files", copy aliceblue.css to Web Applications/baseapp'''
        other_files=automation.MenuItemControl(Name="Other Files")
        other_files.Click()
        automation.TreeItemControl(Name=item).ScrollIntoView()
        time.sleep(8)
        automation.TreeItemControl(Name=item).DoubleClick()
        time.sleep(3)
        item="aliceblue"
        automation.TreeItemControl(Name=item).ScrollIntoView()
        time.sleep(8)
        automation.TreeItemControl(Name=item).RightClick() 
        time.sleep(3)
        automation.MenuItemControl(Name="Copy").DoubleClick()  
        tree_path1="Web Applications"
        hcanvas.select_UI_item_using_right_click_menu(tree_path1, "baseapp", "Paste")
        
        ui_object=automation.ButtonControl(Name="OK")
        stat=automation.ButtonControl(Name="OK").Exists(10,2)
        if stat==True:
            hcanvas.click_on_UI_element(ui_object)
        
        
        '''Step 4. Setting Panels click inside "URL/Find File..." text box, type the following /approot/baseapp/aliceblue.css, hit enter'''
        as_utilobj.expand_doc_pane('Settings')
        as_utilobj.add_css_url_by_keyboard("/approot/baseapp/aliceblue.css")
        
        time.sleep(10)
        
        as_utilobj.verify_picture_using_sikuli("alice_blue.png", 'Step 4. Verify Alice blue applied in canvas')        
        
        ui_object=automation.ListControl(AutomationId='15949')
        hcanvas.wait_for_object_exist(ui_object,15)
        hcanvas.verify_total_no_of_child_objects(ui_object, 1, 'Step 4.2 Verify only 1 item present in css files listbox')
        ui_object1=automation.ListItemControl(Name="/approot/baseapp/aliceblue.css")
        hcanvas.verify_object_exist(ui_object1, True, 'Step 4.2. Verify aliceblue item is present')
        
        '''Step 5. Setting Panels click inside "URL/Find File..." text box, type the following /approot/baseapp/crime1.js, hit enter'''
        as_utilobj.expand_doc_pane('Settings')
        as_utilobj.add_css_url_by_keyboard("/approot/baseapp/crime1.js")
        
        ui_object=automation.ListControl(AutomationId='15952')
        hcanvas.wait_for_object_exist(ui_object,15)
        hcanvas.verify_total_no_of_child_objects(ui_object, 1, 'Step 5 Verify only 1 item present in css files listbox')
        ui_object1=automation.ListItemControl(Name="/approot/baseapp/crime1.js")
        hcanvas.verify_object_exist(ui_object1, True, 'Step 5. Verify crime1 item is present')
        
        
        '''Step 6. Setting Panels click on CSS icon'''
        '''Step 6.1. Double click on turquoise.css'''
        as_utilobj.expand_doc_pane('Settings')
        as_utilobj.add_css_url_by_button("css", "turquoise.css")
        
        time.sleep(10)
        
        as_utilobj.verify_picture_using_sikuli("turquoise_canvas.png", 'Step 6.1. Verify Turquoise applied in canvas')
        as_utilobj.expand_doc_pane('Settings')
        ui_object=automation.ListControl(AutomationId='15949')
        hcanvas.wait_for_object_exist(ui_object,15)
        hcanvas.verify_total_no_of_child_objects(ui_object, 2, 'Step 6.2 Verify 2 item present in css files listbox')
        ui_object1=automation.ListItemControl(Name="turquoise.css")
        hcanvas.verify_object_exist(ui_object1, True, 'Step 6.2. Verify turquoise item is present')
            
        
        '''Step 7. Setting Panels click on CSS icon'''
        '''Step 7.1. Double click on peach.css'''
        as_utilobj.expand_doc_pane('Settings')
        as_utilobj.add_css_url_by_button("css", "peach.css")
        time.sleep(10)
        
        as_utilobj.verify_picture_using_sikuli("peach_canvas.png", 'Step 7.1. Verify peach applied in canvas')        
        as_utilobj.expand_doc_pane('Settings')
        ui_object=automation.ListControl(AutomationId='15949')
        hcanvas.wait_for_object_exist(ui_object,15)
        hcanvas.verify_total_no_of_child_objects(ui_object, 3, 'Step 7.2 Verify 3 item present in css files listbox')
        ui_object1=automation.ListItemControl(Name="peach.css")
        hcanvas.verify_object_exist(ui_object1, True, 'Step 7.2. Verify peach item is present')
    
        '''Step 8. Setting Panels click on JS icon'''
        '''Step 8.1. Double click on mapviewset.js'''
        as_utilobj.expand_doc_pane('Settings')
        as_utilobj.add_css_url_by_button("js", "mapviewset.js")
        as_utilobj.expand_doc_pane('Settings')
        ui_object=automation.ListControl(AutomationId='15952')
        hcanvas.wait_for_object_exist(ui_object,15)
        hcanvas.verify_total_no_of_child_objects(ui_object, 2, 'Step 8 Verify only 2 item present in js files listbox')
        ui_object1=automation.ListItemControl(Name="mapviewset.js")
        hcanvas.verify_object_exist(ui_object1, True, 'Step 8. Verify mapviewset.js item is present')
        
        '''Step 9. Settings panel, click "Move Item Up" and "Move Item Down"'''
        '''Step 9.1. The background color should changed based on the selected .CSS file'''
        as_utilobj.expand_doc_pane('Settings')
        list1=automation.ListControl(AutomationId="15949").GetChildren()
        list1[2].Click()
        time.sleep(3)
        moveup=automation.ButtonControl(Name="Move Item Up")
        moveup.Click()
        time.sleep(10)
        
        as_utilobj.verify_picture_using_sikuli("peach_canvas.png", 'Step 9.1. Verify peach applied in canvas')
        as_utilobj.expand_doc_pane('Settings')        
        list1[0].Click()
        time.sleep(3)
        
        movedown=automation.ButtonControl(Name="Move Item Down")
        movedown.Click()
        time.sleep(3)
        movedown.Click()
        time.sleep(10)
        
        as_utilobj.verify_picture_using_sikuli("alice_blue.png", 'Step 9.1. Verify Alice blue applied in canvas')        
        
        
        '''Step 10. Close and save the page, re-open the saved page'''
        
         
        '''Save report'''
        item="HTML_Canvas"
        automation.TreeItemControl(Name=item).ScrollIntoView()
        time.sleep(3)
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
              
        as_utilobj.save_as_UI_dialog("C2221085")
         
        
        '''Step 10.1. All files should remain in the Settings panel .CSS and .JS'''
        '''Step 11. Close the HTML page'''
        item="C2221085.htm"
        automation.TabItemControl(Name="Home").Click()
        stat=automation.TreeItemControl(Name=item).Exists(5,2)
        if stat==True:
            automation.TreeItemControl(Name=item).ScrollIntoView()
            time.sleep(8)
            automation.TreeItemControl(Name=item).RightClick()
            time.sleep(3)
            automation.MenuItemControl(Name="Open").Click()
            time.sleep(3)
            
        else:
            hcanvas.select_UI_item_using_right_click_menu(tree_path, item, "Open")
        
        time.sleep(10)
        
        as_utilobj.expand_doc_pane('Settings')
        
        ui_object=automation.ListControl(AutomationId="15949")
        hcanvas.wait_for_object_exist(ui_object,15)
        hcanvas.verify_total_no_of_child_objects(ui_object, 3, 'Step 10.1 Verify 3 item present in css files listbox')
        
        ui_object=automation.ListControl(AutomationId="15952")
        hcanvas.wait_for_object_exist(ui_object,15)
        hcanvas.verify_total_no_of_child_objects(ui_object, 2, 'Step 10.1 Verify 3 item present in script files listbox')
        
        all_files=automation.MenuItemControl(Name="All Files")
        all_files.Click()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
    
        
if __name__=='__main__' :
    unittest.main()
