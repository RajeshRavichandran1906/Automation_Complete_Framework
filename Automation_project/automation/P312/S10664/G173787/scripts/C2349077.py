'''
Created on Feb7, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664_paperclicpping_2
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349077
TestCase Name = Treated as SUM if bin field added to Vertical axis bucket

'''
import unittest
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase

class C2349077_TestClass(BaseTestCase):

    def test_C2349077(self):
        visual=visualization.Visualization(self.driver)
        Test_Case_ID = 'C2349077'
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,total_risers,tooltip, step_num,color='lochmara', legend=None):
            visual.verify_x_axis_title(x_title, msg='Step' + step_num + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step' + step_num + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4'+' Verify y-axis label')
            visual.verify_legends(legend, msg='Step ' + step_num + '.5'+' Verify legends')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step' + step_num + '.6:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class*='"+riser+"']", color,  msg='Step' + step_num + '.7:'+' Verify riser color')
            visual.verify_tooltip(riser,tooltip,msg='Step' + step_num + '.8:'+' Verify riser tooltip')
        
        """
        Step01: Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
                http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2349077_Base.fex
        """
        visual.edit_visualization_using_api("C2349077_Base")
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 6, 50) 
          
        """
        Step02: Add 'Product,Category' to Color bucket
        """
        visual.right_click_on_datetree_item("Product,Category",1,'Add To Query->Color')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text.legend-title", "ProductCategory", 60)
         
        """
        Step03: Verify following preview displayed
        """
        expected_xaxis_labels=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        riser="riser!s0!g0!mbar"
        tooltip=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$129,608,338.53', 'Product Category:Accessories', 'Filter Chart', 'Exclude from Chart', 'Drill up to PRODUCT_CATEGORY_1', 'Drill down to']
        legend=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_bar_chart(['PRODUCT_CATEGORY_1'],['Revenue'],expected_xaxis_labels,expected_yaxis_labels,riser, 7,tooltip, '03', legend=legend)
                  
        """
        Step04: Select "Media players and Stereo Systems" risers
        Step05: Click "Group Product,Category selection"
        """
        src_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s3!g2!mbar']")
        tgt_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s4!g3!mbar']")
        visual.create_lasso(src_elem, tgt_elem,source_element_location='middle_left',source_xoffset=-6)
        visual.select_lasso_tooltip("Group Product,Category Selection")
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text.legend-title", "PRODUCT_CATEGORY_2", 60)
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 7, 75)
        
        """
        Step06: Verify "PRODUCT_CATEGORY_2 " created and preview updated
        """
        expected_xaxis_labels=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        riser="riser!s3!g2!mbar"
        color='pale_yellow'
        tooltip=['PRODUCT_CATEGORY_1:Media Player', 'Revenue:$246,073,059.36', 'PRODUCT_CATEGORY_2:Media Player and Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        legend=['PRODUCT_CATEGORY_2', 'Accessories', 'Camcorder', 'Computers', 'Media Player and Stereo Systems', 'Televisions', 'Video Production']
        verify_bar_chart(['PRODUCT_CATEGORY_1'],['Revenue'],expected_xaxis_labels,expected_yaxis_labels,riser, 7,tooltip, '06',color, legend=legend)
        
        """
        Step07: Click Run
        Step08: Hover on media player riser and verify tooltip values
        Step09: Close run window
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 7, 75)
        expected_xaxis_labels=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        riser="riser!s3!g2!mbar"
        color='pale_yellow'
        tooltip=['PRODUCT_CATEGORY_1:Media Player', 'Revenue:$246,073,059.36', 'PRODUCT_CATEGORY_2:Media Player and Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        legend=['PRODUCT_CATEGORY_2', 'Accessories', 'Camcorder', 'Computers', 'Media Player and Stereo Systems', 'Televisions', 'Video Production']
        verify_bar_chart(['PRODUCT_CATEGORY_1'],['Revenue'],expected_xaxis_labels,expected_yaxis_labels,riser, 7,tooltip, '08',color, legend=legend)
        visual.take_run_window_snapshot(Test_Case_ID, '15')
        visual.switch_to_previous_window()
           
        """
        Step10: Click IA > Save as "C2349077" > Click Save
        """
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 7, 75)
        visual.save_as_visualization_from_menubar(Test_Case_ID)
          
        """
        Step11: Logout using API
        """
        visual.logout_visualization_using_api()
          
        """
        Step12: Restore saved fex using API
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349077.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 7, 75)  
        expected_xaxis_labels=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        riser="riser!s3!g2!mbar"
        color='pale_yellow'
        tooltip=['PRODUCT_CATEGORY_1:Media Player', 'Revenue:$246,073,059.36', 'PRODUCT_CATEGORY_2:Media Player and Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        legend=['PRODUCT_CATEGORY_2', 'Accessories', 'Camcorder', 'Computers', 'Media Player and Stereo Systems', 'Televisions', 'Video Production']
        verify_bar_chart(['PRODUCT_CATEGORY_1'],['Revenue'],expected_xaxis_labels,expected_yaxis_labels,riser, 7,tooltip, '12',color, legend=legend)
             
         
        """
        Step20: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        
if __name__ == "__main__":
    unittest.main()