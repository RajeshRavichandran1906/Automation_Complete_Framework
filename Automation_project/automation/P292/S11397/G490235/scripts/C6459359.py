'''
Created on Aug 23, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/11397
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6459359
TestCase Name = Add bin to horizontal axis
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,metadata
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart

class C6459359_TestClass(BaseTestCase):

    def test_C6459359(self):
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C6459359'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        chart = Chart(self.driver)
        
        """
            TESTCASE CSS
        """
        querytree_css = "#queryTreeColumn"
        
        """
        Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S11397%2FG490235&tool=chart&master=baseapp/wf_retail
        """
        utillobj.invoke_infoassist_api_login('chart','baseapp/wf_retail','P292_S11397/G490235', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Expand Product > Model > Attributes
        """
        metadataobj.collapse_data_field_section("Filters and Variables")
        time.sleep(3)
        metaobj.expand_field_tree('Product')
        time.sleep(2)
        metaobj.expand_field_tree('Product')
        time.sleep(2)
        metaobj.expand_field_tree('Model')
        time.sleep(2)
        metaobj.expand_field_tree('Attributes')
        time.sleep(6)
       
        """
        Step03: Right click Price,Dollars > Create Bin
        """ 
        metaobj.expand_field_tree('Price,Dollars', click_opt=1, x_offset=35)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Create Bins...')
        time.sleep(6)
        
        """
        Step04: Click Format
        Step05: Select Integer, select Use Comma, select Currency Symbol = Floating Currency > OK
        Step06: Change bin width to 100 > OK
        """ 
        bin_dialog="div[id^='QbDialog'] div[class*='bi-window active window']"
        resultobj.wait_for_property(bin_dialog, 1)
        metaobj.create_bin('PRICE_DOLLARS_BIN_1',bin_format_btn=True, field_type='Integer',check_box_list=['Use Comma (C)'], currency_symbol='Floating Currency', ok_btn=True, bin_width='100')
        
        """
        Step07: Verify Bin (PRICE_DOLLARS_BIN_1) added to data pane under "Product > Model > Attributes" (below Product, Weight,Units)
        """ 
        time.sleep(4)
        metaobj.verify_data_pane_field("Attributes", "PRICE_DOLLARS_BIN_1", 12, "Step 07: Verify the PRICE_DOLLARS_BIN_1 has been added to the Data pane")
        
        """
        Step08: Double click the bin to add to horizontal axis
        """ 
        metaobj.datatree_field_click('Dimensions->Product->Product->Model->Attributes->PRICE_DOLLARS_BIN_1', 2, 1)
        chart.wait_for_visible_text(querytree_css, "PRICE_DOLLARS_BIN_1")
        
        """
        Step09: Double click Quantity,Sold
        """
        chart.double_click_on_datetree_item("Quantity,Sold", 1)
        chart.wait_for_visible_text(querytree_css, "Quantity,Sold")
        
        """
        Step10: Verity the preview displayed with bin values
        """
        resultobj.verify_xaxis_title("TableChart_1", 'PRICE_DOLLARS_BIN_1', "Step10:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", 'Quantity Sold', "Step10:a(ii) Verify Y-Axis Title")
        expected_xval_list=['$0', '$100', '$200', '$300', '$400', '$500', '$600', '$700', '$800', '$900', '$1,100', '$1,200', '$1,300', '$1,900', '$2,200', '$3,300', '$3,400', '$3,900']
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 18, 'Step10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step10.c: Verify first bar color")
        time.sleep(5)
        
        """ 
        Step11: Click Save in the toolbar > Save as "C6459359" > Click Save    
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """ 
        Step12: Logout using API: http://machine:port/alias/service/wf_security_logout.jsp       
        """
        time.sleep(3)
        utillobj.infoassist_api_logout()
        
        """ 
        Step13: Run from bip: http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S11397%252FG490235%252F&BIP_item=C6459359.fex
        """
        time.sleep(2)
        utillobj.active_run_fex_api_login_(Test_Case_ID+'.fex','G490235','mrid','mrpass')
         
        """
        Step14: Verify run time chart displayed
        """
        parent_css="#jschart_HOLD_0 svg g text[class*='xaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 18)
        parent_css="#jschart_HOLD_0 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(5)
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'PRICE_DOLLARS_BIN_1', "Step14:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", 'Quantity Sold', "Step14:a(ii) Verify Y-Axis Title")
        expected_xval_list=['$0', '$100', '$200', '$300', '$400', '$500', '$600', '$700', '$800', '$900', '$1,100', '$1,200', '$1,300', '$1,900', '$2,200', '$3,300', '$3,400', '$3,900']
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step14:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 18, 'Step14.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step14.c: Verify first bar color")
        time.sleep(5)
         
        """
        Step15: Logout using API: http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()
