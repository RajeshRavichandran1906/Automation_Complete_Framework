'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/11397&group_by=cases:section_id&group_order=asc&group_id=439407
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6467909'''

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


class C6467909_TestClass(AS_BaseTestCase):
    
    def test_C6467909(self):
        
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
        
        '''Step 1. Navigate to P292_S10032_G156801, Right click-> New -> Procedure.'''
        
        hcanvas.select_UI_item_using_right_click_menu(tree_path, folder_item, "New->Procedure")   
         
        '''Step 2. Click on procedure view , Right click Comment ,Select New and select Report from Context menu'''
        automation.PaneControl(AutomationId="1").Click()
        automation.TreeItemControl(Name="Comment").RightClick()
        time.sleep(3)
        automation.MenuItemControl(Name="New ...").Click()
        time.sleep(2)
        automation.MenuItemControl(Name="Report").Click()
         
        '''Step 3. Select ibisamp/car.mas master file'''
        '''Step 3.1. Click Ok.'''
         
        win_control=automation.WindowControl(Name="Select Data Source")
        as_utilobj.wait_for_UI_object(win_control,30)
        time.sleep(8)
        automation.WindowControl(Name="Select Data Source").TreeItemControl(Name="Domains").Click()
        time.sleep(3)
        as_utilobj.select_UI_tree_view_item("ibisamp", "car.mas", 'OK')
 
         
        '''Step 4. In Object Inspector double click on fields COUNTRY, CAR,DEALER_COST'''
   
        hcanvas.add_fields_in_report_painter(['COUNTRY','CAR','DEALER_COST'])
           
        '''Step 5. In Report tab click on Change Theme'''
        automation.TabItemControl(Name='Report').Click(waitTime=1)
        time.sleep(3)
        automation.ButtonControl(Name="Change Theme").Click(waitTime=1)
         
        '''Step 6. Select ENBlue_Dark.sty from Legacy Style Templates files->click OKVerify theme on canvas'''
        win_control=automation.WindowControl(Name="Open File")
        as_utilobj.wait_for_UI_object(win_control,30)
        time.sleep(8)
        automation.WindowControl(Name="Open File").TreeItemControl(Name="Domains").Click()
        time.sleep(3)
        as_utilobj.select_UI_tree_view_item("Legacy Style Templates", "ENBlue_Dark.sty", 'OK')
        as_utilobj.verify_picture_using_sikuli('c6467909_step06.png', 'Step 6 Verify report presentation on canvas')
         
         
        '''Step 7. Click Source at bottom of Report tab'''
        '''Step 7.1. Verify correct syntax'''
         
        automation.TabItemControl(Name="Source").Click()
        object=automation.PaneControl(Name="Online")
        hcanvas.wait_for_object_exist(object, 30)
        automation.PaneControl(Name="Online").Click(30,100)
        time.sleep(3)
        automation.SendKeys('{Ctrl}a')
        time.sleep(3)
        automation.SendKeys('{Ctrl}c')
        time.sleep(3)
         
        fex_string="TABLEFILECARSUMCAR.BODY.DEALER_COSTBYCAR.ORIGIN.COUNTRYBYCAR.COMP.CARONTABLESETPAGE-NUMNOLEADONTABLESETASNAMESONONTABLENOTOTALONTABLEPCHOLDFORMATHTMLONTABLESETHTMLEMBEDIMGONONTABLESETHTMLCSSONONTABLESETSTYLE*INCLUDE=IBFS:/FILE/IBI_HTML_DIR/javaassist/intl/EN/combine_templates/ENBlue_Dark.sty,$ENDSTYLEEND"
         
        cache_string=automation.GetClipboardText()
        cache_string=cache_string.strip().replace(' ','').replace('\n','').replace('\r','')
         
        as_utilobj.asequal(fex_string,cache_string,'Step 7. Verify correct fex code is generated')
         
         
        '''Step 8. Execute report requestVerify correct output'''
        '''Step 9. Close Report Canvas and save as ATEST.fex'''
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
        time.sleep(12)
        object_css="body > table > tbody > tr:nth-child(6) > td:nth-child(1)"
        hcanvas.wait_for_web_object_exist(object_css, 1, 65, 1)
        time.sleep(10)
#         hcanvas.create_web_table_data("html body table tbody tr", "C6467909_Ds01.xlsx")
        
        'color for italy cell'
        hcanvas.verify_web_element_css("body > table > tbody > tr:nth-child(6) > td:nth-child(1)", "background-color", "rgba(54, 96, 146, 1)", 'Step 8. Verify report background color1')
        'color for maserati cell' 
        hcanvas.verify_web_element_css("body > table > tbody > tr:nth-child(7) > td:nth-child(2)", "background-color", "rgba(79, 129, 189, 1)", 'Step 8. Verify report background color2')
        'color for country cell'
        hcanvas.verify_web_element_css("body > table > tbody > tr:nth-child(1) > td:nth-child(1)", "background-color", "rgba(0, 0, 0, 1)", 'Step 8. Verify report background color3')
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467909_Ds01.xlsx", 'Step 8.1 Verify Correct report output')
        
        hcanvas.close_browser_session()
        as_utilobj.select_home_button()
        hcanvas.refresh_tree_and_close_canvas_item(folder_item)
         
        
        '''Step 10. Right click on ATEST-> OpenVerify theme on canvas'''
        hcanvas.open_html_canvas_document(folder_item, fex_item)
        
        object=automation.TreeItemControl(Name="COUNTRY")
        hcanvas.wait_for_object_exist(object, 45)
        
        as_utilobj.verify_picture_using_sikuli('c6467909_step06.png', 'Step 10 Verify report presentation on canvas')
        
        '''Step 11. Execute report requestVerify correct output'''
        hcanvas.run_canvas_item_in_browser(folder_item, "ATEST.fex")
        time.sleep(6)
        object_css="body > table > tbody > tr:nth-child(6) > td:nth-child(1)"
        hcanvas.wait_for_web_object_exist(object_css, 1, 65, 1)
        time.sleep(10)
        #hcanvas.create_web_table_data("html body table tbody tr", "C6467909_Ds01.xlsx")
        'color for italy cell'
        hcanvas.verify_web_element_css("body > table > tbody > tr:nth-child(6) > td:nth-child(1)", "background-color", "rgba(54, 96, 146, 1)", 'Step 11. Verify report background color1')
        'color for maserati cell' 
        hcanvas.verify_web_element_css("body > table > tbody > tr:nth-child(7) > td:nth-child(2)", "background-color", "rgba(79, 129, 189, 1)", 'Step 11. Verify report background color2')
        'color for country cell'
        hcanvas.verify_web_element_css("body > table > tbody > tr:nth-child(1) > td:nth-child(1)", "background-color", "rgba(0, 0, 0, 1)", 'Step 11. Verify report background color3')
         
        hcanvas.verify_web_table_data("html body table tbody tr", "C6467909_Ds01.xlsx", 'Step 11.1 Verify Correct report output')
        
        hcanvas.close_browser_session()
        as_utilobj.select_home_button()
        '''Step 12. Close report output, close Report Canvas'''
        hcanvas.refresh_tree_and_close_canvas_item(folder_item)
        time.sleep(10)
        '''Step 13. Delete ATEST.fex'''
        hcanvas.select_UI_item_using_right_click_menu(folder_item, fex_item, "Delete")
        
        object=automation.ButtonControl(Name="Yes")
        hcanvas.wait_for_object_exist(object, 45)
        
        hcanvas.click_on_UI_element(object)
        
        
                        
if __name__=='__main__' :
    unittest.main()
