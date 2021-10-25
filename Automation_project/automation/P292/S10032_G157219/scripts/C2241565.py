'''
Created on Dec 1, 2017

@author: Praveen Ramkumar 
Testcase Name : API > New > Reporting Object
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2241559
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_reporting_object
from common.lib import utillity

class C2241565_TestClass(BaseTestCase):

    def test_C2241565(self):
        
        """   
                TESTCASE VARIABLES 
        """
        
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(15)
        utillobj = utillity.UtillityMethods(self.driver)
        wfreporting=wf_reporting_object.Wf_Reporting_Object(self.driver)
       
        """
            Step 01: Open existing Reporting Object with IA API:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2241559.fex&tool=reportingobject
        """
        
        utillobj.infoassist_api_edit("C2241559",'reportingobject','P292/S10032_infoassist_5',mrid='mrid', mrpass='mrpass')
        time.sleep(5)
        
        """
            Step 02 : Verify the existing Reporting Object opens
        """
        ro_tool_name=['Reporting Object', 'Preprocessing Other', 'Joins', 'Defines', 'Filters', 'Where Statements', 'Report', 'Chart', 'Postprocessing Other']
        wfreporting.verify_ro_tree_item(ro_tool_name,"Step 02 : Verify the existing Reporting Object opens")
        
        """
            Step 03:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
if __name__ == '__main__':
    unittest.main()