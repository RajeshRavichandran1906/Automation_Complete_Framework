'''@author: Robert 


Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157555
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2229771'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area

import time,unittest,pyautogui,datetime
import keyboard as keys

class C2229771_TestClass(AS_BaseTestCase):
    
    def test_C2229771(self):
        
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
          
        '''Step 2.1. Click Report and draw the report container on the canvas.'''
          
        acanvas_obj.drag_drop_on_canvas('Components', 'Report', 50, 50, 350, 350)
        time.sleep(5)
        '''Step 3. Right click within the report container and select 'Reference existing procedure'''
        '''Step 3.1. Double click on GuidedReport.fex'''
        '''Step 3.2. Click OK button in New Parameters window'''
        hcanvas.use_existing_fex_on_canvas_component_by_context_menu('reference', 'HTML_Canvas', "GuidedReport.fex", 180, 180)
        win_control=automation.WindowControl(Name="New Parameters")
        hcanvas.wait_for_object_exist(win_control, 10)
        automation.ButtonControl(Name="OK").Click()
          
        '''verifying at design time'''
        css=automation.GroupControl(AutomationId="form1")
        hcanvas.verify_object_exist(css, True, 'Step 3. Verify form1 exists')
        css=automation.PaneControl(Name="WebFOCUS Report")
        hcanvas.verify_object_exist(css, True, 'Step 3. Verify report exists')
          
        '''Save the report'''
        hcanvas.refresh_tree(item)
        
        time.sleep(6)
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
                
        as_utilobj.save_as_UI_dialog("C2229771")
          
        '''Step 4. Click Run'''
        '''Step 4.1. Close the browser page'''
        '''Step 4.2. Close HTML page'''
        '''Step 4.3. Click Yes in App Studio prompt message'''
        '''Step 4.4. Type C2229771 for File name and click OK'''
          
          
           
        time.sleep(6)
        
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/HTML_Canvas", "C2229771.htm")
        time.sleep(6)
        
        hcanvas.wait_for_web_object_exist("#form1 #form1Submit", 1, 30, 1)
        
        for i in range(1,2):
            hcanvas.verify_web_object_visible("#report"+str(i), True, "Step 4. Verify Report"+str(i) +" visible")
        
        for i in range(1,2):
            hcanvas.verify_web_object_visible("#form"+str(i), True, "Step 4. Verify form"+str(i) +" visible")
        
        
        for i in range(1,2):
            hcanvas.verify_web_object_visible("#form" +str(i) +" #form"+str(i)+"Submit", True, "Step 4. Verify Form"+str(i) +" Submit visible")
            hcanvas.verify_web_object_visible("#form" +str(i) +" #form"+str(i)+"Reset", True, "Step 4. Verify Form"+str(i) +" Reset visible")
            hcanvas.verify_web_object_visible("#form" +str(i) +" #form"+str(i)+"Defer", True, "Step 4. Verify Form"+str(i) +" Defer visible")
            hcanvas.verify_web_object_visible("#form" +str(i) +" #form"+str(i)+"Schedule", True, "Step 4. Verify Form"+str(i) +" Schedule visible")
        
        hcanvas.verify_web_object_no_of_elements("#form1 [id^='label']", 3, "Step 4. Verify no of label elements")
        hcanvas.verify_web_object_no_of_elements("#form1 [id^='combobox']", 2, "Step 4. Verify no of combobox elements")
        hcanvas.verify_web_object_no_of_elements("#form1 [id^='customselect1']", 7, "Step 4. Verify no of customselect elements")
        
        hcanvas.click_on_web_element("#form1 #form1Submit")
        
        time.sleep(10)
        
        hcanvas.switch_to_web_frame("#report1")
        
#         hcanvas.create_web_table_data("html body table tbody tr", "C2229771_Ds01.xlsx")
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C2229771_Ds01.xlsx", 'Step 4.2 Verify Report1 in iframe')
        
        hcanvas.switch_to_default_content()
        
        '''verify runtime output color to blue'''
        
        hcanvas.close_browser_session()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
    
        
if __name__=='__main__' :
    unittest.main()

