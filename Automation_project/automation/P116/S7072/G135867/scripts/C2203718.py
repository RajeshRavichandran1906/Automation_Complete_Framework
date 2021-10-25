'''
Created on April 25, 2017

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203718
Description = Verify user can link any report to the existing report
'''
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.pages import active_miscelaneous, visualization_ribbon, visualization_metadata, visualization_resultarea, ia_run, ia_ribbon
from common.pages import ia_resultarea
from common.lib import utillity
import unittest,time, re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2203718_TestClass(BaseTestCase):

    def test_C2203718(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultareaobj = ia_resultarea.IA_Resultarea(self.driver)
        result_obj= visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_ribobj = ia_ribbon.IA_Ribbon(self.driver)
        Test_Case_ID = 'C2203718'
        
        """
        Step 01: Right click on folder created in IA and select New > Report and select Reporting server as GGSALES.
        """
        utillobj.infoassist_api_login('report', 'ibisamp/ggsales', 'P116/S7072', 'mrid', 'mrpass')
        elem=(By.CSS_SELECTOR,'#TableChart_1')
        resultareaobj._validate_page(elem)
        parent_css="#TableChart_1 [align='justify']"
        str_val="Draganddropfieldsontothecanvasorintothequerypanetobeginbuildingyourreport."
        result_obj.wait_for_property(parent_css, 1, string_value=str_val, with_regular_exprestion=True)
        time.sleep(1)
        
        
        """
        Step 02: On the Format tab, in the Output Types group, click Active Report.
        """
        ribbonobj.change_output_format_type('active_report')
        parent_css="#HomeFormatType"
        str_val="ActiveReport"
        result_obj.wait_for_property(parent_css, 1, string_value=str_val, with_regular_exprestion=True)
        time.sleep(1)
        
        
        """
        Step 03: Select data from the left pane (Dimensions and Measures) Category, Product ID, Product, State, Unit Sales, Dollar Sales.
        """
        metadataobj.datatree_field_click('Category', 2, 1)
        parent_css="#TableChart_1 [id^='ActivePreviewItem']"
        result_obj.wait_for_property(parent_css, 2)
        time.sleep(1)
        metadataobj.datatree_field_click('Product ID', 2, 1)
        parent_css="#TableChart_1 [id^='ActivePreviewItem']"
        result_obj.wait_for_property(parent_css, 4)
        time.sleep(1)
        metadataobj.datatree_field_click('Product', 2, 1)
        parent_css="#TableChart_1 [id^='ActivePreviewItem']"
        result_obj.wait_for_property(parent_css, 6)
        time.sleep(1)
        metadataobj.datatree_field_click('State', 2, 1)
        parent_css="#TableChart_1 [id^='ActivePreviewItem']"
        result_obj.wait_for_property(parent_css, 8)
        time.sleep(1)
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 [id^='ActivePreviewItem']"
        result_obj.wait_for_property(parent_css, 10)
        time.sleep(1)
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)
        parent_css="#TableChart_1 [id^='ActivePreviewItem']"
        result_obj.wait_for_property(parent_css, 12)
        time.sleep(1)
        coln_list = ['Category', 'Product ID', 'Product', 'State']
        result_obj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 03.1: Verify column titles")
        time.sleep(2)
