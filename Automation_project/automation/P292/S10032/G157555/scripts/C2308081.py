'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157549
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2308081'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area

import time,unittest
import keyboard as keys



class C2308081_TestClass(AS_BaseTestCase):
    
    def test_C2308081(self):
        
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
        
        '''Step 1. Navigate to the domain P292_S10032_G157549'''
        '''Step 1.1 Expand the domain P292_S10032_G157549'''
        '''Step 2. Right click on HTML_Canvas folder-> New-> HTML/Document, click Next, click Finish'''
        
        '''Step 2.1. Click Next'''
        '''Step 2.2. Select 1-2 Template'''
        '''Step 2.3. Check "Run requests on load" and "Add page Header"'''
        '''Step 2.4. Click Finish'''
        
        hcanvas.create_new_html_canvas_document_options(tree_path, item, template="1-2", run_requests_onload='yes', add_page_header='yes')
         
        '''Step 3. Click on Image and draw on canvas above Output Widgets Container'''
        
        
        acanvas_obj.drag_drop_on_canvas('Components', 'Image', 50, 20, 250, 120)
        
        '''Step 3.1. Double click on cactus1.gif'''
        as_utilobj.select_UI_tree_view_item('HTML_Canvas', 'cactus1.gif', 'OK')
        object=automation.ImageControl(AutomationId="image1")
        hcanvas.wait_for_object_exist(object, 30)
        time.sleep(5)
        automation.PaneControl(Name="HtmlPage").Click(250,80)
        time.sleep(15)
        as_utilobj.verify_picture_using_sikuli('C2308081_canvas.png', 'Step 3. Verify template with image')
               
        '''Step 4. Click on Save and type AS4994 as File name, click OK'''
        '''Step 5. Close AS4994'''
           
        hcanvas.refresh_tree(item)
       
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
         
        as_utilobj.save_as_UI_dialog("AS4994")
         
        time.sleep(3)
        
        hcanvas.refresh_tree_and_close_canvas_item(item)
        '''Step 6. Double click on AS4994'''
        '''Step 7. Close AS4994'''
        time.sleep(3)
        hcanvas.open_html_canvas_document('HTML_Canvas', 'AS4994')
        
        object=automation.ImageControl(AutomationId="image1")
        hcanvas.wait_for_object_exist(object, 30)
        time.sleep(10)
        as_utilobj.verify_picture_using_sikuli('C2308081_canvas.png', 'Step 6. Verify template with image')
        
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
    
        
if __name__=='__main__' :
    unittest.main()
