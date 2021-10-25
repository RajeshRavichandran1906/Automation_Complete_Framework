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

class C6467926_TestClass(AS_BaseTestCase):
    
    def test_C6467926(self):
        
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
        '''Step 2. Right click on HTML_Canvas folder-> New-> HTML/Document.'''
        '''Step 3. Click 4-2-1 Responsive Template and Click Finish'''
        
           
        hcanvas.create_new_html_canvas_document_options(tree_path, item,template="4-2-1")
        object=automation.GroupControl(AutomationId="windowPanel8")
        hcanvas.wait_for_object_exist(object, 45)
        
        time.sleep(10)
        
        '''verify the design time output'''
        as_utilobj.verify_picture_using_sikuli('421_canvas.png', 'Step 3. Verify canvas output')
        
        '''Step 4. Click Run'''
        '''Step 5. Close the browser page'''
        
#         win=automation.PaneControl(Name="HtmlPage")
#         hcanvas.wait_for_object_exist(win, 40)
#         time.sleep(5)
#         automation.PaneControl(Name="HtmlPage").RightClick(300,200)
#         time.sleep(10)
        
        '''save the report'''
        hcanvas.refresh_tree(item)
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
          
        as_utilobj.save_as_UI_dialog("C6467926.htm")
        
        time.sleep(6)
        
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/HTML_Canvas", "C6467926.htm")
        time.sleep(6)
        object_css="[id^='windowPanel8'] [id^='windowPanel8']"
        hcanvas.wait_for_web_object_exist(object_css, 1, 45, 1)
        time.sleep(10)
        
        hcanvas.verify_web_object_no_of_elements("[id^='windowPanel']", 16, 'Step 4. verify no of panel elements')
        hcanvas.verify_web_object_text_visible("[id^='windowPanel8']", "OutputWidgetTitle", 'Step 4. Verify panel title')
        
        as_utilobj.verify_picture_using_sikuli('421_runtime.png', 'Step 4. Verify runtime output')
        as_utilobj.close_web_window()
        
        '''Step 6. Right click on any Output Widget Title frame'''
        as_utilobj.maximize_setfocus_ui_window("App")
        automation.GroupControl(AutomationId="windowPanel4").RightClick()
        
        object=automation.ToolBarControl(AutomationId="1")
        hcanvas.wait_for_object_exist(object, 15)
        
        menu_list=['New Report', 'New Chart', 'New Document', 'Import existing...', 'Reference existing procedure...', 'Html page...', 'Map', 'ESRI', 'Use as Toolbox']
        
        a=object.GetChildren()
        actual_list=[i.Name for i in a]
        print ('actual_list',actual_list)
#         for i in a:
#             actual_list= (i.GetWindowText())
#             actual_list1= (i.Name)
#         print ('actual_list',actual_list)
#         print ('actual_list1',actual_list1)       
        as_utilobj.asequal(menu_list,actual_list, 'Step 6. Verify right click menu list')
        
        '''Step 7. Close the HTML page'''
        hcanvas.refresh_tree_and_close_canvas_item(item)
        
        
        '''Step 8. Right click on HTML_Canvas folder-> New-> HTML/Document, click Next, click Finish'''
        '''Step 9. Click 2-2 Responsive Template and Click Finish'''
        hcanvas.create_new_html_canvas_document_options(tree_path, item,template="2-2")
        object=automation.GroupControl(AutomationId="windowPanel5")
        hcanvas.wait_for_object_exist(object, 45)
        
        '''Step 10. Right click on Output Widget Container'''
        '''Step 10.1. AS per the JIRA AS-5384 update size is removed from AS from AS 8202 release'''
        
        object=automation.TextControl(Name="Output widgets container")
        
        object.RightClick()
        
        object=automation.ToolBarControl(AutomationId="1")
        hcanvas.wait_for_object_exist(object, 15)
        
        menu_list=['Template configuration...', 'Append new widget', 'Add page header', 'Edit text', 'Cut\tCtrl+X', 'Copy\tCtrl+C', 'Paste\tCtrl+V', 'Paste - Keep position', 'Delete', 'Select All\tCtrl+A', 'Add selected to new container', 'Style...', 'Properties']
        
        a=object.GetChildren()
        actual_list=[i.Name for i in a]
        print ('actual_list',actual_list)
        as_utilobj.asequal(menu_list,actual_list, 'Step 10. Verify right click menu list')


        '''Step 11. Click Template Configuration'''
        
        object=automation.MenuItemControl(Name="Template configuration...")
        hcanvas.click_on_UI_element(object)

        object=automation.WindowControl(Name="Template Configuration")
        hcanvas.wait_for_object_exist(object, 45)
        
        '''Step 12. Click Add'''
        object=automation.ButtonControl(Name="Add")
        hcanvas.click_on_UI_element(object)
        
        object=automation.GroupControl(AutomationId="windowPanel6")
        hcanvas.wait_for_object_exist(object, 45)
        
        time.sleep(10)
        
        
        as_utilobj.verify_picture_using_sikuli('22_added_row.png', 'Step 12. Verify the new panel is added')
        '''Step 13. Click Remove'''
        object=automation.ButtonControl(Name="Remove")
        hcanvas.click_on_UI_element(object)
        
        time.sleep(30)
        
        
        as_utilobj.verify_picture_using_sikuli('22_removed_row.png', 'Step 13. Verify the new panel is removed')
        
        
        '''Step 14. Click Column-based, click Add'''
        object=automation.RadioButtonControl(Name="Column-based")
        hcanvas.click_on_UI_element(object)
        time.sleep(5)
        object=automation.ButtonControl(Name="Add")
        hcanvas.click_on_UI_element(object)
        
        object=automation.GroupControl(AutomationId="windowPanel7")
        hcanvas.wait_for_object_exist(object, 45)
        
        time.sleep(10)
        
        as_utilobj.verify_picture_using_sikuli('22_added_col.png', 'Step 14. Verify the new panel is added in column')
        
        '''Step 15. Close the HTML page without saving'''
              
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
        
        object=automation.ButtonControl(Name="No")
        hcanvas.wait_for_object_exist(object, 25)
        hcanvas.click_on_UI_element(object)
        
if __name__=='__main__' :
    unittest.main()
