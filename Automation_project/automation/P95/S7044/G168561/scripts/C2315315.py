'''
Created on January 21, 2019

@author: KK14897

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2315315
TestCase Name = Verify Freeze column(s) for each By Field on a report.
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity,core_utility
from common.wftools import active_report
from common.wftools import report, document
from common.lib.javascript import JavaScript

class C2315315_TestClass(BaseTestCase):

    def test_C2315315(self):
        
        """
        Test case Object's
        """
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        ar_obj=active_report.Active_Report(self.driver)
        report_obj=report.Report(self.driver)
        doc_obj=document.Document(self.driver)
        
        '''
        Variables
        '''
        table_css="TableChart_1"
        Test_Case_ID="C2315315"
        Fixed_css="#IFixWindowBody0 table>tbody>tr"
        scroll_css="#IScrollWindowBodyTab0 table>tbody>tr"
        
        def verify_default_active_report_options_dialog(self, exp_val, css, input_type, msg, dropdown_name):
            actual_text=util_obj.validate_and_get_webdriver_object(css, dropdown_name)
            actual_text=util_obj.get_attribute_value(actual_text, input_type)
            util_obj.asequal(exp_val, actual_text[input_type].strip(), msg)
                 
        '''       
        Step 01 : Launch IA Report using below API link
        http://machine:port/{alias}/ia?tool=Report&master=ibisamp/car&item=IBFS:/WFC/Repository/P95_S7044/G168561
        Set the browser size to '1280x720'
        '''
        ar_obj.invoke_report_tool_using_api("ibisamp/car", mrid="mriddev", mrpass="mrpassdev")
        report_obj.set_browser_window_size('1280','720')
        
        '''
        Step 02 :Add fields COUNTRY, CAR, MODEL, BODYTYPE,DEALER_COST, RETAIL_COST, SALES, SEATS, LENGTH, WIDTH & HEIGHT.
        Select Active Report as the output option.
        Expect to see the following Active Report Preview pane.
        Also expect to see a horizontal scrollbar, as there are more fields that appear off-screen to the right.
        '''
        fields_list=["COUNTRY", "CAR", "MODEL", "BODYTYPE", "DEALER_COST", "RETAIL_COST", "SALES", "SEATS", "LENGTH", "WIDTH", "HEIGHT"]
        for field in fields_list:
            report_obj.double_click_on_datetree_item(field, 1)
            report_obj.wait_for_visible_text('#'+table_css, field, 20)
            
        report_obj.change_output_format_type("active_report")
#         report_obj.create_report_data_set_in_preview(table_css, 18, 11, Test_Case_ID+"_Ds_01.xlsx")
        report_obj.verify_report_data_set_in_preview(table_css, 18, 11, Test_Case_ID+"_Ds_01.xlsx","Verify Preview")
        obj=self.driver.find_element_by_css_selector("#TableChart_1 [id^='BiLabel'][style*='overflow: auto']")
        util_obj.verify_element_has_horizontal_scrollbar(obj, "Step 02: verify Scroll bar availability")
        before_loc=util_obj.validate_and_get_webdriver_objects("#TableChart_1 [class^='x']", 'column list')[90]
        x_value_before=int(core_util_obj.get_web_element_coordinate(before_loc, element_location="middle_left")['x'])
        JavaScript.scrollIntoView(self, before_loc)
        after_loc=util_obj.validate_and_get_webdriver_objects("#TableChart_1 [class^='x']", 'column list')[90]
        x_value_after=int(core_util_obj.get_web_element_coordinate(after_loc, element_location="middle_left")['x'])
        util_obj.as_not_equal(x_value_before,x_value_after,"Step 2: verify field value before and after scroll and scroll bar is present")
        
        '''
        Step 03 :Click the Format tab, then select Active Report Options.
        Click the Freeze Columns down arrow.
        Select COUNTRY
        Expect to see the following Active Reports option menu with COUNTRY as the Freeze column.
        '''
        report_obj.select_ia_ribbon_item("Format", "active_report_options")
        util_obj.synchronize_with_number_of_element('[class*="bi-window active window "]', 1, 50)
        ar_obj.active_report_options('General',general_freeze_columns="COUNTRY")
        verify_default_active_report_options_dialog(self, "COUNTRY","#generalPane #freezeColsCombo [class*='combo-box-label']","text","Step 3: Verify Pages Default", "Pages")
         
        '''
        Step 04 : Click the OK button.
        Click the Run button.
        Scroll down slightly to see the horizontal scroll bar
        Expect to see the following Active report.
        '''
        ar_obj.active_report_options('General',btnOk=True)
        report_obj.select_ia_toolbar_item('toolbar_run')
        obj=self.driver.find_element_by_css_selector("#TableChart_1 [id^='BiLabel'][style*='overflow: auto']")
        util_obj.verify_element_has_horizontal_scrollbar(obj, "Step 02: verify Scroll bar availability")
        report_obj.switch_to_frame("[id^='ReportIframe']")
        move_to_bottom=util_obj.validate_and_get_webdriver_objects("#MAINTABLE_0 table>tbody>tr:nth-child(2) td:nth-child(8)", 'move_to_bottom')[18]
        JavaScript.scrollIntoView(self, move_to_bottom)
#         ar_obj.create_active_report_dataset(Test_Case_ID+"_Ds_03.1.xlsx", "#IFixWindowBody0")
        ar_obj.verify_active_report_dataset(Test_Case_ID+"_Ds_03.1.xlsx", "Step 3.1: Dataset Verification", "#IFixWindowBody0")
#         ar_obj.create_active_report_dataset(Test_Case_ID+"_Ds_03.2.xlsx", "#IScrollWindowBodyTab0")
        ar_obj.verify_active_report_dataset(Test_Case_ID+"_Ds_03.2.xlsx", "Step 3.2: Dataset Verification", "#IScrollWindowBodyTab0")
         
        '''
        Step 05 : Move the scroll bar all the way to the right.
        Expect to see the report scroll to the right but the Freeze column - COUNTRY does not move.
        '''
        x_country_before_scroll_obj=util_obj.validate_and_get_webdriver_object(Fixed_css, "Country column")
        x_country_before_scroll=int(core_util_obj.get_web_element_coordinate(x_country_before_scroll_obj, element_location="middle_left")['x'])
        x_car_before_scroll_obj=util_obj.validate_and_get_webdriver_objects(scroll_css, "Car")
        x_car_before_scroll=int(core_util_obj.get_web_element_coordinate(x_car_before_scroll_obj[0], element_location="middle_left")['x'])
        move_to_right=util_obj.validate_and_get_webdriver_objects("#MAINTABLE_0 table>tbody>tr:nth-child(1) td:nth-child(10)", 'move_to_bottom')[18]
        JavaScript.scrollIntoView(self, move_to_right)
        x_country_after_column_obj=util_obj.validate_and_get_webdriver_object(Fixed_css, "Country column")
        x_country_after_column=int(core_util_obj.get_web_element_coordinate(x_country_after_column_obj, element_location="middle_left")['x'])
        x_car_after_scroll_obj=util_obj.validate_and_get_webdriver_objects(scroll_css, "Car")
        x_car_after_scroll=int(core_util_obj.get_web_element_coordinate(x_car_after_scroll_obj[0], element_location="middle_left")['x'])
        util_obj.asequal(x_country_before_scroll,x_country_after_column,"Step 5.1 : verify country column freezes")
        util_obj.as_not_equal(x_car_before_scroll, x_car_after_scroll,"Step 5.2 : verify model column scrolls")
         
        '''
        Step 06 : Click the Format tab, then select Active Report Options.
        Click the Freeze Columns down arrow.
        Select CAR.
        Click OK.
        Click the Run button.
        Scroll down slightly to see the horizontal scroll bar.
        '''
        report_obj.switch_to_default_content()
        report_obj.select_ia_ribbon_item("Format", "active_report_options")
        util_obj.synchronize_with_number_of_element('[class*="bi-window active window "]', 1, 50)
        ar_obj.active_report_options('General',general_freeze_columns="CAR")
        verify_default_active_report_options_dialog(self, "CAR","#generalPane #freezeColsCombo [class*='combo-box-label']","text","Step 6: Verify Pages Default", "Pages")
        ar_obj.active_report_options('General',btnOk=True)
        report_obj.select_ia_toolbar_item('toolbar_run')
        obj=self.driver.find_element_by_css_selector("#TableChart_1 [id^='BiLabel'][style*='overflow: auto']")
        util_obj.verify_element_has_horizontal_scrollbar(obj, "Step 06: verify Scroll bar availability")
        report_obj.switch_to_frame("[id^='ReportIframe']")
        move_to_bottom=util_obj.validate_and_get_webdriver_objects("#MAINTABLE_0 table>tbody>tr:nth-child(2) td:nth-child(8)", 'move_to_bottom')[18]
#         ar_obj.create_active_report_dataset(Test_Case_ID+"_Ds_06.1.xlsx", "#IFixWindowBody0")
        ar_obj.verify_active_report_dataset(Test_Case_ID+"_Ds_06.1.xlsx", "Step 6.1: Dataset Verification", "#IFixWindowBody0")
#         ar_obj.create_active_report_dataset(Test_Case_ID+"_Ds_06.2.xlsx", "#IScrollWindowBodyTab0")
        ar_obj.verify_active_report_dataset(Test_Case_ID+"_Ds_06.2.xlsx", "Step 6.2: Dataset Verification", "#IScrollWindowBodyTab0")
        JavaScript.scrollIntoView(self, move_to_bottom)

         
        '''
        Step 07 : Move the scroll bar all the way to the right.
        Expect to see the report scroll to the right but the Freeze columns - COUNTRY/CAR do not move.
        '''
        x_country_before_scroll_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "country")
        x_country_before_scroll=int(core_util_obj.get_web_element_coordinate(x_country_before_scroll_obj[0], element_location="middle_left")['x'])
        x_car_before_scroll_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "Car")
        x_car_before_scroll=int(core_util_obj.get_web_element_coordinate(x_car_before_scroll_obj[1], element_location="middle_left")['x'])
        x_model_before_scroll_obj=util_obj.validate_and_get_webdriver_objects(scroll_css, "Model")
        x_model_before_scroll=int(core_util_obj.get_web_element_coordinate(x_model_before_scroll_obj[0], element_location="middle_left")['x'])
        move_to_right=util_obj.validate_and_get_webdriver_objects("#MAINTABLE_0 table>tbody>tr:nth-child(1) td:nth-child(9)", 'move_to_bottom')[18]
        JavaScript.scrollIntoView(self, move_to_right)
        x_country_after_column_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "country, car")
        x_country_after_column=int(core_util_obj.get_web_element_coordinate(x_country_after_column_obj[0], element_location="middle_left")['x'])
        x_car_after_column_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "Car")
        x_car_after_column=int(core_util_obj.get_web_element_coordinate(x_car_after_column_obj[1], element_location="middle_left")['x'])
        x_model_after_scroll_obj=util_obj.validate_and_get_webdriver_objects(scroll_css, "Model")
        x_model_after_scroll=int(core_util_obj.get_web_element_coordinate(x_model_after_scroll_obj[0], element_location="middle_left")['x'])
        util_obj.asequal(x_country_before_scroll,x_country_after_column,"Step 7.1: verify country column freezes")
        util_obj.asequal(x_car_before_scroll,x_car_after_column,"Step 7.2: verify car column freezes")
        util_obj.as_not_equal(x_model_before_scroll,x_model_after_scroll,"Step 7.3: verify model column scrolls")
         
         
        '''
        Step 08 : Click the Format tab, then select Active Report Options.
        Click the Freeze Columns down arrow.
        Select BODYTYPE.
        Click OK.
        Click the Run button.
        Scroll down slightly to see the horizontal scroll bar.
        Expect to see the following Active report.
        Note that the horizontal scroll bar has shortened and moved to the right.
        '''
        report_obj.switch_to_default_content()
        report_obj.select_ia_ribbon_item("Format", "active_report_options")
        util_obj.synchronize_with_number_of_element('[class*="bi-window active window "]', 1, 50)
        ar_obj.active_report_options('General',general_freeze_columns="BODYTYPE")
        verify_default_active_report_options_dialog(self, "BODYTYPE","#generalPane #freezeColsCombo [class*='combo-box-label']","text","Step 8: Verify Pages Default", "Pages")
        ar_obj.active_report_options('General',btnOk=True)
        report_obj.select_ia_toolbar_item('toolbar_run')
        obj=self.driver.find_element_by_css_selector("#TableChart_1 [id^='BiLabel'][style*='overflow: auto']")
        util_obj.verify_element_has_horizontal_scrollbar(obj, "Step 08: verify Scroll bar availability")
        report_obj.switch_to_frame("[id^='ReportIframe']")
        move_to_bottom=util_obj.validate_and_get_webdriver_object("#IScrollWindowBodyTab0>tbody>tr:nth-child(19)", 'move_to_bottom')
#         ar_obj.create_active_report_dataset(Test_Case_ID+"_Ds_08.1.xlsx", "#IFixWindowBody0")
        ar_obj.verify_active_report_dataset(Test_Case_ID+"_Ds_08.1.xlsx", "Step 8.1: Dataset Verification", "#IFixWindowBody0")
#         ar_obj.create_active_report_dataset(Test_Case_ID+"_Ds_08.2.xlsx", "#IScrollWindowBodyTab0")
        ar_obj.verify_active_report_dataset(Test_Case_ID+"_Ds_08.2.xlsx", "Step 8.2: Dataset Verification", "#IScrollWindowBodyTab0")
        JavaScript.scrollIntoView(self, move_to_bottom)

        
        '''
        Step 09 :Move the scroll bar all the way to the right.
        Expect to see the report scroll to the right but the Freeze columns - COUNTRY/CAR/MODEL/BODYTYPE do not move.
        '''
        x_country_before_scroll_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "country")
        x_country_before_scroll=int(core_util_obj.get_web_element_coordinate(x_country_before_scroll_obj[0], element_location="middle_left")['x'])
        x_car_before_scroll_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "Car")
        x_car_before_scroll=int(core_util_obj.get_web_element_coordinate(x_car_before_scroll_obj[1], element_location="middle_left")['x'])
        x_model_before_scroll_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "model")
        x_model_before_scroll=int(core_util_obj.get_web_element_coordinate(x_model_before_scroll_obj[2], element_location="middle_left")['x'])
        x_body_before_scroll_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "body type")
        x_body_before_scroll=int(core_util_obj.get_web_element_coordinate(x_body_before_scroll_obj[3], element_location="middle_left")['x'])
        x_dcost_before_scroll_obj=util_obj.validate_and_get_webdriver_objects(scroll_css, "Dealer_Cost")
        x_dcost_before_scroll=int(core_util_obj.get_web_element_coordinate(x_dcost_before_scroll_obj[0], element_location="middle_left")['x'])
        move_to_right=util_obj.validate_and_get_webdriver_objects("#IScrollWindowBodyTab0>tbody>tr>td", 'move_to_bottom')[132]
        JavaScript.scrollIntoView(self, move_to_right)
        x_country_after_column_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "country")
        x_country_after_column=int(core_util_obj.get_web_element_coordinate(x_country_after_column_obj[0], element_location="middle_left")['x'])
        x_car_after_column_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "Car")
        x_car_after_column=int(core_util_obj.get_web_element_coordinate(x_car_after_column_obj[1], element_location="middle_left")['x'])
        x_model_after_scroll_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "Model")
        x_model_after_scroll=int(core_util_obj.get_web_element_coordinate(x_model_after_scroll_obj[2], element_location="middle_left")['x'])
        x_body_after_scroll_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "body type")
        x_body_after_scroll=int(core_util_obj.get_web_element_coordinate(x_body_after_scroll_obj[3], element_location="middle_left")['x'])
        x_dcost_after_scroll_obj=util_obj.validate_and_get_webdriver_objects(scroll_css, "Dealer_Cost")
        x_dcost_after_scroll=int(core_util_obj.get_web_element_coordinate(x_dcost_after_scroll_obj[0], element_location="middle_left")['x'])
        util_obj.asequal(x_country_before_scroll,x_country_after_column,"Step 9.1: verify country column freezes")
        util_obj.asequal(x_car_before_scroll,x_car_after_column,"Step 9.2: verify car column freezes")
        util_obj.asequal(x_model_before_scroll,x_model_after_scroll,"Step 9.3: verify country column freezes")
        util_obj.asequal(x_body_before_scroll,x_body_after_scroll,"Step 9.4: verify car column freezes")
        util_obj.as_not_equal(x_dcost_before_scroll,x_dcost_after_scroll,"Step 9.5: verify model column scrolls")
        
        '''
        Step 10 : Close the Report window.
        Click the Format tab, then click the Document button.
        Expect to see the Active Report converted into an Active Document.
        '''
        report_obj.switch_to_default_content()
        doc_obj.select_result_area_panel_caption_button("window-close")
        report_obj.select_ia_ribbon_item("Home", "document")
        conversion_obj=self.driver.find_element_by_css_selector("#HomeCompose")
        util_obj.verify_checked_class_property(conversion_obj, "Step 10 : verify active report converted to active document")
        
        '''
        Step 11 :Click the Run button.
        Scroll down slightly to see the horizontal scroll bar."
        '''
        report_obj.select_ia_toolbar_item('toolbar_run')
        report_obj.switch_to_frame("[id^='ReportIframe']")
        move_to_bottom=util_obj.validate_and_get_webdriver_object("#IScrollWindowBodyTab0>tbody>tr:nth-child(19)", 'move_to_bottom')
        JavaScript.scrollIntoView(self, move_to_bottom)
#         ar_obj.create_active_report_dataset(Test_Case_ID+"_Ds_11.1.xlsx", "#IFixWindowBody0")
        ar_obj.verify_active_report_dataset(Test_Case_ID+"_Ds_11.1.xlsx", "Step 11.1: Dataset Verification", "#IFixWindowBody0")
#         ar_obj.create_active_report_dataset(Test_Case_ID+"_Ds_11.2.xlsx", "#IScrollWindowBodyTab0")
        ar_obj.verify_active_report_dataset(Test_Case_ID+"_Ds_11.2.xlsx", "Step 11.2: Dataset Verification", "#IScrollWindowBodyTab0")
        
        '''
        Step 12 :Move the scroll bar all the way to the right.
        Expect to see the report scroll to the right but the Freeze columns - COUNTRY/CAR/MODEL/BODYTYPE do not move.
        '''
        x_country_before_scroll_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "country")
        x_country_before_scroll=int(core_util_obj.get_web_element_coordinate(x_country_before_scroll_obj[0], element_location="middle_left")['x'])
        x_car_before_scroll_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "Car")
        x_car_before_scroll=int(core_util_obj.get_web_element_coordinate(x_car_before_scroll_obj[1], element_location="middle_left")['x'])
        x_model_before_scroll_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "model")
        x_model_before_scroll=int(core_util_obj.get_web_element_coordinate(x_model_before_scroll_obj[2], element_location="middle_left")['x'])
        x_body_before_scroll_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "body type")
        x_body_before_scroll=int(core_util_obj.get_web_element_coordinate(x_body_before_scroll_obj[3], element_location="middle_left")['x'])
        x_dcost_before_scroll_obj=util_obj.validate_and_get_webdriver_objects(scroll_css, "Dealer_Cost")
        x_dcost_before_scroll=int(core_util_obj.get_web_element_coordinate(x_dcost_before_scroll_obj[0], element_location="middle_left")['x'])
        move_to_right=util_obj.validate_and_get_webdriver_objects("#IScrollWindowBodyTab0>tbody>tr>td", 'move_to_bottom')[132]
        JavaScript.scrollIntoView(self, move_to_right)
        x_country_after_column_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "country")
        x_country_after_column=int(core_util_obj.get_web_element_coordinate(x_country_after_column_obj[0], element_location="middle_left")['x'])
        x_car_after_column_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "Car")
        x_car_after_column=int(core_util_obj.get_web_element_coordinate(x_car_after_column_obj[1], element_location="middle_left")['x'])
        x_model_after_scroll_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "Model")
        x_model_after_scroll=int(core_util_obj.get_web_element_coordinate(x_model_after_scroll_obj[2], element_location="middle_left")['x'])
        x_body_after_scroll_obj=util_obj.validate_and_get_webdriver_objects(Fixed_css, "body type")
        x_body_after_scroll=int(core_util_obj.get_web_element_coordinate(x_body_after_scroll_obj[3], element_location="middle_left")['x'])
        x_dcost_after_scroll_obj=util_obj.validate_and_get_webdriver_objects(scroll_css, "Dealer_Cost")
        x_dcost_after_scroll=int(core_util_obj.get_web_element_coordinate(x_dcost_after_scroll_obj[0], element_location="middle_left")['x'])
        util_obj.asequal(x_country_before_scroll,x_country_after_column,"Step 10.1: verify country column freezes")
        util_obj.asequal(x_car_before_scroll,x_car_after_column,"Step 10.2: verify car column freezes")
        util_obj.asequal(x_model_before_scroll,x_model_after_scroll,"Step 10.3: verify country column freezes")
        util_obj.asequal(x_body_before_scroll,x_body_after_scroll,"Step 10.4: verify car column freezes")
        util_obj.as_not_equal(x_dcost_before_scroll,x_dcost_after_scroll,"Step 10.5: verify model column scrolls")
        '''
        Step 13 : Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        '''
        
        
if __name__ == '__main__':
    unittest.main()