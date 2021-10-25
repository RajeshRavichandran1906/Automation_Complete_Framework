'''
Created on December 22, 2017

@author: PM14587
Testcase Name : Verify Chart with Multi Drill and Auto Drill is working properly (82xx)
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2228178
'''
import unittest, time
from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea,visualization_ribbon,ia_ribbon,ia_run, metadata

class C2228178_TestClass(BaseTestCase):

    def test_C2228178(self):
        
        """   
            TESTCASE VARIABLES 
        """
        fex_name="Report003"
        Test_Case_ID = 'C2228178'
        
        """   
            TESTCASE OBJECTS 
        """
        iarun=ia_run.IA_Run(self.driver)
        iaribbon=ia_ribbon.IA_Ribbon(self.driver)
        metadataobj=metadata.MetaData(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
         
        def verify_chart_output(parent_id, yaxis_title, xaxis_labels, yaxis_labels, total_risers, riser_class, step_no):
            resultobj.verify_xaxis_title(parent_id, yaxis_title, 'Step '+step_no+'.1 : Verify X-Axis title')
            resultobj.verify_yaxis_title(parent_id, 'DEALER_COST', 'Step '+step_no+'.2 : Verify Y-Axis title')
            resultobj.verify_riser_chart_XY_labels(parent_id, xaxis_labels, yaxis_labels, 'Step '+step_no+'.3 :',20)
            resultobj.verify_number_of_riser(parent_id, 1, total_risers, 'Step '+step_no+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color(parent_id, riser_class, 'bar_blue', 'Step '+step_no+'.5 : Verify chart riser color')
        
        """
            Step 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/carolap
        """ 
        utillobj.infoassist_api_login('Chart','ibisamp/carolap','P292/S10032_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='legend-labels!s0!']", 'Series0', 65)
         
        """
            Step 02 : Double click "DEALER_COST".
        """
        metadataobj.double_click_on_data_filed("Measures->DEALER_COST", 1)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='yaxis-title']", "DEALER_COST", 20)
        
        """
            Step 03 : Expand COUNTRY Dimension > double click "COUNTRY".
        """
        metadataobj.double_click_on_data_filed("Dimensions->COUNTRY->COUNTRY->COUNTRY", 3)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='xaxisOrdinal-title']", 'COUNTRY', 15)
        
        """
            Step 04 : Verify the following "Chart" in Livepreview
        """ 
        expected_xaxis_labels=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        verify_chart_output('TableChart_1', 'COUNTRY', expected_xaxis_labels, expected_yaxis_labels, 5, 'riser!s0!g2!mbar!', '04')
        
        """
            Step 05 : Select "Format" > "Auto Drill" button (from navigation group)
        """
        visul_ribbon.select_ribbon_item('Format', 'auto_drill')
        utillobj.synchronize_with_number_of_element("[id='FormatAutoDrill'][class*='button-checked']", 1, 8)
        
        """
            Step 06 : Select "DEALER_COST" in Query pane
        """ 
        metaobj.querytree_field_click('DEALER_COST',1) 
        utillobj.synchronize_with_visble_text("#FieldDrillDown div", "Drill Down", 12)
         
        """
            Step 07: Click "Links" > "Drill down" from "Field" tab..
        """
        visul_ribbon.select_ribbon_item('Field', 'drilldown')
        utillobj.synchronize_with_visble_text("[id^='IABottomBar'] #ok", 'OK', 10)
         
        """
            Step 08 : Verify the "Drill Down - DEALER_COST" opens and "Report" is enabled by default in the dialog
        """
        actual_label=self.driver.find_element_by_css_selector("[id^='QbDialog'] div[class*='i-window-caption']>div[class='bi-label']").text.strip()
        utillobj.asequal(actual_label, 'Drill Down - DEALER_COST', 'Step 13.1 : Verify the "Drill Down - DEALER_COST" opens')
        
        """
            Step 09 : Click "Browse" > Select "Report003" > Open.
            Step 10 : Set "Description" = "Drilldown to Report".
            Step 11: Click "Create a new drill down" icon
            Step 12: Select "Web Page" option and Type "http://www.ibi.com" in URL input box
        """
        iaribbon.create_drilldown_report('report', browse_file_name=fex_name, set_description='Drilldown to Report',verify_drilldown_type=True,create_new_drilldown=True)
        time.sleep(2)
        
        """
            
            Step 13 : Set "Description" = "Information builders".
            Step 14 : Click "Create a new drill down" icon
        """
        element=self.driver.find_element_by_css_selector("[id^='QbDialog'] div[class*='i-window-caption']>div[class='bi-label']")
        utillobj.click_on_screen(element,'middle')
        time.sleep(2)
        iaribbon.create_drilldown_report('webpage',url_value='http://www.ibi.com', set_description='Information builders', create_new_drilldown=True)
        time.sleep(2)
        
        """
            Step 15 : Select "Web Page" option and Type "http://www.google.com" in URL input box
            Step 16 : Set "Description" = "Google".
            Step 17 : Click "OK"
        """ 
        iaribbon.create_drilldown_report('webpage',url_value='http://www.google.com', set_description='Google', click_ok=True)
        time.sleep(8) 
     
        """
            Step 18 : Click Run
        """ 
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=4)
        core_utils.switch_to_frame(frame_css="iframe[src*='contentDrill']")
