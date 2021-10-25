'''
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227697
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity

class C2227697_TestClass(BaseTestCase):
    def test_C2227697(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227697'
        bar=['Sale Year:2013', 'Product Category:Stereo Systems', 'Quantity Sold:100,263', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K']
        matrix_value=['2011', '2012', '2013', '2014', '2015', '2016']
        
        """    01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F    """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
              
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
         
        """    2. Double click "Quantity Sold", "Product,Category".     """
        metaobj.datatree_field_click("Quantity,Sold", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(8)
        
        """    3. Drag "Sale,Year" to Matrix-Columns.    """
        metaobj.datatree_field_click("Sale,Year", 1, 1, "Add To Query", "Columns")
        time.sleep(8)
        
        """    4. Verify the following chart is displayed.    """
        time.sleep(5)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c2!", bar, "Step04: Verify bar value")
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step04:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Quantity Sold', "Step04:a(ii) Verify Y-Axis Title")
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step04:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 42, 'Step04.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!r0!c0!", "lochmara", "Step04.c: Verify first bar color")
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", "Columns", "Sale Year", matrix_value, "Step04.d:")
        time.sleep(5)
        
        """    5. Click "Clear".    """
        ribbonobj.select_ribbon_item('Home', 'Clear')
        time.sleep(5)
        
        """    6. Verify "Warning" prompt appears.    """
        cap_css="div[id^='BiDialog']>div[class*='window-active'] [class*='caption'] [class*='bi-label']"
        cap_text='Warning'
        popup_css="div[id^='BiDialog']>div[class*='window-active'] [class='bi-component'] [class*='bi-label']"
        pop_text="Are you sure you would like to CLEAR the selected Component?"
        utillobj.verify_popup("div[id^='BiDialog']>div[class*='active']", "Step06: Verify 'Warning' prompt appears", caption_css=cap_css, caption_text=cap_text, popup_text_css=popup_css, popup_text=pop_text)
        
        """    7. Click "OK".    """
        btn_css="div[id^='BiDialog']>div[class*='window-active'] div[class=bi-button-label]"
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('OK')].click()
        
        """    8. Verify the Query bucket have been cleared.    """
        metaobj.verify_query_pane_field('Columns', 'Axis', 1, "Step08a: Verify Sale,Year is cleared from Query pane")
        metaobj.verify_query_pane_field('Vertical Axis', 'Horizontal Axis', 1, "Step08b: Verify Quantity,Sold is cleared from Query pane")
        metaobj.verify_query_pane_field('Horizontal Axis', 'Marker', 1, "Step08c: Verify Product Category is cleared from Query pane")
         
        """    9. Verify the following chart is displayed.    """
        def_chart=driver.find_element_by_css_selector("#TableChart_1 svg>g>text.title").text.strip()
        utillobj.asequal("Drop Measures or Sorts into the Query Pane", def_chart, "Step 09: Verify the default Chart displayed on Preview")
        time.sleep(1)
        ele=driver.find_element_by_css_selector("#TableChart_1")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step09', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    10. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
                     
        
if __name__ == '__main__':
    unittest.main()

