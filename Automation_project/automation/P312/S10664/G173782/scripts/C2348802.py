'''
Created on Jan 12, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2346166
TestCase Name = If more than 1 BY, none in Rows/Columns and 1 in Color, group by Color
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata
from common.lib import utillity
from common.wftools import visualization


class C2348802_TestClass(BaseTestCase):

    def test_C2348802(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2348802'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P312/S10664_paperclipping_1', 'mrid', 'mrpass')
#         visual.invoke_visualization_tool_using_api('new_retail/wf_retail_lite')
        time.sleep(4)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1, expire_time=30)

        """
        Step 02: Double click "Revenue", "Product,Category" add fields to chart
        """
#         visual.double_click_on_datetree_item('Revenue', 1)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        
#         visual.double_click_on_datetree_item("Product,Category",1)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        
        """
        Verify following chart preview displayed
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 02:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 02:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 02:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 02.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 02.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 02.d: Verify bar value")
        time.sleep(5)
        
        """
        Step 03: Multi Select Accessories and Camcorder in preview
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g0!mbar!', target_tag='rect', target_riser='riser!s0!g1!mbar!')
        time.sleep(3)
        
        """
        Step 04: Select "Group Product,Category selection"
        """
        resultobj.select_or_verify_lasso_filter(select='Group Product,Category Selection')
        time.sleep(2)
        
        """
        Step 05: Verify Group created without dialog
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 6)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'PRODUCT_CATEGORY_1', "Step 05:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 05:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 05:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 6, 'Step 05.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 05.c: Verify first bar color")
        metaobj.verify_query_pane_field('Horizontal Axis', 'PRODUCT_CATEGORY_1', 1, "Step 05.d:")
        
        """
        Step 06: Hover over on "Accessories and Camcorder" riser in preview 
        """
        time.sleep(5)
        bar=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 05.e: Verify bar value")
        time.sleep(5)
        
        
        """
        Step 07: Click view source icon to see focexec code
        """
        ribbonobj.select_top_toolbar_item("toolbar_showfex")
        time.sleep(8)
                
        """
        Define shows in fex:
        DEFINE FILE baseapp/wf_retail_lite
        PRODUCT_CATEGORY_1/A100=DECODE WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY ( 'Accessories' 'Accessories and Camcorder' 'Camcorder' 'Accessories and Camcorder' ELSE 'Default');
        PRODUCT_CATEGORY_1 = IF PRODUCT_CATEGORY_1 EQ 'Default' THEN WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY ELSE PRODUCT_CATEGORY_1;
        ENDG
        """
        e = driver.find_element_by_xpath("//iframe[starts-with(@id,'BiRich')]")
        time.sleep(3)
        driver.switch_to.frame(e)
        fex_code = driver.find_element_by_css_selector("body>div").text
        expected_code = "DEFINE FILE new_retail/wf_retail_lite\nPRODUCT_CATEGORY_1/A100=DECODE WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY ( 'Accessories' 'Accessories and Camcorder' 'Camcorder' 'Accessories and Camcorder' ELSE 'Default');\nPRODUCT_CATEGORY_1 = IF PRODUCT_CATEGORY_1 EQ 'Default' THEN WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY ELSE PRODUCT_CATEGORY_1;\nEND"
        bol=expected_code in fex_code
        utillobj.asequal(True, bol, 'Step 07: The query shows the first BY is Store,Business,Region')
        driver.switch_to_default_content()
        time.sleep(4)
        
        """
        Step 08. Close focexec widow
        """
        close_fexcode_btn=driver.find_element_by_css_selector("#showFexOKBtn img")
        utillobj.click_on_screen(close_fexcode_btn, 'middle')
        utillobj.click_on_screen(close_fexcode_btn, 'middle', click_type=0)
        
        """
        Step 09: Click Save in the toolbar > Save as "C2348802" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
        Step 10: Logout using API : http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 11: Run fex from Resource tree using API:
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10664&BIP_item=C2348802.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10664_paperclipping_1', 'mrid', 'mrpass')
        
        """
        Step 12: Hover over on "Accessories and Camcorder" riser in preview 
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 6)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'PRODUCT_CATEGORY_1', "Step 12:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 12:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 6, 'Step 12.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 12.c: Verify first bar color")
        time.sleep(5)
        bar=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 12.d: Verify bar value")
        time.sleep(8)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele, Test_Case_ID+'_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 13: Logout using API : http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 14: Restore saved fex using API:
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348802.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10664_paperclipping_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
        
        """
        Restored successfully 
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 6)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'PRODUCT_CATEGORY_1', "Step 14:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 14:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 14:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 6, 'Step 14.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 14.c: Verify first bar color")
        metaobj.verify_query_pane_field('Horizontal Axis', 'PRODUCT_CATEGORY_1', 1, "Step 14.d:")
        time.sleep(5)
        bar=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 14.e: Verify bar value")
        
        """
        Step 15: Logout using API (without saving) - http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()