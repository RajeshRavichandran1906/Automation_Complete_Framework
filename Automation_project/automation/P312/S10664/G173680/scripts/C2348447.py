'''
Created on Jan 26, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348447
Test_Case Name : If bin field added to BLA Tooltip it is treated as the measure
Preconditions : Continue from C2348445
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages.ia_resultarea import IA_Resultarea
from common.wftools.visualization import Visualization

class C2348447_TestClass(BaseTestCase):

    def test_C2348447(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2348447'
        
        """
            CLASS OBJECTS
        """
        visual= Visualization(self.driver)
        ia_rsultobj= IA_Resultarea(self.driver)
        
        def verify_area_chart(yaxis_title, yaxis_labels, total_risers, step_num):
            visual.verify_x_axis_title(['Product Category'], msg='Step '+step_num+'.1')
            visual.verify_y_axis_title(yaxis_title, msg='Step '+step_num+'.2')
            visual.verify_x_axis_label(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg='Step '+step_num+'.3')
            visual.verify_y_axis_label(yaxis_labels, msg='Step '+step_num+'.4')
            visual.verify_number_of_risers("#MAINTABLE_wbody1_f svg path[class*='marea']", 1, total_risers, msg='Step '+step_num+'.5')
            visual.verify_chart_color_using_get_css_property("path[class='riser!s0!g0!marea!']", 'lochmara',  msg='Step '+step_num+'.6 ')
#             visual.take_preview_snapshot(Test_Case_ID, step_num)
        
        """
            Step 01 : Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10666%2FC2348445.fex
        """
        visual.edit_visualization_using_api('C2348447_Base')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f svg text[class='yaxis-title']", 'Quantity Sold', 90)
        time.sleep(12)
        
        """
            Step 01.1 : Verify preview
        """
        expected_yaxis_labels=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        verify_area_chart(['Quantity Sold'], expected_yaxis_labels, 4, '01')
        visual.verify_legends(['QUANTITY_SOLD_BIN_1', '1', '2', '3', '4'], msg='Step 01.7')
         
        """
            Step 02 : Drag and drop "QUANTITY_SOLD_BIN_1" from Color to tool tip bucket
        """
        visual.drag_field_within_query_pane('QUANTITY_SOLD_BIN_1', 'Tooltip')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f svg text[class='yaxis-labels!m4!']", '1.2M', 40)
        
        """
            Step 03 : Verify bin added to tool tip bucket and preview updated
        """
        expected_yaxis_labels=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        verify_area_chart(['Quantity Sold'], expected_yaxis_labels, 1, '03')
        visual.verify_field_listed_under_querytree('Tooltip', 'FST.QUANTITY_SOLD_BIN_1', 1, 'Step 03.7 ')
        
        """
            Step 04 : Click view source icon to view fex code generated
            FST.QUANTITY_SOLD_BIN_1 added under Measure
            Step 05 : Close view source code window
        """
        expcted_syntax=["SUM WF_RETAIL_LITE.WF_RETAIL_SALES.QUANTITY_SOLD", "FST.QUANTITY_SOLD_BIN_1", "BY WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY", "TYPE=DATA, COLUMN=N3, BUCKET=tooltip, $"]
#         visual.verify_fexcode_syntax(expcted_syntax, 'Step 04.1 : Verify FST.QUANTITY_SOLD_BIN_1 added under Measure')
#         the above line makes time out error so using below function from ia_resultarea.py
        ia_rsultobj.verify_fexcode_syntax(expcted_syntax, 'Step 04.1 : Verify FST.QUANTITY_SOLD_BIN_1 added under Measure')
        
        """
            Step 06 : Right click on "Quantity, Sold" query pane > More > Aggregation Functions > First Value 
        """
        visual.right_click_on_field_under_query_tree('Quantity,Sold', 0, 'More->Aggregation Functions->First Value')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f svg text[class='yaxis-labels!m7!']", '3.5', 120)
        
        """
            Step 07 : Verify following preview updated
        """
        expected_yaxis_labels=['0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5']
        verify_area_chart(['FST Quantity Sold'], expected_yaxis_labels, 1, '07')
        
        """
            Step 08 : Hover on the preview chart and verify tool tip values
            Quantity,Sold and QUANTITY_SOLD_BIN_1 show the same values.
        """
        expected_tooltip=['Product Category:Computers', 'FST Quantity Sold:3', 'FST QUANTITY_SOLD_BIN_1:3', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_tooltip("marker!s0!g2!mmarker", expected_tooltip, 'Step 08.9 : Verify Quantity,Sold and QUANTITY_SOLD_BIN_1 show the same values.', use_marker_enable=True)
        
        """
            Step 09 : Click IA > Save as "C2348447" > Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
            Step 10 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
            Step 11 : Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348447.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f svg text[class='yaxis-labels!m7!']", '3.5', 120)
        
        expected_yaxis_labels=['0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5']
        verify_area_chart(['FST Quantity Sold'], expected_yaxis_labels, 1, '11')
        
        """
            Step 12 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()

if __name__=='__main__' :
    unittest.main()