'''@author: Robert 
Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157555
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2229783'''

from common.lib.as_basetestcase import AS_BaseTestCase  
from common.wftools import html_canvas
from common.lib import as_utility 
import uiautomation as automation
from common.lib.utillity import UtillityMethods
from common.pages import as_panels, as_ribbon, as_html_canvas_area
import time,unittest,pyautogui,datetime
import keyboard as keys
 
class C2229783_TestClass(AS_BaseTestCase):
     
    def test_C2229783(self):
         
        '''Create instance of object '''
         
        hcanvas=html_canvas.Html_Canvas(self.driver)
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        tree_path="Domains->P292_S10032_G157549"
        item="HTML_Canvas"
        as_utilobj.select_home_button()
        browser = UtillityMethods.parseinitfile(self,'browser')
        acanvas_obj=as_html_canvas_area.AS_Html_Canvas(self.driver)
         
        '''Step 1. Navigate to the domain P292_S10032_G157549'''
        '''Step 2. Right click on HTML_Canvas folder->New-> HTML/Document, click Next, click Finish.'''
        '''Step 1.1. Expand the domain P292_S10032_G157549''' 
        hcanvas.create_new_html_canvas_document(tree_path, item)
                 
        '''Step 3.1. Click on Report component and draw a container on canvas'''
        '''Step 3.2. Right click on report container and select "Reference existing procedure"'''
                        
        acanvas_obj.drag_drop_on_canvas('Components', 'Report', 50, 50, 350, 350)
        time.sleep(5)
        '''Step 3. Click Report and draw a container in the canvas.'''
        '''Step '3.1. Right click within the report container and select "Import existing report"'''
        '''Step 3.3. Double click on Autodrill.fex'''
        hcanvas.use_existing_fex_on_canvas_component_by_context_menu('reference', 'HTML_Canvas', 'Autodrill.fex', 180, 180)
        automation.PaneControl(Name="HtmlPage").RightClick(180,180)
        time.sleep(4)
             
        '''Step 4. Click on Chart component and draw on canvas .'''
        '''Step 4.1. Right click the chart and select "Reference existing procedure" and Double click on clrpt914.fex'''
        acanvas_obj.drag_drop_on_canvas('Components', 'Chart', 400, 50, 700, 350)
        time.sleep(5)
        hcanvas.use_existing_fex_on_canvas_component_by_context_menu('reference', 'HTML_Canvas', 'clrpt914.fex', 500, 180) 
        time.sleep(4)
             
        '''Step 5. Click on Chart and draw on canvas'''
        '''Step 5.1. Right click within Chart and select "Reference existing procedure'''
        '''Step 5.2. Double click on "AutodrillChart"'''
        acanvas_obj.drag_drop_on_canvas('Components', 'Chart', 50, 400, 750, 700)
        time.sleep(5)
        hcanvas.use_existing_fex_on_canvas_component_by_context_menu('reference', 'HTML_Canvas', 'AutoDrillChart.fex', 180, 600)
            
        '''Save the report'''
        hcanvas.refresh_tree(item)
        time.sleep(6)
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
        as_utilobj.save_as_UI_dialog("C2229783")
         
        '''Step 6. Click Run'''
        time.sleep(6)
        hcanvas.run_canvas_item_in_browser("P292_S10032_G157549/HTML_Canvas", "C2229783.htm")
        time.sleep(6)
        hcanvas.wait_for_web_object_exist("#jschart_HOLD_0 [class*='riser!s0!g2!mbar!']", 1, 40, 1)
        
        '''Verifying the report in frame1'''
        hcanvas.switch_to_web_frame("#report1")
        hcanvas.switch_to_web_frame("body > iframe") 
