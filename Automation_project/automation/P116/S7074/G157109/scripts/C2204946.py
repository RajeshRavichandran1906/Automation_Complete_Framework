'''
Created on Jan 9, 2019

@author: Magesh
TestCase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2204946
TestCase_Name : Verify Active chart engine is set to JSCHART
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.wftools.active_chart import Active_Chart
from common.wftools import wf_mainpage

class C2204946_TestClass(BaseTestCase):

    def test_C2204946(self):
        
        """
        TESTCASE VARIABLES
        """
        active_chart = Active_Chart(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        wfmain_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        
        """
        COMMON VARIABLES
        """
        MEDIUM_WAIT_TIME = 60
        SHORT_TIME = 10
        preview_parent_css="TableChart_1"
        run_parent_css="MAINTABLE_wbody0"
        fex_name="1Chart_Engine"
        
        """
        Step 01:Sign in to WebFOCUS
        http://machine:port/{alias}
        Step 02:Execute the following URL:
        http://machine:port/{alias}/ia?tool=chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FS10670
        Change the Output type to Active Report.
        """
        active_chart.invoke_ia_chart_tool_using_api('ibisamp/ggsales')
        active_chart.change_output_format_type('active_report')
        active_chart.wait_for_visible_text("#HomeFormatType", 'Active Report', SHORT_TIME)  
         
        """
        Expect to see the following Live Preview pane, with the default Vertical Column Bar Chart on the canvas
        """
        active_chart.verify_x_axis_label_in_preview(['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4'], msg='Step 02.01')
        active_chart.verify_y_axis_label_in_preview(['0', '10', '20', '30', '40', '50'], msg='Step 02.02')
        active_chart.verify_legends_in_preview(['Series 0', 'Series 1', 'Series 2', 'Series 3', 'Series 4'], msg='Step 02.03')
        active_chart.verify_number_of_risers_in_preview('rect', 1, 25, msg='Step 02.04: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='#'+preview_parent_css, msg='Step 02.05')
                
        """ 
        Step 03: Add Category and Product fields to Horizontal Axis 
        and add Unit Sales field to Vertical Axis
        """
        active_chart.double_click_on_datetree_item('Category', 1)
        active_chart.wait_for_visible_text("text[class='xaxisOrdinal-title']", 'Category', MEDIUM_WAIT_TIME)
         
        active_chart.double_click_on_datetree_item('Product', 1)
        active_chart.wait_for_visible_text("text[class='xaxisOrdinal-title']", 'Category : Product', MEDIUM_WAIT_TIME)
         
        active_chart.double_click_on_datetree_item('Unit Sales', 1)
        active_chart.wait_for_visible_text("text[class='yaxis-title']", 'Unit Sales', MEDIUM_WAIT_TIME)
         
        active_chart.verify_x_axis_label_in_preview(['Coffee : Capuccino', 'Coffee : Espresso'], msg='Step 03.01')
        active_chart.verify_y_axis_label_in_preview(['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K'], msg='Step 03.2')
        active_chart.verify_x_axis_title_in_preview(['Category : Product'], msg='Step 03.3')
        active_chart.verify_y_axis_title_in_preview(['Unit Sales'], msg='Step 03.4')
        active_chart.verify_number_of_risers_in_preview('rect', 1, 2, msg='Step 03.5: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='#'+preview_parent_css, msg='Step 03.6')
         
        """ 
        Step 04:Run the chart
        Verify the chart is displayed properly
        """ 
        active_chart.run_chart_from_toptoolbar()
        active_chart.switch_to_frame()
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f rect[class*='riser!']", 10, MEDIUM_WAIT_TIME)
         
        active_chart.verify_x_axis_title_in_run_window(['Category : Product'], msg='Step 04.1')
        active_chart.verify_y_axis_title_in_run_window(['Unit Sales'], msg='Step 04.2')
        active_chart.verify_x_axis_label_in_run_window(['Coffee : Capuccino', 'Coffee : Espresso', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croissant', 'Food : Scone'], msg='Step 04.3')
        active_chart.verify_y_axis_label_in_run_window(['0', '200K', '400K', '600K', '800K', '1,000K'], msg='Step 04.4')
        active_chart.verify_number_of_risers_in_run_window('rect', 1, 10, msg='Step 04.5: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='#'+run_parent_css, msg='Step 04.6')
        active_chart.verify_chart_title('Unit Sales BY Category, Product', msg='Step 04.7', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 04.8', parent_css='#MAINTABLE_wmenu0')
        active_chart.switch_to_default_content()
              
        """ 
        Step 05:Save the chart as Chart_Engine.fex
        """
        active_chart.save_as_chart_from_menubar(fex_name)
        time.sleep(3)
        active_chart.logout_chart_using_api()
             
        """ 
        Step 06:Now edit the saved fex from Text editor
        Verify from the source code whether below
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        time.sleep(10)
        wfmain_page_obj.right_click_folder_item_and_select_menu(fex_name, 'Edit with text editor', folder_path='P116->S7074')
        active_chart.switch_to_new_window()
        text_editor_css = "[class*='text-editor'] .ace_text-layer"
        utillobj.synchronize_with_number_of_element(text_editor_css, 1, 60)
        
        """ 
        Step 06.1: Verify from the source code whether below code is generated:
        ARGRAPHENGINE = JSCHART
        """
        text_editor_obj=utillobj.validate_and_get_webdriver_object(text_editor_css, "Text_editor source code")
        actual_value=text_editor_obj.text.strip()
        expected_value="ARGRAPHENGINE=JSCHART"
        utillobj.asin(expected_value, actual_value, "Step 06:Verify from the source code whether which has ARGRAPHENGINE=JSCHART in editor")
        active_chart.switch_to_previous_window()
        

if __name__ == "__main__":
    unittest.main()