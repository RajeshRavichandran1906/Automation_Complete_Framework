'''
Created on Jan 02, 2019

@author: Magesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8320666
Test Case Title =  Launch Reporting Object, save and restore 
'''

import unittest
#from common.lib.basetestcase import BaseTestCase
from common.lib.basetestcasedocker import BaseTestCaseDocker
from common.wftools import designer_chart
from common.wftools import smoketest

#class C8320666_TestClass(BaseTestCase):
class C8320666_TestClass(BaseTestCaseDocker):

    def test_C8320666(self):
       
        """
        CLASS OBJECTS
        """
        designer_chartobj = designer_chart.Designer_Chart(self.driver)
        smoketestobj = smoketest.Smoketest(self.driver)
        
        """
        COMMON VARIABLES
        """
        Test_Case_ID="c8320666"
        
        """
        STEP 1 : Launch Reporting Object tool with car
        http://machine:port/{alias}/ia?master=ibisamp/car&item=IBFS:/WFC/Repository/Smoke&tool=reportingobject
        """
        designer_chartobj.invoke_ia_using_api('ibisamp/car', tool='reportingobject')
        designer_chartobj.wait_for_number_of_element("#roTree table span", 9, smoketestobj.home_page_long_timesleep)
        
        """
        STEP 1.1 : Verify the Expected Result in Preview
        """
        designer_chartobj.verify_ro_tree_item_list(expected_ro_tree_item_list=['Reporting Object', 'Preprocessing Other', 'Joins', 'Defines', 'Filters', 'Where Statements', 'Report', 'Chart', 'Postprocessing Other'], msg="Step 01.01")
        
        """
        STEP 02 : Click on the Save button > Type "C8320666" > Click on 'Save'
        """
        smoketestobj.save_ro_from_toolbar(Test_Case_ID)
        
        """
        STEP 03 : Select RO > Exit
        """
        #Since testcase is invoked using API. Hence logout is implemented. 
        designer_chartobj.api_logout()
        
        """
        STEP 04 : Edit the saved Reporting Object FEX
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Smoke/C8320666.fex&tool=reportingobject
        """
        designer_chartobj.invoke_ia_in_edit_mode_using_api(Test_Case_ID, tool='reportingobject')
        
        """
        STEP 5.1 : Verify the Expected Result in Preview
        """
        designer_chartobj.wait_for_number_of_element("#roTree table span", 9, smoketestobj.home_page_medium_timesleep)
        designer_chartobj.verify_ro_tree_item_list(expected_ro_tree_item_list=['Reporting Object', 'Preprocessing Other', 'Joins', 'Defines', 'Filters', 'Where Statements', 'Report', 'Chart', 'Postprocessing Other'], msg="Step 05.01")
        
        """
        STEP 6 : Select RO > Exit
        """
        #Since testcase is invoked using API. Hence logout is implemented. 
        designer_chartobj.api_logout()
        
if __name__ == "__main__":
    unittest.main()