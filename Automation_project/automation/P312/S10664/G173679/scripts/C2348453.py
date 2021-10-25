'''
Created on Jan 02, 2018

@author: Nasir
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.lib.basetestcase import BaseTestCase

class C2348453_TestClass(BaseTestCase):


    def test_C2348453(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        Test_Case_ID = 'C2348453'
        
        
        """    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is): http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite    """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_binning_1', 'mrid', 'mrpass')
        time.sleep(4)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1,expire_time=100)
        time.sleep(8)
        
        """    2. Right click Product>Model>Attributes> Price,Dollars > Create Bins...     """
        metaobj.datatree_field_click("Price,Dollars",1,1, "Create Bins...")
        time.sleep(2)
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        resultobj.wait_for_property(parent_css, 1)
        
        """    3. Set bin width '1000'    """
        """    4. Click Format button > Select Filed type "Integer", Use comma checkbox and Currency symbol "Floating Currency" > OK    """
        """    5. Click OK    """
        metaobj.create_bin("PRICE_DOLLARS_BIN_1", bin_format_btn=True, field_type='Integer', check_box_list=['Use Comma (C)'], currency_symbol='Floating Currency' ,ok_btn=True, bin_width='1000')
        
        """    6. Drag and drop "PRICE_DOLLARS_BIN_1" to Rows    """
        metaobj.datatree_field_click('Dimensions->PRICE_DOLLARS_BIN_1', 1, 1, 'Add To Query', 'Rows')
        
        """    7. Verify bin added to rows bucket and Labels for rows display $0, $1,000, etc.    """
        metaobj.verify_query_pane_field('Rows', 'PRICE_DOLLARS_BIN_1', 1, "Step 07a: Verify PRICE_DOLLARS_BIN_1 is visible underneath Rows")
        time.sleep(2)
        expected_label= ['$0', '$1,000', '$2,000', '$3,000']
        resultobj.verify_visualization_row_column_header_labels('TableChart_1','Rows','PRICE_DOLLARS_BIN_1',expected_label, "Step 07b:")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 07c: Verify first bar color")
        
        """    8. Click Run    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        parent_css="#MAINTABLE_wbody1 svg>g rect[class^='riser!']"
        resultobj.wait_for_property(parent_css, 4, expire_time=30)       
        
        expected_label= ['$0', '$1,000', '$2,000', '$3,000']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Rows','PRICE_DOLLARS_BIN_1',expected_label, "Step 08a:")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r2!c0!", "bar_blue", "Step 08b: Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 4, 'Step 08ca: Verify number of risers displayed')
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele,'C2348453_Actual_step08', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    9. Hover on the run time chart and verify tool tip values    """
        expected_tooltip=['PRICE_DOLLARS_BIN_1:$1,000', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar!r1!c0!",expected_tooltip, "Step 09a: verify the default tooltip values")       
        time.sleep(5)
        driver.close()
        time.sleep(2)
        utillobj.switch_to_window(0)
        
        """    10. Click Save in the toolbar > Save as "C2348453" > Click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """    11. Logout using API: http://machine:port/alias/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    12. Restore saved fex using API - http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10666%2FC2348453.fex    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10664_binning_1', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1 svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 4,expire_time=100)
        time.sleep(3)
        expected_label= ['$0', '$1,000', '$2,000', '$3,000']
        resultobj.verify_visualization_row_column_header_labels('TableChart_1','Rows','PRICE_DOLLARS_BIN_1',expected_label, "Step 12a:")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 12b: Verify first bar color")
        resultobj.verify_number_of_riser("TableChart_1" , 1, 4, 'Step 12c: Verify number of risers displayed')
        
        """    13. Logout using API: http://machine:port/alias/service/wf_security_logout.jsp    """
        
        
if __name__ == "__main__":
    unittest.main()