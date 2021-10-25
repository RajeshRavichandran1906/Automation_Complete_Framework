'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/11397&group_by=cases:section_id&group_order=asc&group_id=439407
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6467914'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area
import time,unittest
import keyboard as Keys
import pyautogui


class C6467914_TestClass(AS_BaseTestCase):
    
    def test_C6467914(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        tree_path="Domains"
        folder_item="P292_S10032_G156801"
        fex_item="C6467914"
        as_utilobj.select_home_button()
        browser = UtillityMethods.parseinitfile(self,'browser')
        acanvas_obj=as_html_canvas_area.AS_Html_Canvas(self.driver)
        as_ribbon_obj= as_ribbon.AS_Ribbon(self.driver)
        
        '''Step 1. Right click on folder P292_S10032_G156801-> New-> Report'''
        '''Step 1.1. Click ibisamp'''
        '''Step 1.2. Click on employee.mas'''
        '''Step 1.3. Click Ok.'''
          
        hcanvas.create_new_report_options(tree_path, folder_item, 'context_menu', "ibisamp", "employee.mas")
           
            
        '''Step 1.4. Double click on DEPARTMENT, LAST_NAME, FIRST_NAME, CURR_SAL, SALARY'''
   
        hcanvas.add_fields_in_report_painter(['DEPARTMENT', 'LAST_NAME','FIRST_NAME', 'CURR_SAL','SALARY'])
         
        '''Step 2. Click Format tab'''
 
        automation.TabItemControl(Name='Format').Click(waitTime=1)
         
            
        '''Step 2.1. Click PDF-> click OK in Output Format Options dialog box'''
        time.sleep(3)
        automation.ButtonControl(Name="PDF").Click(waitTime=1)
        object1=automation.WindowControl(Name="Output Format Options")
        hcanvas.wait_for_object_exist(object1, wait_time=30)
         
        btn=automation.ButtonControl(Name="OK")
        hcanvas.click_on_UI_element(btn)
        time.sleep(10)
         
        '''Step 3. Click Report tab'''
        '''Step 3.1. Click on Header & Footer drop down arrow and click Page Header'''
        automation.TabItemControl(Name='Report').Click(waitTime=1)
         
         
        automation.SplitButtonControl(Name="Header  Footer").Click(waitTime=1)
         
        for i in range(0,2):
            automation.SendKey(automation.Keys.VK_DOWN, waitTime=3)
            time.sleep(2)
        automation.SendKey(automation.Keys.VK_ENTER, waitTime=3)
        time.sleep(3)
         
        '''Step 4. Right click on Page Header area-- > Select context menu Alignment Grid'''
        automation.PaneControl(AutomationId="59648").EditControl(ClassName="RICHEDIT50W").RightClick(25,4)
        time.sleep(4)
         
        menu_item=automation.MenuItemControl(Name="Alignment Grid...")
        hcanvas.click_on_UI_element(menu_item)
         
        '''Step 5. In Insert Alignment Grid dialog box check Align with Data and set 5 for number of lines-> Click ok'''
        object1=automation.WindowControl(Name="Insert Alignment Grid")
        hcanvas.wait_for_object_exist(object1, wait_time=30)
         
        automation.CheckBoxControl(Name="Align with Data").Toggle(waitTime=2)
         
        automation.EditControl(Name="Number of lines:").SetValue("5", waitTime=2)
        btn=automation.ButtonControl(Name="OK")
        hcanvas.click_on_UI_element(btn)
         
        '''Step 5.1. Verify correct Report Canvas presentation ( alignment grid appear on Report Canvas'''
        automation.PaneControl(AutomationId="59648").Click(400,400)
        time.sleep(10)
        as_utilobj.verify_picture_using_sikuli('c6467914_step05.png', 'Step 3. Verify report presentation on canvas')
         
         
        '''Step 6. Type something in different cells'''
        '''r1,c1'''
        '''r1,c4'''
        r1=51
        c1=10
        automation.PaneControl(AutomationId="100").Click(r1,c1)
        time.sleep(2)
        automation.SendKeys("11111")
         
        r1=346
        automation.PaneControl(AutomationId="100").Click(r1,c1)
        time.sleep(2)
        automation.SendKeys("fffff")
         
 
        '''r2,c2'''
        '''r2,c5'''
        r2=148
        c2=30
        automation.PaneControl(AutomationId="100").Click(r2,c2)
        time.sleep(2)
        automation.SendKeys("22222")
         
        r2=463
        automation.PaneControl(AutomationId="100").Click(r2,c2)
        time.sleep(2)
        automation.SendKeys("ddddd")
         
        '''r3,c1'''
        '''r3,c3'''
        r3=50
        c1=51
        automation.PaneControl(AutomationId="100").Click(r3,c1)
        time.sleep(2)
        automation.SendKeys("aaaa")
         
        r3=241
        automation.PaneControl(AutomationId="100").Click(r3,c1)
        time.sleep(2)
        automation.SendKeys("3333")
         
        '''r4,c2'''
        '''r4,c4'''
        r4=148
        c2=70
        automation.PaneControl(AutomationId="100").Click(r4,c2)
        time.sleep(2)
        automation.SendKeys("bbbb")
         
        r4=346
        automation.PaneControl(AutomationId="100").Click(r4,c2)
        time.sleep(2)
        automation.SendKeys("444443")
         
        '''r5,c3'''
        '''r5,c5'''
        r5=241
        c3=90
        automation.PaneControl(AutomationId="100").Click(r5,c3)
        time.sleep(2)
        automation.SendKeys("ccccc")
         
        r5=463
        automation.PaneControl(AutomationId="100").Click(r5,c3)
        time.sleep(2)
        automation.SendKeys("5555555")
         
        '''Step 7. Click Run'''
        '''Step 7.1. Verify correct STYLING in report output'''
         
         
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
          
        hcanvas.run_canvas_item_in_browser(folder_item, "C6467914.fex")
        time.sleep(40)
        
#         hcanvas.create_web_table_data("html body table tbody tr", "C6467913_Ds01.xlsx")
#         hcanvas.verify_web_table_data("html body table tbody tr", "C6467914_Ds01.xlsx", 'Step 7.1 Verify Correct report output')
#        
        if browser=="Firefox":
            print ("im here in ff")
            as_utilobj.verify_picture_using_sikuli('c6467914_step07_ff.png', 'Step 7. Verify alignment in runtime report')
        elif browser=="Chrome":
            print ("im here in cr")
            as_utilobj.verify_picture_using_sikuli('c6467914_step07_cr.png', 'Step 7. Verify alignment in runtime report')
        else:
            print ("im here in ie")
            automation.SendKeys('{Ctrl}0')
            time.sleep(10)
            as_utilobj.verify_picture_using_sikuli('c6467914_step07_ie.png', 'Step 7. Verify alignment in runtime report')
        
        
        '''Step 8. Close report output'''
        '''Step 9. Close Report Canvas'''
        '''Step 9.1. Click No in AppStudio prompt message'''
        
        hcanvas.close_browser_session()
        as_utilobj.select_home_button()
        hcanvas.refresh_tree_and_close_canvas_item(folder_item)
        
        '''Created filed deleted for reason of next run'''
        
        as_utilobj.select_component_by_right_click(right_click_item="C6467914",click="Delete")
        time.sleep(2)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
                                
if __name__=='__main__' :
    unittest.main()
