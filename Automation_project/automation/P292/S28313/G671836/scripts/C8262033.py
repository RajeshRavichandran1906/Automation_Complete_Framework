'''
Created on May 17, 2019

@author: vpriya
Testcase Name : Verify saving a procedure from Insight
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8262033
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.lib import utillity
from common.lib import core_utility
from common.locators import designer_chart_locators
from common.lib.webfocus.resource_dialog import Resource_Dialog
from common.wftools import login
from common.wftools import wf_mainpage

class C8262033_TestClass(BaseTestCase):
    
    def test_C8262033(self):
        """
        Test case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        designer_insight_obj=designer_chart.Designer_Insight(self.driver)
        login_obj = login.Login(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        designer_chart_locators_obj=designer_chart_locators.DesignerInsight()
        Resource_Dialog_obj=Resource_Dialog(self.driver)
        wf_mainpage_obj=wf_mainpage.Wf_Mainpage(self.driver)
        
        """
        Test case variables
        """
        x_axis_label_css="text[class*='xaxisOrdinal-labels!']"
        y_axis_label_css="text[class*='yaxis-labels!']"
        Ring_label_css="text[class*='totalLabel!']"
        ring_pie_css=".file-item [src$='pie_ring.svg ']"
        
        """
        Step 1: Launch the IA API with Chart (edit the domain, port and alias of the URL - do not use the URL as is):
        http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api('baseapp/wf_retail_lite')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
 
  
        """
        Step 2:Add "Product, Category" and "Cost of Goods""
        """
        designer_chart_obj.double_click_on_dimension_field('Product->Product->Product,Category')
        utill_obj.synchronize_with_number_of_element(x_axis_label_css,7,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.double_click_on_measures_field('Sales->Cost of Goods')
        utill_obj.synchronize_with_number_of_element(y_axis_label_css,7,designer_chart_obj.home_page_long_timesleep)
 
  
        """
        Step 3:Click More > Select "Run with Insight"
        """
        designer_chart_obj.select_more_option("Run with Insight")
 
        """
        Step 4:Click Preview icon from the toolbar.
        Insight does not display a Save button when run inside Designer.
        """
 
        designer_chart_obj.click_toolbar_item("preview")
        core_utility_obj.switch_to_frame(designer_chart_locators_obj.INSIGHT_PREVIEW_FRAME)
        utill_obj.synchronize_until_element_is_visible(".more-options-button .ibx-glyph-ellipsis-v", designer_chart_obj.home_page_long_timesleep)
        designer_insight_obj.verify_insight_optionsbox_text(['Save'], "Step 04:Insight does not display a Save button when run inside Designer", compare_type='asnotin')
        core_utility_obj.switch_to_default_content()
         
        """
        Step 5:Hover blue icon from the center of the chart > click Return button.
        """
        designer_chart_obj.go_back_to_design_from_preview()
  
        """
        Step 6:Click on Save button in the toolbar > Enter Title as "C8262033" > Save
        """
        designer_chart_obj.save_designer_chart_from_toolbar("c8262033")
  
        """
        Step 7:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
 
        """
        Step 8:Sign in to WF:
        http://machine:port/ibi_apps/
        """
        """
        Step 9:Run the fex from domain tree using API (edit the domain, port and alias of the URL - do not use the URL as is):
         
        http://machine:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S28313%252FG671774%252F&BIP_item=c8262033.fex
         
        "Save" button is displayed
        """
        designer_chart_obj.run_designer_chart_using_api("c8262033")
        utill_obj.synchronize_until_element_is_visible(".more-options-button .ibx-glyph-ellipsis-v", designer_chart_obj.home_page_long_timesleep)
        designer_insight_obj.verify_insight_optionsbox_text(['Save'], "Step 04:Insight does not display a Save button when run inside Designer", compare_type='asin')
         
        """
        Step 10:Click Change Chart > Select Ring Pie
         
        Ring Pie chart has been changed.
        """
        designer_insight_obj.select_chart_from_chartpicker("Ring Pie")
        utill_obj.synchronize_with_visble_text(Ring_label_css, "761.4M",designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_legends_in_preview(['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], ".legend-clip", 8, "Step 10 verify legends in preview")
        designer_chart_obj.verify_number_of_risers(".chartPanel path",1, 7, "Step 10:01 verify the number of risiers")
         
 
        """
        Step 11:Click on "Save" button
        """
         
        designer_insight_obj.select_insight_optionsbox_in_preview('Save')
 
        """
        Step 12:Save as dialog is displayed
        """
        """
        Step 13:In the Title input box, type "C8262033_Insight" > Click "Save as".
        """
        Resource_Dialog_obj.set_title_text("C8262033_Insight")
        button_obj=Resource_Dialog_obj.get_button_object("Save as")
        core_utility_obj.python_left_click(button_obj)
  
        """
        Step 14:Close the Insight window
        C2511645_Insight appears in the My Content Area (area is automatically refreshed)
        Thumbnail displays a Ring Pie image
        Fex displays the Insight icon to the left of the fex name
        """
        designer_chart_obj.api_logout()
        login_obj.invoke_home_page('mrid', 'mrpass')
        wf_mainpage_obj.expand_repository_folder('P292_S28313->My Content')
        wf_mainpage_obj.verify_item_icon_in_content_area("C8262033_Insight", "insight", '14')
        utill_obj.verify_object_visible(ring_pie_css,True,"Step:15")
        

        """
        Step 15:Run the fex from domain tree using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://machine:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S28313%252F&BIP_item=c8262033_Insight.fex
        Insight is displayed with the saved Ring Pie chart.
        """
        designer_chart_obj.api_logout()
        designer_chart_obj.run_insight_procedure_fex_using_api("c8262033_insight")
        utill_obj.synchronize_with_visble_text(Ring_label_css, "761.4M",designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_legends_in_preview(['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], ".legend-clip", 8, "Step 10 verify legends in preview")
        designer_chart_obj.verify_number_of_risers(".chartPanel path",1, 7, "Step 10:01 verify the number of risiers")

        """
        Step 17:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """


if __name__ == '__main__':
    unittest.main()