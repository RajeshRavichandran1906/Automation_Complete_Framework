'''
Created on sep 10, 2019

@author: vpriya

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/9318208
TestCase Name = Verify default User Preferences values
'''

import unittest, time
from common.pages import visualization_ribbon
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report

class C9318208_TestClass(BaseTestCase):

    def test_C9318208(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        report_obj = Report(self.driver)
        
        Step1 ="""
            Step 01:Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        
        report_obj.invoke_ia_tool_using_new_api_login(master='ibisamp/car', mrid='mrid', mrpass='mrpass')
        utillobj.capture_screenshot("01",Step1)
        
        Step2 = """
           Step 02:Click "IA" > "Options".
        Verify the "Options" window is displayed.
        """
        ribbonobj.select_tool_menu_item("menu_options")
        options_css_obj="#dlgPrefs div[class*='active'] [class*='caption'] [class*='bi-label']"
        utillobj.verify_popup(options_css_obj, "Step 03:01 : Verify the Options window is displayed..", caption_css=options_css_obj, caption_text='Options')
        utillobj.capture_screenshot("02",Step2,expected_image_verify=True)
        
        Step3 = """ 
            Step 03:Click "Report output type" (dropdown).
            Verify it contains the following options:
        """
        utillobj.verify_combo_box_item(['HTML', 'PDF', 'PowerPoint (pptx)', 'Excel (xlsx)', 'Excel (xlsx Formula)', 'Excel', 'Excel (Formula)', 'Excel (csv)', 'HTML Analytic Document', 'PDF Analytic Document'], combobox_dropdown_css='#dlgPrefs #dlgPrefsOutputFormatTable', msg="Step 03:01 verify_report_dropdown")
        report_output_css=self.driver.find_element_by_css_selector("#dlgPrefs #dlgPrefsOutputFormatTable")
        time.sleep(1)
        utillobj.default_left_click(object_locator=report_output_css)
        utillobj.capture_screenshot("03",Step3,expected_image_verify=True)
        
        Step4 = """ 
            Step 04:Select "Chart output type" dropdown.
            Verify it contains the following options:
        """
        utillobj.verify_combo_box_item(['HTML', 'HTML5','PDF', 'PowerPoint (pptx)', 'Excel (xlsx)','Excel','HTML Analytic Document', 'PDF Analytic Document'], combobox_dropdown_css='#dlgPrefs #dlgPrefsOutputFormatChart', msg="04:01 verify_chart_dropdown")
        Chart_output_css=self.driver.find_element_by_css_selector("#dlgPrefs #dlgPrefsOutputFormatChart")
        utillobj.capture_screenshot("04",Step4,expected_image_verify=True)
        utillobj.default_left_click(object_locator=Chart_output_css)
        
        
        Step5 = """ 
            Step 05:Select "Document output type" dropdown.
            Check it contains the following options.
        """ 
        utillobj.verify_combo_box_item(['HTML', 'PDF', 'PowerPoint (pptx)', 'Excel (xlsx)', 'Excel (xlsx Formula)', 'Excel', 'Excel (Formula)', 'HTML Analytic Document', 'PDF Analytic Document'],combobox_dropdown_css='#dlgPrefs #dlgPrefsComposeOutputType',msg="05:01 verify_doc_dropdown")
        Doc_output_css=self.driver.find_element_by_css_selector("#dlgPrefs #dlgPrefsComposeOutputType")
        utillobj.capture_screenshot("05",Step5,expected_image_verify=True)
        utillobj.default_left_click(object_locator=Doc_output_css)
        
        Step6 = """ 
            Step 06:Click "Cancel".
        """
        cancel_btn_css=self.driver.find_element_by_css_selector("#dlgPrefsoptionsCancel")
        utillobj.click_on_screen(cancel_btn_css, "middle", 0)
        utillobj.capture_screenshot("06",Step6)
        
        """ 
            Step 07:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()