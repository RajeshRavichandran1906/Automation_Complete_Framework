'''
Created on Dec 01, 2017

@author: PM14587
Testcase Name : API > New > Visualization
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2241564
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea
from common.lib import utillity
from common.wftools.visualization import Visualization

class C2241564_TestClass(BaseTestCase):

    def test_C2241564(self):
        
        """   
        TESTCASE VARIABLES 
        """
        Restore_fex = 'C2241555'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        visualization = Visualization(self.driver)
       
        """
        Step 01 : Open existing Visualization with IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2241555.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Restore_fex,'idis','P292/S10032_infoassist_5',mrid='mrid', mrpass='mrpass')
        visualization.wait_for_visible_text("#MAINTABLE_wbody1", "Computers")
        
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
        
        """
        Step 03 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
         
if __name__=='__main__' :
    unittest.main()