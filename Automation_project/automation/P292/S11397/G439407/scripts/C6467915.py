'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/11397&group_by=cases:section_id&group_order=asc&group_id=439407
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6467915'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area
import time,unittest
import keyboard as Keys
import pyautogui, platform


class C6467915_TestClass(AS_BaseTestCase):
    
    def test_C6467915(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        tree_path="Domains"
        folder_item="P292_S10032_G156801"
        fex_item="C6467915"
        as_utilobj.select_home_button()
        browser = UtillityMethods.parseinitfile(self,'browser')
        acanvas_obj=as_html_canvas_area.AS_Html_Canvas(self.driver)
        as_ribbon_obj= as_ribbon.AS_Ribbon(self.driver)
        
        '''Step 1. Right click on folder P292_S10032_G156801-> New-> Report'''
        '''Step 1.1. Click ibisamp'''
        '''Step 1.2. Click on employee.mas'''
        '''Step 1.3. Click Ok.'''
           
        hcanvas.create_new_report_options(tree_path, folder_item, 'context_menu', "ibisamp", "employee.mas")
            
             
        '''Step 1.4. Double click on LAST_NAME, FIRST_NAME, CURR_SAL'''
    
        hcanvas.add_fields_in_report_painter(['LAST_NAME','FIRST_NAME', 'CURR_SAL'])
          
         
        '''Step 2. Click Report tab'''
        '''Step 2.1. Click on Header & Footer drop down arrow and click Page Header'''
        automation.TabItemControl(Name='Report').Click(waitTime=1)
          
          
        automation.SplitButtonControl(Name="Header  Footer").Click(waitTime=1)
          
        for i in range(0,2):
            automation.SendKey(automation.Keys.VK_DOWN, waitTime=3)
            time.sleep(2)
        automation.SendKey(automation.Keys.VK_ENTER, waitTime=3)
        time.sleep(3)
        '''Step 3. Type LINE1 and LINE2 in Page Heading area'''
        if platform.release()=="10":
            automation.PaneControl(AutomationId="59648").DocumentControl(ClassName="RICHEDIT50W").Click(25,4)
        else:
            automation.PaneControl(AutomationId="59648").EditControl(ClassName="RICHEDIT50W").Click(25,4)
        automation.SendKeys("Line1")
        time.sleep(1)
        automation.SendKey(automation.Keys.VK_ENTER, waitTime=3)
        time.sleep(1)
        automation.SendKeys("Line2")
        time.sleep(1)
          
        '''Step 4. Right click on Page Header area-- > Select context menu Alignment Grid'''
        if platform.release()=="10":
            automation.PaneControl(AutomationId="59648").DocumentControl(ClassName="RICHEDIT50W").RightClick(25,4)
        else:
            automation.PaneControl(AutomationId="59648").EditControl(ClassName="RICHEDIT50W").RightClick(25,4)
        time.sleep(4)
          
        menu_item=automation.MenuItemControl(Name="Alignment Grid...")
        hcanvas.click_on_UI_element(menu_item)
          
        '''Step 5. In Report Canvas select cell Line1-> click on pushbutton Center Justification'''
        '''Step 5.1. Verify correct Report Canvas presentation'''
        automation.PaneControl(AutomationId="100").Click(20,5)
        time.sleep(4)
        automation.ButtonControl(Name="Center").Click()
         
        automation.PaneControl(AutomationId="59648").Click(400,400)
        time.sleep(10)
        as_utilobj.verify_picture_using_sikuli('c6467915_step05.png', 'Step 5. Verify report presentation on canvas')
         
        '''Step 6. Click Run'''
        '''Step 6.1. Verify correct STYLING in report output:'''
        hcanvas.refresh_tree_and_close_canvas_item("Domains") 
               
        as_utilobj.save_as_UI_dialog(fex_item)
             
        time.sleep(6)
           
        hcanvas.run_canvas_item_in_browser(folder_item, "C6467915.fex")
        time.sleep(4)
        hcanvas.wait_for_web_object_exist("html body table", 1, 40, 1)
        
#         hcanvas.create_web_table_data("html body table tbody tr", "C6467915_Ds01.xlsx")
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467915_Ds01.xlsx", 'Step 6.1 Verify Correct report output')
        
        hcanvas.verify_web_element_css("body > table > tbody > tr:nth-child(1) table tbody tr table tbody tr td.x3", "text-align", "center", "Step 6. Verify the center alignment for line1")
        hcanvas.verify_web_element_css("body > table > tbody > tr:nth-child(1) table tbody tr table tbody tr td.x4", "text-align", "left", "Step 6. Verify the left alignment for line2")
        '''Step 7. Close report output, close Report Canvas and save Report1'''
        hcanvas.close_browser_session()
        time.sleep(6)
        
        #hcanvas.refresh_tree_and_close_canvas_item(folder_item)

        '''Step 8. Right click on Report1 and select Open'''
        hcanvas.open_html_canvas_document(folder_item, fex_item)
        
        object=automation.TreeItemControl(Name="LAST_NAME")
        hcanvas.wait_for_object_exist(object, 45)
        '''Step 8.1. Verify correct Report Canvas presentation'''
        automation.PaneControl(AutomationId="59648").Click(400,400)
        time.sleep(10)
        as_utilobj.verify_picture_using_sikuli('c6467915_step05.png', 'Step 8. Verify report presentation on canvas')
        '''Step 9. Click Run'''
        '''Step 9.1. Verify correct STYLING in report ooutput:'''
        hcanvas.run_canvas_item_in_browser(folder_item, "C6467915.fex")
        time.sleep(4)
        hcanvas.wait_for_web_object_exist("html body table", 1, 40, 1)
        
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467915_Ds01.xlsx", 'Step 9.1 Verify Correct report output')
        hcanvas.verify_web_element_css("body > table > tbody > tr:nth-child(1) table tbody tr table tbody tr td.x3", "text-align", "center", "Step 9. Verify the center alignment for line1")
        hcanvas.verify_web_element_css("body > table > tbody > tr:nth-child(1) table tbody tr table tbody tr td.x4", "text-align", "left", "Step 9. Verify the left alignment for line2")
        
        '''Step 9.1. Close report output'''
        '''Step 9.2. Close Report Canvas'''
        
        hcanvas.close_browser_session()
        as_utilobj.select_home_button()
        hcanvas.refresh_tree_and_close_canvas_item("Domains")
        
        '''Step 9.3. Right click on Report1 and select Delete'''
        time.sleep(10)
        hcanvas.select_UI_item_using_right_click_menu(folder_item, fex_item, "Delete")
        
        object=automation.ButtonControl(Name="Yes")
        hcanvas.wait_for_object_exist(object, 45)
        
        hcanvas.click_on_UI_element(object)
    
if __name__=='__main__' :
    unittest.main()
