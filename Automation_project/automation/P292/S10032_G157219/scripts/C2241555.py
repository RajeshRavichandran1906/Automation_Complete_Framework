'''
Created on Nov 30, 2017

@author: PM14587
Testcase Name : API > New > Visualization
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2241555
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,active_miscelaneous
from common.lib import utillity

class C2241555_TestClass(BaseTestCase):

    def test_C2241555(self):
        
        """   
        TESTCASE VARIABLES 
        """
        driver = self.driver
        Test_Case_ID = 'C2241555'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        active=active_miscelaneous.Active_Miscelaneous(self.driver)
       
        """
            Step 01 : Launch Visualization mode with IA API: http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_infoassist_5', 'mrid', 'mrpass')
        element_css="#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(1)"
        utillobj.synchronize_with_visble_text(element_css, 'BarStacked1', expire_time=20)
        
        """
            Step 02 : Verify IA Visualization mode is launched
        """
        utillobj.verify_element_text("#pfjTableChart_1 text[class='title']",'Drop Measures or Sorts into the Query Pane','Step 02.1 : Verify IA Visualization mode is launched')
        resultobj.verify_number_of_riser('pfjTableChart_1',3,4,'Step 02.1 : Verify number of risers')
        
        """
            Step 03 : Double click on fields "Cost of Goods" and "Product,Category"
        """
        metaobj.datatree_field_click('Cost of Goods',2,1)
        element_css="#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(7)"
        utillobj.synchronize_with_visble_text(element_css, 'CostofGoods', expire_time=20)
        
        metaobj.datatree_field_click('Product,Category',2,1)
        element_css="#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(9)"
        utillobj.synchronize_with_visble_text(element_css, 'Product,Category', expire_time=20)
        
        """
            Step 03.1 : Verify the canvas
        """
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f',['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production'],['0','40M','80M','120M','160M','200M','240M'],'Step 03.1 :')
        resultobj.verify_number_of_riser('MAINTABLE_wbody1_f',1,7,'Step 03.2 : Verify number of risers')
        resultobj.verify_xaxis_title('MAINTABLE_wbody1_f','Product Category','Step 03.3 : Verify X-Axis title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1_f','Cost of Goods','Step 03.4 : Verify Y-Axis title')
        utillobj.verify_chart_color('MAINTABLE_wbody1_f','riser!s0!g3!mbar!','bar_blue1','Step 03.5 : Verify char riser color')
        time.sleep(3)
        active.verify_active_chart_tooltip('MAINTABLE_wbody1_f','riser!s0!g3!mbar!',['Product Category:  Media Player', 'Cost of Goods:  $190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory'],'Step 03.6 : Verify tooltip values')
        screenshot_element=self.driver.find_element_by_id("resultArea")
        utillobj.take_screenshot(screenshot_element,Test_Case_ID+'_Actual_Step_03','actual')
        
        """
            Step 04 : Click Run and Verify the output,
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')    
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)  
        element_css="#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'ProductCategory', expire_time=20)
        
        """
            Step 04.1 : Verify the canvas
        """
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f',['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production'],['0','40M','80M','120M','160M','200M','240M'],'Step 04.1 :')
        resultobj.verify_number_of_riser('MAINTABLE_wbody1_f',1,7,'Step 04.2 : Verify number of risers')
        resultobj.verify_xaxis_title('MAINTABLE_wbody1_f','Product Category','Step 04.3 : Verify X-Axis title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1_f','Cost of Goods','Step 04.4 : Verify Y-Axis title')
        utillobj.verify_chart_color('MAINTABLE_wbody1_f','riser!s0!g3!mbar!','bar_blue1','Step 04.5 : Verify char riser color')
        time.sleep(3)
        active.verify_active_chart_tooltip('MAINTABLE_wbody1_f','riser!s0!g3!mbar!',['Product Category:  Media Player', 'Cost of Goods:  $190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory'],'Step 04.6 : Verify tooltip values')
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_04','actual')
        driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        utillobj.synchronize_with_number_of_element("#applicationButton img", 1, 20)
        
        """
            Step 05 : Click "Save" > Save As "C2241555" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 06 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
         
if __name__=='__main__' :
    unittest.main()