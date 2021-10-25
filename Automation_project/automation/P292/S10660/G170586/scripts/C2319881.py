'''----------------------------------------------------------------------------------------------------
Author Name     : PRABHAKARAN M
Automated On    : 26-JULY-19
Test Case Title : Edit Menu
-----------------------------------------------------------------------------------------------------'''

from common.lib.basetestcase import BaseTestCase
from common.wftools.page_designer import Design
from common.pages.page_designer_design import PageDesignerDesign
from common.lib import utillity, core_utility 
import pyautogui, time

class C2319881_TestClass(BaseTestCase):
    
    def test_C2319881(self):
        
        """ CLASS OBJECTS """  
        pd_design = Design(self.driver)
        utils = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        page_designer = PageDesignerDesign(self.driver)
        
        """ COMMON VARIABLES """
        case_id = 'C2319881'
        
        """
            STEP 01 : Login WF as domain developer. Click on Content view from side bar.
            STEP 02 : Expand 'P292_S10660' domain. Click on 'G192933' folder and choose Page action tile from designer category.
            STEP 03 : Create a page with Blank template.
        """
        pd_design.invoke_page_designer_and_select_template("Blank", from_designer_group=True)
        
        """
            STEP 04 : Click on "G192933 > P292_S10660" domain to two level up;
            Navigate to Retail samples --> Portal --> Test Widgets folder.
        """
        folder_path = "G192933->P292_S10660"
        pd_design.collapse_content_folder(folder_path)
        pd_design.expand_content_folder("Retail Samples->Portal->Test Widgets")
        
        """
            STEP 05 : Drag Blue, Gray, Green and Red onto the page canvas respectively.
        """
        pd_design.drag_content_item_to_blank_canvas("Blue", 1)
        pd_design.drag_content_item_to_blank_canvas("Gray", 4)
        pd_design.drag_content_item_to_blank_canvas("Green", 7)
        pd_design.drag_content_item_to_blank_canvas("Red", 10)
        
        """
            STPE 06 : Click on Gray panel and move it to the left.
            AS of now Blue will shift down.
        """
        pd_design.drag_canvas_container_to_section_cell("Gray", 26)
        blue_container = page_designer.get_container_object("Blue")
        section = page_designer._get_page_section_object(1)
        blue_container_x = int(blue_container.location['x'])
        blue_container_y = int(blue_container.size['height'] + blue_container.location['y'])
        section_x = int(section.location['x'])
        section_y = int(section.size['height'] + section.location['y'])
        status = blue_container_x in range(section_x, section_x + 30) and blue_container_y in range(section_y - 40, section_y)
        utils.asequal(True, status,"Step 06.01 : Blue container shifted to down")
        
        """
            STEP 07 : Drag Blue into the empty space
            Verify Blue container is moved to the empty space.
        """
        pd_design.drag_canvas_container_to_section_cell("Blue", 29)
        container_title = ['Gray', 'Blue', 'Green', 'Red']
        actual_loc = []
        for title in container_title :
            container_x = page_designer.get_container_object(title).location['y']
            actual_loc.append(container_x)
        expected_loc = actual_loc.copy()
        actual_loc.reverse()
        utils.asequal(expected_loc, actual_loc, "Step 07.01 : Verify Blue container is moved to the empty space")
        
        """
            STEP 08 : Drag Red container below Blue.
        """
        red_container = page_designer.get_container_object("Red")
        blue_container = page_designer.get_container_object("Blue")
        source_loc1 = core_utils.get_web_element_coordinate(red_container, "top_middle", yoffset=15)
        source_loc2 = core_utils.get_web_element_coordinate(red_container, "bottom_middle", yoffset=30)
        target_loc = core_utils.get_web_element_coordinate(blue_container, "bottom_middle", yoffset=30)
        pyautogui.click(source_loc1['x'], source_loc1['y'], duration=0.7)
        pyautogui.mouseDown(source_loc1['x'], source_loc1['y'])
        pyautogui.moveTo(source_loc2['x'], source_loc2['y'], duration=0.7)
        time.sleep(1)
        pyautogui.moveTo(target_loc['x'], target_loc['y'], duration=0.7)
        time.sleep(1)
        pyautogui.mouseUp(target_loc['x'], target_loc['y'], duration=0.7)
        time.sleep(1)
        
        """
            STEP 09 : Click Application menu and click Save.
        """
        pd_design.save_as_page_from_application_menu(case_id)
        pd_design.switch_to_previous_window()
        
        """
            STEP 10 : Enter "C2319881" in Title and click Save.
            Verify moved panels does not goes blank.
        """
        pd_design.edit_page_designer(case_id)
        pd_design.drag_canvas_container_to_section_cell("Blue", 29)
        container_title = ['Gray', 'Blue', 'Green']
        actual_loc = []
        for title in container_title :
            container_x = page_designer.get_container_object(title).location['y']
            actual_loc.append(container_x)
        expected_loc = actual_loc.copy()
        actual_loc.reverse()
        utils.asequal(expected_loc, actual_loc, "Step 10.01 : Verify moved panels does not goes blank")
        red_container_x =  page_designer.get_container_object("Red").location['x']
        blue_container_x =  page_designer.get_container_object("Blue").location['x']
        utils.asequal(red_container_x, blue_container_x, "Step 10.02 : Verify moved panels does not goes blank")
        
        """
            STEP 11 : Drag the Red report into the empty space
            Verify Red container is moved to the empty space.
        """
        pd_design.drag_canvas_container_to_section_cell("Red", 35)
        actual_loc = []
        for title in container_title :
            container_x = page_designer.get_container_object(title).location['y']
            actual_loc.append(container_x)
        expected_loc = actual_loc.copy()
        actual_loc.reverse()
        utils.asequal(expected_loc, actual_loc, "Step 11.01 : Verify Red container is moved to the empty space")
        
        """
            STEP 12 : Sign out WF.
        """