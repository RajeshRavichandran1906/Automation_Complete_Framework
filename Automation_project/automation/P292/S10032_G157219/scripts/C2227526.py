'''
Created on Nov 25, 2017

@author: BM13368
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227526
Testcase Name : Verify Preview context menus 
'''
import unittest, time, re
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon, ia_run, active_miscelaneous
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2227526_TestClass(BaseTestCase):

    def test_C2227526(self):
        
        Test_Case_ID = "C2227526"
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        active_misc_obj=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
            Step 01: Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/CAR','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """  
            Step 02: Double-click fields CAR and SALES
        """
        metaobj.datatree_field_click('CAR', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('SALES', 2, 1)
        time.sleep(4)
        """
            Verify Report data in live preview
        """
        ia_resultobj.verify_report_data_set('TableChart_1', 5, 2, "C2227526_Ds01.xlsx", 'Step 02:02: Verify report dataset')
        """  
            Step 03: Click on the Output Location shortcut in the lower right corner > Verify menu
        """
        elem=self.driver.find_element_by_css_selector("#sbpTargetOutputPanel")
        elem.click()
        time.sleep(1)
        a=['Single Tab', 'New Tab', 'Single Window', 'New Window']
        utillobj.select_or_verify_bipop_menu(verify='true', expected_popup_list=a, expected_ticked_list=['Single Tab'], msg='Step 03:01 Verify menu displayed')
        
        """ 
            Step 04 : Select "New Window" > Verify selection
        """ 
        utillobj.select_or_verify_bipop_menu('New Window', verify='true', expected_popup_list=a, expected_ticked_list=['Single Tab'], msg='Step 04:01 Select New Window')
        elem=self.driver.find_element_by_css_selector("#sbpTargetOutputPanel")
        elem.click()
        time.sleep(1)
        a=['Single Tab', 'New Tab', 'Single Window', 'New Window']
        utillobj.select_or_verify_bipop_menu(verify='true', expected_popup_list=a, expected_ticked_list=['New Window'], msg='Step 04:02 Verify New Window is selected')
        
        """
            Step 05: Click on the Output Format shortcut in the lower right corner > Verify menu
            Step 06: Select "Active Report" > Verify selection
        """
        list1=['HTML', 'Active Report', 'PDF', 'Excel (xlsx)', 'PowerPoint (pptx)'] 
        ia_ribbobj.select_or_verify_output_type(launch_point='bottom_tool_bar', expected_output_list1=list1, msg1="Step 05:01: Verify output formats.", item_select_path='Active Report')
        time.sleep(1)
        output_css=self.driver.find_element_by_css_selector("#sbpOutputFormat")
        output_css.click()
        time.sleep(2)
        report_format_css=self.driver.find_element_by_css_selector("#menu_ahtml_btn")
        status=True if bool(re.match('.*checked.*', report_format_css.get_attribute("class"))) else False
        utillobj.asequal(True, status, "Step 06:01: Verify Output format has been selected as Active Report")
        """ 
            Step 07: Click "IA" menu > Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        
        """  
            Step 08: Verify Active Report output in a new window > Close the window
        """
        active_misc_obj.verify_page_summary(0, '10of10records,Page1of1', 'Step 08:01: Execute the act-886-report.fex and Verify the Report Heading')
        ia_runobj.verify_table_data_set("#ITableData0", Test_Case_ID+"_Ds02.xlsx", 'Step 08:02: Verify Active Report format report After Run')
        
        driver.close()
        utillobj.switch_to_window(0)
        """ 
            Step 09: Click "IA" menu > Click "New"
        """
        ribbonobj.select_top_toolbar_item('toolbar_new')
        resultobj.wait_for_property("#splash_options", 1, expire_time=8)   
        
        """  
            Step 10: Select "Build a Report" in the Splash Screen
        """
        ribbonobj.select_item_in_splash_options('Build a Report')
        
        """
            Step 11: Select file CAR > Click "Open"
        """  
#         utillobj.select_masterfile_in_open_dialog("ibisamp", "Car")
        """Using API login master selection dialog will not be displayed"""
        """
            Step 12: Verify Status bar options
        """ 
        elem=self.driver.find_element_by_css_selector("#sbpSwitchReport")
        elem.click()
        time.sleep(1)
        a=['Report1', 'Report2']
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=a, expected_ticked_list=['Report2'], msg='Step 12:01 Verify menu displayed and Report1 is selected')
        
        """
           Step 13 : Click on the "2 Reports" shortcut > Verify menu 
        """ 
        a=['Report1', 'Report2']
        utillobj.select_or_verify_bipop_menu('Report2', verify='true',expected_popup_list=a, msg='Step 13:01 Verify menu displayed')
        elem=self.driver.find_element_by_css_selector("#sbpSwitchReport")
        elem.click()
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu('Report2', verify='true',expected_popup_list=a, expected_ticked_list=['Report2'], msg='Step 13:02 Verify menu displayed and Report2 is selected')
        
        """
            Step 14: Select "Report1" > Verify options for Report1
        """
        elem=self.driver.find_element_by_css_selector("#sbpSwitchReport")
        elem.click()
        a=['Report1', 'Report2']
        utillobj.select_or_verify_bipop_menu('Report1', verify='true',expected_popup_list=a, msg='Step 14:01 Verify menu displayed')
        elem=self.driver.find_element_by_css_selector("#sbpSwitchReport")
        elem.click()
        a=['Report1', 'Report2']
        utillobj.select_or_verify_bipop_menu('Report1', verify='true',expected_popup_list=a, expected_ticked_list=['Report1'], msg='Step 14:01 Verify menu displayed')
        
        """
            Step 15: Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    unittest.main()