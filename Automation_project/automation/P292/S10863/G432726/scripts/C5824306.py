'''
Created on Apr 27, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10863
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5824306
TestCase Name = Verify default User Preferences values
'''

import unittest, time, re
from common.pages import visualization_resultarea, visualization_ribbon
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C5824306_TestClass(BaseTestCase):

    def test_C5824306(self):
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
            Step 01:Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.invoke_infoassist_api_login('report','ibisamp/car','P292_S10863/G432726', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        
        """
           Step 02:Click "IA" > "Options".
        """
        ribbonobj.select_tool_menu_item("menu_options")
        
        """ 
            Step 03:Verify the "Options" window is displayed.
        """
        options_css_obj="#dlgPrefs div[class*='active'] [class*='caption'] [class*='bi-label']"
        utillobj.verify_popup(options_css_obj, "Step 03:01 : Verify the Options window is displayed..", caption_css=options_css_obj, caption_text='Options')
        
        """ 
            Step 04:Click "Report output type" (dropdown).
        """
        report_output_css=self.driver.find_element_by_css_selector("#dlgPrefs #dlgPrefsOutputFormatTable")
        utillobj.default_left_click(object_locator=report_output_css)
        time.sleep(1)
            
        """ 
            Step 05:Verify it contains the following options:
        """
        menu_items=driver.find_elements_by_css_selector("div[id^='BiPopup'][style*='inherit'] div[id^='BiComboBoxItem']")
        expected_popup_list=['HTML', 'PDF', 'PowerPoint (pptx)', 'Excel (xlsx)', 'Excel (xlsx Formula)', 'Excel', 'Excel (Formula)', 'Excel (csv)', 'Active Report']
        actual_popup_list=[el.text.strip() for el in menu_items  if bool(re.match('\S+', el.text.strip()))]
        print(actual_popup_list)
        utillobj.as_List_equal(expected_popup_list, actual_popup_list, "Step 05:01: Verify List of Values")
        utillobj.default_left_click(object_locator=report_output_css)
        
        """ 
            Step 06:Select "Chart output type" dropdown.
        """
        report_output_css=self.driver.find_element_by_css_selector("#dlgPrefs #dlgPrefsOutputFormatChart")
        utillobj.default_left_click(object_locator=report_output_css)
        time.sleep(1)
        
        """ 
            Step 07:Verify it contains the following options:
        """
        menu_items=driver.find_elements_by_css_selector("div[id^='BiPopup'][style*='inherit'] div[id^='BiComboBoxItem']")
        expected_popup_list=['HTML', 'HTML5', 'PDF', 'PowerPoint (pptx)', 'Excel (xlsx)', 'Excel', 'Active Report']
        actual_popup_list=[el.text.strip() for el in menu_items  if bool(re.match('\S+', el.text.strip()))]
        utillobj.as_List_equal(expected_popup_list, actual_popup_list, "Step 07:01: Verify List of Values")
        utillobj.default_left_click(object_locator=report_output_css)
        """ 
            Step 08:Select "Document output type" dropdown.
        """ 
        report_output_css=self.driver.find_element_by_css_selector("#dlgPrefs #dlgPrefsComposeOutputType")
        utillobj.default_left_click(object_locator=report_output_css)
        time.sleep(1)
            
        """ 
            Step 09:Verify it contains the following options.
        """
        menu_items=driver.find_elements_by_css_selector("div[id^='BiPopup'][style*='inherit'] div[id^='BiComboBoxItem']")
        expected_popup_list=['HTML', 'PDF', 'PowerPoint (pptx)', 'Excel (xlsx)', 'Excel (xlsx Formula)', 'Excel', 'Excel (Formula)', 'Active Report']
        actual_popup_list=[el.text.strip() for el in menu_items  if bool(re.match('\S+', el.text.strip()))]
        utillobj.as_List_equal(expected_popup_list, actual_popup_list, "Step 08:01: Verify List of Values")
        utillobj.default_left_click(object_locator=report_output_css)
        
        """ 
            Step 10:Click "Cancel".
        """
        cancel_btn_css=self.driver.find_element_by_css_selector("#dlgPrefsoptionsCancel")
        utillobj.click_on_screen(cancel_btn_css, "middle", 0)
        
        """ 
            Step 11:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()