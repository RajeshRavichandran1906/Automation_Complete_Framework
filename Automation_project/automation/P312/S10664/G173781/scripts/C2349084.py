'''
Created on Jan 9, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349084
TestCase Name = If more than 1 BY, none in Rows and 1 in Column, group on Column
'''

import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata

class C2349084_TestClass(BaseTestCase):

    def test_C2349084(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2349084'
        Restore_fex = 'C2349084_Base'
        
        """
        CLASS & OBJECTS
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
#         visual = visualization.Visualization(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)

        """
        Step 01: Restore saved fex using API
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2349084_Base.fex
        """
        utillobj.infoassist_api_edit(Restore_fex, 'idis', 'S10664_paperclipping_1',mrid='mrid',mrpass='mrpass')
#         visual.invoke_visualization_in_edit_mode_using_api(Restore_fex)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 text[class^='colHeader-label!']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        
        """
        Verify Restored successfully
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 643)
        expected_xval_list=['Stereo Systems', 'Camcorder', 'Stereo Systems', 'Camcorder', 'Media Player', 'Accessories', 'Stereo Systems', 'Camcorder', 'Televisions', 'Media Player', 'Accessories', 'Stereo Systems', 'Media Player', 'Accessories', 'Stereo Systems', 'Camcorder', 'Accessories', 'Media Player', 'Accessories', 'Media Player', 'Video Produc...', 'Stereo Systems', 'Accessories', 'Accessories', 'Accessories', 'Accessories', 'Media Player', 'Televisions', 'Televisions', 'Media Player', 'Media Player', 'Televisions', 'Televisions', 'Media Player']
#         expected_xval_list=['Stereo Systems', 'Video Produc...', 'Camcorder', 'Stereo Systems', 'Camcorder', 'Media Player', 'Video Produc...', 'Media Player', 'Stereo Systems', 'Televisions', 'Accessories', 'Stereo Systems', 'Camcorder', 'Media Player', 'Stereo Systems', 'Televisions', 'Media Player', 'Stereo Systems', 'Accessories', 'Media Player', 'Stereo Systems', 'Stereo Systems', 'Media Player', 'Accessories', 'Computers', 'Media Player', 'Stereo Systems', 'Camcorder', 'Stereo Systems', 'Accessories', 'Media Player', 'Stereo Systems', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Produc...', 'Stereo Systems', 'Accessories', 'Accessories', 'Accessories', 'Accessories', 'Media Player', 'Televisions', 'Televisions', 'Media Player', 'Stereo Systems', 'Media Player', 'Televisions', 'Televisions', 'Media Player']
        expected_yval_list=['0', '5.6M', '11.2M', '16.8M', '22.4M', '28M', '0', '5.6M', '11.2M', '16.8M', '22.4M', '28M', '0', '5.6M', '11.2M', '16.8M', '22.4M', '28M', '0', '5.6M', '11.2M', '16.8M', '22.4M', '28M', '0', '5.6M', '11.2M', '16.8M', '22.4M', '28M', '0', '5.6M', '11.2M', '16.8M', '22.4M', '28M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 01.01: X and Y axis Scales Values has changed or NOT')
#         xaxis_value="Pr..."
        yaxis_value="Revenue"
