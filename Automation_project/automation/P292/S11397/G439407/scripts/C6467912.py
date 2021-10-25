'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/11397&group_by=cases:section_id&group_order=asc&group_id=439407
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6467912'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area
import time,unittest
import keyboard as Keys
import pyautogui


class C6467912_TestClass(AS_BaseTestCase):
    
    def test_C6467912(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        tree_path="Domains"
        folder_item="P292_S10032_G156801"
        fex_item="ATEST"
        as_utilobj.select_home_button()
        browser = UtillityMethods.parseinitfile(self,'browser')
        acanvas_obj=as_html_canvas_area.AS_Html_Canvas(self.driver)
        as_ribbon_obj= as_ribbon.AS_Ribbon(self.driver)
        
        '''Step 1. Right click on folder P292_S10032_G156801-> New-> Report'''
        '''Step 2. In Select Data Source dialog select master file ibisamp/car.mas-> Click Ok.'''
          
        hcanvas.create_new_report_options(tree_path, folder_item, 'context_menu', "ibisamp", "car.mas")
          
           
        '''Step 3. In Object Inspector double click on fields COUNTRY, CAR, DEALER_COST, RETAIL_COST, SALES'''
  
        hcanvas.add_fields_in_report_painter(['COUNTRY','CAR','DEALER_COST','RETAIL_COST','SALES'])
            
        '''Step 4. Click on tab Report-> Click on Filter'''
        automation.TabItemControl(Name='Report').Click(waitTime=1)
        time.sleep(3)
        automation.SplitButtonControl(Name="Filter").Click(waitTime=1)
           
        '''Step 5. Select Where from dropdown'''
        automation.SendKey(automation.Keys.VK_DOWN, waitTime=3)
        time.sleep(3)
        automation.SendKey(automation.Keys.VK_ENTER, waitTime=3)
        time.sleep(3)
        win_control=automation.WindowControl(Name="Expression Builder")
        hcanvas.wait_for_object_exist(win_control,30)
        time.sleep(8)
        hcanvas.verify_object_exist(win_control, True, 'Step 5.1. Verify Expression builder is open')
          
        '''Step 6. In Expression Builder double click on COUNTRY on the List Tree-> Select equals for Logical Relation-> Select Parameter(Editor) for Compare Type'''
        '''Step 7. Double Click on <Please,specify> in Compare Value'''
        '''Step 7.1. Verify, that Variable Editor open'''
          
        automation.TreeItemControl(Name="COUNTRY").DoubleClick()
        time.sleep(5)
        win_control.TextControl(Name="Criteria (WHERE)").PaneControl(AutomationId="1").Click(470,5)
        time.sleep(5)
        win_control.ListItemControl(Name="equals").Click()
        time.sleep(5)
        win_control.TextControl(Name="Criteria (WHERE)").PaneControl(AutomationId="1").Click(582,5)
        time.sleep(5)
        automation.MenuItemControl(Name="Parameter").Click()
        time.sleep(2)
        automation.MenuItemControl(Name="Editor").Click()
         
        '''Step 7. Double Click on <Please,specify> in Compare Value'''
        '''Step 7.1. Verify, that Variable Editor open'''
        win_control.TextControl(Name="Criteria (WHERE)").PaneControl(AutomationId="1").Click(680,5)
         
         
        var_editor=automation.WindowControl(Name="Variable Editor")
        hcanvas.wait_for_object_exist(var_editor,30)
        time.sleep(8)
        hcanvas.verify_object_exist(var_editor, True, 'Step 7.1. Verify Variable Editor is open')
         
        '''Step 8. Click OK in Variable Editor'''
        '''Step 8.1. Verify created expression'''
        automation.ButtonControl(Name="OK").Click()
        time.sleep(8)
        as_utilobj.verify_picture_using_sikuli('c6467912_step08.png', 'Step 8.1 Verify the created expression')
         
         
        '''Step 9. Click OK in Expression Builder'''
        automation.ButtonControl(Name="OK").Click()
        time.sleep(8)
         
        '''Step 10. Execute report request'''
        '''Step 10.1. Verify prompt'''
         
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
          
        hcanvas.run_canvas_item_in_browser(folder_item, "ATEST.fex")
        time.sleep(6)
        object_css="#promptPanel"
        hcanvas.wait_for_web_object_exist(object_css, 1, 65, 1)
        time.sleep(10)
        hcanvas.verify_web_object_no_of_elements(object_css, 1, 'Step 10.1. Verify prompt')
        
        '''back button'''
        hcanvas.verify_web_object_no_of_elements("#promptPanel a[class^='autop-btn-back']",1, 'Step 10.1. Verify back button')
        '''refresh button'''
        hcanvas.verify_web_object_no_of_elements("#promptPanel a[class^='autop-btn-refresh']",1, 'Step 10.1. Verify refresh button')
        '''submit button'''
        hcanvas.verify_web_object_no_of_elements("#promptPanel a[class^='autop-btn-submit']",1, 'Step 10.1. Verify submit button')
        '''control container'''
        hcanvas.verify_web_object_no_of_elements("#promptPanel div[class^='autop-amper-ctrl-container']",1, 'Step 10.1. Verify prompt control container')
        '''editbox'''
        hcanvas.verify_web_object_no_of_elements("#ui-id-1",1, 'Step 10.1. Verify editbox')
        
        '''Step 11. Type FRANCE for Country-> click Run'''
        '''Step 11.1. Verify correct data in report output'''
        
        hcanvas.click_on_web_element("#ui-id-1")
        pyautogui.typewrite("FRANCE")
        
        hcanvas.click_on_web_element("#promptPanel a[class^='autop-btn-submit']")
        
        time.sleep(10)
        hcanvas.switch_to_web_frame("#mainPage iframe")
        object_css="html body table tbody tr"
        hcanvas.wait_for_web_object_exist(object_css, 1, 65, 1)
        time.sleep(10)
#         hcanvas.create_web_table_data("html body table tbody tr", "C6467912_Ds01.xlsx")
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467912_Ds01.xlsx", 'Step 11.1 Verify Correct report output')
        
        '''Step 12. Close the output, Report Canvas and save as ATEST'''
        

        hcanvas.close_browser_session()
        as_utilobj.select_home_button()
        hcanvas.refresh_tree_and_close_canvas_item(folder_item)
         
        '''Step 13. Reopen ATEST in Report Canvas'''
        hcanvas.open_html_canvas_document(folder_item, fex_item)
        
        object=automation.TreeItemControl(Name="COUNTRY")
        hcanvas.wait_for_object_exist(object, 45)
        
        '''Step 13.1. Verify that &COUNTRY shown shown in Object Inspector Report Variables'''
        
        object=automation.TreeItemControl(Name="&COUNTRY")
        hcanvas.verify_object_exist(object, True, 'Step 13.1. Verify &COUNTRY shown in object inspector')
        
        
        '''Step 14. Execute report request'''
        '''Step 15. Type FRANCE for Country-> click Run'''
        '''Step 15.1. Verify correct data in report output'''
        hcanvas.run_canvas_item_in_browser(folder_item, "ATEST.fex")
        time.sleep(6)
        object_css="#promptPanel"
        hcanvas.wait_for_web_object_exist(object_css, 1, 65, 1)
        time.sleep(10)
        
        hcanvas.click_on_web_element("#ui-id-1")
        pyautogui.typewrite("FRANCE")
        
        hcanvas.click_on_web_element("#promptPanel a[class^='autop-btn-submit']")
        time.sleep(10)
        hcanvas.switch_to_web_frame("#mainPage iframe")
        object_css="html body table tbody tr"
        hcanvas.wait_for_web_object_exist(object_css, 1, 65, 1)
        time.sleep(10)
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467912_Ds01.xlsx", 'Step 15.1 Verify Correct report output')
        
        '''Step 16. Close report output, close Report Canvas'''
        '''Step 17. Delete ATEST.fex'''
        

        hcanvas.close_browser_session()
        as_utilobj.select_home_button()
        hcanvas.refresh_tree_and_close_canvas_item(folder_item)
       
        time.sleep(10)
        hcanvas.select_UI_item_using_right_click_menu(folder_item, fex_item, "Delete")
        
        object=automation.ButtonControl(Name="Yes")
        hcanvas.wait_for_object_exist(object, 45)
        
        hcanvas.click_on_UI_element(object)
        
                        
if __name__=='__main__' :
    unittest.main()
