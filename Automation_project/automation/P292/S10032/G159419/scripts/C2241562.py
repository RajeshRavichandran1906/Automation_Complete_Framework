'''
Created on Dec 01, 2017

@author: PM14587
Testcase Name : API > Open existing > Document
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2241562
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,ia_resultarea
from common.lib import utillity

class C2241562_TestClass(BaseTestCase):

    def test_C2241562(self):
        
        """   
                TESTCASE VARIABLES 
        """
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        
        """
            Step 01 Open existing Document with IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2241553.fex&tool=Document
        """
        utillobj.infoassist_api_edit('C2241553','Document','P292/S10032_infoassist_5',mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#canvasContainer", 'Computers', resultobj.home_page_long_timesleep)
        
        """
            Step 02 : Verify the existing document opens
        """
        iaresult.verify_across_report_data_set('canvasContainer #TableChart_1', 1,2,8,2,'C2241553_DataSet_01.xlsx','Step 02.1 : Verify the existing document opens')
        
        """
            Step 03 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__=='__main__' :
    unittest.main()