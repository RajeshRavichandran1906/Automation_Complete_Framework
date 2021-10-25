'''Created by June 28 2019

@author: vishnu_priya

http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2241431
Suite : Verify tooltip for Treemap chart displays correctly
'''

import unittest,time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart 

class C2241431_TestClass(BaseTestCase):

    def test_C2241431(self):
        
        utils=utillity.UtillityMethods(self.driver)
        chart_obj=chart.Chart(self.driver)
        preview_chart_css="TableChart_1"
        
        """
        Step 1:Launch the IA API with Chart (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP251_S9164%2FG159435&tool=chart&master=baseapp/wf_retail_lite
        """
        
        chart_obj.invoke_chart_tool_using_api("baseapp/wf_retail_lite")
        chart_obj.wait_for_number_of_element(".chartPanel .risers rect",25,chart_obj.chart_long_timesleep)
 
        """
        Step 2:Select "Format" > "Chart Types" > "Other" > "HTML5" > "Treemap" > "OK".
        """
        chart_obj.select_ia_ribbon_item('Format', 'Other')
        chart_obj.select_other_chart_type('html5',"tree_map",5)
        chart_obj.wait_for_visible_text(".chartPanel", "widgets", chart_obj.chart_long_timesleep)
        
        """
        Step 3:Double click "Product,Subcategory","Brand".
        """
        chart_obj.double_click_on_datetree_item("Product,Subcategory",1)
        chart_obj.wait_for_visible_text("#queryTreeColumn", "Product,Subcategory", chart_obj.chart_long_timesleep)
        chart_obj.double_click_on_datetree_item("Brand",1)
        chart_obj.wait_for_visible_text("#queryTreeColumn", "Brand", chart_obj.chart_long_timesleep)
 
        """
        Step 4:Drag "Cost of Goods" to Size.
        """
        chart_obj.drag_field_from_data_tree_to_query_pane("Cost of Goods", 1, "Size")
        chart_obj.wait_for_visible_text("#queryTreeColumn", "Cost of Goods", chart_obj.chart_long_timesleep)
 
        """
        Step 5:Drag "Gross Profit" to Color.
        """
        chart_obj.drag_field_from_data_tree_to_query_pane("Gross Profit", 1, "Color", 1)
        chart_obj.wait_for_visible_text("#queryTreeColumn", "Gross Profit", chart_obj.chart_long_timesleep)
        
        """
        Step 6:Verify the following chart is displayed.
        """
        chart_obj.verify_number_of_risers("svg g [class^='riser!s']", 79, 1, "Step 02:13: Verify number of risers")
        
        """
        Step 7:Click "Run"
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()

        """
        Step 8:Mouse hover over the chart, verify the tool tip.
        """
        chart_obj.verify_tooltip_in_run_window('riser!sTablet-_-Sony!g0!mnode',['Product Subcategory:Tablet', 'Brand:Sony', 'Cost of Goods:$15,379,721.00', 'Gross Profit:$7,757,160.52'],"Step 8 verfiy the tooltip" )

        """
        Step 9:Click "IA" > "Save As" > "C2241431" > "Save".
        """

        chart_obj.switch_to_default_content()
        chart_obj.save_as_from_application_menu_item("C2241431","P251_S9164->G159435")
        time.sleep(3)
 
        """
        Step 10:Logout using API
        http://domain:port/alias/service/wf_security_logout.jsp
        """
        
        
 
if __name__ == '__main__':
    unittest.main() 




        
