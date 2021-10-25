'''
Created on Jan 5, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2346062
TestCase Name = Group option not available for numeric dimension
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, core_metadata
from common.lib import utillity


class C2346062_TestClass(BaseTestCase):

    def test_C2346062(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2346062'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        core_metaobj = core_metadata.CoreMetaData(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_paperclipping_1', 'mrid', 'mrpass')
#         visual.invoke_visualization_tool_using_api('new_retail/wf_retail_lite')
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 120)
        
        """
        Step 02: Double click "Revenue","ID Store (I9)"
        """
#         visual.add_field_using_double_click('Revenue', 1)
        metaobj.datatree_field_click("Revenue", 2, 1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 90)
        
#         visual.add_field_using_double_click('Sale,Year', 1)
        core_metaobj.collapse_data_field_section('Filters and Variables')
        metaobj.datatree_field_click("ID Store", 2, 1)
        parent_css='#TableChart_1 text[class*=xaxisOrdinal-title]'
        utillobj.synchronize_with_visble_text(parent_css, 'ID Store', 90)
        
        """
        Step 03: Verify following chart preview displayed
        """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'ID Store', "Step 03.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 03.02: Verify Y-Axis Title")
        expected_xval_list=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 03.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 87, 'Step 03.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 03.05: Verify first bar color")
#         bar=['ID Store:0', 'Revenue:$326,563,391.80', 'Filter Chart', 'Exclude from Chart']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 03.d: Verify bar value")
        
        """
        Step 04: Lasso on few risers in preview
        """
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g9!mbar!', target_tag='rect', target_riser='riser!s0!g23!mbar!')
        time.sleep(2)
        
        """
        Step 05: Verify Tooltip does not have option to group.
        """
        resultobj.select_or_verify_lasso_filter(verify=['12 item selected', 'Filter Chart', 'Exclude from Chart'], msg='Step 05.01: Verify following tool tip values displayed')
        time.sleep(8)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele, Test_Case_ID+'_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
        Step 06: Logout using API (without saving)- http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()