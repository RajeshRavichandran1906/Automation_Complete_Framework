'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157549
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2231639'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area

import time,unittest
import keyboard as keys



class C2231639_TestClass(AS_BaseTestCase):
    
    def test_C2231639(self):
        
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
        hcanvas.create_new_html_canvas_document(tree_path, item)
         
        '''Step 3. Requests & Data Sources panel, External Request->WebFOCUS Procedure and double click on Populate.fex'''
        
        as_panelsobj.expand_panel('Requests & Data Sources')
        time.sleep(5)
        menu_path="External Request->WebFOCUS Procedure..."
        hcanvas.select_new_item_from_requests_datasource_menu(menu_path)
        time.sleep(5)
        as_utilobj.select_file_in_dialogs("OK",tree_path="HTML_Canvas",select_file="Populate.fex")
        #as_utilobj.select_UI_tree_view_item('HTML_Canvas', 'Populate.fex', 'OK')
               
        
        '''Step 4. Click on Controls tab, click on Drop Down and draw on canvas; Settings panel, select "Dynamic" radio button, Click on ellipsis for Explicit and double click on "REGION"'''
        
        acanvas_obj.drag_drop_on_canvas('Controls', 'Drop Down', 50, 50, 250, 150)
        time.sleep(6)
        cb1=automation.ComboBoxControl(AutomationId="combobox1")
        hcanvas.verify_object_exist(cb1, True, 'Step 4. Verify Combobox is displayed in design time.')
        as_panelsobj.expand_panel('Settings')
        
        radio=automation.RadioButtonControl(Name="Dynamic")
        radio.MoveCursor()
        radio.Click()
        
        radio=automation.RadioButtonControl(Name="Explicit (Requests panel)")
        radio.MoveCursor()
        radio.Click() 
        
        as_utilobj.settings_pane_select_value_from_list('REGION')   
        time.sleep(10)
        
        '''Step 4.1. Request is automatically populate by "Populate".fex'''
        
        curr_val=automation.ComboBoxControl(AutomationId="combobox1").CurrentValue()
        
        as_utilobj.asequal(curr_val,"Northeast", 'Step 4.1. Verify value automatically populated at design time.')
        
        '''Step 5. Click Run'''    
        hcanvas.refresh_tree_and_close_canvas_item("Domains")
        
        time.sleep(20)
        
        as_utilobj.save_as_UI_dialog("C2231639")
         
        time.sleep(6)
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/HTML_Canvas", "C2231639.htm")
        
        hcanvas.wait_for_web_object_exist("#combobox1", 1, 30, 1)
       
        '''Verifying the combobox'''
        hcanvas.verify_web_object_visible("#combobox1", True, 'Step 5. Verify combobox visible')
        
        
        hcanvas.verify_web_object_no_of_elements("#combobox1 option", 12, 'Step 5. Verify no of combobox elements')
        
        ele_list=['Midwest','Midwest','Midwest','Northeast','Northeast','Northeast','Southeast','Southeast','Southeast','West','West','West']
        val=0
        for i in ele_list:
            val+=1
            hcanvas.verify_web_object_text_visible("#combobox1 option:nth-child("+str(val)+")", i, 'Step 5. Verify the combobox contents')
        
        
        hcanvas.close_browser_session()
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
#         as_utilobj.close_canvas_item()
    
        
if __name__=='__main__' :
    unittest.main()
