'''
Created on Jan 05, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349046
Test_Case Name : Group added to drill hierarchy above field of origin 2
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity

class C2349046_TestClass(BaseTestCase):

    def test_C2349046(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2349046'
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        
        def verify_bar_chart(xaxis_title, xaxis_label, yaxis_label, total_risers, step_num):
            visul_result.verify_xaxis_title('MAINTABLE_wbody1_f', xaxis_title, 'Step ' + step_num + '.1 : Verify X-Axis title')
            visul_result.verify_yaxis_title('MAINTABLE_wbody1_f', 'Cost of Goods', 'Step ' + step_num + '.2 : Verify Y-Axis title')
            visul_result.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f', xaxis_label, yaxis_label, 'Step ' + step_num + '.3 :', x_axis_label_length=25)
            visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, total_risers, 'Step ' + step_num + '.4 : Verify number of bar chart risers')
            utillobj.verify_chart_color('MAINTABLE_wbody1_f', 'riser!s0!g0!mbar!', 'lochmara', 'Step ' + step_num + '.5 : Verify bar chart riser color')
             
        """
            Step 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P312/S10664_paperclipping_2', 'mrid', 'mrpass')
        visul_result.wait_for_property("#pfjTableChart_1 svg text", 1, 120, string_value='DropMeasuresorSortsintotheQueryPane', with_regular_exprestion=True)
        time.sleep(3)
         
        """
            Step 02 : Double click "Cost of Goods", "Product, Subcategory"
        """
        metadata.datatree_field_click('Cost of Goods',2,1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='yaxis-title']", 1, 80, string_value='Cost of Goods')
        
        metadata.datatree_field_click('Product,Subcategory',2,1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='Product Subcategory')
        
        """
            Step 02.1 : Verify preview
        """
        expected_xaxis_labels=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M']
        verify_bar_chart('Product Subcategory', expected_xaxis_labels, expected_yaxis_labels, 21, '02')
    
        """
            Step 03 : Lasso "Boom Box to DVD Players" risers
            Step 04 : Select "Group Product, Subcategory selection"
        """
        visul_result.create_lasso('MAINTABLE_wbody1_f', 'rect', 'riser!s0!g1!mbar!', target_tag='rect', target_riser='riser!s0!g4!mbar!')
        expected_lasso=['4 points', 'Filter Chart', 'Exclude from Chart', 'Group Product,Subcategory Selection']
        visul_result.select_or_verify_lasso_filter(verify=expected_lasso, msg='Step 04.1 : Verify lasso values', select='Group Product,Subcategory Selection')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='PRODUCT_SUBCATEG_1')
        
        """
            Step 05 : Verify following preview displayed
        """
        expected_xaxis_labels=['Blu Ray', 'Boom Box and CRT TV and Charger a...', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        verify_bar_chart('PRODUCT_SUBCATEG_1', expected_xaxis_labels, expected_yaxis_labels, 18, '05')
        
        """
            Step 06 : Click Run
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='PRODUCT_SUBCATEG_1')
        
        """
            Step 06.1 : Verify output in Run window
        """ 
        verify_bar_chart('PRODUCT_SUBCATEG_1', expected_xaxis_labels, expected_yaxis_labels, 18, '06')
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_06', 'actual')
        
        """
            Step 07 : Hover over " "Boom Box and CRT TV and CHARGER and..." group value riser
            Step 08 : Select Drill up to Product Category
        """
        expected_tooltip=['PRODUCT_SUBCATEG_1:Boom Box and CRT TV and Charger and 1 more', 'Cost of Goods:$8,577,754.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Product Subcategory']
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s0!g1!mbar!', expected_tooltip, 'Step 08.1 : Verify tooltip')
        time.sleep(3)
        visul_result.select_default_tooltip_menu('MAINTABLE_wbody1_f', 'riser!s0!g1!mbar!', 'Drill up to Product Category')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='Product Category')
        
        """
            Step 08.1 : Verify chart output 
        """
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        verify_bar_chart('Product Category', expected_xaxis_labels, expected_yaxis_labels, 7, '08')
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_08', 'actual')
        
        """
            Step 09 : Hover over any riser (Ex. Camcorder)
            Step 10 : Verify "Drill down to PRODUCT_SUBCATEG_1" is the only drill option in tooltip
        """
        expected_tooltip=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to PRODUCT_SUBCATEG_1']
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s0!g1!mbar!', expected_tooltip, 'Step 10.1 : Verify "Drill down to PRODUCT_SUBCATEG_1" is the only drill option in tooltip')
        
        """
            Step 11 : Close run window
        """
        self.driver.close()
        utillobj.switch_to_window(0)
        
        """
            Step 12 : Delete "PRODUCT_SUBCATEG_1" from query pane, add "Product,Subcategory"
        """
        metadata.querytree_field_click('PRODUCT_SUBCATEG_1', 1, 1, 'Delete')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg text[class='yaxis-labels!m8!']", 1, 80, string_value='800M')
        
        metadata.datatree_field_click('Product,Subcategory',2,1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='Product Subcategory')
        
        """
            Step 13 : Run again
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='Product Subcategory')
        
        """
            Step 13.1 : Verify chart output in run window
        """
        expected_xaxis_labels=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M']
        verify_bar_chart('Product Subcategory', expected_xaxis_labels, expected_yaxis_labels, 21, '13')
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_13', 'actual')
        
        """
            Step 14 : Hover over any riser (Ex.,Speaker Kits)
            Step 15 : Verify tooltip shows "Drill Up option to PRODUCT_SUBCATEG_1" and "Drill down to Model"
        """
        expected_tooltip=['Product Subcategory:Speaker Kits', 'Cost of Goods:$81,396,140.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to PRODUCT_SUBCATEG_1', 'Drill down to Model']
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s0!g14!mbar!', expected_tooltip, 'Step 15.1 : Verify tooltip shows "Drill Up option to PRODUCT_SUBCATEG_1" and "Drill down to Model"')
        
        """
            Step 16 : Close run window
        """
        self.driver.close()
        utillobj.switch_to_window(0)
        
        """
            Step 17 : Click Save in the toolbar > Save as "C2349046" > Click Save
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 18 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()