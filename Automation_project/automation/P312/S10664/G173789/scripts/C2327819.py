'''
Created on Feb 13, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2327819
TestCase Name = Modify values in a Visualization Filter based on a Group field updates the Filter dialog and Prompt
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.pages import metadata

class C2327819_TestClass(BaseTestCase):

    def test_C2327819(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2327819'
        number_of_element = 1
        sleep_time = 4
        time_out = 200
        visual = visualization.Visualization(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        time.sleep(sleep_time)
        
        """
        Step 02: Right-click "Product,Category"> Create Group...
        """
        field_item = 'Product,Category'
        position = 1
        visual.right_click_on_datetree_item(field_item, position, context_menu_path='Create Group...')
        button_css = "div[id^='QbDialog'] [class*='active'] [id='dynaGrpsCancelBtn'] img"
        visual.wait_for_number_of_element(button_css, number_of_element)
        
        """
        Step 03: Multi-select any values (Accessories, Camcorder, Computer) > Click "Group"
        """
        value_list_for_group=['Accessories', 'Camcorder', 'Computers']
        visual.slect_group_grid_values(value_list_for_group)
        visual.create_group_options('Group')
        time.sleep(4)
        """
        Step 04: Click OK
        """
        visual.exit_group_dialog('ok')
        time.sleep(5)
        """
        Step 05: Verify Group created and displayed in dimension section data pane
        """
        metadataobj.expand_data_field_section('Model->Attributes')
        #metadataobj.collapse_data_field_section('Product')
        metadataobj.collapse_data_field_section('Attributes->Model->Product')
        time.sleep(5)
        parent_css="#iaMetaDataBox table tr:nth-child(11) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='PRODUCT_CATEGORY_1', time_out=time_out)
        visual.verify_field_listed_under_datatree('Dimensions', 'PRODUCT_CATEGORY_1', 6, "Step 05:")
        
        """
        Step 06: Drag "PRODUCT_CATEGORY_1" into Filter pane > Click OK
        """
        time.sleep(sleep_time)
        visual.drag_and_drop_from_data_tree_to_filter('Dimensions->PRODUCT_CATEGORY_1', 1)
        visual.close_filter_dialog('ok')
        time.sleep(3)
        """
        Step 07: Right-click "PRODUCT_CATEGORY_1" in the Data pane > Edit Group...
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        visual.wait_for_number_of_element(parent_css, number_of_element, time_out)
        visual.right_click_on_datetree_item('Dimensions->PRODUCT_CATEGORY_1', 1, context_menu_path='Edit Group...')
        
        """
        Step 08: Multi-select any values (Televisions, Video production) and click "Group" to create another group 
        """
        button_css = "div[id^='QbDialog'] [class*='active'] [id='dynaGrpsCancelBtn'] img"
        visual.wait_for_number_of_element(button_css, number_of_element)
        value_list_for_group=['Televisions', 'Video Production']
        visual.slect_group_grid_values(value_list_for_group)
        time.sleep(sleep_time)
        visual.create_group_options('Group')
        time.sleep(sleep_time)
        expected_group_dialog_list=['Accessories and Camcorder and Computers', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions and Video Production', 'Televisions', 'Video Production']
        visual.verify_group_grid_values(expected_group_dialog_list, "Step 08: Verify group values in the group")
        
        """
        Step 09: Click OK
        """
        visual.exit_group_dialog('ok')
        
        """
        Step 10: Verify Filter Prompt is updated
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        visual.wait_for_number_of_element(parent_css, number_of_element, time_out)
        title_name = "PRODUCT_CATEGORY_1"
        visual.verify_prompt_title(title_name)
        expected_items_list=['[All]', 'Accessories and Camcorder and Computers', 'Media Player', 'Stereo Systems', 'Televisions and Video Production']
        visual.verify_show_prompt_table_list(expected_items_list, msg='Step 10:')
        
        """
        Step 11: Right-click filter in the Filter pane > Edit...
        """
        visual.right_click_on_field_in_filterbox('PRODUCT_CATEGORY_1', 1, context_menu_path='Edit...')
        
        """
        Step 12: Verify Values in Filter dialog are updated
        """
        parent_css="#avFilterOkBtn"
        visual.wait_for_number_of_element(parent_css, number_of_element, time_out)
        field_value_list=['[All]', 'Accessories and Camcorder and Computers', 'Media Player', 'Stereo Systems', 'Televisions and Video Production']
        visual.verify_filter_field_values(field_value_list, verify_type='true')
        
        """
        Step 13: Click Cancel
        """
        visual.close_filter_dialog('cancel')
        visual.take_preview_snapshot(Test_Case_ID ,'13')
        
        """
        Step 14: Logout using API (without saving): http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()