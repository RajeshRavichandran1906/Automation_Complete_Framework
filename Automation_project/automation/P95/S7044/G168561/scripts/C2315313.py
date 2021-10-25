'''
Created on January 10, 2019

@author: KK14897

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2315313
TestCase Name = Verify Active Report Options General Tab
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility,utillity
from common.wftools import active_report
from common.wftools import report
from common.wftools import chart

class C2315313_TestClass(BaseTestCase):

    def test_C2315313(self):
        
        """
        Test case Object's
        """
        util_obj = utillity.UtillityMethods(self.driver)
        ar_obj=active_report.Active_Report(self.driver)
        report_obj=report.Report(self.driver)
        chart_obj=chart.Chart(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        '''
        Variables
        '''
        table_css="TableChart_1"
        file_name="C2315313_Ds_01.xlsx"
        window_list=["Cascade","Tabs"]
        freeze_list=["None","COUNTRY","CAR"]
        Pages_list=['All','10','20','30','40','50']
        Location_list=["Top Row","Bottom Row"]
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        Folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        
        def verify_active_report_options_dialog(self,exp_list,css,dropdown_name):
            dropdown_obj=util_obj.validate_and_get_webdriver_object(css, dropdown_name)
            util_obj.verify_combo_box_item(exp_list, combobox_dropdown_elem=dropdown_obj, msg="step 04")
            core_util_obj.left_click(dropdown_obj)
            
        def verify_datapane_toggle_button_tooltip(self,button_css, expected_tooltip):
            '''
            This function will hover on toggle button to verify it's tooltip value
            expected_tooltip
            '''
            button_elem=self.driver.find_element_by_css_selector(button_css)
            core_util_obj.python_move_to_element(button_elem, element_location='middle')
            time.sleep(2)
            tooltip_css="[id^='BiToolTip']:not([style*='hidden'])"
            toggle_tooltip_elem=util_obj.validate_and_get_webdriver_object(tooltip_css, 'Tooltip of IA metadata')
            actual_tooltip=toggle_tooltip_elem.text
            custom_msg='Step X : Verify datapane toggle button tooltip shown as ' + expected_tooltip + '.'
            util_obj.asequal(expected_tooltip, actual_tooltip, custom_msg)   
        '''       
        Step 01 : Launch IA Report using below API link
        http://machine:port/{alias}/ia?tool=Report&master=ibisamp/car&item=IBFS:/WFC/Repository/P95/S10142
        '''
        ar_obj.invoke_report_tool_using_api("ibisamp/car", mrid="mriddev", mrpass="mrpassdev", repository_path=Folder_path)
        
        '''
        Step 02 : Add fields 
        COUNTRY, CAR, DEALER_COST, RETAIL_COST.
        Select Format Active Report
        Expect to see the following report Preview pane.
        '''
        report_obj.double_click_on_datetree_item("COUNTRY", 1)
        report_obj.wait_for_number_of_element('#'+table_css+' [class*="x"]', 7, 20)
        report_obj.double_click_on_datetree_item("CAR", 1)
        report_obj.wait_for_number_of_element('#'+table_css+' [class*="x"]', 18, 20)
        report_obj.double_click_on_datetree_item("DEALER_COST", 1)
        report_obj.wait_for_number_of_element('#'+table_css+' [class*="x"]', 29, 20)
        report_obj.double_click_on_datetree_item("RETAIL_COST", 1)
        report_obj.wait_for_number_of_element('#'+table_css+' [class*="x"]', 40, 20)
        chart_obj.change_output_format_type("active_report")
        report_obj.verify_report_data_set_in_preview("TableChart_1", 10, 4, file_name,"Verify Preview")
        
        '''
        Step 03 : Click the Format tab, then select Active Report Options.
        Expect to see the following Active Reports menu.
        '''
        report_obj.select_ia_ribbon_item("Format", "active_report_options")
        util_obj.synchronize_with_number_of_element('[class*="bi-window active window "]', 1, 50)
        '''
        Step 04 : Click Display Window down arrow
        Expect to see the Window options.
        Cascade/Tabs.
        '''
        verify_active_report_options_dialog(self,window_list,"#generalPane #genWindowCombo [id^='BiButton']", "window")
        
        '''
        Step 05 : Click Display Freeze Column down arrow
        Expect to see the Freeze columns options.
        None / The Report Columns (i.e. Country / Car)
        '''
        verify_active_report_options_dialog(self,freeze_list,"#generalPane #freezeColsCombo [id^='BiButton']", "Freeze")
        
        '''
        Step 06 : Click Page Options Records Per Page down arrow
        Expect to see the Records Per Page options.
        Also expect to see that the Display Page Information block is checked by default.
        57 / ALL / 10 / 20 / 30 / 40 / 50
        '''
        verify_active_report_options_dialog(self,Pages_list,"#generalPane #recordsPerPageCombo [id^='BiButton']", "Records Per Page")
        
        '''
        Step 07 : Hover over Page Info Alignments
        Expect to see each option highlighted on hover over.
        Left / Center / Right Alignments
        '''
        verify_datapane_toggle_button_tooltip(self,"#generalPane #Left img","Left")
        verify_datapane_toggle_button_tooltip(self,"#generalPane #Center img","Center")
        verify_datapane_toggle_button_tooltip(self,"#generalPane #Right img","Right")
        '''
        Step 08 : Click Page Info Location down arrow
        Expect to see the Page Info Location options.
        Top Row / Bottom Row
        '''
        verify_active_report_options_dialog(self,Location_list,"#generalPane #pageLocationCombo [id^='BiButton']", "Location")
        
        '''
        Step 09 : Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        '''
        
        
if __name__ == '__main__':
    unittest.main()