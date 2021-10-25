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

class C5589271_TestClass(AS_BaseTestCase):
    
    def test_C5589271(self):
        
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
        '''Step 1.1. Right click on HTML_Canvas folder->New-> HTML/Document, click Next, click Finish'''
        
           
        hcanvas.create_new_html_canvas_document(tree_path, item)
         
        '''Step 1.2. Click on Button and draw on canvas'''
        acanvas_obj.drag_drop_on_canvas('Components', 'Button', 50, 50, 220, 220)
        time.sleep(5)
        '''Step 1.3. Click on Controls, click on List Box and draw on canvas'''
         
        acanvas_obj.drag_drop_on_canvas('Controls', 'Listbox', 250, 50, 380, 250)
         
         
        '''Step 2. Select the Button on canvas'''
        automation.PaneControl(Name="HtmlPage").RightClick(150,150)
        '''Step 2.1. Properties panel, Core attributes section'''
        as_utilobj.expand_doc_pane('Properties')
        '''Step 2.2. Unique Identifier Property, type A button'''
        '''Step 2.3. Hit Enter'''
         
        hcanvas.click_change_item_properties_tab_using_sikuli('prop_btn_uid.png', '170', '4', 'double', 'A button')
        '''Step 3. Select the List Box on canvas'''
        automation.PaneControl(Name="HtmlPage").RightClick(300,200)
        '''Step 3.1. Properties panel, Core attributes section'''
        as_utilobj.expand_doc_pane('Properties')
        '''Step 3.2. Unique Identifier Property, type Just listbox'''
        '''Step 3.3. Hit Enter'''
        hcanvas.click_change_item_properties_tab_using_sikuli('prop_lstbox_uid.png', '170', '4', 'double', 'Just listbox')
        '''Step 4. Properties panel, Miscellaneous section'''
        as_utilobj.expand_doc_pane('Properties')
        '''Step 4.1. Name Property, type A listbox'''
        '''Step 4.2. Hit Enter'''
        hcanvas.click_change_item_properties_tab_using_sikuli('prop_lstbox_name.png', '170', '4', 'double', 'A listbox')
        '''Step 5. Click on Parameters tab'''
         
        as_utilobj.click_picture_from_region_using_sikuli('bottom_4_tabs.png', '55', '5', 'double', 'bottom')
        time.sleep(10)
#         
        as_utilobj.verify_picture_using_sikuli('C5589271_param1.png', 'Step 5. Verify Parameters tab')
        
        '''Step 5.1. Click on Design tab'''
        as_utilobj.click_picture_from_region_using_sikuli('bottom_4_tabs.png', '15', '5', 'double', 'bottom')
        win=automation.PaneControl(Name="HtmlPage")
        hcanvas.wait_for_object_exist(win, 40)
        time.sleep(5)
        automation.PaneControl(Name="HtmlPage").RightClick(300,200)
        time.sleep(10)
        '''Step 6. Settings panel, Data type Static'''
        as_utilobj.expand_doc_pane('Settings')
        
        radio=automation.RadioButtonControl(Name="Static")
        radio.MoveCursor()
        radio.Click()
        time.sleep(4)
        
        '''Step 6.1. Click on New button'''
        '''Step 6.2. Click on New button'''
        '''Step 6.3. Click on Properties panel'''
        btn=automation.SplitButtonControl(Name="New").Click(8,5)
        time.sleep(4)
        btn=automation.SplitButtonControl(Name="New").Click(8,5)
        time.sleep(4)
        as_utilobj.expand_doc_pane('Properties')
        time.sleep(10)
        as_utilobj.verify_picture_using_sikuli('C5589271_lstbox_uid.png', 'Step 6. Verify Properties pane for Listbox Unique identifier')
        as_utilobj.verify_picture_using_sikuli('C5589271_lstbox_name.png', 'Step 6. Verify Properties pane for Listbox name')
        
        '''Step 7. Close HtmlPage1 tab'''
        '''Step 7.1. Click Yes in App Studio prompt message'''
        '''Step 7.2. Type as5581'''
        '''Step 7.3. Click OK'''
        hcanvas.refresh_tree(item)
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
          
        as_utilobj.save_as_UI_dialog("as5581.htm")
        hcanvas.refresh_tree_and_close_canvas_item(item)
        
        '''Step 8. In Environments Tree, right click on as8851 and select Open'''
        tree_path="Domains->P292_S10032_G157549->HTML_Canvas"
        item1="HTML_Canvas"
        item2="as5581"
        automation.TreeItemControl(Name=item1).ScrollIntoView()
        time.sleep(2)
        automation.TreeItemControl(Name=item1).DoubleClick(15,3)
        time.sleep(2)
        automation.TreeItemControl(Name=item2).ScrollIntoView()
        time.sleep(2)
        automation.TreeItemControl(Name=item2).RightClick()
        time.sleep(4)
        automation.MenuItemControl(Name="Open").Click(10,4)
        time.sleep(2)
        btn=automation.ButtonControl(AutomationId="A_button")
        hcanvas.wait_for_object_exist(btn, 30)
        '''Step 8.1. Select the Button on canvas'''
        '''Step 8.2. Properties panel, Core attributes section'''
        automation.PaneControl(Name="HtmlPage").RightClick(150,150)
        as_utilobj.expand_doc_pane('Properties')
        time.sleep(10)
        as_utilobj.verify_picture_using_sikuli('C5589271_btn_uid.png', 'Step 8. Verify Properties pane for Button Unique identifier')
        
        '''Step 9. Select the List Box on canvas'''
        '''Step 9.1. Properties panel, Core attributes section'''
        '''Step 9.2. Properties panel, Miscellaneous section'''
        automation.PaneControl(Name="HtmlPage").RightClick(300,200)
        as_utilobj.expand_doc_pane('Properties')
        time.sleep(10)
        as_utilobj.verify_picture_using_sikuli('C5589271_lstbox_uid.png', 'Step 9. Verify Properties pane for Listbox Unique identifier')
        as_utilobj.verify_picture_using_sikuli('C5589271_lstbox_name.png', 'Step 9. Verify Properties pane for Listbox name')
        '''Step 9.3. Click on Parameters tab'''
        
        as_utilobj.click_picture_from_region_using_sikuli('bottom_4_tabs.png', '50', '3', 'double', 'bottom')
        time.sleep(10)
        as_utilobj.verify_picture_using_sikuli('C5589271_param1.png', 'Step 9.3. Verify Parameters tab')
        
        '''Step 9.4. Close as5581 tab'''
        
                        
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
        
if __name__=='__main__' :
    unittest.main()
