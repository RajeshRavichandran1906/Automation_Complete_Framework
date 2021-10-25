'''
Created on January 9, 2019

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2048637
TestCase Name = Active Technologies Dashboard Prompt option - Radio button.
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.lib import base
from common.lib import utillity
from common.wftools import visualization
from common.wftools import report
from common.wftools import document
from common.wftools import active_report

class C2048637_TestClass(BaseTestCase):

    def test_C2048637(self):
        
        """
        Test case Object's
        """
        active_report_obj = active_report.Active_Report(self.driver)
        document_obj = document.Document(self.driver)
        report_obj = report.Report(self.driver)
        visual_obj = visualization.Visualization(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        base_obj = base.BasePage(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        """
        Test case variables
        """
        expected_radio_buttons = ['[All]', 'Coffee', 'Food', 'Gifts']
        
        """ 
        Step 1: Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=ibisamp/ggsales&item=IBFS:/WFC/Repository/P95/S7080
        """
        report_obj.invoke_ia_tool_using_new_api_login(tool='document', master='ibisamp/ggsales',mrid='mriddev',mrpass='mrpassdev')
        chart_obj.wait_for_number_of_element("#canvasContainer", 1, base_obj.report_long_timesleep)
        
        """
        Step 2 : On the Format tab, in the Output Types group, click Active report.
        Click the Insert tab at the top.
        Expect to see the following Dashboard canvas with the following available Dashboard Prompts.
        Step 3: Begin the Document composition by clicking on Report option of the Insert tab.
        Expect to see a Report pane created on the Dashboard.
        """
        chart_obj.change_output_format_type('active_report')
        visual_obj.select_ribbon_item('Insert', 'report')
        chart_obj.wait_for_number_of_element("#TableChart_1", 1, base_obj.report_medium_timesleep)
        
        """
        Step 4 : Double click or drag Category and Product from the Dimensions area to the canvas.
        Double click or drag Unit Sales and Dollar Sales to the canves.
        Expect to see the Report pane with the following fields.
        """
        source_element = util_obj.validate_and_get_webdriver_object("[id^='QbMetaDataTree'] tr:nth-child(2) img", 'category')
        source_coordinates = util_obj.get_object_screen_coordinate(source_element, coordinate_type='middle')
        target_element = util_obj.validate_and_get_webdriver_object("#TableChart_1", 'canvas')
        target_coordinates = util_obj.get_object_screen_coordinate(target_element, coordinate_type='middle')
        util_obj.drag_drop_on_screen(sx_offset=source_coordinates['x'],sy_offset=source_coordinates['y'],tx_offset=target_coordinates['x'],ty_offset=target_coordinates['y'])
        source_element = util_obj.validate_and_get_webdriver_object("[id^='QbMetaDataTree'] tr:nth-child(4) img", 'product')
        source_coordinates = util_obj.get_object_screen_coordinate(source_element, coordinate_type='middle')
        target_element = util_obj.validate_and_get_webdriver_object("#TableChart_1", 'canvas')
        target_coordinates = util_obj.get_object_screen_coordinate(target_element, coordinate_type='middle')
        util_obj.drag_drop_on_screen(sx_offset=source_coordinates['x'],sy_offset=source_coordinates['y'],tx_offset=target_coordinates['x'],ty_offset=target_coordinates['y'])
        chart_obj.double_click_on_datetree_item('Unit Sales', 1)
        chart_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(3) td", 'Unit Sales', base_obj.report_medium_timesleep)
        chart_obj.double_click_on_datetree_item('Dollar Sales', 1)
        chart_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(4) td", 'Dollar Sales', base_obj.report_medium_timesleep)
        
        """
        Step 5: From the Insert button, click on the Radio Button Document Prompt.
        Drag the Radio Button Prompt to the right of the Report by dragging it in the margin.
        """
        visual_obj.select_ribbon_item('Insert', 'radio_button')
        document_obj.drag_drop_document_component('#Prompt_1', '#TableChart_1', 60, 0, target_drop_point='right')
        
        """
        Step 6: Bind the Radio button Prompt to the Report by right clicking the Radio button box.
        Step 7: Click the Properties option.
        Expect to see the following menu for Prompt Source & Targets appear.
        """
        document_obj.choose_right_click_menu_item_for_prompt("#Prompt_1", 'Properties')
        chart_obj.wait_for_number_of_element("#adpPropertiesDlg", 1, base_obj.report_medium_timesleep)
        util_obj.verify_object_visible("#adpPropertiesDlg", True, "Step 6.1: Verify the properties box is visible")
        
        """
        Step 8: The default Report is Report 1.
        From the field dropdown, select the Category value.
        For the Condition, select Equal To.
        For the Sort, select Ascending.
        Check the Include All box if not already checked.
        Expect to see the following options for the Prompt Source & Targets menu.
        Step 9: Click OK.
        Expect to see the following Dashboard canvas the Report and Radio Button components.
        """
        document_obj.customize_active_dashboard_properties(source={'select_field':'Category', 'select_condition':'Equal to', 'select_sort':'Ascending'})
        report_obj.create_report_data_set_in_preview('TableChart_1', 2, 4, 'C2048637_step8.xlsx')
        report_obj.verify_report_data_set_in_preview('TableChart_1', 2, 4, 'C2048637_step8.xlsx', "Step 8.1: Verify the report data set")
        radio_button_elements = util_obj.validate_and_get_webdriver_objects("#Prompt_1 div[id^='BiLabel'] .bi-label", 'radio_buttons')
        radio_buttons = [element.text for element in radio_button_elements]
        util_obj.asequal(expected_radio_buttons, radio_buttons, "Step 8.2: Verify Radio buttons")
        
        """
        Step 10: Click the Run button to generate he Document.
        Expect to see the following Active Dashboard.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        active_report_obj.verify_active_report_dataset('C2048637_step10.xlsx', 'Step 10.1: Verify the active report', table_css='#ITableData0')
        document_obj.verify_prompts('radio', '#radiobuttonPROMPT_1', expected_radio_buttons, 'Step 10.2: Verify the radio buttons')
        
        """
        Step 11: Test the Radio Button Prompt by selecting the Food Category.
        Expect to see the filtered report display only Food rows.
        """
        document_obj.select_prompt('radio', '#radiobuttonPROMPT_1', select_list=['Food'])
        active_report_obj.verify_active_report_dataset('C2048637_step11.xlsx', 'Step 11.1: Verify the active report with food alone', table_css='#ITableData0')
        
        """
        Step 12: Click the All button to return all Categories to the Report
        Expect to see the original full 10 row report with all Categories.
        """
        document_obj.select_prompt('radio', '#radiobuttonPROMPT_1', select_list=["[All]"])
        active_report_obj.verify_active_report_dataset('C2048637_step10.xlsx', 'Step 12.1: Verify the active report after clicking all', table_css='#ITableData0')
        
if __name__ == '__main__':
    unittest.main()