'''
Created on Sep 26, 2019

@author: Niranjan
Testcase Name : Verify use in Calculator tool
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261846
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods

class C8261846_TestClass(BaseTestCase):
    
    def test_C8261846(self):
        """
        Test case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        def collapse_tree(fieldname):
            collapse_tree_css =  '.wfc-dataselector-mdtree-box div[title*="'+fieldname+'"]' ' div[class="tnode-btn tnode-btn-collapsed"]'
            collapse_tree_elem = utils.validate_and_get_webdriver_object(collapse_tree_css, 'tree')
            core_utils.left_click(collapse_tree_elem)
        
        Step1 = """
        Step 1: Launch the API to create new Designer Chart with the Car file

        http://machine:port/{alias}/designer?&item=IBFS:/WFC/Repository/P292_S28313/G671774&master=ibisamp/car&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api('ibisamp/car')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        utils.capture_screenshot("01.00", Step1)
        
        Step2 = """
        Step 2: Right click on the COUNTRY field, select New calculation
        Step 02.00: Verify the list shows the hierarchy without the split between Dimensions and Measures.
        """
        designer_chart_obj.right_click_on_dimensions_field('COUNTRY', 'New calculation...')
        designer_chart_obj.wait_for_number_of_element('.wfc-calculator-dialog div[class*="ibx-dialog-ok-button"]',1, designer_chart_obj.chart_long_timesleep)
#         designer_chart_obj.wait_for_number_of_element('div[class*="ibx-dialog-button ibx-dialog-ok-button"]', 1, designer_chart_obj.chart_long_timesleep)
        tree_css= '.wfc-dataselector-mdtree-box .wfc-mdfp-whole-tree'
        new_calc_tree_ele = utils.validate_and_get_webdriver_object(tree_css, 'tree')
        new_calc_tree = new_calc_tree_ele.text.split('\n')
        utils.as_notin(new_calc_tree, ['Measures', 'Dimensions'], 'Step 02.00: Verify the list shows the hierarchy without the split between Dimensions and Measures.')
        
        utils.capture_screenshot("02.00", Step2)
        
        Step3 = """
        Step 3: Expand all the folders
        Step 03.00: Verify the Dimensions and Measures panes are not present.
        Verify segments represented as folders
        ORIGIN, COMP, CARREC, BODY, SPECS, WARANT and EQUIP should have folder icons.
        """
        collapse_tree('COMP')
        designer_chart_obj.wait_for_visible_text(tree_css, 'CAR')
        collapse_tree('CARREC')
        designer_chart_obj.wait_for_visible_text(tree_css, 'MODEL')
        collapse_tree('WARANT')
        designer_chart_obj.wait_for_visible_text(tree_css, 'WARRANTY')
        collapse_tree('EQUIP')
        designer_chart_obj.wait_for_visible_text(tree_css, 'STANDARD')
        new_calc_tree_ele = utils.validate_and_get_webdriver_object(tree_css, 'tree')
        new_calc_tree = new_calc_tree_ele.text.split('\n')
        utils.as_notin(new_calc_tree, ['Measures', 'Dimensions'], 'Step 03.00: Verify the Dimensions and Measures panes are not present')
        collapse_tree('BODY')
        designer_chart_obj.wait_for_visible_text(tree_css, 'BODYTYPE')
        folder_css= ".wfc-dataselector-mdtree-box .wfc-mdfp-whole-tree div[class*='glyph-folder']+div[class='ibx-label-text']"
        folder_ele = utils.validate_and_get_webdriver_objects(folder_css, 'folder')
        folder= []
        for folder_item in folder_ele:
            folder_label = folder_item.text
            if folder_label == 'BODY' :
                scroll_elem = self.driver.find_element_by_css_selector('.wfc-dataselector-mdtree-box .wfc-mdfp-whole-tree')
                utils.scroll_down_on_element(scroll_elem, number_of_scroll = 2)
            folder.append(folder_label)
        expected_folders = ['ORIGIN', 'COMP', 'CARREC', 'BODY', 'SPECS', 'WARANT', 'EQUIP']
        utils.asequal(folder, expected_folders, 'Step 03.01: Verify segments represented as folders')
        utils.capture_screenshot("03.00", Step3)
        
        Step4 = """
        Step 4: Click Cancel.
        """
        designer_chart_obj.click_button_on_calculation('Cancel')
        utils.capture_screenshot("04.00", Step4)
        
        Step5 = """
        Step 5: Close chart without saving
        """
        designer_chart_obj.close_designer_chart_from_application_menu()
        utils.capture_screenshot("05.00", Step5)
        
        """
        Step 6: Logout using API:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp.
        """
        
if __name__ == '__main__':
    unittest.main()