'''
Created on Feb 27, 2018

@author: Sowmiya
TestSuite ID : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10099
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2227327
TestCase Name: Filter is applied to run time Grid option of Chart
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.pages import visualization_resultarea

class C2227327_TestClass(BaseTestCase):

    def test_C2227327(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227327'
        restore_fex='C2227327_Repro'
        visual = visualization.Visualization(self.driver)
        position=1
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        def verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, total_risers, stepno):        
            visual.verify_x_axis_title(x_axis_title, msg='Step '+stepno+'.1'+' Verify x_axis title')
            visual.verify_y_axis_title(y_axis_title, msg='Step '+stepno+'.2'+' Verify y_axis title')
            visual.verify_x_axis_label(x_axis_label, xyz_axis_label_length=10, msg='Step '+stepno+'.3'+' Verify x_axis label')
            visual.verify_y_axis_label(y_axis_label, msg='Step '+stepno+'.4'+' Verify y_axis label')
            visual.verify_number_of_risers("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 1, total_risers, msg='Step '+stepno+'.5'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("[class='"+riser_css+"']", color_name, msg='Step '+stepno+'.6'+' Verify riser color')
            visual.verify_tooltip(riser_css, tooltip_list, msg='Step '+stepno+'.7'+' Verify tooltip')
    
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                    http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/S10099/C2227327.Repro.fex&tool=idis
        """      
        visual.edit_visualization_using_api(restore_fex)
        
        """
        Step 02 : Verify the following chart is displayed
        """
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal-label']"
        visual.wait_for_number_of_element(element_css, expected_number=7)
        
        x_axis_title=['Product Category']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        total_risers=7
        color_name='bar_blue'
        camcorder_tooltip_list=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        camcorder_riser_css='riser!s0!g1!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, camcorder_tooltip_list, camcorder_riser_css, color_name, total_risers, '2')
        
        """
        Step 03 : Hover over any riser, select 'Filter Chart'
        """        
        #media_player_css='riser!s0!g3!mbar!'
        #visual.select_tooltip(media_player_css, 'Filter Chart')
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', 'riser!s0!g3!mbar!','Filter Chart')
        
        """
        Step 04 : Verify filter applied correctly
        """
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal-label']"
        visual.wait_for_number_of_element(element_css, expected_number=1)
        
        x_axis_title=['Product Category']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Media Player']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M']
        total_risers=1
        color_name='bar_blue'
        media_player_tooltip=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Drill down to Product Subcategory']
        media_player_css='riser!s0!g0!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, media_player_tooltip, media_player_css, color_name, total_risers, '4')
        
        field_name='Product,Category'
        visual.verify_field_in_filterbox(field_name, position, msg='Step 4.8')
        
        """
        Step 05 : Click "Run". Expand menu in the lower right corner, select Grid icon
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal-label']"
        visual.wait_for_number_of_element(element_css, expected_number=1)
        
        x_axis_title=['Product Category']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Media Player']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M']
        total_risers=1
        color_name='bar_blue'
        media_player_tooltip=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Drill down to Product Subcategory']
        media_player_css='riser!s0!g0!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, media_player_tooltip, media_player_css, color_name, total_risers, '5')
        
        visual.select_bottom_right_run_menu_options('show_report_css')
        
        """
        Step 06 : Verify filter applied to Grid at Runtime
        """
#         visual.create_visualization_tabular_report(Test_Case_ID+'_Ds_01.xlsx')
        visual.verify_visualization_tabular_report(Test_Case_ID+'_Ds_01.xlsx', msg='Step 6.1:')
        visual.switch_to_previous_window()
        
        """
        Step 07 : Launch the IA API to logout.
                    http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
#         visual.logout_visualization_using_api()
        
if __name__ == '__main__':
    unittest.main() 