'''
Created on Sep 24, 2019

@author: Niranjan
Testcase Name : Designer Chart : Sort arrow is missing for Midnight.sty theme for DataGrid
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261895
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.pages.wf_mainpage import Wf_Mainpage
from common.wftools import designer_chart, page_designer
from common.lib.global_variables import Global_variables

class C8261895_TestClass(BaseTestCase):
    
    def test_C8261895(self):
        """
        Testcase case objects and variables
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        pd_design = page_designer.Design(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        homepage= Wf_Mainpage(self.driver)
        
        Step1 = """
        Step 1: Launch the IA API with workbook (edit the domain, port and alias of the URL - do not use the URL as is):
        http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%2F&master=baseapp%2Fwf_retail_lite&tool=workbook
        """
        designer_chart_obj.invoke_designer_chart_using_api('baseapp/wf_retail_lite', tool='workbook', mrid='mrid', mrpass ='mrpass')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        utils.capture_screenshot("01.00", Step1)
        
        Step2 = """
        Step 2: Select "DataGrid" from Chart picker component.
        """
        designer_chart_obj.select_chart_from_chart_picker('datagrid')
        utils.capture_screenshot("02.00", Step2)
        
        Step3 = """
        Step 3: Double click Product Category, Cost of Goods, Discount & Gross Profit.
        """
        designer_chart_obj.double_click_on_dimension_field('Product->Product->Product,Category')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "Product,Category", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('Sales->Cost of Goods')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "Cost of Goods", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('Discount')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "Discount", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('Gross Profit')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "Gross Profit", designer_chart_obj.chart_medium_timesleep)
        utils.capture_screenshot("03.00", Step3)
        
        Step4 = """
        Step 4: Click "New embedded Page" at the bottom and select Blank template.
        """
        embedded_page_elem = utils.validate_and_get_webdriver_object("div[class*='designer-new-page']", "New embedded page")
        core_utils.left_click(embedded_page_elem)
        pd_design.select_page_designer_template('Blank')
        pd_design.wait_for_visible_text('.pd-page-title', 'Page Heading')
        utils.capture_screenshot("04.00", Step4)
        
        Step5 = """
        Step 5: Drag "Chart 1" to the page and make the chart large to fit the page.
        """
        pd_design.drag_embedded_content_to_canvas_section('Chart 1', 1)
        if Global_variables.browser_name == 'Chrome':
            content_elem = utils.validate_and_get_webdriver_object('div[data-ibx-type="pdPageSection"] .grid-stack-item-content', 'Chart 1 Content')
            source_content_elem_coordinate = core_utils.get_web_element_coordinate(content_elem, element_location='middle_right')
            target_content_elem_coordinate = core_utils.get_web_element_coordinate(content_elem, element_location='middle_right' , xoffset = 500, yoffset = 200)
            core_utils.drag_and_drop(source_content_elem_coordinate['x'], source_content_elem_coordinate['y'], target_content_elem_coordinate['x'], target_content_elem_coordinate['y'])
            source_content_elem_coordinate = core_utils.get_web_element_coordinate(content_elem, element_location='bottom_right',yoffset = -8)
            target_content_elem_coordinate = core_utils.get_web_element_coordinate(content_elem, element_location='bottom_right' , yoffset = 200)
            core_utils.drag_and_drop(source_content_elem_coordinate['x'], source_content_elem_coordinate['y'], target_content_elem_coordinate['x'], target_content_elem_coordinate['y'])
        else:
            content_elem = utils.validate_and_get_webdriver_object('div[data-ibx-type="pdPageSection"] .grid-stack-item-content div[data-ibx-type="pdContainer"]', 'Chart 1 Content')
            source_content_elem_coordinate = core_utils.get_web_element_coordinate(content_elem, element_location='middle_right', xoffset =-2)
            target_content_elem_coordinate = core_utils.get_web_element_coordinate(content_elem, element_location='middle_right' , xoffset = 500, yoffset = 200)
            core_utils.drag_and_drop(source_content_elem_coordinate['x'], source_content_elem_coordinate['y'], target_content_elem_coordinate['x'], target_content_elem_coordinate['y'])
            source_content_elem_coordinate = core_utils.get_web_element_coordinate(content_elem, element_location='bottom_middle', yoffset =-2)
            target_content_elem_coordinate = core_utils.get_web_element_coordinate(content_elem, element_location='bottom_middle' , yoffset = 200)
            core_utils.drag_and_drop(source_content_elem_coordinate['x'], source_content_elem_coordinate['y'], target_content_elem_coordinate['x'], target_content_elem_coordinate['y'])
        
        utils.capture_screenshot("05.00", Step5)
        
        Step6 = """
        Step 6: Select the whole page and click on properties > Select Format tab(fa-fa-brush)icon.
        """
        page_elem = utils.validate_and_get_webdriver_object("div[class*='pd-page-title'][data-ibx-name='_title']", "page title")
        core_utils.left_click(page_elem)
        pd_design.click_property()
        pd_design.select_property_tab(tab_name = 'style')
        utils.capture_screenshot("06.00", Step6)
        
        Step7 = """
        Step 7: Click Theme drop down > Select "Midnight"
        Step 07.00 : Selected theme applied in Chart canvas and sort arrows are visible to the user.
        """  
        theme_dropdown_ele = utils.validate_and_get_webdriver_object('div[data-ibx-type="ibxAccordionPage"] .ibx-select-open-btn' , 'theme dropdown')
        core_utils.left_click(theme_dropdown_ele)
        homepage.select_context_menu_item('Midnight', pop_up_css="div[class*='pop-top']", row_css="div[class='ibx-label-text']")
        time.sleep(2)
        canvas_ele = utils.validate_and_get_webdriver_object('.pd-page-tab-content-wrapper' , 'background color')
        canvas_color = canvas_ele.value_of_css_property('background-image')
        expected_canvas_color = 'linear-gradient(to right, rgb(77, 64, 112) 0%, rgb(67, 110, 164) 100%)'
        utils.asequal(canvas_color, expected_canvas_color, 'Step 07.00 : Verify the color of canvas')
        core_utils.switch_to_frame(".pd-cont-iframe iframe[class='ibx-iframe-frame']")
        arrows_ele = self.driver.find_elements_by_css_selector('#jschart_HOLD_0 path[class="sortIcon"]')
        num_arrow = len(arrows_ele)
        utils.asequal(num_arrow, 4, 'Step 07.01 : Verify the sort arrow')
        core_utils.switch_to_default_content()
        utils.capture_screenshot("07.00", Step7)
        
        Step8 = """
        Step 8: Click Application menu > Close > No.
        """
        pd_design.close_page_designer_from_application_menu()
        utils.capture_screenshot("08.00", Step8)
        
        """
        Step 9: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
       
if __name__ == '__main__':
    unittest.main()