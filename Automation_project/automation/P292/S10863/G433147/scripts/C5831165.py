'''
Created on October 30, 2018

@author: PM14587
Testcase Name : Verify the Parabox chart using different Themes
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5831165
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea,visualization_ribbon,ia_ribbon
from common.lib import utillity

class C5831165_TestClass(BaseTestCase):
    
    def test_C5831165(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2228174'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbon=ia_ribbon.IA_Ribbon(self.driver)
       
        def verify_chart_output(parent_id,step_no):
            resultobj.verify_riser_legends(parent_id, ['NEW YORK', 'NEWARK', 'STAMFORD', 'UNIONDALE'], 'Step '+step_no+'.1 : Verify chart legend labels')
            resultobj.verify_number_of_riser(parent_id, 1, 4, 'Step '+step_no+'.2 : Verify number of chart risers',custome_css=" svg path[class^='riser!']")   
            resultobj.verify_number_of_riser(parent_id, 1, 3, 'Step '+step_no+'.3 : Verify number of cursor move risers',custome_css=" svg rect[cursor='move']")
            resultobj.verify_number_of_riser(parent_id, 1, 3, 'Step '+step_no+'.4 : Verify number of Parabox chart line risers',custome_css=" svg line")
            expected_label_text=['UNIT_SOLD', 'DELIVER_AMT', 'RETURNS', '42', '377', '60', '431', '1', '41']
            resultobj.verify_data_labels(parent_id, expected_label_text, 'Step '+step_no+'.5 : Verify parabox chart label text',custom_css='svg>g text[cursor]')
            utillobj.verify_chart_color(parent_id, 'None', 'french_lilac', 'Step '+step_no+'.6 : Verify parabox chart move riser color', custom_css="svg rect[cursor='move']")
            
        """
            STEP 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10661&tool=chart&master=ibisamp/sales
        """
        utillobj.infoassist_api_login('Chart','ibisamp/sales','P292/S10032_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='legend-labels!s0!']", 'Series0', 65)
       
        """
            STEP 02 : Select "Format" > "Chart Types" > "Other" > "HTML5"
        """
        visul_ribbon.select_ribbon_item('Format', 'other')
    
        """"
            STEP 03 : Select "Parabox" > "OK".
        """
        iaribbon.select_other_chart_type('html5', 'html5_parabox', 2,ok_btn_click=True)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class*='legend-labels!s6!']",'Series 6', 30)
        
        """
            STEP 04 : Verify the default "Parabox" chart is displayed in "Live Preview" and query pane.
        """
        resultobj.verify_riser_legends('pfjTableChart_1', ['Series0', 'Series1', 'Series2', 'Series3', 'Series4', 'Series 5', 'Series 6'], 'Step 04.1 : Verify chart legend labels')
        resultobj.verify_number_of_riser('pfjTableChart_1', 1, 7, 'Step 04.2 : Verify number of chart risers',custome_css=" svg path[class^='riser!']")   
        resultobj.verify_number_of_riser('pfjTableChart_1', 1, 5, 'Step 04.3 : Verify number of cursor move risers',custome_css=" svg rect[cursor='move']")
        resultobj.verify_number_of_riser('pfjTableChart_1', 1, 6, 'Step 04.4 : Verify number of Parabox chart line risers',custome_css=" svg line")
        expected_label_text=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5', '1', '8', '1', '8', '1', '8', '1', '9', '2', '10', 'A', 'C', 'B']
        resultobj.verify_data_labels('pfjTableChart_1', expected_label_text, 'Step 04.5 : Verify parabox chart label text',custom_css='svg>g text[cursor]')
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_04', 'actual')
        
        """
            STEP 05 : Double click "CITY", "UNIT_SOLD", "DELIVER_AMT", "RETURNS".
        """
        metaobj.datatree_field_click('CITY',2,1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)",'CITY', 20)
        
        metaobj.datatree_field_click('UNIT_SOLD',2,1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)",'UNIT_SOLD', 20)

        metaobj.datatree_field_click('DELIVER_AMT',2,1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 'DELIVER_AMT', 20)
        
        metaobj.datatree_field_click('RETURNS',2,1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)",'RETURNS',20)
        
        """
            STEP 06 : Verify the Parabox chart in "Live Preview" is updated.
        """
        verify_chart_output('pfjTableChart_1','06')
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s0!g0!mline!', 'bar_blue', 'Step 06.7 : Verify chart riser color', attribute_type='stroke')
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s1!g0!mline!', 'bar_green', 'Step 06.8 : Verify chart riser color', attribute_type='stroke')
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s2!g0!mline!', 'med_green', 'Step 06.9 : Verify chart riser color', attribute_type='stroke')
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s3!g0!mline!', 'pale_yellow', 'Step 06.10 : Verify chart riser color', attribute_type='stroke')
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_06', 'actual')
        
        """
            STEP 07 : Select "Home" > "Theme" (in "Report" group).
            STEP 08 : Select "Dark.sty" from the "Templates" library > "Open".
        """
        visul_ribbon.switch_ia_tab('Home')
        visul_ribbon.select_theme('Templates', 'Dark.sty')
        utillobj.synchronize_with_number_of_element("#pfjTableChart_1 svg>g>rect[class='background']", 1,15)
        
        """
            STEP 09 : Verify the following chart is displayed.
        """
        verify_chart_output('pfjTableChart_1','09')
        utillobj.verify_chart_color('pfjTableChart_1', 'None', 'nero', 'Step 09.7 : Verify Dark.sty themes apply',custom_css="svg>g>rect[class='background']")
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_09', 'actual')
        
        """
            STEP 10 : Click "Run".
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 30)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 .legend text[class*='legend-labels!s0!']", 'NEW YORK', 35)
        
        """
            STEP 11 : Verify the following chart is displayed.
        """
        verify_chart_output('jschart_HOLD_0','11')
        utillobj.verify_chart_color('jschart_HOLD_0', 'None', 'nero', 'Step 11.7 : Verify Dark.sty themes apply',custom_css="svg>g>rect[class='background']")
        utillobj.switch_to_default_content(3)
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_11', 'actual')
        
        """
            STEP 12 : Click "IA" > "Save" > "C5831165" > "Save".
        """
        visul_ribbon.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            STEP 13 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(4)
        
        """
            STEP 14 : Run the fex from domains tree
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C5831165.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10032_chart_1',mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 .legend text[class*='legend-labels!s0!']", 'NEW YORK', 80)
        
        """
            STEP 15 : Verify the following chart is displayed.
        """
        verify_chart_output('jschart_HOLD_0','15')
        utillobj.verify_chart_color('jschart_HOLD_0', 'None', 'nero', 'Step 15.7 : Verify Dark.sty themes apply',custom_css="svg>g>rect[class='background']")
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_15', 'actual')
        
        """
            STEP 16 : Dismiss the "Run" window.
        """
        utillobj.infoassist_api_logout()
        
        """
            STEP 17 : Restore saved fex using API
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC5831165.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'Chart', 'S10032_chart_1',mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class*='legend-labels!s0!']", 'NEW YORK', 80)
        
        """
            STEP 18 : Verify the following chart is displayed.
        """
        verify_chart_output('pfjTableChart_1','18')
        utillobj.verify_chart_color('pfjTableChart_1', 'None', 'nero', 'Step 18.7 : Verify Dark.sty themes apply',custom_css="svg>g>rect[class='background']")
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_18', 'actual')
        
        """
            STEP 19 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        
if __name__=='__main__' :
    unittest.main()