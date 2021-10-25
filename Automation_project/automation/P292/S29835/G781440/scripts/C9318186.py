'''
Created on August 6, 2019

@author: Vpriya
Testcase Name : Use of Esc key to exit preview mode
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9318186
'''
import unittest
import keyboard
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.lib import core_utility
from common.lib import utillity
from common.locators.designer_chart_locators import DesignerInsight as insight_locators
from common.wftools import wf_mainpage



class C9318186_TestClass(BaseTestCase):
    
    def test_C9318186(self):
        
        """
        Testcase variables
        """
        Run_parent_css = "#jschart_HOLD_0"
        x_label = ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        y_label =  ['0', '30K', '60K', '90K', '120K', '150K']
        x_title = ['COUNTRY']
        expected_legend_list=['DEALER_COST', 'RETAIL_COST']
        
        """
        Testcase case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        utillity_obj=utillity.UtillityMethods(self.driver)
        insight_loc_obj=insight_locators()
        wf_mainpage_obj=wf_mainpage.Wf_Mainpage(self.driver)
        
        """
        Step 1: Launch the API with Designer Chart (edit the domain, port and alias of the URL - do not use the URL as is):
        http://machine:port/alias/designer?&master=ibisamp%2Fcar&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29835%2FG730863&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api("ibisamp/car")
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
  
        """
        Step 2: Double click "COUNTRY" field under Dimensions.
        "COUNTRY" added to Horizontal bucket.
        """
        """
        Step 3:Add "DEALER_COST" and "RETAIL_COST" under Measures to Vertical bucket.
        "DEALER_COST" and "RETAIL_COST" added to canvas.
        """
        designer_chart_obj.double_click_on_dimension_field("COUNTRY")
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "COUNTRY", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field("COMP->CARREC->BODY->DEALER_COST")
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "DEALER_COST", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field("COMP->CARREC->BODY->RETAIL_COST")
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "RETAIL_COST", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_values_in_querybucket('Horizontal', ['COUNTRY'], 'Step 3.1: Verify the horizontal bucket')
        designer_chart_obj.verify_values_in_querybucket('Vertical', ['DEALER_COST','RETAIL_COST'], 'Step 3.2: Verify the vertical bucket')
        designer_chart_obj.verify_x_axis_label_in_preview(x_label, msg='Step 3.3')
        designer_chart_obj.verify_y_axis_label_in_preview(y_label, msg='Step 3.4')
        designer_chart_obj.verify_x_axis_title_in_preview(x_title, msg='Step 3.5')
        designer_chart_obj.verify_number_of_risers('rect[class^="riser!"]', 1, 10, msg='Step 3.6')
        designer_chart_obj.verify_legends_in_preview(expected_legend_list,msg="Step 3.7")
        
        """
        Step 4:Click Preview. 
        """
        designer_chart_obj.click_toolbar_item("preview")
        core_utility_obj.switch_to_frame(insight_loc_obj.INSIGHT_PREVIEW_FRAME)
        utillity_obj.synchronize_until_element_is_visible(Run_parent_css,designer_chart_obj.home_page_long_timesleep)
        
        """
        Step04:01 :Chart in Preview mode.
        """
        designer_chart_obj.verify_x_axis_label_in_preview(x_label,parent_css="#jschart_HOLD_0",msg='Step:04:01')
        designer_chart_obj.verify_y_axis_label_in_preview(y_label, parent_css="#jschart_HOLD_0",msg='Step:4.02')
        designer_chart_obj.verify_x_axis_title_in_preview(x_title, parent_css="#jschart_HOLD_0",msg='Step 3.5')
        designer_chart_obj.verify_number_of_risers('#jschart_HOLD_0 rect[class^="riser!"]', 1, 10, msg='Step 3.6')
        core_utility_obj.switch_to_default_content()
        
        """
        Step 05: Press "Esc" key in Keyboard.
        """
        keyboard.send('esc')
            
        """   
        After pressing "Esc" key chart returns to design mode.
        """
        designer_chart_obj.verify_values_in_querybucket('Horizontal', ['COUNTRY'], 'Step 3.1: Verify the horizontal bucket')
        designer_chart_obj.verify_values_in_querybucket('Vertical', ['DEALER_COST','RETAIL_COST'], 'Step 3.2: Verify the vertical bucket')
        
        """
        Step 06:Click Application menu > Close > click No.
        """
        designer_chart_obj.close_designer_chart_from_application_menu()
        wf_mainpage_obj.click_button_on_popup_dialog("No")
        
        """
        Step 7:Launch the IA API to logout.
        http://machine:port/alias/service/wf_security_logout.jsp
        """
       
if __name__ == '__main__':
    unittest.main()