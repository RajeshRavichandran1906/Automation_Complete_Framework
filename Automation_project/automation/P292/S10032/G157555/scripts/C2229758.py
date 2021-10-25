'''@author: Robert 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157555
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2229758'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
#from common.wftools.html_canvas import Html_Canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area

import time,unittest
import keyboard as keys

class C2229758_TestClass(AS_BaseTestCase):
    
    def test_C2229758(self):
        
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
        
          
        '''Step 2. Right click on HTML_Canvas folder->New-> HTML/Document, click Next, click Finish.'''
        hcanvas.create_new_html_canvas_document(tree_path, item)
        '''Step 2.1. Click on Report and a draw a container on canvas'''
         
        acanvas_obj.drag_drop_on_canvas('Components', 'Report', 50, 50, 350, 350)
        time.sleep(5)
        '''Step 2.2. Click on Chart and a draw a container on canvas'''
        acanvas_obj.drag_drop_on_canvas('Components', 'Chart', 400, 50, 700, 350)
         
        '''Step 3. Right click within the Report container and select 'Reference existing Procedure'''
        '''Step 3.1. Double click on CarParm.fex Click OK in 'New Parameters' window'''
  
          
        automation.PaneControl(Name="HtmlPage").RightClick(180,180)
           
        menu_item=automation.MenuItemControl(Name="Reference existing procedure")
        hcanvas.wait_for_object_exist(menu_item, 20)
        menu_item.MoveCursor()
        time.sleep(3)
        hcanvas.click_on_UI_element(menu_item)
           
        win_control=automation.WindowControl(Name="Open File")
   
        hcanvas.wait_for_object_exist(win_control, 30)
        automation.TextControl(Name="CarParm.fex").DoubleClick(40,10)
        time.sleep(4)
        win_control=automation.WindowControl(Name="New Parameters")
        hcanvas.wait_for_object_exist(win_control, 10)
        automation.ButtonControl(Name="OK").Click()
           
        '''Step 4. Right click within report container, click "Generate Chart"'''
         
        automation.PaneControl(Name="HtmlPage").RightClick(180,250)
           
        menu_item=automation.MenuItemControl(Name="Generate chart")
        hcanvas.wait_for_object_exist(menu_item, 20)
        menu_item.MoveCursor()
        time.sleep(3)
        hcanvas.click_on_UI_element(menu_item)
           
        '''Step 5. Right click within the Chart container and select 'Reference existing Procedure'''
        automation.PaneControl(Name="HtmlPage").RightClick(450,180)
           
        menu_item=automation.MenuItemControl(Name="Reference existing procedure")
        hcanvas.wait_for_object_exist(menu_item, 20)
        menu_item.MoveCursor()
        time.sleep(3)
        hcanvas.click_on_UI_element(menu_item)
        '''Step 5.1. Double click on SimpChart.fex'''
        win_control=automation.WindowControl(Name="Open File")
   
        hcanvas.wait_for_object_exist(win_control, 30)
        automation.TextControl(Name="SimpChart.fex").DoubleClick(40,10)
        time.sleep(4)
