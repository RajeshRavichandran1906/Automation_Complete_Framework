'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157549
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2036824'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods

import time,unittest
import keyboard as keys

class C2036815_TestClass(AS_BaseTestCase):
    
    def test_C2036815(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        #hcanvas_web=html_canvas.Html_Canvas(self.se_driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        tree_path="Domains->P292_S10032_G157549->API"
        item="IbComposer execute"
        run_item="IbComposer_execute.htm"
        as_utilobj.select_home_button()
        browser = UtillityMethods.parseinitfile(self,'browser')
        
        '''Step 1. Navigate to Domains P292_S10032_G157549, Expand API folder'''
        '''Step 1.2. Right click on IbComposer_setCurrentSelectionAS and click Open.'''
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
        dialog_control=automation.WindowControl(ClassName="#32770")
        automation.WaitForExist(dialog_control, 30)
        dialog_control.ButtonControl(Name="Yes").Click()
        
        button_control=automation.ButtonControl(Name="Display Report in New Window")
        hcanvas.wait_for_object_exist(button_control, 30) 
        
         
        
        'Verify the Design Pane'
        pane_control=automation.PaneControl(Name="HtmlPage")
        pane_control1=automation.PaneControl(Name="WebFOCUS Report")
        hcanvas.verify_object_exist(pane_control1, True, 'Step 1.1 Verify Report Pane exists')
        
        pane_control2=automation.PaneControl(regexName="*empty.htm")
        hcanvas.verify_object_exist(pane_control2, True, 'Step 1.2 Verify Emtpy Report Pane exists')
        
        button_control1=automation.ButtonControl(Name="Display Report in Frame")
        button_control2=automation.ButtonControl(Name="Display Report in Target")
        
        hcanvas.verify_total_no_of_child_objects(pane_control, 7, 'Step 1. Verify Total no of objects inside Pane')
        
        hcanvas.verify_object_exist(button_control, True, 'Step 1.3 Verify Button Display Report in New Window exists')
        hcanvas.verify_object_exist(button_control1, True, 'Step 1.4 Verify Button Display Report in Frame exists')
        hcanvas.verify_object_exist(button_control2, True, 'Step 1.5 Verify Button Display Report in Target exists')
        
         
        '''Step 1.3. Click Run from QAT toolbar and scroll to the bottom of page'''

        
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/API", run_item)
        
        
        hcanvas.wait_for_web_object_exist("body table", 1, 30, 1)
        
        time.sleep(10)
        
        hcanvas.switch_to_web_frame("[id='report1']")
        '''To create dataset'''
        hcanvas.create_web_table_data("html body table tbody tr", "C2036815.xlsx")
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C2036815.xlsx", 'Step 1.3 Verify Report in main window')
        
        hcanvas.switch_to_default_content()
        time.sleep(4)
        hcanvas.verify_web_object_visible("#button1", True, 'Step 1.3. Verify Buton1 is visible')
        hcanvas.verify_web_object_visible("#button2", True, 'Step 1.3. Verify Buton2 is visible')
        hcanvas.verify_web_object_visible("#button3", True, 'Step 1.3. Verify Buton3 is visible')
        hcanvas.verify_web_object_visible("#text1", True, 'Step 1.3. Verify Text1 is visible')
        
        
        time.sleep(4)
        
        '''Step 2. Click on "Display Report in New Window" button'''
        '''Step 2.1. Report displays in new window'''
        
        hcanvas.click_on_web_element("#button2")
        time.sleep(4)
        hcanvas.switch_to_window(1)
        time.sleep(4)
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C2036815.xlsx", 'Step 2.1 Verify Report in new windows')
        
        '''Step 3. Close the WebFOCUS Report browser page and click on "Display Report in Frame" button'''
        '''Step 3.1. Report displays in the Frame'''
        
        hcanvas.switch_to_main_window()
        
        hcanvas.click_on_web_element("#button3")
        
        hcanvas.switch_to_web_frame("[id='iframe1']")
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C2036815.xlsx", 'Step 3.1 Verify Report in main window')
        
        
        time.sleep(4)
        hcanvas.switch_to_default_content()
        
        '''Step 4. Click on "Display Report in Target"'''
        '''Step 4.1. Report displays in new window'''
        
        hcanvas.click_on_web_element("#button1")
        time.sleep(4)
        hcanvas.switch_to_window(1)
        time.sleep(4)
        hcanvas.verify_web_table_data("html body table tbody tr", "C2036815.xlsx", 'Step 4.1 Verify Report in new windows')
        
        '''Step 5. Close the HtmlPage browser page and click on 'Close all tabs'''
        hcanvas.close_browser_session()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
        

        
    
        
if __name__=='__main__' :
    unittest.main()
