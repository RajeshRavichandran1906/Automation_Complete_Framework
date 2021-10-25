'''
Created on Feb, 02 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349048
Test_Case Name : Cannot delete group from data pane while in use
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages.core_metadata import CoreMetaData
from common.wftools.visualization import Visualization

class C2349048_TestClass(BaseTestCase):

    def test_C2349048(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2349048'
        visual=Visualization(self.driver)
        metadataobj = CoreMetaData(self.driver)
        
        def verify_bar_chart(expected_xaxis_title, expected_xaxis_label, total_risers, step_num):
            expected_yaxis_label=['0', '40M', '80M', '120M', '160M', '200M']
            visual.verify_y_axis_title(['Gross Profit'], msg='Step ' + step_num + '.1')
            visual.verify_x_axis_title(expected_xaxis_title, msg='Step ' + step_num + '.2')
            visual.verify_x_axis_label(expected_xaxis_label, msg='Step ' + step_num + '.3')
            visual.verify_y_axis_label(expected_yaxis_label, msg='Step ' + step_num + '.4')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step ' + step_num + '.5')
            visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", 'lochmara',  msg='Step ' + step_num + '.6' )
            
        """
            Step 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        time.sleep(3)
         
        """
            Step 02 : Double click "Gross Profit", "Customer, Business, Region"
        """
        visual.double_click_on_datetree_item('Gross Profit', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "GrossProfit", 30)
        
        visual.double_click_on_datetree_item('Customer,Business,Region', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "CustomerBusinessRegion", 30)
        time.sleep(3)
        
        """
            Step 02.1 : Verify preview
        """
        expected_xaxis_label=['EMEA', 'North America', 'Oceania', 'South America']
        verify_bar_chart(['Customer Business Region'], expected_xaxis_label, 4, '02')
        
        """
            Step 03 : Multi select "EMEA and Oceania"
        """
        emea=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g0!mbar!']")
        oceania=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g2!mbar!']")
        visual.multi_select_chart_component([emea, oceania])
        visual.verify_lasso_tooltip(['2 points', 'Filter Chart', 'Exclude from Chart', 'Group Customer,Business,Region Selection'], 'Step 03.1 : Verify multiple select tooltip')
        
        """
            Step 04 : Select " Group Customer, Business, Region Selection"
        """
        visual.select_lasso_tooltip('Group Customer,Business,Region Selection')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "BUSINESS_REGION_1", 60)
        
        """
            Step 05 : Verify "BUSINESS_REGION_1" group created and preview updated
        """
        expected_xaxis_label=['EMEA and Oceania', 'North America', 'South America']
        verify_bar_chart(['BUSINESS_REGION_1'], expected_xaxis_label, 3, '05')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'BUSINESS_REGION_1', 1, 'Step 05.7')
        expected_tooltip=['BUSINESS_REGION_1:EMEA and Oceania', 'Gross Profit:$159,673,644.62', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer Business Region']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip, 'Step 05.8 : Verify tooltip value for first riser')
        
        """
            Step 06 : Right click on "BUSINESS_REGION_1" in data pane >
            Step 07 : Click Delete
        """
        metadataobj.collapse_data_field_section('Sales')
        time.sleep(5)
        visual.right_click_on_datetree_item('Dimensions->BUSINESS_REGION_1', 1, 'Delete')
        visual.wait_for_visible_text("[id^='BiDialog'][style*='inherit'] div[class*='bi-window-caption']", "Message", 25)
        
        """
            Step 08 : Verify Friendly error displays that the "Currently in use, Cannot be deleted"
        """
        visual.verify_popup_or_dialog_caption_text("[id^='BiDialog'] div[class^='bi-window-caption']", 'Message', 'Step 08.1')
        visual.verify_dialogs_and_popups_text("div[id^='BiOptionPane']>div[class='bi-label']", "Currently in use, cannot be deleted", 'Step 08.2 ')
        
        """
            Step 09  :Click OK
        """
        visual.click_any_bibutton_in_dialog()
        
        """
            Step 10 : Click Save in the toolbar > Save as "C2349048" > Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
            Step 11 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
            Step 12 : Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349048.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "BUSINESS_REGION_1", 60)
        visual.take_preview_snapshot(Test_Case_ID, '12')
        
        """
            Step 12.1 : Verify Restored successfully
        """
        expected_xaxis_label=['EMEA and Oceania', 'North America', 'South America']
        verify_bar_chart(['BUSINESS_REGION_1'], expected_xaxis_label, 3, '12')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'BUSINESS_REGION_1', 1, 'Step 12.7')
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip, 'Step 12.8 : Verify tooltip value for first riser')
        
        """
            Step 13 : Right click on "BUSINESS_REGION_1" in data pane > Delete
        """
        visual.right_click_on_datetree_item('Dimensions->BUSINESS_REGION_1', 1, 'Delete')
        visual.wait_for_visible_text("[id^='BiDialog'][style*='inherit'] div[class*='bi-window-caption']", "Message", 25)
        
        """
            Step 14 : Verify Friendly error displays that the "Currently in use, Cannot be deleted"
        """
        visual.verify_popup_or_dialog_caption_text("[id^='BiDialog'] div[class^='bi-window-caption']", 'Message', 'Step 08.1')
        visual.verify_dialogs_and_popups_text("div[id^='BiOptionPane']>div[class='bi-label']", "Currently in use, cannot be deleted", 'Step 14.1 ')
        
        """
            Step 15 : Click OK
        """
        visual.click_any_bibutton_in_dialog()
        
        """
            Step 16 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
if __name__ == '__main__':
    unittest.main()