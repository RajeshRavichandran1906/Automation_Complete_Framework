'''
Created on Jan 10, 2018
@author: Nasir
'''
import unittest
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization

class C2348421_TestClass(BaseTestCase):

    def test_C2348421(self):
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        oVisualization=Visualization(self.driver)
        
        """    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is): http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite    """
        oVisualization.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """    2. Right click "Gross Profit" > Create Bins    """
        oVisualization.right_click_on_datetree_item("Gross Profit", 1, "Create Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        oVisualization.wait_for_number_of_element(parent_css, 1)
        
        """    3. Click Format button    """
        format_btn_obj=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[class*='bi-window active window'] #qbBinBtnFormat")
        format_btn_obj.click()
        parent_css= "div[id^='QbDialog'] div[class*='bi-window active window'] #fmtDlgOk"
        oVisualization.wait_for_number_of_element(parent_css, 1)
        
        """    4. Verify Format dialog opens    """
        expected_format_title="Field Format Options for (GROSS_PROFIT_US_BIN_1)"
        actual_format_title=driver.find_element_by_css_selector("div[id^='QbDialog'] div[class*='bi-window active window'] div[class*='window-caption']").text.strip()
        utillobj.asequal(actual_format_title, expected_format_title, "Step 04a: Verify the Format dialog Opens :: '" + actual_format_title + "'")
        
        """    5. Verify list of field type in format dialog - Only numeric formats are available (no alphanumeric or dates)    """
        expected_format_field_type_list=['Floating point', 'Integer', 'Decimal', 'Packed']
        actual_format_field_type_list=[]
        parent_obj= driver.find_elements_by_css_selector("div[id^='QbDialog'] div[class*='bi-window active window']")[-1]
        elems=parent_obj.find_elements_by_css_selector("#format-types-list [id^='BiListItem']")
        for elem in elems:
            actual_format_field_type_list.append(elem.text.strip())
        utillobj.asequal(actual_format_field_type_list, expected_format_field_type_list, "Step 05a: Verify list of field type in format dialog - Only numeric formats are available (no alphanumeric or dates)")
            
        """    6. Click Cancel (2x)    """
        driver.find_element_by_css_selector("#fmtDlgCancel").click()
        #utillobj.click_type_using_pyautogui(oformat_Cancel_btn, leftClick=True)
        oVisualization.verify_bins_dialog(name_textbox_value='GROSS_PROFIT_US_BIN_1', btn_click='cancel', msg='Step 06')
               
        """    7. Logout using API - http://machine:port/alias/service/wf_security_logout.jsp    """
        
if __name__ == "__main__":
    unittest.main()