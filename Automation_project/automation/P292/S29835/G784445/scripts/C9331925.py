'''
Created on Oct 1, 2019

@author: Niranjan
Testcase Name : Chart with JSON syntax for Sort
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/9331925
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools import designer_chart

class C9331925_TestClass(BaseTestCase):
    
    def test_C9331925(self):
        
        """
        Testcase case objects and variables
        """
        design_chart  = designer_chart.Designer_Chart(self.driver)
        utils = UtillityMethods(self.driver)
        
        current_file = 'C9331925_base'
        project = utils.parseinitfile('project_id')
        suite = utils.parseinitfile('suite_id')
        group_id = utils.parseinitfile('group_id')
        folder = project + '_' + suite + '/' + group_id
        
        Step1 = """
        Step 1: Run C9331925_base.fex with API call
        domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS:/WFC/Repository/P292_S29835/G730863/&BIP_item=C9331925_base.fex
        Step 01.00 : Slices of pie are sorted descending (size/value) from top clockwise.
        """
        design_chart.run_designer_chart_using_api(current_file,folder_path = folder)
        design_chart.verify_number_of_risers(".chartPanel path[class^='riser']", 1, 10, msg ='Step 01.00')
        expected_list = ['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        design_chart.verify_legends_in_preview(expected_list, '#jschart_HOLD_0', 11, msg = 'Step 01.01')
        title_elem = utils.validate_and_get_webdriver_object("#jschart_HOLD_0 text[class*='mpieLabel']", 'title of x-axis')
        title = utils.get_attribute_value(title_elem, 'dom_visible_text')
        utils.asequal('DEALER_COST', title['dom_visible_text'], 'Step 01.02 : Verify the title of pie chart')
        design_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s2!g0!mwedge!']", 'med_green', '#jschart_HOLD_0', msg = 'Step 01.03')
        design_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s6!g0!mwedge!']", 'periwinkle_gray', '#jschart_HOLD_0', msg = 'Step 01.04')
        utils.verify_picture_using_sikuli('C9331925_Step01.png', 'Step 01.05 : Verify the slices of pie are sorted descending from top clockwise')
        utils.capture_screenshot("01.00", Step1, expected_image_verify = True)
        
if __name__ == '__main__':
    unittest.main()