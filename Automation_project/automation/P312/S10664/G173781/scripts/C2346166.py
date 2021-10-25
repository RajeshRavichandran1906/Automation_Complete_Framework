'''
Created on Jan 9, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2346166
TestCase Name = If more than 1 BY, none in Rows/Columns and 1 in Color, group by Color
'''

import unittest, time
from common.lib import utillity
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata

class C2346166_TestClass(BaseTestCase):

    def test_C2346166(self):
        
        """
        TESTCASE VARIABLES
        """        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        visual = visualization.Visualization(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1, expire_time=30)

        """
        Step 02: Double click "Revenue", "Product,Category" add fields to chart
        """
        visual.double_click_on_datetree_item('Revenue', 1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        
        visual.double_click_on_datetree_item("Product,Category",1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        
        """
        Step 03: Drag and drop "Store,Business,Region" to color bucket
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Store,Business,Region', 1, 'Color', 0)
        time.sleep(6)
        parent_css="#queryTreeWindow table tr:nth-child(12) td"
        resultobj.wait_for_property(parent_css, 1, expire_time=10, string_value="Store,Business,Region")
        
        """
        Step 04: Verify following chart preview displayed
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 28)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 04.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 04.02: Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 04.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 4, 7, 'Step 04.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 04.05: Verify first bar color")
        expected_legend_list = ['Store Business Region', 'EMEA', 'North America', 'Oceania', 'South America']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", expected_legend_list, "Step 04.06:")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Revenue:$51,791,709.98', 'Store Business Region:EMEA', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 04.07: Verify bar value")
        time.sleep(5)
        
        """
        Step 05: Lasso first three risers in preview
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s3!g0!mbar!', target_tag='rect', target_riser='riser!s0!g2!mbar!')
        time.sleep(2)
        
        """
        Step 06: Verify tool tip value
        """
        resultobj.select_or_verify_lasso_filter(verify=['10 items selected', 'Filter Chart', 'Exclude from Chart', 'Group Store,Business,Region Selection'], msg='Step 06.01: Verify following tool tip values displayed')
        time.sleep(2)
        
        """
        Step 07: Click magnifying glass icon in ribbon 
        """
        ribbonobj.select_top_toolbar_item("toolbar_showfex")
        time.sleep(8)
                
        """
        Step 08: Review the fex
        The query shows the first BY is Store,Business,Region:
        SUM WF_RETAIL_LITE.WF_RETAIL_SALES.REVENUE_US
        1. BY WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_STORE.BUSINESS_REGION
        2. BY WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY
        """
        e = driver.find_element_by_xpath("//iframe[starts-with(@id,'BiRich')]")
        time.sleep(3)
        driver.switch_to.frame(e)
        fex_code = driver.find_element_by_css_selector("body>div").text
        expected_code = 'SUM WF_RETAIL_LITE.WF_RETAIL_SALES.REVENUE_US\nBY WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_STORE.BUSINESS_REGION\nBY WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY'
        bol=expected_code in fex_code
        utillobj.asequal(True, bol, 'Step 08.01: The query shows the first BY is Store,Business,Region')
        driver.switch_to_default_content()
        time.sleep(4)
        
        """
        Step 09. Close view focexec window
        """
        close_fexcode_btn=driver.find_element_by_css_selector("#showFexOKBtn img")
        utillobj.click_on_screen(close_fexcode_btn, 'middle')
        utillobj.click_on_screen(close_fexcode_btn, 'middle', click_type=0)
       
        """
        Step 10: Logout using API (without saving) - http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()