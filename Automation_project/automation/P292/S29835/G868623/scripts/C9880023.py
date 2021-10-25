'''
Created on Aug 16, 2019

@author: Prabhakaran
Testcase Name : Tick shape for markers in Scatter/Bubble chart
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261910
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.pages.wf_mainpage import Wf_Mainpage
from common.lib import core_utility
from common.wftools.text_editor import wf_texteditor
from common.pages.designer_metadata import Designer_Metadata
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login

class C9880023_TestClass(BaseTestCase):
    
    def test_C9880023(self):
        """
        Testcase case objects and variables
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        main_obj = Wf_Mainpage(self.driver)
        core_obj = core_utility.CoreUtillityMethods(self.driver)
        texteditor_obj = wf_texteditor(self.driver)
        desingn_metaobj = Designer_Metadata(self.driver)
        utils = UtillityMethods(self.driver)
        login_home = Login(self.driver)
        
        
        """
        Step 1: Launch the API to create new Designer Chart with the Car file
        http://machine:port/{alias}/designer?&item=IBFS:/WFC/Repository/P292_S29835/G730863&master=ibisamp/car&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api("ibisamp/car")
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        
        """
        Step 2 : Select "Scatter/Bubble" Chart from Chart picker component.
        """
        designer_chart_obj.select_chart_from_chart_picker('scatter_bubble')
        
        """
        Step 3: Double click COUNTRY, DEALER_COST.
        """
        designer_chart_obj.double_click_on_dimension_field('COUNTRY')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "COUNTRY", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('COMP->CARREC->BODY->DEALER_COST')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "DEALER_COST", designer_chart_obj.chart_medium_timesleep)
        
        """
        Step 4: Drag and drop "MODEL" into Horizontal bucket.
        """
        expand_obj = utils.validate_and_get_webdriver_object('.wfc-mdfp-dimension-tree div[title*="COMP"]', 'expand-obj')
        desingn_metaobj.field_expand(expand_obj)
        expand_obj = utils.validate_and_get_webdriver_object('.wfc-mdfp-dimension-tree div[title*="CARREC"]', 'expand-obj')
        desingn_metaobj.field_expand(expand_obj)
        designer_chart_obj.drag_and_drop_click_on_dimension_field_to_bucket_container('MODEL', 'Horizontal')
        
        """
        Step 4.00 : Fields added to the query pane and Canvas updated.
        """
        designer_chart_obj.verify_values_in_querybucket('Vertical', ['DEALER_COST'], "Step 4.01 : Verify vertical bucket")
        designer_chart_obj.verify_values_in_querybucket('Horizontal', ['MODEL'], "Step 4.02 : Verify horizontal bucket")
        designer_chart_obj.verify_values_in_querybucket('Detail', ['COUNTRY'], "Step 4.03 : Verify detail bucket")
        
        designer_chart_obj.verify_x_axis_title_in_preview(['MODEL'])
        designer_chart_obj.verify_y_axis_title_in_preview(['DEALER_COST'])
        expectedlist = ['100 LS 2 DOOR AUTO', '2000 4 DOOR BERLINA', '2000 GT VELOCE', '2000 SPIDER VELOCE', '2002 2 DOOR', '2002 2 DOOR AUTO', '3.0 SI 4 DOOR', '3.0 SI 4 DOOR AUTO', '504 4 DOOR', '530I 4 DOOR', '530I 4 DOOR AUTO', 'B210 2 DOOR AUTO', 'COROLLA 4 DOOR DIX AUTO', 'DORA 2 DOOR', 'INTERCEPTOR III', 'TR7', 'V12XKE AUTO', 'XJ12L AUTO']
        designer_chart_obj.verify_x_axis_label_in_preview(expectedlist)
        expectedlist1 = ['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        designer_chart_obj.verify_y_axis_label_in_preview(expectedlist1)
        designer_chart_obj.verify_number_of_risers('.markers circle', 1, 18)
        
        """
        Step 5: Select Format tab(fa-fa-brush) icon.
        Step 6: Click General drop down > Select "Series" option
        """
        designer_chart_obj.select_query_or_format_tab()
        designer_chart_obj.select_format_access_option('Series')
        
        """
        Step 7 : Click on Circle dropdown under Shape option > Select "Tick".
        """
        desingn_metaobj.change_marker_option('Tick')
        
        """
        Step 7.00 : Chart updated in Canvas with selected Tick option under Shape dropdown.
        """
        marker_dropdown_elem = utils.validate_and_get_webdriver_object('div[data-ibx-name="seriesShapeMarker"] input',"marker_dropdown_series")
        marker_dropdown_name  = utils.get_element_attribute(marker_dropdown_elem, 'aria-label')
        utils.asequal(marker_dropdown_name, 'Tick', 'Verify marker dropdown option')
                
        """
        Step 8 : Click Preview icon from toolbar.
        """
        designer_chart_obj.click_toolbar_item('preview')
        core_obj.switch_to_frame(frame_css='.ides-tool-preview-frame  .ibx-iframe-frame')
        
        """
        Step 8.00 : Chart displayed in preview mode with selected Shape option.
        """
        designer_chart_obj.verify_x_axis_title_in_preview(['MODEL'], parent_css = '#jschart_HOLD_0')
        designer_chart_obj.verify_y_axis_title_in_preview(['DEALER_COST'], parent_css = '#jschart_HOLD_0')
        expectedlist = ['100 LS 2 DOOR AUTO', '2000 4 DOOR BERLINA', '2000 GT VELOCE', '2000 SPIDER VELOCE', '2002 2 DOOR', '2002 2 DOOR AUTO', '3.0 SI 4 DOOR', '3.0 SI 4 DOOR AUTO', '504 4 DOOR', '530I 4 DOOR', '530I 4 DOOR AUTO', 'B210 2 DOOR AUTO', 'COROLLA 4 DOOR DIX AUTO', 'DORA 2 DOOR', 'INTERCEPTOR III', 'TR7', 'V12XKE AUTO', 'XJ12L AUTO']
        designer_chart_obj.verify_x_axis_label_in_preview(expectedlist, parent_css = '#jschart_HOLD_0')
        expectedlist1 = ['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        designer_chart_obj.verify_y_axis_label_in_preview(expectedlist1,parent_css = '#jschart_HOLD_0')
        designer_chart_obj.verify_number_of_risers('#jschart_HOLD_0 .markers path', 1, 18)
        core_obj.switch_to_default_content()
        
        """
        Step 9 : Hover blue icon from center of the chart > click Return button.
        """
        designer_chart_obj.go_back_to_design_from_preview()
        
        """
        Step 10:Click Save icon from Toolbar.
        Step 11:Enter Title as "C9880023" > Click Save.
        """
        designer_chart_obj.save_designer_chart_from_toolbar('C9880023')
 
        """
        Step 12:Launch the IA API to logout.
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
       
        """
        Step 13 : Open C9880023.fex in text editor.
        """
        login_home.invoke_home_page('mrid','mrpass')
        main_obj.select_repository_folder_item_context_menu('C9880023', 'Edit with text editor',folder_path = 'P292_S29835->G730863' )
        core_obj.switch_to_new_window()
        
        """
        Step 13.00 : The following syntax ("shape": "rectangleThin") is generated for Tick option in Text editor.
        """
        texteditor_obj.verify_line_in_texteditor(['"shape": "rectangleThin"'], step_num = "13.00",comparison_type="asin")
        
        """
        Step 14 : Close the Text editor.
        """
        core_obj.switch_to_previous_window()
        
        """
        Step 15 : Restore the C9880023.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
                  http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%2Fc8261910.fex
        """
        designer_chart_obj.api_logout()
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api(fex = 'c9880023')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "COUNTRY", designer_chart_obj.chart_long_timesleep)
        
        """
        Step 15.00 : Chart restored successfully.
        """
        designer_chart_obj.verify_x_axis_title_in_preview(['MODEL'])
        designer_chart_obj.verify_y_axis_title_in_preview(['DEALER_COST'])
        expectedlist = ['100 LS 2 DOOR AUTO', '2000 4 DOOR BERLINA', '2000 GT VELOCE', '2000 SPIDER VELOCE', '2002 2 DOOR', '2002 2 DOOR AUTO', '3.0 SI 4 DOOR', '3.0 SI 4 DOOR AUTO', '504 4 DOOR', '530I 4 DOOR', '530I 4 DOOR AUTO', 'B210 2 DOOR AUTO', 'COROLLA 4 DOOR DIX AUTO', 'DORA 2 DOOR', 'INTERCEPTOR III', 'TR7', 'V12XKE AUTO', 'XJ12L AUTO']
        designer_chart_obj.verify_x_axis_label_in_preview(expectedlist)
        expectedlist1 = ['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        designer_chart_obj.verify_y_axis_label_in_preview(expectedlist1)
        designer_chart_obj.verify_number_of_risers("[id*='chartpreview'] .markers path[class^='riser']", 1, 18)
        
        """
        Step 16 : Launch the IA API to logout.
                  http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()