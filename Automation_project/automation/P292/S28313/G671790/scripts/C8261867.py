'''
Created on May 17, 2019

@author: vpriya
Testcase Name : Creating new Designer Chart with Filters
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261867
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.text_editor import wf_texteditor
from common.wftools.login import Login
from common.wftools import wf_mainpage

class C8261867_TestClass(BaseTestCase):
    
    def test_C8261867(self):
        """
        Test case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        text_editor = wf_texteditor(self.driver)
        Login_obj = Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
    
        """
        Test case variables
        """
        
        Expected_lines = ["-DEFAULTH &WF_TITLE='WebFOCUS Report';"]
        Expected_Business_region = ['-DEFAULT &BUSINESS_REGION = _FOC_NULL;']
        Expected_Quantity_sold = ['-DEFAULT &QUANTITY_SOLD_FROM = _FOC_NULL;']
        Expected_Sale_Year = ['-DEFAULT &QUANTITY_SOLD_TO = _FOC_NULL;']
        
        Expected_where_condition1 =['WHERE WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_STORE.BUSINESS_REGION EQ &BUSINESS_REGION.(OR(FIND WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_STORE.BUSINESS_REGION IN BASEAPP/WF_RETAIL_LITE |FORMAT=A15V,SORT=ASCENDING)).Store Business Region.;']
        Expected_where_condition2 = ['WHERE WF_RETAIL_LITE.WF_RETAIL_SALES.QUANTITY_SOLD FROM &QUANTITY_SOLD_FROM.(FROM 1 TO 4 |FORMAT=I11C,LINK_TO=QUANTITY_SOLD_TO,TITLE=Quantity Sold).Quantity Sold From. TO &QUANTITY_SOLD_TO.(FROM 1 TO 4 |FORMAT=I11C,LINK_TO=QUANTITY_SOLD_FROM,TITLE=Quantity Sold).Quantity Sold To.;']
        
        Step1 = """
        Step 1: Launch the API to create new Designer Chart with the CAR file
        http://machine:port/ibi_apps/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%
        2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api('baseapp/wf_retail_lite')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        utill_obj.capture_screenshot("Step 01.01",Step1)
         
        Step2 = """
        Step 2:Drag and drop Store,Business,Region in to Horizontal Bucket from Dimensions > Store.
        Verify live preview updated with Store Business Region data.
        """
        designer_chart_obj.drag_dimension_field_to_query_bucket('Store->Store->Store,Business,Region','Horizontal')
        designer_chart_obj.wait_for_number_of_element("[class*='xaxisOrdinal-labels!']", 4, designer_chart_obj.chart_long_timesleep)
        designer_chart_obj.verify_number_of_risers('rect',1,4,msg="Step 02:01")
        designer_chart_obj.verify_x_axis_title_in_preview(["Store Business Region"],msg="Step 02:02")
        designer_chart_obj.verify_x_axis_label_in_preview(['EMEA', 'North America', 'Oceania', 'South America'],msg="Step 02:03")
        utill_obj.capture_screenshot("Step 02.01",Step2,True)
         
        Step3 = """
        Step 3:Double click Revenue under Measures > Sales.
        Verify Revenue field added to Vertical bucket and live preview updated with Revenue by Store Business Region.
        """
        designer_chart_obj.drag_measure_field_to_query_bucket("Sales->Revenue",'Vertical')
        designer_chart_obj.wait_for_number_of_element('[class*="yaxis-labels"]',8,designer_chart_obj.chart_long_timesleep)
        designer_chart_obj.verify_number_of_risers('rect',1,4,msg="Step 03:01")
        designer_chart_obj.verify_x_axis_title_in_preview(["Store Business Region"],msg="Step 03:02")
        designer_chart_obj.verify_y_axis_title_in_preview(["Revenue"],msg="Step 03:03")
        designer_chart_obj.verify_x_axis_label_in_preview(['EMEA', 'North America', 'Oceania', 'South America'],msg="Step 03:04")
        designer_chart_obj.verify_y_axis_label_in_preview(['0', '100M', '200M', '300M', '400M', '500M', '600M', '700M'],msg="Step 03:05")
        utill_obj.capture_screenshot("Step 03.01",Step3,True)
         
        Step4 = """
        Step4:Drag and drop "Sale,Year" into Color Bucket from Dimensions > Sales_Related > Transaction Date, Components.
        Verify live preview updated with Sale Year Color.
        """
         
        designer_chart_obj.drag_dimension_field_to_query_bucket('Sales_Related->Transaction Date, Components->Sale,Year','Color')
        designer_chart_obj.wait_for_number_of_element('rect[class*="riser"]',20,designer_chart_obj.home_page_medium_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(['EMEA', 'North America', 'Oceania', 'South America'],msg="Step 04:01")
        designer_chart_obj.verify_y_axis_label_in_preview(['0', '100M', '200M', '300M', '400M', '500M', '600M', '700M'],msg="Step 04:02")
        designer_chart_obj.verify_number_of_risers('rect',1,20,msg="Step 04:03")
        designer_chart_obj.verify_x_axis_title_in_preview(["Store Business Region"],msg="Step 04:04")
        designer_chart_obj.verify_y_axis_title_in_preview(["Revenue"],msg="Step 04:05")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s0!g0!mbar!"]','bar_blue',msg="Step 04:06")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s1!g0!mbar!"]','pale_green',msg="Step 04:07")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s2!g0!mbar!"]','dark_green',msg="Step 04:08")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s3!g0!mbar!"]','pale_yellow_2',msg="Step 04:09")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s4!g0!mbar!"]','sunset_orange',msg="Step 04:10")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s5!g0!mbar!"]','orange',msg="Step 04:11")
        designer_chart_obj.verify_legends_in_preview(['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016'],msg="Step 04:13")
        utill_obj.capture_screenshot("Step 04.01",Step4,True)
         
        Step5 = """
        Step 5:Drag and drop Store,Business,Region into Filter Bar present in top of the live preview from Dimensions > Store.
        Verify Store Business Region filter control added into the filter toolbar and does not display comma in filter pills.
        """
         
        designer_chart_obj.drag_data_field_from_dimensions_to_filter_pane("Store,Business,Region")
        designer_chart_obj.wait_for_number_of_element('.pop-top',1,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_filter_shelf([["Store Business Region","All"]],msg="Step 05:01")
        designer_chart_obj.verify_textbox_in_filter_shelf_fields_popup('Enter Search String','', msg="Step 05:02")
        designer_chart_obj.verify_button_in_filter_shelf_fields_popup("Select all",msg="Step 05:03")
        designer_chart_obj.verify_button_in_filter_shelf_fields_popup("Clear",msg="Step 05:04")
        checkbox_name = ['EMEA','North America','Oceania','South America']
        for name in checkbox_name:
            designer_chart_obj.verify_checkbox_in_filter_shelf_fields_popup(name,msg ="Step 05:05")
        utill_obj.capture_screenshot("Step 05.01",Step5,True)
         
        Step6 = """
        Step 6:Right click Quantity,Sold under Measures > Sales select Add to filter toolbar.
        Then right click on the Quantity Sold filter pill and select Filter on > Detail
        Verify Quantity Sold filter added into the filter toolbar.
        """
        designer_chart_obj.right_click_on_measures_field("Quantity,Sold",'Add to filter toolbar')
        designer_chart_obj.wait_for_number_of_element('.pop-top',1,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.right_click_filter_shelf_field("SUM.Quantity Sold",'Filter on->Detail')
        designer_chart_obj.verify_filter_shelf([["Quantity Sold","141 : 990,162"]],msg="Step 06:01")
        utill_obj.capture_screenshot("Step 06.01",Step6,True)
         
        Step7 = """
        Step 7:Drag and drop Sale,Day into the Filter Bar from Dimensions > Sales_Related > Transaction Date, Components.
        Verify Sale Day filter added into the filter toolbar.
        """
        designer_chart_obj.drag_data_field_from_dimensions_to_filter_pane("Sale,Day")
        designer_chart_obj.wait_for_number_of_element('.pop-top',1,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_filter_shelf([["Sale Day","All"]],msg="Step 07:01")
        designer_chart_obj.verify_button_in_filter_shelf_fields_popup("Clear",msg="Step 07:02")
        designer_chart_obj.verify_button_in_filter_shelf_fields_popup("Custom",msg="Step 07:03")
        designer_chart_obj.verify_radio_in_filter_shelf_fields_popup("Previous year and current",msg="Step 07:04")
        designer_chart_obj.verify_radio_in_filter_shelf_fields_popup("YTD",msg="Step 07:05")
        utill_obj.capture_screenshot("Step 07.01",Step7,True)
         
        Step8 = """
        Step 8:Click Save icon, enter Title as "C8261867" > click Save.
        """
        designer_chart_obj.save_as_from_application_menu(title="C8261867")
        utill_obj.capture_screenshot("Step 08.01",Step8)
 
        Step9 = """
        Step 9:Sign out using API:
        http://machine:port/alias/service/wf_security_logout.jsp.
        """
        designer_chart_obj.api_logout()
        utill_obj.capture_screenshot("Step 09.01",Step9)

        Step10 = """
        Step 10:Open the fex in Text editor
        """
        Login_obj.invoke_home_page('mrid', 'mrpass')
        main_page_obj.select_content_from_sidebar()
        main_page_obj.expand_repository_folder('P292_S28313->G671774')
        main_page_obj.right_click_folder_item_and_select_menu('C8261867','Edit with text editor')
        core_utils.switch_to_new_window()
        utill_obj.capture_screenshot("Step 10.01",Step10)
        
        Step11 ="""
        Step 11:Close Text Editor without saving.
        """
        text_editor.verify_line_in_texteditor(Expected_lines, step_num="Step11.01",comparison_type='asin')
        text_editor.verify_line_in_texteditor(Expected_Business_region, step_num="Step11.02",comparison_type='asin')
        text_editor.verify_line_in_texteditor(Expected_Quantity_sold, step_num="Step11.03",comparison_type='asin')
        text_editor.verify_line_in_texteditor(Expected_Sale_Year, step_num="Step11.04",comparison_type='asin')
        text_editor.verify_line_in_texteditor(Expected_where_condition1, step_num="Step11.05",comparison_type='asin')
        text_editor.verify_line_in_texteditor(Expected_where_condition2, step_num="Step11.06",comparison_type='asin')
        core_utils.switch_to_previous_window()
        utill_obj.capture_screenshot("Step 11.01",Step11,True)
        
        Step12 = """
        Step 12:Run created Designer Chart using API:
        http://machine:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S28313%252FG671774%252F&BIP_item=c8261867.fex
        Verify chart run successfully and no Auto Prompt window appears
        """
        designer_chart_obj.api_logout()
        designer_chart_obj.run_designer_chart_using_api('c8261867')
        utill_obj.verify_object_visible('.pop-top',False,msg= 'Step:12.01')
        designer_chart_obj.verify_x_axis_label_in_preview(['EMEA', 'North America', 'Oceania', 'South America'],parent_css='[id*="jschart_HOLD_0"]',msg="Step 12:01")
        designer_chart_obj.verify_y_axis_label_in_preview(['0', '100M', '200M', '300M', '400M', '500M', '600M', '700M'],parent_css='[id*="jschart_HOLD_0"]',msg="Step 12:02")
        designer_chart_obj.verify_number_of_risers('rect',1,20,msg="Step 12:03")
        designer_chart_obj.verify_x_axis_title_in_preview(["Store Business Region"],parent_css='[id*="jschart_HOLD_0"]',msg="Step 12:04")
        designer_chart_obj.verify_y_axis_title_in_preview(["Revenue"],parent_css='[id*="jschart_HOLD_0"]',msg="Step 12:05")
        utill_obj.capture_screenshot("Step 12.01",Step12,True)

        """
        Step 13: Sign out using API:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp.
        """
        
if __name__ == '__main__':
    unittest.main()