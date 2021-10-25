'''
Created on August 17, 2019

@author: vpriya
Testcase Name : Calculate Moving Aggregate using wf_retail_lite
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261996
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.lib import core_utility
from common.lib import utillity
import time

class C8261996_TestClass(BaseTestCase):
    
    def test_C8261996(self):
        """
        Test case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        utils = utillity.UtillityMethods(self.driver)
        
        
    
        Step1 = """
        Step 1: Launch the API to create new Designer Chart with the CAR file
        http://machine:port/ibi_apps/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%
        2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api('baseapp/wf_retail_lite')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        utils.capture_screenshot("01.01", Step1)
         
        Step2 = """
        Step2:Select Side-by-Side from Chart Layout.
        """
         
        designer_chart_obj.select_display_toolbar_in_query_bucket("Side-by-Side")
        utils.synchronize_with_visble_text("[class='yaxis-labels!m5!']",'50',designer_chart_obj.chart_medium_timesleep)
        utils.capture_screenshot("02.01", Step2)
 
        Step3 = """
        Step 3:Select "Revenue" from the Measures and drop it into Vertical bucket.
        """
        designer_chart_obj.drag_measure_field_to_query_bucket('Sales->Revenue','Vertical')
        utils.synchronize_with_visble_text(".yaxis-title",'Revenue',designer_chart_obj.chart_medium_timesleep)
        utils.capture_screenshot("03.01", Step3)
  
        Step4 = """
        Step 4:Select "Sale,Year" from the Dimensions (Sales Related > Transaction Date,Components ) and drop it into Horizontal bucket
        """
        designer_chart_obj.drag_dimension_field_to_query_bucket('Sales_Related->Transaction Date, Components->Sale,Year', 'Horizontal')
        utils.synchronize_with_visble_text("text[class = 'xaxisOrdinal-labels!g5!mgroupLabel!']",'2016',designer_chart_obj.chart_medium_timesleep)
        utils.capture_screenshot("04.01", Step4)
  
        Step5 = """
        Step 5:Select "Sale,Year /Quarter" from the Dimensions and drop it into Horizontal bucket.
        Date (Sale, Quarter) field appears into Horizontal bucket.
        """
        designer_chart_obj.drag_dimension_field_to_query_bucket('Sale,Year/Quarter', 'Horizontal')
        utils.synchronize_with_number_of_element("text[class*='xaxisOrdinal-labels']",24,designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_values_in_querybucket('Horizontal',['Sale,Year', 'Sale,Year/Quarter'],msg="Step5:Date (Sale, Quarter) field appears into Horizontal bucket.")
        utils.capture_screenshot("05.01", Step5,True)
         
        Step6 = """
        Step 6:Select "Sale,Year/Month" from the Dimensions and drop it into Horizontal bucket.
        Date (Sale, Month) field appears into Horizontal bucket.
        """
        designer_chart_obj.drag_dimension_field_to_query_bucket('Sale,Year/Month', 'Horizontal')
        utils.synchronize_with_number_of_element("text[class*='xaxisOrdinal-labels']",72,designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_values_in_querybucket('Horizontal',['Sale,Year', 'Sale,Year/Quarter', 'Sale,Year/Month'],msg="Step6:Date (Sale, Month) field appears into Horizontal bucket.")
        utils.capture_screenshot("06.01", Step6,True)
         
        Step7 = """
        Step 7:Select Revenue field from the Vertical bucket -> Right click -> Quick Transform -> Moving Aggregate -> Aggregation -> AVG (Break On -> Sale, Year/Quarter Year and Look Back = 1)
        Click Ok button.
        Revenue moving avg back1 Sale, Year/Quarter field is added into Vertical bucket.
        """
        designer_chart_obj.select_query_bucket_field_context_menu('Vertical', 'Revenue', 'Quick transform->Moving aggregate',click_type=None,element_location="middle_right",xoffset=12)
        time.sleep(2)
        designer_chart_obj.controls_menu_dialog().select_combobox_option('Aggregation','Average')
        designer_chart_obj.controls_menu_dialog().select_combobox_option('Break on','Sale,Year/Quarter')
        time.sleep(2)
        designer_chart_obj.controls_menu_dialog().enter_values_in_textbox('Look back','1')
        time.sleep(2)
        designer_chart_obj.controls_menu_dialog().click_ok_button()
        utils.synchronize_with_number_of_element("rect[class*='riser']",144,designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_values_in_querybucket('Vertical',['Revenue', 'Revenue moving ave back1 Sale,Year/Quarter'],msg="Step 7:Revenue moving avg back1 Sale, Year/Quarter field is added into Vertical bucket.")
        utils.capture_screenshot("07.01", Step7,True)
         
        Step8 = """
        Step 8:Select Revenue field from the Vertical bucket -> Right click -> Quick Transform -> Moving Aggregate -> Aggregation -> AVG (Break On -> Sale, Year and Look Back = 1)
        Click Ok button.
        Revenue moving avg back1 Sale, Year field is added into Vertical bucket.
        Chart is displayed as shown in the image below.
        """
        designer_chart_obj.select_query_bucket_field_context_menu('Vertical', 'Revenue', 'Quick transform->Moving aggregate',click_type=None,element_location="middle_right",xoffset=12)
        time.sleep(2)
        designer_chart_obj.controls_menu_dialog().select_combobox_option('Aggregation','Average')
        designer_chart_obj.controls_menu_dialog().select_combobox_option('Break on','Sale,Year')
        designer_chart_obj.controls_menu_dialog().enter_values_in_textbox('Look back','1')
        time.sleep(2)
        designer_chart_obj.controls_menu_dialog().click_ok_button()
        utils.synchronize_with_number_of_element("rect[class*='riser']",216,designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_values_in_querybucket('Vertical',['Revenue', 'Revenue moving ave back1 Sale,Year/Quarter', 'Revenue moving ave back1 Sale,Year'],msg="Step 8:Revenue moving avg back1 Sale, Year/Quarter field is added into Vertical bucket.")
        utils.capture_screenshot("08.01", Step8,True)
         
        Step9 = """
        Step 9:Select DataGrid from Chart picker component.
        """
        designer_chart_obj.select_chart_from_chart_picker('datagrid')
        utils.synchronize_with_visble_text(".rowTitleScroll",'Sale Year',designer_chart_obj.chart_medium_timesleep)
        #designer_chart_obj.create_data_grid_set("C8261996") writing expected data from web
        designer_chart_obj.verify_data_grid_set("C8261996","Step:09.01")
        utils.capture_screenshot("09.01", Step9)
  
        Step10 = """
        Step 10:Click run button, following report is displayed.
        Data is displayed as shown in the image below.
        """
        designer_chart_obj.click_toolbar_item("preview")
        core_utility_obj.switch_to_frame(frame_css="iframe[src*='TableChart_1']")
        utils.synchronize_with_visble_text(".tablePanel",'2012',designer_chart_obj.chart_medium_timesleep)
        #designer_chart_obj.create_data_grid_set("C8261996_run")  writing expected data from web
        designer_chart_obj.verify_data_grid_set("C8261996_run","Step:10.01")
        utils.capture_screenshot("10.01", Step10)
 
        Step11 = """
        Step 11:Click Save and Enter title as "C8261996" > Save
        """
        utils.switch_to_default_content()
        designer_chart_obj.go_back_to_design_from_preview()
        utils.synchronize_until_element_is_visible('[data-ibx-name="wfcTBButtonFileMenu"]',designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.save_as_from_application_menu("C8261996")
        utils.capture_screenshot("11.01", Step11)
 
        Step12 = """
        Step 12:Logout using API:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp.
        """
        designer_chart_obj.api_logout()
        utils.capture_screenshot("12.01", Step12)
 
        Step13 = """
        Step 13:Run C8261996.fex from BIP.
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%2P292_S28313%2FG671774 &BIP_item=c8261996.fex
        """
        designer_chart_obj.run_designer_chart_using_api('c8261996')
        utils.synchronize_with_visble_text(".tablePanel",'2012',designer_chart_obj.chart_medium_timesleep)
        #designer_chart_obj.create_data_grid_set("C8261996_run_1")writing expected data from web
        designer_chart_obj.verify_data_grid_set("C8261996_run_1","Step:13.01")
        utils.capture_screenshot("13.01", Step13)
        
        """
        Step 14:Logout using API:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp.
        """
        time.sleep(2)        
        
if __name__ == '__main__':
    unittest.main()