"""-------------------------------------------------------------
Author Name : Prabhakaran
Automated on : 26-September-2019
-------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.pages.core_metadata import CoreMetaData
from common.wftools.visualization import Visualization

class C9926879_TestClass(BaseTestCase):

    def test_C9926879(self):
        
        """
            CLASS OBJECTS
        """
        core_met = CoreMetaData(self.driver)
        visual = Visualization(self.driver)
        
        """
            VARIABLES
        """
        case_id = "C9926879"
        default_preview_css = "#pfjTableChart_1"
        preview_css = "#MAINTABLE_wbody1"
        riser1_css = "path[class='riser!s0!g33!mregion!']"
        riser2_css = "path[class='riser!s0!g13!mregion!']"
        legends = ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        query_fields = ['Choropleth Map1', 'Location', 'Layer', 'Store,Country', 'Metric', 'Color', 'Revenue', 'Tooltip']
        
        """
            STEP 01 : Launch IA Visualization using wfretail.mas in developer user
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29835%2FG840058%2F&master=baseapp%2Fwf_retail_lite&tool=idis
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        visual.wait_for_visible_text(default_preview_css, "Drop", visual.chart_long_timesleep)
        
        """
            STEP 02 : Click Change visual drop down > Click ESRI Choropleth Map
        """
        visual.change_chart_type('choropleth_map')
        visual.wait_for_visible_text(default_preview_css, "Esri", visual.chart_medium_timesleep)
        
        """
            STEP 03 : Double click "Revenue" and "Store,Country"
        """
        visual.double_click_on_datetree_item('Revenue', 1)
        visual.wait_for_visible_text('#queryTreeColumn', "Revenue", visual.chart_long_timesleep)
        core_met.collapse_data_field_section('Filters and Variables')
        visual.double_click_on_datetree_item('Store,Country', 1)
        visual.wait_for_visible_text(preview_css, "Revenue", visual.chart_long_timesleep)
        
        """
            STEP 03 - Expected : Fields added to query pane and canvas updated.
        """
        visual.wait_for_number_of_element(preview_css + " path[class^='riser']", 34, visual.chart_long_timesleep)
        visual.verify_legends(legends, msg="Step 03.01")
        visual.verify_number_of_risers(preview_css + " path", 1, 34, msg="Step 03.02")
        visual.verify_chart_color_using_get_css_property(riser1_css, 'elf_green', msg="Step 03.03 ")
        visual.verify_chart_color_using_get_css_property(riser2_css, 'persian_red3', msg="Step 03.04 ")
        visual.verify_all_fields_in_query_pane(query_fields, "Step 03.05 : Verify fields added to query")
        
        """
            STEP 04 : Click Run button
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_visible_text(preview_css, "Revenue", visual.chart_long_timesleep)
        
        """
            STEP 04 - Expected : Map displayed in run time 
        """
        visual.wait_for_number_of_element(preview_css + " path[class^='riser']", 34, visual.chart_long_timesleep)
        visual.verify_legends(legends, msg="Step 04.01")
        visual.verify_number_of_risers(preview_css + " path", 1, 34, msg="Step 04.02")
        visual.verify_chart_color_using_get_css_property(riser1_css, 'elf_green', msg="Step 04.03 ")
        visual.verify_chart_color_using_get_css_property(riser2_css, 'persian_red3', msg="Step 04.04 ")
        
        """
            STEP 05 : Close the output window
        """
        visual.switch_to_previous_window()
        
        """
            STEP 06 : Click Save icon in the toolbar > Enter title as "C9926879" > Click Save button.
        """
        visual.save_visualization_from_top_toolbar(case_id)
        
        """
            STEP 07 : Launch the IA API to logout
        """
        visual.logout_visualization_using_api()
        
        """
            STEP 08 : Restore C9926879.fex using API 
        """
        visual.edit_visualization_using_api(case_id)
        visual.wait_for_visible_text(preview_css, "Revenue", visual.chart_long_timesleep)
        
        """
            STEP 08 - Expected : Map restored successfully without error.
        """
        visual.wait_for_number_of_element(preview_css + " path[class^='riser']", 34, visual.chart_long_timesleep)
        visual.verify_legends(legends, msg="Step 08.01")
        visual.verify_number_of_risers(preview_css + " path", 1, 34, msg="Step 08.02")
        visual.verify_chart_color_using_get_css_property(riser1_css, 'elf_green', msg="Step 08.03 ")
        visual.verify_chart_color_using_get_css_property(riser2_css, 'persian_red3', msg="Step 08.04 ")
        visual.verify_all_fields_in_query_pane(query_fields, "Step 08.05 : Verify fields added to query")
        
        """
            STEP 09 : Launch the IA API to logout
        """