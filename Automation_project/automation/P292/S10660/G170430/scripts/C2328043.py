'''
Created on Nov 1, 2017

@author: BM13368
Testcase_Name : PCT.CNT as aggregation option for dimension (char) fields in IA+
Testcase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2328043&group_by=cases:section_id&group_id=170430&group_order=asc
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_metadata, visualization_ribbon
from common.lib import utillity

class C2328043_TestClass(BaseTestCase):

    def test_C2328043(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2328043'
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        
        """
            Step 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=chart&master=wf_retail_lite
        """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10660_chart_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        
        """
            Step 02 : Double click "Product, Category" to Horizontal axis
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(3)
        
        """
            Step 03 : Drag and drop "Model" to Vertical Axis
        """
        metaobj.datatree_field_click('Model', 1, 0, 'Add To Query','Vertical Axis')
        time.sleep(3)
        
        """
            Step 04 : Verify in query pane Vertical axis CNT prefix added to "Model" field and displayed same in preview
            Verification : Expected to see "CNT.Model"
        """
        metaobj.verify_query_pane_field("Vertical Axis", "CNT.Model", 1, 'Step 04 :01: Verify in query pane Vertical axis CNT prefix added to "Model" field')
        """
            Step 05 : Right click on "CNT.Model" > More >Aggregations functions (pull right)
        """
        metaobj.querytree_field_click('CNT.Model', 1, 1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('More')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Aggregation Functions')
        time.sleep(0.5)
                
        """
            Step 06 : Verify the list of options
            Verification : Count (grey dot)
            Count Distinct
            Percent of Count
        """
        utillobj.select_or_verify_bipop_menu(verify='true', expected_popup_list=['Count', 'Count Distinct', 'Percent of Count'], expected_ticked_list=['Count'], msg='Step 06:01 Verify popup menu')
        time.sleep(2)
        
        """
            Step 07 : Click "Percent of Count" option
        """
        utillobj.select_or_verify_bipop_menu('Percent of Count')
        time.sleep(2)
        """
            Step 08 : Verify query pane and preview updated with "PCT.CNT.Model" aggregation function
        """
        metaobj.verify_query_pane_field("Vertical Axis", "PCT.CNT.Model", 1, 'Step 08 :01: Verify in query pane Vertical axis PCT.CNT prefix added to "Model" field')
        """
            Step 09 : Right Click "PCT.CNT.Model" > More >Aggregations functions (pull right)
        """
        metaobj.querytree_field_click('PCT.CNT.Model', 1, 1)
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu('More')
        time.sleep(0.5)
        utillobj.select_or_verify_bipop_menu('Aggregation Functions')
        time.sleep(0.5)
        
        """
            Step 10 : Verify "Percent of Count" option is selected (grey dot)
            Step 11 : Click OK
        """
        a=['Count','Count Distinct','Percent of Count']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a,expected_ticked_list=['Percent of Count'],msg='Step 10:01 Verify "Percent of Count" option is selected')
        
        """
            Step 12 : Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 35)
        
        utillobj.switch_to_frame(pause=2)
        parent_css="#jschart_HOLD_0 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(parent_css, "Product Category", 30)
        
        expected_yval_list=[]
        expected_xval_list=[]
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, 'Step 12:01: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 12:02: Verify first bar color")
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 7, 'Step 12.03: Verify Number of bar chart')
        resultobj.verify_xaxis_title('jschart_HOLD_0', 'Product Category', "Step 12:04: Verify X-Axis Title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', 'PCT.CNT Model', "Step 12:05: Verify y-Axis Title")
        time.sleep(1)
        
        """
            Step 13 : over on "Media Player " riser
            Step 14 : Verify the tool tip value
        """
        expected_tooltip_list=['Product Category:Media Player', 'PCT.CNT Model:27.04']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g3!mbar!", expected_tooltip_list, "Step 13:01: Hover on Media Player riser and verify the tooltip value")
        time.sleep(1)
        
        """
            Step 15 : Click Save in the toolbar > Save as "C2328043" > Click Save
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(1)
        obj1=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step14', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 16 : Logout using API
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
            Step 17 : Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2328043.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_2', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1 text[class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(parent_css, 'Product Category', 65)
        
        """
            Step 18 : Verify restored successfully
        """
        parent_css=("#TableChart_1 text[class^='xaxis'][class$='title']")
        resultobj.wait_for_property(parent_css, 1)
        expected_yval_list=['0', '5', '10', '15', '20', '25', '30']
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 18:01: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 18:02: Verify first bar color")
        resultobj.verify_number_of_riser('TableChart_1', 1, 7, 'Step 18.03: Verify Number of bar chart')
        resultobj.verify_xaxis_title('TableChart_1', 'Product Category', "Step 18:04: Verify X-Axis Title")
        resultobj.verify_yaxis_title('TableChart_1', 'PCT.CNT Model', "Step 18:05: Verify y-Axis Title")
        time.sleep(1)
        
        """
            Step 19 : Right Click "PCT.CNT.Product, Category" > More >Aggregations functions (pull right)
        """
        metaobj.querytree_field_click('PCT.CNT.Model', 1, 1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('More')
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Aggregation Functions')
        time.sleep(2)
        
        """
            Step 20 : Verify "Percent of Count" option is selected (grey dot)
        """
        utillobj.select_or_verify_bipop_menu(verify='true', expected_popup_list=['Count','Count Distinct','Percent of Count'], expected_ticked_list=['Percent of Count'], msg='Step 19:01 Verify "Percent of Count" option is selected (grey dot)')
        
        """
            Step 21 : Logout using API
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
       
        
if __name__ == "__main__":
    unittest.main()
        




    

        
        
