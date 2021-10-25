'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157549
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2036812'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods

import time,unittest
import keyboard as keys

class C2036812_TestClass(AS_BaseTestCase):
    
    def test_C2036812(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        tree_path="Domains->P292_S10032_G157549->API"
        item="IbComposer getCurrentSelectionAS"
        as_utilobj.select_home_button()
        browser = UtillityMethods.parseinitfile(self,'browser')
        
        '''Step 1. Navigate to Domains P292_S10032_G157549, Expand API folder'''
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
  
        
        button_control=automation.ButtonControl(AutomationId='button5')
        
        hcanvas.wait_for_object_exist(button_control, 30)
        
        'Verify the Design Pane'
        pane_control=automation.PaneControl(Name="HtmlPage")
        hcanvas.verify_object_exist(pane_control, True, 'Step 1. Verify Pane exists')
        hcanvas.verify_total_no_of_child_objects(pane_control, 34, 'Step 1. Verify Total no of objects inside Pane')
        list_control=automation.ListControl(AutomationId='listbox1')
        hcanvas.verify_object_exist(list_control, True, 'Step 1. Verify list exists')
        hcanvas.verify_object_exist(button_control, True, 'Step 1. Verify Button exists')
        group_control=automation.GroupControl(AutomationId='radio1')
        hcanvas.verify_object_exist(group_control, True, 'Step 1. Verify Group exists')
        
        '''Step 2. Right click on IbComposer_getCurrentSelectionAS and click Run'''
        
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/API", "IbComposer_getCurrentSelectionAS.htm")
       
        
        '''Step 3. Change the value in the Drop Down list to 'Value5' and click 'Test Drop Down'''
        
        hcanvas.select_combobox_option_item("#combobox1", "value", "Value5")
        
        hcanvas.click_on_web_element("#button5")
        time.sleep(10)
        '''Verify value5 msgbox'''
        val_text=automation.TextControl(Name="Value5")
        hcanvas.verify_object_exist(val_text, True, 'Step 3. Verify Value5 msgbox displayed')
        
        btn_ok=automation.ButtonControl(Name="OK")
        hcanvas.click_on_UI_element(btn_ok)
        time.sleep(10)
        
        
        '''Step 4. Click the buttons to display the selected values in each HTML Control and click OK from message box'''
        '''Step 4.1. A message box will appears with the value selected for each control'''
        '''Step 5. Click 'Test Multi Source Tree' and click OK from message box'''
        
        hcanvas.click_on_web_element("#button14")
        time.sleep(10)
        '''Verify Length is: 1 msgbox'''
        val_text=automation.TextControl(Name="Length is: 1")
        hcanvas.verify_object_exist(val_text, True, 'Step 5. Verify Length is: 1 msgbox displayed')
        
        btn_ok=automation.ButtonControl(Name="OK")
        hcanvas.click_on_UI_element(btn_ok)
        time.sleep(10)
        automation.PaneControl(Name="HtmlPage - Google Chrome").SetFocus()
        stat=automation.PaneControl(Name="HtmlPage - Google Chrome").ButtonControl(Name="OK").Exists(5,2)
        print (stat)
        if stat==True:
            btn_ok=automation.ButtonControl(Name="OK")
            as_utilobj.asequal(stat,False,"Step. AS-6122 Clicking Test Multi Source Tree button gives one more empty message dialogue box")
            hcanvas.click_on_UI_element(btn_ok)
        
        #hcanvas.verify_object_exist(btn_ok, False, "AS-6122 Clicking Test Multi Source Tree button gives one more empty message dialogue box")
        
        time.sleep(10)
        
        
        '''Step 6. Click 'Test Radio Button' and click OK from message box'''
        hcanvas.click_on_web_element("#button13")
        time.sleep(10)
        '''Verify FOC_NOSELECTION msgbox'''
        val_text=automation.TextControl(Name="FOC_NOSELECTION")
        hcanvas.verify_object_exist(val_text, True, 'Step 6. Verify FOC_NOSELECTION msgbox displayed')
        
        btn_ok=automation.ButtonControl(Name="OK")
        hcanvas.click_on_UI_element(btn_ok)
        time.sleep(10)
        '''Step 7. Click 'Test Vertical Slider' and click OK from message box'''
        
        hcanvas.click_on_web_element("#button16")
        time.sleep(10)
        '''Verify 0 msgbox'''
        val_text=automation.TextControl(Name="0")
        hcanvas.verify_object_exist(val_text, True, 'Step 7. Verify 0 msgbox displayed')
        
        btn_ok=automation.ButtonControl(Name="OK")
        hcanvas.click_on_UI_element(btn_ok)
        time.sleep(10)
        '''Step 8. Click 'Test Horizontal Slider' and click OK from message box'''
        
        hcanvas.click_on_web_element("#button15")
        time.sleep(10)
        '''Verify 0 msgbox'''
        val_text=automation.TextControl(Name="0")
        hcanvas.verify_object_exist(val_text, True, 'Step 8. Verify 0 msgbox displayed')
        
        btn_ok=automation.ButtonControl(Name="OK")
        hcanvas.click_on_UI_element(btn_ok)
        time.sleep(10)
        '''Step 9. Close the HtmlPage browser page'''
        
        hcanvas.close_browser_session()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
    
        
if __name__=='__main__' :
    unittest.main()
