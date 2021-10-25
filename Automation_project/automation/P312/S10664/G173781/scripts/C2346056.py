'''
Created on Jan 8, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2346056
TestCase Name = Group option uses field name if there is no title in meta data
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_metadata
from common.lib import utillity


class C2346056_TestClass(BaseTestCase):

    def test_C2346056(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2346056'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/EMPDATA
        """
        utillobj.infoassist_api_login('idis','ibisamp/empdata','P312/S10664_paperclipping_1', 'mrid', 'mrpass')
        time.sleep(4)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1, expire_time=30)

        """
        Step 02: Double click "SALARY", "FIRSTNAME" add fields to chart
        """
        metaobj.datatree_field_click("SALARY", 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        
        metaobj.datatree_field_click("FIRSTNAME", 2, 1)
        time.sleep(4)
        
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 41)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'FIRSTNAME', "Step 02:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'SALARY', "Step 02:a(ii) Verify Y-Axis Title")
        expected_xval_list=['ADAM', 'ANNE', 'ANTHONY', 'ARLEEN', 'BEN', 'CAROL', 'CASSANDRA', 'CHRIS', 'DANIEL', 'DAVID', 'DORINA', 'ELAINE', 'ERIC', 'ERICA', 'ERWIN', 'EVELYN', 'HENRY', 'JEFF', 'JIM', 'JOHN', 'KAREN', 'KARL', 'KATE', 'KATRINA', 'LAURA', 'LOIS', 'MARCUS', 'MARIANNE', 'MARIE', 'MARK', 'MARSHALL', 'MICHAEL', 'PAMELA', 'PETER', 'ROSE', 'RUTH', 'TIM', 'VERONICA', 'WILLIAM', 'WILMA', 'YOLANDA']
        expected_yval_list=['0', '30K', '60K', '90K', '120K', '150K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 02:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 41, 'Step 02.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 02.c: Verify first bar color")
        time.sleep(5)
        bar=['FIRSTNAME:ANNE', 'SALARY:$26,400.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar", bar, "Step 02.d: Verify bar value")
        time.sleep(5)
        
        """
        Step 03: Lasso on few risers
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 41)
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g1!mbar!', target_tag='rect', target_riser='riser!s0!g14!mbar!')
        time.sleep(2)
        
        """
        Step 04: Verify the tool tip values displayed
        """
        resultobj.select_or_verify_lasso_filter(verify=['14 items selected', 'Filter Chart', 'Exclude from Chart', 'Group FIRSTNAME Selection'],msg='Step 04: Verify Tooltip shows option to Group FIRSTNAME Selection')
        query_filter_area_obj = self.driver.find_element_by_css_selector("#qbFilterBox")
        utillobj.click_on_screen(query_filter_area_obj, 'middle', click_type=0)
        
        """
        Step 05: Hover over on FIRSTNAME in query pane
        Step 06: Verify the tool tip values displayed in query pane value
        """
        expected_list=['Segment: EMPDATA', 'Name: FIRSTNAME', 'Alias: FN', 'Title: FIRSTNAME', 'Description: FIRSTNAME', 'Format: A10']
        metaobj.verify_querytree_tooltip("FIRSTNAME", 1, expected_list, 'Step 06: Verify the tool tip values displayed in query pane value')
        time.sleep(8)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele, Test_Case_ID+'_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 07: Logout using API (without saving)- http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()