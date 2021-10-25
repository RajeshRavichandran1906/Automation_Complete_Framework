'''
Created on Jan 08, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349045
Test_Case Name : Group added to drill hierarchy above field of origin 2
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization

class C2349045_TestClass(BaseTestCase):

    def test_C2349045(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2349045'
        visual=Visualization(self.driver)
        
        def verify_bar_chart(expected_xaxis_title, expected_xaxis_label, expected_yaxis_label, total_risers, step_num):
            visual.verify_y_axis_title(['Revenue'], msg='Step ' + step_num + '.1')
            visual.verify_x_axis_title(expected_xaxis_title, msg='Step ' + step_num + '.2')
            visual.verify_x_axis_label(expected_xaxis_label, msg='Step ' + step_num + '.3')
            visual.verify_y_axis_label(expected_yaxis_label, msg='Step ' + step_num + '.4')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step ' + step_num + '.5 ')
            visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", 'lochmara',  msg='Step ' + step_num + '.6 ')
        """
            Step 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        time.sleep(3)
         
        """
            Step 02 : Double click "Revenue", "Product,Category"
        """
        visual.double_click_on_datetree_item('Revenue', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "Revenue", 80)
        
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "ProductCategory", 80)
        time.sleep(3)
        
        """
            Step 03 : Multi select "Camcorder" and "Media player" > Group Product, Category selection
        """
        camcorder=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g1!mbar!']")
        mediaplayer=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g3!mbar!']")
        visual.multi_select_chart_component([camcorder, mediaplayer])
        visual.select_lasso_tooltip('Group Product,Category Selection')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "PRODUCT_CATEGORY_1", 80)
        
        """
            Step 04 : Verify following preview displayed
        """
        expected_xaxis_labels=['Accessories', 'Camcorder and Media Player', 'Computers', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        verify_bar_chart(['PRODUCT_CATEGORY_1'], expected_xaxis_labels, expected_yaxis_labels, 6, '04')
        
        """
            Step 05 : Click Run
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "PRODUCT_CATEGORY_1", 80)
        
        """
            Step 05.1 : Verify run window output
        """
        verify_bar_chart(['PRODUCT_CATEGORY_1'], expected_xaxis_labels, expected_yaxis_labels, 6, '05')
        
        """
            Step 06 : Hover over "Camcorder" and "Media player" group value riser
            Tooltip displays "drill down option to Product Category"
        """
        expected_tooltip=['PRODUCT_CATEGORY_1:Camcorder and Media Player', 'Revenue:$400,538,761.60', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip("riser!s0!g1!mbar!", expected_tooltip, 'Step 06.1 : Verify tooltip displays "drill down option to Product Category"')
        
        """
            Step 07 : Select "Drill Down to Product Category"
        """
        visual.select_tooltip('riser!s0!g1!mbar!', 'Drill down to Product Category')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "ProductCategory", 80)
        
        """
            Step 08 : Verify run time updated
            Group is broken down showing a riser for each value in the group
        """
        expected_xaxis_labels=['Camcorder', 'Media Player']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        verify_bar_chart(['Product Category'], expected_xaxis_labels, expected_yaxis_labels, 2, '08')
        
        """
            Step 09 : Hover over "Media player" riser 
            Drill Up option to PRODUCT_CATEGORY_1 displays
        """
        expected_tooltip=['Product Category:Media Player', 'Revenue:$246,073,059.36', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to PRODUCT_CATEGORY_1', 'Drill down to Product Subcategory']
        visual.verify_tooltip("riser!s0!g1!mbar!", expected_tooltip, 'Step 09.1 : Verify tooltip displays "Drill Up option to PRODUCT_CATEGORY_1"')
        
        """
            Step 10 : Drill up to PRODUCT_CATEGORY_1
        """
        visual.select_tooltip('riser!s0!g1!mbar!', 'Drill up to PRODUCT_CATEGORY_1')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "PRODUCT_CATEGORY_1", 80)
        
        """
            Step 11 : Verify run time updated
            Group values display in one riser
        """
        expected_xaxis_labels=['Accessories', 'Camcorder and Media Player', 'Computers', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        verify_bar_chart(['PRODUCT_CATEGORY_1'], expected_xaxis_labels, expected_yaxis_labels, 6, '11')
        
        """
            Step 12 : Dismiss run window
        """
        visual.switch_to_previous_window()
        
        """
            Step 13 : Click Save in the toolbar > Save as "C2349045" > Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
            Step 14 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
if __name__ == '__main__':
    unittest.main()