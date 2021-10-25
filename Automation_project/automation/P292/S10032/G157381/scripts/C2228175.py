'''
Created on December 27, 2017

@author: PM14587
Testcase Name : Verify Chart with Auto Link and Multi Drill is working properly (82xx)
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2228175
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea,visualization_ribbon,ia_ribbon, ia_resultarea, metadata
from common.lib import utillity
from common.wftools.visualization import Visualization
from common.lib.global_variables import Global_variables
from common.lib.core_utility import CoreUtillityMethods

class C2228175_TestClass(BaseTestCase):

    def test_C2228175(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2228175'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbon=ia_ribbon.IA_Ribbon(self.driver)
        visual = Visualization(self.driver)
        ia_resultarea_obj=ia_resultarea.IA_Resultarea(self.driver)
        metaobj1=metadata.MetaData(self.driver)
        core_utillobj = CoreUtillityMethods(self.driver)
        
        def verify_chart_output(parent_id, yaxis_title, xaxis_labels, yaxis_labels, total_risers, riser_class, step_no):
            resultobj.verify_xaxis_title(parent_id, 'COUNTRY', 'Step '+step_no+'.1 : Verify X-Axis title')
            resultobj.verify_yaxis_title(parent_id, yaxis_title, 'Step '+step_no+'.2 : Verify Y-Axis title')
            resultobj.verify_riser_chart_XY_labels(parent_id, xaxis_labels, yaxis_labels, 'Step '+step_no+'.3 :',20)
            resultobj.verify_number_of_riser(parent_id, 1, total_risers, 'Step '+step_no+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color(parent_id, riser_class, 'bar_blue', 'Step '+step_no+'.5 : Verify chart riser color')
        
        """
            Step 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/carolap.mas
        """
        utillobj.infoassist_api_login('Chart','ibisamp/carolap','P292/S10032_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='legend-labels!s0!']", 'Series0', 65)
            
        """
            Step 02 : Double click "DEALER_COST".
        """
        metaobj.datatree_field_click('DEALER_COST',2,1)
        parent_css="#TableChart_1 text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'DEALER_COST', 15)
           
        """
            Step 03 : Expand COUNTRY Dimension > double click "COUNTRY".
        """
        metaobj1.double_click_on_data_filed('COUNTRY->COUNTRY->COUNTRY', 3)
        parent_css="#TableChart_1 text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'COUNTRY', 15)
         
        """
            Step 04 : Select "Format" > "Enable Auto Linking".
        """
        visul_ribbon.select_ribbon_item('Format', 'enable_auto_linking')
        utillobj.synchronize_with_number_of_element("[id='FormatEnableAutoLink'][class*='button-checked']", 1, 15)
#            
        """
            Step 04.1 : Verify chart output
        """
        expected_xaxis_labels=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        verify_chart_output('TableChart_1', 'DEALER_COST', expected_xaxis_labels, expected_yaxis_labels, 5, 'riser!s0!g2!mbar!', '04')
           
        """
            Step 05 : Click Save > enter "Title:" = "Chart_Source01", click "Save".
        """
        visul_ribbon.select_top_toolbar_item('toolbar_save')
        time.sleep(1)
        utillobj.ibfs_save_as(Test_Case_ID+'_Chart_Source01')
        time.sleep(2)
        
        """
            STEP 06 : Click IA > Close.
        """
        visul_ribbon.select_tool_menu_item('menu_close')
        utillobj.infoassist_api_logout()
          
        """
            Step 07 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/carolap.mas
        """
        utillobj.infoassist_api_login('Chart','ibisamp/carolap','P292/S10032_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='legend-labels!s0!']", 'Series0', 65)
          
        """
            Step 08 : Double click "RETAIL_COST".
        """
        metaobj.datatree_field_click('RETAIL_COST',2,1)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='yaxis-title']", 'RETAIL_COST', 15)
          
        """
            Step 09 : Expand COUNTRY Dimension > double click "COUNTRY".
        """
        metaobj1.double_click_on_data_filed('COUNTRY->COUNTRY->COUNTRY', 3)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='xaxisOrdinal-title']",'COUNTRY', 15)
          
        """
            Step 09.1 : Verify chart output
        """
        expected_xaxis_labels=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        verify_chart_output('TableChart_1', 'RETAIL_COST', expected_xaxis_labels, expected_yaxis_labels, 5, 'riser!s0!g2!mbar!', '09')
          
        """
            Step 10 : Drag and drop "COUNTRY" into Filter panel
        """
        metaobj1.drag_and_drop_data_field_to_filter('COUNTRY', field_position=3)
        utillobj.synchronize_with_visble_text("#dlgWhere_btnNewWhere div", 'New Filter', 45)
          
        """
            Step 11 : Double click "<Value>", set "Type:" = "Parameter", click "OK" (2x).
        """
        iaribbon.create_parameter_filter_condition(None, None)
        utillobj.synchronize_with_visble_text("#filterBox table>tbody>tr:nth-child(1)>td", 'COUNTRY Equal to Simple Parameter (Name: COUNTRY)', 35)
          
        """
            Step 12 : Verify "Filter" is created
        """
        metaobj.verify_filter_pane_field('COUNTRY Equal to Simple Parameter (Name: COUNTRY)', 1, 'Step 12.1 ')
          
        """
            Step 13 : Select "Format" > "Auto Link Target".
        """
        visul_ribbon.select_ribbon_item('Format', 'auto_link_target')
        utillobj.synchronize_with_number_of_element("[id='FormatTargetAutoLink'][class*='button-checked']", 1, 10)
#           
        """
            Step 14 : Click Save > enter "Title:" = "Chart_Target01", click "Save"
        """
        visul_ribbon.select_top_toolbar_item('toolbar_save')
        time.sleep(1)
        utillobj.ibfs_save_as(Test_Case_ID+'_Chart_Target01')
        
        """
            STEP 15 : Click IA > Close.
        """
        visul_ribbon.select_tool_menu_item('menu_close')
        utillobj.infoassist_api_logout() 
        
        """
            Step 16 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FChart_Source01.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID+'_Chart_Source01', 'Chart', 'S10032_chart_1',mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='xaxisOrdinal-title']", 'COUNTRY', 65) 
          
        """
            Step 17 : Select the field "DEALER_COST" in query pane > "Drill Down" on the Ribbon
        """
        metaobj.querytree_field_click('DEALER_COST',1) 
        utillobj.synchronize_with_visble_text("#FieldDrillDown div", 'Drill Down', 15)
           
        visul_ribbon.select_ribbon_item('Field', 'drilldown')
        utillobj.synchronize_with_visble_text("[id^='IABottomBar'] #ok", 'OK', 15)
          
        """
            Step 18 : Verify the "Drill Down - DEALER_COST" dialog opens
        """
        actual_label=self.driver.find_element_by_css_selector("[id^='QbDialog'] div[class*='i-window-caption']>div[class='bi-label']").text.strip()
        utillobj.asequal(actual_label, 'Drill Down - DEALER_COST', 'Step 18.1 : Verify the "Drill Down - DEALER_COST" opens')
          
        """
            Step 19 : Click "Web Page" radio button in "Drill Down - DEALER_COST"
            Step 20 : Click URL input box -> Type "http://www.ibi.com"
            Step 21 : lick "Create a new drill down" icon in "Drill Down - DEALER_COST"
        """
        iaribbon.create_drilldown_report('webpage', url_value='http://www.ibi.com', create_new_drilldown=True)
        time.sleep(8)
          
        """
            Step 22 : Select "Web Page" radio button
            Step 23 : Enter "http://www.bbc.com" in URL input box
            Step 24 : Click OK
        """
        iaribbon.create_drilldown_report('webpage', url_value='http://www.bbc.com', click_ok=True)
        time.sleep(8)
          
        """
            Step 25 : Click "IA" > "Close " > "Yes".
        """
        visul_ribbon.select_tool_menu_item('menu_close')
        ia_resultarea_obj.ia_exit_save("Yes")
        utillobj.infoassist_api_logout()
        
        """
            Step 26 : Launch the API to run from BIP.
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=Chart_Source01.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+'_Chart_Source01.fex', 'S10032_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", 'COUNTRY',45)
        screen_avail_height = self.driver.execute_script('return screen.availHeight')
        window_inner_height = self.driver.execute_script('return window.innerHeight')
        browser_y = screen_avail_height - window_inner_height
        Global_variables.current_working_area_browser_y = browser_y
        
        """
            Step 26.1 : Verify chart output
        """
        expected_xaxis_labels=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        verify_chart_output('jschart_HOLD_0', 'DEALER_COST', expected_xaxis_labels, expected_yaxis_labels, 5, 'riser!s0!g2!mbar!', '26')
                
        """
            Step 27 : Hover over on Chart riser "ITALY" and Verify the Autolink and Multidrill menus are displayed
        """
        expected_tooltip= ['COUNTRY:ITALY', 'DEALER_COST:41,235', 'Drill Down 1', 'Drill Down 2', 'Auto Links']
        msg = "Step 27.1 : Verify the Autolink and Multidrill menus are displayed"
        visual.verify_tooltip("riser!s0!g2!mbar!", expected_tooltip, msg, parent_css="jschart_HOLD_0")
        
        """
            Step 28 : Hover over "Autolink" > Select "Chart_Target01"
        """
        chart_obj = self.driver.find_element_by_id("jschart_HOLD_0")
        core_utillobj.python_move_to_element(chart_obj, element_location='top_left')
        visual.select_tooltip('riser!s0!g2!mbar!', "Auto Links->"+Test_Case_ID+"_Chart_Target01", parent_css='jschart_HOLD_0')
        core_utillobj.switch_to_new_window()
        
        """
            Step 29 : Verify "Chart_Target01" is displayed in a new window
        """
        expected_xaxis_labels=['ITALY']
        expected_yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        verify_chart_output('jschart_HOLD_0', 'RETAIL_COST', expected_xaxis_labels, expected_yaxis_labels, 1, 'riser!s0!g0!mbar!', '29')
        expected_tooltip= ['COUNTRY:ITALY', 'RETAIL_COST:51,065']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g0!mbar!',expected_tooltip, 'Step 29.6 : Verify tooltip value for England riser')
        
        """
            Step 30 : Close the window
        """
        core_utillobj.switch_to_previous_window()
        Global_variables.current_working_area_browser_y = browser_y
        
        """
            Step 31 : Select "ENGLAND" > Click "Drill down1"
        """
        expected_tooltip= ['COUNTRY:ENGLAND', 'DEALER_COST:37,853', 'Drill Down 1', 'Drill Down 2', 'Auto Links']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g0!mbar!',expected_tooltip, 'Step 31.1 : Verify tooltip value for England riser')
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!', 'Drill Down 1')
        core_utillobj.switch_to_new_window()
        
        """
            Step 32 : Verify it displays a new window going to IBI site
        """
        utillobj.asin('Data and Analytics Company | ibi', self.driver.title, 'Step 32.1 : Verify it displays a new window going to IBI site')
        
        """
            Step 33 : Close the IBI window
        """
        core_utillobj.switch_to_previous_window()
        Global_variables.current_working_area_browser_y = browser_y
        
        """
            Step 34 : Select "JAPAN" > Click "Drill down2"
        """
        expected_tooltip= ['COUNTRY:JAPAN', 'DEALER_COST:5,512', 'Drill Down 1', 'Drill Down 2', 'Auto Links']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g3!mbar!',expected_tooltip, 'Step 34.1 : Verify tooltip value for JAPAN riser')
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g3!mbar!', 'Drill Down 2')
        core_utillobj.switch_to_new_window()
        
        """
            Step 35 : Verify it displays a new window going to "BBC" site.
        """
        utillobj.asin('BBC', self.driver.title, 'Step 35.1 : Verify it displays a new window going to "BBC" site.')
        
        """
            Step 36 : Close the BBC window
        """
        core_utillobj.switch_to_previous_window()
        
        """
            Step 37 : Close the tool window
        """
        
if __name__=='__main__' :
    unittest.main()