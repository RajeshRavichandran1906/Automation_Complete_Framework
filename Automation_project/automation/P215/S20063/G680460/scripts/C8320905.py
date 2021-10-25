'''
Created on Jan 03, 2019

@author: Magesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8320905
Test Case Title =  Launch Designer Workbook based on Reporting Object
'''
import sys
sys.path.append(r'C:\Users\td13786\eclipse-workspace\selenium')
import unittest,time
#from common.lib.basetestcase import BaseTestCase
from common.lib.basetestcasedocker import BaseTestCaseDocker
from common.wftools import designer_chart
from common.wftools import smoketest

#class C8320905_TestClass(BaseTestCase):
class C8320905_TestClass(BaseTestCaseDocker):

    def test_C8320905(self):
       
        """
        CLASS OBJECTS
        """
        designer_chartobj = designer_chart.Designer_Chart(self.driver)
        smoketestobj = smoketest.Smoketest(self.driver)
        
        """
        COMMON VARIABLES
        """
        Test_Case_ID = "c8320905"
        Restore_fex = "C8320905_RO"
        SHORT_WAIT_TIME = 5
        
        """
        STEP 1 : Launch Reporting Object tool with car
        http://machine:port/{alias}/ia?master=ibisamp/car&item=IBFS:/WFC/Repository/P215_S20063/G680460&tool=reportingobject
        """
        designer_chartobj.invoke_ia_using_api('ibisamp/car', tool='reportingobject')
        designer_chartobj.wait_for_number_of_element("#roTree table span", 9, smoketestobj.home_page_long_timesleep)
        
        """
        STEP 1.1 : Verify the Expected Result in Preview
        """
        designer_chartobj.verify_ro_tree_item_list(expected_ro_tree_item_list=['Reporting Object', 'Preprocessing Other', 'Joins', 'Defines', 'Filters', 'Where Statements', 'Report', 'Chart', 'Postprocessing Other'], msg="Step 01.01")
        
        """
        STEP 02 : Click on the Save button > Type "C8320905_RO" > Click on 'Save'
        """
        smoketestobj.save_ro_from_toolbar(Restore_fex)
        
        """
        STEP 03 : Select RO > Exit
        """
        #Since testcase is invoked using API. Hence logout is implemented. 
        designer_chartobj.api_logout()
        
        """
        STEP 04 : Launch IA Report based on the saved Reporting Object, C8320905_RO:
        http://machine:port/{alias}/designer?item=IBFS:/WFC/Repository/P215_S20063/G680460/C8320905_RO.fex&tool=workbook
        """
        designer_chartobj.invoke_designer_chart_in_edit_mode_using_api(Restore_fex+'.fex', tool='workbook')
        designer_chartobj.wait_for_visible_text("text[class='legend-labels!s0!']", 'Series 0', smoketestobj.home_page_long_timesleep)
        
        """
        STEP 04.1 : Verify the Expected Result in Preview
        """
        expected_xval_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        designer_chartobj.verify_x_axis_label_in_preview(expected_xval_list, msg="Step 04.01: Verify x_axis_label_in_preview")
        expected_yval_list=['0', '40', '80', '120', '160', '200']
        designer_chartobj.verify_y_axis_label_in_preview(expected_yval_list, msg="Step 04.02: Verify Y_axis_label_in_preview")
        designer_chartobj.verify_number_of_risers("[id*='chartpreview'] rect", 1, 25, msg="Step 04.03: Verify number of risers_in_preview")
        legend=['Series 0', 'Series 1', 'Series 2', 'Series 3', 'Series 4']
        designer_chartobj.verify_legends_in_preview(legend, msg="Step 04.04: Verify legend_in_preview")
        
        """
        STEP 05 : Double click COUNTRY
        """
        smoketestobj.double_click_on_dimension_field('COUNTRY')
        
        """
        STEP 05.1 : Verify the Expected Result in Preview
        """
        designer_chartobj.wait_for_visible_text("#arpreview_fdmId_11_fmg", "COUNTRY")
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        designer_chartobj.verify_x_axis_label_in_preview(expected_xval_list, msg="Step 05.01: Verify x_axis_label_in_preview")
        designer_chartobj.verify_x_axis_title_in_preview(['COUNTRY'], msg="Step 05.02: Verify x_axis title in_preview")
        designer_chartobj.verify_number_of_risers("div.wfc-bc-output-div rect", 1, 5, msg="Step 05.03: Verify number of risers_in_preview")
        designer_chartobj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', msg='Step 05.04')
        
        """
        STEP 06 : Click on Save > Type "C8320905" > Click 'Save'
        """
        smoketestobj.save_designer_chart_from_toolbar(Test_Case_ID)
        time.sleep(SHORT_WAIT_TIME)
        
        """
        STEP 07 : Click on the application menu > Close
        """
        #Since testcase is invoked using API, application menu > Close not working. Hence logout is implemented. 
        designer_chartobj.api_logout()
        
        """
        STEP 08 : Edit the saved workbook
        http://machine:port/{alias}/designer?item=IBFS:/WFC/Repository/P215_S20063/G680460/C8320905&startlocation=IBFS:/WFC/Repository/P215_S20063/G680460
        """
        designer_chartobj.invoke_designer_chart_in_edit_mode_using_api(Test_Case_ID, tool='workbook')
        
        """
        STEP 08.1 : Verify the Expected Result in Preview
        """
        designer_chartobj.wait_for_visible_text("#arpreview_fdmId_11_fmg", "COUNTRY")
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        designer_chartobj.verify_x_axis_label_in_preview(expected_xval_list, msg="Step 08.01: Verify x_axis_label_in_preview")
        designer_chartobj.verify_x_axis_title_in_preview(['COUNTRY'], msg="Step 08.02: Verify x_axis title in_preview")
        designer_chartobj.verify_number_of_risers("div.wfc-bc-output-div rect", 1, 5, msg="Step 08.03: Verify number of risers_in_preview")
        designer_chartobj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', msg='Step 08.04')
        
        """
        STEP 09 : Click on the application menu > Close 
        """
        #Since testcase is invoked using API, application menu > Close not working. Hence logout is implemented. 
        designer_chartobj.api_logout()
        
if __name__ == "__main__":
    unittest.main()