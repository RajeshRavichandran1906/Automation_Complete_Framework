"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 23-September-2021
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9929779_TestClass(BaseTestCase):
    
    def test_C9929779(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        
        
        STEP_01 = """
            STEP 01 : Create new DF content with CAR using API call:
            http://machine:port/alias/designer?master=ibisamp/car&item=IBFS:/WFC/Repository/P215_S31921/G875470&tool=framework
        """
        Designer.API.invoke_new_visualization(credential_keys=('mriddev', 'mrpassdev'), master_file='ibisamp/car')
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Double click 'CAR'.
        """
        Designer.ResourcesPanel.Fields.Dimensions.double_click('COMP->CAR')
        Designer.PropertiesPanel.Settings.Display.Horizontal.wait_for_text('CAR')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Right click 'CAR' in Horizontal bucket.
        """
        Designer.PropertiesPanel.Settings.Display.Horizontal.right_click('CAR')
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Check the context menu option for 'CAR' field.
        """
        Designer.ContextMenu.verify_options(['Add to filter toolbar', 'Bottom axis', 'Top column', 'Sort ascending', 'Sort descending', 'Sort limit', 'Format data', 'Rename', 'Hide', 'Remove'], '03')
        Designer._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Double click 'DEALER_COST'
        """
        Designer.ResourcesPanel.Fields.Measures.double_click('DEALER_COST')
        Designer.PropertiesPanel.Settings.Display.Vertical.wait_for_text('DEALER_COST')
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Right click 'DEALER_COST' in Vertical bucket.
        """
        Designer.PropertiesPanel.Settings.Display.Vertical.right_click('DEALER_COST')
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Check the context menu option for 'DEALER_COST' field.
        """
        Designer.ContextMenu.verify_options(['Add to filter toolbar', 'Left Axis (Y1)', 'Right Axis (Y2)', 'Log scale', 'Shape', 'No sort', 'Sort ascending', 'Sort descending', 'Sort limit', 'Format data', 'Aggregate', 'Quick transform', 'Add calculation', 'Configure drill downs', 'Conditional Styling', 'Rename', 'Hide', 'Remove'], '05')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Drag and drop 'RETAIL_COST' to Size bucket.
        """
        Designer.ResourcesPanel.Fields.Measures.drag_to_bucket('RETAIL_COST', 'Size')
        Designer.PropertiesPanel.Settings.Display.Size.wait_for_text('RETAIL_COST')
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Right click 'RETAIL_COST' in Size bucket.
        """
        Designer.PropertiesPanel.Settings.Display.Size.right_click('RETAIL_COST')
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Check the context menu option for 'RETAIL_COST' field.
        """
        Designer.ContextMenu.verify_options(['Add to filter toolbar', 'Format data', 'Aggregate', 'Quick transform', 'Add calculation', 'Conditional Styling', 'Rename', 'Remove'], '07')
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Drag and drop 'COUNTRY' to Color bucket
        """
        Designer.ResourcesPanel.Fields.Dimensions.drag_to_bucket('COUNTRY', 'Color')
        Designer.PropertiesPanel.Settings.Display.Color.wait_for_text('COUNTRY')
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Right click 'COUNTRY' in Color bucket.
        """
        Designer.PropertiesPanel.Settings.Display.Color.right_click('COUNTRY')
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Check the context menu option for 'COUNTRY' field.
        """
        Designer.ContextMenu.verify_options(['Add to filter toolbar', 'Sort ascending', 'Sort descending', 'Sort limit', 'Format data', 'Rename', 'Hide', 'Remove'], '09')
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Drag and drop 'SALES' to Tooltip bucket.
        """
        Designer.ResourcesPanel.Fields.Measures.drag_to_bucket('SALES', 'Tooltip')
        Designer.PropertiesPanel.Settings.Display.Tooltip.wait_for_text('SALES')
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Right click 'SALES' in Tooltip bucket.
        """
        Designer.PropertiesPanel.Settings.Display.Tooltip.right_click('SALES')
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Check the context menu option for 'SALES' field.
        """
        Designer.ContextMenu.verify_options(['Add to filter toolbar', 'Format data', 'Aggregate', 'Quick transform', 'Add calculation', 'Conditional Styling', 'Rename', 'Remove'], '11')
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Drag and drop 'BODYTYPE' to Animate bucket.
        """
        Designer.ResourcesPanel.Fields.Dimensions.drag_to_bucket('CARREC->BODY->BODYTYPE', 'Animate')
        Designer.PropertiesPanel.Settings.Display.Animate.wait_for_text('BODYTYPE')
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Right click 'BODYTYPE' in Animate bucket.
        """
        Designer.PropertiesPanel.Settings.Display.Animate.right_click('BODYTYPE')
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Check the context menu option for 'BODYTYPE' field.
        """
        Designer.ContextMenu.verify_options(['Add to filter toolbar', 'Sort ascending', 'Sort descending', 'Sort limit', 'Format data', 'Rename', 'Hide', 'Remove'], '13')
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Drag and drop 'MODEL' to MultiPage bucket.
        """
        Designer.ResourcesPanel.Fields.Dimensions.drag_to_bucket('CARREC->MODEL', 'MultiPage')
        Designer.PropertiesPanel.Settings.Display.MultiPage.wait_for_text('MODEL')
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Right click 'MODEL' in MultiPage bucket.
        """
        Designer.PropertiesPanel.Settings.Display.MultiPage.right_click('MODEL')
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Check the context menu option for 'MODEL' field.
        """
        Designer.ContextMenu.verify_options(['Add to filter toolbar', 'Sort ascending', 'Sort descending', 'Sort limit', 'Format data', 'Number of columns', 'Rename', 'Hide', 'Remove'], '15')
        Designer._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Click on the WebFOCUS DESIGNER dropdown and Select 'Close'.
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer.ContextMenu.select('Close')
        Designer._utils.capture_screenshot("16", STEP_16)

        STEP_17 = """
            STEP 17 : Click 'NO' button.
        """
        Designer.Dialog.Alert.No.click()
        Designer._utils.capture_screenshot("17", STEP_17)

        STEP_18 = """
            STEP 18 : Logout using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("18", STEP_18)