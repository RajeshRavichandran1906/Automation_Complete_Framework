'''
Created on Jan 02, 2019

@author: Magesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8320685
Test Case Title =  Launch IA Report, save and restore 
'''

import unittest,time
#from common.lib.basetestcase import BaseTestCase
from common.lib.basetestcasedocker import BaseTestCaseDocker
from common.lib import utillity
from common.wftools import designer_chart, report, smoketest

#class C8320685_TestClass(BaseTestCase):
class C8320685_TestClass(BaseTestCaseDocker):

    def test_C8320685(self):
       
        """
        CLASS OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        designer_chartobj = designer_chart.Designer_Chart(self.driver)
        reportobj = report.Report(self.driver)
        smoketestobj = smoketest.Smoketest(self.driver)
        
        """
        COMMON VARIABLES
        """
        Test_Case_ID="c8320685"
        SHORT_WAIT_TIME = 5
        preview_parent_css = "TableChart_1"
        preview_text_css="#TableChart_1 [class='bi-label'] [style*='font']"
        
        """
        STEP 1 : Launch InfoAssist Chart with car
        http://machine:port/ibi_apps/ia?&master=ibisamp/car&item=IBFS:/WFC/Repository/Smoke&tool=report
        """
        designer_chartobj.invoke_ia_using_api('ibisamp/car', tool='report')
        designer_chartobj.wait_for_number_of_element(preview_text_css, 1, smoketestobj.home_page_long_timesleep)
        
        """
        STEP 1.1 : Verify the Expected Result in Preview
        """
        preview_text_obj=utillobj.validate_and_get_webdriver_object(preview_text_css, "Preview text css")
        actual_text=preview_text_obj.text.strip().replace('\n', ' ')
        expected_text='Drag and drop fields onto the canvas or into the query pane to begin building your report.'
        utillobj.asequal(actual_text, expected_text, "Step 01.01: Verify the Expected text in Preview")
        
        """
        STEP 02 : Double click COUNTRY
        """
        smoketestobj.double_click_on_datetree_item('COUNTRY', 1)
        
        """
        STEP 2.1 : Verify the Expected Result in Preview
        """
        designer_chartobj.wait_for_number_of_element("#TableChart_1 div[class^='x']", 6, smoketestobj.home_page_medium_timesleep)
        reportobj.verify_report_column_titles_on_preview(1, 1, expected_list=['COUNTRY'], msg="Step 02.01: Verify report title")
#         reportobj.create_report_data_set_in_preview(preview_parent_css, 5, 1, "C8320685_Ds01.xlsx")
        reportobj.verify_report_data_set_in_preview(preview_parent_css, 5, 1, "C8320685_Ds01.xlsx", msg="Step 02.02: Verify report dataset")
        
        """
        STEP 03 : Click on Save button > Type C8320685 > Click on 'Save'
        """
        smoketestobj.select_item_in_top_toolbar('save')
        smoketestobj.save_file_in_save_dialog(Test_Case_ID)
        time.sleep(SHORT_WAIT_TIME)
        
        """
        STEP 4 : Select IA > Exit
        """
        #Since testcase is invoked using API. Hence logout is implemented. 
        designer_chartobj.api_logout()
        
        """
        STEP 5 : Edit the saved FEX
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Smoke/C8320685.fex&tool=report
        """
        designer_chartobj.invoke_ia_in_edit_mode_using_api(Test_Case_ID, tool='report')
        
        """
        STEP 5.1 : Verify the Expected Result in Preview
        """
        designer_chartobj.wait_for_number_of_element("#TableChart_1 div[class^='x']", 6, smoketestobj.home_page_long_timesleep)
        reportobj.verify_report_column_titles_on_preview(1, 1, expected_list=['COUNTRY'], msg="Step 05.01: Verify report title")
        reportobj.verify_report_data_set_in_preview(preview_parent_css, 5, 1, "C8320685_Ds01.xlsx", msg="Step 05.02: Verify report dataset")
        
        """
        STEP 6 : Select IA > Exit
        """
        #Since testcase is invoked using API. Hence logout is implemented. 
        designer_chartobj.api_logout()
        
if __name__ == "__main__":
    unittest.main()