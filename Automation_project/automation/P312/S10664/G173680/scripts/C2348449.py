'''
Created on Jan 8, 2018

@author: KS13172
TestSuite : 8202 New Features and product changes for existing functionality
TestCase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348449
TestCase Name: bin is added to header the value
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.pages.core_metadata import CoreMetaData
from common.pages import visualization_ribbon,ia_styling

class C2348449_TestClass(BaseTestCase):

    def test_C2348449(self):
        Test_Case_ID = "C2348449"
        visual = visualization.Visualization(self.driver)
        ia_styobj = ia_styling.IA_Style(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = CoreMetaData(self.driver)
        """
        Step 01:Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://machine:port/alias/ia?tool=idis&master=baseapp/WF_RETAIL&item=IBFS%3A%2FWFC%2FRepository%2FS10664
        """
        visual.invoke_visualization_using_api('new_retail/wf_retail_lite') 
             
        """ 
        Step02: Double click "Model", "Quantity,Sold"
        """
        visual.double_click_on_datetree_item('Model', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "Model", 45)
        visual.double_click_on_datetree_item('Quantity,Sold', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "QuantitySold", 45)
        metadataobj.collapse_data_field_section('Sales')
        time.sleep(5)             
        """
        Step03: Create Bin for "Price,Dollars" with bin width 100
        Step 04: Click OK
        """
        visual.right_click_on_datetree_item("Price,Dollars",1,'Create Bins...')
        visual.create_bins("PRICE_DOLLARS_BIN_1", bin_width='100', btn_click='OK')
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 157,30)
         
        """
        Step 05: Drag 'PRICE_DOLLARS_BIN_1' bin to Horizontal under "Product,Category"
        """ 
            
        visual.drag_field_from_data_tree_to_query_pane('Dimensions->PRICE_DOLLARS_BIN_1',1,"Model",1)  
            
        parent_css= "#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 157,30)
        visual.verify_field_listed_under_querytree('Horizontal Axis',"PRICE_DOLLARS_BIN_1",2,"Step 05: Verify PRICE_DOLLARS_BIN_1 added to Horizontal Axis bucket")   
        metadataobj.collapse_data_field_section('Attributes->Model->Product')
        time.sleep(5) 
        """
        Step06: Select Home > Header & Footer
        """
        ribbonobj.select_ribbon_item('Format', 'header_footer_img')
          
        """
        Step07: Add text "<PRICE_DOLLARS_BIN_1" , Text Bold, Center alignment, font color Red, background color yellow.
        Step08: Click 'OK'
        """
        visual.wait_for_number_of_element("#pgHding", 1, 10)
        ia_styobj.create_header_footer('frame','Page Header', '<PRICE_DOLLARS_BIN_1',bold=True,center_justify=True,text_color='red',background_color='yellow', btn_apply='btn_apply', btn_ok='btn_ok')
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 157,30) 
        verify_style={'font_color':'red','bold':True, 'text_value':'100.00','text_align':'634','bg_color':'yellow'}
        visual.verify_header_footer_property('MAINTABLE_1', 1, verify_style, "07")

        """
        Step09: Verify the following preview with query and data pane
        """
        
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 157,30)
        visual.verify_field_listed_under_querytree('Model',"PRICE_DOLLARS_BIN_1",1,"Step 09.1: Verify PRICE_DOLLARS_BIN_1 added to Model bucket")
        visual.verify_field_listed_under_datatree('Dimensions',"PRICE_DOLLARS_BIN_1",6,"Step 09.2: Verify data pane")

        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 157, msg='Step 09.03: Verify the total number of risers displayed on livepreview Chart')
        visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", 'bar_blue',  msg='Step09.04: Verify first bar color')
        expected_tooltip_list=['Model:2100', 'PRICE_DOLLARS_BIN_1:100.00', 'Quantity Sold:42,241', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory']
        visual.verify_tooltip("riser!s0!g0!mbar",expected_tooltip_list,msg='Step09.05: Verify first riser to verify tooltip values')
              
        """
        Step10: Click Run
        Step11: Verify the following chart with header displayed
        Step12: Dismiss run window
        """  
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()        
        parent_css="#MAINTABLE_wbody1 [class^='riser!']"        
        visual.wait_for_number_of_element(parent_css, 157,30)

        verify_style={'font_color':'red','bold':True, 'text_value':'100.00','bg_color':'yellow','text_allign':'754'}
        visual.verify_header_footer_property('MAINTABLE_1', 1, verify_style, "11.1")
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 157, msg='Step11.2: Verify the total number of risers displayed on run')
        visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", 'bar_blue',  msg='Step11.3: Verify first bar color')
        expected_tooltip_list=['Model:2100', 'PRICE_DOLLARS_BIN_1:100.00', 'Quantity Sold:42,241', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory']
        visual.verify_tooltip('riser!s0!g0!mbar',expected_tooltip_list,msg='Step11.4: Verify first riser to verify tooltip values')
        
        visual.take_run_window_snapshot(Test_Case_ID, '12')
        visual.switch_to_previous_window()
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 [class^='riser!']", 157,30)  
                
        """
        Step13: Logout using API (without saving)
        """
#         utillobj.infoassist_api_logout()



if __name__ == "__main__":
    unittest.main()