'''
Created on Jun 19, 2019

@author: Varun/Prasanth
Testcase Name : Run simple insight chart in IE browser
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2509821

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.lib import core_utility
from common.wftools.designer_chart import Designer_Insight

class C2509821_TestClass(BaseTestCase):
    
    def test_C2509821(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        insight_obj=Designer_Insight(self.driver)
        
        """
        Test case variables
        """
        project_id=core_util_obj.parseinitfile("project_id")
        suite_id=core_util_obj.parseinitfile("suite_id")
        group_id=core_util_obj.parseinitfile("group_id")
        folder_path=project_id+"_"+suite_id+"/"+group_id
        
        """
        STEP 1:Launch the API to create new Chart.
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=chart&master=baseapp/wf_retail_lite
        """
        chart_obj.invoke_chart_tool_using_api("baseapp/wf_retail_lite", mrid="mrid", mrpass="mrpass", folder_path=folder_path)
        chart_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        
        """
        STEP 2 : Add "Product, Category" and "Cost of Goods"
        """
        chart_obj.double_click_on_datetree_item("Product,Category", 1)
        chart_obj.wait_for_visible_text("#singleReportPanel", "Product Category")
        chart_obj.double_click_on_datetree_item("Cost of Goods", 1)
        chart_obj.wait_for_visible_text("#singleReportPanel", "Cost of Goods")
        
        """
        STEP 3 : Select Format > Run with > Insight
        """
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        chart_obj.select_ia_ribbon_item('Format', "insight")
        
        """
        STEP 4: Click Run 
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_visible_text(".main-box", "Product Category")
        
        """
        STEP 5 : Verify insight chart run fine and displayed options shelf
        """
        chart_obj.verify_x_axis_title_in_run_window(['Product Category'], parent_css=".main-box", msg='Step 05.01')
        chart_obj.verify_y_axis_title_in_run_window(["Cost of Goods"], parent_css=".main-box", msg='Step 05.02')
        expected_x_axis_label_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css=".main-box", msg='Step 05.03')
        expected_y_axis_label_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_label_list, parent_css=".main-box", msg='Step 05.04')
        
        insight_obj.verify_insight_querybox_text_options(['Vertical Axis', 'Group', 'Color'], "Step 05.05 : Verify_insight_querybox_text_options")
        insight_obj.verify_insight_optionsbox_text(['Reset', 'Swap  Axis', 'Change chart', 'Show Filter', 'Swap  Axis', 'More Options'], "Step 05.06 : Verify_insight_optionsbox_text")
        
        """
        STEP 6 : Click IA > Close > click No.
        """
        chart_obj.switch_to_default_content()
        chart_obj.close_ia_without_save()
        
        """
        STEP 7 :Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
if __name__ == '__main__':
    unittest.main()
        