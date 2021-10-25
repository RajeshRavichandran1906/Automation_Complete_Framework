'''
Created on Feb 08, 2018

@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349031
Test_Case Name :Paperclipping in Treemap

'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization
class C2349031_TestClass(BaseTestCase):

    def test_C2349031(self):
        
        """   
            TESTCASE VARIABLES 
        """
        
        Test_Case_ID='C2349031'
        visual=Visualization(self.driver)
        driver = self.driver #Driver reference object created
        
        """
            Step 01 :Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 12, 50)
        
        """
            Step 02:Click Change drop down > Treemap chart
        """
        
        visual.change_chart_type('treemap')
        visual.wait_for_visible_text("#TableChart_1 svg g text.title", 'DropMeasuresorSortsintotheQueryPane',20)
        
        """
            Step 03:Double click "Store,Country" to add Grouping bucket and "Gross Profit" to Size bucket
        """
        visual.double_click_on_datetree_item('Store,Country', 1)
        visual.double_click_on_datetree_item('Gross Profit', 1)

        """
            Step 04:Drag and drop "Store, Business,Sub Region" to color bucket
        """
        visual.drag_field_from_data_tree_to_query_pane('Store,Business,Sub Region', 1, 'Color')
        
        """
            Step 05:Double click "Store Front (from query variables)"            
        """ 
               
        visual.double_click_on_datetree_item('Query Variables->Store Front', 1)
        
        """
            Step 06:Verify following preview displayed            
        """
        time.sleep(5)
        element_css="#MAINTABLE_wbody1_f text[text-anchor='middle']"
        visual.wait_for_number_of_element(element_css, 47, 25)
        visual.verify_legends(['Africa', 'Asia', 'Australia-New Zealand', 'Canada', 'East', 'Europe', 'Mexico', 'Midwest', 'Northeast', 'SA-Port', 'SA-Span', 'South', 'Southeast', 'West'], msg='Step 6.1')
        visual.verify_x_axis_label(['Europe', 'South', 'Midwest', 'Canada', 'East', 'West', 'Asia', 'SA-Port', 'Mexico', 'Southeast'], xyz_axis_label_css="text[text-anchor='middle']", msg='step 6.3 : verify random X labels ')
        visual.verify_chart_color_using_get_css_property("[class='riser!sEurope-_-United Kingdom!g0!mnode']", 'orange', msg='Step 6.4a: Verify_random colors_Europe-United Kingdom')
        visual.verify_chart_color_using_get_css_property("[class='riser!sMidwest-_-United States!g0!mnode']", 'Feijoa', msg='Step 6.4b: Verify_random colors_Midwest-_-United States')
        visual.verify_chart_color_using_get_css_property("[class='riser!sCanada-_-Canada!g0!mnode']", 'pale_yellow', msg='Step 6.4c: Verify_random colors_Canada-_-Canada')
        visual.verify_chart_color_using_get_css_property("[class='riser!sEast-_-United States!g0!mnode']", 'brick_red', msg='Step 6.4d: Verify_random colors_East-_-United States')
        visual.verify_chart_color_using_get_css_property("[class='riser!sMexico-_-Mexico!g0!mnode']", 'Polo_Blue', msg='Step 6.4e: Verify_random colors_Mexico-_-Mexico')
        
        """
            Step 07:Multi select(Using CTRL KEY) "East, West, South, Midwest, Southeast"
            Step 08:Click "Group Store, Business,Sub Region selection"
        """ 
        Midwest=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!sMidwest-_-United States!g0!mnode']")
        east=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!sEast-_-United States!g0!mnode']")
        west=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!sWest-_-United States!g0!mnode']")           
        south=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!sSouth-_-United States!g0!mnode']")    
        Southeast=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!sSoutheast-_-United States!g0!mnode']")
        visual.multi_select_chart_component([east, west,Midwest,south,Southeast])
        time.sleep(2)
        visual.select_lasso_tooltip('Group Store,Business,Sub Region Selection')
        time.sleep(5)
        element_css="#MAINTABLE_wbody1_f text[text-anchor='middle']"
        visual.wait_for_number_of_element(element_css, 38, 25)
        """
            Step 09:Verify following preview displayed All of United States appears in tree map as one rectangle.       
        """
        
        visual.verify_legends(['Africa', 'Asia', 'Australia-New Zealand', 'Canada', 'East and West and Midwest and 2 more', 'Europe', 'Mexico', 'Northeast', 'SA-Port', 'SA-Span'], msg='Step 8.1')
        visual.verify_x_axis_label(['Europe', 'East and West and Midwest and 2 more', 'Canada', 'Asia', 'SA-Port', 'Mexico'], xyz_axis_label_css="text[text-anchor='middle']", msg='step 8.3: verify random X labels')
        visual.verify_chart_color_using_get_css_property("[class='riser!sEurope-_-Sweden!g0!mnode']", 'orange', msg='Step 9a: Verify_random colors_Europe-_-Sweden')
        visual.verify_chart_color_using_get_css_property("[class='riser!sEast and West and Midwest and 2 more-_-United States!g0!mnode']", 'brick_red', msg='Step 9b: Verify_random colors_East and West and Midwest and 2 more-_-United States')
        visual.verify_chart_color_using_get_css_property("[class='riser!sCanada-_-Canada!g0!mnode']", 'pale_yellow', msg='Step 9c: Verify_random colors_Canada-_-Canada')
        visual.verify_chart_color_using_get_css_property("[class='riser!sAsia-_-Singapore!g0!mnode']", 'bar_green', msg='Step 9d: Verify_random colors_Asia-_-Singapore')
 
 
        """
            Step 10:Hover on "United States" and verify tool tip values       
        """
        expected_tooltip=['BUSINESS_SUB_REGION_1:East and West and Midwest and 2 more', 'Store Country:United States', 'Gross Profit:$61,427,880.51', 'Filter Chart', 'Exclude from Chart', 'Drill up to', 'Drill down to']
        visual.verify_tooltip('riser!sEast and West and Midwest and 2 more-_-United States!g0!mnode', expected_tooltip, 'Step 10.1 : Verify tooltip values',element_location='top_middle',yoffset=30)
        
        """
            Step 11:Click Save in the toolbar > Save as "C2349031" > Click Save    
        """
        
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
            Step 12:Logout using API http://machine:port/alias/service/wf_security_logout.jsp    
        """
        
        visual.logout_visualization_using_api()
        
        """
            Step 13:Run fex from Resource tree using API
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10664&BIP_item=C2349031.fex
            Hover on United Kindom and tooltip values displayed as following        
        """
        visual.run_visualization_using_api("C2349031.fex")
        expected_tooltip=['BUSINESS_SUB_REGION_1:Europe', 'Store Country:United Kingdom', 'Gross Profit:$14,563,437.36', 'Filter Chart', 'Exclude from Chart', 'Drill up to', 'Drill down to']
        visual.verify_tooltip('riser!sEurope-_-United Kingdom!g0!mnode', expected_tooltip, 'Step 13.1 : Verify tooltip values',element_location='top_middle',yoffset=30)
       
        """
            Step 14:Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
            Step 15:Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349031.fex
        """        
        visual.edit_visualization_using_api(Test_Case_ID)
        
        """
            Step 16:Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
                
if __name__ == '__main__':
    unittest.main()        
        