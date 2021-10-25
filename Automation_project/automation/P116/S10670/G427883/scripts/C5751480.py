'''
Created on January 02, 2019

@author: AA14564

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10670&group_by=cases:section_id&group_id=427883&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5751480
TestCase Name = AHTML: Add Sets to overide cache format and mode. (ACT-362)
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.active_report import Active_Report


class C5751480_TestClass(BaseTestCase):

    def test_C5751480(self):
        """
        TESTCASE Object's
        """
        utillobj = utillity.UtillityMethods(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        active_rpt_obj = Active_Report(self.driver)
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        folder_path = '{0}/{1}'.format(project_id, suite_id)
        
        """ Step 1: Execute the attached repro - ACT-362.fex
                    This repro runs 12 different combinations of the three control syntax commands: WEBVIEWER, ARCACHEMODE & ARCACHEFMT.
                    Expect to see just the HOLD output, no Active output.
                    All requests should give 18 records in Table and 10 lines of HTML output.
        """
        active_rpt_obj.run_active_report_using_api("ACT-362.fex", column_css="[class='errorContainer'] [class*='errorMain']", synchronize_visible_element_text='Nooutputwasreturned', repository_path=folder_path)
        actual_raw_data = utillobj.validate_and_get_webdriver_object("[class='errorContainer']", 'file text')
        actual_data=actual_raw_data.text.strip().split('\n')
        expected_data=['No output was returned', 'Possible causes:', '- Output was directed to a destination such as a file or printer', 'Detail:', ' Cache = On, Arcachemode = Noextract, Arcachefmt = Binary', ' ********************************************************', ' WEBVIEWER                 ON', ' ARCACHEMODE        NOEXTRACT', ' ARCACHEFMT            BINARY', ' 0 NUMBER OF RECORDS IN TABLE=       18  LINES=     10', ' 0 HTML FILE SAVED ...', ' *', ' *******************************************************', ' Cache = On, Arcachemode = Noextract, Arcachefmt = Focus', ' *******************************************************', ' WEBVIEWER                 ON', ' ARCACHEMODE        NOEXTRACT', ' ARCACHEFMT             FOCUS', ' 0 NUMBER OF RECORDS IN TABLE=       18  LINES=     10', ' 0 HTML FILE SAVED ...', ' *', ' *****************************************************', ' Cache = On, Arcachemode = Hold, Arcachefmt = Binary', ' *****************************************************', ' WEBVIEWER                 ON', ' ARCACHEMODE             HOLD', ' ARCACHEFMT            BINARY', ' 0 NUMBER OF RECORDS IN TABLE=       18  LINES=     10', ' 0 HTML FILE SAVED ...', ' *', ' *****************************************************', ' Cache = On, Arcachemode = Hold, Arcachefmt = Focus', ' *****************************************************', ' WEBVIEWER                 ON', ' ARCACHEMODE             HOLD', ' ARCACHEFMT             FOCUS', ' 0 NUMBER OF RECORDS IN TABLE=       18  LINES=     10', ' 0 HTML FILE SAVED ...', ' *', ' *****************************************************', ' Cache = On, Arcachemode = Nohold, Arcachefmt = Binary', ' *****************************************************', ' WEBVIEWER                 ON', ' ARCACHEMODE           NOHOLD', ' ARCACHEFMT            BINARY', ' 0 NUMBER OF RECORDS IN TABLE=       18  LINES=     10', ' 0 HTML FILE SAVED ...', ' *', ' *****************************************************', ' Cache = On, Arcachemode = Nohold, Arcachefmt = Focus', ' *****************************************************', ' WEBVIEWER                 ON', ' ARCACHEMODE           NOHOLD', ' ARCACHEFMT             FOCUS', ' 0 NUMBER OF RECORDS IN TABLE=       18  LINES=     10', ' 0 HTML FILE SAVED ...', ' *', ' *********************************************************', ' Cache = Off, Arcachemode = Noextract, Arcachefmt = Binary', ' *********************************************************', ' WEBVIEWER                OFF', ' ARCACHEMODE        NOEXTRACT', ' ARCACHEFMT            BINARY', ' 0 NUMBER OF RECORDS IN TABLE=       18  LINES=     10', ' 0 HTML FILE SAVED ...', ' *', ' *********************************************************', ' Cache = Off, Arcachemode = Noextract, Arcachefmt = Focus', ' *********************************************************', ' WEBVIEWER                OFF', ' ARCACHEMODE        NOEXTRACT', ' ARCACHEFMT             FOCUS', ' 0 NUMBER OF RECORDS IN TABLE=       18  LINES=     10', ' 0 HTML FILE SAVED ...', ' *', ' *****************************************************', ' Cache = Off, Arcachemode = Hold, Arcachemt = Binary', ' *****************************************************', ' WEBVIEWER                OFF', ' ARCACHEMODE             HOLD', ' ARCACHEFMT            BINARY', ' 0 NUMBER OF RECORDS IN TABLE=       18  LINES=     10', ' 0 HTML FILE SAVED ...', ' *', ' *****************************************************', ' Cache = Off, Arcachemode = Hold, Arcachemt = Focus', ' *****************************************************', ' WEBVIEWER                OFF', ' ARCACHEMODE             HOLD', ' ARCACHEFMT             FOCUS', ' 0 NUMBER OF RECORDS IN TABLE=       18  LINES=     10', ' 0 HTML FILE SAVED ...', ' *', ' ******************************************************', ' Cache = Off, Arcachemode = Nohold, Arcachefmt = Binary', ' ******************************************************', ' WEBVIEWER                OFF', ' ARCACHEMODE           NOHOLD', ' ARCACHEFMT            BINARY', ' 0 NUMBER OF RECORDS IN TABLE=       18  LINES=     10', ' 0 HTML FILE SAVED ...', ' *', ' ******************************************************', ' Cache = Off, Arcachemode = Nohold, Arcachefmt = Focus', ' ******************************************************', ' WEBVIEWER                OFF', ' ARCACHEMODE           NOHOLD', ' ARCACHEFMT             FOCUS', ' 0 NUMBER OF RECORDS IN TABLE=       18  LINES=     10', ' 0 HTML FILE SAVED ...']
        utillobj.asequal(actual_data, expected_data, 'Step 1: Expect to see just the HOLD output, no Active output.')
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()