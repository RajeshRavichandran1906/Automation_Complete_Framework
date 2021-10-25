'''
Created on May 08, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227628
Test case Name =  Show Data via runtime menu
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon,visualization_run,\
    ia_run
from common.lib import utillity
from common.lib import core_utility


class C2227628_TestClass(BaseTestCase):

    def test_C2227628(self):
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_runobj = visualization_run.Visualization_Run(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        data_list = ["Cost of Goods", "Product,Category"]
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
        elem = "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(elem, 1, metaobj.chart_long_timesleep)
 
        """
        Step 02: Double-click "Cost of Goods", located under Sales Measures
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        for item in data_list:
            metaobj.datatree_field_click(item,2,1)
            utillobj.synchronize_with_visble_text("#queryTreeColumn", item, metaobj.chart_medium_timesleep)
         
        """
        Step04: Drag and drop "Product,Category" to the Filter pane
        Step05: Deselect "All"
        Step06: Select "Camcorder", "Computers", "Media Player" and "Televisions"
        Step07: Click OK
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.drag_drop_data_tree_items_to_filter("Product,Category", 1)
        item_list=['[All]','Camcorder','Computers','Media Player','Televisions']
        metaobj.select_or_verify_visualization_filter_values(item_list, Ok_button=True)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step07a: Verify filter pane has Product Category")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step07:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step07:a(i) Verify Y-Axis Title")
        expected_xval_list=['Camcorder','Computers','Media Player','Televisions']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step07:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step07.c: Verify first bar color")
        
        """
        Step08: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_util_obj.switch_to_new_window()
            
        """
        Step09: Verify output
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 09:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step 09:a(i) Verify Y-Axis Title")
        expected_xval_list=['Camcorder','Computers','Media Player','Televisions']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 09.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 09.c: Verify first bar color")
        
        """
        Step10: Expand Filter menu in the lower right corner
        Step11: Click Show Data icon (first icon with grid image)
        """
        vis_runobj.select_run_menu_option('MAINTABLE_menuContainer1',"show_report")
        
        """
        Step12:Deselect "Camcorder" in the Filter prompt
        """
        propertyobj.select_or_verify_show_prompt_item('1', 'Camcorder')#selecting Computers in FF
        propertyobj.select_or_verify_show_prompt_item('1', 'Camcorder',verify=True,verify_type=False,msg="Step12:Verify Camcorder deselected")
                
        """
        Step13: Verify output
        """
        utillobj.synchronize_with_number_of_element('table.arPivot', 1, metaobj.chart_medium_timesleep)
        ia_runobj.verify_table_data_set("table.arPivot", "C2227628_Ds01.xlsx", "Step13: Verify Cost of Goods and product category data values")
        
        """
        Step14: Click Show Data icon to return to the Chart
        """
        vis_runobj.select_run_menu_option('MAINTABLE_menuContainer1',"show_report")
        
        """
        Step15: Verify output
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 15:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step 15:a(i) Verify Y-Axis Title")
        expected_xval_list=['Computers','Media Player','Televisions']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 15:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step 15.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 15.c: Verify first bar color")

        """
        Step16: Click the Undo icon in the Filter menu (icon after Grid)
        """
        vis_runobj.select_run_menu_option('MAINTABLE_menuContainer1',"reset", toggle='no')
        
        """
        Step17: Verify output
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step17:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step17:a(i) Verify Y-Axis Title")
        expected_xval_list=['Camcorder','Computers','Media Player','Televisions']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step17:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step17.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step17.c: Verify first bar color")
           
        """
        Step18: Close output window
        """
        core_util_obj.switch_to_previous_window()
        utillobj.synchronize_with_number_of_element("#applicationButton img", 1, metaobj.chart_medium_timesleep)
               
        """
        Step19: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """       
        
if __name__ == '__main__':
    unittest.main()
        
        