'''
Created on December 26, 2017

@author: PM14587
Testcase Name : Verify Streamgraph using Join field (82xx)
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2228173
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea,visualization_ribbon,ia_ribbon
from common.lib import utillity

class C2228173_TestClass(BaseTestCase):
    
    def test_C2228173(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2228173'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbon=ia_ribbon.IA_Ribbon(self.driver)
       
        def verify_chart_output(parent_id,step_no):
            expected_xaxis_labels=['ADAMS', 'ADDAMS', 'ANDERSON', 'BELLA', 'CASSANOVA', 'CASTALANETTA', 'CHISOLM', 'CONRAD', 'CONTI', 'CVEK', 'DONATELLO', 'DUBOIS', 'ELLNER', 'FERNSTEIN', 'GORDON', 'GOTLIEB', 'GRAFF', 'HIRSCHMAN', 'KASHMAN', 'LASTRA', 'LEWIS', 'LIEBER', 'LOPEZ', 'MARTIN', 'MEDINA', 'MORAN', 'NOZAWA', 'OLSON', 'PATEL', 'PULASKI', 'PUMA', 'ROSENTHAL', 'RUSSO', 'SANCHEZ', 'SO', 'SOPENA', 'VALINO', 'WANG', 'WHITE']
            resultobj.verify_xaxis_title(parent_id, 'LASTNAME', 'Step '+step_no+'.1 : Verify chart X-Axis title')
            resultobj.verify_riser_chart_XY_labels(parent_id , expected_xaxis_labels, [], 'Step '+step_no+'.2 :', 15)
            resultobj.verify_riser_legends(parent_id, ['SALARY', 'EXPENSES'], 'Step '+step_no+'.3 : Verify chart legend labels')
            resultobj.verify_number_of_riser(parent_id, 1, 2, 'Step '+step_no+'.4 : Verify number of chart risers',custome_css=" svg path[class^='riser!']")
            utillobj.verify_chart_color(parent_id, 'riser!s1!g0!marea!', 'pale_green', 'Step '+step_no+'.5 : Verify chart riser color')
            utillobj.verify_chart_color(parent_id, 'riser!s0!g0!marea!', 'lochmara', 'Step '+step_no+'.6 : Verify chart riser color')  
         
        """
            Step 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/empdata
        """
        utillobj.infoassist_api_login('Chart','ibisamp/empdata','P292/S10032_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='legend-labels!s0!']", 'Series0', 65)
         
        """
            Step 02 : Select "Format" tab > "Chart Types" group > "Other" icon.
            Step 03 : Click "HTML5" icon in the dialogue and select "Streamgraph" > click Ok.
        """
        visul_ribbon.select_ribbon_item('Format', 'other')
        iaribbon.select_other_chart_type('html5', 'stream_graph', 2,ok_btn_click=True)
        utillobj.synchronize_with_number_of_element("#pfjTableChart_1 path[class*='riser!']", 5,25)
        """
            Step 04 : Verify the Default Streamgraph is displayed in "Live Preview".
        """
        resultobj.verify_riser_chart_XY_labels('pfjTableChart_1 ', ['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4'], [], 'Step 08.1 :', 10)
        resultobj.verify_riser_legends('pfjTableChart_1', ['Series0', 'Series1', 'Series2', 'Series3', 'Series4'], 'Step 08.2 : Verify chart legend labels')
        resultobj.verify_number_of_riser('pfjTableChart_1', 1, 5, 'Step 08.3 : Verify number of chart risers',custome_css=" svg path[class^='riser!']")   
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s3!g0!marea!', 'pale_yellow_2', 'Step 08.4 : Verify chart riser color')   
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_08', 'actual')
    
        """"
            Step 05 : Click "Data" tab > "Join" icon.
            Step 06 : Click "Add New" in the "Join" window.
            Step 07: Select "TRAINING.MAS" > Click "Open".
        """
        
        iaribbon.create_join_to_handle_lessthan_two_targets('ibisamp->training.mas', 'ibisamp', save_folder='ibisamp')
        join_css="#dlgJoinLinkManager [id^='JoinPanel'] div[class*='window-caption']> div[id^='BiLabel']"
        utillobj.synchronize_with_number_of_element(join_css, 2, 45)
        
        """
            Step 08:Verify a JOIN is created between the two master files.
        """
        actual_text_list=[join.text.strip() for join in self.driver.find_elements_by_css_selector(join_css)]
        print(actual_text_list)
        utillobj.asequal(actual_text_list, ['ibisamp/empdata', 'ibisamp/training'], 'Step 12.1 : Verify a JOIN is created between the two master files.')
        
        """
            Step 09 : Click "OK".
        """
        iaribbon.select_join_menu_buttons('ok')
        utillobj.synchronize_with_visble_text("#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr:nth-child(13)>td[class='']", 'COURSECODE', 25)
        
        """
            Step 10 : Double click "LASTNAME", "SALARY", "EXPENSES".
        """
        metaobj.datatree_field_click('LASTNAME',2,1)
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='xaxisOrdinal-title']", 'LASTNAME', 25)
        
        metaobj.datatree_field_click('SALARY',2,1)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        utillobj.synchronize_with_visble_text(parent_css, 'SALARY', 15)

        metaobj.datatree_field_click('EXPENSES',2,1)
        parent_css="#queryTreeWindow table tr:nth-child(6) td"
        utillobj.synchronize_with_visble_text(parent_css, 'EXPENSES', 15)
        
        """
            Step 11 : Verify the Streamgraph in "Live Preview" is updated to display the selected data.
        """
        verify_chart_output('pfjTableChart_1','15')
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_15', 'actual')
        
        """
            Step 12 : Click "Run".
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 35)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", 'LASTNAME', 25)
        
        """
            Step 13 : Verify the same chart is displayed at run time.
        """
        verify_chart_output('jschart_HOLD_0', '18')
        resultobj.verify_number_of_riser('jschart_HOLD_0', 2, 39, 'Step 18.7 : Verify number of marker',custome_css=" circle[class^='marker']")
        utillobj.switch_to_default_content(3)
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_17', 'actual')
        
        """
            Step 14 : Click Save in the toolbar > Save as "C2228173" > Click Save
            Step 15 : Close IA window.
        """
        visul_ribbon.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 16: Launch the IA API to run fex from bip.
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2228173.fex
        """
        utillobj.infoassist_api_logout()
        time.sleep(5)
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10032_chart_1',mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", 'LASTNAME', 65)
        
        """
            Step 17 : Verify the Streamgraph is run in a new window.
        """
        resultobj.verify_number_of_riser('jschart_HOLD_0', 2, 39, 'Step 18.7 : Verify number of marker',custome_css=" circle[class^='marker']")
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_22', 'actual')
        
        """
            Step 18:Close the chart run window.
        """
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
            Step 19:Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228173.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'Chart', 'S10032_chart_1',mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='xaxisOrdinal-title']", 'LASTNAME', 65)
        
        """
            Step 20:Verify IA is launched preserving the Streamgraph in "Live Preview".
        """
        verify_chart_output('pfjTableChart_1','25')
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_25', 'actual')
        time.sleep(4)
        
        """
            Launch the IA API to logout.
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        
if __name__=='__main__' :
    unittest.main()