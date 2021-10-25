'''
Created on Jun 18, 2019

@author: Varun/Prasanth
Testcase Name : Auto Drill with ESRI Charts
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/7279905

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.wftools.visualization import Visualization
from common.lib import global_variables
from common.lib import core_utility
from common.pages import ia_resultarea

class C7279905_TestClass(BaseTestCase):
    
    def test_C7279905(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
        visual_obj=Visualization(self.driver)
        global_var_obj=global_variables.Global_variables()
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        ia_result_obj=ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Test case variables
        """
        case_id=global_var_obj.current_test_case
        project_id=core_util_obj.parseinitfile("project_id")
        suite_id=core_util_obj.parseinitfile("suite_id")
        group_id=core_util_obj.parseinitfile("group_id")
        folder_path=project_id+"_"+suite_id+"/"+group_id
        
        """
        STEP 1:Launch the API to create new Chart.
        http://machine:port/{alias}/ia?is508=false&tool=chart&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/P292_S10117/G580387
        """
        chart_obj.invoke_chart_tool_using_api("baseapp/wf_retail_lite", mrid="mrid", mrpass="mrpass", folder_path=folder_path)
        chart_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        
        """
        STEP 2 : Click "Format tab" and Click "ESRI Choropleth".
        """
        chart_obj.select_ia_ribbon_item('Format', "choropleth")
        chart_obj.wait_for_visible_text(".esriControlsBR", "Esri")
        
        """
        STEP 3 : Drag and drop "Revenue" to "Color" bucket in Query pane.
        """
        chart_obj.drag_field_from_data_tree_to_query_pane("Revenue", 1, "Color")
        chart_obj.wait_for_visible_text(".esriControlsBR", "Esri")
        
        """
        STEP 4 : Drag and drop "Store,Country" to "Layer" bucket in Query pane.
        """
        chart_obj.drag_field_from_data_tree_to_query_pane("Store,Country", 1, "Layer")
        chart_obj.wait_for_visible_text(".legend", "Revenue")
        
        """
        STEP 5 : Click on "Auto Drill" button.
        """
        chart_obj.select_ia_ribbon_item("Format", "auto_drill")
        
        """
        STEP 6: Click Run in toolbar
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.switch_to_frame("iframe")
        chart_obj.wait_for_visible_text(".esriControlsBR", "Esri")
        
        """
        STEP 7: Hover "Continental United States" (Green colored area between Canada and Mexico ).
        """
        """
        STEP 7.01 Expected: Check the following Output and the Tooltip.
        """
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 path", 1, 34, 'Step 07.01')
        chart_obj.verify_chart_color("jschart_HOLD_0", "riser!s0!g3!mregion!", "sorbus_2", "Step 07.02 : Verify map colors")
        ia_result_obj.verify_color_scale_esri_maps("jschart_HOLD_0",['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 07.03 ")
        chart_obj.verify_tooltip_in_run_window("riser!s0!g3!mregion!", ['Store Country:UNITED STATES', 'Revenue:$545,792,166.40', 'Drill down to Store State Province'], "Step 07.04 : Verify tooltip ", element_location='bottom_middle')

        """
        STEP 8: Click "Drill down to Store State Province".
        """
        visual_obj.select_tooltip("riser!s0!g3!mregion!", "Drill down to Store State Province", parent_css="jschart_HOLD_0", element_location="bottom_middle")
        
        
        """
        STEP 9: Hover over "California" and Click "Drill down to Store City".
        """
        visual_obj.select_tooltip("riser!s0!g4!mregion!", "Drill down to Store City", parent_css="jschart_HOLD_0")
        chart_obj.wait_for_visible_text(".esriControlsBR", "Esri")
        
        """
        STEP 9.01 Expected: Check the Breadcrumb and following Output.
        """
        expected_breadcrumb=['Home->(StoreCountry)UnitedStates->(StoreStateProvince)California']
        chart_obj.verify_chart_autodrill_breadcrumb_text(expected_breadcrumb, step_num="09.01")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 path", 1, 3, 'Step 09.02')
        chart_obj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mregion!", "elf_green", "Step 09.03 : Verify map colors")
        ia_result_obj.verify_color_scale_esri_maps("jschart_HOLD_0",['Revenue', '4.4M', '5M', '5.4M', '6M', '6.4M'], "Step 09.04 ")
        
        """
        STEP 10: Close the Run window.
        """
        chart_obj.switch_to_default_content()
    
        
        """
        STEP 11 : Click "ESRI Proportional Symbol" from "Chart types" under "Format tab".
        """
        chart_obj.select_ia_ribbon_item('Format', "proportional_symbol")
        chart_obj.wait_for_visible_text(".esriControlsBR", "Esri")
        
        """
        STEP 12: Click Run in toolbar
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.switch_to_frame("iframe")
        chart_obj.wait_for_visible_text(".esriControlsBR", "Esri")
        
        """
        STEP 13: Hover over "Continental United States" and Hover over "Drill down to".
        """
        """
        STEP 13.01 Expected: Check the following Output and the Tooltip.
        """
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 circle", 1, 34, 'Step 13.01')
        chart_obj.verify_chart_color("jschart_HOLD_0", "riser!s0!g33!mregion!", "lochmara", "Step 13.02 : Verify bubble colors")
        chart_obj.verify_tooltip_in_run_window("riser!s0!g33!mregion!", ['Store Country:UNITED STATES', 'Revenue:$545,792,166.40', 'Drill down to Store State Province'], "Step 13.04 : Verify tooltip")
        
        """
        STEP 14: Click "Drill down to Store State Province".
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s0!g33!mregion!", 'Drill down to Store State Province')
        
        """
        STEP 15: Hover over "California" and Click "Drill down to Store City".
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s0!g4!mregion!", 'Drill down to Store City')
        
        """
        STEP 15.01 Expected: Check the Breadcrumb and following Output.
        """
        expected_breadcrumb=['Home->(StoreCountry)UnitedStates->(StoreStateProvince)California']
        chart_obj.verify_chart_autodrill_breadcrumb_text(expected_breadcrumb, step_num="15.01")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 circle", 1, 3, 'Step 15.02')
        chart_obj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mregion!", "lochmara", "Step 15.03 : Verify bubble colors")
        
        """
        STEP 16: Click "Save" in toolbar Enter "C7279905" and click "Save" button.
        """
        chart_obj.switch_to_default_content()
        chart_obj.select_ia_toolbar_item("infomini_save")
        chart_obj.wait_for_number_of_element("#IbfsOpenFileDialog7_cbFileName input",1)
        chart_obj.save_file_in_save_dialog(case_id)
        
        """
        STEP 17: Logout
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        STEP 18:Reopen the saved fex using API link
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/C7279905.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name=folder_path, fex_name=case_id)
        chart_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        
        """
        STEP 19:Click "Format" tab
        """
        chart_obj.switch_ia_ribbon_tab("Format")
        
        """
        STEP 19.01 Expected : Check "Auto Drill" button is active.
        """
        chart_obj.verify_ribbon_item_selected("format_auto_drill", "19.01")
        
        """
        STEP 20: Logout
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()
        