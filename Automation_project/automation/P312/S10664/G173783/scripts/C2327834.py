'''
Created on Jan 31, 2018

@author: Sowmiya
TestSuite Name : 8202 New Features and product changes for existing functionality 
TestSuite ID : http://172.19.2.180/testrail/index.php?/suites/view/10664&group_by=cases:section_id&group_order=asc&group_id=173783
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2327834
TestCase Name: Able to rename/ungroup values if value group name has comma
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2327834_TestClass(BaseTestCase):

    def test_C2327834(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2327834'
        Restore_fex = 'C2327834_Base'
        driver = self.driver #Driver reference object created
        visual = visualization.Visualization(self.driver)
        
        """
            Step 01 : Restore saved fex using API
                        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2327834_Base.fex
        """
        visual.edit_visualization_using_api(Restore_fex)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 4, time_out=20)        
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 1.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 1.2')
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems and Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 1.3')
        expected_y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 1.4")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 4, msg="Step 1.5")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 1.6")
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$362,455,173.58', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip("riser!s0!g0!mbar", expected_tooltip_list,msg="Step 1.7")    
        
        """
            Step 02 : Click riser "Accessories and Camcorder" in preview
            Step 03 : Verify the tooltip options and values
        """
        riser_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f [class='riser!s0!g0!mbar!']")
        visual.select_chart_component(riser_css)
        expected_tooltip_list=['1 point', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename Accessories and Camcorder...', 'Ungroup Accessories and Camcorder...', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg='Step 3.1')
        
        """
            Step 04 : Select 'Rename Accessories and Camcorder from tooltip
        """
        visual.select_lasso_tooltip('Rename Accessories and Camcorder...')
        
        """
            Step 05 : Type "Accessories, Camcorders & TV"
            Step 06 : Click OK
        """
        visual.rename_grouped_riser_name('Accessories and Camcorder' , 'Accessories, Camcorders & TV', 'OK')
        visual.wait_for_visible_text("#MAINTABLE_wbody1 text[class*='xaxisOrdinal-labels!g0!mgroupLabel!']", visble_element_text='Accessories,Camcorders&TV', time_out=300)
        
        """
            Step 07 : Verify the preview updated
        """
        expected_label_list=['Accessories, Camcorders & TV', 'Computers', 'Media Player', 'Stereo Systems and Video Production']
        visual.verify_x_axis_label(expected_label_list, msg='Step 7.1')
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 4, msg="Step 7.2")
        
        """
            Step 08 : Click on "Accessories, Camcorders & TV " riser
            Step 09 : Verify the tooltip
        """
        riser_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f [class='riser!s0!g0!mbar!']")
        visual.select_chart_component(riser_css)
        expected_tooltip_list=['1 point', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename Accessories, Camcorders...', 'Ungroup Accessories, Camcorders...', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg='Step 9.1')
        
        """
            Step 10 : Click Run and hover on "Accessories, Camcorders & TV " riser
            Step 11 : Verify the run time chart tooltip
            Step 12 : Dismiss run window
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_visible_text("#MAINTABLE_wbody1 text[class*='xaxisOrdinal-labels!g0!mgroupLabel!']", 'Accessories,Camcorders&TV')
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories, Camcorders & TV', 'Revenue:$362,455,173.58', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list, msg='Step 11.1')
        expected_label_list=['Accessories, Camcorders & TV', 'Computers', 'Media Player', 'Stereo Systems and Video Production']
        visual.verify_x_axis_label(expected_label_list, msg='Step 11.2')
        expected_label_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        visual.verify_y_axis_label(expected_label_list, msg='Step 11.3')
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 11.4')
        visual.verify_y_axis_title(['Revenue'], msg='Step 11.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g2!mbar']", "bar_blue", msg="Step 11.6")
        visual.take_run_window_snapshot(Test_Case_ID, '11')
        visual.switch_to_previous_window()
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 4, time_out=20)
        
        """
            Step 13 : Click IA > Save as "C2327834" > Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
            Step 14 : Logout using API
                        http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
            Step 15 : Reopen the fex using API
                        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2327834.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        
        """
            Step 16 : Verify successfully restored
        """
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class^='xaxis'][class$='title']", 'PRODUCT_CATEGORY_1', time_out=20)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 16.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 16.2')
        expected_xaxis_label=['Accessories, Camcorders & TV', 'Computers', 'Media Player', 'Stereo Systems and Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 16.3')
        expected_y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 16.4")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 4, msg="Step 16.5")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 16.6")
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories, Camcorders & TV', 'Revenue:$362,455,173.58', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list, msg='Step 16.7 : Verify tooltip values')
        
        """
            Step 17 : Click on "Accessories, Camcorders & TV " riser
            Step 18 : Verify the tooltip
        """
        riser_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f [class='riser!s0!g0!mbar!']")
        visual.select_chart_component(riser_css)
        expected_tooltip_list=['1 point', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename Accessories, Camcorders...', 'Ungroup Accessories, Camcorders...', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg='Step 18.1')
        visual.logout_visualization_using_api()
       
if __name__ == '__main__':
    unittest.main()