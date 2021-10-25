'''
Created on Feb 26, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253019
TestCase Name = IA-4036:(FOC002) generated when delete filter created from "Drill Down" action
'''
import unittest, time, pyautogui
from common.wftools import visualization
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.pages.core_metadata import CoreMetaData
from common.pages.visualization_resultarea import Visualization_Resultarea

class C2253019_TestClass(BaseTestCase):

    def test_C2253019(self):
        """
        TESTCASE VARIABLES        
        """
        Test_Case_ID = 'C2253019'
        master_file = 'baseapp/wf_retail_lite'
        chart_type = 'heatmap'
        sleep_time = 4
        position = 1
        position2 = 2
        riser = [12,28,139,4,112]
        time_out = 200
        num = 1
        expected_num = [7,2]
        
        utils = UtillityMethods(self.driver)
        core_metaobj = CoreMetaData(self.driver)
        resultobj= Visualization_Resultarea(self.driver)
        visual = visualization.Visualization(self.driver)
                        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/WF_RETAIL_LITE
        """
        visual.invoke_visualization_using_api(master_file)
               
        """
        Step 02: Change to chart type Heatmap
        """
        visual.change_chart_type(chart_type)
        parent_css="#resultArea svg>g.chartPanel rect[class*='riser!']"
        visual.wait_for_number_of_element(parent_css, riser[0])
        
        """
        Step 03: Add Dimensions/Product/Product/Product,Category to Vertical axis
        """
        field_name='Product,Category'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 text[class^='zaxisOrdinal-label']"
        visual.wait_for_number_of_element(parent_css, expected_num[0], time_out)
        
        """
        Step 04: Add Dimensions/Store/Store/Store,Business,Region to Horizontal axis
        """
        visual.right_click_on_datetree_item('Store,Business,Region', position, context_menu_path='Add To Query->Horizontal Axis')
        parent_css="#MAINTABLE_wbody1 text[class^='xaxisOrdinal-title']"
        visual.wait_for_number_of_element(parent_css, expected_num[1], time_out)
        
        """
        Step 04.00: Verify x and y axis labels
        """
        x_axis_title=['Store Business Region','Product Category']
        visual.verify_x_axis_title(x_axis_title, msg='Step 04.01')
        expected_xaxis_label=['EMEA', 'North America', 'Oceania', 'South America']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 04.02')
        expected_zaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_z_axis_label(expected_zaxis_label, msg='Step 04.03')
        expected_legend_list=['0', '0.3', '0.5', '0.8', '1']
        visual.verify_legends(expected_legend_list, msg='Step 04.04')
        
        """
        Step 05: Add Measures/Gross Profit to Color
        """
        field_name='Gross Profit'
        visual.right_click_on_datetree_item(field_name, position, context_menu_path='Add To Query->Color')
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser[1], time_out)
        
        """
        Step 06: Add Dimensions/Shipments_Related/Transaction Date.Simple/Sale,Year to Rows
        """
        field_name='Sale,Year'
        visual.right_click_on_datetree_item(field_name, position, context_menu_path='Add To Query->Rows')
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser[2], time_out)
        
        """
        Step 07: Verify query pane
        """
        bucket_type='Rows'
        field_name='Sale,Year'
        visual.verify_field_listed_under_querytree(bucket_type, field_name, position, "Step 07.01")
        
        bucket_type='Vertical Axis'
        field_name='Product,Category'
        visual.verify_field_listed_under_querytree(bucket_type, field_name, position, "Step 07.02")
        
        bucket_type='Horizontal Axis'
        field_name='Store,Business,Region'
        visual.verify_field_listed_under_querytree(bucket_type, field_name, position, "Step 07.03")
        
        bucket_type='Color'
        field_name='Gross Profit'
        visual.verify_field_listed_under_querytree(bucket_type, field_name, position, "Step 07.04")
        
        """
        Step 08: Verify 2011:Televisions tooltip
        """
        expected_tooltip_list=['Sale Year:2011', 'Gross Profit:$1,064,257.53', 'Product Category:Televisions', 'Store Business Region:EMEA', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        riser_css="riser!s5!g0!mbar!r0!c0!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 08.01: Verify Tooltip') 
        expected_xaxis_label=['EMEA', 'North America', 'Oceania', 'South America']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 08.02')
        expected_zaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production','Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production','Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production','Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production','Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production','Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_z_axis_label(expected_zaxis_label, msg='Step 08.03')
        parent_css='#MAINTABLE_wbody1_f rect'
        visual.verify_number_of_risers(parent_css, num, riser[2], msg='Step 08.04')
        riser_css="[class*='riser!s0!g0!mbar!r0!c0!']"
        color="cinnabar"
        visual.verify_chart_color_using_get_css_property(riser_css, color, msg='Step 08.05')
        expected_row_label_list=['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016']
        visual.verify_rows_label(expected_row_label_list, msg="Step 08.06")
        expected_legend_list=['Gross Profit', '0M', '5.9M', '11.8M', '17.6M', '23.5M']
        visual.verify_legends(expected_legend_list, msg='Step 08.07')
        title_ele = self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1_f text[class^='xaxis'][class$='title']")
        title = [x.text for x in title_ele]
        if title[6] == 'Store Business Region':
            status = True
        else:
            status = False
        utils.asequal(status, True, 'Step 08.08: Verify title')
        
        """
        Step 9: Add Sale,Year to Filter
        """
        core_metaobj.collapse_data_field_section('Filters and Variables')
        field_name='Sale,Year'
        visual.right_click_on_datetree_item(field_name, position, context_menu_path='Filter')
        parent_css="#avFilterOkBtn"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        btn='ok'
        visual.close_filter_dialog(btn)
        
        """
        Step 10: verify query added to filter pane
        """
        parent_css="#qbFilterBox table>tbody>tr>td img"
        visual.wait_for_number_of_element(parent_css, position, time_out)
        field_name='Sale,Year'
        visual.verify_field_in_filterbox(field_name, position, "Step 10.01")
        
        """
        Step 11: Drill down on sale,quarter for any product category (2013:computers:EMEA)
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        riser_css="#MAINTABLE_wbody1_f .chartPanel rect[class*='riser']"
        visual.wait_for_number_of_element(riser_css, 139)
        time.sleep(sleep_time)