#         win_control=automation.WindowControl(Name="New Parameters")
#         hcanvas.wait_for_object_exist(win_control, 10)
#         automation.ButtonControl(Name="OK").Click()
         
        '''Step 6. Click on Report and a draw a container on canvas, click on Chart and a draw a container on canvas'''
         
        acanvas_obj.drag_drop_on_canvas('Components', 'Report', 750, 50, 1050, 350)
        time.sleep(5)
        '''Step 2.2. Click on Chart and a draw a container on canvas'''
        acanvas_obj.drag_drop_on_canvas('Components', 'Chart', 420, 450, 800, 800)
         
        '''Step 7. Right click within the Report container and select 'Reference existing procedure'''
        hcanvas.use_existing_fex_on_canvas_component_by_context_menu('reference', 'HTML_Canvas', 'CountryParm.fex', 850,180)
         
        '''Step 7.1. Double click on CountryParm.fex'''
        '''Step 7.2. Click OK in 'New Parameters' window'''
        
        win_control=automation.WindowControl(Name="New Parameters")
        hcanvas.wait_for_object_exist(win_control, 10)
        automation.ButtonControl(Name="OK").Click()
        time.sleep(10) 
        '''Step 8. Right click within the Chart container and select 'Reference existing procedure'''
        hcanvas.use_existing_fex_on_canvas_component_by_context_menu('reference', 'HTML_Canvas', 'ChartParm.fex', 590,630)
         
        '''Step 8.1. Double click on ChartParm.fex'''
        '''Step 8.2. Click OK in 'New Parameters' window'''
 
        
        time.sleep(4)
        win_control=automation.WindowControl(Name="New Parameters")
        hcanvas.wait_for_object_exist(win_control, 10)
        automation.ButtonControl(Name="OK").Click()
        time.sleep(6)
         
        '''Step 9. Click Run'''
        
        automation.TreeItemControl(Name=item).RightClick()
        time.sleep(3)
        automation.MenuItemControl(Name="Refresh Descendants").MoveCursor()
        time.sleep(3)
        automation.MenuItemControl(Name="Refresh Descendants").Click()
        time.sleep(6)
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
          
        as_utilobj.save_as_UI_dialog("C2229758")
          
        time.sleep(6)
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/HTML_Canvas", "C2229758.htm")
        
        hcanvas.wait_for_web_object_exist("#report1", 1, 30, 1)
       
        '''Verifying the report/chart components'''
        for i in range(1,4):
            hcanvas.verify_web_object_visible("#chart"+str(i), True, "Step 7. Verify Chart"+str(i) +" visible")
        
        for i in range(1,3):
            hcanvas.verify_web_object_visible("#report"+str(i), True, "Step 7. Verify Report"+str(i) +" visible")
        
        for i in range(1,4):
            hcanvas.verify_web_object_visible("#form" +str(i) +" #form"+str(i)+"Submit", True, "Step 7. Verify Form"+str(i) +" Submit visible")
            hcanvas.verify_web_object_visible("#form" +str(i) +" #form"+str(i)+"Reset", True, "Step 7. Verify Form"+str(i) +" Reset visible")
            hcanvas.verify_web_object_visible("#form" +str(i) +" #form"+str(i)+"Defer", True, "Step 7. Verify Form"+str(i) +" Defer visible")
            hcanvas.verify_web_object_visible("#form" +str(i) +" #form"+str(i)+"Schedule", True, "Step 7. Verify Form"+str(i) +" Schedule visible")
        
        '''Step 9.1. Click Submit button for CAR/ALFA ROMEO'''
        hcanvas.click_on_web_element("#form1 #form1Submit")
        time.sleep(6)
        '''Step 9.2. Click Submit button for COUNTRY/ENGLAND'''
        hcanvas.click_on_web_element("#form2 #form2Submit")
        time.sleep(6)
        '''Step 9.3. Click Submit button for YEAR/1982'''
        hcanvas.click_on_web_element("#form3 #form3Submit")
        time.sleep(6)
        '''verifying the contents of report1'''
        hcanvas.switch_to_web_frame("#report1")
        
        hcanvas.create_web_table_data("html body table tbody tr", "C2229758_Ds01.xlsx")
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C2229758_Ds01.xlsx", 'Step 9.1 Verify Report1 in main window')
        
        hcanvas.switch_to_default_content()
        '''verifying the contents of report2'''
        hcanvas.switch_to_web_frame("#report2")
        
        hcanvas.create_web_table_data("html body table tbody tr", "C2229758_Ds02.xlsx")
        
        hcanvas.verify_web_table_data("html body table tbody tr", "C2229758_Ds02.xlsx", 'Step 9.2 Verify Report2 in main window')
        
        hcanvas.switch_to_default_content()
        
        '''Verifying contents of chart2'''
        hcanvas.switch_to_web_frame("#chart2")
        hcanvas.verify_web_object_visible("body > img", True, "Step 9.1. Verify Chart image in chart2")
        hcanvas.switch_to_default_content()
        
        '''Verifying contents of chart2'''
        hcanvas.switch_to_web_frame("#chart3")
        hcanvas.verify_color_web_object_chart("jschart_HOLD_0", 'riser!s0!g0!mbar!', 'bar_blue', 'Step 9.3 Verify Riser color')
        labels=['1000', '1010', '2000', '4000', '5000', '6000', '6500', '6600', '6900', '7000', '0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M']
        hcanvas.verify_labels_for_web_object_chart("jschart_HOLD_0", labels, 'Step 9.3 Verify data labels', custom_css=" text[class*='labels']")
        hcanvas.verify_no_of_risers_for_web_object_chart("#jschart_HOLD_0", 1, 11, 'Step 9.3 Verify no of risers')
        hcanvas.verify_xy_axis_title_for_web_object_chart("jschart_HOLD_0", 'ACCOUNT', 'AMOUNT', 'Step 9.3 Verify x y axis title ')
        hcanvas.switch_to_default_content()
        time.sleep(4)
        
        '''verifying contents of chart1'''
        hcanvas.switch_to_web_frame("#chart1")
        hcanvas.verify_color_web_object_chart("jschart_HOLD_0", 'riser!s2!g0!mwedge!', 'violet', 'Step 9.1 Verify Pie riser color')
        labels=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        hcanvas.verify_labels_for_web_object_chart("jschart_HOLD_0", labels, 'Step 9.3 Verify legend Pie labels', custom_css="[class*='legend-labels']")
        hcanvas.verify_no_of_risers_for_web_object_chart("#jschart_HOLD_0", 1, 5, 'Step 9.3 Verify no Pie of risers')
        hcanvas.verify_web_object_text_visible("#jschart_HOLD_0 [class*='pieLabel!g0!mpieLabel!']", 'DEALER_COST', 'Step 9. Verify Pie Chart Label')
        
        hcanvas.switch_to_default_content()
        time.sleep(4)
        
        '''Step 10. Close Output browser and close HTML page and save'''
        '''Step 9. Close the HtmlPage browser page'''
        
        hcanvas.close_browser_session()
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        
        as_utilobj.close_canvas_item()
    
        
if __name__=='__main__' :
    unittest.main()
