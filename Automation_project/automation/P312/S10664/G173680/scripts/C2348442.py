'''
Created on Jan22, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664_binning_2
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348442
TestCase Name = Treated as SUM if bin field added to Vertical axis bucket

'''
import unittest,time
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.pages.ia_resultarea import IA_Resultarea

class C2348442_TestClass(BaseTestCase):

    def test_C2348442(self):
        
        """
            CLASS OBJECTS
        """
        ia_rsultobj= IA_Resultarea(self.driver)
        visual=visualization.Visualization(self.driver)
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2348442'
        
        """
        Step01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 12, 50) 
           
        """
        Step02: Double click "Quantity, Sold" and "Product, Category"
        """
        visual.double_click_on_datetree_item('Quantity,Sold', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "Quantity Sold", 60)
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "ProductCategory", 60)
          
        """
        Step03: Verify following chart preview displayed
        """
        def verify_bar_chart(x_title,x_label, y_label,riser,total_risers,tooltip, step_num):
            visual.verify_x_axis_title(x_title, msg='Step' + step_num + '.2:'+' Verify x-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step' + step_num + '.5:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", 'lochmara',  msg='Step' + step_num + '.6:'+' Verify riser color')
            visual.verify_tooltip(riser,tooltip,msg='Step' + step_num + '.7:'+' Verify riser tooltip')
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        riser="riser!s0!g0!mbar"
        tooltip=['Product Category:Accessories', 'Quantity Sold:511,667', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_y_axis_title(['Quantity Sold'], msg='Step03.1: Verify y-axis title')
        verify_bar_chart(['Product Category'],expected_xaxis_labels,expected_yaxis_labels,riser, 7,tooltip, '03')
           
        """
        Step04: Right click on "Quantity, Sold" from data pane > Create Bins...
        Step05: Set Width of bins = 1
        Step06: Click OK
        """
        visual.right_click_on_datetree_item("Quantity,Sold",1,'Create Bins...')
        visual.create_bins("QUANTITY_SOLD_BIN_1", bin_width='1', btn_click='OK')
        visual.wait_for_number_of_element("#IaToolbar", 1, 30)       
          
        """
        Step07: Change chart type to Bar chart
        """
        visual.change_chart_type('bar') 
        riser_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(riser_css, 7, 30)
           
        """
        Step08: Add bin "QUANTITY_SOLD_BIN_1" to Vertical axis
        Bin added to Vertical axis with CNT. prefix prepended
        """
        visual.right_click_on_datetree_item('Dimensions->QUANTITY_SOLD_BIN_1',1,'Add To Query->Vertical Axis')
#         visual.drag_field_from_data_tree_to_query_pane("QUANTITY_SOLD_BIN_1",0,'Quantity,Sold')
        riser_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(riser_css, 14, 30)
        visual.verify_field_listed_under_querytree('Vertical Axis', 'CNT.QUANTITY_SOLD_BIN_1', 2, "Step08.1: Verify datatree field context menu")
         
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        riser="riser!s1!g0!mbar"
        tooltip=['Product Category:Accessories', 'CNT QUANTITY_SOLD_BIN_1:362992', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        verify_bar_chart(['Product Category'],expected_xaxis_labels,expected_yaxis_labels,riser, 14,tooltip, '08')
        
        """
        Step09: Click on view source icon from tool bar
        Step10: Verify fex code "CNT.QUANTITY_SOLD_BIN_1" added in SUM and Y axis bucket
        Step11: Close view source code window
        """
#         visual.verify_fexcode_syntax(['CNT.QUANTITY_SOLD_BIN_1','TYPE=DATA, COLUMN=N3, BUCKET=y-axis, $'], "Step10: Verify fex code CNT.QUANTITY_SOLD_BIN_1 added in SUM and Y axis bucket")
        ia_rsultobj.verify_fexcode_syntax(['CNT.QUANTITY_SOLD_BIN_1','TYPE=DATA, COLUMN=N3, BUCKET=y-axis, $'], "Step10: Verify fex code CNT.QUANTITY_SOLD_BIN_1 added in SUM and Y axis bucket")
         
        """
        Step12: Right click on "Quantity, Sold" > More > Aggregation Functions > Count
        """
        query_tree="#queryTreeColumn td[class='']"
        visual.wait_for_number_of_element(query_tree, 14, 10)
        visual.right_click_on_field_under_query_tree("Quantity,Sold", 1, 'More->Aggregation Functions->Count')
         
        """
        Bars for Quantity,Sold and for QUANTITY_SOLD_BIN_1 are of same height.
        Step13: Hover on the run time chart and verify tool tip values
        """
        riser_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(riser_css, 14, 30)
        visual.verify_legends(['CNT Quantity Sold','CNT QUANTITY_SOLD_BIN_1'],msg="Step13: Verify yaxis legends")
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '200K','400K','600K','800K','1,000K']
        riser="riser!s1!g0!mbar"
        tooltip=['Product Category:Accessories', 'CNT QUANTITY_SOLD_BIN_1:362992', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        verify_bar_chart(['Product Category'], expected_xaxis_labels,expected_yaxis_labels,riser, 14,tooltip,'13')
         
        """
        Step14: Click Run
        Step15: Verify
        Step16: Close run window
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.verify_legends(['CNT Quantity Sold','CNT QUANTITY_SOLD_BIN_1'],msg="Step15: Verify yaxis legends")
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '200K','400K','600K','800K','1,000K']
        riser="riser!s1!g0!mbar"        
        tooltip=['Product Category:Accessories', 'CNT QUANTITY_SOLD_BIN_1:362992', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        verify_bar_chart(['Product Category'], expected_xaxis_labels, expected_yaxis_labels,riser, 14,tooltip, '15')
        visual.take_run_window_snapshot(Test_Case_ID, '15')
        visual.switch_to_previous_window()
            
        """
        Step17: Click Save in the toolbar > Save as "C2348442" > Click Save
        """
        visual.wait_for_number_of_element(riser_css, 14, 30)
        tooltip=['PRODUCT_CATEGORY_1:Camcorder and Media Player', 'Revenue:$400,538,761.60', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.save_as_visualization_from_menubar(Test_Case_ID)
           
        """
        Step18: Logout using API
        """
        visual.logout_visualization_using_api()
        time.sleep(1)
          
        """
        Step19: Restore saved fex using API
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348443.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        visual.wait_for_number_of_element(riser_css, 14, 30)        
        visual.verify_legends(['CNT Quantity Sold','CNT QUANTITY_SOLD_BIN_1'],msg="Step19.1: Verify yaxis legends")
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '200K','400K','600K','800K','1,000K']
        riser="riser!s1!g0!mbar"
        tooltip=['Product Category:Accessories', 'CNT QUANTITY_SOLD_BIN_1:362992', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        verify_bar_chart(['Product Category'],expected_xaxis_labels,expected_yaxis_labels,riser, 14,tooltip, '19')  
        
        """
        Step20: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        
if __name__ == "__main__":
    unittest.main()