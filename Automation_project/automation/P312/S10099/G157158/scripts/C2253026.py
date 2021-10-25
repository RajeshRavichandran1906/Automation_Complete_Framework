'''
Created on Feb 20, 2018

@author: Sowmiya
TestSuite ID : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2253026
TestCase Name: Drilldown on 2nd hierarchy dimension if integer shows wrong dimension in tooltip
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.pages.visualization_resultarea import Visualization_Resultarea as resultobject
from common.lib.utillity import UtillityMethods

class C2253026_TestClass(BaseTestCase):

    def test_C2253026(self):
        
        """
        CLASS OBJECTS
        """
        utils = UtillityMethods(self.driver)
        visual = visualization.Visualization(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2253026'
        position=1
        
        def verify_bar_chart(x_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, legend_list, total_risers, stepno):        
            
            visual.verify_x_axis_title(x_axis_title, msg='Step '+stepno+'.01')
            visual.verify_legends(legend_list, "#MAINTABLE_wbody1", msg='Step '+stepno+'.02')
            visual.verify_x_axis_label(x_axis_label, xyz_axis_label_length=10, msg='Step '+stepno+'.03')
            visual.verify_y_axis_label(y_axis_label, msg='Step '+stepno+'.04')
            visual.verify_number_of_risers("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 1, total_risers, msg='Step '+stepno+'.05')
            visual.verify_chart_color_using_get_css_property("rect[class='"+riser_css+"']", color_name, msg='Step '+stepno+'.06')
            visual.verify_tooltip(riser_css, tooltip_list, msg='Step '+stepno+'.07: Verify tool tip')
    
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """      
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02 : Double click Shipment Unit(s), 'Days,Delayed', 'Shipped,Year' and 'Shipped,Quarter'
        """
        field_name="Shipment Unit(s)"
        visual.double_click_on_datetree_item(field_name, position)
        element_css="#MAINTABLE_wbody1_f g text[class='yaxis-title']"
        visual.wait_for_visible_text(element_css, 'ShipmentUnit(s)')
         
        field_name="Days,Delayed"
        visual.double_click_on_datetree_item(field_name, position)
        element_css="#TableChart_1 rect[class^='riser']"
        visual.wait_for_number_of_element(element_css, expected_number=2)
         
        field_name="Shipped,Year"
        visual.double_click_on_datetree_item(field_name, position)
        element_css="#MAINTABLE_wbody1_f g text[class='xaxisOrdinal-title']"
        visual.wait_for_visible_text(element_css, 'ShippedYear')
         
        field_name="Shipped,Quarter"
        visual.double_click_on_datetree_item(field_name, position)
        element_css="#TableChart_1 rect[class^='riser']"
        visual.wait_for_number_of_element(element_css, expected_number=42)
         
        """
        Step 03 : Verify horizontal axis label
        """
        x_axis_title=['Shipped Year : Shipped Quarter']
        legend_list=['Shipment Unit(s)', 'Days Delayed']
        x_axis_label=['2012 : 1', '2012 : 2', '2012 : 3', '2012 : 4', '2013 : 1', '2013 : 2', '2013 : 3', '2013 : 4', '2014 : 1', '2014 : 2', '2014 : 3', '2014 : 4', '2015 : 1', '2015 : 2', '2015 : 3', '2015 : 4', '2016 : 1', '2016 : 2', '2016 : 3', '2016 : 4', '2017 : 1']
        y_axis_label=['0', '40K', '80K', '120K', '160K', '200K']
        color_name='bar_blue'
        tooltip_list=['Shipped Year:2013', 'Shipped Quarter:1', 'Shipment Unit(s):8,652', 'Filter Chart', 'Exclude from Chart', 'Drill up to Shipped Year', 'Drill down to']
        riser_css='riser!s0!g4!mbar!'
        verify_bar_chart(x_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, legend_list, 42, '03')
         
        """
        Step 04 : verify query pane
        """
        visual.verify_field_listed_under_querytree('Vertical Axis', 'Shipment Unit(s)', position, msg='Step 04.01')
        visual.verify_field_listed_under_querytree('Vertical Axis', 'Days,Delayed', position+position, msg='Step 04.02')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Shipped,Year', position, msg='Step 04.03')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Shipped,Quarter', position+position, msg='Step 04.04')
         
        """
        Step 05 : Verify 2016:3 shipments values in tooltip
        """
        tooltip_list=['Shipped Year:2016', 'Shipped Quarter:3', 'Shipment Unit(s):98,537', 'Filter Chart', 'Exclude from Chart', 'Drill up to Shipped Year', 'Drill down to']
        riser_css = 'riser!s0!g18!mbar!'
        tooltip_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g18!mbar!']")
        resultobject.move_mouse_to_chart_component(self, tooltip_elem,move_to_tooltip=True)
        tooltip_css="span[id*='tdgchart-tooltip']:not([style*='hidden'])"
        raw_tooltip_list=self.driver.find_element_by_css_selector(tooltip_css).text.replace(u'\xa0\n', '').replace(u'\xa0', ' ').split('\n')
#         raw_tooltip_list=utillityobject.validate_and_get_webdriver_object(self, tooltip_css, "tooltip", pause_time=0.1).text.replace(u'\xa0\n', '').replace(u'\xa0', ' ').split('\n')
        actual_list=utils.get_actual_tooltip_list(raw_tooltip_list)
        utils.asequal(tooltip_list, actual_list, 'Step 05.01: Verify tool tip')
        
        
        """
        Step 06 : Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element("#MAINTABLE_1 rect[class^='riser']", expected_number=42)
       
        """
        Step 07 : Hover over 2016:4 > Drill Down > "Shipped Month"
        """
        visual.select_tooltip('riser!s1!g19!mbar!', 'Drill down to->Shipped Month')
        visual.wait_for_number_of_element("#MAINTABLE_1 rect[class^='riser']", expected_number=6)
        
        """
        Step 07.00 : Verify horizontal label changed to Shipped Month
        """
        x_axis_title=['Shipped Year : Shipped Month']
        x_axis_label=['2016 : 10', '2016 : 11', '2016 : 12']
        visual.verify_x_axis_title(x_axis_title, msg='Step 07.01')
        visual.verify_x_axis_label(x_axis_label, msg='Step 07.02')
       
        """
        Step 08 : Hover on "2016:10" green color bar.
        Step 08.00 : Verify the tool tip:
        """
        tooltip_list = ['Shipped Year:2016', 'Shipped Month:10', 'Days Delayed:20,975', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Shipped Quarter', 'Drill down to']
        visual.verify_tooltip('riser!s1!g0!mbar!', tooltip_list, msg='Step 08.01 : Verify tool tip')
        visual.verify_chart_color_using_get_css_property("rect[class='riser!s1!g0!mbar!']", 'pale_green', msg='Step 08.02')
              
        """
        Step 09 : Close the output window
        """
        visual.switch_to_previous_window()
        visual.wait_for_number_of_element("#TableChart_1 rect[class^='riser']", expected_number=42)
        
        """
        Step 10 : Click "Save" in the toolbar > Type C2141379 > Click "Save" in the Save As dialog
                    Save the fex with the same name as this test caseear
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 11 : Logout of the IA API using the following URL.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main() 