#         WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='contentDrill']")))
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", "COUNTRY", 30)
        
        """
            Step 18:01
        """
        expected_xaxis_labels=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        verify_chart_output('jschart_HOLD_0', 'COUNTRY', expected_xaxis_labels, expected_yaxis_labels, 5, 'riser!s0!g0!mbar!', '23')
       
        """
            Step 19 : Hover over on Chart riser "ENGLAND"
            Step 20 : Verify the Autodrill and Multidrill menus are displayed
        """
        expected_tooltip= ['COUNTRY:ENGLAND', 'DEALER_COST:37,853', 'Drill down to CAR', 'Drilldown to Report', 'Information builders', 'Google']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g0!mbar!',expected_tooltip, 'Step 20.1 : Verify the Autodrill and Multidrill menus are displayed')
         
        """
            Step 21 : Select "Drill Down to CAR" and Verify Chart
        """ 
        time.sleep(5)
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!', 'Drill down to CAR')
        time.sleep(8)
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", "CAR", 20)
        
        """
            Step 21.1 : Verify chart 
        """ 
        expected_xaxis_labels=['JAGUAR', 'JENSEN', 'TRIUMPH']
        expected_yaxis_labels=['0', '4K', '8K', '12K', '16K', '20K']
        verify_chart_output('jschart_HOLD_0', 'CAR', expected_xaxis_labels, expected_yaxis_labels, 3, 'riser!s0!g1!mbar!', '26')
        resultobj.verify_drilldown_navigation_menu('[class="title"]', ['Home','->','ENGLAND'], 'Step 21.1 : Verify drilldown navigation menu')
    
        
        """
            Step 22 : Hover over Chart riser "JENSEN" and Verify menus
        """
        expected_tooltip= ['CAR:JENSEN', 'DEALER_COST:14,940', 'Restore Original', 'Drill up to COUNTRY', 'Drill down to MODEL', 'Drilldown to Report', 'Information builders', 'Google']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g1!mbar!',expected_tooltip, 'Step 27.1 : Verify chart riser "JENSEN" menus')
       
        """
           Step 23 :Click "Drilldown to Report"
        """
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g1!mbar!', 'Drilldown to Report')
        time.sleep(4)
        utillobj.switch_to_window(1, pause=8)
        
        """
            Step 24 : Verify that drilldown to "Report003" is working properly and it opens in a new window 
        """
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(1)>td:nth-child(1)", "COUNTRY", 20)
        iarun.verify_table_data_set('table[summary]', Test_Case_ID+'_DataSet_01.xlsx', 'Step 29.1 : Verify that drilldown to "Report003" is working properly and it opens in a new window')
        
        """
            Step 25 : Close the Report window
        """
        core_utils.switch_to_previous_window()
        utillobj.switch_to_default_content()
        utillobj.switch_to_frame(pause=1)
        core_utils.switch_to_frame(frame_css="iframe[src*='contentDrill']")
