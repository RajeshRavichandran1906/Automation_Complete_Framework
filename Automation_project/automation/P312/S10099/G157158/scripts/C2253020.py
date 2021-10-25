'''
Created on Feb 15, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253020
TestCase Name = IA-3987:Drill down to 2nd level of hierarchy in a Visualization throws FOC ERRORS-lacks quotes
'''

import unittest, time
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase

class C2253020_TestClass(BaseTestCase):

    def test_C2253020(self):
        
        """
        CLASS OBJECTS
        """
        visual = visualization.Visualization(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2253020'
        sleep_time=4
        position=1
        riser=[7,5,10]
        time_out=300
        num=1
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/WF_RETAIL_LITE
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02: Add Product Category to Horizontal axis and Quantity Sold to Vertical axis.
        """
        field_name='Product,Category'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, riser[0], time_out)
        
        field_name='Quantity,Sold'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 text[class^='yaxis-title']"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        
        """
        Step 03: Verify label values
        """
        visual.verify_x_axis_title(['Product Category'], msg='Step 03.01')
        visual.verify_y_axis_title(['Quantity Sold'], msg='Step 03.02')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 03.03')
        expected_yaxis_label=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 03.04')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', num, riser[0], msg='Step 03.05')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 03.06')
        
        """
        Step 04: Verify query pane
        """
        visual.verify_field_listed_under_querytree( 'Vertical Axis', 'Quantity,Sold', position, "Step 04.01:")
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Category', position, "Step 04.02:")
        
        """
        Step 05: Verify all bar riser values
        """
        expected_tooltip_list=['Product Category:Accessories', 'Quantity Sold:511,667', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 05.01: Verify Tooltip') 
        expected_tooltip_list=['Product Category:Stereo Systems', 'Quantity Sold:1,114,332', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_tooltip('riser!s0!g4!mbar!', expected_tooltip_list,'Step 05.02: Verify Tooltip') 
        
        """
        Step 06: Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Step 07: Hover over on any riser(Stereo systems) and Choose Drill Down. 
        """
        parent_css="#MAINTABLE_wbody1 text[class^='xaxisOrdinal-title']"
        visual.wait_for_visible_text(parent_css, visble_element_text='ProductCategory', time_out=time_out)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser[0], time_out)
        visual.select_tooltip('riser!s0!g4!mbar!', 'Drill down to Product Subcategory')
        
        """
        Step 08: Verify product category is drill down to Product Subcategory
        """
        visual.verify_x_axis_title(['Product Subcategory'], msg='Step 08.01')
        visual.verify_y_axis_title(['Quantity Sold'], msg='Step 08.02')
        expected_xaxis_label=['Boom Box', 'Home Theater Systems', 'Receivers', 'Speaker Kits', 'iPod Docking Station']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 08.03')
        expected_yaxis_label=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '400K', '450K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 08.04')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', num, riser[1], msg='Step 08.05')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 08.06')
        
        """
        Step 09: Verify drill down bar values
        """
        expected_tooltip_list=['Product Subcategory:Receivers', 'Quantity Sold:150,568', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Category', 'Drill down to Model']
        visual.verify_tooltip('riser!s0!g2!mbar!', expected_tooltip_list,'Step 09.01: Verify Tooltip') 
        
        """
        Step 10: Hover over on any riser (Speaker Kits) and Choose Drill Down
        """
        visual.select_tooltip('riser!s0!g3!mbar!', 'Drill down to Model')
        
        """
        Step 11: Verify Product subcategory is drilldown to Model
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser[2], time_out)
        visual.verify_x_axis_title(['Model'], msg='Step 11.01')
        visual.verify_y_axis_title(['Quantity Sold'], msg='Step 11.02')
        expected_xaxis_label=['BOSE AM10IV', 'BOSE AM16II', 'Harman Kardon HKTS20BQ', 'Harman Kardon HKTS30BQ', 'Onkyo SKSHT540', 'Onkyo SKSHT750B', 'Onkyo SKSHT870', 'Polk Audio LSIFX', 'Polk Audio RM705', 'Yamaha NSSP1800']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 11.03')
        expected_yaxis_label=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 11.04')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', num, riser[2], msg='Step 11.05')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 11.06')
        
        """
        Step 12: Verify first and last 2 bar riser values
        """
        expected_tooltip_list=['Model:BOSE AM10IV', 'Quantity Sold:15,732', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Subcategory']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 12.01: Verify Tooltip') 
        expected_tooltip_list=['Model:Polk Audio RM705', 'Quantity Sold:50,462', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Subcategory']
        visual.verify_tooltip('riser!s0!g8!mbar!', expected_tooltip_list,'Step 12.02: Verify Tooltip') 
        visual.take_run_window_snapshot(Test_Case_ID, '12')
        
        """
        Step 13: Close the output window
        """
        visual.switch_to_previous_window()
        
        """
        Step 14: Click "Save" in the toolbar > Type C2141371 > Click "Save" in the Save As dialog
        """
        parent_css="#applicationButton img"
        visual.wait_for_number_of_element(parent_css, num)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, riser[0])
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 15: Logout of the IA API using the following URL: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()