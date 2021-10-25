'''
Created on Feb 13, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2327045
TestCase Name = Change name of Dynamic Group field used in Visualization Filter
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.pages.core_metadata import CoreMetaData

class C2327045_TestClass(BaseTestCase):

    def test_C2327045(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2327045'
        visual = visualization.Visualization(self.driver)
        metadataobj = CoreMetaData(self.driver)
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=wf_retail_lite
        """
        visual.invoke_visualization_using_api('new_retail/wf_retail_lite')
        time.sleep(4)

        """
        Step 02: Right-click "Product,Category"> Create Group...
        """
        visual.right_click_on_datetree_item('Product,Category', 1, context_menu_path='Create Group...')
        button_css = "div[id^='QbDialog'] [class*='active'] [id='dynaGrpsCancelBtn'] img"
        visual.wait_for_number_of_element(button_css, 1)
        
        """
        Step 03: Multi-select any values > Click "Group" 
        """
        value_list_for_group=['Accessories', 'Camcorder', 'Computers']
        visual.slect_group_grid_values(value_list_for_group)
        visual.create_group_options('Group')
        
        """
        Step 04: Click OK
        """
        visual.exit_group_dialog('ok')
        
        """
        Step 05: Drag "PRODUCT_CATEGORY_1" into Filter pane 
        """
        visual.drag_and_drop_from_data_tree_to_filter('Dimensions->PRODUCT_CATEGORY_1', 1)
#         visual.right_click_on_datetree_item('Dimensions->PRODUCT_CATEGORY_1', 1, context_menu_path='Filter')
#         visual.drag_datatree_item_to_filter_pane('PRODUCT_CATEGORY_1', 1)
        
        """
        Step 06: Click OK
        """
        parent_css="#avFilterOkBtn"
        visual.wait_for_number_of_element(parent_css, 1, 300)
        visual.close_filter_dialog('ok')
        
        """
        Step 07: Right-click "PRODUCT_CATEGORY_1" in the Data pane > Edit Group...
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        visual.wait_for_number_of_element(parent_css, 1, 300)
        time.sleep(3)
        visual.right_click_on_datetree_item('Dimensions->PRODUCT_CATEGORY_1', 1, context_menu_path='Edit Group...')
        
        """
        Step 08: Change name to 'TEST1' and select 'Show Other'
        """
        button_css = "div[id^='QbDialog'] [class*='active'] [id='dynaGrpsCancelBtn'] img"
        visual.wait_for_number_of_element(button_css, 1)
        visual.enter_field_text_group('TEST1')
        time.sleep(5)
        visual.create_group_options('Show Other')
        time.sleep(3)
        expected_group_dialog_list=['Accessories and Camcorder and Computers', 'Accessories', 'Camcorder', 'Computers', 'Other', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_group_grid_values(expected_group_dialog_list, "Step 08: Verify group values in the group")
        
        """
        Step 09: Click OK
        """
        visual.exit_group_dialog('ok')
        
        """
        Step 10: Verify following chart displayed without any error
        Data pane, Filter pane and prompt updated with 'TEST1' name
        """
        parent_css="#iaMetaDataBox table tr:nth-child(11) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='TEST1', time_out=300)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        visual.wait_for_number_of_element(parent_css, 1, 300)
        visual.verify_field_listed_under_datatree('Customer', 'TEST1', 1, "Step 10.1:")
        visual.verify_field_in_filterbox('TEST1', 1, "Step 10.2:")
        visual.verify_prompt_title('TEST1')
        visual.take_preview_snapshot(Test_Case_ID ,'10')
        
        """
        Step 11: Logout using API: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()