#         resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 01:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 01.02: Verify Y-Axis Title")
        expected_header='Store Business Sub Region'
        expected_label=['Africa', 'Asia', 'Australia-New Zealand', 'Canada', 'East', 'Europe']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Rows',expected_header,expected_label,"Step 01.03:")
        expected_header='Brand : Product Category'
        expected_label=['A...', 'A...', 'A...', 'BOSE', 'C...', 'D...', 'G...', 'G...', 'H...', 'JVC', 'LG', 'L...', 'Magn...', 'N...', 'O...', 'Panasonic', 'Philips', 'Pioneer', 'P...', 'P...', 'R...', 'Samsung', 'Sanyo', 'S...', 'Sharp', 'Sony', 'S...', 'T...', 'T...', 'T...', 'Y...']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Column',expected_header,expected_label,"Step 01.04:", label_length=1)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 643, 'Step 01.05: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!r5!c25!", "bar_blue", "Step 01.06: Verify bar color")
        expected_legend_list = ['Store Business Region', 'EMEA', 'North America', 'Oceania', 'South America']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", expected_legend_list, "Step 01.07:")
        time.sleep(5)
        
        """
        Step 02: Right click "Store,Business,Sub Region" in Rows > Delete
        """
        time.sleep(6)
        metaobj.querytree_field_click("Store,Business,Sub Region", 1, 1, 'Delete')
        time.sleep(6)
        
        """
        Step 03: Verify following preview displayed
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 201)
        expected_xval_list=['Accessories', 'Media Player', 'Televisions', 'Stereo Systems', 'Video Product...', 'Camcorder', 'Accessories', 'Televisions', 'Accessories', 'Stereo Systems', 'Camcorder', 'Media Player', 'Video Product...', 'Media Player', 'Stereo Systems', 'Televisions', 'Accessories', 'Media Player', 'Stereo Systems', 'Accessories', 'Stereo Systems', 'Camcorder', 'Media Player', 'Stereo Systems', 'Televisions', 'Media Player', 'Stereo Systems', 'Accessories', 'Media Player', 'Stereo Systems', 'Media Player', 'Stereo Systems', 'Media Player', 'Accessories', 'Computers', 'Media Player', 'Stereo Systems', 'Camcorder', 'Stereo Systems', 'Accessories', 'Media Player', 'Stereo Systems', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Televisions', 'Video Product...', 'Televisions', 'Media Player', 'Stereo Systems']
#         expected_xval_list=['Stereo Systems', 'Video Produc...', 'Camcorder', 'Stereo Systems', 'Camcorder', 'Media Player', 'Video Produc...', 'Media Player', 'Stereo Systems', 'Televisions', 'Accessories', 'Stereo Systems', 'Camcorder', 'Media Player', 'Stereo Systems', 'Televisions', 'Media Player', 'Stereo Systems', 'Accessories', 'Media Player', 'Stereo Systems', 'Stereo Systems', 'Media Player', 'Accessories', 'Computers', 'Media Player', 'Stereo Systems', 'Camcorder', 'Stereo Systems', 'Accessories', 'Media Player', 'Stereo Systems', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Produc...', 'Stereo Systems', 'Accessories', 'Accessories', 'Accessories', 'Accessories', 'Media Player', 'Televisions', 'Televisions', 'Media Player', 'Stereo Systems', 'Media Player', 'Televisions', 'Televisions', 'Media Player']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M', '80M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 03.01: X and Y axis Scales Values has changed or NOT')
#         xaxis_value="P"
        yaxis_value="Revenue"
#         resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 03:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 03.02: Verify Y-Axis Title")
        expected_header='Brand : Product Category'
        expected_label=['A...', 'A...', 'A...', 'BOSE', 'C...', 'D...', 'G...', 'G...', 'H...', 'JVC', 'LG', 'L...', 'Magn...', 'N...', 'O...', 'Panasonic', 'Philips', 'Pioneer', 'P...', 'P...', 'R...', 'Samsung', 'Sanyo', 'S...', 'Sharp', 'Sony', 'S...', 'T...', 'T...', 'T...', 'Y...']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Column',expected_header,expected_label,"Step 03.03:", label_length=1)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 201, 'Step 03.04: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!r0!c4!", "bar_blue", "Step 03.05: Verify bar color")
        expected_legend_list = ['Store Business Region', 'EMEA', 'North America', 'Oceania', 'South America']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", expected_legend_list, "Step 03.06:")
        time.sleep(5)
        
        """
        Step 04: Lasso several data points in preview
        """
        time.sleep(4)
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s3!g3!mbar!r0!c9!', target_tag='rect', target_riser='riser!s0!g0!mbar!r0!c7!')
        time.sleep(2)
        
        """
        Step 05: Verify Tooltip shows "Group Brand Selection" option
        """
        resultobj.select_or_verify_lasso_filter(verify=['16 items selected', 'Filter Chart', 'Exclude from Chart', 'Group Brand Selection'], msg='Step 05.01: Verify following tool tip values displayed')
        time.sleep(2)
        
        """
        Step 06. Click magnifying glass icon in ribbon > Review the fex
        """
        ribbonobj.select_top_toolbar_item("toolbar_showfex")
        time.sleep(8)
                
        """
        The query shows the first BY is Brand:
        SUM WF_RETAIL_LITE.WF_RETAIL_SALES.REVENUE_US
        1. BY WF_RETAIL_LITE.WF_RETAIL_PRODUCT.BRAND
        2. BY WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_STORE.BUSINESS_REGION
        3. BY WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY
        """
        e = driver.find_element_by_xpath("//iframe[starts-with(@id,'BiRich')]")
        time.sleep(3)
        driver.switch_to.frame(e)
        fex_code = driver.find_element_by_css_selector("body>div").text
        expected_code = 'SUM WF_RETAIL_LITE.WF_RETAIL_SALES.REVENUE_US\nBY WF_RETAIL_LITE.WF_RETAIL_PRODUCT.BRAND\nBY WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_STORE.BUSINESS_REGION\nBY WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY'
        bol=expected_code in fex_code
        utillobj.asequal(True, bol, 'Step 06.01: The query shows the first BY is Brand')
        driver.switch_to_default_content()
        time.sleep(4)
        
        """
        Step 07. Close focexec window
        """
        close_fexcode_btn=driver.find_element_by_css_selector("#showFexOKBtn img")
        utillobj.click_on_screen(close_fexcode_btn, 'middle')
        utillobj.click_on_screen(close_fexcode_btn, 'middle', click_type=0)
        time.sleep(8)
        
        """
        Step 08: Logout using API (without saving) - http://machine:port/alias/service/wf_security_logout.jsp
        """
       
        
if __name__ == '__main__':
    unittest.main()