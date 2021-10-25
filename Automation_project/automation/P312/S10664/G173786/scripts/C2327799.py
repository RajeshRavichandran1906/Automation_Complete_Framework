'''
Created on Feb 6, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2327799
Test_Case Name : Undo Merge with Group Value
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2327799_TestClass(BaseTestCase):

    def test_C2327799(self):
        
        Test_Case_ID = "C2327799"
        visual = visualization.Visualization(self.driver)
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,total_risers,tooltip, step_num):
            visual.verify_x_axis_title(x_title, msg='Step' + step_num + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step' + step_num + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step' + step_num + '.5:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class*='"+riser+"']", 'lochmara',  msg='Step' + step_num + '.6:'+' Verify riser color')
            visual.verify_tooltip(riser,tooltip,msg='Step' + step_num + '.7:'+' Verify riser tooltip')
            
        """
        Step1: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        visual.invoke_visualization_using_api('new_retail/wf_retail_lite')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 12, 50)
        
        """
        Step02: Add fields "Cost of Goods" and "Product,Category"
        """
        visual.double_click_on_datetree_item('Cost of Goods', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "CostofGoods", 45)
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "ProductCategory", 45)
        
        """
        Step03: Lasso select Accessories, Camcorder and Computer (you may have to use CNTL key)
        Step04: Click "Group Product, Category Selection"
        """
        src_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class*='riser!s0!g0!mbar']")
        tgt_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class*='riser!s0!g2!mbar']")
        visual.create_lasso(src_elem, tgt_elem,source_element_location='middle_left',source_xoffset=-6)
        visual.select_lasso_tooltip("Group Product,Category Selection")
        
        """
        Step05: Verify following preview displayed
        """   
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 5, 120)     
        expected_xaxis_labels=['Accessories and Camcorder and Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0','50M','100M','150M','200M','250M','300M']
        riser="riser!s0!g0!mbar"
        tooltip=['PRODUCT_CATEGORY_1:Accessories and Camcorder and Computers', 'Cost of Goods:$264,428,419.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        verify_bar_chart(['PRODUCT_CATEGORY_1'],['Cost of Goods'],expected_xaxis_labels,expected_yaxis_labels,riser,5,tooltip, '05')        
                
        """
        Step06: Select "Accessories and Camcorder and Computer" and "Media player" riser (lasso or CTRL key)
        Step07: Click "Merge with "Accessories and Camcorder..." in tooltip info
        """
        src_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class*='riser!s0!g0!mbar']")
        tgt_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class*='riser!s0!g1!mbar']")
        visual.create_lasso(src_elem, tgt_elem,source_element_location='middle_left',source_xoffset=-6)
        visual.select_lasso_tooltip("Merge with Accessories and Camcorder...")      
        
        """
        Step08: Verify risers merged and displayed following
        """
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 4, 120)
        expected_xaxis_labels=['Accessories and Camcorder and Computers', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0','100M','200M','300M','400M','500M']
        riser="riser!s0!g0!mbar"
        tooltip=['PRODUCT_CATEGORY_1:Accessories and Camcorder and Computers', 'Cost of Goods:$454,668,900.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        verify_bar_chart(['PRODUCT_CATEGORY_1'],['Cost of Goods'],expected_xaxis_labels,expected_yaxis_labels,riser,4,tooltip, '08')        
         
        """
        Step09: Click 'Undo' icon in toolbar
        """
        visual.select_item_in_top_toolbar("undo")
         
        """
        Step10: Verify preview refreshed and displayed the previous result as following
        """
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 5, 120)     
        expected_xaxis_labels=['Accessories and Camcorder and Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0','50M','100M','150M','200M','250M','300M']
        riser="riser!s0!g0!mbar"
        tooltip=['PRODUCT_CATEGORY_1:Accessories and Camcorder and Computers', 'Cost of Goods:$264,428,419.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        verify_bar_chart(['PRODUCT_CATEGORY_1'],['Cost of Goods'],expected_xaxis_labels,expected_yaxis_labels,riser,5,tooltip, '10')
        
        """
        Step11: Click Run
        Step12: Verify run time chart
        Step13: Dismiss run window
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 5, 120)     
        expected_xaxis_labels=['Accessories and Camcorder and Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0','50M','100M','150M','200M','250M','300M']
        riser="riser!s0!g0!mbar"
        tooltip=['PRODUCT_CATEGORY_1:Accessories and Camcorder and Computers', 'Cost of Goods:$264,428,419.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        verify_bar_chart(['PRODUCT_CATEGORY_1'],['Cost of Goods'],expected_xaxis_labels,expected_yaxis_labels,riser,5,tooltip, '12')
        visual.take_run_window_snapshot(Test_Case_ID, '12')
        visual.switch_to_previous_window()
        
        """
        Step14: Click Redo
        """
        visual.wait_for_number_of_element("#topToolBar #redoButton img", 1, 30)
        visual.select_item_in_top_toolbar("redo")
         
        """
        Step15: Verify preview refreshed and displayed following
        """
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 4, 120)
        expected_xaxis_labels=['Accessories and Camcorder and Computers', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0','100M','200M','300M','400M','500M']
        riser="riser!s0!g0!mbar"
        tooltip=['PRODUCT_CATEGORY_1:Accessories and Camcorder and Computers', 'Cost of Goods:$454,668,900.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        verify_bar_chart(['PRODUCT_CATEGORY_1'],['Cost of Goods'],expected_xaxis_labels,expected_yaxis_labels,riser,4,tooltip, '15')        
         
        """
        Step16: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()

if __name__ == '__main__':
    unittest.main()        
