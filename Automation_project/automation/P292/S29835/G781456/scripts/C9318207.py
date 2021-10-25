"""----------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 26-August-2019
----------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.pages.ia_ribbon import IA_Ribbon
from common.wftools.report import Report
from common.wftools.chart import Chart
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
import time
from common.lib.global_variables import Global_variables

class C9318207_TestClass(BaseTestCase):
    
    def test_C9318207(self):
        
        """CLASS OBJECTS"""
        report = Report(self.driver)
        chart = Chart(self.driver)
        ia_ribbon = IA_Ribbon(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
        
        """COMMON VARIABLES"""
        case_id = "C9318207"
        chart_fex_name = case_id + "_Chart"
        preview_table_id = "TableChart_1"
        preview_table_css = "#" + preview_table_id
        preview_chart_css = "#pfjTableChart_1"
        run_table_css = "table[summary]"
        data_set01 = case_id + "_DataSet01.xlsx"
        data_set02 = case_id + "_DataSet02.xlsx"
        data_set03 = case_id + "_DataSet03.xlsx"
        
        """
            STEP 01 : Launch the API to create new Report with WF_RETAIL_LITE.
            http://machine:port/{alias}/ia?is508=false&tool=report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/P292_S29835/G781455
            Check the Live preview
        """
        report.invoke_ia_tool_using_new_api_login(master='baseapp/wf_retail_lite')
        report.wait_for_visible_text(preview_table_css, "Drag", report.report_long_timesleep)
        
        """
            STEP 02 : Double click "Product,Category","Product,Subcategory" and "Cost of Goods" in Data pane.
        """
        report.double_click_on_datetree_item('Product,Category', 1)
        report.wait_for_visible_text(preview_table_css, "Product", report.report_short_timesleep)
        
        report.double_click_on_datetree_item('Product,Subcategory', 1)
        report.wait_for_visible_text(preview_table_css, "Subcategory", report.report_short_timesleep)
        
        report.double_click_on_datetree_item('Cost of Goods', 1)
        report.wait_for_visible_text(preview_table_css, "Cost of Goods", report.report_short_timesleep)
        
        #report.create_acrossreport_data_set_in_preview(preview_table_id, 2, 3, 1, 3, data_set01)
        report.verify_across_report_data_set_in_preview(preview_table_id, 2, 3, 1, 3, data_set01, "Step 02.01 : Verify live preview data")
        
        """
            STEP 03 : Click "Procedure Settings" in the toolbar.
            Check the default settings.
        """
        report.select_ia_toolbar_item("toolbar_showfex_setting")
        report.wait_for_visible_text("#qbEnvSetParametersDlgOkBtn", "OK", report.report_short_timesleep)
        
        button_obj = utils.validate_and_get_webdriver_object("#ARVERSION div[id^='BiButton']", "button obj")
        core_utils.python_left_click(button_obj)
        time.sleep(5)
        designer_obj = self.driver.find_element_by_xpath("//*[contains(text(), 'Designer Style')]")
        core_utils.python_left_click(designer_obj)
        time.sleep(5)
        
        unchecked_row=['Collation Sequence','Summary Lines','Missing Value','Decimal Notation']
        for row in unchecked_row :
            ia_ribbon.procedure_setting_dialogverify(row,'checkbox','unchecked','Step 03.01 : Verify '+row+' is not selected as default')
        
        checked_row=['In-Document Analytics', 'HTML Encode','Empty Report']
        for row in checked_row :
            ia_ribbon.procedure_setting_dialogverify(row,'checkbox','checked','Step 03.01 : Verify '+row+' is selected as default')
        
        combobox_row=['Collation Sequence','Summary Lines', 'In-Document Analytics']
        expected_chombobox_values=['Code Page','New', 'Designer Style']
        for i in range(len(combobox_row)) :
            ia_ribbon.procedure_setting_dialogverify(combobox_row[i],'combobox',expected_chombobox_values[i],'Step 03.01 : Verify '+combobox_row[i]+' default value is '+expected_chombobox_values[i])
        
        for row in ['HTML Encode', 'Empty Report'] :
            ia_ribbon.procedure_setting_dialogverify(row,'radiobutton','checked','Step 03.01 : Verify '+row+' ON is selected',1)
            ia_ribbon.procedure_setting_dialogverify(row,'radiobutton','unchecked','Step 03.01 : Verify '+row+' OFF is not selected',2)
            
        ia_ribbon.procedure_setting_dialogverify('Missing Value','textbox','.','Step 03.01 : Verify Missing Value value')
        ia_ribbon.procedure_setting_dialogverify('Decimal Notation','radiobutton','unchecked','Step 03.01 : Verify Decimal Notation ON is not selected',1)
        ia_ribbon.procedure_setting_dialogverify('Decimal Notation','radiobutton','checked','Step 03.01 : Verify Decimal Notation OFF is selected',2)
        
        """
            STEP 04 : Click "Decimal Notation" checkbox and Click "On" radio button.
            Check the following settings
        """
        ia_ribbon.procedure_setting_dialog_input('Decimal Notation','checkbox','unchecked')
        ia_ribbon.procedure_setting_dialog_input('Decimal Notation','radiobutton','unchecked')
        
        """
            STEP 05 : Click "OK" button.
            Check placement of the period and comma for the 'Cost of Goods' column in Preview.
        """
        ia_ribbon.procedure_setting_dialog_dismiss('OK')
        report.wait_for_visible_text(preview_table_css, "$2.052.711,00", report.report_short_timesleep)
        #report.create_acrossreport_data_set_in_preview(preview_table_id, 2, 3, 1, 3, data_set02)
        report.verify_across_report_data_set_in_preview(preview_table_id, 2, 3, 1, 3, data_set02, "Step 05.01 : Verify live preview data")
        
        """
            STEP 06 : Click "Run" from toolbar.
            Check the following Output.
        """
        report.run_report_from_toptoolbar()
        report.switch_to_frame()
        report.wait_for_visible_text(run_table_css, "$2.052.711,00", report.report_medium_timesleep)
        #report.create_html_report_dataset(data_set03)
        report.verify_html_report_dataset(data_set03, "Step 06.01 : Verify run output")
        report.switch_to_default_content()
        
        """
            STEP 07 : Click "Save" in toolbar Enter "C9318207" and Click "Save" button.
        """
        report.save_report_from_toptoolbar()
        report.save_file_in_save_dialog(case_id)
        
        """
            STEP 08 : Logout. http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report.api_logout()
        
        """
            STEP 09 : Reopen the saved fex using API link
            http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S29835/G781455/C9318207.fex&tool=Report
            Check the Live preview.
        """
        report.edit_fex_using_api_url(case_id)
        report.wait_for_visible_text(preview_table_css, "Subcategory", report.report_long_timesleep)
        report.verify_across_report_data_set_in_preview(preview_table_id, 2, 3, 1, 3, data_set02, "Step 09.01 : Verify live preview data")
        
        """
            STEP 10 : Click "Chart" in Home tab.
        """
        report.select_ia_ribbon_item('Home', 'chart')
        report.wait_for_visible_text(preview_chart_css, "Cost of Goods", report.report_long_timesleep)
        
        """
            STEP 11 : Click "Procedure Settings" in the toolbar.
            Check the default settings.
        """
        report.select_ia_toolbar_item("toolbar_showfex_setting")
        report.wait_for_visible_text("#qbEnvSetParametersDlgOkBtn", "OK", report.report_short_timesleep)
        button_obj = utils.validate_and_get_webdriver_object("#ARVERSION div[id^='BiButton']", "button obj")
        core_utils.python_left_click(button_obj)
        time.sleep(5)
        designer_obj = self.driver.find_element_by_xpath("//*[contains(text(), 'Designer Style')]")
        core_utils.python_left_click(designer_obj)
        time.sleep(5)
        unchecked_row=['Collation Sequence','Summary Lines','Missing Value','Decimal Notation']
        for row in unchecked_row :
            ia_ribbon.procedure_setting_dialogverify(row,'checkbox','unchecked','Step 11.01 : Verify '+row+' is not selected as default')
        
        checked_row=['In-Document Analytics', 'HTML Encode','Empty Report']
        for row in checked_row :
            ia_ribbon.procedure_setting_dialogverify(row,'checkbox','checked','Step 11.01 : Verify '+row+' is selected as default')
        
        combobox_row=['Collation Sequence','Summary Lines', 'In-Document Analytics']
        expected_chombobox_values=['Code Page','New', 'Designer Style']
        for i in range(len(combobox_row)) :
            ia_ribbon.procedure_setting_dialogverify(combobox_row[i],'combobox',expected_chombobox_values[i],'Step 11.01 : Verify '+combobox_row[i]+' default value is '+expected_chombobox_values[i])
        
        for row in ['HTML Encode', 'Decimal Notation'] :
            ia_ribbon.procedure_setting_dialogverify(row,'radiobutton','unchecked','Step 11.01 : Verify '+row+' ON is selected',1)
            ia_ribbon.procedure_setting_dialogverify(row,'radiobutton','checked','Step 11.01 : Verify '+row+' OFF is not selected',2)
            
        ia_ribbon.procedure_setting_dialogverify('Missing Value','textbox','.','Step 11.01 : Verify Missing Value value')
        ia_ribbon.procedure_setting_dialogverify('Empty Report','radiobutton','checked','Step 11.01 : Verify Decimal Notation ON is not selected',1)
        ia_ribbon.procedure_setting_dialogverify('Empty Report','radiobutton','unchecked','Step 11.01 : Verify Decimal Notation OFF is selected',2)
        
        """
            STEP 12 : Click "Cancel" button.
        """
        ia_ribbon.procedure_setting_dialog_dismiss('Cancel')
        
        """
            STEP 13 : Click "Save" in toolbar Enter "C9318207_Chart" and Click "Save" button.
        """
        report.save_report_from_toptoolbar()
        report.save_file_in_save_dialog(chart_fex_name)
        
        """
            STEP 14 : Logout http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report.api_logout()
        
        """
            STEp 15 : Reopen the saved fex using API link
            http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S29835/G781455/C9318207_Chart.fex&tool=Chart
            Check the Live preview
        """
        chart.edit_fex_using_api_url(folder_name='P292_S29835/G781455', fex_name=chart_fex_name)
        report.wait_for_visible_text(preview_chart_css, "Cost of Goods", report.report_long_timesleep)
        if Global_variables.browser_name == 'chrome':
            expected_x_axis = ['Accessories : Charger', 'Accessories : Headphones', 'Accessories : Universal Remote...', 'Camcorder : Handheld', 'Camcorder : Professional', 'Camcorder : Standard', 'Computers : Smartphone', 'Computers : Tablet', 'Media Player : Blu Ray', 'Media Player : DVD Players', 'Media Player : DVD Players - Por...', 'Media Player : Streaming', 'Stereo Systems : Boom Box', 'Stereo Systems : Home Theater...', 'Stereo Systems : Receivers', 'Stereo Systems : Speaker Kits', 'Stereo Systems : iPod Docking S...', 'Televisions : CRT TV', 'Televisions : Flat Panel TV', 'Televisions : Portable TV', 'Video Production : Video Editing']
        else:
            expected_x_axis = ['Accessories : Charger', 'Accessories : Headphones', 'Accessories : Universal Remote C...', 'Camcorder : Handheld', 'Camcorder : Professional', 'Camcorder : Standard', 'Computers : Smartphone', 'Computers : Tablet', 'Media Player : Blu Ray', 'Media Player : DVD Players', 'Media Player : DVD Players - Portable', 'Media Player : Streaming', 'Stereo Systems : Boom Box', 'Stereo Systems : Home Theater S...', 'Stereo Systems : Receivers', 'Stereo Systems : Speaker Kits', 'Stereo Systems : iPod Docking Stat...', 'Televisions : CRT TV', 'Televisions : Flat Panel TV', 'Televisions : Portable TV', 'Video Production : Video Editing']
#             expected_x_axis = ['Accessories : Charger', 'Accessories : Headphones', 'Accessories : Universal Re...', 'Camcorder : Handheld', 'Camcorder : Professional', 'Camcorder : Standard', 'Computers : Smartphone', 'Computers : Tablet', 'Media Player : Blu Ray', 'Media Player : DVD Players', 'Media Player : DVD Players...', 'Media Player : Streaming', 'Stereo Systems : Boom Box', 'Stereo Systems : Home Th...', 'Stereo Systems : Receivers', 'Stereo Systems : Speaker K...', 'Stereo Systems : iPod Dock...', 'Televisions : CRT TV', 'Televisions : Flat Panel TV', 'Televisions : Portable TV', 'Video Production : Video Ed...']
        expected_y_axis = ['0', '40M', '80M', '120M', '160M', '200M']
        chart.verify_x_axis_label_in_preview(expected_x_axis, msg="Step 15.01")
        chart.verify_y_axis_label_in_preview(expected_y_axis, msg="Step 15.02")
        chart.verify_x_axis_title_in_preview(['Product Category : Product Subcategory'], msg="15.03")
        chart.verify_y_axis_title_in_preview(['Cost of Goods'], msg="15.04")
        chart.verify_number_of_risers("#pfjTableChart_1 rect", 1, 21, msg="15.05")
        chart.verify_chart_color('pfjTableChart_1', 'riser!s0!g8!mbar!', 'bar_blue', 'Step 15.06 : Verify riser color')
        
        """
            STEP 16 : Logout - http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """