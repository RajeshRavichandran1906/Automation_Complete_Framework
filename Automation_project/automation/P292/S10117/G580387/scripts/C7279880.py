"""-------------------------------------------------------------------------------------------
Created on June 13, 2019
@author: Aftab/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22268772
Test Case Title =  Auto drill for non-hierarchy field used as a sorting field in chart 
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart

class C7279880_TestClass(BaseTestCase):

    def test_C7279880(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        format_css = "#FormatTab"
        chart_css = "#pfjTableChart_1"
        title_css = "#pfjTableChart_1 .scrollColTitle"
        raiser_class_css = "riser!s5!g24!mbar!r0!c0!"
        chart_frame_css = "#jschart_HOLD_0"

        """
            STEP 1 : Reopen the saved fex using API link:
        """
        chart_obj.edit_fex_using_api_url("P292_S10117%2FG580387", fex_name="IA-Chart")
        chart_obj.wait_for_visible_text(chart_css, "Revenue")

        """
            STEP 2 : Drag "Brand" from Data tab and Drop over the "Product,Category" in "Horizontal axis" bucket.
        """
        chart_obj.drag_field_from_data_tree_to_query_pane("Brand", 1, "Product,Category", 1, bucket_loc="middle")
        chart_obj.wait_for_visible_text(title_css, "Brand")
        
        """
            STEP 02.01 : Check "Brand" replaces "Product,Category".
        """
        chart_obj.verify_field_listed_under_querytree("Horizontal Axis", "Brand", 1, "STEP 02.01 : Check 'Brand' replaces 'Product,Category'")

        """
            STEP 3 : Click "Format" tab and Click "Auto Drill" button.
        """
        chart_obj.select_ia_ribbon_item("Format", "auto_drill")
 
        """
            STEP 4 : Click "Run" in tollbar and Hover over any bar.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.switch_to_frame(frame_css="body > iframe")
        chart_obj.wait_for_visible_text(chart_frame_css, "Revenue")
        
        """
            STEP 5 : Hover over "Drill down to"
            STEP 05.01 : Check the drill menu appears only for Region and Year.
        """
        tooltip_list = ['Store Business Sub Region', 'Sale Year/Quarter']
        chart_obj.verify_autolink_tooltip_submenu(raiser_class_css, "Drill down to", tooltip_list, "STEP 05.01 : Check the drill menu appears only for Region and Year.")
        chart_obj.switch_to_default_content()
        
        """
            STEP 6 : Click "IA" menu and Click "Save As" option.
            STEP 7 : Enter "C7279880" in Tittle textbox and Click "Save" button.
        """
        chart_obj.save_as_from_application_menu_item("C7279880", target_table_path="P292_S10117->G580387")

        """
            STEP 8 : Click "IA" menu and Select "Close" option.
        """
        chart_obj.select_ia_application_menu("close")
        
        """
            STEP 9 : Logout
        """
        chart_obj.logout_chart_using_api()
        
        """
            STEP 10 : Reopen the saved fex using API link
        """
        chart_obj.edit_fex_using_api_url("P292_S10117%2FG580387", fex_name="C7279880")
        chart_obj.wait_for_visible_text(chart_css, "Revenue")

        """
            STEP 11 : Click "Format" tab.
        """
        chart_obj.switch_ia_ribbon_tab('Format')
        chart_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 11.01 : Check" Auto Drill" is still selected.
        """
        chart_obj.verify_ribbon_item_selected("format_auto_drill", "11.01")
        
        """
            STEP 12 : Click "IA" menu and Select "Close" option.
        """
        chart_obj.select_ia_application_menu("close")
        
        """
            STEP 13 : Logout
        """
        chart_obj.logout_chart_using_api()
        
if __name__ == '__main__':
    unittest.main()