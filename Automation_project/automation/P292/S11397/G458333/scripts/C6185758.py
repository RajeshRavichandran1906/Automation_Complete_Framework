"""-------------------------------------------------------------------------------------------
Created on July 02, 2019
@author: Aftab/Samuel

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6185758
Test Case Title =  Add Link tile to the page canvas
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer
from common.wftools import wf_mainpage
from common.lib import utillity, core_utility

class C6185758_TestClass(BaseTestCase):

    def test_C6185758(self):
        
        """
        TESTCASE OBJECTS 
        """
        pd_design=page_designer.Design(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
      
        """
        TESTCASE VARIABLES 
        """
        TEMPLATE_NAME = 'Blank'
        
        """
        TESTCASE CSS
        """
        panels_data_css = ".tpg-selected [data-ibx-type='pdPageSection'] div[data-ibx-type='pdContainer']"
        
        """
        LOCAL FUNCTIONS
        """
        def drag_and_drop(panels_data, index):
            src = core_util_obj.get_web_element_coordinate(panels_data[index], 'bottom_middle')
            core_util_obj.python_left_click(panels_data[index], 'bottom_middle')
            core_util_obj.drag_and_drop_without_using_click(int(src['x']+7), int(src['y']), int(src['x']+7), int(src['y']+60))
            
        def verify_panel_size(panels_data, msg):
            panel1_size = (round(panels_data[0].size['width']), round(panels_data[0].size['height']))
            panel2_size = (round(panels_data[1].size['width']), round(panels_data[1].size['height']))
            panel3_size = (round(panels_data[2].size['width']), round(panels_data[2].size['height']))
            actual_status = (panel1_size==panel2_size==panel3_size)
            util_obj.asequal(True, actual_status, msg)
            
  
        """
        STEP 1 : Login WF as domain developer
        STEP 2 : Click on Content view from side bar
        STEP 3 : Expand 'P292_S11397' domain;Click on 'G458333' folder and click on 'page' action tile from under Designer category
        STEP 4 : Choose blank template
        """
        pd_design.invoke_page_designer_and_select_template(TEMPLATE_NAME)
        
        """
        STEP 5 : Navigate Retail Samples -> Portal -> Test Widgets from the tree;
        Drag and drop 'Blue' to the page canvas.
        """
        pd_design.collapse_content_folder("G458333->P292_S11397")
        pd_design.drag_content_item_to_blank_canvas('Blue', 1, 'Retail Samples->Portal->Test Widgets')
        
        """
        STEP 6 : Click on Containers tab;
        Drag and drop a Panel container to the page canvas after Blue
        """
        pd_design.select_option_from_carousel_items("Containers")
        pd_design.drag_container_item_to_blank_canvas('Panel', 4)
        
        """
        STEP 7 : Click Content tab -> Open Repository Widgets;
        Drag and drop Link tile widget on to the page canvas following the two panels in an orderly fashion
        """
        pd_design.select_option_from_carousel_items("Content")
        pd_design.expand_and_collapse_repository_widgets_tab('expand')
        pd_design.drag_repository_widgets_item_to_blank_canvas('Link tile', 7)
        
        """
        STEP 7.01 : Verify the size of link tile widget is similar to the other two panels already available in the page as below
        """
        panels_data = util_obj.validate_and_get_webdriver_objects(panels_data_css, 'panels_data')
        verify_panel_size(panels_data, "Step 7.01 : Verify the size of link tile widget is similar to the other two panels already available in the page")
        
        """
        STEP 8 : Resize the added 'Blue' content, 'Panel' container and 'Link tile' widget one by one
        """
        drag_and_drop(panels_data, 0)
        drag_and_drop(panels_data, 1)
        drag_and_drop(panels_data, 2)
        
        """
        STEP 8.01 : Verify that 'Link tile' widget behaves in the same way the other two panels do for resize, drag/drop actions as below
        """
        panels_data2 = util_obj.validate_and_get_webdriver_objects(panels_data_css, 'panels_data2')
        verify_panel_size(panels_data2, "Step 8.01 : Verify that 'Link tile' widget behaves in the same way the other two panels do for resize, drag/drop actions")
        
        """
        STEP 9 : Click on Save button;
        Enter title as 'Link tile on the canvas';
        Click save.
        """
        pd_design.save_page_from_toolbar('Link tile on the canvas')
        
        """
        STEP 10 : Close page designer
        """
        pd_design.switch_to_previous_window()
        
        """
        STEP 11 : In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()         