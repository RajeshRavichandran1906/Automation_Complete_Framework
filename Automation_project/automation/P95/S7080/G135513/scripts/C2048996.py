'''
Created on January 10, 2019

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2048996
TestCase Name = Document/Dashboard with Multiple Reports and Prompts
'''

"""Comments: Testcase may not exactly match the test rail in few steps because of the limitations in document window
"""

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.lib import utillity
from common.wftools import visualization
from common.wftools import report
from common.wftools import document
from common.wftools import active_report
from common.lib import core_utility
# from common.lib.global_variables import Global_variables

class C2048996_TestClass(BaseTestCase):

    def test_C2048996(self):
        """
        Test case Object's
        """
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        active_report_obj = active_report.Active_Report(self.driver)
        document_obj = document.Document(self.driver)
        report_obj = report.Report(self.driver)
        visual_obj = visualization.Visualization(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        """
        Test case variables
        """
        expected_radio_buttons = ['[All]', 'EMEA', 'North America', 'Oceania', 'South America']
        final_radio_list = ['[All]', '195', '458', '975', '1,059', '1,201', '1,937', '2,572', '5,403', '9,733', '17,049', '22,593', '25,042', '38,199', '41,924', 
                            '54,898', '57,666', '83,417', '106,141', '153,721', '180,032', '190,216', '214,078', '241,376', '271,346', '319,671', '412,127', '464,688', '592,174']
        
        """
        Test case css
        """
        report_css= '#TableChart_1'
        radio_css = '#Prompt_1'
        report_two_css = '#TableChart_2'
        drop_down_css = '#Prompt_2'
        document_title_css = "#iaCanvasCaptionLabel"
        
        """ 
        Step 1: Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=new_retail/wf_retail_lite&item=IBFS:/WFC/Repository/P95/S7080
        """
        report_obj.invoke_ia_tool_using_new_api_login(tool='document', master='new_retail/wf_retail_lite',mrid='mriddev',mrpass='mrpassdev', report_css="#canvasContainer", no_of_element=1)
        
        """
        Step 2 : On the Format tab, in the Output Types group, click Active report.
        Expect to see the initial Dashboard, in Document view.
        """
        chart_obj.change_output_format_type('active_report')
        chart_obj.wait_for_number_of_element("#canvasContainer", 1, chart_obj.chart_short_timesleep)
        document_title = util_obj.validate_and_get_webdriver_object(document_title_css, 'document_title').text.strip()
        util_obj.asequal('Document', document_title, "Step 02.01: Verify Document is open")
        
        """
        Step 3: Select Quantity,Sold from the Sales group as the Measure.
        Select Customer,Business,Region from the Customer group and Product_Category from the Product group for the Dimensions.
        Expect to see the following Dashboard canvas with the Report.
        """
        report_obj.double_click_on_datetree_item('Quantity,Sold', 1)
        chart_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(3) td", 'Quantity,Sold', chart_obj.report_medium_timesleep)
        report_obj.double_click_on_datetree_item('Customer->Customer,Business,Region', 1)
        chart_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(5) td", 'Customer,Business,Region', chart_obj.report_medium_timesleep)
        report_obj.double_click_on_datetree_item('Product->Product,Category', 1)
        chart_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(6) td", 'Product,Category', chart_obj.report_medium_timesleep)
        report_obj.verify_report_data_set_in_preview('TableChart_1', 30, 3, 'C2048996_step3.xlsx', 'Step 03.01: Verify the table dataset')
        
        """
        Step 4: From the Insert button, click the Radio Button Dashboard prompt.
        Click inside the Report and drag it to the right of the Radio Button.
        Expect to see the following Dashboard canvas, with the Radio Button to the left of the Report.
        """
        visual_obj.select_ribbon_item('Insert', 'radio_button')
        document_obj.drag_drop_document_component( '#TableChart_1','#Prompt_1', 200, 0)
        radio_element = util_obj.validate_and_get_webdriver_object(radio_css,'radio-element')
        radio_coordinates = util_obj.get_object_screen_coordinate(radio_element, coordinate_type='right')
        report_element = util_obj.validate_and_get_webdriver_object(report_css,'report-element')
        report_coordinates = util_obj.get_object_screen_coordinate(report_element, coordinate_type='left')
        util_obj.as_LE(radio_coordinates['x'], report_coordinates['x'], "Step 04.01: Verify radio on the left")
        
        """
        Step 5: From the Insert button, click Report.
        Drag the new report below the initial report.
        Expect to see the following canvas with the second empty report beneath the first report.
        """
        visual_obj.select_ribbon_item('Insert', 'report')
        document_obj.drag_drop_document_component( report_two_css, report_css, 200, 0)
        
        """
        Step 6: Select Product,Category for the Dimension.
        Select Store,Business Region & Store,Business,Sub Region.
        Expect to see the second report with the three selected fields.
        """
        report_obj.double_click_on_datetree_item('Product->Product,Category', 1)
        chart_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(5) td", 'Product,Category', chart_obj.report_medium_timesleep)
        report_obj.double_click_on_datetree_item('Store->Store,Business,Region', 1)
        chart_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(6) td", 'Store,Business,Region', chart_obj.report_medium_timesleep)
        report_obj.double_click_on_datetree_item('Store->Store,Business,Sub Region', 1)
        chart_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(7) td", 'Store,Business,Sub Region', chart_obj.report_medium_timesleep)
        report_obj.verify_report_data_set_in_preview('TableChart_2', 30, 3, 'C2048996_step6.xlsx', 'Step 06.01: Verify the table dataset')
        
        """
        Step 7: From the Insert button, click the Drop Down List Dashboard prompt.
        Expect to see the Drop Down Box on the left of the second report.
        """
        visual_obj.select_ribbon_item('Insert', 'drop_down')
        chart_obj.wait_for_number_of_element(drop_down_css, 1, chart_obj.chart_short_timesleep)
        document_obj.drag_drop_document_component(drop_down_css, radio_css, 0, 200, target_drop_point='bottom_left')
        document_obj.resizing_document_component(1, 1)
#         if Global_variables.browser_name == 'firefox':
#             resize_dropdown_css = "#Prompt_2 div[id*='BiResizeHandle']"
#             dropdown_ele = util_obj.validate_and_get_webdriver_objects(resize_dropdown_css, 'drop down resize')[5]    
#             dropdown_coordinate = core_util_obj.get_web_element_coordinate(dropdown_ele, element_location= 'top_left')
#             util_obj.drag_drop_on_screen(sx_offset = dropdown_coordinate['x'],sy_offset = dropdown_coordinate['y'], tx_offset= dropdown_coordinate['x']+50, ty_offset = dropdown_coordinate['y']+40)
#         else:
#             pass
        
        """
        Step 8: Scroll the canvas so that the first report is visible again.
        Right click inside the Radio Button Dashboard prompt box. 
        Expect to see the following menu of options for the Radio Button.
        Step 9: Click the Properties entry.
        Expect to see the following screen of properties.
        Expect to see the radiobutton_1 highlighted.    
        """
        document_obj.choose_right_click_menu_item_for_prompt(radio_css, 'Properties')
        chart_obj.wait_for_number_of_element("#adpPropertiesDlg", 1, chart_obj.report_medium_timesleep)
        util_obj.verify_object_visible("#adpPropertiesDlg", True, "Step 08.01: Verify the properties box is visible")
#         util_obj.verify_element_color_using_css_property("#gridADPrompts tr:first-child td", 'Pale_Cornflower_Blue', 'Step 08.02: Verify radio button is highligthened', attribute='background-color')
        background_css = self.driver.find_element_by_css_selector('#gridADPrompts tr:first-child td')
        background_color = background_css.value_of_css_property('background-color')
        util_obj.asequal(background_color, 'rgba(224, 224, 224, 1)', 'Step 08.02: Verify radio button is highligthened')
        
        """
        Step 10: For the Report drop down, click Report1.
        For the Field, click Customer,Business,Region.
        For the Condition, accept the default of Equal to.
        For the Sort , accept the default of Ascending.
        Accept the Include All checked box.
        Expect to see the following Radio Button options for Report1.
        Step 11: Click OK to the Prompt Sources & Targets options.
        Expect to see the Radio Button now showing Preview values.
        """
        document_obj.customize_active_dashboard_properties(source={'select_report':'Report1','select_field':'Customer,Business,Region', 'select_condition':'Equal to', 'select_sort':'Ascending'})
        radio_button_elements = util_obj.validate_and_get_webdriver_objects("#Prompt_1 div[id^='BiLabel'] .bi-label", 'radio_buttons')
        radio_buttons = [element.text for element in radio_button_elements]
        util_obj.asequal(expected_radio_buttons, radio_buttons, "Step 11.01: Verify Radio buttons")
        
        """
        Step 12: Scroll to the second report, right click in the Drop Down Box.
        Click Properties.
        Expect to see the Prompt Source & Targets screen, this time with combobox_2 highlighted.
        """
        document_obj.choose_right_click_menu_item_for_prompt(drop_down_css, 'Properties')
        chart_obj.wait_for_number_of_element("#adpPropertiesDlg", 1, chart_obj.report_medium_timesleep)
        util_obj.verify_object_visible("#adpPropertiesDlg", True, "Step 12.01: Verify the properties box is visible")
#         util_obj.verify_element_color_using_css_property("#gridADPrompts tr:nth-child(2) td:last-child", 'Pale_Cornflower_Blue', 'Step 12.02: Verify combo box is highligthened', attribute='background-color')
        background_css = self.driver.find_element_by_css_selector('#gridADPrompts tr:nth-child(2) td:last-child')
        background_color = background_css.value_of_css_property('background-color')
        util_obj.asequal(background_color, 'rgba(224, 224, 224, 1)', 'Step 12.02: Verify combo box is highligthened')
        
        """
        Step 13: For the Report drop down, click Report2.
        For the Field, click Product,Category.
        For the Condition, accept the default of Equal to.
        For the Sort , accept the default of Ascending.
        Accept the Include All checked box.
        Step 14: Click OK.
        Expect to see the Drop Down box with only the [All] value showing.
        """
        document_obj.customize_active_dashboard_properties(source={'select_report':'Report2','select_field':'Product,Category', 'select_condition':'Equal to', 'select_sort':'Ascending'})
        drop_down_element = util_obj.validate_and_get_webdriver_object("#Prompt_2 div[id^='BiLabel'] .bi-label", 'drop_down_buttons').text
        util_obj.asequal('[All]', drop_down_element, "Step 13.01: Verify drop down value")
        
        """
        Step 15: Scroll back to the first report.
        Click the Run button.
        Expect to see the following Active Dashboard.
        """
        chart_obj.run_chart_from_toptoolbar()
        util_obj.wait_for_page_loads(15)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element('#radiobuttonPROMPT_1', 1, chart_obj.chart_medium_timesleep)
        active_report_obj.verify_active_report_dataset('C2048996_step15.xlsx', 'Step 15.01: Verify the active report 1', table_css='#ITableData0')
        active_report_obj.verify_active_report_dataset('C2048996_step15_report2.xlsx', 'Step 15.02: Verify the active report 2', table_css='#ITableData1')
        document_obj.verify_prompts('radio', '#radiobuttonPROMPT_1', expected_radio_buttons, 'Step 15.03: Verify the radio buttons')
        
        """
        Step 16: From the Radio Button list, click 'Oceania'.
        Expect to see 7 rows, all with the filtered value of Oceania for the Customer Business Region.
        """
        document_obj.select_prompt('radio', '#radiobuttonPROMPT_1', select_list=['Oceania'])
        active_report_obj.verify_active_report_dataset('C2048996_step16_report1.xlsx', 'Step 16.01: Verify the active report 1', table_css='#ITableData0')
        
        """
        Step 17: Click the [All] button .
        Scroll downward, so that the second report and the Drop Down Box are visible.
        """
        document_obj.select_prompt('radio', '#radiobuttonPROMPT_1', select_list=["[All]"])
        active_report_obj.verify_active_report_dataset('C2048996_step15.xlsx', 'Step 17.01: Verify the active report 1', table_css='#ITableData0')
        active_report_obj.verify_active_report_dataset('C2048996_step15_report2.xlsx', 'Step 17.02: Verify the active report 2', table_css='#ITableData1')
        document_obj.verify_prompts('radio', '#radiobuttonPROMPT_1', expected_radio_buttons, 'Step 17.03: Verify the radio buttons')
        
        """
        Step 18: From the Drop Down list, select Media Players
        Expect to see a 14 row report, all for Product Category of Media Players.
        """
    
        util_obj.select_dropdown('#combobox_dsPROMPT_2', 'value', 'Media Player')
        active_report_obj.verify_active_report_dataset('C2048996_step18_report2.xlsx', 'Step 18.01: Verify the active report 2', table_css='#ITableData1')
        
        """
        Step 19: From the Drop Down list, click the [All] entry.
        Scroll down to the bottom of the second report.
        """
        util_obj.select_dropdown('#combobox_dsPROMPT_2', 'value', "[All]")
        active_report_obj.verify_active_report_dataset('C2048996_step15_report2.xlsx', 'Step 19.01: Verify the active report 2', table_css='#ITableData1')
        
        """
        Step 20: Scroll back to the top and right click in the Radio Button.
        Click the Properties button.
        Change the field that controls the first report to Quantity Sold. 
        Click the OK button to accept the new field.
        Change the Condition to Greater than or equal to.
        """
        chart_obj.switch_to_default_content()
        document_obj.select_result_area_panel_caption_button('close')
        document_obj.choose_right_click_menu_item_for_prompt(radio_css, 'Properties')
        chart_obj.wait_for_number_of_element("#adpPropertiesDlg", 1, chart_obj.report_medium_timesleep)
        util_obj.select_combobox_item('comboSourceFields', 'Quantity,Sold')
        chart_obj.wait_for_number_of_element("#promptDlg", 1, chart_obj.report_medium_timesleep)
        util_obj.verify_object_visible("#promptDlg", True, "Step 20.01: Verify the prompt box is visible")
        ok_button = util_obj.validate_and_get_webdriver_object("#promptDlg div[id='btnOK'] img", 'ok-button')
        core_util_obj.left_click(ok_button)
        document_obj.customize_active_dashboard_properties(source={'select_condition':'Greater than or equal to'})
        
        """
        Step 21: Click OK to exit the Prompt Sources & Targets options screen.
        Click the Run button to verify the new field used in the Radiobutton.
        """
        chart_obj.run_chart_from_toptoolbar()
        util_obj.wait_for_page_loads(20)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element('#PROMPT_1_cs', 1, chart_obj.chart_medium_timesleep)
        document_obj.verify_prompts('radio', '#radiobuttonPROMPT_1', final_radio_list, 'Step 21.01: Verify the radio buttons')
        
        """
        Step 22: Scroll down the Radio Button list and check the value for 106,141.
        Expect to see the report with values greater than or equal to 106,141 and containing 11 rows.
        """
        document_obj.select_prompt('radio', '#radiobuttonPROMPT_1', select_list=['106,141'])
        active_report_obj.verify_active_report_dataset('C2048996_step22_report1.xlsx', 'Step 22.01: Verify the active report 1', table_css='#ITableData0')
        
        """
        Step 21: Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        time.sleep(3)
                
if __name__ == '__main__':
    unittest.main()