'''
Created on 21-Dec-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228176
TestCase Name = Verify Chart with Auto Drill (82xx)
'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon

class C2228176_TestClass(BaseTestCase):

    def test_C2228176(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2228176"
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        def verify_chart_output(parent_id, xaxis_title, xaxis_labels, yaxis_labels, total_risers, riser_class, step_no):
            resultobj.verify_xaxis_title(parent_id, xaxis_title, 'Step '+step_no+'.1: Verify X-Axis title')
            resultobj.verify_yaxis_title(parent_id, 'DEALER_COST', 'Step '+step_no+'.2: Verify Y-Axis title')
            resultobj.verify_riser_chart_XY_labels(parent_id, xaxis_labels, yaxis_labels, 'Step '+step_no+'.3:',20)
            resultobj.verify_number_of_riser(parent_id, 1, total_risers, 'Step '+step_no+'.4: Verify number of chart risers')
            utillobj.verify_chart_color(parent_id, riser_class, 'bar_blue', 'Step '+step_no+'.5: Verify chart riser color')

        
        """ Step 1: Launch WF, New > Chart with CAROLAP.MAS.
        """
        utillobj.infoassist_api_login('chart','ibisamp/carolap','P292/S10032_chart_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1 text", 16, expire_time=25)    
          
        """ Step 2: Double click "DEALER_COST".
        """
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        parent_css = "#TableChart_1 text.yaxis-title"
        resultobj.wait_for_property(parent_css, 0, expire_time=25, string_value='DEALER_COST', with_regular_exprestion=True)    
          
        """ Step 3: Expand COUNTRY Dimension > double click "COUNTRY".
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        parent_css = "#TableChart_1 text.xaxisOrdinal-title"
        resultobj.wait_for_property(parent_css, 0, expire_time=25, string_value='COUNTRY', with_regular_exprestion=True)    
          
        """ Step 4: Select "Format" > "Auto Drill" button.
        """
        time.sleep(1)
        vis_ribbonobj.select_ribbon_item('Format', 'Auto_Drill')
        time.sleep(3)
        xaxis_labels=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        verify_chart_output('TableChart_1', 'COUNTRY', xaxis_labels, yaxis_labels, 5, 'riser!s0!g2!mbar', '4')
          
        """ Step 5: Click "IA" > "Save As" > "C2021069" > "Save".
        """
        time.sleep(2)
        vis_ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
          
        """ Step 6: Dismiss the tool window.
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """ Step 7: Highlight "C2021069" > Right mouse click > "Run".
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10032_chart_1', 'mrid', 'mrpass')
        parent_css = "iframe[src*='contentDrill']"
        resultobj.wait_for_property(parent_css, 1, expire_time=25)
        
        """ Step 8: Hover over "ITALY" riser > verify Tooltip menu.
        """
        utillobj.switch_to_frame(frame_css="iframe[src*='contentDrill']", frame_height_value=0)
        parent_css = "#jschart_HOLD_0 text.xaxisOrdinal-title"
        resultobj.wait_for_property(parent_css, 0, expire_time=25, string_value='COUNTRY', with_regular_exprestion=True)
        xaxis_labels=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        verify_chart_output('jschart_HOLD_0', 'COUNTRY', xaxis_labels, yaxis_labels, 5, 'riser!s0!g2!mbar', '8')
        expected_tooltip_list=['COUNTRY:ITALY', 'DEALER_COST:41,235', 'Drill down to CAR']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g2!mbar', expected_tooltip_list, "Step 8.6: verify 'ITALY' riser Tooltip menu.")
        
        """ Step 9: Select "Drill down to CAR",
        """
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g2!mbar', 'Drill down to CAR')
        parent_css = "#jschart_HOLD_0 text.xaxisOrdinal-title"
        resultobj.wait_for_property(parent_css, 0, expire_time=25, string_value='CAR', with_regular_exprestion=True) 
        
        """ Step 10: Verify the following chart is displayed.
        """
        xaxis_labels=['ALFA ROMEO', 'MASERATI']
        yaxis_labels=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        verify_chart_output('jschart_HOLD_0', 'CAR', xaxis_labels, yaxis_labels, 2, 'riser!s0!g1!mbar', '10')
        resultobj.verify_drilldown_navigation_menu('foreignObject div', ['Home','->','ITALY'], 'Step 10.6 : Verify drilldown navigation menu')
        
        """ Step 11: Hover over "MASERATI" riser > verify Tooltip menu.
        """
        expected_tooltip_list=['CAR:MASERATI', 'DEALER_COST:25,000', 'Restore Original', 'Drill up to COUNTRY', 'Drill down to MODEL']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g1!mbar', expected_tooltip_list, "Step 11: verify 'MASERATI' riser Tooltip menu.")
        
        """ Step 12" Select "Drill Down to MODEL".
        """
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g1!mbar', 'Drill down to MODEL')
        parent_css = "#jschart_HOLD_0 text.xaxisOrdinal-title"
        resultobj.wait_for_property(parent_css, 0, expire_time=25, string_value='MODEL', with_regular_exprestion=True) 
        
        """ Step 13: Hover over "DORA 2 DOOR" riser > verify Tooltip menu.
        """
        xaxis_labels=['DORA 2 DOOR']
        yaxis_labels=['0', '5K', '10K', '15K', '20K', '25K', '30K']
        verify_chart_output('jschart_HOLD_0', 'MODEL', xaxis_labels, yaxis_labels, 1, 'riser!s0!g0!mbar', '13')
        resultobj.verify_drilldown_navigation_menu('foreignObject div', ['Home','->','ITALY','->','MASERATI'], 'Step 13.6 : Verify drilldown navigation menu')
        
        """ Step 14: Select "Restore Original".
        """
        resultobj.select_drilldown_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!', 'Restore Original')
        parent_css = "#jschart_HOLD_0 text.xaxisOrdinal-title"
        resultobj.wait_for_property(parent_css, 0, expire_time=25, string_value='COUNTRY', with_regular_exprestion=True) 
        
        """ Step 15: Verify the following chart is displayed.
        """
        xaxis_labels=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        verify_chart_output('jschart_HOLD_0', 'COUNTRY', xaxis_labels, yaxis_labels, 5, 'riser!s0!g2!mbar', '15')
        expected_tooltip_list=['COUNTRY:ENGLAND', 'DEALER_COST:37,853', 'Drill down to CAR']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0', 'riser!s0!g0!mbar', expected_tooltip_list, "Step 15.6: verify riser Tooltip menu.")
        
        """ Step 16: Dismiss the tool window.
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()