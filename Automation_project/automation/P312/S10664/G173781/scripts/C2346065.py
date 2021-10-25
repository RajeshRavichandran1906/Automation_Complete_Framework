'''
Created on Jan 4, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2346065
TestCase Name = No group option If 2 BY fields and first is Date or Numeric
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata
from common.wftools import visualization
from common.lib import utillity


class C2346065_TestClass(BaseTestCase):

    def test_C2346065(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2346065'
        Restore_fex = 'C2346065_Base'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01: Restore the C2346065_Base.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2346065_Base.fex
        """
        utillobj.infoassist_api_edit(Restore_fex, 'idis', 'S10664_paperclipping_1',mrid='mrid',mrpass='mrpass')
#         visual.invoke_visualization_in_edit_mode_using_api(Restore_fex)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 01:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 01:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 01:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 01.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 01.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 01.d: Verify bar value")
        time.sleep(5)
        
        """
        Step 02: Drag and drop "Sale, Year (YYMDy)"(Sales_Related\Transaction Date, Component) to Matrix - Rows bucket
        """
#         visual.add_field_using_double_click('Revenue', 1)
        metaobj.drag_drop_data_tree_items_to_query_tree('Sale,Year', 1, 'Rows', 0)
        time.sleep(4)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resultobj.wait_for_property(parent_css, 1, expire_time=10, string_value="Sale,Year")
        
        """
        Step 03: Verify following chart preview displayed
        """
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 42)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M', '0', '30M', '60M', '90M', '120M', '150M', '0', '30M', '60M', '90M', '120M', '150M', '0', '30M', '60M', '90M', '120M', '150M', '0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step03.a: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 03:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 03:a(ii) Verify Y-Axis Title")
        expected_header='Sale Year'
        expected_label=['2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Rows',expected_header,expected_label,"Step 03:a(iii):")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 42, 'Step 03.b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!r3!c0!", "bar_blue", "Step 03.c: Verify bar color")
        time.sleep(5)
        tooltip_val=['Sale Year:2016', 'Product Category:Accessories', 'Revenue:$53,208,007.57', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar!r5!c0!',tooltip_val,"Step 03.d: Verify output value")
        time.sleep(5)
        
        """
        Step 04: Lasso on few risers in preview
        """
        time.sleep(4)
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g0!mbar!r0!c0!', target_tag='rect', target_riser='riser!s0!g0!mbar!r2!c0!')
        time.sleep(2)
        
        """
        Step 05: Verify Tooltip does not have option to group.
        """
        resultobj.select_or_verify_lasso_filter(verify=['3 points', 'Filter Chart', 'Exclude from Chart'], msg='Step 05: Verify following tool tip values displayed')
        time.sleep(2)
        
        """
        Step 06: Drag and drop "ID, Product" to Matrix - Rows bucket to replace "Sale, Year (YYMDy)" value
        """
#         visual.add_field_using_double_click('Revenue', 1)
        metaobj.drag_drop_data_tree_items_to_query_tree('ID Product', 1, 'Sale,Year', 0)
        time.sleep(4)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resultobj.wait_for_property(parent_css, 1, expire_time=10, string_value="ID Product")
        
        """
        Step 07: Verify following chart preview displayed
        """
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 159)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '0', '4M', '8M', '12M', '16M', '0', '4M', '8M', '12M', '16M', '0', '4M', '8M', '12M', '16M', '0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step07.a: X and Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 07:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 07:a(ii) Verify Y-Axis Title")
        expected_header='ID Product'
        expected_label=['1000', '1001', '1002', '1003', '1004', '1005', '1006']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Rows',expected_header,expected_label,"Step 07:a(iii):")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 159, 'Step 07.b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0!", "bar_blue", "Step 07.c: Verify bar color")
        time.sleep(5)
        tooltip_val=['ID Product:1000', 'Product Category:Media Player', 'Revenue:$7,594,935.71', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g3!mbar!r0!c0!',tooltip_val,"Step 07.d: Verify output value")
        time.sleep(5)
        
        """
        Step 08: Lasso several data points in preview (1000 to 1002 Media player riser) 
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g3!mbar!r0!c0!', target_tag='rect', target_riser='riser!s0!g3!mbar!r2!c0!')
        time.sleep(2)
        
        """
        Step 09: Verify Tooltip does not have option to group.
        """
        resultobj.select_or_verify_lasso_filter(verify=['3 items selected', 'Filter Chart', 'Exclude from Chart'], msg='Step 09: Verify following tool tip values displayed')
        time.sleep(8)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele, Test_Case_ID+'_Actual_step09', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
        Step 10: Logout using API (without saving)- http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()