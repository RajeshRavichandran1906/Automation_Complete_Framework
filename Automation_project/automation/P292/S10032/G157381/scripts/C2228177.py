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
            Step 01 :Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/car
        """
        utillobj.infoassist_api_login('Chart','ibisamp/car','P292/S10032_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='legend-labels!s0!']", 'Series0', 85)
        
        """
            Step 02 : Double click "DEALER_COST".
        """
        metaobj.datatree_field_click('DEALER_COST',2,1)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='yaxis-title']", 'DEALER_COST', 20)
        
        """
            Step 03 : Double click "COUNTRY".
        """
        metaobj.datatree_field_click('COUNTRY',2,1)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='xaxisOrdinal-title']", 'COUNTRY', 20)
        
        """
            Step 04 : Click "DEALER_COST" in the Query pane
            Step 05 : Click "Drill Down" in the Field Tab Ribbon
        """
        metaobj.querytree_field_click('DEALER_COST', 1, 1,'Drill Down')
        utillobj.synchronize_with_visble_text("[id^='IABottomBar'] #ok", 'OK', 20)
        
        """
            Step 06 : Click "Web Page" radio button
            Step 07 : Click URL input box -> Type http://www.ibi.com
            Step 08 : Click "Create a new drill down" button
        """
        iaribbon.create_drilldown_report('webpage',url_value='http://www.ibi.com',create_new_drilldown=True)
        time.sleep(5)
        
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
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 35)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", 'COUNTRY', 35)
        
        """
            Step 13 : Hover over ENGLAND -> Verify Drill Down menu
        """
        verify_chart_output('jschart_HOLD_0', '13')
        expected_tooltip=['COUNTRY:ENGLAND', 'DEALER_COST:37,853', 'Drill Down 1', 'Drill Down 2']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g0!mbar!',expected_tooltip, 'Step 13.6 :  Verify Drill Down menu')
        utillobj.switch_to_default_content(2)
        
        """
            Step 14 : Click Save in the toolbar > Save as "C2228177" > Click Save.
        """
        visul_ribbon.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
            Step 15 : Launch the IA API to logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(4)
        
        """
            Step 16 : Run chart using API code
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2228177.fex
        """
        
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10032_chart_1', 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", 'COUNTRY', 65)
        
        """
            Step 16:01
        """
        verify_chart_output('jschart_HOLD_0', '16')
        #utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_18')
        
        """
            Step 17 : Hover over ENGLAND -> Verify Drill Down menu
        """
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g0!mbar!',expected_tooltip, 'Step 17.1 :  Verify Drill Down menu')
        time.sleep(2)
        
        """
            Step 18 : Select "Drill Down 2" -> Verify the google page is displayed
        """
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!', 'Drill Down 2', cord_type="middle")
        time.sleep(10)
        utillobj.switch_to_window(1)
        
        """
            Step 19 : Launch the IA API to logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.asequal('Google', self.driver.title, 'Step 19.1 : Verify the google page is displayed')
        self.driver.close()
        time.sleep(2)
                
        """
            Step 21 : Dismiss the output window.
        """
              
if __name__=='__main__' :
    unittest.main()