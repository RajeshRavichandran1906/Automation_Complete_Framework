"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 20 July 2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927891_TestClass(BaseTestCase):
    
    def test_C9927891(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)

        STEP_01 = """
            STEP 01 : Sign into WebFOCUS as Administrator.
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' from the tree and Click Retail samples --> Portal --> Small widgets
        """
        HomePage.Workspaces.ResourcesTree.expand_workspaces()
        HomePage.Workspaces.ResourcesTree.select('Retail Samples->Portal->Small Widgets')
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_04 = """
            STEP 04 : Double Click 'Category Sales' procedure.
        """
        category_sales = "Category Sales"
        HomePage.Workspaces.ContentArea.double_click_on_file(category_sales)
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.RunWindow.locators.title[1], category_sales, 30)
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify that the Preview Window appears
        """
        HomePage.RunWindow.verify_title(category_sales, '04.01')
        HomePage.Home._utils.capture_screenshot('04.01', STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Close the Preview Window.
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_06 = """
            STEP 06 : Click on 'Test Widgets' folder from resource tree and Double Click 'Blue' procedure.
        """
        blue = "Blue"
        HomePage.Workspaces.ResourcesTree.select('Test Widgets')
        HomePage.Workspaces.ContentArea.double_click_on_file(blue)
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.RunWindow.locators.title[1], blue, 30)
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify that the Preview Window appears
        """
        HomePage.RunWindow.verify_title(blue, '06.01')
        HomePage.Home._utils.capture_screenshot('06.01', STEP_06_01, True)
        
        STEP_07 = """
            STEP 07 : Close the Preview Window.
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_08 = """
            STEP 08 : Right click on 'Blue' procedure and Click 'View' option from context menu.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(blue)
        HomePage.ContextMenu.select('View')
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.RunWindow.locators.title[1], blue, 30)
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_08_01 = """
            STEP 08.01 : Verify that the Preview Window appears
        """
        HomePage.RunWindow.verify_title(blue, '08.01')
        HomePage.Home._utils.capture_screenshot('08.01', STEP_08_01, True)
        
        STEP_09 = """
            STEP 09 : Close the Preview Window.
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_10 = """
            STEP 10 : Click on 'Small Widgets' folder from resource tree.
        """
        HomePage.Workspaces.ResourcesTree.select('Small Widgets')
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)
        
        STEP_11 = """
            STEP 11 : Right click on 'Category Sales' procedure and Click 'Run' option from context menu.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(category_sales)
        HomePage.ContextMenu.select('Run')
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.RunWindow.locators.title[1], category_sales, 30)
        HomePage.Home._utils.capture_screenshot('11.00', STEP_11)
        
        STEP_11_01 = """
            STEP 11.01 : Verify that the Preview Window appears
        """
        HomePage.RunWindow.verify_title(category_sales, '11.01')
        HomePage.Home._utils.capture_screenshot('11.01', STEP_11_01, True)
        
        STEP_12 = """
            STEP 12 : Close the Preview Window.
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot('12.00', STEP_12)
        
        STEP_13 = """
            STEP 13 : Right click on 'Category Sales' procedure and Hover over 'Run..' then Click 'Run in new window' option from context menu.
        """
        legend_css = "#jschart_HOLD_0 .legend-title"
        HomePage.Workspaces.ContentArea.right_click_on_file(category_sales)
        HomePage.ContextMenu.select('Run...->Run in new window')
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_visble_text(legend_css, 'Product Category', 120)
        HomePage.Home._utils.capture_screenshot('13.00', STEP_13)
        
        STEP_13_01 = """
            STEP 13.01 : Verify that it runs in another tab
        """
        legend_title = self.driver.find_element_by_css_selector(legend_css).text.strip()
        HomePage.Home._utils.asequal('Product Category', legend_title, 'Step 13.01 : Verify "Category Sales" runs in another bowser tab')
        HomePage.Home._utils.capture_screenshot('13.01', STEP_13_01, True)
        
        STEP_14 = """
            STEP 14 : Close that window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot('14.00', STEP_14)
        
        STEP_15 = """
            STEP 15 : Click on 'Test Widgets' folder from resource tree.
        """
        HomePage.Workspaces.ResourcesTree.select('Test Widgets')
        HomePage.Home._utils.capture_screenshot('15.00', STEP_15)
        
        STEP_16 = """
            STEP 16 : Right click on 'Blue' procedure and Click 'View in new window' option from context menu.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(blue)
        HomePage.ContextMenu.select('View in new window')
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot('16.00', STEP_16)
        
        STEP_16_01 = """
            STEP 16.01 : Verify that it runs in another tab
        """
        HomePage.Home._utils.verify_element_color_using_css_property('body', 'blue', 'Step 16.01 : Verify "Blue" runs in another tab', attribute='background-color')
        HomePage.Home._utils.capture_screenshot('16.01', STEP_16_01, True)
        
        STEP_17 = """
            STEP 17 : Close that window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot('17.00', STEP_17)
        
        STEP_18 = """
            STEP 18 : Right click on 'Blue' procedure and choose 'Add to favorites' option
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(blue)
        HomePage.ContextMenu.select('Add to Favorites')
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot('18.00', STEP_18)
        
        STEP_19 = """
            STEP 19 : Click on 'WebFOCUS' Logo
        """
        HomePage.Banner.click_home()
        HomePage.Home._utils.capture_screenshot('19.00', STEP_19)
        
        STEP_19_01 = """
            STEP 19.01 : Verify the 'Blue' procedure is dispalyed under FAVORITES.
        """
        HomePage.Home.Favorites.verify_items([blue], '19.01')
        HomePage.Home._utils.capture_screenshot('19.01', STEP_19_01, True)
        
        STEP_20 = """
            STEP 20 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('20.00', STEP_20)