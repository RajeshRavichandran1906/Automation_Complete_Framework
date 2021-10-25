"""-------------------------------------------------------------------------------------------
Created on May 23, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262081
Test Case Title =  Create and Preview PGX for Section Theme and Grid style
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools import page_designer


class C8262081_TestClass(BaseTestCase):

    def test_C8262081(self):
        
        """
            CLASS OBJECTS 
        """
        pd_design=page_designer.Design(self.driver)
        pd_preview=page_designer.Preview(self.driver)
        homepage = Wf_Mainpage(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        LONG_TIME = 40
        TEMPLATE_NAME = "Grid 2-1"
        COLLAPSE_FOLDER_PATH = "G513470->P292_S19901"
        CONTENT_ITEM = "Category Sales"
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User.
            STEP 02 : Expand 'P292_S19901' domain > click on G513470 folder
            STEP 03 : Click on Designer and Create a new PGX Page using Grid 2-1 template
        """
        pd_design.invoke_page_designer_and_select_template(TEMPLATE_NAME)
        
        """
            STEP 04 : Click section on the page canvas
        """
        pd_design.select_page_section(1)
        
        """
            STEP 05 : From the designer toolbar,click on Properties button > click style tab.
        """
        pd_design.click_property()
        pd_design.select_property_tab("Style")
        
        """
            STEP 05 : Expected - Verify Section style appears with 8 options (default, style 2to style 8)
        """
        pd_design.verify_section_style_options("05.01")
        
        """
            STEP 06 : Select Style 2
        """
        pd_design.select_section_style("Style 2")
        
        """
            STEP 07 : Click on left arrow to G513470 folder > P292_S19901 domain.
        """
        pd_design.collapse_content_folder(COLLAPSE_FOLDER_PATH)
        
        """
            STEP 07 : Expected - Verify Domains appears.
        """
        pd_design.verify_page_domain_tree_node(["Domains"], "Step 07.01 : Verify Domains appears")
        
        """
            STEP 08 : Drag and drop 'Category Sales' onto the Panel 1.
        """
        pd_design.drag_content_item_to_container(CONTENT_ITEM, "Panel 1")
        
        """
            STEP 09 : Click Containers tab. Drag and drop the grid container onto the Panel 2.
        """
        pd_design.select_option_from_carousel_items("Containers")
        pd_design.drag_basic_container_to_canvas_container("Grid", "Panel 2")
        
        """
            STEP 10 : From the designer toolbar, click on Page filter configuration button.
        """
        pd_design.click_filter_configuration()
        
        """
            STEP 10 : Expected - Verify that Page Filter Configuration opens.
            STEP 11 : Click on Create empty filter bar.
        """
        pd_design.select_filter_configurations_property("Create empty filter bar")
        
        """
            STEP 12 : Right click on first cell in Panel 2 > click Add filter controls.
        """
        pd_design.select_container_context_menu("Panel 2", "Add filter controls")
        
        """
            STEP 12 : Expected - Verify Add Filter Controls dialog box opens.
        """
        pd_design.add_filter_controls_dialog().verify_title("12.01")
        
        """
            STEP 13 : Unchecked BUSINESS_REGION,STORE_TYPE, TIME_DATE and TIME_DATE_TO.
        """
        pd_design.add_filter_controls_dialog("BUSINESS_REGION").uncheck()
        pd_design.add_filter_controls_dialog("STORE_TYPE").uncheck()
        pd_design.add_filter_controls_dialog("TIME_DATE").uncheck()
        pd_design.add_filter_controls_dialog("TIME_DATE_TO").uncheck()
        
        """
            STEP 14 : Click on Add filter controls.
        """
        pd_design.add_filter_controls_dialog().click_add_filter_controls_button()
        
        """
            STEP 14 : Expected - Verify grid panel populated with some controls and quick filters shows 4 inside the red circle.
        """
        pd_design.verify_quick_filter_properties({'text':'4', 'background_color':'mandy'}, "Step 14.01")
        pd_design.verify_filter_control_labels(['Category:', 'Product Model:'], "Step 14.02 : Verify grid panel populated with some controls", grid_container_title="Panel 2")
        
        """
            STEP 15 : Click on quick filer button.
        """
        pd_design.click_quick_filter()
        
        """
            STEP 15 : Expected - Verify page filter populated with some controls.
        """
        pd_design.verify_filter_control_labels(['Region:', 'Store Type:', 'From:', 'To:'], "Step 15.01 : Verify grid panel populated with some controls",)
        
        """
            STEP 16 : Click on the Panel 2 (grid container).
        """
        pd_design.select_container("Panel 2")
        
        """
            STEP 17 : Choose Style 3 in Properties panel
        """
        pd_design.select_container_style("Style 3")
        
        """
            STEP 17 : Expected - Verify that the whole grid area has now style 3
        """
        pd_design.verify_container_style_color("Panel 2", "fern2", "17.01")
        
        """
            STEP 18 : Click on the page filter area and choose Style 4.
        """
        pd_design.select_filter_grid_cell(1)
        pd_design.select_grid_style("Style 4")
        
        """
            STEP 18 : Expected - Verify that the whole grid area has now style 4 and the grid panel has style 2 and 3 still set
        """
        pd_design.verify_container_style_color("Panel 2", "fern2", "18.01")
        pd_design.verify_page_section_style_color(1, "curious_blue", "18.02")
        pd_design.verify_filter_grid_style_color("Sea_Serpent", "18.03")
        
        """
            STEP 19 : Click on Page filter configuration button > Change to Filter modal window > Click OK.
        """
        pd_design.click_filter_configuration()
        pd_design.select_filter_configurations_property("Filter modal window")
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterWindow']", "Selections", LONG_TIME)
        
        """
            STEP 19 : Expected - Verify all the changes still exist as below
        """
        pd_design.verify_filter_grid_style_color("Sea_Serpent", "19.01", model_window=True)
        pd_design.verify_filter_control_labels(['Region:', 'Store Type:', 'From:', 'To:'], "Step 18.02 : Verify grid panel populated with some controls", model_window=True)
       
        """
            STEP 20 : Click the preview button.
        """
        pd_design.click_preview()
        
        """
            STEP 20 : Expected - Verify all the changes still exist
        """
        pd_preview.verify_containers_title(['Category Sales', 'Panel 2', 'Panel 3'], "Step 20.01 : Verify 3 panels appear in preview canvas")
        pd_preview.verify_page_section_style_color(1, "curious_blue", "20.02")
        pd_preview.verify_container_style_color("Panel 2", "fern2", "20.03")
        pd_preview.verify_filter_control_labels(['Category:', 'Product Model:'], "Step 20.04 : Verify grid panel populated with some controls", grid_container_title="Panel 2")
        pd_preview.verify_page_heading_title(['Page Heading'], "Step 20.05 : Verify page heading title")
        pd_preview.verify_page_header_visible_buttons(['Refresh', 'Show filters'], 'Step 20.06 : Verify Refresh and Filter buttons are display on page header in preview')
        
        """
            STEP 21 : Click on the filter button to bring up the modal.
        """
        pd_preview.click_show_filters()
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterWindow']", "Selections", LONG_TIME)
        
        """
            STEP 21 : Expected - Verify all the changes still exist
        """
        pd_preview.verify_filter_control_labels(['Region:', 'Store Type:', 'From:', 'To:'], "Step 21.01 : Verify grid panel populated with some controls", model_window=True)
        pd_preview.verify_filter_grid_style_color("Sea_Serpent", "21.02", model_window=True)
        
        """
            STEP 22 : Close the Filter modal window selection dialog box.
        """
        pd_preview.close_filter_model_window()
        
        """
            STEP 23 : Click on preview button to back to page designer canvas.
        """
        pd_preview.go_back_to_design_from_preview()
        
        """
            STEP 24 : Click on Save button and give 'section theme and grid styling'> click save and Close the Page Designer from application menu.
        """
        pd_design.save_page_from_toolbar("section theme and grid styling")
        pd_design.switch_to_previous_window()
        
        """
            STEP 25 : In the banner link, click on the top right username > Click Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()