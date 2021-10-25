'''
Created on Feb 08, 2018

@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348446
Test_Case Name : If bin field added to Color in Pie it is treated as BY

'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages.ia_resultarea import IA_Resultarea
from common.wftools.visualization import Visualization

class C2348446_TestClass(BaseTestCase):

    def test_C2348446(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2348446'
        visual=Visualization(self.driver)
        ia_rsultobj= IA_Resultarea(self.driver)
    
        """
            Step 01 :Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 12, 50)
        
        """
            Step 02: Click Change drop down > Select Pie chart
        """
        visual.change_chart_type('pie')
        visual.wait_for_visible_text("#TableChart_1 svg g text.title", 'DropMeasuresorSortsintotheQueryPane',20)
        
        """
            Step 03:Right click on "Quantity, Sold" > Create Bins...
        """
        visual.right_click_on_datetree_item('Quantity,Sold', 1,'Create Bins...')
        
        """
            Step 04:Set Width of bins = 1
            Step 05:Click OK
        """
#         visual.create_bins(bin_width=1,btn_click='OK')
        visual.create_bins("QUANTITY_SOLD_BIN_1", name_textbox_value="QUANTITY_SOLD_BIN_1", format_textbox_value="I11C",bin_width='1', btn_click='OK')
        
        """
            Step 06:Double click "QUANTITY_SOLD_BIN_1" bin
        """
        visual.double_click_on_datetree_item('Dimensions->QUANTITY_SOLD_BIN_1', 1)
        
        """
            Step 07:Add "Quantity, Sold" measure bucket
        """
        
        visual.double_click_on_datetree_item('Quantity,Sold', 1)
        
        """
            Step 08:Verify following preview displayed 4 Slices displayed
        """
        
        visual.verify_legends(['QUANTITY_SOLD_BIN_1', '1', '2', '3', '4'], msg='Step 8.1')
        visual.verify_chart_color_using_get_css_property("path[class='riser!s0!g0!mwedge!']", 'bar_blue',  msg='Step 8.2')
        visual.verify_number_of_pie_segments("#MAINTABLE_wbody1_f", 1, 4, 'Step 8.3: Verify tooltip values')
        visual.take_preview_snapshot(Test_Case_ID, '08.4')
        
        """
            Step 09:Click view source icon to view fex code generated
            Step 10:Close view source code window
        """
        expcted_syntax=["SUM WF_RETAIL_LITE.WF_RETAIL_SALES.QUANTITY_SOLD", "BY QUANTITY_SOLD_BIN_1", "TYPE=DATA, COLUMN=N1, BUCKET=color, $"]
#         visual.verify_fexcode_syntax(expcted_syntax, 'Step 10: Verify FST.QUANTITY_SOLD_BIN_1 added under Measure')
#         the above line makes time out error so using below function from ia_resultarea.py
        ia_rsultobj.verify_fexcode_syntax(expcted_syntax, 'Step 10: Verify FST.QUANTITY_SOLD_BIN_1 added under Measure')
        
        """
            Step 11:Hover on the preview chart and verify tool tip values
        """
        expected_tooltip=['QUANTITY_SOLD_BIN_1:4', 'Quantity Sold:99,944  (2.85%)', 'Filter Chart', 'Exclude from Chart']
        visual.verify_tooltip('riser!s3!g0!mwedge!', expected_tooltip, 'Step 11.1 : Verify tooltip values',element_location='top_middle',yoffset=30)
        
        """
            Step 12:Click Save in the toolbar > Save as "C2348446" > Click Save
        """
        
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
            Step 13:Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """                        
        visual.logout_visualization_using_api()
        
        """
            Step 14:Run the fex from treehttp://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10664&BIP_item=C2348446.fex
        """
        
        visual.run_visualization_using_api("C2348446.fex")
        visual.verify_legends(['QUANTITY_SOLD_BIN_1', '1', '2', '3', '4'], msg='Step 14.1')
        visual.verify_chart_color_using_get_css_property("path[class='riser!s0!g0!mwedge!']", 'bar_blue',  msg='Step 14.2')
        visual.verify_number_of_pie_segments("#MAINTABLE_wbody1_f", 1, 4, 'Step 14.3: Verify tooltip values')
                
        """
            Step 15:Hover on the run time chart and verify tool tip values
        """
        
        expected_tooltip=['QUANTITY_SOLD_BIN_1:2', 'Quantity Sold:1,493,612  (42.55%)', 'Filter Chart', 'Exclude from Chart']
        visual.verify_tooltip('riser!s1!g0!mwedge!', expected_tooltip, 'Step 15.1 : Verify tooltip values')
        
        """
            Step 16:Hover on the run time chart and verify tool tip values
        """
        
        visual.logout_visualization_using_api()
        
        """
            Step 17:Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348446.fex
        """
        
        visual.edit_visualization_using_api(Test_Case_ID)
        time.sleep(10)
        visual.verify_legends(['QUANTITY_SOLD_BIN_1', '1', '2', '3', '4'], msg='Step 17.1')
        visual.verify_chart_color_using_get_css_property("path[class='riser!s0!g0!mwedge!']", 'bar_blue',  msg='Step 17.2')
        visual.verify_number_of_pie_segments("#MAINTABLE_wbody1_f", 1, 4, 'Step 17.3: Verify number of Pie chart segments.')
        """
            Step 18:Logout using API  http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
if __name__ == "__main__":
    unittest.main()        