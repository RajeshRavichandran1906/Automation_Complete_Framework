'''
Created on Jun 26, 2019
@author: Aftab
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5852681
TestCase Name : After Deleting Field, label doen't remains in axis
'''

import unittest
from common.wftools.chart import Chart
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity

class C5852681_TestClass(BaseTestCase):

    def test_C5852681(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj= Chart(self.driver)
        util_obj=utillity.UtillityMethods(self.driver)

        """
            TESTCASE ID Variable 
        """
        format_css = "#FormatTab"
        querypane_css = "#queryBoxColumn"
        
        """       
        1 : Launch the IA API with Chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%253A%252FWFC%252FRepository%252FP309_S10666%252FG169735&tool=chart&master=ibisamp/car
        """
        chart_obj.invoke_chart_tool_using_api("ibisamp/car")
         
        """
        2 : Double click "COUNTRY", "DEALER_COST"
        """
        chart_obj.double_click_on_datetree_item('COUNTRY', 1)
        chart_obj.wait_for_visible_text(querypane_css,'COUNTRY')
        chart_obj.double_click_on_datetree_item('DEALER_COST', 1)
        chart_obj.wait_for_visible_text(querypane_css,'DEALER_COST')
              
        """
        3 : On the Format tab > Run With > Click "Insight "
        """
        chart_obj.select_ia_ribbon_item("Format", "run_with")
        chart_obj.wait_for_visible_text(format_css, "Run with")
        chart_obj.select_ia_ribbon_item("Format", "insight")
         
        """
        4 : Click Run
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
            
        """
        5 : Verify following insight chart displayed
        """
        chart_obj.verify_number_of_risers('#runbox_id rect', 1, 5, msg='Insight chart')
         
        """
        6 : Delete "DEALER_COST" from bucket shelf by click "x" on field
        """
        chart_obj.delete_field_in_query_bucket_container_in_insight('Vertical Axis', 'DEALER_COST')
        util_obj.synchronize_until_element_disappear("#runbox_id text[class='yaxis-title']", 9)
        
        """
        7 : Verify "DEALER_COST" removed from Vertical axis bucket as well as  text[class^='yaxis-labels']
        """
        chart_obj.verify_field_visible_in_query_bucket_container_in_insight('Vertical Axis', 'DEALER_COST', msg='Verify "DEALER_COST" removed from Vertical axis bucket',visible=False)
        actual_data_lables=len(self.driver.find_elements_by_css_selector("#runbox_id svg > g text[class^='yaxis-labels']"))
        util_obj.asequal(0, actual_data_lables, "Verify no y axis labels are displayed in run time")

        """
        8 : Click 'Reset' button
        """
        chart_obj.select_header_option_item_in_insight('reset')
        chart_obj.wait_for_visible_text('#runbox_id','COUNTRY')
         
        """
        9 : Now Delete "COUNTRY" from bucket shelf by click "x" on field
        """
        chart_obj.delete_field_in_query_bucket_container_in_insight('Group', 'COUNTRY')
        util_obj.synchronize_until_element_disappear('#runbox_id text[class="xaxisOrdinal-title"]', 9)
        
        """
        10 : Verify "COUNTRY" removed from Group bucket as well as label removed from X axis
        """
        chart_obj.verify_field_visible_in_query_bucket_container_in_insight('Group', 'COUNTRY', msg='Verify "COUNTRY" removed from Group bucket',visible=False)
        try:
            actual_data_lables=util_obj.validate_and_get_webdriver_object("#runbox_id svg > g text[class^='xaxis'][class*='labels']", 'x-axis label').text.strip()
        except AttributeError:
            actual_data_lables=''
        util_obj.asequal('', actual_data_lables, "Verify no x axis labels are displayed in run time")

        """
        11 : Click IA > Close > click No.
        """
        chart_obj.switch_to_default_content()
        chart_obj.close_ia_without_save()        
         
        """
        12 : Logout using API 
             http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()