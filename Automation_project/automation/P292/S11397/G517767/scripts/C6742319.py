'''
Created on Sept 17, 2018

@author: Varun

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/11397
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6742319
TestCase Name = Paperclipping at Design Time
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.lib import utillity
from common.pages.core_metadata import CoreMetaData
from common.pages.ia_resultarea import IA_Resultarea

class C6742319_TestClass(BaseTestCase):

    def test_C6742319(self):
        
        """
        TESTCASE OBJECTS
        """
        visual_obj = visualization.Visualization(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        fexcode_obj = IA_Resultarea(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C6742319'
        x_axis_css = "#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        y_axis_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        expected_xval_list=['Stereo Systems', 'Media Player', 'Camcorder', 'Accessories', 'Computers', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        updated_xval_list=['Accessories and Computers and Televisions and 1 more', 'Stereo Systems', 'Media Player', 'Camcorder']
        updated_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        
        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2F
        """
        visual_obj.invoke_visualization_using_api('baseapp/wf_retail_lite')
         
        """
        Step 02: Double click Revenue and Product,Category
        """
        visual_obj.double_click_on_datetree_item("Revenue", 1)
        util_obj.synchronize_with_visble_text("#TableChart_1 [class='yaxis-title']", 'Revenue', 20)
        
        visual_obj.double_click_on_datetree_item("Product,Category",1)
        util_obj.synchronize_with_visble_text("#TableChart_1 [class='xaxisOrdinal-title']", 'Product Category', 20)
         
        """
        Step 03: Right click Revenue > Sort >Sort > Descending
        """
        visual_obj.right_click_on_field_under_query_tree("Revenue", 1, "Sort->Sort->Descending")
        util_obj.synchronize_with_visble_text("#queryTreeColumn", "Revenue", 20)
        visual_obj.verify_x_axis_title(['Product Category'],  msg="Step 03.00: Verify X-Axis Title")
        visual_obj.verify_y_axis_title(['Revenue'], msg="Step 03.01: Verify Y-Axis Title")
        visual_obj.verify_x_axis_label(expected_xval_list, msg="Step 03.02: Verify X-Axis Label")
        visual_obj.verify_y_axis_label(expected_yval_list, msg="Step 03.03: Verify Y-Axis Label")
        visual_obj.verify_number_of_risers("#MAINTABLE_wbody1_f rect[class^=riser]", 1, 7, msg='Step 03.04')
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g2!mbar\"]", "bar_blue", msg="Step 03.05: Verify first bar color")
         
        """
        Step 04: Lasso Accessories, Computers, Televisions and Video Production > Group Product,Category
        """
        accessories_riser = util_obj.validate_and_get_webdriver_object('rect[class*=\"riser!s0!g3!mbar\"]',"accessories_riser")
        video_riser = util_obj.validate_and_get_webdriver_object('rect[class*=\"riser!s0!g6!mbar\"]',"video_riser")
        visual_obj.create_lasso(accessories_riser,video_riser,target_element_location='bottom_right')
        visual_obj.select_lasso_tooltip('Group Product,Category Selection')
   
        """
        Step 05: Review the preview and the data and query panes. 
        """
        visual_obj.wait_for_number_of_element(x_axis_css, 4, 120)
        visual_obj.wait_for_number_of_element(y_axis_css, 9, 120)
        visual_obj.verify_x_axis_title(['PRODUCT_CATEGORY_1'],  msg="Step 05.00: Verify X-Axis Title")
        visual_obj.verify_y_axis_title(['Revenue'], msg="Step 05.01: Verify Y-Axis Title")
        visual_obj.verify_x_axis_label(updated_xval_list, msg="Step 05.02: Verify X-Axis Label")
        visual_obj.verify_y_axis_label(updated_yval_list, msg="Step 05.03: Verify Y-Axis Label")
        visual_obj.verify_number_of_risers("#MAINTABLE_wbody1_f rect[class^=riser]", 1, 4, msg='Step 05.04')
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g2!mbar\"]", "bar_blue", msg="Step 05.05: Verify first bar color")
        CoreMetaData.collapse_data_field_section(self, 'Filters and Variables', find_from_top=True)
        visual_obj.verify_field_listed_under_datatree("Product", "PRODUCT_CATEGORY_1", 5, "Step 05.06")
        visual_obj.verify_field_listed_under_querytree("Horizontal Axis", "PRODUCT_CATEGORY_1", 2,"Step 05.07" )
        
        """
        Step 06: Review the fex. The fex contains a define.
        -*COMPONENT=Define_wf_retail_lite
        DEFINE FILE baseapp/wf_retail_lite
        PRODUCT_CATEGORY_1/A100=DECODE WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY ( 'Accessories' 'Accessories and Computers and Televisions and 1 more' 'Computers' 'Accessories and Computers and Televisions and 1 more' 'Televisions' 'Accessories and Computers and Televisions and 1 more' 'Video Production' 'Accessories and Computers and Televisions and 1 more' ELSE 'Default');
        PRODUCT_CATEGORY_1 = IF PRODUCT_CATEGORY_1 EQ 'Default' THEN WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY ELSE PRODUCT_CATEGORY_1;
        END
        """
        expected_code=['-*COMPONENT=Define_wf_retail_lite', 'DEFINE FILE baseapp/wf_retail_lite', "PRODUCT_CATEGORY_1/A100=DECODE WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY ( 'Accessories' 'Accessories and Computers and Televisions and 1 more' 'Computers' 'Accessories and Computers and Televisions and 1 more' 'Televisions' 'Accessories and Computers and Televisions and 1 more' 'Video Production' 'Accessories and Computers and Televisions and 1 more' ELSE 'Default');", "PRODUCT_CATEGORY_1 = IF PRODUCT_CATEGORY_1 EQ 'Default' THEN WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY ELSE PRODUCT_CATEGORY_1;", 'END']
#         visual_obj.verify_fexcode_syntax(expected_code, "verify the Fex Code ")
        fexcode_obj.verify_fexcode_syntax(expected_code, "Step 06.01: Verify the Fex Code ")   
        """
        Step07: Click Run
        """
        visual_obj.run_visualization_from_toptoolbar()
        visual_obj.switch_to_new_window()
         
        """
        Verify output
        """
        visual_obj.wait_for_number_of_element(x_axis_css, 4, 120)
        visual_obj.wait_for_number_of_element(y_axis_css, 9, 120)
        visual_obj.verify_x_axis_title(['PRODUCT_CATEGORY_1'],  msg="Step 07.00: Verify X-Axis Title")
        visual_obj.verify_y_axis_title(['Revenue'], msg="Step 07.01: Verify Y-Axis Title")
        visual_obj.verify_x_axis_label(updated_xval_list, msg="Step 07.02: Verify X-Axis Label")
        visual_obj.verify_y_axis_label(updated_yval_list, msg="Step 07.03: Verify Y-Axis Label")
        visual_obj.verify_number_of_risers("#MAINTABLE_wbody1_f rect[class^=riser]", 1, 4, msg='Step 07.04')
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g2!mbar\"]", "bar_blue", msg="Step 07.05: Verify first bar color")
        visual_obj.switch_to_previous_window()
        visual_obj.wait_for_number_of_element("#applicationButton img", 1, 120)

        """
        Step 08: Save visualization with name C6742319 and close.
        """       
        visual_obj.save_as_visualization_from_menubar(Test_Case_ID)
        visual_obj.logout_visualization_using_api()
              
        """
        Step 09: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2313000.fex&tool=idis
        """
        visual_obj.edit_visualization_using_api(Test_Case_ID)
        visual_obj.wait_for_number_of_element("#applicationButton img", 1, 120)
             
        """
        Verify Canvas
        """
        visual_obj.wait_for_number_of_element(x_axis_css, 4, 120)
        visual_obj.wait_for_number_of_element(y_axis_css, 9, 120)
        visual_obj.verify_x_axis_title(['PRODUCT_CATEGORY_1'],  msg="Step 09.00: Verify X-Axis Title")
        visual_obj.verify_y_axis_title(['Revenue'], msg="Step 09.01: Verify Y-Axis Title")
        visual_obj.verify_x_axis_label(updated_xval_list, msg="Step 09.02: Verify X-Axis Label")
        visual_obj.verify_y_axis_label(updated_yval_list, msg="Step 09.03: Verify Y-Axis Label")
        visual_obj.verify_number_of_risers("#MAINTABLE_wbody1_f rect[class^=riser]", 1, 4, msg='Step 09.04')
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g2!mbar\"]", "bar_blue", msg="Step 09.05: Verify first bar color")
         
        """
        Step 10: Logout using API (without saving): http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()