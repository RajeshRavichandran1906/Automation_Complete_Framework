'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157555
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2229763'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
from common.lib import as_utility 
import uiautomation as automation
from common.pages import as_ribbon, as_html_canvas_area

import time,unittest,pyautogui,datetime

class C2229763_TestClass(AS_BaseTestCase):
    
    def test_C2229763(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        as_ribbonobj=as_ribbon.AS_Ribbon(self.driver)
        tree_path="Domains->P292_S10032_G157549"
        item="HTML_Canvas"
        as_utilobj.select_home_button()
        acanvas_obj=as_html_canvas_area.AS_Html_Canvas(self.driver)
        
        '''Step 1. Navigate to the domain P292_S10032_G157549'''
        '''Step 1.1. Expand the domain P292_S10032_G157549'''
        '''Step 2. Right click on HTML_Canvas folder->New-> HTML/Document, click Next, click Finish.''' 
        hcanvas.create_new_html_canvas_document(tree_path, item)
        '''Step 2.1. Click on Save Selection and draw on canvas'''
        acanvas_obj.drag_drop_on_canvas('Components', 'Save Selection', 50, 50, 100, 100)
             
        '''Step 3. Click on Controls tab, place a Drop Down, a List Box, a Radio Button, a Check Box and a Calendar control on the canvas'''
        acanvas_obj.drag_drop_on_canvas('Controls', 'Drop Down', 150, 150, 250, 200)
        acanvas_obj.drag_drop_on_canvas('Controls', 'List Box', 150, 200, 250, 300)
        acanvas_obj.drag_drop_on_canvas('Controls', 'Radio Button', 300, 200, 400, 300)
        acanvas_obj.drag_drop_on_canvas('Controls', 'Check Box', 450, 200, 550, 300)
        acanvas_obj.drag_drop_on_canvas('Controls', 'Calendar', 150, 50, 250, 100)
             
             
        '''Step 4. Click Settings panel and pinned'''
             
        '''Step 5. Select the Radio Button control and populate with Static values by clicking the new icon 4 times'''
        automation.PaneControl(Name="HtmlPage").Click(350,250)
        as_utilobj.expand_doc_pane('Settings')
        time.sleep(5)
        for i in range(4):
            automation.ToolBarControl(AutomationId='23001').SplitButtonControl(Name="New").Click(10,10)
            time.sleep(5)
             
        '''Step 6. Select the Check Box control and populate with Static values by clicking the new icon 4 times'''
        automation.PaneControl(Name="HtmlPage").Click(500,250)
        as_utilobj.expand_doc_pane('Settings')
        time.sleep(5)
        for i in range(4):
            automation.ToolBarControl(AutomationId='23001').SplitButtonControl(Name="New").Click(10,10)
            time.sleep(5)   
        '''Step 7. Select the Calendar control and check Current/Start date'''
        '''Step 7.1. There is no ability to add New Static Value'''
        automation.PaneControl(Name="HtmlPage").Click(170,55)
        time.sleep(5)
        as_utilobj.expand_doc_pane('Settings')
        time.sleep(5)
        chkbox=automation.CheckBoxControl(Name="Current/Start date")
        hcanvas.click_on_UI_element(chkbox)
        '''Step 8. Select the Drop Down control and click on Settings panel, check Dynamic radio button; Data Source -> Click on selection button(...) and double click on car.mas in 'Open File' window'''
        automation.PaneControl(Name="HtmlPage").Click(180,160)
        time.sleep(2)
        as_utilobj.expand_doc_pane('Settings')
             
        as_utilobj.settings_pane_select_data_source("ibisamp", "car.mas")
             
        '''Step 9. Populate the 'Value from' field, click on selection button (...) and double click on COUNTRY data field from the list'''
        as_utilobj.expand_doc_pane('Settings')
        as_utilobj.settings_pane_select_value_from("COUNTRY")
        '''Step 10. Select the List Box control and click on Settings panel, check Dynamic radio button'''
        automation.PaneControl(Name="HtmlPage").Click(180,210)
        as_utilobj.expand_doc_pane('Settings')
             
        pane=automation.PaneControl(Name="Settings")
        automation.WaitForExist(pane, 30)
             
        radio=automation.RadioButtonControl(Name="Dynamic")
        radio.MoveCursor()
        radio.Click()
             
        '''Step 10.1. Populate the 'Value from' field, click on selection button (...) and double click on CAR data field from the list; Unpinned the Settings panel'''
        as_utilobj.settings_pane_select_value_from("CAR")
             
        '''Step 11. Click on Drop Down control, then press ?and hold shift key,? click on List box'''
        automation.PaneControl(Name="HtmlPage").Click(180,160)
        time.sleep(2)
        automation.KeyDown(automation.Keys.VK_SHIFT, 2)
        time.sleep(2)
        automation.PaneControl(Name="HtmlPage").Click(180,210)
        time.sleep(2)
        automation.KeyUp(automation.Keys.VK_SHIFT, 2)
        time.sleep(5)
       
        '''Step 11.1. Click on 'Utilities' tab and click on 'Add' from Chaining group'''
        '''Step 11.2. Both Drop Down and List Box are selected'''
        as_ribbonobj.click_ribbon_item('Utilities', 'add')
             
        '''Step 12. Save the HTML Page; Click Run'''
        hcanvas.refresh_tree_and_close_canvas_item("Domains")
        
        as_utilobj.save_as_UI_dialog("C2229763")
               
        time.sleep(6)
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/HTML_Canvas", "C2229763.htm")
        
        hcanvas.wait_for_web_object_exist("#radio1", 1, 30, 1)
        
        today=datetime.datetime.today().strftime("%Y%m%d")
        today=today[2:]
        hcanvas.verify_web_object_visible("#calendar1", True, "Step 12. Verify Calendar textbox")
        hcanvas.verify_web_object_visible("body img[src*='dynCalendar']", True, "Step 12. Verify Calendar image")
        hcanvas.verify_web_object_visible("#saveButton", True, "Step 12. Verify Save Button")
        hcanvas.verify_web_object_visible("#combobox1", True, "Step 12. Verify Combo dropdown")
        hcanvas.verify_web_object_visible("#listbox1", True, "Step 12. Verify Listbox control")
        hcanvas.verify_web_object_visible("#radio1", True, "Step 12. Verify radio control")
        hcanvas.verify_web_object_visible("#checkbox1", True, "Step 12. Verify checkbox control")
        
        hcanvas.verify_web_object_no_of_elements("#radio1 table tbody tr", 4, 'Step 12. Verify no of radiobutton elements')
        hcanvas.verify_web_object_no_of_elements("#checkbox1 table tbody tr", 4, 'Step 12. Verify no of checkbox elements')
        hcanvas.verify_web_object_no_of_elements("#listbox1 option", 3, 'Step 12. Verify no of listbox elements')
        hcanvas.verify_web_object_no_of_elements("#combobox1 option", 5, 'Step 12. Verify no of combobox elements')
        
        '''Step 12.1. Calendar will contain the date of test case execution'''
        
        hcanvas.verify_web_element_attribute("#calendar1", 'rawvalue', today, 'Step 12.1 Verify Calendar contains todays date of execution')
        
        '''Step 13. Highlight TOYOTA in the List Box Control and click the Save Selection button'''
        
        hcanvas.select_combobox_option_item("#combobox1", 'value', 'JAPAN')
        
        time.sleep(3)
        
        hcanvas.click_on_web_element("#listbox1 > option:nth-child(2)")
        time.sleep(3)
        
        hcanvas.click_on_web_element("#saveButton")
       
        '''Step 14. From the Save File Content window, append the default title with listbox and click Save'''
        hcanvas.switch_to_window(1)
        hcanvas.click_on_web_element_default("#IbfsOpenFileDialog7_cbFileName input[id^='BiTextField']")
        time.sleep(2)
        pyautogui.hotkey('ctrl','a')
        time.sleep(2)
        pyautogui.hotkey('del')
        time.sleep(2)
        automation.SendKeys('save_selectionlistbox')
        
        time.sleep(6)
        hcanvas.wait_for_web_object_exist("[id^='IbfsOpenFileDialog7_btnOK']", 1, 20, 1)
        
        hcanvas.click_on_web_element_default("[id^='IbfsOpenFileDialog7_btnOK']")
        time.sleep(6)
        
        hcanvas.click_web_button_exists("//div[contains(text(), 'Yes')]")
        time.sleep(6)
        
        hcanvas.switch_to_main_window()
        
        '''Step 15. Close Browser and close the HTML page and save'''
        hcanvas.close_browser_session()
        '''Step 16. Right click on save_selectionlistbox and Run'''
        '''Step 16.1. Verify output'''
        '''Step 17. Close the browser page'''
        
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/HTML_Canvas", "save_selectionlistbox.htm")
        
        hcanvas.wait_for_web_object_exist("#radio1", 1, 30, 1)
        
        hcanvas.verify_web_object_text_visible("#listbox1 > option:nth-child(2)", 'TOYOTA', 'Step 16.1. Verify the listbox selected text is TOYOTA')
        
        '''Step 14. Close Browser page'''
        hcanvas.close_browser_session()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        
if __name__=='__main__' :
    unittest.main()
