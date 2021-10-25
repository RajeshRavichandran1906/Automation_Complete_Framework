'''
Created on 

@author: 

Test Case = 
TestCase Name = 
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_report import Active_Report
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.lib.base import BasePage

class C8358934_TestClass(BaseTestCase):

    def test_C8358934(self):
        
        """
        TESTCASE Object's
        """
        base_obj = BasePage(self.driver)
        util_obj = UtillityMethods(self.driver)
        active_report_obj = Active_Report(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        
        """
        Test case variables
        """
        test_case_id = 'C8358920'
        project = core_util_obj.parseinitfile('project_id')
        suite = core_util_obj.parseinitfile('suite_id')
        group = core_util_obj.parseinitfile('group_id')
        folder_path = "{0}_{1}/{2}".format(project, suite, group)
        
if __name__ == '__main__':
    unittest.main()