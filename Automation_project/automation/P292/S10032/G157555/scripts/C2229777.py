'''@author: Robert 


Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157555
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2229777'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area

import time,unittest,pyautogui,datetime
import keyboard as keys

class C2229777_TestClass(AS_BaseTestCase):
    
    def test_C2229777(self):
        
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
            
        '''Step 2.1. Click Report and draw the report container on the canvas.'''
           
        acanvas_obj.drag_drop_on_canvas('Components', 'Report', 50, 50, 350, 350)
        time.sleep(5)
        '''Step 3. Click Report and draw a container in the canvas.'''
        '''Step '3.1. Right click within the report container and select "Import existing report"'''
        automation.PaneControl(Name="HtmlPage").RightClick(180,180)
              
        menu_item=automation.MenuItemControl(Name="Import existing report")
        hcanvas.wait_for_object_exist(menu_item, 20)
        menu_item.MoveCursor()
        time.sleep(3)
        hcanvas.click_on_UI_element(menu_item)
              
        win_control=automation.WindowControl(Name="Open File")
           
        '''Step 3.1. Double click on ActiveFormatReport.fex'''
          
        hcanvas.wait_for_object_exist(win_control, 30)
        automation.TextControl(Name="ActiveFormatReport.fex").DoubleClick(40,10)
        time.sleep(4)
         
        '''Step 4. Click Controls tab, and click on the Tree icon and select Select Multi source Tree control and draw on the canvas'''
         
        as_ribbonobj.switch_as_tab('Controls')
        time.sleep(4)
        as_utilobj.click_element_using_ui(split_button_with_offset='Tree', x=10, y=50, send_keys=['down','down'])
        time.sleep(4)
        html = self.driver.find_element_by_name("HtmlPage")
        acanvas_obj.drag_drop_by_coordinate_offsets(html, html, 400, 50, 700, 650)
        time.sleep(9)
         
        '''Step 5. Click on Parameters Tab, right click on multisourcetreecontrol1 and select 'Add Level' from the context menu'''
         
        as_utilobj.click_picture_using_sikuli('bottom_4_tabs.png', "70","5", "double")
        time.sleep(40)
        object=automation.PaneControl(Name="about:blank")
        hcanvas.wait_for_object_exist(object, 40)
        time.sleep(30)
        automation.PaneControl(Name="about:blank").RightClick(60,30)
        time.sleep(7)
        automation.MenuItemControl(Name="Add level").DoubleClick()
        time.sleep(7)
        automation.PaneControl(Name="about:blank").Click(60,30)
         
        '''Step 6. Select First level, click on Settings panel'''
         
        as_utilobj.expand_doc_pane('Settings')
         
        '''Step 6.1. Click on 'Active Report' radio button from the Data type; select report1 -> Menu Option Types default to "List of columns"'''
        btn=automation.RadioButtonControl(Name="Active Report")
        btn.MoveCursor()
        btn.Click()
        time.sleep(5)
        automation.ListItemControl(Name="report1").Click()
        time.sleep(5)
 
        automation.ComboBoxControl(AutomationId='23235').Click()
        time.sleep(5)
        automation.ListItemControl(Name="List of columns").Click()
         
        '''Step 7. Select Second level, click on Settings panel'''
        automation.PaneControl(Name="about:blank").Click(130,30)
        time.sleep(5)
        as_utilobj.expand_doc_pane('Settings')
         
        '''Step 7.1. Click on 'Active Report' radio button select report1 -> Menu Option Types select 'Column value' from the drop down list'''
        btn=automation.RadioButtonControl(Name="Active Report")
        btn.MoveCursor()
        btn.Click()
        time.sleep(5)
        automation.ListItemControl(Name="report1").Click()
        time.sleep(5)
 
        automation.ComboBoxControl(AutomationId='23235').Click()
        time.sleep(5)
        automation.ListItemControl(Name="Column value").Click()
         
         
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
                 
        as_utilobj.save_as_UI_dialog("C2229777")
         
         
        '''Step 8. Click Run, expand COUNTRY from the Tree and select "FRANCE"'''
         
        
        time.sleep(6)
        
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/HTML_Canvas", "C2229777.htm")
        time.sleep(6)
        
        
        hcanvas.wait_for_web_object_exist("#report1", 1, 30, 1)
        
        for i in range(1,2):
            hcanvas.verify_web_object_visible("#report"+str(i), True, "Step 8. Verify Report"+str(i) +" visible")
        
        for i in range(1,2):
            hcanvas.verify_web_object_visible("label[id^='multisource']", True, "Step 8. Verify form"+str(i) +" visible")
        
        hcanvas.verify_web_object_no_of_elements("label[id^='multisource']", 20, "Step 8. Verify no of listbox elements")
        
        hcanvas.create_web_table_data("html body table tbody tr", "C2229777_Ds01.xlsx")
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C2229777_Ds01.xlsx", 'Step 8.2 Verify Report1 in iframe')
       
        hcanvas.click_on_web_element("#multisourcetreecontrol1_image_1 > img")
        time.sleep(3)
        hcanvas.click_on_web_element("#multisourcetreecontrol1_1_1")
        time.sleep(3)
        
        hcanvas.create_web_table_data("html body table tbody tr", "C2229777_Ds02.xlsx")
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C2229777_Ds02.xlsx", 'Step 8.2 Verify Report1 in iframe')
        
        
        '''Step 9. Expand CAR from the Tree and select "AUDI"'''
        
        hcanvas.switch_to_default_content()
        hcanvas.click_on_web_element("#multisourcetreecontrol1_image_2 > img")
        time.sleep(3)
        hcanvas.click_on_web_element("#multisourcetreecontrol1_1_6")
        time.sleep(3)
        
        hcanvas.create_web_table_data("html body table tbody tr", "C2229777_Ds03.xlsx")
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C2229777_Ds03.xlsx", 'Step 9.2 Verify Report1 in iframe')
        
        '''Step 10. Close the browser page, close and save the HTML page'''
        
        hcanvas.close_browser_session()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
    
        
if __name__=='__main__' :
    unittest.main()

