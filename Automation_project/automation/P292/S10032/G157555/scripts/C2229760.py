'''@author: Robert 
c
Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157555
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2229760'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area

import time,unittest,pyautogui
import keyboard as keys

class C2229760_TestClass(AS_BaseTestCase):
    
    def test_C2229760(self):
        
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
        
        '''Step 1. Navigate to the domain P292_S10032_G157549'''
        '''Step 1.1. Expand the domain P292_S10032_G157549'''
        '''Step 2. Right click on HTML_Canvas folder->New-> HTML/Document, click Next, click Finish.'''
        hcanvas.create_new_html_canvas_document(tree_path, item) 
            
        '''Step 3. Place a Hyperlink element on the canvas'''
        as_utilobj.expand_doc_pane('Tasks & Animations')
           
        '''Step 3.1. Before placing an Hyperlink'''
          
        ui_object=automation.ListControl(AutomationId='15689')
        hcanvas.wait_for_object_exist(ui_object,15)
        hcanvas.verify_total_no_of_child_objects(ui_object, 1, 'Step 3.1 Verify only 1 item present before placing hyperlink')
        ui_object=automation.ListItemControl(Name="load")
        hcanvas.verify_object_exist(ui_object, True, 'Step 3.1. Verify only load item is present')
           
        '''Step 3.2. After placing an hyperlink; a Task is created'''
        automation.PaneControl(Name="HtmlPage").Click(580,550) 
        time.sleep(4)
        acanvas_obj.drag_drop_on_canvas('Components', 'Hyperlink', 50, 50, 350, 350)
        time.sleep(15)
        as_utilobj.expand_doc_pane('Tasks & Animations')
        ui_object=automation.ListControl(AutomationId='15689')
        hcanvas.wait_for_object_exist(ui_object,15)
        hcanvas.verify_total_no_of_child_objects(ui_object, 2, 'Step 3.2 Verify only 1 item present before placing hyperlink')
        ui_object1=automation.ListItemControl(Name="load")
        hcanvas.verify_object_exist(ui_object1, True, 'Step 3.2. Verify load item is present')
        ui_object2=automation.ListItemControl(Name="task2")
        hcanvas.verify_object_exist(ui_object2, True, 'Step 3.2. Verify task2 item is present')
           
        '''Step 4. Double click on hyperlink text'''
           
        automation.PaneControl(Name="HtmlPage").Click(580,550)
           
        time.sleep(5)
        ui_object=automation.TextControl(Name="go to...")
        ui_object.DoubleClick()
           
        '''Step 5. Select Hyperlink text and press delete button.'''
        '''Step 5.1. Type 'Open URL in windows' in the hyperlink'''
        '''Step 5.2. Click outside the hyperlink.'''
        time.sleep(3)
        automation.SendKey(automation.Keys.VK_HOME, waitTime=3)
        time.sleep(3)
        automation.SendKeys('{Shift}{End}')
        time.sleep(3)
        automation.SendKey(automation.Keys.VK_DELETE, waitTime=3)
        time.sleep(3)
           
        value="Open URL in windows"
        time.sleep(2)
        pyautogui.typewrite(value)
        time.sleep(5)
        automation.PaneControl(Name="HtmlPage").Click(580,550)
        time.sleep(5)
        ui_object=automation.TextControl(Name=value)
        hcanvas.verify_object_exist(ui_object, True, 'Step 4. Verify hyperlink text is changed')
           
        '''Step 6. Click on Requests & Data Sources panel'''
        as_utilobj.expand_doc_pane('Requests & Data Sources')
           
        '''Step 6.1. Click on drop down arrow next to New'''
        '''Step 6.2. Click on URL request; type www.informationbuilders.com after the // and click OK'''
        hcanvas.select_new_item_from_requests_datasource_menu("Url Request...")
           
        object1=automation.EditControl(AutomationId='23521')
        hcanvas.wait_for_object_exist(object1, 15)
        object1.SetValue("http://www.informationbuilders.com")
           
        button_control=automation.ButtonControl(Name="OK")
        hcanvas.click_on_UI_element(button_control)
           
        '''Step 7. For Requests/Actions, click on drop down arrow'''
        '''Step 7.1. Run Request->Request1 and select Same Window for Target/Template Name in the drop down list'''
        as_utilobj.expand_doc_pane('Tasks & Animations')
           
        hcanvas.select_dropdown_item_from_run_requests_menu('Run Request->Request1')
   
        '''Step 8. Click on Image, draw a place holder on canvas;'''
        '''Step 8.1. Double click on mickey-mouse-14.jpg'''
           
        acanvas_obj.drag_drop_on_canvas('Components', 'Image', 450, 50, 750, 350)
   
        win_control=automation.WindowControl(Name="Open File")
      
        hcanvas.wait_for_object_exist(win_control, 30)
        automation.TextControl(Name="mickey-mouse-14.jpg").DoubleClick(40,10)
        time.sleep(4)
        '''Step 9. Click on Requests & Data sources panel, click on drop down arrow next to New'''
        '''Step 9.1. Click on External Request->WebFOCUS Procedure'''
        '''Step 9.2. Double click on ActiveFormatReport.fex'''
   
           
        as_utilobj.expand_doc_pane('Requests & Data Sources')
           
        hcanvas.select_new_item_from_requests_datasource_menu("External Request->WebFOCUS Procedure...")
        win_control=automation.WindowControl(Name="Open File")
      
        hcanvas.wait_for_object_exist(win_control, 30)
        automation.TextControl(Name="ActiveFormatReport.fex").DoubleClick(40,10)
        time.sleep(4)
           
        '''Step 10. Click on Tasks & Animations panel, click on click on drop down arrow next to New Task3 is created'''
        as_utilobj.expand_doc_pane('Tasks & Animations')
        hcanvas.select_new_item_from_requests_datasource_menu("New")
           
        time.sleep(15)
        ui_object=automation.ListControl(AutomationId='15689')
        hcanvas.wait_for_object_exist(ui_object,15)
        hcanvas.verify_total_no_of_child_objects(ui_object, 3, 'Step 10.2 Verify only 3 item present in the lisbox')
          
        ui_object2=automation.ListItemControl(Name="task3")
        hcanvas.verify_object_exist(ui_object2, True, 'Step 10.2. Verify task3 item is present')
        '''Step 11. For Trigger Identifier, check image1; for Requests/Actions, click on drop down arrow Run Request->ActiveFormatReport and select Same Window for Target/Template Name in the drop down list'''
           
           
        chkbox=automation.CheckBoxControl(Name='image1')
        chkbox.Toggle()
        time.sleep(3)
        hcanvas.select_dropdown_item_from_run_requests_menu('Run Request->ActiveFormatReport')
        ui_object=automation.ComboBoxControl(AutomationId='23456').ButtonControl(Name="Open")
           
        list_item=automation.ListItemControl(Name="Same window")
           
        hcanvas.click_on_UI_element(ui_object)
        time.sleep(3)
        hcanvas.click_on_UI_element(list_item)
           
        '''Step 12. Click Run and click on go to...'''
        hcanvas.refresh_tree(item)
        time.sleep(6)
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
             
        as_utilobj.save_as_UI_dialog("hyperlink1")
             
        time.sleep(6)
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/HTML_Canvas", "hyperlink1.htm")
        
        hcanvas.wait_for_web_object_exist("body div img", 1, 30, 1)
        
        hcanvas.verify_web_object_visible("a[id='anchor1']", True, "Step 12. Verify hyperlink")
        hcanvas.verify_web_object_visible("body div img", True, "Step 12. Verify Mickey mouse image")
        '''click on go to'''
        hcanvas.click_on_web_element("a[id='anchor1']")
        time.sleep(6)
        hcanvas.switch_to_window(1)
        '''Step 12.1. Information Builders page should load'''
        expected_url="informationbuilders.com"
        hcanvas.verify_current_web_url(expected_url, 'Step 12. Verify Information Builders page is loaded')
        
        '''Step 13. Close Browser page and click on Image'''
        hcanvas.switch_to_main_window()
        hcanvas.click_on_web_element("body div img")
        time.sleep(6)
        
        '''Step 14. Close Browser page'''
#         hcanvas.create_web_table_data("table[id='ITableData0'] tbody tr", "C2229760.xlsx")
#         
        hcanvas.verify_web_table_data("table[id='ITableData0'] tbody tr", "C2229760.xlsx", 'Step 14.1 Verify Report in main window')
        
        hcanvas.switch_to_main_window()
        
        hcanvas.close_browser_session()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
    
        
if __name__=='__main__' :
    unittest.main()
