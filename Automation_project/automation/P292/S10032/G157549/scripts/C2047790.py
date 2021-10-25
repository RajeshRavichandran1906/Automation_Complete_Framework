'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157549
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2047790'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
from common.lib import as_utility 
import uiautomation as automation
import time,unittest

class C2047790_TestClass(AS_BaseTestCase):
    
    def test_C2047790(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        tree_path="Domains->P292_S10032_G157549->API"
        item="IbComposer populateDynamicCtrl"
        run_item="IbComposer_populateDynamicCtrl.htm"
        as_utilobj.select_home_button()
        
        '''Step 1. Navigate to Domains P292_S10032_G157549'''
        
        hcanvas.open_html_canvas_document(tree_path, item) 
        
        button_control=automation.PaneControl(Name="HtmlPage").ButtonControl(AutomationId="button1")
 
        hcanvas.wait_for_object_exist(button_control, 30)
         
        '''Step 1.2. Right click on IbComposer_populateDynamicCtrl and click Run '''
        
        'Verify the Design Pane'
        pane_control=automation.PaneControl(Name="HtmlPage")
        hcanvas.verify_object_exist(pane_control, True, 'Step 1. Verify Pane exists')
        hcanvas.verify_total_no_of_child_objects(pane_control, 6, 'Step 1. Verify Total no of objects inside Pane')
        
        list_control=pane_control.ListControl(AutomationId="listbox1")
        hcanvas.verify_object_exist(list_control, True, 'Step 1. Verify Listbox exists')
        
        button_control=pane_control.ButtonControl(Name="Populate Listbox")
        hcanvas.verify_object_exist(button_control, True, 'Step 1. Verify button exists')
        
        text_control=pane_control.TextControl(Name="Testing API IbComposer_populateDynamicCtrl")
        hcanvas.verify_object_exist(text_control, True, 'Step 1. Verify textbox exists')

        group_control=pane_control.GroupControl(AutomationId="Country")
        hcanvas.verify_object_exist(group_control, True, 'Step 1. Verify Country listbox exists')
                 
        '''run the item'''

        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/API", run_item)
        
        '''Verify the runtime options'''
        time.sleep(4)
        
        hcanvas.wait_for_web_object_exist("[id='button1']", 1, 30, 1)
        
        hcanvas.verify_web_object_no_of_elements("[id^='button']", 1, 'Step 1.3 Verify no of buttons')
        hcanvas.verify_web_object_no_of_elements("[id^='listbox']", 1, 'Step 1.3 Verify no of listbox')
        hcanvas.verify_web_object_no_of_elements("#Country table tr", 5, 'Step 1.3 Verify no of radiobutton items')
       
        '''Step 1.4. Clicking on the buttons sets values to the controls using the API'''
        '''Step 1.5. Multisource tree control is expanded and only top item is selected by default.'''
        '''Step 2. Click on 'Populate Listbox' button'''
        
        '''populate listbox button'''
        hcanvas.click_on_web_element("#button1")
        time.sleep(10)
        hcanvas.verify_web_element_attribute("#listbox1 > option", 'value', "ENGLAND", 'Step 2. Verify ENGLAND populated in the listbox')
        
        '''Step 3. Click JAPAN radio button and click on 'Populate Listbox' button'''
        
        hcanvas.click_on_web_element("#Country3")
        time.sleep(5)
        hcanvas.click_on_web_element("#button1")
        time.sleep(10)
        hcanvas.verify_web_element_attribute("#listbox1 > option", 'value', "JAPAN", 'Step 2. Verify JAPAN populated in the listbox')
                
        '''Step 4. Close HtmlPage browser page'''
        
        hcanvas.close_browser_session()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
        
if __name__=='__main__' :
    unittest.main()
