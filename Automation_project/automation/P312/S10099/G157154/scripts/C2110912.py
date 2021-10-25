'''
Created on March 1, 2018

@author: Sowmiya
TestSuite ID : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10099
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2110912
TestCase Name: Cannot exclude a value on chart when a filter on a Measure exists (Runtime only)
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2110912_TestClass(BaseTestCase):

    def test_C2110912(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2110912'
        visual = visualization.Visualization(self.driver)
        position=1
        
        def verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, total_risers, stepno):        
            visual.verify_x_axis_title(x_axis_title, msg='Step '+stepno+'.01')
            visual.verify_y_axis_title(y_axis_title, msg='Step '+stepno+'.02')
            visual.verify_x_axis_label(x_axis_label, xyz_axis_label_length=10, msg='Step '+stepno+'.03')
            visual.verify_y_axis_label(y_axis_label, msg='Step '+stepno+'.04')
            visual.verify_number_of_risers("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 1, total_risers, msg='Step '+stepno+'.05')
            visual.verify_chart_color_using_get_css_property("[class='"+riser_css+"']", color_name, msg='Step '+stepno+'.06')
            visual.verify_tooltip(riser_css, tooltip_list, msg='Step '+stepno+'.07 :'+' Verify tooltip')
    
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                    http://domain.com:port/alias/ia?item=IBFS:/WFC/Repository/S10099/C2102820_Repro.fex&tool=idis
        """      
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02 : Double click "Cost of Goods", "Product,Category" 
        """
        field_name='Cost of Goods'
        visual.double_click_on_datetree_item(field_name, position)
        element_css="#MAINTABLE_wbody1_f svg g text[class^='yaxis-labels']"
        visual.wait_for_number_of_element(element_css, expected_number=9)
        
        field_name='Product,Category'
        visual.double_click_on_datetree_item(field_name, position)
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal']"
        visual.wait_for_number_of_element(element_css, expected_number=8)
        
        x_axis_title=['Product Category']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        total_risers=7
        color_name='bar_blue'
        camcord_tooltip_list=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        camcord_riser_css='riser!s0!g1!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, camcord_tooltip_list, camcord_riser_css, color_name, total_risers, '02')
        
        """
        Step 03 : Right click "Cost of Goods" > "Filter values"
        """
        field_name='Cost of Goods'
        visual.right_click_on_field_under_query_tree(field_name, position, 'Filter Values...')
        element_css="[class^='bi-window active window ']"
        visual.wait_for_number_of_element(element_css, expected_number=1)
        
        """
        Step 04 : Click OK in the Filter dialog
        """
        visual.close_filter_dialog('ok')
        
        element_css="div[id='Prompt_1'] div[class^='ui-slider ui']"
        visual.wait_for_number_of_element(element_css, expected_number=1)
        
        visual.verify_field_in_filterbox('Cost of Goods', position, msg='Step 04.01')
        
        """
        Step 05 : Click "Run"
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        x_axis_title=['Product Category']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        total_risers=7
        color_name='bar_blue'
        camcord_tooltip_list=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        camcord_riser_css='riser!s0!g1!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, camcord_tooltip_list, camcord_riser_css, color_name, total_risers, '05')
        
        """
        Step 06 : Hover over "Media Player" riser >
        Step 07 : Click "Exclude from Chart"
        """
        media_riser='riser!s0!g3!mbar!'
        visual.select_tooltip(media_riser,'Exclude from Chart')
        
        """
        Step 08 : Verify 'Media Player' is no more selected value and BAR
        """
        x_axis_title=['Product Category']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories', 'Camcorder', 'Computers', 'Stereo Systems', 'Televisions', 'Video Production']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        total_risers=6
        color_name='bar_blue'
        camcord_tooltip_list=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill down to Product Subcategory']
        camcord_riser_css='riser!s0!g1!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, camcord_tooltip_list, camcord_riser_css, color_name, total_risers, '08')
        
        """
        Step 09 : Close run window
        """
        visual.switch_to_previous_window()
        
        """
        Step 10 : Logout using API(without saving)
                    http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
#         visual.logout_visualization_using_api()   
        
if __name__ == '__main__':
    unittest.main() 