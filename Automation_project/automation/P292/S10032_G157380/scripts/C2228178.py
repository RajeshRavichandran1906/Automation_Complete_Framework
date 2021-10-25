'''
Created on December 22, 2017

@author: PM14587
Testcase Name : Verify Chart with Multi Drill and Auto Drill is working properly (82xx)
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2228178
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea,visualization_ribbon,ia_ribbon,ia_resultarea,ia_run
from common.lib import utillity
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class C2228178_TestClass(BaseTestCase):

    def test_C2228178(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2228178'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbon=ia_ribbon.IA_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        
        def verify_chart_output(parent_id, yaxis_title, xaxis_labels, yaxis_labels, total_risers, riser_class, step_no):
            resultobj.verify_xaxis_title(parent_id, yaxis_title, 'Step '+step_no+'.1 : Verify X-Axis title')
            resultobj.verify_yaxis_title(parent_id, 'DEALER_COST', 'Step '+step_no+'.2 : Verify Y-Axis title')
            resultobj.verify_riser_chart_XY_labels(parent_id, xaxis_labels, yaxis_labels, 'Step '+step_no+'.3 :',20)
            resultobj.verify_number_of_riser(parent_id, 1, total_risers, 'Step '+step_no+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color(parent_id, riser_class, 'bar_blue', 'Step '+step_no+'.5 : Verify chart riser color')
            
        """
            Step 01 : Launch IA, New > Report with CAR.MAS.
        """
        utillobj.infoassist_api_login('Report','ibisamp/car','P292/S10032_chart_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#queryTreeWindow tr:nth-child(2) td", 1,30,string_value='Sum')
        time.sleep(3)
        
        """
            Step 02 : Double click "Country", "Sales"
        """
        metaobj.datatree_field_click('COUNTRY',2,1)
        resultobj.wait_for_property("#queryTreeWindow tr:nth-child(4) td", 1,10,string_value='COUNTRY')
        
        metaobj.datatree_field_click('SALES',2,1)
        resultobj.wait_for_property("#queryTreeWindow tr:nth-child(3) td", 1,10,string_value='SALES')
        time.sleep(2)
        
        """
            Step 02.1 : Verify preview output 
        """
        #iaresult.create_across_report_data_set('TableChart_1', 1, 2, 5, 2, Test_Case_ID+'_DataSet_01.xlsx')
        iaresult.verify_across_report_data_set('TableChart_1', 1, 2, 5, 2, Test_Case_ID+'_DataSet_01.xlsx', 'Step 02.1 : Verify preview output')
        
        """
            Step 03 : Click "IA" > "Save".
            Step 04 : Enter title= "Report003" > Click "Save".
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID+'_Report003')
        time.sleep(2)
        
        """
            Step 05 : Click "IA" > "Exit"
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 06 : Launch IA, New > Chart with CAROLAP.MAS.
        """ 
        utillobj.infoassist_api_login('Chart','ibisamp/carolap','P292/S10032_chart_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1 text[class='legend-labels!s0!']", 1,40,string_value='Series0')
        time.sleep(3) 
         
        """
            Step 07 : Double click "DEALER_COST".
        """
        metaobj.datatree_field_click('DEALER_COST',2,1)
        resultobj.wait_for_property("#TableChart_1 text[class='yaxis-title']", 1,13,string_value='DEALER_COST')
        
        """
            Step 08 : Expand COUNTRY Dimension > double click "COUNTRY".
        """
        metaobj.datatree_field_click('COUNTRY',2,1)
        resultobj.wait_for_property("#TableChart_1 text[class='xaxisOrdinal-title']", 1,13,string_value='COUNTRY')
        time.sleep(2)
        
        """
            Step 09 : Verify the following "Chart" in Livepreview
        """ 
        expected_xaxis_labels=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        verify_chart_output('TableChart_1', 'COUNTRY', expected_xaxis_labels, expected_yaxis_labels, 5, 'riser!s0!g2!mbar!', '09')
        
        """
            Step 10 : Select "Format" > "Auto Drill" button (from navigation group)
        """
        visul_ribbon.select_ribbon_item('Format', 'auto_drill')
        resultobj.wait_for_property("[id='FormatAutoDrill'][class*='button-checked']", 1,8)
        
        """
            Step 11 : Select "DEALER_COST" in Query pane
        """ 
        metaobj.querytree_field_click('DEALER_COST',1) 
        resultobj.wait_for_property("#FieldDrillDown div", 1, 8, string_value='Drill Down') 
         
        """
            Step 12 : Click "Links" > "Drill down" from "Field" tab.
        """
        visul_ribbon.select_ribbon_item('Field', 'drilldown')
        resultobj.wait_for_property("[id^='IABottomBar'] #ok", 1,10,string_value='OK')
         
        """
            Step 13 : Verify the "Drill Down - DEALER_COST" opens and "Report" is enabled by default in the dialog
        """
        actual_label=self.driver.find_element_by_css_selector("[id^='QbDialog'] div[class*='i-window-caption']>div[class='bi-label']").text.strip()
        utillobj.asequal(actual_label, 'Drill Down - DEALER_COST', 'Step 13.1 : Verify the "Drill Down - DEALER_COST" opens')
        
        """
            Step 14 : Click "Browse" > Select "Report003" > Open.
            Step 15 : Set "Description" = "Drilldown to Report".
            Step 16 : Click "Create a new drill down" icon
        """ 
        iaribbon.create_drilldown_report('report',browse_file_name=Test_Case_ID+'_Report003', set_description='Drilldown to Report',verify_drilldown_type=True,create_new_drilldown=True)
        time.sleep(2)
        
        """
            Step 17 : Select "Web Page" option and Type "http://www.ibi.com" in URL input box
            Step 18 : Set "Description" = "Information builders".
            Step 19 : Click "Create a new drill down" icon
        """
        element=self.driver.find_element_by_css_selector("[id^='QbDialog'] div[class*='i-window-caption']>div[class='bi-label']")
        utillobj.click_on_screen(element,'middle')
        time.sleep(2)
        iaribbon.create_drilldown_report('webpage',url_value='http://www.ibi.com', set_description='Information builders', create_new_drilldown=True)
        time.sleep(2)
        
        """
            Step 20 : Select "Web Page" option and Type "http://www.google.com" in URL input box
            Step 21 : Set "Description" = "Google".
            Step 22 : Click "OK"
        """ 
        iaribbon.create_drilldown_report('webpage',url_value='http://www.google.com', set_description='Google', click_ok=True)
        time.sleep(8) 
     
        """
            Step 23 : Click Run
        """ 
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=4)
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='contentDrill']")))
        resultobj.wait_for_property("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", 1,30,string_value='COUNTRY')
        time.sleep(2)
        
        """
            Step 23.1 : Verify chart output
        """
        expected_xaxis_labels=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        verify_chart_output('jschart_HOLD_0', 'COUNTRY', expected_xaxis_labels, expected_yaxis_labels, 5, 'riser!s0!g0!mbar!', '23')
       
        """
            Step 24 : Hover over on Chart riser "ENGLAND"
            Step 25 : Verify the Autodrill and Multidrill menus are displayed
        """
        expected_tooltip= ['COUNTRY:ENGLAND', 'DEALER_COST:37,853', 'Drill down to CAR', 'Drilldown to Report', 'Information builders', 'Google']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g0!mbar!',expected_tooltip, 'Step 25.1 : Verify the Autodrill and Multidrill menus are displayed')
         
        """
            Step 26 : Select "Drill Down to CAR" and Verify Chart
        """ 
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!', 'Drill down to CAR') 
        resultobj.wait_for_property("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", 1,20,string_value='CAR') 
         
        """
            Step 26.1 : Verify chart 
        """ 
        expected_xaxis_labels=['JAGUAR', 'JENSEN', 'TRIUMPH']
        expected_yaxis_labels=['0', '4K', '8K', '12K', '16K', '20K']
        verify_chart_output('jschart_HOLD_0', 'CAR', expected_xaxis_labels, expected_yaxis_labels, 3, 'riser!s0!g1!mbar!', '26')
        resultobj.verify_drilldown_navigation_menu('foreignObject div', ['Home','->','ENGLAND'], 'Step 26.6 : Verify drilldown navigation menu')
    
        
        """
            Step 27 : Hover over Chart riser "JENSEN" and Verify menus
        """
        expected_tooltip= ['CAR:JENSEN', 'DEALER_COST:14,940', 'Restore Original', 'Drill up to COUNTRY', 'Drill down to MODEL', 'Drilldown to Report', 'Information builders', 'Google']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g1!mbar!',expected_tooltip, 'Step 27.1 : Verify chart riser "JENSEN" menus')
       
        """
           Step 28 : Click "Drilldown to Report"
        """
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g1!mbar!', 'Drilldown to Report')
        time.sleep(4)
        utillobj.switch_to_window(1, pause=8)
        
        """
            Step 29 : Verify that drilldown to "Report003" is working properly and it opens in a new window 
        """
        resultobj.wait_for_property("table[summary]>tbody>tr:nth-child(1)>td:nth-child(1)", 1,20,string_value='COUNTRY')
        iarun.verify_table_data_set('table[summary]', Test_Case_ID+'_DataSet_01.xlsx', 'Step 29.1 : Verify that drilldown to "Report003" is working properly and it opens in a new window')
        
        """
            Step 30 : Close the Report window
        """
        self.driver.close()
        utillobj.switch_to_window(0, pause=5)
        utillobj.switch_to_default_content()
        utillobj.switch_to_frame(pause=1)
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='contentDrill']")))
        
        """
            Step 31 : Hover over Chart riser "TRIUMPH", Click "Drill down to MODEL"
        """
        expected_tooltip=  ['CAR:TRIUMPH', 'DEALER_COST:4,292', 'Restore Original', 'Drill up to COUNTRY', 'Drill down to MODEL', 'Drilldown to Report', 'Information builders', 'Google']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g2!mbar!',expected_tooltip, 'Step 31.1 : Verify chart riser "TRIUMPH" menus')
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g2!mbar!', 'Drill down to MODEL') 
        resultobj.wait_for_property("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", 1,20,string_value='MODEL') 
        
        """
            Step 32 : Verify the following "Chart" is displayed
        """
        expected_xaxis_labels=['TR7']
        expected_yaxis_labels=['0', '1,000', '2,000', '3,000', '4,000', '5,000']
        verify_chart_output('jschart_HOLD_0', 'MODEL', expected_xaxis_labels, expected_yaxis_labels, 1, 'riser!s0!g0!mbar!', '32')
        resultobj.verify_drilldown_navigation_menu('foreignObject div', ['Home','->','ENGLAND','->','TRIUMPH'], 'Step 32.6 : Verify drilldown navigation menu')
        
        """
            Step 33 : Hover over Chart riser "TR7" , Click "Information builders"
        """
        expected_tooltip=  ['MODEL:TR7', 'DEALER_COST:4,292', 'Restore Original', 'Drill up to CAR', 'Drilldown to Report', 'Information builders', 'Google']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g0!mbar!',expected_tooltip, 'Step 33.1 : Verify chart riser "TR7" menus')
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!', 'Information builders') 
        time.sleep(4)
        utillobj.switch_to_window(1, pause=8)
        time.sleep(3)
        
        """
            Step 34 : Verify it displays a new window going to IBI site.
        """
        utillobj.asin('Business', self.driver.title, 'Step 34 : Verify it displays a new window going to IBI site')
        
        """
            Step 35 : Close the window
        """
        self.driver.close()
        utillobj.switch_to_window(0, pause=5)
        utillobj.switch_to_default_content()
        utillobj.switch_to_frame(pause=1)
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='contentDrill']")))
        
        """
            Step 36 : Hover over Chart riser "TR7" , Click "Restore original"
        """
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!', 'Restore Original')
        resultobj.wait_for_property("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", 1,30,string_value='COUNTRY')
        
        """
            Step 37 : Verify the following Chart is displayed
        """
        expected_xaxis_labels=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        verify_chart_output('jschart_HOLD_0', 'COUNTRY', expected_xaxis_labels, expected_yaxis_labels, 5, 'riser!s0!g0!mbar!', '37')
        
        """
            Step 38 : Hover over on Chart riser "ITALY" , Click "Google"
        """
        expected_tooltip= ['COUNTRY:ITALY', 'DEALER_COST:41,235', 'Drill down to CAR', 'Drilldown to Report', 'Information builders', 'Google']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g2!mbar!',expected_tooltip, 'Step 38.1 : Verify chart riser "ITALY" menus')
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g2!mbar!', 'Google') 
        time.sleep(4)
        utillobj.switch_to_window(1, pause=8)
        time.sleep(3)
        
        """
            Step 39 : Verify it displays a new window going to "Google" site.
        """
        utillobj.asequal('Google', self.driver.title, 'Step 39.1 : Verify it displays a new window going to "Google" site.')
        
        """
            Step 40 : Close the window
        """
        self.driver.close()
        utillobj.switch_to_window(0, pause=5)
        utillobj.switch_to_default_content()
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_40', 'actual')
        
        """
            Step 41 : Click "IA" > "Save".
            Step 42 : Enter Title = "CHART-VAL-Multidrill" > Save
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID+'_CHART-VAL-Multidrill')
        time.sleep(2)
        
        """
            Step 43 : Click "IA" > "Exit"
        """
        utillobj.infoassist_api_logout()
        
if __name__=='__main__' :
    unittest.main()