'''
Created on Jan 02, 2018

@author: Nasir
'''
import unittest,time
from common.lib import utillity
from common.lib import core_utility
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon

class C2348454_TestClass(BaseTestCase):


    def test_C2348454(self):
        
        """
        Class & Objects
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        
        """
        Testcase Variable
        """
        Test_Case_ID = 'C2348454'
        long_wait=120
        
        
        """    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is): http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite    """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_binning_1', 'mrid', 'mrpass')
        utillobj.wait_for_page_loads(20)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1,long_wait)
        
        """    2. Right click Product>Model>Attributes> Price,Dollars > Create Bins...     """
        metaobj.datatree_field_click("Price,Dollars",1,1, "Create Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        resultobj.wait_for_property(parent_css, 1,long_wait)
        
        """    3. Set bin width '1000'    """
        """    4. Click Format button > Select Filed type "Integer", Use comma checkbox and Currency symbol "Floating Currency" > OK    """
        """    5. Click OK    """
        metaobj.create_bin("PRICE_DOLLARS_BIN_1", bin_format_btn=True, field_type='Integer', check_box_list=['Use Comma (C)'], currency_symbol='Floating Currency' ,ok_btn=True, bin_width='100')
        
        """    6. Drag and drop "PRICE_DOLLARS_BIN_1" to Color bucket    """
        metaobj.drag_drop_data_tree_items_to_query_tree('Dimensions->PRICE_DOLLARS_BIN_1', 1, 'Color', 0)
        utillobj.synchronize_with_visble_text('#queryTreeWindow', 'PRICE_DOLLARS_BIN_1', long_wait)
        
        """    7. Drag and drop "PRICE_DOLLARS_BIN_1" to filter pane    """
        metaobj.drag_drop_data_tree_items_to_filter('Dimensions->PRICE_DOLLARS_BIN_1', 1)
        utillobj.synchronize_with_number_of_element('#avFilterOkBtn', 1, long_wait)
                
        """    8. Set filter condition "greater or equal to 1000"    """
        """    9. Click OK    """
        metaobj.create_visualization_filters('numeric', ['Operator','Greater than or equal to'], ['From','1000'])
        utillobj.synchronize_until_element_disappear('#avFilterOkBtn', long_wait) 
        utillobj.synchronize_with_number_of_element('#TableChart_1  svg g.risers >g>rect[class^="riser"]',8,long_wait)       
        
        """    10. Verify following preview displayed: Legend displays bin values $1,100, $1,200, etc.    """
        resultobj.verify_number_of_riser("TableChart_1", 1, 8, 'Step 10.01: Verify the total number of risers displayed on preview')
        color_list=[['0','bar_blue'],['1','pale_green'], ['2', 'dark_green'], ['3', 'pale_yellow'], ['4', 'brick_red'], ['5', 'orange']]
        for item in color_list:
            utillobj.verify_chart_color("TableChart_1", "riser!s"+item[0]+"!g0!mbar", item[1], "Step 10.02: Verify " + item[0] + " bar color")
        legend=['PRICE_DOLLARS_BIN_1', '$1,100', '$1,200', '$1,300', '$1,900', '$2,200', '$3,300', '$3,400', '$3,900']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step 10.03: Verify Legends Title")
        
        """    11. Click Run    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utill_obj.switch_to_new_window()
        utillobj.synchronize_with_number_of_element('#MAINTABLE_wbody1_f .risers rect',8,long_wait)
        
        """    12. Hover on the run time chart and verify tool tip values    """
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 8, 'Step 12.01: Verify the total number of risers displayed on preview')
        color_list=[['0','bar_blue'],['1','pale_green'], ['2', 'dark_green'], ['3', 'pale_yellow'], ['4', 'brick_red'], ['5', 'orange'], ['6', 'periwinkle_gray'], ['7', 'tea_green']]
        for item in color_list:
            utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s"+item[0]+"!g0!mbar", item[1], "Step 12.02: Verify " + item[0] + " bar color")
        legend=['PRICE_DOLLARS_BIN_1', '$1,100', '$1,200', '$1,300', '$1,900', '$2,200', '$3,300', '$3,400', '$3,900']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 12.03: Verify Legends Title")
        time.sleep(5)
#         ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
#         utillobj.take_screenshot(ele,'C2348454_Actual_step08', image_type='actual',x=1, y=1, w=-1, h=-1)
#         time.sleep(2)
        bar=['PRICE_DOLLARS_BIN_1:$1,900', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s3!g0!mbar!", bar,"Step 12.04: Verify bar value")
        time.sleep(5)
        core_utill_obj.switch_to_previous_window()
        
        """    13. Click Save in the toolbar > Save as "C2343108" > Click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """    14. Logout using API:- http://machine:port/alias/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    15. Restore saved fex using API:- http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10666%2FC2343108.fex    """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10664_binning_1', mrid='mrid', mrpass='mrpass')
        utillobj.wait_for_page_loads(20)
        parent_css="#TableChart_1 svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1,long_wait)
        resultobj.verify_number_of_riser("TableChart_1", 1, 8, 'Step 15.01: Verify the total number of risers displayed on preview')
        color_list=[['0','bar_blue'],['1','pale_green'], ['2', 'dark_green'], ['3', 'pale_yellow'], ['4', 'brick_red'], ['5', 'orange'], ['6', 'periwinkle_gray'], ['7', 'tea_green']]
        for item in color_list:
            utillobj.verify_chart_color("TableChart_1", "riser!s"+item[0]+"!g0!mbar", item[1], "Step 15.02: Verify " + item[0] + " bar color")
        legend=['PRICE_DOLLARS_BIN_1', '$1,100', '$1,200', '$1,300', '$1,900', '$2,200', '$3,300', '$3,400', '$3,900']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step 15.03: Verify Legends Title")
         
        """    16. Logout using API:- http://machine:port/alias/service/wf_security_logout.jsp    """
           
if __name__ == "__main__":
    unittest.main()