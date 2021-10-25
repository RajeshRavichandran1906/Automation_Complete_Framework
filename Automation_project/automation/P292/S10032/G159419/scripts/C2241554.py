'''
Created on Nov 30, 2017

@author: PM14587
Testcase Name : API > New > Chart
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2241554
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,active_miscelaneous
from common.lib import utillity

class C2241554_TestClass(BaseTestCase):

    def test_C2241554(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2241554'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        active=active_miscelaneous.Active_Miscelaneous(self.driver)
       
        """
            Step 01 : Launch Chart mode with IA API: http://machine:port/ibi_apps/ia?tool=Chart&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('Chart','baseapp/wf_retail_lite','P292/S10032_infoassist_5', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1 text[class='legend-labels!s0!']", 'Series 0', 80)
        
        """
            Step 02 : Verify IA Chart mode is launched
        """
        resultobj.verify_riser_chart_XY_labels('pfjTableChart_1',['Group 1','Group 2','Group 3','Group 4'],['0','10','20','30','40','50'],'Step 02.1 :')
        resultobj.verify_number_of_riser('pfjTableChart_1',5,5,'Step 02.2 : Verify number of risers')
        resultobj.verify_riser_legends('pfjTableChart_1',['Series0','Series1','Series2','Series3','Series4'],'Step 02.3 : Verify legend values')
        screenshot_element=self.driver.find_element_by_id("resultArea")
        utillobj.take_screenshot(screenshot_element,Test_Case_ID+'_Actual_Step_02','actual')
        
        """
            Step 03 : Double click on fields "Cost of Goods" and "Product,Category"
        """
        metaobj.datatree_field_click('Cost of Goods',2,1)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='yaxis-title']", 'Cost of Goods', 20)
        metaobj.datatree_field_click('Product,Category',2,1)
        utillobj.synchronize_with_visble_text("#TableChart_1 [class='xaxisOrdinal-title']", 'Product Category', 20)
        
        """
            Step 03.1 : Verify the canvas,
        """
        resultobj.verify_riser_chart_XY_labels('pfjTableChart_1',['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production'],['0','40M','80M','120M','160M','200M','240M'],'Step 02.1 :')
        resultobj.verify_number_of_riser('pfjTableChart_1',1,7,'Step 02.2 : Verify number of risers')
        resultobj.verify_xaxis_title('pfjTableChart_1','Product Category','Step 02.3 : Verify X-Axis title')
        resultobj.verify_yaxis_title('pfjTableChart_1','Cost of Goods','Step 02.4 : Verify Y-Axis title')
        utillobj.verify_chart_color('pfjTableChart_1','riser!s0!g3!mbar!','bar_blue1','Step 02.5 : Verify char riser color')
        screenshot_element=self.driver.find_element_by_id("resultArea")
        utillobj.take_screenshot(screenshot_element,Test_Case_ID+'_Actual_Step_03','actual')
        
        """
            Step 04 : Click Run and Verify the output,
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#jschart_HOLD_0 text[class='xaxisOrdinal-title']", 'Product Category', 35)
        
        """
            Step 04 : Verify output
        """
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0',['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production'],['0','40M','80M','120M','160M','200M','240M'],'Step 02.1 :')
        resultobj.verify_number_of_riser('jschart_HOLD_0',1,7,'Step 02.2 : Verify number of risers')
        resultobj.verify_xaxis_title('jschart_HOLD_0','Product Category','Step 02.3 : Verify X-Axis title')
        resultobj.verify_yaxis_title('jschart_HOLD_0','Cost of Goods','Step 02.4 : Verify Y-Axis title')
        utillobj.verify_chart_color('jschart_HOLD_0','riser!s0!g3!mbar!','bar_blue1','Step 02.5 : Verify char riser color')
        active.verify_active_chart_tooltip('jschart_HOLD_0','riser!s0!g3!mbar!',['Product Category:  Media Player', 'Cost of Goods:  $190,240,481.00'],'Step 02.6 : Verify tooltip values')
        
        utillobj.switch_to_default_content(3)
        screenshot_element=self.driver.find_element_by_id("resultArea")
        utillobj.take_screenshot(screenshot_element,Test_Case_ID+'_Actual_Step_04','actual')
        
        """
            Step 05 : Click "Save" > Save As "C2241553" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
            Step 06 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__=='__main__' :
    unittest.main()