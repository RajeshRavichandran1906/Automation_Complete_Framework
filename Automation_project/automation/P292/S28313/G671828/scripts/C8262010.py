'''
Created on July 24, 2019

@author: Vpriya

Test Case : http://172.19.2.180/testrail/index.php?/cases/view/8262010
TestCase Name : Verify Streamgraph using Join field
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer_chart import Designer_Chart
from common.lib.utillity import UtillityMethods
from common.wftools.designer import joining_data
from common.locators.designer_chart_locators import DesignerChart as dc_locators

class C8262010_TestClass(BaseTestCase):

    def test_C8262010(self):
        """
            CLASS OBJECTS 
        """
        designer_chart_obj=Designer_Chart(self.driver)
        utils=UtillityMethods(self.driver)
        joining_data_obj=joining_data.Joining_Data(self.driver)
        
        """
            TESTCASE CSS 
        """
        
        DATA_TAB_CSS ="[role='tablist'] .wb-data-tab-button"
        QUERY_BOX_CSS = ".wfc-bucket-display-box"
        RUN_PARENT_CSS = '#jschart_HOLD_0'
        
        
        """
            TESTCASE ID Variable 
        """
        
        """
        JOIN_1 variables
        """

        
        """
        STEP 1:Launch the API to create new Designer chart with wf_retail_sales master file as developer user:
  
        http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29835%2FG728361%2F&master=baseapp%2Ffacts%2Fwf_retail_sales&tool=chart
  
        Designer chart created without error and Dimensions tree is empty.
          
        """
          
        designer_chart_obj.invoke_designer_chart_using_api("ibisamp/empdata", mrid='mrid', mrpass='mrpass')
        utils.synchronize_until_element_is_visible(dc_locators.DIMENSIONS_FIELD_AREA_CSS,designer_chart_obj.chart_long_timesleep)
        utils.verify_object_visible(".chart-picker-box",True,"Step 01:01 verify the chart picker icon")
        utils.verify_object_visible(".pop-top",False,"Step 01:02 Verify the chart opens without any error")
          
        """
        Select "Streamgraph" from Business chart picker component.
        """
        designer_chart_obj.select_chart_from_chart_picker('streamgraph',expand=True)
          
        """
        Step 3:Select Data tab in Designer.
        """
        designer_chart_obj.select_tab_button("Data")
        
        """
        Step 4:Drag and drop "training.mas" file over "empdata.mas" to create new join.
        Verify new Join 1 created.
        """
        joining_data_obj.switch_to_frame()
        joining_data_obj.resource_tree(['training']).drag_to_canvas('empdata')
        
        """
        Step 5:Select Chart 1 tab in Designer.
        """
        """
        Step 6:Double click "LASTNAME", "SALARY", "EXPENSES".
        """
        """
        Step 7:Verify the following chart displayed.
        """
        """
        Step 8:Click "Run".
        """
        """
        Step 9:Verify the same chart is displayed at run time.
        """
        """
        Step 10: Click Save in the toolbar > Save as "C8262010" > Click Save
        """
        """
        Step 11: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        """
        Step 12:Run C8261996.fex from BIP.
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%2P292_S28313%2FG671774 &BIP_item=c8262010.fex
        """
        """
        Step 13:Verify the Streamgraph is run in a new window.
        """
        """
        Step 14:Hover over on chart and verify tooltip values
        """
        """
        Step1 5:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        """
        Step 16:Launch the API with Designer in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%2Fc8262010.fex
        """
        """
        Step 17:Verify IA is launched preserving the Streamgraph in "Live Preview".
        """

        """
        Step 18:Log out WF using API:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

        
if __name__ == '__main__':
    unittest.main()