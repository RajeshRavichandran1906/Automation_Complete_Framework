'''
Created on Jun 20, 2019

@author: Varun/Prasanth
Testcase Name : Horizontal Axis on Circle Plot is BY when sort field is added
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2510334

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.lib import core_utility
from common.wftools.designer_chart import Designer_Insight
from common.pages.insight_header import Insight_Header

class C2510334_TestClass(BaseTestCase):
    
    def test_C2510334(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        insight_obj=Designer_Insight(self.driver)
        insight_header_obj= Insight_Header(self.driver)
        
        """
        Test case variables
        """
        project_id=core_util_obj.parseinitfile("project_id")
        suite_id=core_util_obj.parseinitfile("suite_id")
        group_id=core_util_obj.parseinitfile("group_id")
        folder_path=project_id+"_"+suite_id+"/"+group_id
        
        """
        STEP 1:Launch the API to create new Chart.
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=chart&master=ibisamp/car
        """
        chart_obj.invoke_chart_tool_using_api("ibisamp/car", mrid="mrid", mrpass="mrpass", folder_path=folder_path)
        chart_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        
        """
        STEP 2 : Select Format > Run with > Insight
        """
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        chart_obj.select_ia_ribbon_item('Format', "insight")
        
        """
        STEP 3: Click Run 
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_visible_text(".main-box","Vertical Axis")
        
        """
        STEP 4: Click Chart picker drop down > Select Circle plot 
        """
        insight_header_obj.change_chart_type_from_chart_picker_option("Circle Plot")
        
        """
        STEP 5: Click on Horizontal Axis bucket > select "COUNTRY" 
        """
        insight_header_obj.search_and_add_field_to_query_bucket("Horizontal Axis", "COUNTRY")
        chart_obj.wait_for_visible_text(".main-box","COUNTRY")
        
        """
        STEP 6: Verify Horizontal axis shows "COUNTRY" values (By field) 
        """
        insight_header_obj.verify_selected_field_in_query_bucket("Horizontal Axis", "By COUNTRY", "06.01")

        """
        STEP 7: Click on Vertical Axis bucket > select "DEALER_COST" 
        """
        insight_header_obj.search_and_add_field_to_query_bucket("Vertical Axis", "DEALER_COST")
        chart_obj.wait_for_visible_text(".main-box","DEALER_COST")
        
        """
        STEP 8 Verify following insight circle plot chat displayed
        """
        chart_obj.verify_x_axis_title_in_run_window(["COUNTRY"], parent_css=".main-box", msg='Step 08.01')
        chart_obj.verify_y_axis_title_in_run_window(["DEALER_COST"], parent_css=".main-box", msg='Step 08.02')
        expected_x_axis_label_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css=".main-box", msg='Step 08.03')
        expected_y_axis_label_list=['0', '15K', '30K', '45K', '60K']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_label_list, parent_css=".main-box", msg='Step 08.04')
        chart_obj.verify_number_of_risers("#runbox_id circle", 1, 5, "Step 08.05 : Verify displayed circle plot chat")
        
        insight_obj.verify_insight_querybox_text_options(['Vertical Axis', 'Horizontal Axis', 'Size', 'Detail', 'Color'], "Step 08.06 : Verify_insight_querybox_text_options")
        insight_obj.verify_insight_optionsbox_text(['Reset', 'Swap  Axis', 'Change chart', 'Show Filter', 'Swap  Axis', 'More Options'], "Step 08.07 : Verify_insight_optionsbox_text")
        
        """
        STEP 9 : Click IA > Close > click No.
        """
        chart_obj.switch_to_default_content()
        chart_obj.close_ia_without_save()
        
        """
        STEP 10 :Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
if __name__ == '__main__':
    unittest.main()
        