"""-------------------------------------------------------------------------------------------
Created on June 28, 2019
@author: Niranjan/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2276144
Test Case Title =  Treemap: Tooltip does not show all fields
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart

class C2276144_TestClass(BaseTestCase):

    def test_C2276144(self):
        
        """
            CLASS OBJECTS 
        """
        chart = Chart(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        qwerty_tree_css = "#queryTreeWindow"
        chart_css = "#pfjTableChart_1"
        ok_button_css = "#qbSelectChartTypeDlgOkBtn"
        
        """
            STEP 1 : Launch the IA API with Chart (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP251_S9164%2FG159435&tool=chart&master=baseapp/wf_retail_lite
        """
        chart.invoke_chart_tool_using_api("baseapp/wf_retail_lite")
        chart.wait_for_visible_text(chart_css, "Group 0")
 
        """
            STEP 2 : Select "Format" > "Chart Types" > "Other" > "HTML5" > "Treemap" > "OK".
        """
        chart.select_ia_ribbon_item("Format", "other")
        chart.wait_for_visible_text(ok_button_css, "OK")
        chart.select_other_chart_type("html5", "tree_map", 5, verify_selection=False)
        
        """
            STEP 3 : Double click "Product,Subcategory","Brand".
        """
        chart.double_click_on_datetree_item("Product,Subcategory", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Product,Subcategory")
        
        chart.double_click_on_datetree_item("Brand", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Brand")

        """
            STEP 4 : Drag "Cost of Goods" to Size.
        """
        chart.drag_field_from_data_tree_to_query_pane("Cost of Goods", 1, "Size", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Cost of Goods")
    
        """
            STEP 5 : Drag "Gross Profit" to Color.
        """
        chart.drag_field_from_data_tree_to_query_pane("Gross Profit", 1, "Color", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Gross Profit")
        
        chart.verify_number_of_risers("#pfjTableChart_1 rect", 1, 79, msg="step 05.01")
        chart.verify_legends_in_preview(['Gross Profit', '0M', '2.7M', '5.4M', '8.1M', '10.8M'], msg="step 05.02")
        chart.verify_x_axis_label_in_preview(['Blu Ray', 'Speaker Kits', 'Flat Panel TV', 'Home Theater Systems', 'Headphones', 'Standard', 'Smartphone', 'Receivers', 'Video Editing', 'Universal Remote Controls', 'Professional', 'iPod Docking Station', 'Tablet', 'Handheld', 'Streaming', 'DVD Players', 'Charger', 'CRT TV', 'B...', 'P...', 'Pioneer', 'Samsung', 'Sony', 'Panasonic', 'JVC', 'Sharp', 'Onkyo', 'BOSE', 'Harman Kardon', 'Polk Audio', 'Yamaha', 'Sony', 'LG', 'Panasonic', 'Panasonic', 'LG', 'Pioneer', 'Samsung', 'Sony', 'Sharp', 'Sennheiser', 'Grado', 'Audio Tech...', 'Denon', 'Sony', 'Pioneer', 'Sony', 'Canon', 'JVC', 'Sony', 'Samsung', 'Yamaha', 'Sony', 'Onkyo', 'Thomson Grass Valley', 'BOSE', 'JVC', 'Niles Audio', 'Logitech', 'Sony', 'Canon', 'JVC', 'Philips', 'LG', 'Sony', 'Sanyo', 'Sony', 'Samsung', 'Sanyo', 'Panaso...', 'Sony', 'JVC', 'Roku', 'LG', 'Tos...', 'JVC', 'P', 'P', 'Sa...', 'S', 'S', 'Pa...', 'LG', 'S...', 'Gross Profit'], xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1, msg="step 05.03")
        chart.verify_chart_color("pfjTableChart_1", "riser!sBlu Ray-_-Samsung!g0!mnode", "mantis2", msg="step 05.04 verify color")
        chart.verify_chart_color("pfjTableChart_1", "riser!sCRT TV-_-Panasonic!g0!mnode", "punch", msg="step 05.05 verify color")
        
        """
            STEP 6 : Click Run
        """
        chart.run_chart_from_toptoolbar()
        chart.switch_to_frame()
        chart.wait_for_visible_text("#jschart_HOLD_0", "Blu")

        """
            STEP 7 : Verify tooltip displaying all the fields.
        """
        chart.verify_tooltip_in_run_window("riser!sBlu Ray-_-Samsung!g0!mnode", ['Product Subcategory:Blu Ray', 'Brand:Samsung', 'Cost of Goods:$38,015,625.00', 'Gross Profit:$8,814,029.55'], msg="STEP 7 : Verify tooltip displaying all the fields.")
        
        """
            STEP 8 : Logout using API
            http://domain:port/alias/service/wf_security_logout.jsp
        """
        chart.switch_to_default_content()
        chart.api_logout()
        
if __name__ == '__main__':
    unittest.main()  