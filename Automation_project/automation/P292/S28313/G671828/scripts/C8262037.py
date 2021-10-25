'''
Created on september 7 ,2018

@author: vishnu_priya.
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer_chart import Designer_Chart
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib import utillity
from common.lib import core_utility
from common.wftools import chart
from common.locators.designer_chart_locators import DesignerChart as dc_locators

class C8262037_TestClass(BaseTestCase):
    
    def test_C8262037(self):
        """
        TESTCASE VARIABLES
        """
        
        utillobj = utillity.UtillityMethods(self.driver)
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        chart_obj = chart.Chart(self.driver)
        designer_chart_obj=Designer_Chart(self.driver)
        project_id=core_utill_obj.parseinitfile('project_id')
        suite_id = core_utill_obj.parseinitfile('suite_id')
        group_id = core_utill_obj.parseinitfile('group_id')
        folder_name = project_id+'_'+suite_id+'/'+group_id
        main_page = Wf_Mainpage(self.driver)
        
        """
        Step 1:Launch the API to create new Designer Chart with the Car file
        http://machine:port/{alias}/designer?&item=IBFS:/WFC/Repository/P292_S28313/G671774&master=ibisamp/car&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api("ibisamp/car", mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_until_element_is_visible(dc_locators.DIMENSIONS_FIELD_AREA_CSS,designer_chart_obj.chart_long_timesleep)
        utillobj.verify_object_visible(".chart-picker-box",True,"Step 01:01 verify the chart picker icon")
        utillobj.verify_object_visible(".pop-top",False,"Step 01:02 Verify the chart opens without any error")
 
        """
        Step 2:Double click "COUNTRY" and "DEALER_COST"
        """
         
        designer_chart_obj.double_click_on_dimension_field('COUNTRY')
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box","COUNTRY",designer_chart_obj.home_page_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('COMP->CARREC->BODY->DEALER_COST')
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box","DEALER_COST",designer_chart_obj.home_page_medium_timesleep)
         
        """
        Step 3:Right click "DEALER_COST" > Aggregate > "Percent of Count"
        """
        designer_chart_obj.select_query_bucket_field_context_menu('Vertical', 'DEALER_COST','Aggregate->Percent of count')
        time.sleep(2)
        utillobj.synchronize_with_visble_text(".wfc-bucket-display-box","PCT.CNT.DEALER_COST",designer_chart_obj.home_page_medium_timesleep)
  
        """
        Step 4:Right click PCT.CNT.DEALER_COST > "Format Data"
        """
        designer_chart_obj.select_query_bucket_field_context_menu('Vertical', 'PCT.CNT.DEALER_COST','Format data')
        utillobj.synchronize_until_element_is_visible(".dataformat-dlg-menu-item",designer_chart_obj.home_page_short_timesleep)
        percentage_css = ".dataformat-dlg-menu-item [data-ibxp-user-value='percentage']"
        perc_elem = utillobj.validate_and_get_webdriver_object(percentage_css,"percentage_css")
        core_utill_obj.left_click(perc_elem)
        time.sleep(4)
  
        """
        Step 5:Select Percent(%) > click Ok.
        """
        main_page.click_button_on_popup_dialog("OK")
         
        """
        Step 6:Verify chart in canvas .
        """
        time.sleep(2)
        designer_chart_obj.verify_y_axis_title_in_preview(['PCT.CNT DEALER_COST'],msg="step:06")
         
        """
        Step 7:Click Run.
        """
        designer_chart_obj.click_toolbar_item("preview")
  
        """
        Step 8:Verify chart and hover over chart display values with % symbol.
        """
         
        core_utill_obj.switch_to_frame("iframe[src*='TableChart_1']")
        utillobj.synchronize_until_element_is_visible("#jschart_HOLD_0 [class='riser!s0!g2!mbar!']",designer_chart_obj.home_page_long_timesleep)
        chart_obj.verify_tooltip_in_run_window('riser!s0!g2!mbar!',['COUNTRY:ITALY', 'PCT.CNT DEALER_COST:22%'], msg="Step08:")
        """
        Step 9:Click save > type "C8262037" > save.
        """
        core_utill_obj.switch_to_default_content()
        designer_chart_obj.go_back_to_design_from_preview()
        designer_chart_obj.save_as_from_application_menu('C8262037')
 
        """
        Step 10:Launch the IA API to logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()

        """
        Step 11:Run C8262037.fex from BIP.
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%2P292_S28313%2FG671774 &BIP_item=C8262037.fex
        """
        chart_obj.run_fex_using_api_url(folder_name, 'c8262037', "mrid", "mrpass")
        utillobj.synchronize_until_element_is_visible("#jschart_HOLD_0 [class='riser!s0!g2!mbar!']",designer_chart_obj.home_page_long_timesleep)
 
        """
        Step 12:Verify chart and hover over chart display values with % symbol.
        """
        chart_obj.verify_tooltip_in_run_window('riser!s0!g2!mbar!',['COUNTRY:ITALY', 'PCT.CNT DEALER_COST:22%'], msg="Step08:")
        designer_chart_obj.api_logout()

        """
        Step 13:Launch the API with Designer in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%2Fc8262037.fex
        """
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api('c8262037', mrid='mrid', mrpass='mrpass', folder_path=folder_name)
        utillobj.synchronize_until_element_is_visible(dc_locators.DIMENSIONS_FIELD_AREA_CSS,designer_chart_obj.chart_long_timesleep)
        utillobj.verify_object_visible(".chart-picker-box",True,"Step 01:01 verify the chart picker icon")
        utillobj.verify_object_visible(".pop-top",False,"Step 01:02 Verify the chart opens without any error")
 
        """
        Step 14:Verify chart preview.
        """
        designer_chart_obj.verify_y_axis_title_in_preview(['PCT.CNT DEALER_COST'],msg="step:06")


        """
        step 15:close the output window
        """
        designer_chart_obj.api_logout()

        """
        Step 16:Launch the IA API to logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

 

 
    if __name__ == "__main__":
        unittest.main()