#         riser_css="riser!s2!g0!mbar!r2!c0!"
#         visual.select_tooltip("riser!s2!g0!mbar!r2!c0!", "Drill down to->Sale Quarter") its not working hence using below function
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s2!g0!mbar!r2!c0!", "Drill down to->Sale Quarter")
        
        """
        Step 12: Verify uneditable query added to filter pane
        """
        parent_css="#qbFilterBox table>tbody>tr>td img"
        visual.wait_for_number_of_element(parent_css, expected_num[1], time_out)
        field_name='TIME_YEAR and BUSINESS_REGION and PRODUCT_CATEGORY'
        visual.verify_field_in_filterbox(field_name, position2, "Step 12.01:")
        
        """
        Step 13: Verify filtered bar values 
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser[3], time_out)
        x_axis_title=['Product Category','Product Category','Product Category','Product Category','Store Business Region']
        visual.verify_x_axis_title(x_axis_title, msg='Step 13.01')
        expected_xaxis_label=['EMEA']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 13.02')
        expected_zaxis_label=['Computers', 'Computers', 'Computers', 'Computers']
        visual.verify_z_axis_label(expected_zaxis_label, msg='Step 13.03')
        parent_css='#MAINTABLE_wbody1_f rect'
        visual.verify_number_of_risers(parent_css, num, riser[3], msg='Step 13.04')
        riser_css="[class*='riser!s0!g0!mbar!r1!c0!']"
        color="persian_red"
        visual.verify_chart_color_using_get_css_property(riser_css, color, msg='Step 13.05')
        expected_row_label_list=['Sale Quarter', '1', '2', '3', '4']
        visual.verify_rows_label(expected_row_label_list, msg="Step 13.06:")
        expected_legend_list=['Gross Profit', '192.6K', '233.2K', '273.8K', '314.4K', '355K']
                
        """
        Step 14: Delete this filter from the filter bucket using the Delete key on the keyboard.
        """
        field_name='TIME_YEAR and BUSINESS_REGION and PRODUCT_CATEGORY'
        visual.select_field_in_filterbox(field_name, position)
        pyautogui.press('delete')
        
        """
        Step 15: Hover on 1st quarter Stereo Systems and verify tooltip.
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser[4], time_out)
        expected_tooltip_list=['Sale Quarter:1', 'Gross Profit:$8,290,320.67', 'Product Category:Stereo Systems', 'Store Business Region:EMEA', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        riser_css="riser!s4!g0!mbar!r0!c0!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 15.01: Verify Tooltip') 
        
        x_axis_title=['Product Category','Product Category','Product Category','Product Category','Store Business Region']
        visual.verify_x_axis_title(x_axis_title, msg='Step 15.02')
        expected_xaxis_label=['EMEA', 'North America', 'Oceania', 'South America']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 15.03')
        expected_zaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production','Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production','Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production','Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_z_axis_label(expected_zaxis_label, msg='Step 15.04')
        parent_css='#MAINTABLE_wbody1_f rect'
        visual.verify_number_of_risers(parent_css, num, riser[4], msg='Step 15.05')
        riser_css="[class*='riser!s0!g3!mbar!r0!c0!']"
        color="punch"
        visual.verify_chart_color_using_get_css_property(riser_css, color, msg='Step 15.06')
        expected_row_label_list=['Sale Quarter', '1', '2', '3', '4']
        visual.verify_rows_label(expected_row_label_list, msg="Step 15.07")
        expected_legend_list=['Gross Profit', '0M', '3.6M', '7.1M', '10.7M', '14.2M']
        visual.verify_legends(expected_legend_list, msg='Step 15.08')
        
        """
        Step 16: Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Step 17: Hover over on 2nd Quarter:Media player:North America tooltip.
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser[4], time_out)
        expected_tooltip_list=['Sale Quarter:2', 'Gross Profit:$7,204,536.60', 'Product Category:Media Player', 'Store Business Region:North America', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        riser_css="riser!s3!g1!mbar!r1!c0!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 17.01: Verify Tooltip') 
        
        x_axis_title=['Product Category','Product Category','Product Category','Product Category','Store Business Region']
        visual.verify_x_axis_title(x_axis_title, msg='Step 17.02')
        expected_xaxis_label=['EMEA', 'North America', 'Oceania', 'South America']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 17.03')
        expected_zaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production','Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production','Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production','Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_z_axis_label(expected_zaxis_label, msg='Step 17.04')
        parent_css='#MAINTABLE_wbody1_f rect'
        visual.verify_number_of_risers(parent_css, num, riser[4], msg='Step 17.05')
        riser_css="[class*='riser!s0!g3!mbar!r0!c0!']"
        color="punch"
        visual.verify_chart_color_using_get_css_property(riser_css, color, msg='Step 17.06')
        expected_row_label_list=['Sale Quarter', '1', '2', '3', '4']
        visual.verify_rows_label(expected_row_label_list, msg="Step 17.07:")
        expected_legend_list=['Gross Profit', '0M', '3.6M', '7.1M', '10.7M', '14.2M']
        visual.verify_legends(expected_legend_list, msg='Step 17.08')
        
        """
        Step 18: Close the output window
        """
        visual.switch_to_previous_window()
        
        """
        Step 19: Click "Save" in the toolbar > Type C2141219 > Click "Save" in the Save As dialog
        """
        parent_css="#applicationButton img"
        visual.wait_for_number_of_element(parent_css, position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, riser[4])
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 20: Logout of the IA API using the following URL: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()