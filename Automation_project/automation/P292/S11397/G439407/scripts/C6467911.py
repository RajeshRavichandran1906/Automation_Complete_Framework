'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/11397&group_by=cases:section_id&group_order=asc&group_id=439407
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6467911'''

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


class C6467911_TestClass(AS_BaseTestCase):
    
    def test_C6467911(self):
        
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
           
        '''Step 4. In tab Data click on pushbutton Summary (Compute)'''
        automation.TabItemControl(Name='Data').Click(waitTime=1)
        time.sleep(3)
        automation.ButtonControl(Name="Summary (Compute)").Click(waitTime=1)
         
        '''Step 4.1. Verify that dialog box Computed Field Creator open'''
        win_control=automation.WindowControl(Name="Computed Field Creator")
        as_utilobj.wait_for_UI_object(win_control,30)
        time.sleep(8)
        hcanvas.verify_object_exist(win_control, True, 'Step 4.1. Verify Compute Field Creator dialogbox is open')
        
        
        '''Step 5. In dialog box Computed Field Creator type TEST for name'''
        '''Step 6 Double click on field DEALER_COST, click on pushbutton + , click on pushbutton 7'''
        '''Step 7. Click OK in Computed Field Creator dialog box'''
        
        automation.EditControl(Name="Computed Field Name:").SetValue("TEST", waitTime=2)
        time.sleep(3)
        automation.TreeItemControl(Name="DEALER_COST").DoubleClick()
        time.sleep(3)
        automation.ButtonControl(Name="+").Click()
        time.sleep(3)
        automation.ButtonControl(Name="7").Click()
        time.sleep(3)
        automation.ButtonControl(Name="OK").Click()
        time.sleep(3)
        
        '''Step 7.1. Verify that field TEST appears on report Canvas'''
        as_utilobj.verify_picture_using_sikuli('c6467911_step07.png', 'Step 7.1 Verify that field TEST appears on report Canvas')
        
        
        '''Step 8. Execute report request.Verify correct data in report output.'''
        '''Step 9. Close report output, close Report Canvas and Save ATEST'''
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
        hcanvas.wait_for_web_object_exist(object_css, 1, 65, 1)
        time.sleep(10)
        
        #hcanvas.create_web_table_data("html body table tbody tr", "C6467911_Ds01.xlsx")
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467911_Ds01.xlsx", 'Step 8.1 Verify Correct report output')
        
        hcanvas.close_browser_session()
        as_utilobj.select_home_button()
        hcanvas.refresh_tree_and_close_canvas_item(folder_item)
         
        '''Step 10. Open ATEST in Report Canvas'''
        '''Step 10.1. Verify no parsing error and correct presentation of computed field TEST on Report Canvas'''
        hcanvas.open_html_canvas_document(folder_item, fex_item)
        
        object=automation.TreeItemControl(Name="COUNTRY")
        hcanvas.wait_for_object_exist(object, 45)
        
        as_utilobj.verify_picture_using_sikuli('c6467911_step10.png', 'Step 10.1 Verify report presentation on canvas')
        
        '''Step 11. Execute report request.Verify correct data in report output.'''
        
        hcanvas.run_canvas_item_in_browser(folder_item, "ATEST.fex")
        time.sleep(6)
        object_css="body > table"
        hcanvas.wait_for_web_object_exist(object_css, 1, 65, 1)
        time.sleep(10)
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467911_Ds01.xlsx", 'Step 11.1 Verify Correct report output')
        
        hcanvas.close_browser_session()
        as_utilobj.select_home_button()
        '''Step 12. Close Report Canvas, delete ATEST'''
        hcanvas.refresh_tree_and_close_canvas_item(folder_item)
        time.sleep(10)
        hcanvas.select_UI_item_using_right_click_menu(folder_item, fex_item, "Delete")
        
        object=automation.ButtonControl(Name="Yes")
        hcanvas.wait_for_object_exist(object, 45)
        
        hcanvas.click_on_UI_element(object)
        
                        
if __name__=='__main__' :
    unittest.main()
