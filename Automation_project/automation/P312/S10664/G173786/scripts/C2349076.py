'''
Created on Feb 2, 2018

@author: Vinitha

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349076
Test_Case Name : Undo delete Group from query
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2349076_TestClass(BaseTestCase):

    def test_C2349076(self):
        
        Test_Case_ID = "C2349076"
        visualobj = visualization.Visualization(self.driver)
        
        def verify(xval_list, yval_list, number_of_riser, bar_color, yaxis_title, bar, step):
            visualobj.verify_x_axis_label(xval_list, msg="Step " + str(step) + ".a")
            visualobj.verify_y_axis_label(yval_list, msg="Step " + str(step) + ".b")
            visualobj.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, number_of_riser, msg="Step " + str(step) + ".c")        
            visualobj.verify_chart_color_using_get_css_property("rect[class*='riser!s0!g0!mbar']", bar_color, msg="Step " + str(step) + ".d")                           
            visualobj.verify_y_axis_title(yaxis_title, msg="Step " + str(step) + ".f")                                    
            visualobj.verify_tooltip('riser!s0!g0!mbar', bar, "Step " + str(step) + ".g : Verify riser values")
            
        """
        Step1: Restore saved fex using API (edit the domain, port and alias 
        of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349075.fex
        """
        visualobj.edit_visualization_using_api("C2349075")
        visualobj.wait_for_number_of_element("#metaDataSearchTxtFld", 1)
        xval_list = [""]
        yval_list = ["0", "0.2B", "0.4B", "0.6B", "0.8B", "1B", "1.2B"]
        yaxis_title = ["Revenue"]
        bar= ["Revenue:$1,061,192,925.21"]
        visualobj.wait_for_number_of_element("#MAINTABLE_wbody1_f svg > g text[class^='xaxis'][class*='labels']", 1, 30)
        """
        Step2: Right click "PRODUCT_CATEGORY_1" group from Data pane >
        Step3: Click "Delete"
        """
        visualobj.wait_for_number_of_element("#metaDataSearchTxtFld", 1, 30)        
        visualobj.right_click_on_datetree_item("Dimensions->PRODUCT_CATEGORY_1",1,'Delete')      
        
        """
        Step4: Verify "PRODUCT_CATEGORY_1" group deleted from data pane
        """
        visualobj.verify_field_listed_under_datatree("Dimensions", " ", 6, "Step04: Verify data tree")
        visualobj.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 1, 30)
        verify(xval_list, yval_list, 1, "bar_blue",  yaxis_title, bar, 4)
         
        """
        Step5: Click Undo button in tool bar menu
        """
        visualobj.select_item_in_top_toolbar("undo")
         
        """
        Step6: Verify Group is returned to data pane
        """
        visualobj.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 1, 30)
        visualobj.verify_field_listed_under_datatree("Dimensions", "PRODUCT_CATEGORY_1", 6, "Step06: Verify data tree")
        
        """
        Step7: Click Redo
        """
        visualobj.wait_for_number_of_element("#topToolBar #redoButton img", 1, 30)
        visualobj.select_item_in_top_toolbar("redo")
         
        """
        Step8: Verify "PRODUCT_CATEGORY_1" group deleted from data pane
        """
        visualobj.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 1, 30)
        visualobj.verify_field_listed_under_datatree("Dimensions", " ", 6, "Step08: Verify data tree")       
         
        visualobj.take_preview_snapshot(Test_Case_ID ,'08')
         
        """
        Click IA > Save as "C2349076" > Click Save
        """
        visualobj.save_as_visualization_from_menubar(Test_Case_ID)
         
        """
        Step09: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visualobj.logout_visualization_using_api()

if __name__ == '__main__':
    unittest.main()        
