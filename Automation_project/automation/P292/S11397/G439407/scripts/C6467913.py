'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/11397&group_by=cases:section_id&group_order=asc&group_id=439407
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6467913'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area
import time,unittest
import keyboard as Keys
import pyautogui


class C6467913_TestClass(AS_BaseTestCase):
    
    def test_C6467913(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        tree_path="Domains"
        folder_item="P292_S10032_G156801"
        fex_item="C6467913"
        as_utilobj.select_home_button()
        browser = UtillityMethods.parseinitfile(self,'browser')
        acanvas_obj=as_html_canvas_area.AS_Html_Canvas(self.driver)
        as_ribbon_obj= as_ribbon.AS_Ribbon(self.driver)
        
        '''Step 1. Right click on folder P292_S10032_G156801-> New-> Report'''
        '''Step 1.1. Click ibisamp'''
        '''Step 1.2. Click on employee.mas'''
        '''Step 1.3. Click Ok.'''
          
        hcanvas.create_new_report_options(tree_path, folder_item, 'context_menu', "ibisamp", "employee.mas")
          
           
        '''Step 1.4. Double click on FIRST_NAME, LAST_NAME, CURR_SAL'''
  
        hcanvas.add_fields_in_report_painter(['FIRST_NAME','LAST_NAME','CURR_SAL'])
        
        '''Step 2. Click Report tab'''
        
        automation.TabItemControl(Name='Report').Click(waitTime=1)
        time.sleep(3)
        automation.SplitButtonControl(Name="Header  Footer").Click(waitTime=1)
           
        '''Step 2.1. Click on Header & Footer drop down arrow and click Report Header'''
        automation.SendKey(automation.Keys.VK_DOWN, waitTime=3)
        time.sleep(3)
        automation.SendKey(automation.Keys.VK_ENTER, waitTime=3)
        time.sleep(3)
        
        '''Step 2.2. Click on Header & Footer drop down arrow and click Report Footer''' 
        automation.SplitButtonControl(Name="Header  Footer").Click(waitTime=1)
        
        for i in range(0,4):
            automation.SendKey(automation.Keys.VK_DOWN, waitTime=3)
            time.sleep(2)
        automation.SendKey(automation.Keys.VK_ENTER, waitTime=3)
        time.sleep(3)
        
        '''Step 3. Type "This is Report Heading' in Page Heading area on Report Canvas'''
        '''Step 3.1. Type "This is Report Footing' in Page Footing area on Report Canvas'''
        
        automation.PaneControl(AutomationId="59648").EditControl(ClassName="RICHEDIT50W").Click(25,4)
        time.sleep(2)
        automation.SendKeys("This is Report Heading")
        
        footer=automation.PaneControl(AutomationId="59648").EditControl(ClassName="RICHEDIT50W").GetNextSiblingControl()
        footer.Click()
        time.sleep(2)
        automation.SendKeys("This is Report Footing")
        
        automation.PaneControl(AutomationId="59648").Click(400,400)
        time.sleep(10)
        as_utilobj.verify_picture_using_sikuli('c6467913_step03.png', 'Step 3. Verify report presentation on canvas')
        '''Step 4. Click Run'''
        '''Step 4.1. Verify correct DATA in report output'''
        
        
        hcanvas.refresh_tree(folder_item)
        as_utilobj.select_component_by_right_click(right_click_item="Domains",click="Refresh Descendants")
        time.sleep(4)
           
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
          
        time.sleep(2)
             
        as_utilobj.save_as_UI_dialog(fex_item)
           
        time.sleep(6)
          
        hcanvas.run_canvas_item_in_browser(folder_item, "C6467913.fex")
        time.sleep(6)
        object_css="body > table"
        hcanvas.wait_for_web_object_exist(object_css, 1, 45, 1)
        time.sleep(10)
        #hcanvas.create_web_table_data("html body table tbody tr", "C6467913_Ds01.xlsx")
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467913_Ds01.xlsx", 'Step 4.1 Verify Correct report output')
        '''Step 5. Close report output'''
        '''Step 5.1. Close Report canvas'''
        '''Step 5.2. Click Save in App Studio saving prompt message'''
        '''Step 5.3. Type C2224390 for File name and click OK'''

        hcanvas.close_browser_session()
        as_utilobj.select_home_button()
        hcanvas.refresh_tree_and_close_canvas_item(folder_item)
        
        '''Step 6. Right on C2224390 and select Open'''
        '''Step 6.1. Close C2224390 tab'''
        '''Step 6.2. Verify no parsing error and correct Report canvas presentation'''

        hcanvas.open_html_canvas_document(folder_item, fex_item)
        
        object=automation.TreeItemControl(Name="COUNTRY")
        hcanvas.wait_for_object_exist(object, 45)
        
        as_utilobj.verify_picture_using_sikuli('c6467913_step06.png', 'Step 6. Verify report presentation on canvas')
        
        hcanvas.refresh_tree_and_close_canvas_item(folder_item)
        
        '''Created file deleted for reason of next run'''
        
        as_utilobj.select_component_by_right_click(right_click_item="C6467913",click="Delete")
        time.sleep(2)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
                        
if __name__=='__main__' :
    unittest.main()
