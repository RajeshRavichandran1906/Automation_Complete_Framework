'''
Created on Nov 30, 2017

@author: PM14587
Testcase Name : API > Open existing > Report
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2241558
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,ia_resultarea,visualization_metadata
from common.lib import utillity

class C2241558_TestClass(BaseTestCase):

    def test_C2241558(self):
        
        """   
                TESTCASE VARIABLES 
        """
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        
        """
            Step 01 : Open existing Report with IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2241552.fex&tool=Report
        """
        utillobj.infoassist_api_edit('C2241552_base','report','P292/S10032_infoassist_5',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        time.sleep(3)
        
        """
            Step 02 : Verify the existing Report opens
        """
        expected_fields=['Sum', 'Cost of Goods', 'By', 'Product,Category', 'Across']
        position=1
        for field in expected_fields :
            metaobj.verify_query_pane_field('Report (wf_retail_lite)',field,position,'Step 2.'+str(position))
            position+=1
            
        iaresult.verify_across_report_data_set('TableChart_1', 1,2,8,2,'C2241552_DataSet_01.xlsx','Step 2.6 : Verify the existing Report opens')
        
        """
            Step 03 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__=='__main__' :
    unittest.main()