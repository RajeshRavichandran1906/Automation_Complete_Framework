'''
Created on May 4, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2511545
TestCase Name = API > Run > Existing FEX
'''

import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,ia_resultarea
from common.lib.basetestcase import BaseTestCase

class C2511545_TestClass(BaseTestCase):

    def test_C2511545(self):
        
        Test_Case_ID = "C2511545"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)  
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)  
        
        """       
        Step 01:Launch IA master list dialog with ibisamp, Report mode:
        http://machine:port/ibi_apps/ia?tool=report&reportingServerNode=EDASERVE&reportingServerAppPath=ibisamp&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login_with_masterfile_promt('report&reportingServerNode=EDASERVE&reportingServerAppPath=ibisamp', 'mrid', 'mrpass')
        parent_css="#IbfsOpenFileDialog7_btnOK"
        utillobj.synchronize_until_element_is_visible(parent_css, resobj.home_page_long_timesleep)
        
        """
        Step 02:Select car > Click on "Open"
        """
        utillobj.select_masterfile_in_open_dialog('ibisamp', 'car')
        parent_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-']"
        utillobj.synchronize_until_element_is_visible(parent_css, resobj.home_page_long_timesleep)
        
        """
        Step 03:Add field car
        """
        metaobj.datatree_field_click("CAR", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(4) td"
        utillobj.synchronize_with_visble_text(parent_css, 'CAR', resobj.home_page_long_timesleep)
#         ia_resultobj.create_across_report_data_set('TableChart_1', 1, 1, 10, 1, Test_Case_ID+'_DataSet_01.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1',1,1,10,1,Test_Case_ID+'_DataSet_01.xlsx','Step 02 : Verify report')
        
        """
        Step 04: Click Save > Save as C2511545 > Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID) 
        
        """
        Step 05: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        utillobj.wf_logout()
        
        """
        Step 06:Reopen the saved fex:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2511545.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_5',mrid='mrid',mrpass='mrpass')
        utillobj.synchronize_with_visble_text(parent_css, 'CAR', resobj.home_page_long_timesleep)
               
        """
        Step 07:Verify Live Preview
        """
        ia_resultobj.verify_across_report_data_set('TableChart_1',1,1,10,1,Test_Case_ID+'_DataSet_01.xlsx','Step 07: Verify Live Preview')
       
        """
        Step 08:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main() 