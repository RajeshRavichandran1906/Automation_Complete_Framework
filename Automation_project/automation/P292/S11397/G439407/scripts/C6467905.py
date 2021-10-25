'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/11397&group_by=cases:section_id&group_order=asc&group_id=439407
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6467905'''

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


class C6467905_TestClass(AS_BaseTestCase):
    
    def test_C6467905(self):
        
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
        '''Step 2.1. Verify that master file CAR open in Report Canvas'''
        
        hcanvas.create_new_report_options(tree_path, folder_item, "context_menu", 'ibisamp', 'car.mas')   
         
        object=automation.TreeItemControl(Name="COUNTRY")
        hcanvas.wait_for_object_exist(object, 45)
        hcanvas.verify_object_exist(object, True, 'Step 2.1. Verify CAR master file is open')
         
        time.sleep(10)
         
        '''Step 3. Double click on fields COUNTRY, CAR, SALES in Object Inspector'''
        '''Step 3.1. Verify report presentation on canvas'''
         
        hcanvas.add_fields_in_report_painter(['COUNTRY','CAR','SALES'])
         
        time.sleep(15)
 
        '''verify the design time output'''
        as_utilobj.verify_picture_using_sikuli('c6467905_step3.png', 'Step 3. Verify report presentation on canvas')
         
        '''Step 4. Execute report request'''
        '''Step 4.1. Verify correct data in report output'''
         
        '''save the report'''
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
        object_css="body > table"
        hcanvas.wait_for_web_object_exist(object_css, 1, 45, 1)
        time.sleep(10)
        hcanvas.create_web_table_data("html body table tbody tr", "C6467905_Ds01.xlsx")
         
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467905_Ds01.xlsx", 'Step 4.1 Verify Correct report output')
         
        '''Step 5. Close report output. Close Report canvas'''
         
        as_utilobj.close_web_window()
         
        '''Step 6. Click Yes in AppStudio message:'''
        '''Step 7. In Save As dialog box type ATEST for File Name -> click OK'''
        as_utilobj.select_home_button()
        hcanvas.refresh_tree(folder_item)
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
           
        as_utilobj.save_as_UI_dialog(fex_item)
        hcanvas.refresh_tree_and_close_canvas_item(folder_item)
         
         
        '''Step 8. Right click on ATEST-> Open'''
        '''Step 8.1. Verify no parsing error and correct Report Canvas presentation'''
         
         
        hcanvas.open_html_canvas_document(folder_item, fex_item)
         
        object=automation.TreeItemControl(Name="COUNTRY")
        hcanvas.wait_for_object_exist(object, 45)
        time.sleep(10)
        as_utilobj.verify_picture_using_sikuli('c6467905_step8.png', 'Step 8. Verify report presentation on canvas')
         
        '''Step 9. Execute report request'''
        '''Step 9.1. Verify correct data in report output'''
         
        hcanvas.run_canvas_item_in_browser(folder_item, "ATEST.fex")
        time.sleep(6)
        object_css="body > table"
        hcanvas.wait_for_web_object_exist(object_css, 1, 45, 1)
        time.sleep(10)
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467905_Ds01.xlsx", 'Step 9.1 Verify Correct report output')
         
        hcanvas.close_browser_session()
         
        '''Step 10. Close report output, close Report Canvas'''
        '''Step 11. Right click on ATEST.fex -> Select context menu Delete'''
        '''Step 12. click Yes in AppStudio Warning'''
         
        as_utilobj.select_home_button()
        hcanvas.refresh_tree_and_close_canvas_item(folder_item)
        time.sleep(10)
         
        hcanvas.select_UI_item_using_right_click_menu(folder_item, fex_item, "Delete")
         
        object=automation.ButtonControl(Name="Yes")
        hcanvas.wait_for_object_exist(object, 45)
         
        hcanvas.click_on_UI_element(object)
        
        '''Step 13. Click on pushbutton Report on Home toolbar'''
        '''Step 14. In Report Wizard click on pushbutton Create Report'''
        '''Step 15. Select P292_S10032_G156801 in Select Procedure Location-> Click Next'''
        '''Step 16. In Select Data Source select master file ibisamp/car.mas-> Finish'''

        hcanvas.create_new_report_options(tree_path, folder_item, "toolbar_button",'ibisamp', 'car.mas') 

        '''Step 16.1. Verify that master file CAR open in Report Canvas'''
        object=automation.TreeItemControl(Name="COUNTRY")
        hcanvas.wait_for_object_exist(object, 45)
        hcanvas.verify_object_exist(object, True, 'Step 16.1. Verify CAR master file is open')
        
        
        '''Step 17. In Object Inspector double click on fields COUNTRY, CAR, SALES'''
        '''Step 17.1. Verify report presentation on canvas'''
        
        hcanvas.add_fields_in_report_painter(['COUNTRY','CAR','SALES'])
        
        time.sleep(15)

        '''verify the design time output'''
        as_utilobj.verify_picture_using_sikuli('c6467905_step3.png', 'Step 17. Verify report presentation on canvas')
        
        '''Step 18. Execute report request'''
        '''Step 18.1. Verify correct report output'''
        
        '''save the report'''
        
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
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467905_Ds01.xlsx", 'Step 18.1 Verify Correct report output')
        
        '''Step 19. Close report output. Close Report canvas'''
        '''Step 20. Click Yes in AppStudio message:'''
        '''Step 21. In Save As dialog box type ATEST for File Name -> click OK'''

        as_utilobj.close_web_window()

        hcanvas.refresh_tree(folder_item)
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
          
        as_utilobj.save_as_UI_dialog(fex_item)
        
        hcanvas.refresh_tree_and_close_canvas_item(folder_item)
        '''Step 22. Right click on ATEST-> Open'''
        '''Step 22.1. Verify no parsing error and correct Report Canvas presentation'''

       
        hcanvas.open_html_canvas_document(folder_item, fex_item)
        
        object=automation.TreeItemControl(Name="COUNTRY")
        hcanvas.wait_for_object_exist(object, 45)
        
        as_utilobj.verify_picture_using_sikuli('c6467905_step8.png', 'Step 22. Verify report presentation on canvas')
        
        '''Step 23. Execute report request'''
        '''Step 23.1. Verify correct data in report output'''
        
        '''save the report'''
        
        hcanvas.refresh_tree(folder_item)
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
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467905_Ds01.xlsx", 'Step 23 Verify Correct report output')
        
        hcanvas.close_browser_session()
        '''Step 24. Close report output, close Report Canvas'''
        '''Step 25. Right click on ATEST.fex-> Select context menu Delete'''
        '''Step 26. Click Yes in AppStudio Warning '''
        as_utilobj.select_home_button()
        hcanvas.refresh_tree_and_close_canvas_item(folder_item)
        
        hcanvas.select_UI_item_using_right_click_menu(folder_item, fex_item, "Delete")
        
        object=automation.ButtonControl(Name="Yes")
        hcanvas.wait_for_object_exist(object, 45)
        
        hcanvas.click_on_UI_element(object)
                
if __name__=='__main__' :
    unittest.main()
