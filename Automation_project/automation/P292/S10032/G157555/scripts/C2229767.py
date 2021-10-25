'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157555
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2229767'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area

import time,unittest,pyautogui,datetime
import keyboard as keys

class C2229767_TestClass(AS_BaseTestCase):
    
    def test_C2229767(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        as_panelsobj=as_panels.AS_Panels(self.driver)
        as_ribbonobj=as_ribbon.AS_Ribbon(self.driver)
        tree_path="Domains->P292_S10032_G157549"
        item="HTML_Canvas"
        as_utilobj.select_home_button()
        browser = UtillityMethods.parseinitfile(self,'browser')
        acanvas_obj=as_html_canvas_area.AS_Html_Canvas(self.driver)
        email_id="report_caster@ibi.com"
        
        '''Step 1. Navigate to the domain P292_S10032_G157549'''
        '''Step 1.1. Expand the domain P292_S10032_G157549'''
        '''Step 2. Right click on HTML_Canvas folder->New-> HTML/Document, click Next, click Finish.''' 
        hcanvas.create_new_html_canvas_document(tree_path, item)
          
          
        '''Step 3. Click on Report and draw a container on canvas'''
          
        acanvas_obj.drag_drop_on_canvas('Components', 'Report', 100, 100, 500, 500)
        time.sleep(5)
          
        '''Step 3.1. Right click within the report container and select 'Reference existing procedure'''
        '''Step 4. Double click on 'Filter_Type_ParameterSimple.fex' Click OK in New Parameters window'''
          
        hcanvas.use_existing_fex_on_canvas_component_by_context_menu("reference", "HTML_Canvas", "Filter_Type_ParameterSimple.fex", 280, 280)
        time.sleep(5)
        btn=automation.ButtonControl(Name="OK")
        if btn.Exists()==True:
            hcanvas.click_on_UI_element(btn)
            time.sleep(5) 
        '''save the report'''
        hcanvas.refresh_tree(item)
          
        time.sleep(6)
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
               
        as_utilobj.save_as_UI_dialog("C2229767")
               
        time.sleep(6)
        '''Step 5. Run the html page and type ACTION for CATEGORY'''
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/HTML_Canvas", "C2229767.htm")
        hcanvas.wait_for_web_object_exist("#form1 #form1Submit", 1, 30, 1)
        
        for i in range(1,2):
            hcanvas.verify_web_object_visible("#report"+str(i), True, "Step 5. Verify Report"+str(i) +" visible")
        for i in range(1,2):
            hcanvas.verify_web_object_visible("#form" +str(i) +" #form"+str(i)+"Submit", True, "Step 5. Verify Form"+str(i) +" Submit visible")
            hcanvas.verify_web_object_visible("#form" +str(i) +" #form"+str(i)+"Reset", True, "Step 5. Verify Form"+str(i) +" Reset visible")
            hcanvas.verify_web_object_visible("#form" +str(i) +" #form"+str(i)+"Defer", True, "Step 5. Verify Form"+str(i) +" Defer visible")
            hcanvas.verify_web_object_visible("#form" +str(i) +" #form"+str(i)+"Schedule", True, "Step 5. Verify Form"+str(i) +" Schedule visible")
        
        
        hcanvas.click_on_web_element("#form1 #edit1")
        time.sleep(3)
        pyautogui.typewrite("ACTION")
        
        '''Step 5.1. Click the Submit button'''
        hcanvas.click_on_web_element("#form1 #form1Submit")
        time.sleep(6)
        '''Step 5.2. Report displays record for ACTION category'''
        hcanvas.switch_to_web_frame("#report1")
        
        hcanvas.create_web_table_data("html bod table tbody tr", "C2229767_Ds01.xlsx")
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C2229767_Ds01.xlsx", 'Step 5.2 Verify Report For ACTION')
        
        hcanvas.switch_to_default_content()
        '''Step 6. Click on the Schedule button'''
        hcanvas.click_on_web_element("#form1 #form1Schedule")
        time.sleep(6)
        
        '''Step 6.1. A new 'Distribution Method Selection' window opens'''
        hcanvas.switch_to_window(1)
        hcanvas.wait_for_web_object_exist("#ReportCasterDistribution div div[id^='BiLabel']:nth-child(2)", 1, 20, 1)
        hcanvas.verify_web_object_visible("#ReportCasterDistribution", True, 'Step 6. Verify Distribution Method Selection window is open')
        '''Step 7. Click on an Email method'''
        hcanvas.click_on_web_element_default("#ReportCasterDistribution div div[id^='BiLabel']:nth-child(2)")
        
        '''Step 7.1 ReportCaster's Schedule window opens'''
        hcanvas.wait_for_web_object_exist("#rcBiBasicScheduleEditor", 1, 50, 1)
        hcanvas.verify_web_object_visible("#rcBiBasicScheduleEditor", True, 'Step 7. Verify RC schedule window is open')
        
        '''Step 8. Click on the Distribution button and enter email id's in To/From and Reply Address fields'''
        
        hcanvas.click_on_web_element_default("#DistributeEmailPane_mailToTextField")
        time.sleep(3)
        pyautogui.hotkey('ctrl','a')
        time.sleep(2)
        pyautogui.hotkey('del')
        time.sleep(3)
        pyautogui.typewrite(email_id)
        
        hcanvas.click_on_web_element_default("#DistributeEmailPane_mailFromTextField")
        time.sleep(3)
        pyautogui.hotkey('ctrl','a')
        time.sleep(2)
        pyautogui.hotkey('del')
        time.sleep(3)
        pyautogui.typewrite(email_id)
        
        hcanvas.click_on_web_element_default("#DistributeEmailPane_mailReplyTextField")
        time.sleep(3)
        pyautogui.hotkey('ctrl','a')
        time.sleep(2)
        pyautogui.hotkey('del')
        time.sleep(3)
        pyautogui.typewrite(email_id)
        time.sleep(5)  
        hcanvas.switch_to_default_content()
        time.sleep(5)
        hcanvas.double_click_web_element_default("img[src*='app_save_close']")
        
        '''Step 8.1. Click on 'Save & Close' button'''
        '''Step 9. Close Browser page; close and Save the html page'''
        hcanvas.wait_for_web_object_exist("#IbfsOpenFileDialog7_cbFileName", 1, 30, 1)
        
        hcanvas.click_on_web_element_default("#IbfsOpenFileDialog7_btnOK")
        
        time.sleep(10)  
        hcanvas.switch_to_main_window()
        
        hcanvas.close_browser_session()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
    
        
if __name__=='__main__' :
    unittest.main()
