'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/11397&group_by=cases:section_id&group_order=asc&group_id=439407
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6467907'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area
import time,unittest
import keyboard as Keys
import pyautogui


class C6467907_TestClass(AS_BaseTestCase):
    
    def test_C6467907(self):
        
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
        
        '''Step 1. Right click on P292_S10032_G156801-> New-> Report'''
        '''Step 2. In Select Data Source select master file ibisamp/car.mas and click Ok.'''
        hcanvas.create_new_report_options(tree_path, folder_item, "context_menu", 'ibisamp', 'car.mas')   
          
        object=automation.TreeItemControl(Name="COUNTRY")
        hcanvas.wait_for_object_exist(object, 45)
        hcanvas.verify_object_exist(object, True, 'Step 2.1. Verify CAR master file is open')
          
        time.sleep(10)
         
         
        '''Step 3. In Object Inspector double click on filed COUNTRY , CAR, SALES'''
         
          
        hcanvas.add_fields_in_report_painter(['COUNTRY','CAR','SALES'])
          
        '''Step 4. In tab Report click on pushbutton Drill Down'''
        automation.TabItemControl(Name='Report').Click(waitTime=1)
        time.sleep(3)
        automation.ButtonControl(Name="Drill Down").Click(waitTime=1)
         
        '''Step 5. In Drill Down dialog box click on Add New Item'''
         
        object=automation.WindowControl(Name="Drill Down")
        hcanvas.wait_for_object_exist(object, wait_time=30)
        automation.WindowControl(Name="Drill Down").ButtonControl(Name="Add new item").Click()
        time.sleep(3)
        '''Step 6. Double click on Source-> In Open File dialog box select DD_Child.fex'''
        '''Step 6.1. Click Ok'''
        automation.WindowControl(Name="Drill Down").TextControl(AutomationId="1000").PaneControl(ClassName="AfxWnd110u").DoubleClick(400,4)
         
        win_control=automation.WindowControl(Name="Open File")
        hcanvas.wait_for_object_exist(win_control, wait_time=30)
        hcanvas.select_item_from_tree_view("P292_S10032_G156801", "DD_Child.fex", 'OK')
         
         
        '''Step 7. In Drill Down dialog box double click on Parameters'''
        automation.WindowControl(Name="Drill Down").TextControl(AutomationId="1000").PaneControl(ClassName="AfxWnd110u").DoubleClick(710,4)
         
        '''Step 8. In Parameters dialog box click on Add New Item'''
        win_control=automation.WindowControl(Name="Parameters")
        hcanvas.wait_for_object_exist(win_control, wait_time=30)
        automation.WindowControl(Name="Parameters").ButtonControl(Name="Add new item").Click()
         
        '''Step 9. Type COUNTRY for Parameter name, select CAR.ORIGIN.COUNTRY from drop down for Parameter value'''
        automation.WindowControl(Name="Parameters").TextControl(AutomationId="1000").PaneControl(ClassName="AfxWnd110u").DoubleClick(10,4)
        time.sleep(3)
         
        automation.WindowControl(Name="Parameters").EditControl(AutomationId="123").SetValue("COUNTRY", 2)
        automation.SendKey(automation.Keys.VK_ENTER, waitTime=3)
        time.sleep(3)
         
        automation.WindowControl(Name="Parameters").TextControl(AutomationId="1000").PaneControl(ClassName="AfxWnd110u").Click(423,4)
        time.sleep(3)
        automation.WindowControl(Name="Parameters").ListItemControl(Name="CAR.ORIGIN.COUNTRY").Click()
        '''Step 10. Click Ok in Parameters, click OK in Drill Down '''
        automation.WindowControl(Name="Parameters").ButtonControl(Name="OK").Click()
        time.sleep(3)
        automation.WindowControl(Name="Drill Down").ButtonControl(Name="OK").Click()
        time.sleep(3)
        '''Step 11. Execute Report'''
        hcanvas.refresh_tree(folder_item)
        as_utilobj.select_component_by_right_click(right_click_item="Domains",click="Refresh Descendants")
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
        object_css="body > table"
        hcanvas.wait_for_web_object_exist(object_css, 1, 45, 1)
        time.sleep(10)
         
        '''Step 11.1 Verify that all values in report output underlined'''
        hcanvas.create_web_table_data("html body table tbody tr", "C6467905_Ds01.xlsx")
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467905_Ds01.xlsx", 'Step 11.1 Verify Correct report output')
         
        hcanvas.verify_web_object_no_of_elements("html body table tbody tr a", 28, 'Step 11.1. Verify all values in report are underlined')
         
        '''Step 12. Click on ENGLAND'''
        '''Step 12.1. Drilldown1 appears in report output'''
        '''Step 13. Click on Drilldown1Verify correct data report output from DD_Child.fex'''
         
        hcanvas.select_report_autolink_tooltip_value("html body table", 2, 1, "DrillDown 1")
         
        time.sleep(10)
        #hcanvas.create_web_table_data("html body table tbody tr", "C6467907_Ds01.xlsx")
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467907_Ds01.xlsx", 'Step 13.1 Verify drilldown report output')
         
         
         
        '''Step 14. Close report output, close Report Canvas, save report as ATEST'''
        hcanvas.close_browser_session()
        as_utilobj.select_home_button()
        hcanvas.refresh_tree(folder_item)
        as_utilobj.select_component_by_right_click(right_click_item="Domains",click="Refresh Descendants")
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
           
        as_utilobj.save_as_UI_dialog(fex_item)
         
        time.sleep(6)
        '''Step 15. Double click ATEST to reopen in Report Canvas.'''
        as_utilobj.select_home_button()
        hcanvas.refresh_tree_and_close_canvas_item(folder_item)
        time.sleep(10)
        automation.TreeItemControl(Name=folder_item).ScrollIntoView()
        if automation.ExpandCollapseState.Collapsed==automation.TreeItemControl(Name=folder_item).CurrentExpandCollapseState():
            time.sleep(2)
            print ("im in here")
            automation.TreeItemControl(Name=folder_item).Expand(waitTime=2)
        time.sleep(2)
        automation.TreeItemControl(Name=fex_item).ScrollIntoView()
        
        automation.TreeItemControl(Name=fex_item).DoubleClick(waitTime=3)
        text_control=automation.WindowControl(Name="Project View")
        hcanvas.wait_for_object_exist(text_control, 30)
        
        
        
        
        '''Step 16. In tab Report click on pushbutton Hyperlink'''
        automation.TabItemControl(Name='Report').Click(waitTime=1)
        time.sleep(3)
        automation.ButtonControl(Name="Drill Down").Click(waitTime=1)
        
        object=automation.WindowControl(Name="Drill Down")
        hcanvas.wait_for_object_exist(object, wait_time=30)
        
        '''Step 16.1. Verify correct presentation in Drill Down dialog box'''
        '''Step 17. Click OK in Drill down'''
        time.sleep(10)
        as_utilobj.verify_picture_using_sikuli('c6467907_step16.png', 'Step 16.1. Verify Drilldown dialog shows correct values')
        time.sleep(3)
        automation.WindowControl(Name="Drill Down").ButtonControl(Name="OK").Click()
        time.sleep(3)
        
        '''Step 18. Execute report request'''
        
        time.sleep(6)
        
        hcanvas.run_canvas_item_in_browser(folder_item, "ATEST.fex")
        time.sleep(6)
        object_css="body > table"
        hcanvas.wait_for_web_object_exist(object_css, 1, 45, 1)
        time.sleep(10)
        
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467905_Ds01.xlsx", 'Step 11.1 Verify Correct report output')
        
        hcanvas.verify_web_object_no_of_elements("html body table tbody tr a", 28, 'Step 11.1. Verify all values in report are underlined')
        
        '''Step 19. Click on ENGLAND-> click on Click on Drilldown1Verify correct data report output from DD_Child.fex'''
        
        hcanvas.select_report_autolink_tooltip_value("html body table", 2, 1, "DrillDown 1")
        
        time.sleep(10)
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467907_Ds01.xlsx", 'Step 13.1 Verify drilldown report output')
        
        
        '''Step 20. Close report output, close Report Canvas'''
        hcanvas.close_browser_session()
            
        as_utilobj.close_canvas_item()
        
        '''Step 21. Delete ATEST.fex'''
        time.sleep(10)
         
        hcanvas.select_UI_item_using_right_click_menu(folder_item, fex_item, "Delete")
         
        object=automation.ButtonControl(Name="Yes")
        hcanvas.wait_for_object_exist(object, 45)
         
        hcanvas.click_on_UI_element(object)
        
                        
if __name__=='__main__' :
    unittest.main()
