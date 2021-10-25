'''
Created on December 21, 2017

@author: PM14587
Testcase Name : Verify Chart with Multi Drill (82xx)
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2228177
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea,visualization_ribbon,ia_ribbon
from common.lib import utillity

class C2228177_TestClass(BaseTestCase):

    def test_C2228177(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2228177'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbon=ia_ribbon.IA_Ribbon(self.driver)
        
        def verify_chart_output(parent_id,step_no):
            expected_xaxis_labels=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
            expected_yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
            resultobj.verify_xaxis_title(parent_id, 'COUNTRY', 'Step '+step_no+'.1 : Verify X-Axis title')
            resultobj.verify_yaxis_title(parent_id, 'DEALER_COST', 'Step '+step_no+'.2 : Verify Y-Axis title')
            resultobj.verify_riser_chart_XY_labels(parent_id, expected_xaxis_labels, expected_yaxis_labels, 'Step '+step_no+'.3 :',20)
            resultobj.verify_number_of_riser(parent_id, 1, 5, 'Step '+step_no+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color(parent_id, 'riser!s0!g0!mbar!', 'bar_blue', 'Step '+step_no+'.5 : Verify chart riser color')
            
        """
            Step 01 :Launch WF, New > Chart with CAR.MAS.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/car','P292/S10032_chart_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1 text[class='legend-labels!s0!']", 1,40,string_value='Series0')
        time.sleep(3)
        
        """
            Step 02 : Double click "DEALER_COST".
        """
        metaobj.datatree_field_click('DEALER_COST',2,1)
        resultobj.wait_for_property("#TableChart_1 text[class='yaxis-title']", 1,20,string_value='DEALER_COST')
        
        """
            Step 03 : Double click "COUNTRY".
        """
        metaobj.datatree_field_click('COUNTRY',2,1)
        resultobj.wait_for_property("#TableChart_1 text[class='xaxisOrdinal-title']", 1,20,string_value='COUNTRY')
        time.sleep(2)
        
        """
            Step 03.1 : Verify char output.
        """
        verify_chart_output('TableChart_1', '03')
        
        """
            Step 04 : Click "DEALER_COST" in the Query pane
            Step 05 : Click "Drill Down" in the Field Tab Ribbon
        """
        metaobj.querytree_field_click('DEALER_COST', 1, 1,'Drill Down')
        resultobj.wait_for_property("[id^='IABottomBar'] #ok", 1,10,string_value='OK')
        
        """
            Step 06 : Click "Web Page" radio button
            Step 07 : Click URL input box -> Type http://www.ibi.com
            Step 08 : Click "Create a new drill down" button
        """
        iaribbon.create_drilldown_report('webpage',url_value='http://www.ibi.com',create_new_drilldown=True)
        time.sleep(2)
        
        """
            Step 09 : Click "Web Page" radio button
            Step 10 : Click URL input box -> Type http://www.google.com
            Step 11 : Click OK
        """
        iaribbon.create_drilldown_report('webpage',url_value='http://www.google.com',click_ok=True)
        time.sleep(4)
        verify_chart_output('TableChart_1', '11')
        
        """
            Step 12 : Click "Run"
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        resultobj.wait_for_property("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", 1,30,string_value='COUNTRY')
        time.sleep(2)
        
        """
            Step 13 : Hover over ENGLAND -> Verify Drill Down menu
        """
        verify_chart_output('jschart_HOLD_0', '13')
        expected_tooltip=['COUNTRY:ENGLAND', 'DEALER_COST:37,853', 'Drill Down 1', 'Drill Down 2']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g0!mbar!',expected_tooltip, 'Step 13.6 :  Verify Drill Down menu')
        utillobj.switch_to_default_content(2)
        
        """
            Step 14 : Click "IA" > "Save As".
            Step 15 : Enter Title = "IA-VAL-CHART-MULTI2".
            Step 16 : Click "Save".
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as('IA-VAL-CHART-MULTI2')
        time.sleep(2)
        
        """
            Step 17 : Dismiss the tool window.
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 18 : Right mouse click the saved report > Run ( API link using here to run chart)
        """
        
        utillobj.active_run_fex_api_login('IA-VAL-CHART-MULTI2.fex', 'S10032_chart_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", 1,30,string_value='COUNTRY')
        
        """
            Step 18.1 : Verify chart output
        """
        verify_chart_output('jschart_HOLD_0', '18')
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_18')
        
        """
            Step 19 : Hover over ENGLAND -> Verify Drill Down menu
        """
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g0!mbar!',expected_tooltip, 'Step 13.6 :  Verify Drill Down menu')
        time.sleep(2)
        
        """
            Step 20 : Select "Drill Down 2" -> Verify the google page is displayed
        """
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!', 'Drill Down 2')
        time.sleep(4)
        utillobj.switch_to_window(1)
        
        """
            Step 20.1 : Verify the google page is displayed
        """
        utillobj.asequal('Google', self.driver.title, 'Step 20.1 : Verify the google page is displayed')
        self.driver.close()
        time.sleep(2)
        utillobj.switch_to_main_window()
        
        """
            Step 21 : Dismiss the output window.
        """
        utillobj.infoassist_api_logout()
       
if __name__=='__main__' :
    unittest.main()