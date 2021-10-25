'''
Created on Aug 20, 2019

@author:Vpriya
Testcase Name : Supported and unsupported buttons are grayed out and active again respectively for Currency local
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9331935
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.lib import utillity
from common.wftools.designer_chart import Designer_Chart
from common.wftools.designer_chart import Designer_calculation_edit_format as edit_format
from common.locators.designer_chart_locators import DesignerChart as dc_locators


class C9335860_TestClass(BaseTestCase):
    
    def test_C9335860(self):
        """
        Test case objects
        """
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        utils = utillity.UtillityMethods(self.driver)
        designer_chart_obj=Designer_Chart(self.driver)
        edit_format_obj = edit_format(self.driver)
        
        """
        STEP 1:Launch the API to create new Designer Chart with the Car file
        http://machine:port/{alias}/designer?&item=IBFS:/WFC/Repository/P292_S29835/G730863&master=ibisamp/car&tool=chart. 
        """  
        designer_chart_obj.invoke_designer_chart_using_api("ibisamp/car", mrid='mriddev', mrpass='mrpassdev')
        utils.synchronize_until_element_is_visible(dc_locators.DIMENSIONS_FIELD_AREA_CSS,designer_chart_obj.chart_long_timesleep)
        utils.verify_object_visible(".chart-picker-box",True,"Step 01:03 verify the chart picker icon")
        utils.verify_object_visible(".pop-top",False,"Step 01:04 Verify the chart opens without any error")
        designer_chart_obj.verify_x_axis_label_in_preview(['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4'],msg="Step 01:05")
        designer_chart_obj.verify_y_axis_label_in_preview(['0', '40', '80', '120', '160', '200'],msg="Step 01:06")
        designer_chart_obj.verify_legends_in_preview(['Series 0', 'Series 1', 'Series 2', 'Series 3', 'Series 4'],msg="Step 01:07")
        
        """
        Step 2: Click on the vertical dots to the right of "Dimensions" > Click on "New calculation"
        New Calculation dialog is displayed
        
        """
        designer_chart_obj.select_new_calculation_from_dimensions_or_measures("Dimensions")
        utils.synchronize_until_element_is_visible(".wfc-calculator-dialog",designer_chart_obj.home_page_long_timesleep)
        utils.verify_object_visible(".wfc-calculator-dialog",True,"Step 02:New Calculation dialog is displayed")
        

        """
        Step 3:Click "Edit format" button
        """
        edit_format_obj.click_edit_format_on_calculation_dialog()
        
   
        """
        Step 4:Click Data type Integer (123) > Click Type "$" Currency (local)
        Verify the following dialog
        """
        edit_format_obj.select_datatype_in_dialog("numeric")
        edit_format_obj.select_datatype_in_numeric('currency')
        edit_format_obj.verify_selected_datatype_in_numeric('currency',"Step 04:01")
        edit_format_obj.verify_selected_datatype_in_dialog("numeric", "Step 04:02")
        edit_format_obj.verify_max_length_in_numeric('5',"Step 04:03")
        edit_format_obj.verify_decimal_place_in_numeric('2',"Step 04:04")
        edit_format_obj.verify_negative_numbers_in_numeric("Step 04:05",'-123')
        edit_format_obj.verify_currency_symbol_in_numeric('Base on locale',"step 04:06")
        edit_format_obj.verify_symbol_position_disabled_in_numeric("Step 04:07",checkbox_state='disable')
        edit_format_obj.verify_checkbox_in_numeric('Show 1000 separator', 'uncheck',"Step 04:08")
        edit_format_obj.verify_checkbox_in_numeric('Show leading zero', 'uncheck',"Step 04:09")

        """
        Step 5:Click on Negative brackets (123)
        Verify "Show thousand separator" and "Show leading zero" are grayed out
        """
        edit_format_obj.select_negative_numbers_in_numeric("(123)")
        edit_format_obj.verify_checkbox_is_disable_in_numeric("Show 1000 separator",'disable',"Step:05.01")
        edit_format_obj.verify_checkbox_is_disable_in_numeric("Show leading zero",'disable',"Step:05.01")
        
        """
        Step 6:Click on Negative number -123
        """
        edit_format_obj.select_negative_numbers_in_numeric("-123")

        """
        Step 7:Check off "Show 1000 separator"
        Verify "Show leading zero" is grayed out
        """
        edit_format_obj.select_checkbox_in_numeric("Show 1000 separator",'check')
        edit_format_obj.verify_checkbox_is_disable_in_numeric("Show leading zero",'disable',"Step:07.01")


        """
        Step 8:Uncheck "Show 1000 separator"
        Verify "Show leading zero" is active again
        """
        edit_format_obj.select_checkbox_in_numeric("Show 1000 separator",'uncheck' )
        edit_format_obj.verify_checkbox_is_disable_in_numeric("Show leading zero",'enable',"Step:08.01")

        """
        Step 9:Check off "Show leading zero"
        Verify "Show 1000 separator" is grayed out
        """
        edit_format_obj.select_checkbox_in_numeric("Show leading zero",'check')
        edit_format_obj.verify_checkbox_is_disable_in_numeric("Show 1000 separator",'disable',"Step:09.01")
        

        """
        Step 10:Uncheck "Show leading zero"
        Verify "Show 1000 separator" is active again
        """
        edit_format_obj.select_checkbox_in_numeric("Show leading zero",'uncheck')
        edit_format_obj.verify_checkbox_is_disable_in_numeric("Show 1000 separator",'enable',"Step:10.01")
        
        
        """
        Step 11:Check off "Show 1000 separator" and select Negative brackets (123)
        Verify "Show 1000 separator" is grayed out
        """
        edit_format_obj.select_checkbox_in_numeric("Show 1000 separator",'check' )
        edit_format_obj.select_negative_numbers_in_numeric("(123)")
        edit_format_obj.verify_checkbox_is_disable_in_numeric("Show 1000 separator",'disable',"Step:11.01")

        """
        Step 12:Click on Negative number -123
        """
        edit_format_obj.select_negative_numbers_in_numeric("-123")
        
        """
        Step 13:Check off "Show leading zero" and select Negative brackets (123)
        Verify "Show leading zero" is grayed out
        """
        edit_format_obj.select_checkbox_in_numeric("Show leading zero",'check')
        edit_format_obj.select_negative_numbers_in_numeric("(123)")
        edit_format_obj.verify_checkbox_is_disable_in_numeric("Show leading zero",'disable',"Step:13.01")

        """
        Step 14:Click "Currency symbol" dropdown > Select "Dollar($)" or any symbols
        Verify symbol position are active
        """
        edit_format_obj.select_currency_symbol_in_numeric("Dollar($)")
        edit_format_obj.verify_symbol_position_disabled_in_numeric("Step:14")

        """
        Step 15:Click "Currency symbol" dropdown > Select "Base on locale"
        Verify symbol position are grayed out
        """
        edit_format_obj.select_currency_symbol_in_numeric("Base on locale")
        edit_format_obj.verify_symbol_position_disabled_in_numeric("Step:14",checkbox_state='disable')

        """
        Step 16:Click Cancel (2X)
        """
        main_page_obj.click_button_on_popup_dialog("Cancel")
        designer_chart_obj.click_button_on_calculation("Cancel")
        
 
        """
        Step 17:Click Application menu > Close > click No.
        """
 
        designer_chart_obj.close_designer_chart_from_application_menu()
 
        """
        Step 18:Logout using API:
        http://machine:port/alias/service/wf_security_logout.jsp.
        """

 

 
        
        
        
               
if __name__ == '__main__':
    unittest.main()