'''
Created on December 26, 2017

@author: PM14587
Testcase Name : Verify the Parabox chart using different Themes (82xx)
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2228174
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea,visualization_ribbon,ia_ribbon
from common.lib import utillity

class C2228174_TestClass(BaseTestCase):
    
    def test_C2228174(self):
        
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
            Step 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10661&tool=chart&master=baseapp/SALES
        """
        utillobj.infoassist_api_login('Chart','ibisamp/sales','P292/S10032_chart_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1 text[class='legend-labels!s0!']", 1,40,string_value='Series0')
        time.sleep(3) 
         
        """
            Step 02 : Select "Format" > "Chart Types" > "Other" > "HTML5"
        """
        visul_ribbon.select_ribbon_item('Format', 'other')
    
        """"
            Step 03 : Select "Parabox" > "OK".
        """
        iaribbon.select_other_chart_type('html5', 'html5_parabox', 2,ok_btn_click=True)
        resultobj.wait_for_property("#pfjTableChart_1 text[class*='legend-labels!s6!']", 1,20,string_value='Series 6')
        time.sleep(3)
        
        """
            Step 04 : Verify the default "Parabox" chart is displayed in "Live Preview".
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
            Step 05 : Double click "CITY", "UNIT_SOLD", "DELIVER_AMT", "RETURNS".
        """
        metaobj.datatree_field_click('CITY',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,12,string_value='CITY')
        
        metaobj.datatree_field_click('UNIT_SOLD',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)", 1,12,string_value='UNIT_SOLD')

        metaobj.datatree_field_click('DELIVER_AMT',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,12,string_value='DELIVER_AMT')
        
        metaobj.datatree_field_click('RETURNS',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 1,12,string_value='RETURNS')
        time.sleep(2)
        
        """
            Step 06 : Verify the Parabox chart in "Live Preview" is updated.
        """
        verify_chart_output('pfjTableChart_1','06')
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s0!g0!mline!', 'bar_blue', 'Step 06.7 : Verify chart riser color', attribute_type='stroke')
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s1!g0!mline!', 'bar_green', 'Step 06.8 : Verify chart riser color', attribute_type='stroke')
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s2!g0!mline!', 'med_green', 'Step 06.9 : Verify chart riser color', attribute_type='stroke')
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s3!g0!mline!', 'pale_yellow', 'Step 06.10 : Verify chart riser color', attribute_type='stroke')
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_06', 'actual')
        
        """
            Step 07 : Select "Home" > "Theme" (in "Report" group).
            Step 08 : Select "Dark.sty" from the "Templates" library > "Open".
        """
        visul_ribbon.switch_ia_tab('Home')
        visul_ribbon.select_theme('Templates', 'Dark.sty')
        resultobj.wait_for_property("#pfjTableChart_1 svg>g>rect[class='background']", 1,10)
        
        """
            Step 09 : Verify the following chart is displayed.
        """
        verify_chart_output('pfjTableChart_1','09')
        utillobj.verify_chart_color('pfjTableChart_1', 'None', 'nero', 'Step 09.7 : Verify Dark.sty themes apply',custom_css="svg>g>rect[class='background']")
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_09', 'actual')
        
        """
            Step 10 : Click "Run".
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        resultobj.wait_for_property("#jschart_HOLD_0 .legend text[class*='legend-labels!s0!']", 1,20,string_value='NEW YORK')
        time.sleep(2)
        
        """
            Step 11 : Verify the following chart is displayed.
        """
        verify_chart_output('jschart_HOLD_0','11')
        utillobj.verify_chart_color('jschart_HOLD_0', 'None', 'nero', 'Step 11.7 : Verify Dark.sty themes apply',custom_css="svg>g>rect[class='background']")
        utillobj.switch_to_default_content(3)
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_11', 'actual')
        
        """
            Step 12 : Click "IA" > "Save" > "C2228174" > "Save".
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
            Step 13 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 14 : Run the fex from domains tree
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2228174.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10032_chart_1',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#jschart_HOLD_0 .legend text[class*='legend-labels!s0!']", 1,20,string_value='NEW YORK')
        time.sleep(2)
        
        """
            Step 15 : Verify the following chart is displayed.
        """
        verify_chart_output('jschart_HOLD_0','15')
        utillobj.verify_chart_color('jschart_HOLD_0', 'None', 'nero', 'Step 15.7 : Verify Dark.sty themes apply',custom_css="svg>g>rect[class='background']")
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_15', 'actual')
        
        """
            Step 16 : Dismiss the "Run" window.
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 17 : Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228174.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'Chart', 'S10032_chart_1',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#pfjTableChart_1 text[class*='legend-labels!s0!']", 1,35,string_value='NEW YORK')
        time.sleep(3)
        
        """
            Step 18 : Verify the following chart is displayed.
        """
        verify_chart_output('pfjTableChart_1','18')
        utillobj.verify_chart_color('pfjTableChart_1', 'None', 'nero', 'Step 18.7 : Verify Dark.sty themes apply',custom_css="svg>g>rect[class='background']")
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_18', 'actual')
        
        """
            Step 19 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        
if __name__=='__main__' :
    unittest.main()