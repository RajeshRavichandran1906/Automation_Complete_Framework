'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157549
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2036812'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area

import time,unittest
import keyboard as keys



class C2229755_TestClass(AS_BaseTestCase):
    
    def test_C2229755(self):
        
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
        
        '''Step 1. Navigate to Domains P292_S10032_G157549, Expand API folder'''
        '''Step 1. 1. Navigate to the domain P292_S10032_G157549'''
        '''Step 1. 1.1. Expand the domain P292_S10032_G157549'''
        
        hcanvas.create_new_html_canvas_document(tree_path, item)
         
        '''Step 1. 1.3. Click on Properties panel and verified Theme property.'''
        '''Step 1. 1.4. Set "Dynamic Styling" property value to "Yes"'''
        as_panelsobj.expand_panel('Properties')
        time.sleep(5)
        hcanvas.click_change_item_properties_tab_using_sikuli('dynamic_styling.png', "150","5", "double", 'Yes')
               
        '''Step 2. Click on the phrase 'To import existing HTML content, click here before beginning your work'''
        '''Step 3. Double click on 'animation.htm' from Open File window'''
         
        time.sleep(5)
        automation.GroupControl(AutomationId='RLT_Greeting_element').Click()
        win_control=automation.WindowControl(Name="Open File")
 
        hcanvas.wait_for_object_exist(win_control, 30)
         
        text_control=automation.TextControl(Name="Animation.htm")
        text_control.DoubleClick()
         
        button_control=automation.ButtonControl(AutomationId='button2')
        hcanvas.wait_for_object_exist(button_control, 30)
         
        '''Step 4. Click on Report and a draw a container on canvas, click on Chart and a draw a container on canvas'''
         
         
        acanvas_obj.drag_drop_on_canvas('Components', 'Report', 220, 500, 520, 800)
        time.sleep(5)
        acanvas_obj.drag_drop_on_canvas('Components', 'Chart', 600, 500, 900, 800)
 
        '''Step 5. Right click within the Report container and select 'New Report'''
        '''Step 5.1. Click on "ibisamp" and double click on car.mas'''
        
        hcanvas.create_new_report_chart_from_canvas_component_by_context_menu('report', 'ibisamp', 'car.mas', 320,650) 
                
        '''Step 5.2. Double click on COUNTRY, CAR DEALER_COST to add'''
        '''Step 5.3. Close HtmlPage1_report1 and Save'''
        
        hcanvas.add_fields_in_report_painter(["COUNTRY","CAR","DEALER_COST"])
        
        hcanvas.refresh_tree_and_close_canvas_item(item)
         
        '''Step 6. Right click within the Chart container and select 'New Chart'''
        '''Step 6.1. Click on on "ibisamp" and double click on empdata.mas'''
        hcanvas.create_new_report_chart_from_canvas_component_by_context_menu('chart', 'ibisamp', 'empdata.mas', 650,650) 
                
         
        '''Step 6.2. Double click on DEPT, SALARY to add'''
        '''Step 6.3. Close HtmlPage1_chart1 and Save'''
        hcanvas.add_fields_in_ia(["DEPT","SALARY"]) 
        
        text_control=automation.PaneControl(Name="600K")
        hcanvas.wait_for_object_exist(text_control, 90)
        
        
        hcanvas.refresh_tree_and_close_canvas_item(item)
        
         
        '''    Step 7. Click Run    '''
        '''    Step 8. Close Output Browser Viewer and Close HTML page and Save    '''
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
         
        as_utilobj.save_as_UI_dialog("HtmlPage2")
         
        time.sleep(6)
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/HTML_Canvas", "HtmlPage2.htm")
        
        hcanvas.wait_for_web_object_exist("#report1", 1, 30, 1)
       
        '''Verifying the button'''
        hcanvas.verify_web_object_visible("#button2", True, 'Step 7. Verify button visible')
        
        '''verifying the report'''
        hcanvas.switch_to_web_frame("#report1")
        hcanvas.create_web_table_data("html body table tbody tr", "C2229755.xlsx")
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C2229755.xlsx", 'Step 7.1 Verify Report in main window')
        
        hcanvas.switch_to_default_content()
        time.sleep(4)
        
        '''verifying the chart'''
        hcanvas.switch_to_web_frame("#chart1")
        hcanvas.verify_color_web_object_chart("jschart_HOLD_0", 'riser!s0!g4!mbar!', 'bar_blue', 'Step 7. Verify Riser color')
        labels=['ACCOUNTING', 'ADMIN SER...', 'CONSULTING', 'CUSTOMER...', 'MARKETING', 'PERSONNEL', 'PROGRAMM...', 'SALES', '0', '100K', '200K', '300K', '400K', '500K', '600K']
        hcanvas.verify_labels_for_web_object_chart("jschart_HOLD_0", labels, 'Step 7. Verify data labels', custom_css=" text[class*='labels']")
        hcanvas.verify_no_of_risers_for_web_object_chart("#jschart_HOLD_0", 1, 9, 'Step 7. Verify no of risers')
        hcanvas.verify_xy_axis_title_for_web_object_chart("jschart_HOLD_0", 'DEPT', 'SALARY', 'Step 7. Verify x y axis title ')
        hcanvas.switch_to_default_content()
        time.sleep(4)
        '''Step 9. Close the HtmlPage browser page'''
        
        hcanvas.close_browser_session()
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
    
        
if __name__=='__main__' :
    unittest.main()
