'''
Created on January 16, 2019

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2231422
TestCase Name = Click cancel in ADP prop dialog clears document source (147897)
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.lib import utillity
from common.wftools import visualization
from common.wftools import report
from common.wftools import document
from common.lib import core_utility

class C2231422_TestClass(BaseTestCase):

    def test_C2231422(self):
        """
        Test case Object's
        """
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        document_obj = document.Document(self.driver)
        report_obj = report.Report(self.driver)
        visual_obj = visualization.Visualization(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        """
        Test case variables
        """
        expected_list_elements = ['[All]', 'ACCOUNTING', 'ADMIN SERVICES', 'CONSULTING', 'CUSTOMER SUPPORT', 'MARKETING', 'PERSONNEL', 'PROGRAMMING & DVLPMT', 'SALES']
        
        """ 
        Step 1: Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=ibisamp/empdata&item=IBFS:/WFC/Repository/P95/S10142
        """
        report_obj.invoke_ia_tool_using_new_api_login(tool='document', master='ibisamp/empdata',mrid='mriddev',mrpass='mrpassdev', report_css="#canvasContainer", no_of_element=1)
        
        """
        Step 2 : Now open the report again in IA (Edit), and right click on dropdown, and select properties. 
        """
        chart_obj.change_output_format_type('active_report')
        
        """
        Step 3: Double click fields DIV, DEPT and SALARY
        """
        chart_obj.double_click_on_datetree_item('DIV', 1)
        chart_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(4) td", 'DIV', chart_obj.report_medium_timesleep)
        chart_obj.double_click_on_datetree_item('DEPT', 1)
        chart_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(5) td", 'DEPT', chart_obj.report_medium_timesleep)
        chart_obj.double_click_on_datetree_item('SALARY', 1)
        chart_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(3) td", 'SALARY', chart_obj.report_medium_timesleep)
        report_obj.verify_report_data_set_in_preview('TableChart_1', 22, 3, 'C2231422_step3.xlsx', 'Step 3.1: Verify the table dataset')
        
        """
        Step 4: Go to "Insert" tab
        Step 5: Insert "Drop Down", "List", and "Radio Button" prompts
        Step 6: Reposition each prompt component
        """
        visual_obj.select_ribbon_item('Insert', 'drop_down')
        chart_obj.wait_for_number_of_element("#Prompt_1", 1, chart_obj.report_medium_timesleep)
        document_obj.drag_drop_document_component( '#Prompt_1', '#TableChart_1', 200, -10)
        visual_obj.select_ribbon_item('Insert', 'list')
        chart_obj.wait_for_number_of_element("#Prompt_2", 1, chart_obj.report_medium_timesleep)
        document_obj.drag_drop_document_component( '#Prompt_2', '#TableChart_1', 150, 40)
        visual_obj.select_ribbon_item('Insert', 'radio_button')
        chart_obj.wait_for_number_of_element("#Prompt_3", 1, chart_obj.report_medium_timesleep)
        document_obj.drag_drop_document_component( '#Prompt_3', '#TableChart_1', 300, 40)
        
        """
        Step 7: Right click the Drop Down prompt component > "Properties"
        """
        document_obj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        chart_obj.wait_for_number_of_element("#adpPropertiesDlg", 1, chart_obj.report_medium_timesleep)
        
        """
        Step 8: Click "Field" dropdown > "DIV"
        Step 9: Click OK
        """
        document_obj.customize_active_dashboard_properties(source={'select_field':'DIV'})
        
        """
        Step 10: Right click the List prompt component > "Properties"
        """
        document_obj.choose_right_click_menu_item_for_prompt('#Prompt_2', 'Properties')
        chart_obj.wait_for_number_of_element("#adpPropertiesDlg", 1, chart_obj.report_medium_timesleep)
        
        """
        Step 11: Click "Field" dropdown > "DEPT"
        Step 12: Click OK
        """
        document_obj.customize_active_dashboard_properties(source={'select_field':'DEPT'})
        report_obj.verify_report_data_set_in_preview('TableChart_1', 22, 3, 'C2231422_step12.xlsx', 'Step 12.1: Verify the table dataset')
        combo_box = util_obj.validate_and_get_webdriver_object("#Prompt_1 .combo-box-label", "combo-box").text.strip()
        util_obj.asequal(expected_list_elements[0], combo_box, "Step 12.2: Verify the combo box")
        list_box = util_obj.validate_and_get_webdriver_objects("#Prompt_2 div[id^='BiListItem']", 'list-values')
        list_box_elements = [element.text for element in list_box]
        util_obj.asequal(expected_list_elements ,list_box_elements, "Step 12.3: Verify the list elements")
        
        """
        Step 13: Right click the List prompt component > "Properties"
        """
        document_obj.choose_right_click_menu_item_for_prompt('#Prompt_2', 'Properties')
        chart_obj.wait_for_number_of_element("#adpPropertiesDlg", 1, chart_obj.report_medium_timesleep)
        
        """
        Step 14: Click "Field" dropdown > "DIV"
        Step 15: Click ok on Alert window and click Cancel on Active dashboard properties
        """
        util_obj.select_combobox_item('comboSourceFields', 'DIV')
        chart_obj.wait_for_number_of_element("#promptDlg", 1, chart_obj.report_medium_timesleep)
        ok_button = util_obj.validate_and_get_webdriver_object("#promptDlg div[id='btnOK'] img", 'ok-button')
        core_util_obj.left_click(ok_button)
        document_obj.customize_active_dashboard_properties(btn_type='cancel')
        
        """
        Step 16: Verify the Drop Down and List prompts are preserved
        """
        chart_obj.wait_for_number_of_element("#Prompt_1", 1, chart_obj.report_medium_timesleep)
        combo_box = util_obj.validate_and_get_webdriver_object("#Prompt_1 .combo-box-label", "combo-box").text.strip()
        util_obj.asequal(expected_list_elements[0], combo_box, "Step 16.1: Verify the combo box")
        list_box = util_obj.validate_and_get_webdriver_objects("#Prompt_2 div[id^='BiListItem']", 'list-values')
        list_box_elements = [element.text for element in list_box]
        util_obj.asequal(expected_list_elements ,list_box_elements, "Step 16.2: Verify the list elements")
        
        """
        Step 17: Verify the report is preserved
        """
        report_obj.verify_report_data_set_in_preview('TableChart_1', 22, 3, 'C2231422_step12.xlsx', 'Step 17.1: Verify the table dataset')
        
        """
        Step 18: Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()