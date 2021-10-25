'''
Created on June 3, 2019

@author: Varun
Testcase Name : Line style widget
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261909
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.lib import utillity

class C8261909_TestClass(BaseTestCase):
    
    def test_C8261909(self):
        """
        Testcase case objects and variables
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        utillity_obj=utillity.UtillityMethods(self.driver)
        x_label = ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'] 
        y_label = ['0', '10K', '20K', '30K', '40K', '50K', '60K']
        x_title = ['COUNTRY']
        y_title=['DEALER_COST']
        line_dash_css="[class*='risers'] path[stroke-dasharray]"
        
        """
        Step 1: Launch the API to create new Designer Chart with the Car file
        http://machine:port/{alias}/designer?&item=IBFS:/WFC/Repository/P292_S29835/G730863&master=ibisamp/car&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api("ibisamp/car")
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
  
        """
        Step 2: Double click COUNTRY, DEALER_COST.
        """
        designer_chart_obj.double_click_on_dimension_field('COUNTRY')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "COUNTRY", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('COMP->CARREC->BODY->DEALER_COST')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "DEALER_COST", designer_chart_obj.chart_medium_timesleep)
        
        """
        Step 3:Select "Line" chart from Chart picker component.
        """
        designer_chart_obj.select_chart_from_chart_picker("absolute_line")
        designer_chart_obj.verify_x_axis_label_in_preview(x_label,msg="Step:3.1")
        designer_chart_obj.verify_y_axis_label_in_preview(y_label,msg="Step:3.2")
        designer_chart_obj.verify_x_axis_title_in_preview(x_title,msg="Step:3.3")
        designer_chart_obj.verify_y_axis_title_in_preview(y_title,msg="Step:3.4")
        designer_chart_obj.verify_text_in_heading(['Chart', 'Heading'], msg="Step:3.5")

        """
        Step 4:Select Format tab(fa-fa-brush) icon.
        Step 5 Click General drop down > Select "Series"
        Line style displayed.
        """
        designer_chart_obj.select_query_or_format_tab()
        designer_chart_obj.select_format_access_option('Series')
        
        """
        Step 6:Click Line style drop down > Select "------" style.
        Changed settings reflected in canvas.
        """
        designer_chart_obj.select_line_style_options_series_format("Dash")
        utillity_obj.synchronize_until_element_is_visible(line_dash_css,designer_chart_obj.chart_long_timesleep)
        utillity_obj.verify_object_visible(line_dash_css, True,"Step 06.1 verify the Changed line style settings reflected in canvas. ")
    
        """
        Step 7:Click Save icon from Toolbar.
        Step 8:Enter Title as "C8261909" > Click Save.
        """
        designer_chart_obj.save_designer_chart_from_toolbar('C8261909')
 
        """
        Step 9:Launch the IA API to logout.
        http://machine:port/alias/service/wf_security_logout.jsp
        """
if __name__ == '__main__':
    unittest.main()