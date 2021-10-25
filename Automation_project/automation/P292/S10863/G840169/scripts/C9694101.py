"""------------------------------------------------------------------------
Author Name : Prabhakaran.
Automated On : 24-August-2019
------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.visualization import Visualization

class C9694101_TestClass(BaseTestCase):

    def test_C9694101(self):
        
        """CLASS OBJECT"""
        visual = Visualization(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """COMMON VARIABLES"""
        chart_css = "#MAINTABLE_wbody1"
        case_id = "C9694101"
        x_axis_title = ['Product Category']
        y_axis_title = ['AVE Cost of Goods']
        y_axis_labels = ['0', '200', '400', '600', '800', '1,000']
        x_axis_labels = ['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
                        
        """
            STEP 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10863%2FG193338%2F&master=baseapp%2Fwf_retail_lite&tool=idis
        """
        visual.invoke_visualization_using_api("baseapp/wf_retail_lite")
        visual.wait_for_visible_text("#pfjTableChart_1", "Drop", 320)
        
        """
            STEP 02 : Double-click "Cost of Goods", located under Sales Measures
        """
        visual.double_click_on_datetree_item("Cost of Goods", 1)
        visual.wait_for_visible_text(chart_css, "Cost of Goods", 120)
        
        """
            STEP 03 : Double-click "Product,Category", from Product Dimension
        """
        visual.double_click_on_datetree_item("Product,Category", 1)
        visual.wait_for_visible_text(chart_css, "Product Category", 120)
        
        """
            STEP 04 : Right-click "Cost of Goods" in the Query pane.
            The following options displayed in context menu.
        """
        expected_context_menu = ['Filter Values...', 'Sort', 'Visibility', 'Change Title...', 'Edit Format', 'Drill Down', 'More', 'Delete']
        visual.verify_query_field_context_menu("Cost of Goods", 1, expected_context_menu, "Step 04.01 : Verify 'Cost of Goods' filed context menu in query pane")
        chart = self.driver.find_element_by_css_selector(chart_css)
        core_utils.python_left_click(chart, "top_middle")
        
        """
            STEP 05 : Select "More > Aggregation Functions > Average"
            Selected aggregation is added in fields prefix and canvas updated.
        """
        visual.right_click_on_field_under_query_tree("Cost of Goods", 1, "More->Aggregation Functions->Average")
        visual.wait_for_visible_text(chart_css, "AVE Cost of Goods", 120)
        visual.verify_x_axis_title(x_axis_title, msg="Step 05.01")
        visual.verify_y_axis_title(y_axis_title, msg="Step 05.02")
        visual.verify_x_axis_label(x_axis_labels, msg="Step 05.03")
        visual.verify_y_axis_label(y_axis_labels, msg="Step 05.04")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 7, msg="Step 05.05")
        visual.verify_chart_color_using_get_css_property("rect[class*='riser!s0!g0!mbar']", "bar_blue",  msg="Step 05.06 ")
        
        """
            STEP 06 : Click Save in the toolbar > Enter title as "C9694101" > Click Save button.
        """
        visual.save_visualization_from_top_toolbar(case_id)
        
        """
            STEWP 07 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
            STEP 08 : Reopen C9694101.fex using IA API:
            http://domain.com:port/alias/ia?is508=false&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10863%2FG193338%2FC9694101.fex
            Chart restored successfully.
        """
        visual.edit_visualization_using_api(case_id)
        visual.wait_for_visible_text(chart_css, "AVE Cost of Goods", 320)
        visual.verify_x_axis_title(x_axis_title, msg="Step 08.01")
        visual.verify_y_axis_title(y_axis_title, msg="Step 08.02")
        visual.verify_x_axis_label(x_axis_labels, msg="Step 08.03")
        visual.verify_y_axis_label(y_axis_labels, msg="Step 08.04")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 7, msg="Step 08.05")
        visual.verify_chart_color_using_get_css_property("rect[class*='riser!s0!g0!mbar']", "bar_blue",  msg="Step 08.06 ")
        
        """
            STEP 09 : Logout
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """