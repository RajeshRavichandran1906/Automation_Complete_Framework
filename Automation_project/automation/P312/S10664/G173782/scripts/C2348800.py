'''
Created on Jan 12, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348800
TestCase Name = Group many values
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization


class C2348800_TestClass(BaseTestCase):

    def test_C2348800(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2348800'
        
        driver = self.driver #Driver reference object created
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        time.sleep(4)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        visual.wait_for_number_of_element(parent_css, 1, 250)

        """
        Step 02: Double click "Revenue","Store,Country" to add fields
        """
        visual.double_click_on_datetree_item("Revenue", 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 1, 250)
        
        visual.double_click_on_datetree_item("Store,Country", 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 34, 300)
        
        """
        Verify following chart preview displayed
        """
        time.sleep(5)
        visual.verify_x_axis_title(['Store Country'], msg='Step 2.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 2.2')
        expected_xaxis_label=['Australia', 'Belgium', 'Brazil', 'Canada', 'Chile', 'China', 'Czech Republic', 'Denmark', 'Egypt', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Luxembourg', 'Mexico', 'Netherlands', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Singapore', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'United Kingdom', 'United States']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 2.3')
        expected_yaxis_label=['0', '100M', '200M', '300M', '400M', '500M', '600M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 2.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 34, msg='Step 2.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g3!mbar']", "bar_blue", msg='Step 2.6')
        time.sleep(5)   
        expected_tooltip_list=['Store Country:Canada', 'Revenue:$51,147,788.36', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to Store State Province']
        visual.verify_tooltip("riser!s0!g3!mbar", expected_tooltip_list,'Step 2.7: Verify Tooltip') 
        
        """
        Step 03: Lasso all risers in preview 
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        visual.wait_for_number_of_element(parent_css, 34, 300)
        source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g0!mbar!']")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g33!mbar!']")
        visual.create_lasso(source_element, target_element, source_yoffset=10, target_xoffset=10, source_element_location='bottom_middle')
        time.sleep(3)

        """
        Step 04: Click "Group Store,Country selection"
        """
        visual.select_lasso_tooltip('Group Store,Country Selection')
        time.sleep(2)

        """
        Step 05: Verify the preview
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 1, 300)
        visual.verify_x_axis_title(['COUNTRY_NAME_1'], msg='Step 5.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 5.2')
        expected_xaxis_label=['Australia and Belgium and Brazil and 31 more']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 5.3')
        expected_yaxis_label=['0', '0.2B', '0.4B', '0.6B', '0.8B', '1B', '1.2B']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 5.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 1, msg='Step 5.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg='Step 5.6')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'COUNTRY_NAME_1', 1, "Step 05.7:")
        
        """
        Step 06: Hover over on riser and verify tool tip
        """
        time.sleep(5)   
        expected_tooltip_list=['COUNTRY_NAME_1:Australia and Belgium and Brazil and 31 more', 'Revenue:$1,061,192,925.22', 'Drill up to Store Business Sub Region', 'Drill down to Store Country']
        visual.verify_tooltip("riser!s0!g0!mbar", expected_tooltip_list,'Step 06: Verify Tooltip') 
        time.sleep(5)

        """
        Step 07: Click Run
        """
        time.sleep(5)
        visual.run_visualization_from_toptoolbar()
        time.sleep(10)
        visual.switch_to_new_window()
        time.sleep(5)
        print("Switched to run window:") 

        """
        Step 08: Verify run time chart
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 1, 300)
        visual.verify_x_axis_title(['COUNTRY_NAME_1'], msg='Step 8.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 8.2')
        expected_xaxis_label=['Australia and Belgium and Brazil and 31 more']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 8.3')
        expected_yaxis_label=['0', '0.2B', '0.4B', '0.6B', '0.8B', '1B', '1.2B']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 8.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 1, msg='Step 8.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg='Step 8.6')
        time.sleep(5)   
        expected_tooltip_list=['COUNTRY_NAME_1:Australia and Belgium and Brazil and 31 more', 'Revenue:$1,061,192,925.22', 'Drill up to Store Business Sub Region', 'Drill down to Store Country']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list,'Step 8.7: Verify Tooltip') 
        time.sleep(8)
        visual.take_run_window_snapshot(Test_Case_ID, '08')

        """
        Step 09: Dismiss run time chart
        """
        visual.switch_to_previous_window()
        time.sleep(8)
        parent_css="#applicationButton img"
        visual.wait_for_number_of_element(parent_css, 1, 200)
        print("Switched back to main window:")

        """
        Step 10: Click Save in the toolbar > Save as "C2348800" > Click Save
        """
        time.sleep(4)
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        time.sleep(5)

        """
        Step 11: Logout using API : http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        time.sleep(2)

        """
        Step 12: Restore saved fex using API:
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348800.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        time.sleep(10)
        
        """
        Restored successfully 
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 1, time_out=500)
        time.sleep(5)
        visual.verify_x_axis_title(['COUNTRY_NAME_1'], msg='Step 12.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 12.2')
        expected_xaxis_label=['Australia and Belgium and Brazil and 31 more']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 12.3')
        expected_yaxis_label=['0', '0.2B', '0.4B', '0.6B', '0.8B', '1B', '1.2B']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 12.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 1, msg='Step 12.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg='Step 12.6')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'COUNTRY_NAME_1', 1, "Step 12.7:")
        time.sleep(5)   
        expected_tooltip_list=['COUNTRY_NAME_1:Australia and Belgium and Brazil and 31 more', 'Revenue:$1,061,192,925.22', 'Drill up to Store Business Sub Region', 'Drill down to Store Country']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list,'Step 12.8: Verify Tooltip') 
        
        """
        Step 13: Logout using API (without saving) - http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()