'''
Created on Sept 25, 2018

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6678133
Test case Name =  Create a Map with Multi-Graph field
'''
import unittest
from common.pages import  ia_resultarea
from common.lib import utillity 
from common.lib.core_utility import CoreUtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization,chart
from common.lib import base



class C6778133_TestClass(BaseTestCase):

    def test_C6778133(self):
        
        visual_obj = visualization.Visualization(self.driver)
        chart_obj = chart.Chart(self.driver)
        base_obj = base.BasePage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj=CoreUtillityMethods(self.driver)
        x_axis_css = "svg g text[class*='mgroupLabel']"
        y_axis_css= "svg g text[class*='yaxis-labels']"
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        project_id = util_obj.parseinitfile('project_id')
        suite_id = util_obj.parseinitfile('suite_id')
        
        '''    TESTCASE ID Variable    '''
        Test_Case_ID = "C6778133"
        
        '''    1. Launch the IA API with Chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS11397&tool=chart&master=jsonmaps/south_america   '''
        chart_obj.invoke_chart_tool_using_api('jsonmaps/south_america', folder_path=project_id+'/'+suite_id)
         
        '''    2. Add fields "ISO_A2", "RANDOM_NUMBER"    '''
        chart_obj.double_click_on_datetree_item('ISO_A2', 1)
        chart_obj.wait_for_number_of_element(x_axis_css,13,base_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('RANDOM_NUMBER', 1)
        visual_obj.wait_for_number_of_element(y_axis_css, 7, base_obj.chart_short_timesleep)
          
        '''    3. Drag/drop "COUNTRY_NAME" in "Multi-graph" bucket    '''
        visual_obj.drag_field_from_data_tree_to_query_pane('COUNTRY_NAME', 1, 'Multi-graph')
        chart_obj.wait_for_number_of_element(x_axis_css, 1, base_obj.chart_short_timesleep)
          
          
        '''    4. Select Format tab    '''
        '''    5. Click "Other" > "Map"  '''
        visual_obj.select_ribbon_item("Format", "Other")
        ok_button_css="#qbSelectChartTypeDlgOkBtn"
        visual_obj.wait_for_number_of_element(ok_button_css, 1, base_obj.chart_short_timesleep)
         
        '''    6. Select "Leaflet Choropleth"    '''
        chart_obj.select_other_chart_type('map', 'leaflet_choropleth', 3,close_dialog='no')
        combo_css = "div[id^='SelectChartTypeDlg'] div[id^='RightPane'] div[id^='BiButton']"
        combo_button_obj = util_obj.validate_and_get_webdriver_object(combo_css, "Combo_css")
         
        '''    7. Select 'South America' Territory > OK    '''
        util_obj.select_any_combobox_item(combo_button_obj, 'South America')
        ok_btn_css="div[id='qbSelectChartTypeDlgOkBtn']"
        util_obj.validate_and_get_webdriver_object(ok_btn_css, "ok_button_css").click()
 
        '''   8. Select "iso_a2" from Geographic Role dropdown > OK    '''
        util_obj.synchronize_with_number_of_element("div[id^='QbDialog'] div[id$='geoRoleComboBox'] div[id^='BiButton'] ", 1,190)
        visual_obj.set_geo_role_location(role_name='iso_a2 (AR, BO, BR)', btn_click='Ok')
          
        '''    9. Verify Preview   '''
          
        visual_obj.wait_for_number_of_element("#pfjTableChart_1 path[class^='riser!s0!g0!mstate!']",1,base_obj.chart_short_timesleep)
        chart_obj.verify_color_scale_esri_maps_in_preview(['RANDOM_NUMBER', '540', '546.3', '552.5', '558.8', '565'], "Step 9a Colour scale", "pfjTableChart_1")
        visual_obj.verify_chart_color_using_get_css_property("path[class*=\"riser!s0!g0!mstate!\"]", 'persian_red', msg='Step 9b Verify map color',parent_css="#pfjTableChart_1")
                                   
        '''    10. Click "Save" icon    '''
        '''    11. Save fex as "C2229110"    '''
        visual_obj.save_as_visualization_from_menubar(Test_Case_ID)
         
        '''    12. Logout:    '''
        visual_obj.logout_visualization_using_api()
         
        '''    13. Reopen fex using IA API:    '''
        visual_obj.edit_visualization_using_api(Test_Case_ID)
        
        '''    14. Verify the map is restored    '''
        visual_obj.wait_for_number_of_element("#pfjTableChart_1 path[class^='riser!s0!g0!mstate!']",1,base_obj.chart_short_timesleep)
        chart_obj.verify_color_scale_esri_maps_in_preview(['RANDOM_NUMBER', '540', '546.3', '552.5', '558.8', '565'], "Step 14a Colour Scale", "pfjTableChart_1")
        iaresult.verify_color_scale_esri_maps("pfjTableChart_1", ['RANDOM_NUMBER', '540', '546.3', '552.5', '558.8', '565'], "Step 14a) colour scale")
        visual_obj.verify_chart_color_using_get_css_property("path[class*=\"riser!s0!g0!mstate!\"]", 'persian_red', msg='Step 14b) Verify map color',parent_css="#pfjTableChart_1")
         
        '''    15. Click Run    '''
        visual_obj.run_visualization_from_toptoolbar()
        visual_obj.switch_to_frame()

        '''    16. Verify output displays a chart for each country    '''
        visual_obj.wait_for_number_of_element("#jschart_HOLD_0 path[class^='riser!s0!g0!mstate!']",1,base_obj.chart_short_timesleep)
        chart_obj.verify_color_scale_esri_maps_in_preview(['RANDOM_NUMBER', '540', '546.3', '552.5', '558.8', '565'], "Step 16a Colour Scale", "jschart_HOLD_0")
        visual_obj.verify_chart_color_using_get_css_property("path[class*=\"riser!s0!g0!mstate!\"]", 'persian_red', msg='Step 16b) Verify map color',parent_css="#jschart_HOLD_0")
        total_charts = len(util_obj.validate_and_get_webdriver_objects("div[id^='jschart_HOLD'][class='chart']", "Total Charts"))
        util_obj.asequal(total_charts,13,'Step 16c) Verify output displays a chart for each country ')


if __name__ == '__main__':
    unittest.main()
    