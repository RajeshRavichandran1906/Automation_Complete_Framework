'''
Created on Jun 11, 2019

@author: Sudhan/Pearlson Joyal 
Test rail link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/7922375
TestCase Name : Single-select Dynamic Filter using Define from master
'''

import unittest
from common.wftools import report
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata

class C7922375_TestClass(BaseTestCase):

    def test_C7922375(self):
        """
            CLASS OBJECTS 
        """
        report_obj = report.Report(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """
            TESTCASE ID Variable 
        """
        tablechart_css = "#TableChart_1"
        querypane_css = "#queryBoxColumn"
        cancel_css = "#dlgWhere_btnCancel"
        case_id = 'C7922375'
        table_css="table[summary='Summary']"
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        
        """
            STEP 1 : Create new IA report using EMDPATA mas file using API:
            http://machine_name:port/alias/ia?tool=Report&master=baseapp/empdata&item=IBFS:/WFC/Repository/P292_S10117/G636265
        """
        report_obj.invoke_ia_tool_using_new_api_login(master='baseapp/empdata')
        report_obj.wait_for_visible_text(tablechart_css, "Drag and drop")        
         
        """
            STEP 2 : Double click add LAST NAME, AREA and SALARY fields
        """
        report_obj.double_click_on_datetree_item('LASTNAME', 1)
        report_obj.wait_for_visible_text(querypane_css, "LASTNAME")
        
        report_obj.double_click_on_datetree_item('AREA', 1)
        report_obj.wait_for_visible_text(querypane_css, "AREA")
        
        report_obj.double_click_on_datetree_item('SALARY', 1)
        report_obj.wait_for_visible_text(querypane_css, "SALARY")     
         
        """
            STEP 3 : Drag "AREA" to Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter("AREA", field_position=1)
        report_obj.wait_for_visible_text(cancel_css, "Cancel")    
         
        """
            STEP 4 : Double-click <Value>, Select Type = "Parameter"
        """
        report_obj.open_filter_where_value_dialog()
        report_obj.select_filter_type("Parameter")
                
        """
            STEP 5 : Select "Dynamic" radio button
        """   
        report_obj.select_filter_parameter_type("Dynamic")
                 
        """
            STEP 6 : Select "Area" field and click OK
        """
        report_obj.select_field_in_filter_tree("Dimensions->AREA", 1)
        report_obj.close_filter_where_value_popup_dialog()
         
        """
            STEP 7 : Click OK in filtering condition
        """
        report_obj.close_filter_dialog()
        
        """
            STEP 8 : Click Run
        """
        report_obj.run_report_from_toptoolbar()
        
        """
            STEP 8.01 : Verify auto prompt (AREA = CENTRAL) is displayed as below
        """
        report_obj.switch_to_frame()
        report_obj.verify_selected_field_dropdown_value_in_autoprompt("AREA:", "CENTRAL", "STEP 8.01 : Verify auto prompt (AREA = CENTRAL) is displayed")
        
        """
            STEP 9 : Click on AREA and select CORPORATE
        """        
        report_obj.select_field_filter_values_dropdown_in_auto_prompt('AREA:')
        report_obj.select_single_field_filter_value_in_auto_prompt(['CORPORATE'])
         
        """
            STEP 10 : Click Run with filter values
        """
        report_obj.run_auto_prompt_report()
        report_obj.wait_for_number_of_element("iframe[name='wfOutput']",1) 
        
        """
            STEP 10.01 : Verify report appears as below
        """
        report_obj.switch_to_frame("iframe[name='wfOutput']") 
        report_obj.wait_for_visible_text(table_css, "AREA")
        #report_obj.create_html_report_dataset(DATA_SET_NAME1)
        report_obj.verify_html_report_dataset(DATA_SET_NAME1,"Step 10.01 : Verify report")
        report_obj.switch_to_default_content()    
        
        """
            STEP 11 : Close IA without saving
        """
        report_obj.close_ia_without_save()
         
        """
            STEP 12 : Logout WF using API:
            http://machine_name:port/alias/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
         
if __name__ == '__main__':
    unittest.main()