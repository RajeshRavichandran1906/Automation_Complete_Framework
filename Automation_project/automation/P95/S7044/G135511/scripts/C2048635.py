'''
Created on January 16, 2019

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2048635
TestCase Name = Click cancel in ADP prop dialog clears document source (147897)
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.lib import utillity
from common.wftools import visualization
from common.wftools import report
from common.wftools import document
from common.lib import core_utility

class C2048635_TestClass(BaseTestCase):

    def test_C2048635(self):
        """
        Test case Object's
        """
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        document_obj = document.Document(self.driver)
        report_obj = report.Report(self.driver)
        visual_obj = visualization.Visualization(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        """
        Test case variables
        """
        expected_list_elements = ['[All]', 'ACCOUNTING', 'ADMIN SERVICES', 'CONSULTING', 'CUSTOMER SUPPORT', 'MARKETING', 'PERSONNEL', 'PROGRAMMING & DVLPMT', 'SALES']
        
        """ 
        Step 1: Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=ibisamp/empdata&item=IBFS:/WFC/Repository/P95/S10142
        """
        report_obj.invoke_ia_tool_using_new_api_login(tool='document', master='ibisamp/empdata', report_css="#canvasContainer", no_of_element=1)
        
        """
        Step 2: Select AHTML as the output.
        Select the ENIADefault_combine.sty stylesheet as directed on the Preconditions section.
        """
        chart_obj.change_output_format_type('ahtml')