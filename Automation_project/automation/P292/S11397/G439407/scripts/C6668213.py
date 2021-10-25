'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/11397&group_by=cases:section_id&group_order=asc&group_id=439407
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6668213'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area
import time,unittest
import keyboard as Keys
import pyautogui


class C6668213_TestClass(AS_BaseTestCase):
    
    def test_C6668213(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        tree_path="Domains"
        folder_item="P292_S10032_G156801"
        fex_item="C6668213"
        as_utilobj.select_home_button()
        browser = UtillityMethods.parseinitfile(self,'browser')
        acanvas_obj=as_html_canvas_area.AS_Html_Canvas(self.driver)
        as_ribbon_obj= as_ribbon.AS_Ribbon(self.driver)
        sort1_actual=['COUNTRY', 'CAR', 'SALES']
        sort2_actual=['MODEL', 'CAR','SALES']
        
        '''Step 1. Navigate to P292_S10032_G156801 -> New-> Report'''
        '''Step 1.1. In Select Data Source, select ibisamp/car.mas -> click OK'''
          
        hcanvas.create_new_report_options(tree_path, folder_item, 'context_menu', "ibisamp", "car.mas")
          
           
        '''Step 1.2. In Object Inspector double click on fields COUNTRY, CAR, CAR,MODEL, SALES, SALES'''
  
        hcanvas.add_fields_in_report_painter(['COUNTRY','CAR','CAR','MODEL','SALES','SALES'])
            
        
        '''Step 2. Click in second column SALES-> change column type for Detail'''
        automation.TabItemControl(Name='Field').Click(waitTime=1)
        time.sleep(3)
        automation.ButtonControl(Name='Detail').Click(waitTime=1)
        time.sleep(3)
           
        '''Step 3. In tab Report click on Filter-> select Where'''
        automation.TabItemControl(Name='Report').Click(waitTime=1)
        time.sleep(3)
        automation.SplitButtonControl(Name="Filter").Click(waitTime=1)
        time.sleep(3)
        automation.SendKey(automation.Keys.VK_DOWN, waitTime=3)
        time.sleep(3)
        automation.SendKey(automation.Keys.VK_ENTER, waitTime=3)
        time.sleep(3)
        win_control=automation.WindowControl(Name="Expression Builder")
        hcanvas.wait_for_object_exist(win_control,30)
        time.sleep(8)
        hcanvas.verify_object_exist(win_control, True, 'Step 5.1. Verify Expression builder is open')
        
        '''Step 4. In Expression Builder create expression: SALES NE 0'''
        
        automation.TreeItemControl(Name="SALES").DoubleClick()
        time.sleep(5)
        win_control.TextControl(Name="Criteria (WHERE)").PaneControl(AutomationId="1").Click(470,5)
        time.sleep(5)
        win_control.ListItemControl(Name="does not equal").Click()
        time.sleep(5)
        win_control.TextControl(Name="Criteria (WHERE)").PaneControl(AutomationId="1").Click(582,5)
        time.sleep(5)
        automation.MenuItemControl(Name="Value").Click()
         
        
        win_control.TextControl(Name="Criteria (WHERE)").PaneControl(AutomationId="1").DoubleClick(620,5)
         
         
        var_editor=automation.WindowControl(Name="Multiple Value Builder CAR.BODY.SALES")
        hcanvas.wait_for_object_exist(var_editor,30)
        time.sleep(8)
        hcanvas.verify_object_exist(var_editor, True, 'Step 7.1. Verify Variable Editor is open')
        
        automation.ButtonControl(Name="Browse...").Click()
        var_editor1=automation.WindowControl(Name="Value Retrieval")
        hcanvas.wait_for_object_exist(var_editor,30)
        time.sleep(8)
        
        var_editor1.TreeItemControl(Name="SALES").DoubleClick()
        time.sleep(3)
        var_editor.ListItemControl(Name="0").Click(6,4)
        time.sleep(3)
        var_editor.ButtonControl(Name=">>").Click()
        time.sleep(3)
        var_editor.ButtonControl(Name="OK").Click()
        time.sleep(3)
        
        '''Click on ok in the expression builder'''
        
        automation.ButtonControl(Name="OK").Click()
        time.sleep(8)
        
        '''Step 5. Click on Object Inspector tab Sort Group:'''
        automation.TabItemControl(Name='Sort Groups').Click(waitTime=1)
        
        '''Step 6. Drag and Drop CAR from Sort Group1 in Sort Group 2'''
        
        source_item=automation.TreeItemControl(Name="CAR").BoundingRectangle
        s_left=source_item[0]
        s_top=source_item[1]
        s_right=source_item[2]
        s_bottom=source_item[3]
        
        target_item=automation.TreeItemControl(Name="Sort Group 2").BoundingRectangle
        t_left=target_item[0]
        t_top=target_item[1]
        t_right=target_item[2]
        t_bottom=target_item[3]
        
        automation.Win32API.MouseDragDrop(s_left+3, s_top+3, t_left+3, t_top+3,waitTime=5)
        time.sleep(8)
        
        
        
        '''Step 7. Drag and Drop MODEL from Sort Group1 in Sort Group2'''
        source_item=automation.TreeItemControl(Name="MODEL").BoundingRectangle
        s_left=source_item[0]
        s_top=source_item[1]
        s_right=source_item[2]
        s_bottom=source_item[3]
        
        target_item=automation.TreeItemControl(Name="Sort Group 2").BoundingRectangle
        t_left=target_item[0]
        t_top=target_item[1]
        t_right=target_item[2]
        t_bottom=target_item[3]
        
        automation.Win32API.MouseDragDrop(s_left+3, s_top+3, t_left+3, t_top+3,waitTime=5)
        time.sleep(8)
        '''Step 8. Execute report request'''
        
         
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
          
        hcanvas.run_canvas_item_in_browser(folder_item, "C6668213.fex")
        time.sleep(6)
        '''Step 8.1. Verify correct DATA in report output'''
        

        object_css="html body table"
        hcanvas.wait_for_web_object_exist(object_css, 1, 65, 1)
        time.sleep(10)
#         hcanvas.create_web_table_data("html body table tbody tr", "C6668213_Ds01.xlsx")
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C6668213_Ds01.xlsx", 'Step 8.1 Verify Correct report output')
        
        '''Step 9. Close Report Canvas and save Report1'''
        
        

        hcanvas.close_browser_session()
        as_utilobj.select_home_button()
        hcanvas.refresh_tree_and_close_canvas_item(folder_item)
         
        '''Step 10. Reopen Report 1 in Report Canvas, click on Sort Group'''
        
        
        hcanvas.open_html_canvas_document(folder_item, fex_item)
        
        object=automation.TreeItemControl(Name="COUNTRY")
        hcanvas.wait_for_object_exist(object, 45)
        
        
        automation.TabItemControl(Name='Sort Groups').Click(waitTime=1)
        time.sleep(9)
        '''Step 10.1. Verify correct Report Canvas presentation:'''
        
        
        group1=automation.TreeItemControl(Name="Sort Group 1").GetChildren()
        group2=automation.TreeItemControl(Name="Sort Group 2").GetChildren()
        sort1=[]
        sort2=[]
        for i in group1:
            sort1.append(i.AccessibleCurrentName())
        
        for i in group2:
            sort2.append(i.AccessibleCurrentName())
        
        as_utilobj.asequal(sort1,sort1_actual,'Step 10. Verify the sort groups1')
        as_utilobj.asequal(sort2,sort2_actual,'Step 10. Verify the sort groups2')
        
        as_utilobj.verify_picture_using_sikuli('c6668213_step10.png', 'Step 10.1 Verify report canvas')
        
        '''Step 11. Close Report Canvas, delete Report1'''
        
        as_utilobj.select_home_button()
        hcanvas.refresh_tree_and_close_canvas_item(folder_item)
       
        time.sleep(10)
        hcanvas.select_UI_item_using_right_click_menu(folder_item, fex_item, "Delete")
        
        object=automation.ButtonControl(Name="Yes")
        hcanvas.wait_for_object_exist(object, 45)
        
        hcanvas.click_on_UI_element(object)
        
                        
if __name__=='__main__' :
    unittest.main()
