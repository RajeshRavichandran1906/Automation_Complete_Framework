'''
Created on DEC 01, 2017

@author: Pavithra 

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2247608
TestCase Name = API > Open existing > Alert
'''
import unittest
import time
from common.lib import utillity
from common.pages import wf_alert_assist
from common.lib.basetestcase import BaseTestCase

class C2247608_TestClass(BaseTestCase):

    def test_C2247608(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        alertobj= wf_alert_assist.Wf_Alert_Assist(self.driver) 
              
        """   
            Step 01:Launch Report mode with IA API:
                    http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2241557.fex
        """
        utillobj.infoassist_api_edit("C2241557",'alert','P292/S10032_infoassist_5',mrid='mrid', mrpass='mrpass')
        time.sleep(5)
 
        """
            Step 02:Verify the existing Alert opens
        """
        alertobj.verify_aa_tree_item('Alert', "Step 02:verify tool menu item Alert Assist is launched")        

        """
            Step 03:Logout:http://machine:port/ibi_apps/service/wf_security_    logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main() 
