'''
Created on Nov 20, 2017

@author: Praveen Ramkumar
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234975
TestCase Name =ID:Script error with field in Vertical Axis and Rows/Columns Matrix (167569)
'''
import unittest
from common.wftools import visualization
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.pages.visualization_resultarea import Visualization_Resultarea

class C2234975_TestClass(BaseTestCase):

    def test_C2234975(self):
        
        """
            TESTCASE VARIABLES
        """     
        visual_obj = Visualization_Resultarea(self.driver)
        visual = visualization.Visualization(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            Step 01:Create new Visualization with car
        """
        visual.invoke_visualization_using_api('ibisamp/car')
         
        """
            Step 02:Double-click Sales to add field to Vertical Axis
        """
        visual.double_click_on_datetree_item('SALES', 1)
        parent_css="#queryTreeWindow"
        visual.wait_for_visible_text(parent_css, 'SALES')
        
        """
            Step 03:Drag/drop Country to Columns in Matrix bucket
        """
        visual.drag_field_from_data_tree_to_query_pane('COUNTRY', 1, 'Columns')
        visual.wait_for_visible_text(parent_css, 'COUNTRY')

        """
            Step 04:Drag/drop Car to Rows in Matrix bucket
        """
        visual.drag_field_from_data_tree_to_query_pane('CAR', 1, 'Rows')
        visual.wait_for_visible_text('#MAINTABLE_wbody1', 'CAR')
        
        """
        Step 04.00: Verify no script error appears.

        Live Preview:
        """
        parent_css= "#MAINTABLE_wbody1_f text[class^='yaxis'][class$='title']"
        visual.wait_for_visible_text(parent_css, 'SALES')
        title_number = utils.validate_and_get_webdriver_objects(parent_css, 'number of title')
        utils.asequal(len(title_number), 10, 'Step 04.01 : Verify y axis title')
        expected_yaxis_label= ['0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 04.02', xyz_axis_label_length=4)
        visual.verify_chart_color_using_get_css_property('[class="riser!s0!g0!mbar!r0!c2!"]', "bar_blue", msg='Step 04.03 ')
        expected_label_list = ['CAR']
        visual_obj.verify_xy_axis_title(expected_label_list, parent_css='#MAINTABLE_wbody1_f', x_or_y_axis_title_css=' g[class="scrollRowTitle"]', msg='Step 04.04 : Verify scroll row title ')
        expected_label_list = ['COUNTRY']
        visual_obj.verify_xy_axis_title(expected_label_list, parent_css='#MAINTABLE_wbody1_f', x_or_y_axis_title_css=' g[class="scrollColTitle-clip"]', msg='Step 04.05 : Verify scroll column title ')
        expected_label_list = ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        visual_obj.verify_xy_axis_title(expected_label_list, parent_css='#MAINTABLE_wbody1_f', x_or_y_axis_title_css=' [class*="colLabel"]', msg='Step 04.06 : Verify scroll column label')
        expected_yaxis_label = ['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR']
        visual_obj.verify_xyz_labels(expected_yaxis_label,parent_css='#MAINTABLE_wbody1_f',  xyz_axis_label_css=' [class*="rowLabel"]', msg='Step 04.07 : Verify scroll row label', xyz_axis_label_length=4)
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 10, 'Step 04.08')
                
        """
        Run View:
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        parent_css= "#MAINTABLE_wbody1_f text[class^='yaxis'][class$='title']"
        visual.wait_for_visible_text(parent_css, 'SALES')
        title_number = utils.validate_and_get_webdriver_objects(parent_css, 'number of title')
        utils.asequal(len(title_number), 10, 'Step 04.09 : Verify y axis title')
        expected_yaxis_label= ['0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K', '', '', '', '60K', '80K', '100K', '', '', '', '', '', '']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 04.10', xyz_axis_label_length=4)
        visual.verify_chart_color_using_get_css_property('[class="riser!s0!g0!mbar!r0!c2!"]', "bar_blue", msg='Step 04.11 ')
        expected_label_list = ['CAR']
        visual_obj.verify_xy_axis_title(expected_label_list, parent_css='#MAINTABLE_wbody1_f', x_or_y_axis_title_css=' g[class="scrollRowTitle"]', msg='Step 04.12 : Verify scroll row title ')
        expected_label_list = ['COUNTRY']
        visual_obj.verify_xy_axis_title(expected_label_list, parent_css='#MAINTABLE_wbody1_f', x_or_y_axis_title_css=' g[class="scrollColTitle-clip"]', msg='Step 04.13 : Verify scroll column title ')
        expected_label_list = ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        visual_obj.verify_xy_axis_title(expected_label_list, parent_css='#MAINTABLE_wbody1_f', x_or_y_axis_title_css=' [class*="colLabel"]', msg='Step 04.14 : Verify scroll column label ')
        expected_yaxis_label = ['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR']
        visual_obj.verify_xyz_labels(expected_yaxis_label,parent_css='#MAINTABLE_wbody1_f',  xyz_axis_label_css=' [class*="rowLabel"]', msg='Step 04.15 : Verify scroll row label', xyz_axis_label_length=4)
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 10, 'Step 04.16')
        visual.switch_to_previous_window()
          
if __name__ == '__main__':
    unittest.main()