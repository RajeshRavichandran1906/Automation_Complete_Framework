'''@author: Robert 


Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157555
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2229769'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area

import time,unittest,pyautogui,datetime
import keyboard as keys

class C2229769_TestClass(AS_BaseTestCase):
    
    def test_C2229769(self):
        
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
        '''Step 2. Right click on HTML_Canvas folder-> New-> HTML/Document, click Next, click Finish; click on 'Button' and draw on canvas'''  
        
        hcanvas.create_new_html_canvas_document(tree_path, item)
        '''Drawing a button on the canvas'''
   
         
         
        acanvas_obj.drag_drop_on_canvas('Components', 'Button', 100, 100, 300, 300)
        time.sleep(5)
         
        '''Step 3. Click on Settings panel, click on JavaScript icon and double click on ExternalJS.js'''
         
        as_utilobj.expand_doc_pane('Settings')
        as_utilobj.add_css_url_by_button("js", "ExternslJavaScriptFile.js")
        '''Step 4. Click on Task & Animations panel, create a new Task; check 'button1' in Trigger Identifier; select 'JavaScript call' from Requests/Actions drop down and type mytest() in Function name'''
        as_utilobj.expand_doc_pane('Tasks & Animations')
        hcanvas.select_new_item_from_requests_datasource_menu("New")
         
        chkbox=automation.CheckBoxControl(Name='button1')
        chkbox.Toggle()
        time.sleep(5)
        hcanvas.select_dropdown_item_from_run_requests_menu('JavaScript call')
        time.sleep(8) 
        automation.EditControl(AutomationId='1001').Click()
        time.sleep(4) 
        automation.SendKeys("mytest()", waitTime=4)
         
        '''Step 5. Settings panel, click on CSS... icon and double click on 'ExternalCSS.css' from the 'Open File' dialog window'''
        as_utilobj.expand_doc_pane('Settings')
        as_utilobj.add_css_url_by_button("css", "externalCSS.css")
         
        '''save the report'''
        hcanvas.refresh_tree(item)
        time.sleep(6)
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
              
        as_utilobj.save_as_UI_dialog("C2229769")
              
        time.sleep(6)
        
        '''Step 6. Click Run and click the 'button' and click OK from message box'''
        
        
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/HTML_Canvas", "C2229769.htm")
        hcanvas.wait_for_web_object_exist("#button1", 1, 30, 1)
        
        hcanvas.click_on_web_element("#button1")
        
        val_text=automation.TextControl(Name=" A test for External Java Script")
        if browser=="Firefox":
            val_text=automation.EditControl(Name=" A test for External Java Script")
        else:
            val_text=automation.TextControl(Name=" A test for External Java Script")
            
        hcanvas.verify_object_exist(val_text, True, 'Step 6. Verify  A test for External Java Script msgbox displayed')
        
        btn_ok=automation.ButtonControl(Name="OK")
        hcanvas.click_on_UI_element(btn_ok)
        time.sleep(10)
        
        hcanvas.close_browser_session()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
    
        
if __name__=='__main__' :
    unittest.main()
