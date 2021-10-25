"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 12-October-2021
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9929774_TestClass(BaseTestCase):
    
    def test_C9929774(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        
        """
        TEST CASE VARIABLES
        """
        riser_css = "[class='riser!s0!g3!mbar!']"
        riser_css2 = "[class='riser!s0!g0!mbar!']"
        riser_css3 = "[class='riser!s0!g1!mbar!']"
        
        STEP_01 = """
            STEP 01 : Create new DF content with wf_retail_lite using API call:
            http://machine:port/alias/designer?master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/P215_S31921/G875470&tool=framework
        """
        Designer.API.invoke_new_visualization(credential_keys=('mriddev', 'mrpassdev'), master_file='retail_samples/wf_retail_lite')
        Designer._utils.capture_screenshot("01", STEP_01)
    
        STEP_02 = """
            STEP 02 : Double click 'Product,Category' and 'Cost of Goods'
        """
        Designer.ResourcesPanel.Fields.Dimensions.double_click('Product->Product Category')
        Designer.VisualizationCanvas.Bar.wait_for_text('Product Category')
        Designer.ResourcesPanel.Fields.Measures.double_click('Cost of Goods')
        Designer.VisualizationCanvas.Bar.wait_for_text('Cost of Goods')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Check Fields added to query pane and canvas updated.
        """
        Designer.PropertiesPanel.Settings.Display.Horizontal.verify_available_fields(['Product Category'], '02.01')
        Designer.PropertiesPanel.Settings.Display.Vertical.verify_available_fields(['Cost of Goods'], '02.02')
        Designer.VisualizationCanvas.Bar.verify_xaxis_title(['Product Category'], '02.03')
        Designer.VisualizationCanvas.Bar.verify_xaxis_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '02.04')
        Designer.VisualizationCanvas.Bar.verify_yaxis_title(['Cost of Goods'], '02.05')
        Designer.VisualizationCanvas.Bar.verify_yaxis_labels(['0', '40M', '80M', '120M', '160M', '200M', '240M'], '02.06')
        Designer.VisualizationCanvas.Bar.verify_number_of_risers(7, '02.07')
        Designer.VisualizationCanvas.Bar.verify_riser_color([(1, 'bar_blue'), (7, 'bar_blue')], '02.08')
        Designer._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Click 'Content' under Settings tab.
        """
        Designer._utils.capture_screenshot("03", STEP_03)
        STEP_04 = """
            STEP 04 : Click 'AutoDrill' checkbox under 'Interactivity'.
        """
        Designer.PropertiesPanel.Settings.ContentSettings.AutoDrill.check()
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Click Run in new window in the toolbar.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Check the chart output.
        """
        Designer.VisualizationCanvas.RunMode.switch_to_frame()
        Designer.VisualizationCanvas.RunMode.Bar.wait_for_text('Product Category', time_out=120)
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_title(['Product Category'], '05.01')
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '05.02')
        Designer.VisualizationCanvas.RunMode.Bar.verify_yaxis_title(['Cost of Goods'], '05.03')
        Designer.VisualizationCanvas.RunMode.Bar.verify_yaxis_labels(['0', '40M', '80M', '120M', '160M', '200M', '240M'], '05.04')
        Designer.VisualizationCanvas.RunMode.Bar.verify_number_of_risers(7, '05.05')
        Designer.VisualizationCanvas.RunMode.Bar.verify_riser_color([(1, 'bar_blue'), (7, 'bar_blue')], '05.06')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Hover over 'Media Player' riser.
        """
        Designer.VisualizationCanvas.RunMode.AutoDrill.hover_chart_riser(riser_css)
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Check the tooltip.
        """
        Designer.VisualizationCanvas.RunMode.AutoDrill.verify_tooltip_values(['Product Category:', 'Media Player', 'Cost of Goods:', '$190,240,481.00'], '06.01')
        Designer.VisualizationCanvas.RunMode.AutoDrill.verify_autodrill_options(['Drill down to Product Subcategory'], '06.02')
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click 'Drill down to Product Subcategory'
        """
        Designer.VisualizationCanvas.RunMode.AutoDrill.select_autodrill_option('Drill down to Product Subcategory')
        Designer._utils.capture_screenshot("07", STEP_07)
        
        STEP_07_EXPECTED = """
            STEP 07 - Expected : Check the chart output.
        """ 
        Designer.VisualizationCanvas.RunMode.Bar.wait_for_text('Blu Ray', time_out=30)
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_title(['Product Subcategory'], '07.01')
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_labels(['Blu Ray', 'DVD Players', 'DVD Players - Portable', 'Streaming'], '07.02')
        Designer.VisualizationCanvas.RunMode.Bar.verify_yaxis_title(['Cost of Goods'], '07.03')
        Designer.VisualizationCanvas.RunMode.Bar.verify_yaxis_labels(['0', '40M', '80M', '120M', '160M', '200M'], '07.04')
        Designer.VisualizationCanvas.RunMode.Bar.verify_number_of_risers(4, '07.05')
        Designer.VisualizationCanvas.RunMode.Bar.verify_riser_color([(1, 'bar_blue'), (4, 'bar_blue')], '07.06')
        Designer.VisualizationCanvas.RunMode.BreadCrumbTrail.verify_bread_crumb_trail(['Home', '(Product Category) Media Player'], '7.07')
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Hover over 'Blu Ray' riser.
        """
        Designer.VisualizationCanvas.RunMode.AutoDrill.hover_chart_riser(riser_css2)
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Check the tooltip.
        """
        Designer.VisualizationCanvas.RunMode.AutoDrill.verify_tooltip_values(['Product Subcategory:', 'Blu Ray', 'Cost of Goods:', '$181,112,921.00'], '08.01')
        Designer.VisualizationCanvas.RunMode.AutoDrill.verify_autodrill_options(['Reset', 'Go up to Product Category', 'Drill down to Model'], '08.02')
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Click 'Drill down to Model'
        """
        Designer.VisualizationCanvas.RunMode.AutoDrill.select_autodrill_option('Drill down to Model')
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Check the chart output.
        """
        Designer.VisualizationCanvas.RunMode.Bar.wait_for_text('JVC XV-BP1', time_out=30)
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_title(['Model'], '09.01')
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_labels(['JVC XV-BP1', 'JVC XV-BP10', 'JVC XV-BP11', 'Panasonic DMP-BD30', 'Panasonic DMP-BD60', 'Panasonic DMP-BD70V', 'Panasonic DMP-BD80', 'Pioneer BDP-120', 'Pioneer BDP-320', 'Pioneer BDP-330', 'Pioneer BDP-51', 'SAMSUNG BD-C6500', 'SHARP BD-HP70U', 'Samsung BD-C5500', 'Samsung BD-P1600', 'Samsung BD-P3600', 'Sharp BD-HP24U', 'Sony BDP-S360', 'Sony BDP-S370', 'Sony BDP-S470', 'Sony BDP-S570'], '09.02')
        Designer.VisualizationCanvas.RunMode.Bar.verify_yaxis_title(['Cost of Goods'], '09.03')
        Designer.VisualizationCanvas.RunMode.Bar.verify_yaxis_labels(['0', '3M', '6M', '9M', '12M', '15M'], '09.04')
        Designer.VisualizationCanvas.RunMode.Bar.verify_number_of_risers(21, '09.05')
        Designer.VisualizationCanvas.RunMode.Bar.verify_riser_color([(1, 'bar_blue'), (19, 'bar_blue')], '09.06')
        Designer.VisualizationCanvas.RunMode.BreadCrumbTrail.verify_bread_crumb_trail(['Home', '(Product Category) Media Player', '(Product Subcategory) Blu Ray'], '09.07')
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Hover over 'JVC XV-BP10' riser and Click 'Restore Original'
        """
        Designer.VisualizationCanvas.RunMode.AutoDrill.select_autodrill_option("Reset", riser_css=riser_css3, hover_wait=True)
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Check the chart output.
        """
        Designer.VisualizationCanvas.RunMode.Bar.wait_for_text('Accessories', time_out=30)
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_title(['Product Category'], '10.01')
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '10.02')
        Designer.VisualizationCanvas.RunMode.Bar.verify_yaxis_title(['Cost of Goods'], '10.03')
        Designer.VisualizationCanvas.RunMode.Bar.verify_yaxis_labels(['0', '40M', '80M', '120M', '160M', '200M', '240M'], '10.04')
        Designer.VisualizationCanvas.RunMode.Bar.verify_number_of_risers(7, '10.05')
        Designer.VisualizationCanvas.RunMode.Bar.verify_riser_color([(1, 'bar_blue'), (7, 'bar_blue')], '10.06')
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Close the Designer Run in new window
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Click 'Save' Enter 'C9929774_base' in Title and Click 'Save as' button.
        """
        Designer.ToolBar.save('C9929774_base')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : STEP 12 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Restore C9929774_base fex using API:
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P215_S31921/G875470/c9929774.fex&startlocation=IBFS:/WFC/Repository/P215_S31921/G875470
        """
        Designer.API.edit_fex("C9929774_base", credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Check 'C9929774_base' is restored successfully.
        """
        Designer.VisualizationCanvas.Bar.wait_for_text('Cost of Goods')
        Designer.PropertiesPanel.Settings.Display.Horizontal.verify_available_fields(['Product Category'], '14.01')
        Designer.PropertiesPanel.Settings.Display.Vertical.verify_available_fields(['Cost of Goods'], '14.02')
        Designer.VisualizationCanvas.Bar.verify_xaxis_title(['Product Category'], '14.03')
        Designer.VisualizationCanvas.Bar.verify_xaxis_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '14.04')
        Designer.VisualizationCanvas.Bar.verify_yaxis_title(['Cost of Goods'], '14.05')
        Designer.VisualizationCanvas.Bar.verify_yaxis_labels(['0', '40M', '80M', '120M', '160M', '200M', '240M'], '14.06')
        Designer.VisualizationCanvas.Bar.verify_number_of_risers(7, '14.07')
        Designer.VisualizationCanvas.Bar.verify_riser_color([(1, 'bar_blue'), (7, 'bar_blue')], '14.08')
        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Click 'Content' under Settings tab.
        """
        Designer._utils.capture_screenshot("15", STEP_15)
        STEP_15_EXPECTED = """
            STEP 15 - Expected : Check 'AutoDrill' is enabled under 'Interactivity'.
        """
        Designer.PropertiesPanel.Settings.ContentSettings.AutoDrill.verify_checked('15')
        Designer._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Logout using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("16", STEP_16)