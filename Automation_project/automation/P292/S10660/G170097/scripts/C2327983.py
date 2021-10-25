'''
Created on Dec 13, 2017

@author: Praveen Ramkumar
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2327983
Testcase Name : Verify push buttons and split menus in default IA Theme
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.color import Color


class C2327983_TestClass(BaseTestCase):

    def test_C2327983(self):
        
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
            Step 01:Launch the IA API with wf_retail_lite, Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2F
        """  
               
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P292/S10660_infoassist_2', 'mrid', 'mrpass')
        parent_css="div[align='justify']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
            Step 02:Double-click "Cost of Goods" from Sales Measures
        """
        metaobj.datatree_field_click('Cost of Goods', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=15, string_value='Cost of Goods')
        
        """
            Step 03:Double-click "Product,Subcategory", located under Product Dimension
        """
        metaobj.datatree_field_click('Product,Subcategory', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=15, string_value='Product,Subcategory', with_regular_exprestion=True)
        
        """
            Step 04:Select Format Tab > Click on "Table of Contents"
        """
        
        ribbonobj.select_ribbon_item('Format','table_of_contents')
        
        """
            Step 05:Verify button appears toggled ON (with blue color)
        """
        
        ele=driver.find_element_by_css_selector("#FormatReportToc")
        utillobj.verify_checked_class_property(ele, "Step 5:#FormatReportToc", check_property=True) 
        time.sleep(5)
        ele1=driver.find_element_by_css_selector("[id='FormatReportToc']")
        actual_color = Color.from_string(ele1.value_of_css_property('background-color')).rgba
        expected_color=utillobj.color_picker('Pale_Cornflower_Blue', 'rgba')
        print(actual_color)
        print(expected_color)
        utillobj.asequal(actual_color,expected_color,"Step 5:Verify button appears toggled ON (with blue color)")
        
        """
            Step 06:Hover over the "InfoMini" button in the Format Tab
        """
        
        ribbonobj.select_ribbon_item('Format','infomini')
        
        
        """
            Step 07:Verify button is highlighted with blue color
        """
        ele2=driver.find_element_by_css_selector("[id='FormatApplicationRibbonEnable']")
        utillobj.verify_checked_class_property(ele2, "Step 07:InfoMini", check_property=True) 
        time.sleep(5)
        elem=self.driver.find_element_by_css_selector("[id='FormatApplicationRibbonEnable']")
        utillobj.click_on_screen(elem, 'middle', click_type=3)
        time.sleep(5)
        y=driver.find_element_by_css_selector("[id='FormatApplicationRibbonEnable']")
        actual_color = Color.from_string(y.value_of_css_property('background-color')).rgba
        expected_color=utillobj.color_picker('Pale_Cornflower_Blue', 'rgba')
         
        """
            Step 08:Hover over the split menu (arrow) in the "InfoMini" button
        """        
        ribbonobj.select_ribbon_item('Format','infomini_arrow')
        
        """
            Step 09:Verify button is highlighted with blue color
        """  
        elem=self.driver.find_element_by_css_selector("#FormatApplicationRibbonEnableMenuBtn div[class$='drop-down-arrow']")
        utillobj.click_on_screen(elem, 'middle', click_type=3)
        time.sleep(5)
        z=driver.find_element_by_css_selector("[id='FormatApplicationRibbonEnable']")
        actual_color = Color.from_string(z.value_of_css_property('background-color')).rgba
        expected_color=utillobj.color_picker('Pale_Cornflower_Blue', 'rgba')
 
        """
            Step 10:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()        