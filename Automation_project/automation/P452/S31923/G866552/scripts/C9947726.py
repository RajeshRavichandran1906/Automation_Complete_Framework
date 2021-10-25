"""-------------------------------------------------------------------------------------------
Author Name  : BM13368
Automated On : 09-December-2020
-------------------------------------------------------------------------------------------"""
from common.wftools.reports import Reports
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer import Designer
import re
import pyautogui as pyauto
import pyperclip as pc
import time

class C9947726_TestClass(BaseTestCase):
    
    def test_C9947726(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        DesignerPage = Designer()
        HtmlReport = Reports().HTML5()
                                        
        """
        TEST CASE VAIABLES
        """
        file_name="C9947726"
        panel_content1 ="chartDrilldown"
        panel_content2 ="reportDrilldown"
        panel1 = 'Container 1'
        panel2 = 'Container 2'
        data_set1 = file_name  +"_DataSet01"
        data_set2 = file_name  +"_DataSet02"
        data_set3 = file_name  +"_DataSet03"
        
        STEP_01 = """
            STEP 01 : Login WF as domain developer
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select Workspaces and navigate to 'P452_S31923/G866552' folder;
            Click on '+' button in top bar and select Assemble Visualizations.
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Workspaces.ResourcesTree.select('P452_S31923->G866552')
        HomePage.Workspaces._utils.wait_for_page_loads(20)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool("Assemble Visualization")
        HomePage.Home._core_utils.switch_to_new_window("Designer")
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Choose Grid 2-1 template.
        """
        DesignerPage._utils.wait_for_page_loads(30)
        DesignerPage.Dialog.ChooseTemplate.Common.select("Grid 2-1")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Drag 'chartDrilldown' onto the Container 1.
        """
        DesignerPage.ResourcesPanel.Content.drag_to_container(panel_content1, container_title=panel1)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Copy the Content ID of Container 1 content from Settings.
        """
        DesignerPage.PropertiesPanel.Settings.ContentSettings.ID.click()
        pyauto.hotkey('ctrl','a')
        pyauto.hotkey('ctrl','c')
        page_content_id=pc.paste()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Edit reportDrilldown with Text Editor without closing the page.
        """
        self.driver.execute_script('''window.open("http://google.com","_blank");''')
        DesignerPage._core_utils.switch_to_new_window('Google')
        DesignerPage.API.edit_fex_in_texteditor(panel_content2, workspace_folder='P452_S31923/G866552')
        text_editor=self.driver.find_element_by_css_selector("[data-ibx-type='aceEditor'] .ace_content")
        text_editor.click()
        pyauto.hotkey('ctrl','a')          
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Paste the copied Content ID in TARGET and update the FOCEXEC path of the targetReport report.
        """
        COPY_BUTTON_CSS="div.te-menu-button[title='Copy']"
        copy_btn_object=self.driver.find_element_by_css_selector(COPY_BUTTON_CSS)
        copy_btn_object.click()
        time.sleep(10)
        text_editor.click()
        copied_code=pc.paste()
        pyauto.hotkey('ctrl','h')                                
        find=self.driver.find_element_by_css_selector("div.findText [role='textbox']")         
        replace=self.driver.find_element_by_css_selector("div.replaceText [role='textbox']")
        find_text=re.findall(r"'[^A-B]\w{6}-\w+'", copied_code)
        find.click()
        time.sleep(10)
        find.send_keys(find_text)
        replace.click()
        time.sleep(15)
        replace_page_content_id="\'"+page_content_id+"\'"
        replace.send_keys(replace_page_content_id)
        replace_button=self.driver.find_element_by_css_selector("div.btnReplaceAll[role='button']")
        replace_button.click()
        time.sleep(15)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Save and close the editor.
        """
        SAVE_CSS="div.te-menu-button[title='Save']"
        save=self.driver.find_element_by_css_selector(SAVE_CSS)
        save.click()
        time.sleep(15)
        DesignerPage._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Drag and drop reportDrilldown onto the Container 2
        """
        DesignerPage.ResourcesPanel.Content.drag_to_container(panel_content2, container_title=panel2)
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Click Run in new window icon in the toolbar
        """
        DesignerPage.VisualizationToolBar.RunInNewWindow.click()
        DesignerPage._core_utils.switch_to_new_window()
        DesignerPage.RunMode.PageCanvas.wait_for_text(panel_content2)
        DesignerPage.RunMode.PageCanvas.Containers.Basic(panel_content2).switch_to_frame()
        HtmlReport.wait_for_text('SALES')
        #HtmlReport.convert_to_excel(data_set1)
        HtmlReport.verify_data(data_set1, '10.01')
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Click on ENGLAND in Container 2.
        """
        HtmlReport.click_on_hyperlink_cell(2, 1)
        DesignerPage._core_utils.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify panel 1 is updated with target report.
        """
        DesignerPage.RunMode.PageCanvas.wait_for_text(panel_content1)
        DesignerPage.RunMode.PageCanvas.Containers.Basic(panel_content1).switch_to_frame()
        HtmlReport.wait_for_text('SALES', time_out=160)
        #HtmlReport.convert_to_excel(data_set2)
        HtmlReport.verify_data(data_set2, '11.01')
        DesignerPage._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Click Save and enter C9947726 in Title and click Save;
            Close the designer.
        """
        DesignerPage.ToolBar.save(file_name)
        DesignerPage._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Right click on 'C9947726' and select Run.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file(file_name)
        HomePage.ContextMenu.select('Run')
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Click on FRANCE in Container 2.
        """
        DesignerPage.RunMode.PageCanvas.wait_for_text(panel_content2)
        DesignerPage.RunMode.PageCanvas.Containers.Basic(panel_content2).switch_to_frame()
        HtmlReport.wait_for_text('SALES',time_out=160)
        HtmlReport.click_on_hyperlink_cell(6, 1)
        DesignerPage._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify panel 1 is updated with target report.
        """
        DesignerPage.RunMode.PageCanvas.wait_for_text(panel_content1)
        DesignerPage.RunMode.PageCanvas.Containers.Basic(panel_content1).switch_to_frame()
        HtmlReport.wait_for_text('SALES',time_out=160)
        #HtmlReport.convert_to_excel(data_set3)
        HtmlReport.verify_data(data_set3, '14.01')
        DesignerPage._core_utils.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Close the designer.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : Sign out WF.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("16", STEP_16)