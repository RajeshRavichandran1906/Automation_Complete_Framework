'''
Created on Jan 8, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2346068
TestCase Name = If more than 1 BY and 1 is in Rows, group on rows
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, core_metadata, metadata
from common.lib import utillity


class C2346068_TestClass(BaseTestCase):

    def test_C2346068(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2346068'
        
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        core_metaobj=core_metadata.CoreMetaData(self.driver)
        metadataobj = metadata.MetaData(self.driver)
       
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_paperclipping_1', 'mrid', 'mrpass')
        time.sleep(4)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1, expire_time=30)

        """
        Step 02: Double click "Revenue", "Product,Category" add fields to chart
        """
        metadataobj.collapse_data_field_section('Filters and Variables')
        time.sleep(3)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        
        """
        Step 03: Drag and drop "Store,Business,Sub Region" to Rows and "Brand" to Columns
        """
        core_metaobj.collapse_data_field_section('Sales')
        time.sleep(3)
        metaobj.drag_drop_data_tree_items_to_query_tree('Store,Business,Sub Region', 1, 'Rows', 0)
        time.sleep(6)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resultobj.wait_for_property(parent_css, 1, expire_time=10, string_value="Store,Business,Sub Region")
        parent_css="#MAINTABLE_wbody1 text[class^='rowHeader-label!']"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.drag_drop_data_tree_items_to_query_tree('Brand', 1, 'Columns', 0)
        time.sleep(6)
        parent_css="#queryTreeWindow table tr:nth-child(6) td"
        resultobj.wait_for_property(parent_css, 1, expire_time=10, string_value="Brand")
        parent_css="#MAINTABLE_wbody1 text[class^='colHeader-label!']"
        resultobj.wait_for_property(parent_css, 1)
        
        """
        Step 04: Add "Store,Business,Region" to Color bucket
        """
        time.sleep(6)
        metaobj.datatree_field_click("Store,Business,Region", 1, 1, 'Add To Query', 'Color')
        time.sleep(15)
        
        """
        Step 05: Verify following preview displayed
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 643)
        time.sleep(10)
        
        expected_xval_list=['Stereo Systems', 'Camcorder', 'Stereo Systems', 'Camcorder', 'Media Player', 'Accessories', 'Stereo Systems', 'Camcorder', 'Televisions', 'Media Player', 'Accessories', 'Stereo Systems', 'Media Player', 'Accessories', 'Stereo Systems', 'Camcorder', 'Accessories', 'Media Player', 'Accessories', 'Media Player', 'Video Produc...', 'Stereo Systems', 'Accessories', 'Accessories', 'Accessories', 'Accessories', 'Media Player', 'Televisions', 'Televisions', 'Media Player', 'Media Player', 'Televisions', 'Televisions', 'Media Player']
        expected_yval_list=['0', '5.6M', '11.2M', '16.8M', '22.4M', '28M', '0', '5.6M', '11.2M', '16.8M', '22.4M', '28M', '0', '5.6M', '11.2M', '16.8M', '22.4M', '28M', '0', '5.6M', '11.2M', '16.8M', '22.4M', '28M', '0', '5.6M', '11.2M', '16.8M', '22.4M', '28M', '0', '5.6M', '11.2M', '16.8M', '22.4M', '28M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step05.a: X and Y axis Scales Values has changed or NOT',x_axis_label_length=1)
        expected_header='Store Business Sub Region'
        expected_label=['Africa', 'Asia', 'Australia-New Zealand', 'Canada', 'East', 'Europe']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Rows',expected_header,expected_label,"Step 05:a(iii):")
        expected_header='Brand : Product Category'
        expected_label=['A...', 'A...', 'A...', 'BOSE', 'C...', 'D...', 'G...', 'G...', 'H...', 'JVC', 'LG', 'L...', 'Magn...', 'N...', 'O...', 'Panasonic', 'Philips', 'Pioneer', 'P...', 'P...', 'R...', 'Samsung', 'Sanyo', 'S...', 'Sharp', 'Sony', 'S...', 'T...', 'T...', 'T...', 'Y...']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Column',expected_header,expected_label,"Step 05:a(iv):", label_length=1)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 643, 'Step 05.b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!r5!c25!", "bar_blue", "Step 05.c: Verify bar color")
        expected_legend_list = ['Store Business Region', 'EMEA', 'North America', 'Oceania', 'South America']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", expected_legend_list, "Step 05.d:")
        time.sleep(5)
        tooltip_val=['Store Business Sub Region:Canada', 'Brand:Sony', 'Product Category:Camcorder', 'Revenue:$3,197,678.80', 'Store Business Region:North America', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Region', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s1!g1!mbar!r3!c25!',tooltip_val,"Step 05.e: Verify output value")
        
        """
        Step 06: Lasso several data points in preview
        """
        time.sleep(9)
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s1!g1!mbar!r3!c25!', target_tag='rect', target_riser='riser!s0!g5!mbar!r5!c25!')
        time.sleep(2)
        
        """
        Step 07: Verify tooltip shows option "Group Store,Business,Sub Region" (First BY)
        """
        resultobj.select_or_verify_lasso_filter(verify=['15 items selected', 'Filter Chart', 'Exclude from Chart', 'Group Store,Business,Sub Region Selection'], msg='Step 05: Verify following tool tip values displayed')
        time.sleep(2)
        
        """
        Step 08. Click magnifying glass icon in ribbon > Review the fex
        """
        ribbonobj.select_top_toolbar_item("toolbar_showfex")
        utillobj.synchronize_with_number_of_element("iframe[id*='BiRich']", 1, 190)
        
        """
        Step 08.a The query shows the first BY is Store,Business,Sub Region:
        SUM WF_RETAIL_LITE.WF_RETAIL_SALES.REVENUE_US
        1. BY WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_STORE.BUSINESS_SUB_REGION
        2. BY WF_RETAIL_LITE.WF_RETAIL_PRODUCT.BRAND
        3. BY WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_STORE.BUSINESS_REGION
        4. BY WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY
        """
        e = self.driver.find_element_by_xpath("//iframe[starts-with(@id,'BiRich')]")
        time.sleep(3)
        self.driver.switch_to.frame(e)
        fex_code = self.driver.find_element_by_css_selector("body>div").text
        expected_code = 'SUM WF_RETAIL_LITE.WF_RETAIL_SALES.REVENUE_US\nBY WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_STORE.BUSINESS_SUB_REGION\nBY WF_RETAIL_LITE.WF_RETAIL_PRODUCT.BRAND\nBY WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_STORE.BUSINESS_REGION\nBY WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY'
        bol=expected_code in fex_code
        utillobj.asequal(True, bol, 'Step 08.a The query shows the first BY is Store,Business,Sub Region')
        self.driver.switch_to_default_content()
        time.sleep(4)
        
        """
        Step 09. Close focexec window
        """
        close_fexcode_btn=self.driver.find_element_by_css_selector("#showFexOKBtn img")
        utillobj.click_on_screen(close_fexcode_btn, 'middle')
        utillobj.click_on_screen(close_fexcode_btn, 'middle', click_type=0)
        time.sleep(8)
        ele=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele, Test_Case_ID+'_Actual_step09', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 10. Click Save in the toolbar > Save as "C2346068" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
        Step 11: Logout using API - http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()