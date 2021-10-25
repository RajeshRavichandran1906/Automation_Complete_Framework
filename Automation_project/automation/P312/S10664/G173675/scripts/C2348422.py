'''
Created on Jan 02, 2018
@author: Nasir
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization

class C2348422_TestClass(BaseTestCase):


    def test_C2348422(self):
        
        Test_Case_ID = 'C2348422'
        oVisualization=Visualization(self.driver)
          
        """    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is): http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite    """
        oVisualization.invoke_visualization_using_api('new_retail/wf_retail_lite')
        
        """    2. Right click on "Revenue" in data pane > Create Bins...    """
        oVisualization.right_click_on_datetree_item("Revenue", 1, "Create Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        oVisualization.wait_for_number_of_element(parent_css, 1)
        
        """    3. Set bin width = 100    """
        """    4. Click OK    """
        oVisualization.create_bins('REVENUE_US_BIN_1', bin_width='100')
        
        """    5. Right click "REVENUE_US_BIN_1" in data pane > Edit Bin    """
        """    6. Verify following right click menu options for bin
        SUM
        Edit Bins...
        Add to Query >
        Filter
        Delete    """
        """    7. Click Edit Bin    """
        datatree_list=['Sum', 'Edit Bins...', 'Add To Query', 'Filter', 'Delete']
        oVisualization.verify_datatree_field_context_menu("Dimensions->REVENUE_US_BIN_1", 1, datatree_list, 'Step 07:')
        oVisualization.right_click_on_datetree_item("Dimensions->REVENUE_US_BIN_1", 1, 'Edit Bins...')
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        oVisualization.wait_for_number_of_element(parent_css, 1)
        
        """    8. Verify bin dialog opened Bin dialog opens with input for field name, bin width and format, including a format button and OK button disabled    """
        """    9. Click Cancel    """
        oVisualization.verify_bins_dialog(name_textbox_value='REVENUE_US_BIN_1', format_textbox_value='D20.2M', format_button_visible=True, bin_width_value='100', ok_btn_status='Disabled', btn_click='cancel', msg='Step 08')
        
        """    10. Drag and drop bin from data pane to Horizontal Axis    """
        oVisualization.drag_field_from_data_tree_to_query_pane('Dimensions->REVENUE_US_BIN_1', 1, 'Horizontal Axis')
#         oVisualization.right_click_on_datetree_item('REVENUE_US_BIN_1', 1, 'Add To Query->Horizontal Axis')
        oVisualization.verify_field_listed_under_querytree('Horizontal Axis', 'REVENUE_US_BIN_1', 1, "Step 10a: Verify REVENUE_US_BIN_1 is visible underneath Horizontal Axis")
        
        """    11. Right click on "REVENUE_US_BIN_1" in query pane    """
        """    12. Verify following RMC menu for bin in query pane
        Filter values...
        Sort >
        Visibility >
        Edit Bins...
        Change title
        More >
        Delete    """
        query_list=['Filter Values...', 'Sort', 'Visibility', 'Edit Bins...', 'Change Title...', 'More', 'Delete']
        oVisualization.verify_query_field_context_menu("REVENUE_US_BIN_1", 1, query_list, 'Step 12:')
        
        """    13. Click Edit Bin    """
        oVisualization.select_field_under_query_tree('Horizontal Axis', 1)
        oVisualization.right_click_on_field_under_query_tree("REVENUE_US_BIN_1", 1, "Edit Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        oVisualization.wait_for_number_of_element(parent_css, 1)
        
        """    14. Verify bin dialog opened - Bin dialog opens with input for field name, bin width and format, including a format button and OK button disabled    """
        """    15. Click Cancel    """
        oVisualization.verify_bins_dialog(name_textbox_value='REVENUE_US_BIN_1', format_textbox_value='D20.2M', format_button_visible=True, bin_width_value='100', ok_btn_status='Disabled', btn_click='cancel', msg='Step 14')
        
        """    16. Click Save in the toolbar > Save as "C2348422" > Click Save    """
        oVisualization.save_as_visualization_from_menubar(Test_Case_ID)
        
        """    17. Logout using API - http://machine:port/alias/service/wf_security_logout.jsp    """
        
if __name__ == "__main__":
    unittest.main()