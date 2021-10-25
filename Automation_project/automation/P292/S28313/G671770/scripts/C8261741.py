'''
Created on April 13, 2019

@author: Niranjan\Samuel

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8261741
TestCase Name = Check Legacy Home Page
'''

import unittest
from common.lib import utillity
from common.pages import wf_legacymainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods

class C8261741_TestClass(BaseTestCase):

    def test_C8261741(self):
        
        """
            TESTCASE OBJECTS
        """
        core_utils = CoreUtillityMethods(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        
        """
            TESTCASE CSS
        """
        parent_css="#bipTreePanel"
        
        """
            TESTCASE VARIABLES
        """
        expected_list = ['Portal', 'Workbook', 'Insight Charts']
        
        """
            Step 1 : Sign into WebFOCUS legacy home page as Administrator
            Navigate URL to http://environment_name:port/alias/legacyhom
        """
        util_obj.invoke_legacyhomepage('mrid', 'mrpass')
        util_obj.synchronize_with_visble_text(parent_css, 'Workspaces', wf_mainobj.chart_long_timesleep)
        
        """
            Step 2 : Right click on Domain node
            Verify that Portal, Workbook and Insight Charts are not available in the context menu.
        """
        wf_mainobj.select_menu(folder_path='Workspaces', menu_item='New', expected_menu_list = expected_list, item_exit = False, msg='Step 2.1: Verify that Portal, Workbook and Insight Charts are not available in the context menu')
        toolbar = self.driver.find_element_by_id("topBannerMenuBox")
        core_utils.python_left_click(toolbar)
         
        """
            Step 3: Right click on "P292_S10660" domain > New
            Verify that Portal, Workbook and Insight Charts are not available in the context menu.
            Step 4: Using API link Sign out WebFOCUS
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        wf_mainobj.select_menu(folder_path='P292_S10660', menu_item='New', expected_menu_list = expected_list, item_exit = False, msg='Step 3.1: Verify that Portal, Workbook and Insight Charts are not available in the context menu')
        
if __name__ == '__main__':
    unittest.main()