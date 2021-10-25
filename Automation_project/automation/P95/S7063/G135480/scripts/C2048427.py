'''
Created on December 31, 2018

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2048427
TestCase Name = Creating a basic Active Technologies Chart.
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility
from common.wftools import active_chart
from common.wftools import chart
from common.lib import base
from common.pages import core_metadata
from common.lib import global_variables

class C2048427_TestClass(BaseTestCase):

    def test_C2048427(self):
        
        """
        Test case Object's
        """
        global_obj = global_variables.Global_variables()
        core_meta_obj = core_metadata.CoreMetaData(self.driver)
        base_obj = base.BasePage(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        """
        Test case variables
        """
        x_label = ['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_label = ['0', '20M', '40M', '60M', '80M', '100M']
        chart_title = "Gross Profit by Product Category"
        
        """
        Test case CSS
        """
        y_title_css = "#TableChart_1 g.chartPanel text[class^='yaxis-title']"
        x_title_css = "#pfjTableChart_1 text[class^='xaxis']"
        run_window_x_title_css = "#MAINTABLE_wbody0 text[class^='xaxis']"
        
        """ 
        Step 1: Sign in to WebFOCUS as a developer user
        http://machine:port/{alias}
        Step 2: Launch IA Chart using below API link
        http://machine:port/{alias}/iatool=Chart&master=baseapp/wf_retail&item=IBFS%3A%2FWFC%2F
        Repository%2FP95_S7063%2FG135480%2F
        """
        active_chart_obj.invoke_chart_tool_using_api('baseapp/wf_retail',mrid='mriddev',mrpass='mrpassdev')
        
        """
        Step 3 : On the Format tab, in the Output Types group, click Active report.
        Expect to see the following Chart development canvas.
        """
        chart_obj.change_output_format_type('active_report')
          
        """
        Step 4 : Select Gross Profit from the Sales group for the Vertical Axis field.
        Select Product,Category from the Product group for the Horizontal Axis field.
        """
        
        active_chart_obj.drag_field_from_data_tree_to_query_pane('Gross Profit', 1, 'Vertical Axis', 1)
        active_chart_obj.wait_for_number_of_element(y_title_css, 1, base_obj.chart_short_timesleep )
        core_meta_obj.expand_data_field_section('Product->Product')
        active_chart_obj.double_click_on_datetree_item('Product,Category', 1)
        active_chart_obj.wait_for_number_of_element(x_title_css, 8, base_obj.chart_short_timesleep)

        """
        Step 5: Click the Run button.
        Expect to see the following Vertical Bar Chart, with 7 Bars for the Product Category values.
        """        
        active_chart_obj.run_chart_from_toptoolbar()
        core_util_obj.switch_to_frame()
        active_chart_obj.wait_for_number_of_element(run_window_x_title_css, 8, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(x_label,  parent_css='#MAINTABLE_wbody0', msg="Step 5.1: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(y_label, parent_css='#MAINTABLE_wbody0', msg="Step 5.2: y-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 7, parent_css="#MAINTABLE_wbody0", msg="Step 5.3: Riser verification")
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 5.4')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 5.5:", parent_css="#MAINTABLE_wbody0_ft")
        
        """
        Step 6: From the option bar at the top of the Chart, click the first icon, for general options.
        Expect to see the following options available for the chart.
        """
        if global_obj.browser_name is 'ie':
            active_chart_obj.verify_menu_bar_popup_values('MAINTABLE_wmenu0', 0, ['Chart/Rollup Tool', 'Restore Original'],"step 6: Verify the popup")
            
        else:   
            active_chart_obj.verify_menu_bar_popup_values('MAINTABLE_wmenu0', 0, ['Chart/Rollup Tool', 'Restore Original'],"step 6: Verify the popup")
            
        """
        Step 7: Move the cursor to the last option, Export to.
        Expect to see the following menu of Export destinations.
        """
        if global_obj.browser_name is 'ie':
            active_chart_obj.verify_menu_bar_popup_values('MAINTABLE_wmenu0', 0, ['Excel', 'Word', 'PowerPoint'],"step 7: Verify the bipopup",popup_path='Export to')
            
        """
        Step 8: Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()