'''
Created on December 21, 2017

@author: PM14587
Testcase Name : Verify Sort on field works properly (82xx)
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2228179
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea,visualization_ribbon
from common.lib import utillity

class C2228179_TestClass(BaseTestCase):

    def test_C2228179(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2228179'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        
        def verify_chart_output(parent_id,expected_xaxis_labels,step_no):
            expected_yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
            resultobj.verify_xaxis_title(parent_id, 'Product Category', 'Step '+step_no+'.1 : Verify X-Axis title')
            resultobj.verify_yaxis_title(parent_id, 'Revenue', 'Step '+step_no+'.2 : Verify Y-Axis title')
            resultobj.verify_riser_chart_XY_labels(parent_id, expected_xaxis_labels, expected_yaxis_labels, 'Step '+step_no+'.3 :',20)
            resultobj.verify_number_of_riser(parent_id, 1, 7, 'Step '+step_no+'.4 : Verify number of chart risers')
            utillobj.verify_chart_color(parent_id, 'riser!s0!g3!mbar!', 'bar_blue', 'Step '+step_no+'.5 : Verify chart riser color')
            
        """
            Step 01 :Launch WF, New > Chart with WF_RETAIL.MAS.
        """
        utillobj.infoassist_api_login('Chart','new_retail/wf_retail','P292/S10032_chart_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1 text[class='legend-labels!s0!']", 1,40,string_value='Series0')
        time.sleep(3)
        
        """
            Step 02 : Double click "Revenue","Product,Category".
        """
        metaobj.datatree_field_click('Revenue',2,1)
        resultobj.wait_for_property("#TableChart_1 text[class='yaxis-title']", 1,20,string_value='Revenue')
        
        metaobj.datatree_field_click('Product,Category',2,1)
        resultobj.wait_for_property("#TableChart_1 text[class='xaxisOrdinal-title']", 1,20,string_value='Product Category')
        time.sleep(2)
        
        """
            Step 03 : Verify the following chart is displayed.
        """
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_chart_output('TableChart_1', expected_xaxis_labels, '3')
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_3', 'actual')
        
        """
            Step 04 : Highlight "Revenue" > Right mouse click > "Sort" > Ascending".
        """
        metaobj.querytree_field_click('Revenue', 1, 1,'Sort','Sort','Ascending')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(9)", 1,60,string_value='Revenue')
        time.sleep(3)
        
        """
            Step 05 : Verify the following chart is displayed.
        """
        expected_xaxis_labels_2=['Video Production', 'Televisions', 'Computers', 'Accessories', 'Camcorder', 'Media Player', 'Stereo Systems']
        verify_chart_output('TableChart_1', expected_xaxis_labels_2, '5')
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_5', 'actual')
        
        """
            Step 06 : Click "Run".
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        resultobj.wait_for_property("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", 1,30,string_value='Product Category')
        time.sleep(2)
        
        """
            Step 07 : Verify the following chart is displayed.
        """
        verify_chart_output('jschart_HOLD_0', expected_xaxis_labels_2, '7')
        expected_tooltip=['Product Category:Accessories', 'Revenue:$129,608,338.53']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g3!mbar!',expected_tooltip, 'Step 07.6 : Verify chart tooltip value for Accessories riser')
        utillobj.switch_to_default_content(3)
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_7', 'actual')
        
        """
            Step 08 : Click "IA" > "Save" > "C2022172" > "Save".
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
            Step 09 : Dismiss the tool window.
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 10 : Highlight "C2022172" > Right mouse click > "Edit With..." > "InfoAssist+".
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'Chart', 'S10032_chart_1',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#TableChart_1 text[class='xaxisOrdinal-title']", 1,40,string_value='Product Category')
        time.sleep(2)
        
        """
            Step 11 : Verify the following chart is displayed.
        """
        verify_chart_output('TableChart_1', expected_xaxis_labels_2, '11')
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_11', 'actual')

if __name__=='__main__' :
    unittest.main()