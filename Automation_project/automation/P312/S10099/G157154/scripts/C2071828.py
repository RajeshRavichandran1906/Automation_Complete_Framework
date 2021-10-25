'''
Created on Feb 27, 2018

@author: Sowmiya
TestSuite ID : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10099
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2102820
TestCase Name: Hiding the Visibility with 2 dimensions, doesn't display correct output
'''
import unittest
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.pages.core_metadata import CoreMetaData

class C2071828_TestClass(BaseTestCase):

    def test_C2071828(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2071828'
        visual = visualization.Visualization(self.driver)
        core_meta = CoreMetaData(self.driver)
        position=1
        
        def verify_map(legend_list, riser_css, color_name, stepno):
            visual.verify_legends(legend_list, msg='Step '+stepno+'.01 : Verify the legends')
            visual.verify_chart_color_using_get_css_property("path[class='"+riser_css[0]+"']", color_name[0], msg='Step '+stepno+'.02'+' Verify riser color')
            visual.verify_chart_color_using_get_css_property("path[class='"+riser_css[1]+"']", color_name[1], msg='Step '+stepno+'.03'+' Verify riser color')
        
        """
        Step 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                    http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10099&tool=idis&master=baseapp/wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02 : Click "Change" dropdown > "Map"
        Step 03 : Click OK in "Select a Map" dialog
        """
        visual.change_chart_type('map')
        visual.select_map_dialog(map_type=None, teritory_name=None, close_dialog='ok')
        
        """
        Step 04 : Double click "Cost of Goods"
        """
        field_name='Cost of Goods'
        visual.double_click_on_datetree_item(field_name, position)
        element_css="#pfjTableChart_1  a[class^='leaflet-control-layers-toggle']"
        visual.wait_for_number_of_element(element_css, expected_number=position)
        
        """
        Step 05 : Double click "Store,State,Province"
        """
        core_meta.collapse_data_field_section('Filters and Variables')
        field_name='Store,State,Province'
        visual.double_click_on_datetree_item(field_name, position)
        
        """
        Step 06 : Select "State name" from Geographic Role dropdown > OK
        """
        visual.set_geo_role_location(role_name='state_name (Alabama, Alaska, Arizona)', btn_click='Ok')
        element_css="#MAINTABLE_wbody1_f [class^='colorScale-labe']"
        visual.wait_for_number_of_element(element_css, expected_number=5)
        
        """
        Step 07 : Verify following Leaflet map displayed
        """
        legend_list=['Cost of Goods', '0M', '59M', '117.8M', '176.7M', '235.6M']
        riser_css=['riser!s0!g46!mstate!','riser!s0!g25!mstate!']
        color_name=['punch','elf_green']
        verify_map(legend_list, riser_css, color_name, '07')
            
        """
        Step 08 : Click "Pan" in the map component
        """
        pan_css="#MAINTABLE_1 button[class^='data-s']"
        pan_elem=self.driver.find_element_by_css_selector(pan_css)
        pan_elem.click()
        
        """
        Step 09 : Lasso values in map.
        """
        source_element="#MAINTABLE_wbody1_f svg g path[class='riser!s0!g1!mstate!']"
        source=self.driver.find_element_by_css_selector(source_element)
        target_element="#MAINTABLE_wbody1_f svg g path[class='riser!s0!g25!mstate!']"
        target=self.driver.find_element_by_css_selector(target_element)
        visual.create_lasso(source, target, source_xoffset=-20, source_yoffset=-10, target_xoffset=10, target_yoffset=10, source_element_location='top_left', target_element_location='middle')
#         element_css="div[class='tdgchart-tooltip'] span"
#         visual.wait_for_number_of_element(element_css, expected_number=4)
        
        """
        Step 10 : Verify the updated preview after lasso, tooltip displayed
        """
        expected_tooltip_list=['4 points', 'Filter Chart', 'Exclude from Chart', 'Group Store,State,Province Selection']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg='Step 10.01')
        
#         visual.take_preview_snapshot(Test_Case_ID,'10')
        
        """
        Step 11 : Logout using API
                    http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()