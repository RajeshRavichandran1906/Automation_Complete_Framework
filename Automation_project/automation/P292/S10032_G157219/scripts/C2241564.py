'''
Created on Dec 01, 2017

@author: PM14587
Testcase Name : API > New > Visualization
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2241564
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea,active_miscelaneous
from common.lib import utillity

class C2241564_TestClass(BaseTestCase):

    def test_C2241564(self):
        
        """   
        TESTCASE VARIABLES 
        """
        Restore_fex = 'C2241555'
        Test_Case_ID = 'C2241564'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        active=active_miscelaneous.Active_Miscelaneous(self.driver)
       
        """
        Step 01 : Open existing Visualization with IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2241555.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Restore_fex,'idis','P292/S10032_infoassist_5',mrid='mrid', mrpass='mrpass')
        element_css="#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'ProductCategory', expire_time=30)
        
        """
        Step 02 : Verify the existing Visualization opens
        """
        expected_fields=['Bar Stacked1', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Cost of Goods', 'Horizontal Axis', 'Product,Category', 'Marker', 'Color', 'Size', 'Tooltip']
        metaobj.verify_query_panel_all_field(expected_fields,'Step 02.0 : Verify query panel fields')
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f',['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production'],['0','40M','80M','120M','160M','200M','240M'],'Step 03.1 :')
        resultobj.verify_number_of_riser('MAINTABLE_wbody1_f',1,7,'Step 03.2 : Verify number of risers')
        resultobj.verify_xaxis_title('MAINTABLE_wbody1_f','Product Category','Step 03.3 : Verify X-Axis title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1_f','Cost of Goods','Step 03.4 : Verify Y-Axis title')
        utillobj.verify_chart_color('MAINTABLE_wbody1_f','riser!s0!g3!mbar!','bar_blue1','Step 03.5 : Verify char riser color')
        time.sleep(3)
        active.verify_active_chart_tooltip('MAINTABLE_wbody1_f','riser!s0!g3!mbar!',['Product Category:  Media Player', 'Cost of Goods:  $190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory'],'Step 03.6 : Verify tooltip values')
        screenshot_element=self.driver.find_element_by_id("resultArea")
        utillobj.take_screenshot(screenshot_element,Test_Case_ID+'_Actual_Step_02','actual')
        
        """
        Step 03 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
         
if __name__=='__main__' :
    unittest.main()