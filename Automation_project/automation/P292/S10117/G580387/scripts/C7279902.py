"""-------------------------------------------------------------------------------------------
Created on June 17, 2019
@author: magesh/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22268776
Test Case Title =  Drilling all the way down and up a long hierarchy path in chart
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib import utillity
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables

class C7279902_TestClass(BaseTestCase):

    def test_C7279902(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
        utils = utillity.UtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        format_css = "#FormatTab"
        chart_frame_css = "#jschart_HOLD_0"
        chart_css = "#pfjTableChart_1"
        breadcrumb_css = "foreignObject.title"
        
        """
            STEP 1 : Reopen the saved fex using API link:
        """
        chart_obj.edit_fex_using_api_url("P292_S10117%2FG580387", fex_name="IA-Chart")
        chart_obj.wait_for_visible_text('#TableChart_1', visble_element_text='EMEA', time_out=chart_obj.chart_long_timesleep)
        utils.wait_for_page_loads(chart_obj.home_page_long_timesleep) #firefox its required
        
        """
            STEP 2 : Click "Format tab" and Click "Auto Drill"option.
        """
        chart_obj.select_ia_ribbon_item("Format", "auto_drill")
    
        """
            STEP 3 : Click "Run" in toolbar.    
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.switch_to_frame(frame_css="body > iframe")
        chart_obj.wait_for_visible_text(chart_frame_css, visble_element_text="Revenue", time_out=chart_obj.chart_long_timesleep)
        
        """
            STEP 4 : Hover over Top bar(2016) in "Stereo Systems" under "North America" > Hover over "Drill down to" and Click "Store Business Sub Region".
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s5!g4!mbar!r0!c1!", "Drill down to->Store Business Sub Region")
        chart_obj.wait_for_visible_text(breadcrumb_css, visble_element_text="North America", time_out=chart_obj.chart_long_timesleep)
 
        """
            STEP 5 : Hover over "West" > Hover over "Drill down to" and Click "Store Country".
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s0!g0!mbar!r0!c7!", "Drill down to->Store Country" )
        chart_obj.wait_for_visible_text(breadcrumb_css, visble_element_text="West", time_out=chart_obj.chart_long_timesleep)
        
        """
            STEP 6 : Hover over "United States" > Hover over "Drill down to" and Click "Store State Province".
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s0!g0!mbar!r0!c0!", "Drill down to->Store State Province" )
        chart_obj.wait_for_visible_text(breadcrumb_css, "United States", time_out=chart_obj.chart_long_timesleep)
 
        """
            STEP 7 : Hover over "California" > Hover over "Drill down to" and Click "Store City"
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s0!g0!mbar!r0!c1!", "Drill down to->Store City")
        chart_obj.wait_for_visible_text(breadcrumb_css, "California", time_out=chart_obj.chart_long_timesleep)
        
        """
            STEP 8 : Hover over "San Diego" > Hover over "Drill down to" and Click "Store Postal Code"
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s0!g0!mbar!r0!c1!", "Drill down to->Store Postal Code")
        chart_obj.wait_for_visible_text(breadcrumb_css, "San Diego", time_out=chart_obj.chart_long_timesleep)
    
        """
            STEP 9 : Hover over "92101" > Hover over "Drill down to" and Click "Store Name".
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s0!g0!mbar!r0!c0!", "Drill down to->Store Name")
        chart_obj.wait_for_visible_text(breadcrumb_css, "92101", time_out=chart_obj.chart_long_timesleep)
    
        """
            STEP 09.01 : Check the Breadcrumb and following Output.
        """
        chart_obj.verify_x_axis_label_in_run_window(['Stereo Systems'], msg="Step 09.01")
        chart_obj.verify_y_axis_label_in_run_window(['0', '200K', '400K', '600K', '800K', '1,000K'], msg="Step 09.02")
        chart_obj.verify_y_axis_title_in_run_window(['Revenue'], msg="Step 09.03")
        chart_obj.verify_legends_in_run_window(['Sale Year', '2016'], msg="Step 09.04")
        chart_obj.verify_column_label_in_run_window(['Store Name : Product Category', 'San Diego'], msg="Step 09.05")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 1, msg="Step 09.06")
        chart_obj.verify_chart_autodrill_breadcrumb_text(['Home->(StoreBusinessRegion)NorthAmerica->(StoreBusinessSubRegion)West->(StoreCountry)UnitedStates->(StoreStateProvince)California->(StoreCity)SanDiego->(StorePostalCode)92101'], "09.07")
        
        """
            STEP 10 : Hover over "San Diego" and Click "Drill up to Store Postal Code".
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s0!g0!mbar!r0!c0!", "Go up to Store Postal Code")
        chart_obj.wait_for_visible_text(breadcrumb_css, "San Diego", time_out=chart_obj.chart_long_timesleep)
 
        """
            STEP 11 : Hover over "92101" and Click "Drill up to Store City".
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s0!g0!mbar!r0!c0!", "Go up to Store City")
        chart_obj.wait_for_visible_text(breadcrumb_css, "California", time_out=chart_obj.chart_long_timesleep)
 
        """
            STEP 12 : Hover over "San Diego" and Click "Drill up to Store State Province".
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s0!g0!mbar!r0!c1!", "Go up to Store State Province")
        chart_obj.wait_for_visible_text(breadcrumb_css, "United States", time_out=chart_obj.chart_long_timesleep)
        
        """
            STEP 13 : Hover over "California" and Click "Drill up to Store Country".
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s0!g0!mbar!r0!c1!", "Go up to Store Country")
        chart_obj.wait_for_visible_text(breadcrumb_css, "West", time_out=chart_obj.chart_long_timesleep)
        
        """
            STEP 14 : Hover over "United States" and Click "Drill up to Store Business Sub Region".
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s0!g0!mbar!r0!c0!", "Go up to Store Business Sub Region")
        chart_obj.wait_for_visible_text(breadcrumb_css, "North America", time_out=chart_obj.chart_long_timesleep)
 
        """
            STEP 15 : Hover over "West" and Click "Drill up to Store Business Region".
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s0!g0!mbar!r0!c7!", "Go up to Store Business Region")
        chart_obj.wait_for_visible_text(chart_frame_css, "Revenue", time_out=chart_obj.chart_long_timesleep)
    
        """
            STEP 15.01 : Check the following output.
        """
        if Global_variables.browser_name == "chrome" or "cr" :
            chart_obj.verify_x_axis_label_in_run_window(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Product...', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Product...', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Product...', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Product...'], xyz_axis_label_length=9, msg="Step 15.01")
        else :
            chart_obj.verify_x_axis_label_in_run_window(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], xyz_axis_label_length=9, msg="Step 15.01")
        chart_obj.verify_y_axis_label_in_run_window(['0', '40M', '80M', '120M', '160M', '200M'], msg="Step 15.02")
        chart_obj.verify_y_axis_title_in_run_window(['Revenue'], msg="Step 15.03")
        chart_obj.verify_legends_in_run_window(['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016'], msg="Step 15.04")
        chart_obj.verify_column_label_in_run_window(['Store Business Region : Product Category', 'EMEA', 'North America', 'Oceania', 'South America'], msg="Step 15.05")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 139, msg="Step 15.06" )
        
        """
            STEP 16 : Click "IA" menu and Select "Save As" option.
            STEP 17 : Enter "C7279902 " in Title textbox and Click "Save" button.
        """
        chart_obj.switch_to_default_content()
        chart_obj.save_as_from_application_menu_item("C7279902", target_table_path="P292_S10117->G580387")
 
        """
            STEP 18 : Logout
        """
        chart_obj.logout_chart_using_api()
    
        """
            STEP 19 : Reopen the saved fex using API link
        """
        chart_obj.edit_fex_using_api_url("P292_S10117%2FG580387", fex_name="C7279902")
        chart_obj.wait_for_visible_text(chart_css, "Revenue", time_out=chart_obj.chart_long_timesleep)
        utils.wait_for_page_loads(chart_obj.home_page_long_timesleep) #firefox its required
        
        """
            STEP 20 : Click "Format tab".
        """
        chart_obj.switch_ia_ribbon_tab('Format')
        chart_obj.wait_for_visible_text(format_css, "Features", time_out=chart_obj.chart_long_timesleep)
    
        """
            STEP 20.01 : Check" Auto Drill" is still selected.
        """
        chart_obj.verify_ribbon_item_selected("format_auto_drill", "20.01")
    
        """
            STEP 21 : Logout
        """
        chart_obj.logout_chart_using_api()
    
if __name__ == '__main__':
    unittest.main()