#         resultareaobj.create_report_data_set('TableChart_1', 19, 6, 'C2203718_Ds01.xlsx')
        resultareaobj.verify_report_data_set('TableChart_1', 19, 6, 'C2203718_Ds01.xlsx','Step 03.2: Verify data is displayed in the Live Preview pane')
 
        """
        Step 04: Click Run command.
        """
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(3)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it
            ((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
         
        """ Step 05: Verify Active Report is displayed and all the report menu options are present on a report Save as AR-RP-001 and exit the report
        """
        time.sleep(2)
        parent_css="table#ITableData0 tr:nth-child(2) td:nth-child(1)"
        result_obj.wait_for_property(parent_css, 1, string_value='Coffee', with_regular_exprestion=True)
        time.sleep(1)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 05.1: Verify Page summary")
#         ia_runobj.create_table_data_set('table#ITableData0', 'C2203718_Ds02.xlsx')
        ia_runobj.verify_table_data_set('table#ITableData0', 'C2203718_Ds02.xlsx', 'Step 05.2: Verify data is displayed in the Live Preview pane')
        time.sleep(5)
        self.driver.switch_to_default_content()
        time.sleep(1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
         
         
        """
        Step 06: Right click on folder created in IA and select New >Text Editor
        Step 07: Add ahtml002.fex code in Text Editor and save as Ahtml002
        Step 08: Edit the AR-RP-001.fex via IA. Report will be opened under IA tool.
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7072', mrid='mrid', mrpass='mrpass')
        time.sleep(6)
        parent_css="#TableChart_1 [id^='ActivePreviewItem']"
        result_obj.wait_for_property(parent_css, 12)
        resultareaobj.verify_report_data_set('TableChart_1', 19, 6, 'C2203718_Ds01.xlsx','Step 08: Verify data is displayed in the Live Preview pane')
         
         
        """
        Step 09: Highlight Product column under report
                Verify that Field-Category menu is available in the menu bar Verify that Filter, Sort, Break, Style and Links sub-menu options are now visible.
        """
        resultareaobj.select_field_on_canvas('TableChart_1', 3)
         
         
        """ Step 10: Click Links > Hyperlink option
                    Verify that Drill Down pop up opens up
        """
        ribbonobj.select_ribbon_item('Field', 'drilldown')
        time.sleep(1)
        parent_css="[id^='QbDialog'] [class*='active'] [class*='caption']"
        result_obj.wait_for_property(parent_css, 1, string_value='DrillDown-Product', with_regular_exprestion=True)
        time.sleep(1)
        popup=driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] [class*='caption']").text.strip().replace('\n','')
        popup_title=re.sub(' ','',popup)
        status=False
        if popup_title == 'DrillDown-Product':
            status=True
        utillobj.asequal(status, True,'Step 10.1: Verify that Drill Down pop up opens up. ')
         
        ia_ribobj.create_drilldown_report('report', browse_file_name='ahtml_002', set_target='New Window', click_ok=True)
        time.sleep(9)
         
         
        """ Step 11: Verify show fex data containing 'SET HTMLENCODE ON'
        """
        ribbonobj.select_top_toolbar_item("toolbar_showfex")
        time.sleep(3)
        parent_css="[id^='BiDialog'] [class*='active'] [class*='caption']"
        result_obj.wait_for_property(parent_css, 1, string_value='CurrentFocexecContent', with_regular_exprestion=True)
        time.sleep(7)
        e = driver.find_element_by_xpath("//iframe[starts-with(@id,'BiRich')]")
        time.sleep(3)
        driver.switch_to.frame(e)
        fex_code = driver.find_element_by_css_selector("body>div").text
        expected_code = 'SET HTMLENCODE=ON'
        vp_text = "Step 11.1: Verify show fex data containing 'SET HTMLENCODE ON'"
        bol=expected_code in fex_code
        utillity.UtillityMethods.asequal(self,True, bol, vp_text)
        time.sleep(3)
        driver.switch_to_default_content()
        time.sleep(4)
        close_fexcode_btn=driver.find_element_by_css_selector("#showFexOKBtn img")
        utillobj.default_left_click(object_locator=close_fexcode_btn)
        time.sleep(4)
        driver.switch_to_default_content()
        time.sleep(2)
        resultareaobj.verify_report_data_set('TableChart_1', 19, 6, 'C2203718_Ds01.xlsx','Step 11.2: Verify data is displayed in the Live Preview pane')
         
        
         
         
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        frameobj=driver.find_element_by_css_selector('[id^=ReportIframe-]')
        x_fr=frameobj.location['x']
        y_fr=frameobj.location['y'] - 9
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it
            ((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(1)
        ia_runobj.verify_table_data_set('table#ITableData0', 'C2203718_Ds02.xlsx', 'Step 11.3: Verify data is displayed in the Live Preview pane')
        time.sleep(1)
        ia_runobj.select_and_verify_drilldown_report_field('table#ITableData0', 2, 3, browser_height=80, x_offset=x_fr, y_offset=y_fr)
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(9)
         
        """ Step 12: Verify that user will be redirected to inserted chart correctly.
        """
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(1)
        driver.maximize_window()
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '134of134records,Page1of3', 'Step 12.1: Verify the Report Heading')
#         ia_runobj.create_table_data_set('table#ITableData0', 'C2203718_Ds03.xlsx')
        ia_runobj.verify_table_data_set('table#ITableData0', 'C2203718_Ds03.xlsx', 'Step 12.2: Verify data set')
        time.sleep(5)
        driver.close()
        time.sleep(7)
        utillobj.switch_to_window(0)
        time.sleep(9)
        self.driver.switch_to_default_content()
        time.sleep(1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        


if __name__ == "__main__":
    unittest.main()