'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157549
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2036814'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods

import time,unittest
import keyboard as keys

class C2036814_TestClass(AS_BaseTestCase):
    
    def test_C2036814(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        #hcanvas_web=html_canvas.Html_Canvas(self.se_driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        tree_path="Domains->P292_S10032_G157549->API"
        item="AS API IbComposer selectTab"
        run_item="AS_API_IbComposer_selectTab.htm"
        as_utilobj.select_home_button()
        browser = UtillityMethods.parseinitfile(self,'browser')
        
        '''Step 1. Navigate to Domains P292_S10032_G157549, Expand API folder'''
        automation.TabItemControl(Name="Home").Click()
        automation.MenuItemControl(Name="All Files").Click()
        stat=automation.TreeItemControl(Name=item).Exists(5,2)
#         
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
 
        button_control=automation.GroupControl(AutomationId="windowPanel1").ButtonControl(Name="Button")
         
        hcanvas.wait_for_object_exist(button_control, 30)
         
        '''Step 2. Right click on IbComposer_selectTab and click Open'''
        'Verify the Design Pane'
        pane_control=automation.PaneControl(Name="HtmlPage")
        hcanvas.verify_object_exist(pane_control, True, 'Step 1. Verify Pane exists')
        group_control=automation.PaneControl(Name="HtmlPage").GroupControl(RegexName="Tab #")
        hcanvas.verify_total_no_of_child_objects(group_control, 8, 'Step 1. Verify Total no of objects inside Group Pane')
        text_control=automation.GroupControl(AutomationId="windowPanel1").TextControl(Name="Tab #1")
        hcanvas.verify_object_exist(text_control, True, 'Step 1. Verify list exists')
         
        hcanvas.verify_object_exist(button_control, True, 'Step 1. Verify Button exists')
        combo_control = automation.GroupControl(AutomationId="windowPanel1").ComboBoxControl(AutomationId="combobox1")
        hcanvas.verify_object_exist(combo_control, True, 'Step 1. Verify Combobox exists')
         
        '''Step 2.1. Click Run from QAT toolbar'''

        
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/API", run_item)
       
        
        '''Step 3. Select Tab 4 value 4 from the drop down list and click on Button'''
        
        hcanvas.wait_for_web_object_exist("#windowPanel1 > div:nth-child(4) > div", 1, 30, 1)
        
        
        hcanvas.select_combobox_option_item("#combobox1", "value", "4")
        
        hcanvas.click_on_web_element("#button1")
        
        value="IBI_pageHeader IBI_pageHeaderTab_TopBottom IBI_DisplayBlock IBI_temp_unselect IBI_pageHeader_Selected"
        hcanvas.verify_web_element_attribute("#windowPanel1 > div:nth-child(4)", "class", value, 'Step 3. Verify Tab4 is selected.')
        
        as_utilobj.verify_web_object_visible("#combobox1", False, 'Step 3. Verify Combobox not visible in Tab 4')
        as_utilobj.verify_web_object_visible("#button1", False, 'Step 3. Verify Button1 not visible in Tab 4')
        
        '''Step 4. Close the HtmlPage browser page'''
        
        hcanvas.close_browser_session()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
    
        
if __name__=='__main__' :
    unittest.main()
