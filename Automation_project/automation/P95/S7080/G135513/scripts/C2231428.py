'''
Created on January 30, 2019

@author:Kavin 

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2231428
TestCase Name = DOC:Restoring a multiple page Document with filter objects, all objects appear on last page 145196
'''

import unittest
from time import sleep
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.wftools import report
from common.wftools import document
from common.lib import core_utility
from common.pages.ia_miscelaneous import IA_Miscelaneous

class C2231428_TestClass(BaseTestCase):

    def test_C2231428(self):
        """
        Test case Object's
        """
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        document_obj = document.Document(self.driver)
        report_obj = report.Report(self.driver)
        chart_obj=chart.Chart(self.driver)
        mis_obj = IA_Miscelaneous(self.driver)
        
        """
        Test case variables
        """
        TestcaseID= 'C2231428'
        table_css="TableChart_1"
        table_css_2="TableChart_2"
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        property_dialog_css="#adpPropertiesDlg"
        dropdown_css="#Prompt_1"
        radio_button_css="#Prompt_2"
        dropdown_box=['[All]']
        list_box=['[All]','ALFA ROMEO','AUDI','BMW','DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        """ 
        Step 1: Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=ibisamp/car&item=IBFS:/WFC/Repository/P95_S7080/G135513
        """
        document_obj.invoke_ia_tool_using_api(tool='document', master='ibisamp/car',mrid='mriddev',mrpass='mrpassdev', report_css="#canvasContainer", no_of_element=1)
        
        """
        Step 2: Add fields COUNTRY & CAR for first page.
        Expect to see the following Preview pane.
        """
        chart_obj.double_click_on_datetree_item('COUNTRY', 1)
        document_obj.wait_for_visible_text("#"+table_css, 'COUNTRY', document_obj.report_medium_timesleep)
        chart_obj.double_click_on_datetree_item('CAR', 1)
        document_obj.wait_for_visible_text("#"+table_css, 'CAR', document_obj.report_medium_timesleep)
        report_obj.verify_report_data_set_in_preview(table_css, 10, 2, TestcaseID+"_DS_02.xlsx", "Step 02 : verify dataset")
        
        """
        Step 3: Select Insert Tab, click 'Drop Down, place object next to the report.
        Right-click Dropdown object on Canvas and select 'Properties'.
        Click on 'Field' dropdown box in ADP dlg and select COUNTRY.
        Click OK.
        Expect to see the following Document preview pane with a report and a Dropdown object
        """
        document_obj.select_ia_ribbon_item("Insert", "drop_down")
        document_obj.drag_drop_document_component(dropdown_css, "#theCanvas", 0, 50, target_drop_point='top_middle')
        document_obj.choose_right_click_menu_item_for_prompt(dropdown_css, 'Properties')
        document_obj.wait_for_number_of_element(property_dialog_css, 1, chart_obj.report_medium_timesleep)
        document_obj.customize_active_dashboard_properties(source={'select_field':'COUNTRY'})
        report_obj.verify_report_data_set_in_preview(table_css, 10, 2, TestcaseID+"_DS_03.xlsx", "Step 03.1 : verify dataset")
        document_obj.verify_prompts_in_preview('dropdown', dropdown_css, dropdown_box, 'Step 03.2: Verify the dropdown box') 
        
        """
        Step 4: Click 'Page' on Ribbon to create a second page.
        Add fields CAR & MODEL.
        Select Insert and click 'List' on the ribbon, place object next to the report.
        Right-click List object on Canvas and select 'Properties'.
        Click on 'Report' dropdown box and select 'Report2'
        Click on 'Field' dropdown box and select CAR. 
        Expect to see the following Properties menu for
        Page 2.
        Step 05: Click OK to the Properties menu.
        Expect to see the Page 2 of the Document with the CAR & MODEL report along with a Listbox object.
        """
        document_obj.select_or_verify_document_page_menu("New Page")
        chart_obj.double_click_on_datetree_item("CAR", 1)
        document_obj.wait_for_visible_text("#"+table_css_2, 'CAR', document_obj.report_medium_timesleep)
        chart_obj.double_click_on_datetree_item("MODEL", 1)
        document_obj.wait_for_visible_text("#"+table_css_2, 'MODEL', document_obj.report_medium_timesleep)
        report_obj.verify_report_data_set_in_preview(table_css_2, 18, 2, TestcaseID+"_DS_04.xlsx", "Step 04 : verify dataset")
        document_obj.select_ia_ribbon_item("Insert", "list")
        document_obj.drag_drop_document_component(radio_button_css, "#theCanvas", 0, 50, target_drop_point='top_middle')
        document_obj.choose_right_click_menu_item_for_prompt(radio_button_css, 'Properties')
        document_obj.wait_for_number_of_element(property_dialog_css, 1, chart_obj.report_medium_timesleep)
        document_obj.customize_active_dashboard_properties(source={'select_report':'Report2', 'select_field':'CAR'})
        document_obj.choose_right_click_menu_item_for_prompt(radio_button_css, 'Properties')
        document_obj.wait_for_number_of_element(property_dialog_css, 1, chart_obj.report_medium_timesleep)
        document_obj.customize_active_dashboard_properties(source={"verify_report":"Report2","verify_field":"CAR"})
        report_obj.verify_report_data_set_in_preview(table_css_2, 18, 2, TestcaseID+"_DS_05.xlsx", "Step 05.1 : verify dataset")
        document_obj.verify_prompts_in_preview('listbox',radio_button_css, list_box, 'Step 05.2: Verify the list box')

        """
        Step 6: Exit and save the Document.
        """
        
        chart_obj.save_as_chart_from_menubar(TestcaseID)
        document_obj.api_logout()
        
        """
        Step 7: http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/P95/S10142/Document.fex&tool=Document
        Expect to see the Page 1 of the Document, containing the COUNTRY & CAR report and the Dropdown object.
        """
        mis_obj.edit_fex_using_api(folder_path, tool="Document", fex_name=TestcaseID, mrid='mriddev',mrpass='mrpassdev')
        sleep(chart_obj.document_component_timesleep)
        report_obj.verify_report_data_set_in_preview(table_css, 10, 2, TestcaseID+"_DS_07.xlsx", "Step 07.1 : verify dataset")
        document_obj.verify_prompts_in_preview('dropdown', dropdown_css, dropdown_box, 'Step 07.2: Verify the dropdown box')
        
        """
        Step 8: Click on Page 2.
        Expect to see the Page 2 of the Document, containing the CAR & MODEL report and the Listbox object.
        """
        document_obj.select_or_verify_document_page_menu("Page 2",default_page_name="Page 1")
        report_obj.verify_report_data_set_in_preview(table_css_2, 18, 2, TestcaseID+"_DS_08.xlsx", "Step 08.1 : verify dataset")
        document_obj.verify_prompts_in_preview('listbox', radio_button_css, list_box, 'Step 08.2: Verify the list box')
        
        """
        Step 9: Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp

        """
        document_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()