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
            Step 01 :Launch WF, New > Chart with EMPDATA.MAS.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/empdata','P292/S10032_chart_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1 text[class='legend-labels!s0!']", 1,40,string_value='Series0')
        time.sleep(3) 
         
        """
            Step 02 : Select "HTML5" from format group under Home tab (if not selected by default).
            Step 03 : Select "Format" tab.
            Step 04 : Expand "Chart Types" group (if not already expanded).
            Step 05 : Click "Other" icon.
        """
        visul_ribbon.select_ribbon_item('Format', 'other')
    
        """"
            Step 06 : Click "HTML5" icon in the dialogue and select "Streamgraph".
            Step 07 : Click "OK".
        """
        iaribbon.select_other_chart_type('html5', 'stream_graph', 2,ok_btn_click=True)
        resultobj.wait_for_property("#pfjTableChart_1 path[class*='riser!']", 5,10)
        
        """
            Step 08 : Verify the Default Streamgraph is displayed in "Live Preview".
        """
        resultobj.verify_riser_chart_XY_labels('pfjTableChart_1 ', ['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4'], [], 'Step 08.1 :', 10)
        resultobj.verify_riser_legends('pfjTableChart_1', ['Series0', 'Series1', 'Series2', 'Series3', 'Series4'], 'Step 08.2 : Verify chart legend labels')
        resultobj.verify_number_of_riser('pfjTableChart_1', 1, 5, 'Step 08.3 : Verify number of chart risers',custome_css=" svg path[class^='riser!']")   
        utillobj.verify_chart_color('pfjTableChart_1', 'riser!s3!g0!marea!', 'pale_yellow_2', 'Step 08.4 : Verify chart riser color')   
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_08', 'actual')
        
        """
            Step 09 : Click "Data" tab > "Join" icon.
            Step 10 : Click "Add New" in the "Join" window.
            Step 11 : Select "TRAINING.MAS" > Click "Open".
        """
        iaribbon.create_join('ibisamp->training.mas',save_folder='ibisamp')
        join_css="#dlgJoinLinkManager [id^='JoinPanel'] div[class*='window-caption']> div[id^='BiLabel']"
        resultobj.wait_for_property(join_css, 2,10)
        
        """
            Step 12 : Verify a JOIN is created between the two master files.
        """
        actual_text_list=[join.text.strip() for join in self.driver.find_elements_by_css_selector(join_css)]
        utillobj.asequal(actual_text_list, ['ibisamp/empdata', 'ibisamp/training'], 'Step 12.1 : Verify a JOIN is created between the two master files.')
        
        """
            Step 13 : Click "OK".
        """
        iaribbon.select_join_menu_buttons('ok')
        resultobj.wait_for_property("#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr:nth-child(13)>td[class='']", 1,20,string_value='COURSECODE')
        
        """
            Step 14 : Double click "LASTNAME", "SALARY", "EXPENSES".
        """
        metaobj.datatree_field_click('LASTNAME',2,1)
        resultobj.wait_for_property("#pfjTableChart_1 text[class='xaxisOrdinal-title']", 1,12,string_value='LASTNAME')
        
        metaobj.datatree_field_click('SALARY',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,12,string_value='SALARY')

        metaobj.datatree_field_click('EXPENSES',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 1,12,string_value='EXPENSES')
        time.sleep(2)
        
        """
            Step 15 : Verify the Streamgraph in "Live Preview" is updated to display the selected data.
        """
        verify_chart_output('pfjTableChart_1','15')
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_15', 'actual')
        
        """
            Step 16 : Click "Run".
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        
        utillobj.switch_to_frame(pause=2)
        resultobj.wait_for_property("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", 1,12,string_value='LASTNAME')
        time.sleep(2)
        
        """
            Step 17 : Verify the same chart is displayed at run time.
        """
        verify_chart_output('jschart_HOLD_0', '18')
        resultobj.verify_number_of_riser('jschart_HOLD_0', 2, 39, 'Step 18.7 : Verify number of marker',custome_css=" circle[class^='marker']")
        utillobj.switch_to_default_content(3)
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_17', 'actual')
        
        """
            Step 18 : Click "IA" > "Save".
            Step 19 : Enter Title = "IA-CHART-VAL-019".
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step : Click "Save" and dismiss IA window.
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 21 : Locate the saved fex > Right mouse click > "Run". ( Here API using for run fex)
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10032_chart_1',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", 1,12,string_value='LASTNAME')
        time.sleep(2)
        
        """
            Step 22 : Verify the Streamgraph is run in a new window.
        """
        verify_chart_output('jschart_HOLD_0', '22')
        resultobj.verify_number_of_riser('jschart_HOLD_0', 2, 39, 'Step 18.7 : Verify number of marker',custome_css=" circle[class^='marker']")
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_22', 'actual')
        
        """
            Step 23 : Close the chart run window.
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 24 : Locate the saved fex > Right mouse click > "Edit".
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'Chart', 'S10032_chart_1',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#pfjTableChart_1 text[class='xaxisOrdinal-title']", 1,12,string_value='LASTNAME')
        time.sleep(2)
        
        """
            Step 25 : Verify IA is launched preserving the Streamgraph in "Live Preview".
        """
        verify_chart_output('pfjTableChart_1','25')
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_25', 'actual')
        
if __name__=='__main__' :
    unittest.main()