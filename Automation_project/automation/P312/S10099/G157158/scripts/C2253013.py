'''
Created on Feb 14, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10099
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253013
Test_Case Name : IA-4419:Drilldown when more than one by field gives error, can't continue
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2253013_TestClass(BaseTestCase):

    def test_C2253013(self):
        
        Test_Case_ID = "C2253013"
        total_no_of_riser_css="#MAINTABLE_wbody1 rect[class^='riser']"  
        wait_time_in_sec=120
        visual = visualization.Visualization(self.driver)
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,total_risers, step_num, tooltip=None):
            visual.verify_x_axis_title(x_title, msg='Step' + str(step_num) + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step' + str(step_num) + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + str(step_num) + '.3'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + str(step_num) + '.4'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step' + str(step_num) + '.5: Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class*='"+riser+"']", 'lochmara',  msg='Step' + str(step_num) + '.6: Verify riser color')
            if tooltip!=None:
                visual.verify_tooltip(riser,tooltip,msg='Step' + str(step_num) + '.7: Verify riser tooltip')
            
        """
        Step1:Launch the IA API with wf_retail_lite
         http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8358%2F
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step02: Double click "Cost of Goods", "Product,Categroy" and "Store,Business,Region"
        """
        visual.double_click_on_datetree_item('Cost of Goods', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "CostofGoods", 45)
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "ProductCategory", 45)
        visual.double_click_on_datetree_item('Store,Business,Region', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "ProductCategory:StoreBusinessRegion", 45)
        
        """
        Step03: Hover on Computers:NorthAmerica
        Step04: select > drill down > "Store Business Sub Region"
        Step05: Verify query added to filter pane
        """
        Computers_North_America_riser='riser!s0!g9!mbar'
        visual.select_tooltip(Computers_North_America_riser, 'Drill down to->Store Business Sub Region')
        no_of_riser=8
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec )
        visual.verify_field_in_filterbox('PRODUCT_CATEGORY and BUSINESS_REGION', 1, msg="Step08: Verify  Query added to filter pane")
             
        """
        Step06: Click Run in the toolbar
        Step07: Verify output
        Step08: Close the output window
        """
        expected_xaxis_labels=['Computers : Canada', 'Computers : East', 'Computers : Mexico', 'Computers : Midwest', 'Computers : Northeast', 'Computers : South', 'Computers : Southeast', 'Computers : West']
        expected_yaxis_labels=['0', '5M', '10M', '15M', '20M', '25M', '30M']
        Computers_riser="riser!s0!g0!mbar"
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)    
        verify_bar_chart(['Product Category : Store Business Sub Region'],['Cost of Goods'],expected_xaxis_labels,expected_yaxis_labels,Computers_riser,no_of_riser,'12')  
        
        visual.take_run_window_snapshot(Test_Case_ID, '12')
        visual.switch_to_previous_window()
        
        """
        Step09:Click "Save" in the toolbar > Type C2141212 > Click "Save" in the Save As dialog
        Step10: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)  
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        visual.logout_visualization_using_api()

if __name__ == '__main__':
    unittest.main()        
