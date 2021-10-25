'''@author: Robert 


Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157555
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2229772'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area
import time,unittest


class C2229772_TestClass(AS_BaseTestCase):
    
    def test_C2229772(self):
        
        '''Create instance of object '''
        
        hcanvas=html_canvas.Html_Canvas(self.driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        tree_path="Domains->P292_S10032_G157549"
        item="HTML_Canvas"
        as_utilobj.select_home_button()
        acanvas_obj=as_html_canvas_area.AS_Html_Canvas(self.driver)
        
        '''Step 1. Navigate to the domain P292_S10032_G157549'''
        '''Step 1.1. Expand the domain P292_S10032_G157549'''
        '''Step 2. Right click on HTML_Canvas folder->New-> HTML/Document, click Next, click Finish.''' 
        hcanvas.create_new_html_canvas_document(tree_path, item)
           
        '''Step 2.1. Click Report and draw the report container on the canvas.'''
          
        acanvas_obj.drag_drop_on_canvas('Components', 'Report', 50, 50, 350, 350)
        time.sleep(5)
        '''Step 3. Right click within the report container and select 'Reference existing procedure'''
        automation.PaneControl(Name="HtmlPage").RightClick(180,180)
             
        menu_item=automation.MenuItemControl(Name="Reference existing procedure")
        hcanvas.wait_for_object_exist(menu_item, 20)
        menu_item.MoveCursor()
        time.sleep(3)
        hcanvas.click_on_UI_element(menu_item)
             
        win_control=automation.WindowControl(Name="Open File")
          
        '''Step 3.1. Double click on GuidedReport.fex'''
         
        hcanvas.wait_for_object_exist(win_control, 30)
        automation.TextControl(Name="MultipleMultiSelectOR.fex").DoubleClick(40,10)
        time.sleep(4)
        win_control=automation.WindowControl(Name="New Parameters")
        hcanvas.wait_for_object_exist(win_control, 10)
         
        '''Step 3.2. Check "Auto chain controls in above specified order"'''
        time.sleep(4)
        chkbox=automation.CheckBoxControl(Name="Auto chain controls in above specified order")
        chkbox.Toggle()
        time.sleep(4)
        '''Step 3.3. Click OK button in New Parameters window'''
        automation.ButtonControl(Name="OK").Click()
          
          
        '''verifying at design time'''
        css=automation.GroupControl(AutomationId="form1")
        hcanvas.verify_object_exist(css, True, 'Step 3. Verify form1 exists')
        css=automation.PaneControl(Name="WebFOCUS Report")
        hcanvas.verify_object_exist(css, True, 'Step 3. Verify report exists')
          
        '''Save the report'''
        hcanvas.refresh_tree_and_close_canvas_item("Domains")
        
        as_utilobj.save_as_UI_dialog("C2229772")
          
        '''Step 4. Click Run'''
         
        time.sleep(6)
        
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/HTML_Canvas", "C2229772.htm")
        time.sleep(6)
        
        
        '''Verifying the runtime components'''
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
        
        hcanvas.verify_web_object_no_of_elements("#form1 select[id^='listbox']", 3, "Step 4. Verify no of listbox elements")
        hcanvas.verify_web_object_no_of_elements("#form1 label[id^='label']", 3, "Step 4. Verify no of label elements")
        
        hcanvas.click_on_web_element("#listbox1 > option:nth-child(1)")
        time.sleep(3)
        automation.KeyDown(automation.Keys.VK_CONTROL)
        hcanvas.click_on_web_element("#listbox1 > option:nth-child(2)")
        time.sleep(3)
        automation.KeyDown(automation.Keys.VK_CONTROL)
        time.sleep(3)
        hcanvas.click_on_web_element("#listbox1 > option:nth-child(3)")
        time.sleep(3)
        automation.KeyUp(automation.Keys.VK_CONTROL)
        time.sleep(5)
        hcanvas.click_on_web_element("#listbox2 > option:nth-child(1)")
        time.sleep(5)
        hcanvas.click_on_web_element("#listbox2 > option:nth-child(2)")
        time.sleep(5)
        
        
        '''Step 5. Multiselect values; 2,626 and 2,886 for DEALER_COST and Select 3,319 from RETAIL_COST.'''
        '''Step 5.1. click the Submit button'''
        
        
        hcanvas.click_on_web_element("#form1 #form1Submit")
        
         
        time.sleep(10)
        
        hcanvas.switch_to_web_frame("#report1")
        
        hcanvas.create_web_table_data("html body table tbody tr", "C2229772_Ds01.xlsx")
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C2229772_Ds01.xlsx", 'Step 5.2 Verify Report1 in iframe')
        
        hcanvas.switch_to_default_content()
        
        hcanvas.close_browser_session()
        
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        
if __name__=='__main__' :
    unittest.main()

