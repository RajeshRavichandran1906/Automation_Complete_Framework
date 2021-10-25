"""-------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 10-September-2019
-------------------------------------------------------------"""

from common.wftools.visualization import Visualization
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods

class C9693767_TestClass(BaseTestCase):
    
    def test_C9693767(self):
        
        """
            CLASS OBJECTS
        """
        visual = Visualization(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            VARIABLES
        """
        case_id = 'C9693767'
        default_chart_css = "#pfjTableChart_1"
        riser = "riser!s0!g5!mregion!"
        riser_css = "#MAINTABLE_wbody1_f path[class='{0}']".format(riser)
        tooltip = ['Store Country:Canada', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        msg = "Step {0} : Verify {1} tooltip displayed"
        
        """
            STEP 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S11397%2FG435181%2F&master=baseapp%2Fwf_retail_lite&tool=idis
        """
        visual.invoke_visualization_using_api("baseapp/wf_retail_lite")
        visual.wait_for_visible_text(default_chart_css, "Drop", visual.chart_long_timesleep)
        
        """
            STEP 02 : Select change drop down > ESRI Choropleth.
        """
        visual.change_chart_type("choropleth_map")
        visual.wait_for_visible_text(default_chart_css, "Esri", visual.chart_medium_timesleep)
        
        """
            STEP 03 : Double click "Store,Country"
        """
        visual.double_click_on_datetree_item('Store,Country', 1)
        utils.synchronize_until_element_is_visible(riser_css, visual.chart_medium_timesleep)
        
        """
            STEP 04 : Hover over ESRI display Drilldown options in tooltip
            It displays tooltip values
        """
        visual.verify_tooltip(riser, tooltip, msg.format("04.01", tooltip), yoffset=-100, xoffset=20)
        
        """
            STEP 05 : Click Save in the toolbar > Enter title as "C9693767" > Click Save.
        """
        visual.save_visualization_from_top_toolbar(case_id)
        
        """
            STEP 06 : Logout using API
        """
        visual.logout_visualization_using_api()
        
        """
            STEP 07 : Restore the C9693767.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?is508=false&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29835%2FG840059%2FC9693767.fex
        """
        visual.edit_visualization_using_api(case_id)
        utils.synchronize_until_element_is_visible(riser_css, visual.chart_medium_timesleep)
        
        """
            STEP 08 : Hover over ESRI map it displaying Drill options in tooltip
        """
        visual.verify_tooltip(riser, tooltip, msg.format("08.01", tooltip), yoffset=-100, xoffset=20)
        
        """
            STEP 09 : Logout using API
        """