#         WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='contentDrill']")))
        
        """
            Step 26 : Hover over Chart riser "TRIUMPH", Click "Drill down to MODEL"
        """
        expected_tooltip=  ['CAR:TRIUMPH', 'DEALER_COST:4,292', 'Restore Original', 'Drill up to COUNTRY', 'Drill down to MODEL', 'Drilldown to Report', 'Information builders', 'Google']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g2!mbar!',expected_tooltip, 'Step 26.1 : Verify chart riser "TRIUMPH" menus')
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g2!mbar!', 'Drill down to MODEL') 
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", "MODEL", 25)
        
        """
            Step 27 : Verify the following "Chart" is displayed
        """
        expected_xaxis_labels=['TR7']
        expected_yaxis_labels=['0', '1,000', '2,000', '3,000', '4,000', '5,000']
        verify_chart_output('jschart_HOLD_0', 'MODEL', expected_xaxis_labels, expected_yaxis_labels, 1, 'riser!s0!g0!mbar!', '32')
        resultobj.verify_drilldown_navigation_menu('[class="title"]', ['Home','->','ENGLAND','->','TRIUMPH'], 'Step 27.1 : Verify drilldown navigation menu')
        
        """
            Step 28 : Hover over Chart riser "TR7" , Click "Information builders"
        """
        expected_tooltip=  ['MODEL:TR7', 'DEALER_COST:4,292', 'Restore Original', 'Drill up to CAR', 'Drilldown to Report', 'Information builders', 'Google']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g0!mbar!',expected_tooltip, 'Step 28.1 : Verify chart riser "TR7" menus')
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!', 'Information builders') 
        time.sleep(4)
        utillobj.switch_to_window(1, pause=8)
        time.sleep(3)
        
        """
            Step 29 : Verify it displays a new window going to IBI site.
        """
        utillobj.asin('Data and Analytics Company | ibi', self.driver.title, 'Step 29 : Verify it displays a new window going to IBI site')
        
        """
            Step 30 : Close the window
        """
        self.driver.close()
        utillobj.switch_to_window(0, pause=5)
        utillobj.switch_to_default_content()
        utillobj.switch_to_frame(pause=1)
        core_utils.switch_to_frame(frame_css="iframe[src*='contentDrill']")
#         WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='contentDrill']")))
        
        """
            Step 31 : Hover over Chart riser "TR7" , Click "Restore original"
        """
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!', 'Restore Original')
        time.sleep(8)
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", "COUNTRY", 30)
        
        """
            Step 32 : Verify the following Chart is displayed
        """
        expected_xaxis_labels=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        verify_chart_output('jschart_HOLD_0', 'COUNTRY', expected_xaxis_labels, expected_yaxis_labels, 5, 'riser!s0!g0!mbar!', '37')
        
        """
            Step 33 : Hover over on Chart riser "ITALY" , Click "Google"
        """
        expected_tooltip= ['COUNTRY:ITALY', 'DEALER_COST:41,235', 'Drill down to CAR', 'Drilldown to Report', 'Information builders', 'Google']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g2!mbar!',expected_tooltip, 'Step 33.1 : Verify chart riser "ITALY" menus')
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g2!mbar!', 'Google') 
        time.sleep(4)
        utillobj.switch_to_window(1, pause=8)
        time.sleep(3)
        
        """
            Step 34 : Verify it displays a new window going to "Google" site.
        """
        utillobj.asequal('Google', self.driver.title, 'Step 34.1 : Verify it displays a new window going to "Google" site.')
        
        """
            Step 35 : Close the window
        """
        self.driver.close()
        utillobj.switch_to_window(0, pause=5)
        utillobj.switch_to_default_content()
      
        """
            Step 36 : Click Save in the toolbar > Save as "C2228178" > Click Save.
        """
        visul_ribbon.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
            Step 37 :Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        
if __name__=='__main__' :
    unittest.main()