#         hcanvas.create_web_table_data("html body table tbody tr", "C2229783_Ds01.xlsx")
        hcanvas.verify_web_table_data("html body table tbody tr", "C2229783_Ds01.xlsx", 'Step 6.1 Verify Report1 in iframe')
        hcanvas.switch_to_default_content()
        '''Verifying the chart in frame2'''
          
        hcanvas.switch_to_web_frame("#chart1")
        hcanvas.switch_to_web_frame("body > iframe")
        hcanvas.verify_color_web_object_chart("jschart_HOLD_0", 'riser!s0!g0!mbar!', 'bar_blue', 'Step 6.2a. Verify Riser color')
        labels=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY', '0', '10K', '20K', '30K', '40K', '50K', '60K']
        hcanvas.verify_labels_for_web_object_chart("jschart_HOLD_0", labels, 'Step 6.2b Verify data labels', custom_css=" text[class*='labels']")
        hcanvas.verify_no_of_risers_for_web_object_chart("#jschart_HOLD_0", 1, 6, 'Step 6.2c. Verify no of risers')
        hcanvas.verify_xy_axis_title_for_web_object_chart("jschart_HOLD_0", 'COUNTRY', 'DEALER_COST', 'Step 6.2d. Verify x y axis title ')
        hcanvas.switch_to_default_content()
        time.sleep(4)
          
        '''Verifying the chart in frame3'''
          
        hcanvas.switch_to_web_frame("#chart2")
        hcanvas.switch_to_web_frame("body > iframe")
        hcanvas.verify_color_web_object_chart("jschart_HOLD_0", 'riser!s0!g2!mbar!', 'bar_blue', 'Step 6.3a. Verify Riser color')
        labels=['100 LS 2...', '2000 4 DO...', '2000 GT V...', '2000 SPID...', '2002 2 DOOR', '2002 2 DO...', '3.0 SI 4 D...', '3.0 SI 4 D...', '504 4 DOOR', '530I 4 DOOR', '530I 4 DO...', 'B210 2 DO...', 'COROLLA...', 'DORA 2 D...', 'INTERCEP...', 'TR7', 'V12XKE A...', 'XJ12L AUTO', '0', '1', '2', '3', '4', '5', '6']
        hcanvas.verify_labels_for_web_object_chart("jschart_HOLD_0", labels, 'Step 6.3b Verify data labels', custom_css=" text[class*='labels']")
        hcanvas.verify_no_of_risers_for_web_object_chart("#jschart_HOLD_0", 1, 19, 'Step 6.3c. Verify no of risers')
        hcanvas.verify_xy_axis_title_for_web_object_chart("jschart_HOLD_0", 'MODEL', 'SEATS', 'Step 6.3d. Verify x y axis title ')
        hcanvas.switch_to_default_content()
        time.sleep(4)
          
        '''Step 7. For report, click on "ALFA ROMEO" and click "Drill down to MODEL"'''
        hcanvas.switch_to_web_frame("#report1")
        hcanvas.switch_to_web_frame("body > iframe")
        hcanvas.select_report_autolink_tooltip_value("body table", 6, 2, "Drill down to MODEL")
         
        '''Step 8. First chart, hover on the first bar graph (ENGLAND) and click "Drill down to CAR"'''
        
        hcanvas.switch_to_default_content()
        time.sleep(5)
        c_obj=hcanvas.get_element_obj("#chart1", 'start')
        hcanvas.switch_to_web_frame("#chart1")
        hcanvas.switch_to_web_frame("body > iframe")
        
        hcanvas.click_elem("rect[class*='riser!s0!g0!mbar!']", x_offset=c_obj['x']+5, y_offset=c_obj['y']-99)
        time.sleep(1)
        if browser.lower()=="firefox" or browser.lower()=="ie":
            hcanvas.click_on_web_element_default("#jschart_HOLD_0_tdgchart-tooltip div ul td[class*='ooltip-name']")
            hcanvas.click_on_web_element_default("#jschart_HOLD_0_tdgchart-tooltip > div > ul > li[class*='ooltip-hover']")
        else:
            hcanvas.double_click_web_element_default("#jschart_HOLD_0_tdgchart-tooltip > div > ul > li[class*='tooltip-hover']")
       
        '''Step 9. Second chat, hover on Model 504 4 Door bar and click on "Drill up to CAR"'''
        hcanvas.switch_to_default_content()
        c_obj=hcanvas.get_element_obj("#chart2", 'start')
        hcanvas.switch_to_web_frame("#chart2")
        hcanvas.switch_to_web_frame("body > iframe")
        hcanvas.click_elem("rect[class*='riser!s0!g8!mbar!']", x_offset=c_obj['x'], y_offset=c_obj['y']-99)
        time.sleep(1)
        if browser.lower()=="firefox" or browser.lower()=="ie":
            hcanvas.click_on_web_element_default("#jschart_HOLD_0_tdgchart-tooltip div ul td[class*='ooltip-name']")
            hcanvas.click_on_web_element_default("#jschart_HOLD_0_tdgchart-tooltip > div > ul > li[class*='ooltip-hover']")
        else:
            hcanvas.double_click_web_element_default("#jschart_HOLD_0_tdgchart-tooltip > div > ul > li[class*='tooltip-hover']")
        time.sleep(4)
        
        hcanvas.wait_for_web_object_exist("[class*='riser!s0']", 15, 30, 1)
        
        '''verifying after drilldown'''
        hcanvas.switch_to_default_content()
        hcanvas.switch_to_web_frame("#chart1")
        hcanvas.switch_to_web_frame("body > iframe")
        hcanvas.verify_color_web_object_chart("jschart_HOLD_0", 'riser!s0!g0!mbar!', 'bar_blue', 'Step 9.2a. Verify Riser color')
        labels=['JAGUAR', 'JENSEN', 'TRIUMPH', '0', '4K', '8K', '12K', '16K', '20K']
        hcanvas.verify_labels_for_web_object_chart("jschart_HOLD_0", labels, 'Step 9.2b Verify data labels', custom_css=" text[class*='labels']")
        hcanvas.verify_no_of_risers_for_web_object_chart("#jschart_HOLD_0", 1, 4, 'Step 9.2c. Verify no of risers')
        hcanvas.verify_xy_axis_title_for_web_object_chart("jschart_HOLD_0", 'CAR', 'DEALER_COST', 'Step 9.2d. Verify x y axis title ')
        hcanvas.switch_to_default_content()
        time.sleep(4)
         
        '''Verifying the chart in frame3'''
         
        hcanvas.switch_to_web_frame("#chart2")
        hcanvas.switch_to_web_frame("body > iframe")
        hcanvas.verify_color_web_object_chart("jschart_HOLD_0", 'riser!s0!g2!mbar!', 'bar_blue', 'Step 9.3a. Verify Riser color')
        labels=['ALFA ROM...', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH', '0', '5', '10', '15', '20', '25', '30', '35']
        lables_cr=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH', '0', '5', '10', '15', '20', '25', '30', '35']
        hcanvas.verify_labels_for_web_object_chart("jschart_HOLD_0", lables_cr, 'Step 9.3b Verify data labels', custom_css=" text[class*='labels']")
        hcanvas.verify_no_of_risers_for_web_object_chart("#jschart_HOLD_0", 1, 11, 'Step 9.4c. Verify no of risers')
        hcanvas.verify_xy_axis_title_for_web_object_chart("jschart_HOLD_0", 'CAR', 'SEATS', 'Step 9.3d. Verify x y axis title ')
        hcanvas.switch_to_default_content()
        time.sleep(4)
                
        '''Step 10. Close the browser page, close and save the HTML page'''
        
        hcanvas.close_browser_session()
        time.sleep(10)
        as_utilobj.maximize_setfocus_ui_window("App")
        as_utilobj.close_canvas_item()
    
        
if __name__=='__main__' :
    unittest.main()

