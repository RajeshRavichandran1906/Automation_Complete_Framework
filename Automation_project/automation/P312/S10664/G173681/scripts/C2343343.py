'''
Created on Feb 5, 2018
@author: KS13172

TestSuite : 8202 New Features and product changes for existing functionality
TestCase ID :http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2343343
TestCase Name :Filter option when horizontal axis is a bin field
'''
import unittest
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata
from common.lib import utillity

class C2343343_TestClass(BaseTestCase):

    def test_C2343343(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID='C2343343'
        utillobj = utillity.UtillityMethods(self.driver)
        visual=visualization.Visualization(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,total_risers,tooltip, step_num):
            visual.verify_x_axis_title(x_title, msg='Step' + step_num + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step' + step_num + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step' + step_num + '.5:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class*='"+riser+"']", 'lochmara',  msg='Step' + step_num + '.6:'+' Verify riser color')
            visual.verify_tooltip(riser,tooltip,msg='Step' + step_num + '.7:'+' Verify riser tooltip')
                
        """
        Step 01:Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10666&tool=idis&master=baseapp/wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite') 
           
        """ 
        Step02: Right click on "Price,Dollars" > Create bins..
        Step03: Set Width of bins= 100 and Format = D20 > Click OK
        """
        metaobj.datatree_field_click("Price,Dollars",1,1,"Create Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, metaobj.home_page_long_timesleep)
        metaobj.create_bin("PRICE_DOLLARS_BIN_1", btn_click = 'OK', bin_width = '100', bin_format_edit = 'D20')
        utillobj.synchronize_with_visble_text("[id^='QbMetaDataTree']", 'Price,Dollars', metaobj.home_page_long_timesleep)
        
        """ 
        Step 04:Double click "Revenue", "PRICE_DOLLARS_BIN_1" to add fields
        """
        visual.double_click_on_datetree_item('Revenue', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "Revenue", 60)
        visual.double_click_on_datetree_item('Dimensions->PRICE_DOLLARS_BIN_1', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "PRICE_DOLLARS_BIN_1", 60)
                 
        """ 
        Step 05:Right click "Revenue" > More > Aggregations > Count
        """
        visual.right_click_on_field_under_query_tree("Revenue", 1, 'More->Aggregation Functions->Count')
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'CNT.Revenue', metaobj.home_page_long_timesleep)
        visual.verify_field_listed_under_querytree('Vertical Axis', 'CNT.Revenue', 1, "Step05: Verify querytree Vertical Axis")
           
        """ 
        Step 06:Verify following preview displayed
        """
        expected_xaxis_labels=['0','100','200','300','400']
        expected_yaxis_labels=['0','200K','400K','600K','800K','1,000K']
        riser="riser!s0!g0!mbar"
        tooltip=['PRICE_DOLLARS_BIN_1:0', 'CNT Revenue:201625', 'Filter Chart', 'Exclude from Chart']
        verify_bar_chart(['PRICE_DOLLARS_BIN_1'],['CNT Revenue'],expected_xaxis_labels,expected_yaxis_labels,riser,18,tooltip, '06')
                
        """ 
        Step07: Lasso a few risers (First 4 riser) > Filter chart
        """
        src_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class*='riser!s0!g0!mbar']")
        tgt_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class*='riser!s0!g3!mbar']")
        visual.create_lasso(src_elem, tgt_elem,source_element_location='middle_left')
        visual.select_lasso_tooltip("Filter Chart")
        
        """ 
        Step08: Verify filter added in filter pane and preview updated
        """       
        visual.wait_for_number_of_element("#qbFilterBox table>tbody>tr", 2, 60)
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 4, 300)
        
        visual.verify_field_in_filterbox('PRICE_DOLLARS_BIN_1', 1, "Step08: Verify filter added in filter pane")
        expected_xaxis_labels=['0','100','200','300']
        expected_yaxis_labels=['0','200K','400K','600K','800K','1,000K']
        riser="riser!s0!g0!mbar"
        tooltip=['PRICE_DOLLARS_BIN_1:0', 'CNT Revenue:201625', 'Filter Chart', 'Exclude from Chart']
        verify_bar_chart(['PRICE_DOLLARS_BIN_1'],['CNT Revenue'],expected_xaxis_labels,expected_yaxis_labels,riser,4,tooltip, '08')
        
        """ 
        Step09: Click Run
        Step10: Verify filtered output result in run time and tool tip values
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 4, 300)
        expected_xaxis_labels=['0','100','200','300']
        expected_yaxis_labels=['0', '200K','400K','600K','800K','1,000K']
        riser="riser!s0!g0!mbar"        
        tooltip=['PRICE_DOLLARS_BIN_1:0', 'CNT Revenue:201625', 'Filter Chart', 'Exclude from Chart']
        verify_bar_chart(['PRICE_DOLLARS_BIN_1'],['CNT Revenue'], expected_xaxis_labels, expected_yaxis_labels,riser, 4,tooltip, '10')
        visual.switch_to_previous_window()
        
        """ 
        Step 11:Click Save in the toolbar > Save as "C2343343" > Click Save
        """
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f rect[class^='riser']", 4, 240)
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """ 
        Step 12:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()