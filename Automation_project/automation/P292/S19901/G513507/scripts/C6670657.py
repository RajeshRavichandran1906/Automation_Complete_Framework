'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/19901&group_by=cases:section_id&group_id=513507&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6670657'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
from common.lib import as_utility 
import uiautomation as automation
import time,unittest

class C6670657_TestClass(AS_BaseTestCase):
    
    def test_C6670657(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        tree_path="Domains->P292_S10032_G157549->API"
        item="IbComposer getCurrentSelectionEx"
        run_item="IbComposer_getCurrentSelectionEx.htm"
        as_utilobj.select_home_button()
        
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
        
                 
        '''Step 2. Right click on IbComposer getCurrentSelectionEx and click Open.'''
        '''Step 2.1. Click 'Yes' in AppStudio prompt'''
        dialog=automation.WindowControl(Name="App Studio").ButtonControl(Name="No")
        hcanvas.wait_for_object_exist(dialog, 30)
        hcanvas.click_on_UI_element(dialog)
 
        button_control=automation.PaneControl(Name="HtmlPage").ButtonControl(Name="Get Index, Value and Display Value of Dropdown List")
  
        hcanvas.wait_for_object_exist(button_control, 90)

        
        'Verify the Design Pane'
        pane_control=automation.PaneControl(Name="HtmlPage")
        hcanvas.verify_object_exist(pane_control, True, 'Step 1. Verify Pane exists')
        hcanvas.verify_total_no_of_child_objects(pane_control, 17, 'Step 2. Verify Total no of objects inside Pane')
        
        listbox_control=pane_control.ListControl(AutomationId="listbox1")
        hcanvas.verify_object_exist(listbox_control, True, 'Step 2. Verify Listbox exists')
        
        combo_control=pane_control.ComboBoxControl(AutomationId="combobox1")
        hcanvas.verify_object_exist(combo_control, True, 'Step 2. Verify Combobox exists')
        
        group_control=pane_control.GroupControl(AutomationId="text5")
        hcanvas.verify_object_exist(group_control, True, 'Step 2. Verify Texbox exists')
        
        group_control=pane_control.GroupControl(AutomationId="customselect1")
        hcanvas.verify_object_exist(group_control, True, 'Step 2. Verify Double listbox exists')
        
        button_control=pane_control.ButtonControl(AutomationId="button1")
        hcanvas.verify_object_exist(button_control, True, 'Step 2. Verify Get Index, Value and Display Value of List Box button exists')
        
        button_control=pane_control.ButtonControl(AutomationId="button2")
        hcanvas.verify_object_exist(button_control, True, 'Step 2. Verify Get Index, Value and Display Value of Dropdown List button exists')
        
        button_control=pane_control.ButtonControl(AutomationId="button7")
        hcanvas.verify_object_exist(button_control, True, 'Step 2. Verify Get Index, Value and Display Value of Double List Box button exists')
        
        listbox_control=pane_control.ListControl(AutomationId="listbox2")
        hcanvas.verify_object_exist(listbox_control, True, 'Step 2. Verify Index Listbox exists')
        
        listbox_control=pane_control.ListControl(AutomationId="listbox3")
        hcanvas.verify_object_exist(listbox_control, True, 'Step 2. Verify Value Listbox exists')
        
        listbox_control=pane_control.ListControl(AutomationId="listbox4")
        hcanvas.verify_object_exist(listbox_control, True, 'Step 2. Verify Display Value Listbox exists')
        
        text_control=pane_control.TextControl(Name="Displays Display Value")
        hcanvas.verify_object_exist(text_control, True, 'Step 2. Verify Display Value Textbox exists')
        
        text_control=pane_control.TextControl(Name="Displays Value")
        hcanvas.verify_object_exist(text_control, True, 'Step 2. Verify Value Textbox exists')
        
        text_control=pane_control.TextControl(Name="Displays Index")
        hcanvas.verify_object_exist(text_control, True, 'Step 2. Verify Index Textbox exists')
        
        group_control=pane_control.GroupControl(AutomationId="multisourcetreecontrol1")
        hcanvas.verify_object_exist(group_control, True, 'Step 2. Verify Tree control grup exists')
        
        button_control=pane_control.ButtonControl(AutomationId="button8")
        hcanvas.verify_object_exist(button_control, True, 'Step 2. Verify Display values button exists')
        
        
         
        '''Step 3. Click Run from QAT toolbar and scroll to the bottom of page'''

        
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/API", run_item)
        
        '''Verify the runtime options'''
        '''Step 3.1. Scroll to the bottom of page'''
        '''Step 3.2. 100 LS 2 DOOR AUTO is selected for W Germany'''
        time.sleep(4)
        hcanvas.wait_for_web_object_exist("[id^='combobox']", 2, 30, 1)
        
        hcanvas.verify_web_object_no_of_elements("[id^='button']", 4, 'Step 3. Verify no of buttons')
        hcanvas.verify_web_object_no_of_elements("[id^='listbox']", 4, 'Step 3. Verify no of listbox')
        hcanvas.verify_web_object_no_of_elements("[id^='combobox']", 2, 'Step 3. Verify no of combobox items')
        hcanvas.verify_web_object_no_of_elements("[id^='customselect']", 7, 'Step 3. Verify no of custom select')
        hcanvas.verify_web_object_no_of_elements("[id^='text']", 4, 'Step 3. Verify no of text')
       
        hcanvas.verify_web_object_no_of_elements("[id^='multisourcetreecontrol']", 116, 'Step 3. Verify no of multi source tree control items')
        hcanvas.verify_web_object_visible("#multisourcetreecontrol1_2_11:checked", True, 'Step 3. Verify 100 LS 2 DOOR AUTO is checked')
       
       
        '''Step 4. Select Yellow and click the button'''
        hcanvas.click_on_web_element("#listbox1 > option:nth-child(4)")
        time.sleep(5)
        hcanvas.click_on_web_element("#button1")
        time.sleep(5)
        
        hcanvas.verify_web_object_visible("#listbox2 > option:nth-child(4):checked", True, 'Step 4 Verify index value is checked')
        hcanvas.verify_web_object_visible("#listbox3 > option:nth-child(4):checked", True, 'Step 4 Verify value is checked')
        hcanvas.verify_web_object_visible("#listbox4 > option:nth-child(4):checked", True, 'Step 4 Verify display value is checked')
        
        
        
        '''Step 5. Click button under the Drop Down control'''
        time.sleep(5)
        hcanvas.click_on_web_element("#button2")
        time.sleep(5)
        
        hcanvas.verify_web_object_visible("#listbox2 > option:nth-child(1):checked", True, 'Step 5 Verify index value is checked')
        hcanvas.verify_web_object_visible("#listbox3 > option:nth-child(1):checked", True, 'Step 5 Verify value is checked')
        hcanvas.verify_web_object_visible("#listbox4 > option:nth-child(5):checked", True, 'Step 5 Verify display value is checked')
        
        '''Step 6. Click button under the Double list control'''
        time.sleep(5)
        hcanvas.click_on_web_element("#button7")
        time.sleep(5)
        
        hcanvas.verify_web_object_visible("#listbox2 > option:nth-child(1):checked", True, 'Step 6 Verify index value is checked')
        hcanvas.verify_web_object_visible("#listbox3 > option:nth-child(2):checked", True, 'Step 6 Verify value is checked')
        hcanvas.verify_web_object_visible("#listbox4 > option:nth-child(9):checked", True, 'Step 6 Verify display value is checked')
        
        '''Step 7. Click on 'Display Selected Values' button'''
        time.sleep(5)
        hcanvas.click_on_web_element("#button8")
        time.sleep(5)
        
        val_text=automation.TextControl(Name="Selected Value: ENGLAND,FRANCE,ITALY,JAPAN,W GERMANY")
        hcanvas.verify_object_exist(val_text, True, 'Step 7. Verify Selected Value: ENGLAND,FRANCE,ITALY,JAPAN,W GERMANY msgbox displayed')
        
        '''Step 8. Click OK from message box'''
        
        btn_ok=automation.ButtonControl(Name="OK")
        hcanvas.click_on_UI_element(btn_ok)
        time.sleep(10)
        
        val_text=automation.TextControl(Name="Selected Display Value: ENGLAND,FRANCE,ITALY,JAPAN,W GERMANY")
        hcanvas.verify_object_exist(val_text, True, 'Step 8. Verify Display Selected Value: ENGLAND,FRANCE,ITALY,JAPAN,W GERMANY msgbox displayed')
        stat=automation.ButtonControl(Name="OK").Exists()
        print (stat)
        btn_ok=automation.ButtonControl(Name="OK")
        hcanvas.click_on_UI_element(btn_ok)
        time.sleep(10)
        
        '''Step 9. Close HtmlPage browser page'''
        
        hcanvas.close_browser_session()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
        
if __name__=='__main__' :
    unittest.main()
