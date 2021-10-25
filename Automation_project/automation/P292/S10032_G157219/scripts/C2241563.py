'''
Created on Nov 30, 2017

@author: Aftab/Somwiya
Testcase Name : API > Open existing > Chart
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2241563
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea
from common.lib import utillity

class C2241563_TestClass(BaseTestCase):

    def test_C2241563(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID='C2241563'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
            Step 01 : Open existing Chart with IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2241554.fex&tool=Chart
        """
        utillobj.infoassist_api_edit('C2241554','chart','P292/S10032_infoassist_5',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#pfjTableChart_1 text[class='xaxisOrdinal-title']", 1,60,string_value='Product Category')
        
        """
            Step 02 : Verify the existing chart opens
        """ 
        resultobj.verify_riser_chart_XY_labels('pfjTableChart_1',['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production'],['0','40M','80M','120M','160M','200M','240M'],'Step 02.1 :')
        resultobj.verify_number_of_riser('pfjTableChart_1',1,7,'Step 02.2 : Verify number of risers')
        resultobj.verify_xaxis_title('pfjTableChart_1','Product Category','Step 02.3 : Verify X-Axis title')
        resultobj.verify_yaxis_title('pfjTableChart_1','Cost of Goods','Step 02.4 : Verify Y-Axis title')
        utillobj.verify_chart_color('pfjTableChart_1','riser!s0!g3!mbar!','bar_blue1','Step 02.5 : Verify char riser color')
        screenshot_element=self.driver.find_element_by_id("resultArea")
        utillobj.take_screenshot(screenshot_element,Test_Case_ID+'_Actual_Step_02','actual')
        
        """
            Step 02.1 : Verify query panel
        """
        expected_fields=['Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Cost of Goods', 'Horizontal Axis', 'Product,Category', 'Marker', 'Color', 'Size', 'Tooltip', 'Multi-graph', 'Animate']
        position=1
        for field in expected_fields :
            metaobj.verify_query_pane_field('Chart (wf_retail_lite)',field,position,'Step 02.6.'+str(position))
            position+=1
        
        """
            Step 03 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__=='__main__' :
    unittest.main()