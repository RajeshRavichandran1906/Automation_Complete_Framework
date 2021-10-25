'''
Created on May 17, 2019

@author: vpriya
Testcase Name : Export Data names works as Export Image
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262032
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.lib import utillity
from common.lib import core_utility
from common.locators import designer_chart_locators
import uiautomation as automation


class C8262032_TestClass(BaseTestCase):
    
    def test_C8262032(self):
        """
        Test case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        designer_insight_obj=designer_chart.Designer_Insight(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        designer_chart_locators_obj=designer_chart_locators.DesignerInsight()
        
        
        def verify_file_name_file_type(expected_file_name,expected_file_type):
            window_upload_ = automation.WindowControl(ClassName="#32770")
            save_dialog = window_upload_.EditControl(ClassName="Edit")
            save_dialog.Exists(maxSearchSeconds=29, searchIntervalSeconds=1)
            file_name=save_dialog.CurrentValue()
            file_type=window_upload_.ComboBoxControl(Name="Save as type:").AccessibleCurrentValue()
            utill_obj.asequal(file_name,expected_file_name,"File_name_Adhoc")
            utill_obj.asequal(file_type,expected_file_type,"File_type_xlsx")
            automation.WindowControl(ClassName="#32770").ButtonControl(Name="Cancel").DoubleClick()
        
        """
        Test case variables
        """
        x_axis_label_css="text[class*='xaxisOrdinal-labels!']"
        y_axis_label_css="text[class*='yaxis-labels!']"
        
        """
        Step 1: Launch the IA API with Chart (edit the domain, port and alias of the URL - do not use the URL as is):
        http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api('baseapp/wf_retail_lite')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)

 
        """
        Step 2:Add "Product, Category" and "Revenue"
        """
        designer_chart_obj.double_click_on_dimension_field('Product->Product->Product,Category')
        utill_obj.synchronize_with_number_of_element(x_axis_label_css,7,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.double_click_on_measures_field('Sales->Revenue')
        utill_obj.synchronize_with_number_of_element(y_axis_label_css,8,designer_chart_obj.home_page_long_timesleep)

 
        """
        Step 3:Click More > Select "Run with Insight"
        """
        designer_chart_obj.select_more_option("Run with Insight")

        """
        Step 4:Click Preview icon from the toolbar.
        """

        designer_chart_obj.click_toolbar_item("preview")
        core_utility_obj.switch_to_frame(designer_chart_locators_obj.INSIGHT_PREVIEW_FRAME)
        utill_obj.synchronize_until_element_is_visible(".more-options-button .ibx-glyph-ellipsis-v", designer_chart_obj.home_page_long_timesleep)
 
        """
        Step 5:Click on the "More Options" icon > Select "Export Data".

        Exported file name ADHOC.xlsx
        """
        designer_insight_obj.select_more_options_in_preview("Export Data")
        verify_file_name_file_type("ADHOC","Microsoft Excel Worksheet")
        automation.WindowControl(ClassName="#32770").ButtonControl(Name="Open", foundIndex=3).MoveCursor()
        automation.WindowControl(ClassName="#32770").ButtonControl(Name="Open", foundIndex=3).Click()
        
        """
        Step 6:Hover blue icon from the center of the chart > click Return button.
        """
        
        utill_obj.switch_to_main_window()
        core_utility_obj.switch_to_default_content()
        designer_chart_obj.go_back_to_design_from_preview()
        

        """
        Step 7:Click Save in the toolbar > Enter Title as "C8262032" > Click Save
        """
        designer_chart_obj.save_designer_chart_from_toolbar("C8262032")
 
        """
        Step 8:Logout using API

        http://machine:port/alias/service/wf_security_logout.jsp
        """
        
        designer_chart_obj.api_logout()

 
        """
        Step 9:Run the fex from domain tree using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://machine:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S28313%252FG671774%252F&BIP_item=c8262032.fex
        Expected to see insight chart
        """
        designer_chart_obj.run_designer_chart_using_api("c8262032")


        """
        Step 10:Click on the "More Options" icon > Select "Export Image"
        
        Image file named "C2509903_1.png" has been downloaded
        """
        utill_obj.synchronize_until_element_is_visible(".more-options-button .ibx-glyph-ellipsis-v", designer_chart_obj.home_page_long_timesleep)
        designer_insight_obj.select_more_options_in_preview("Export Image")
        automation.WindowControl(ClassName="#32770").ButtonControl(Name="Save").DoubleClick()

        """
        Step 11:Open "C2509903_1.png" in image viewer
        Interactive heading is replaced by a Static (non-interactive) heading.
        """


        """
        Step 12:Click on the "More Options" icon > Select "Export Data"

        Exported file name
        """


        """
        Step 13:Open the downloaded excel file
        The exported data.
        """


        """
        Step 14:Close excel
        """

 

 
        """
        Step 15:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """


if __name__ == '__main__':
    unittest.main()