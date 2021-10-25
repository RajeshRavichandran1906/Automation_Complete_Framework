'''
Created on Jul 28, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2235071
TestCase Name = Funnel/Pyramid - Bar Chart failure. Proj. 159307
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_resultarea,active_chart_rollup,ia_resultarea
from common.lib import utillity

class C2235071_TestClass(BaseTestCase):

    def test_C2235071(self):
        TestCase_ID='C2235071'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        def verify_Bar_chart(step_no,vertical_bar=True):
            print("\n---------------------  Verifying Chart ---------------------\n")
            miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category, Product ID', 'Step '+step_no+'.1 : Verify Chart Title')
            tooltip1=['Unit Sales: 630K', 'X: Food/F103']
            tooltip2=['Dollar Sales: 7.7M', 'X: Food/F103']
            if vertical_bar :
                tooltip1=['Unit Sales, Food/F103: 630,054']
                tooltip2=['Dollar Sales, Food/F103: 7,749,902']
                result_obj.verify_xaxis_title('MAINTABLE_wbody0','Category : Product ID', 'Step '+step_no+'.2 : Verify X-Axis Title')
                
            expected_xval_list=['Coffee/C141','Coffee/C142','Coffee/C144','Food/F101','Food/F102','Food/F103','Gifts/G100','Gifts/G104','Gifts/G110','Gifts/G121']
            expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
            result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step '+step_no+'.3 :')
            result_obj.verify_riser_legends('MAINTABLE_wbody0',['Unit Sales','Dollar Sales'], 'Step '+step_no+'.4 : Verify chart legends label ')
            result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 20, 'Step '+step_no+'.5 : Verify number of risers')
            utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g5!mbar!', 'lochmara', 'Step '+step_no+'.6 : Verify chart color')
            utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s1!g5!mbar!', 'pale_green', 'Step '+step_no+'.7 : Verify chart color')
            miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s0!g5!mbar!',tooltip1,'Step '+step_no+'.11 : Verify chart tooptip value')
            miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s1!g5!mbar!',tooltip2,'Step '+step_no+'.12 : Verify chart tooptip value')
            miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],'Step '+step_no+'.13 : Verify Chart toolbar')
            miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],'Step '+step_no+'.14 : Verify Chart toolbar', custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
            miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],'Step '+step_no+'.15 : Verify Chart toolbar', custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)  
            ele=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
            utillobj.take_screenshot(ele,TestCase_ID+'_Actual_Step'+step_no, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        def verify_Funnel_and_Pyramid_Chart(step_no):
            print("\n---------------------  Verifying Chart ---------------------\n")
            miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category, Product ID', 'Step '+step_no+'.1 : Verify Chart Title')
            expected_ledend=['Coffee/C141','Coffee/C142','Coffee/C144','Food/F101','Food/F102','Food/F103','Gifts/G100','Gifts/G104','Gifts/G110','Gifts/G121']
            result_obj.verify_riser_legends('MAINTABLE_wbody0',expected_ledend, 'Step '+step_no+'.3 : Verify chart legends label ')
            ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10,'Step '+step_no+'.4 : Verify number of funnel chart path')
            utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mriser!', 'lochmara', 'Step '+step_no+'.5 : Verify chart color',attribute_type='fill')
            utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s1!g0!mriser!', 'pale_green', 'Step '+step_no+'.6 : Verify chart color')
            miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s0!g0!mriser!',['Coffee/C141','X: Unit Sales','Y: 309K'],'Step '+step_no+'.7 : Verify chart tooptip value')
            miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0','riser!s1!g0!mriser!',['Coffee/C142','X: Unit Sales','Y: 878K'],'Step '+step_no+'.8 : Verify chart tooptip value')
            miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],'Step '+step_no+'.9 : Verify Chart toolbar')
            miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],'Step '+step_no+'.10 : Verify Chart toolbar', custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
            miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],'Step '+step_no+'.11 : Verify Chart toolbar', custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
            ele=driver.find_element_by_css_selector("#MAINTABLE_wbody0")
            utillobj.take_screenshot(ele,TestCase_ID+'_Actual_Step'+step_no, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        01. Execute the attached repro - ahtml_chart.fex. This will create an initial Bar Chart.
        """
        utillobj.active_run_fex_api_login("ahtml-chart.fex", "S7074", 'mrid', 'mrpass')
        parent_css="#MAINTABLE_wbody0_f g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 18)
        time.sleep(3)
        
        """
        01.1 Verify Outpu Chart 
        """      
        verify_Bar_chart('01')
        
        """
        Step 02 : From the Bar Chart, select the Advanced Chart tab, then Charts, then select Funnel.Click OK.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0',5)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1','funnel')
        result_obj.wait_for_property("#MAINTABLE_wbody0_f g[class='legend'] text", 10)
        time.sleep(3)
        
        """
        Step 02.1 : Expect to see the following Funnel Chart.
        """
        verify_Funnel_and_Pyramid_Chart('02')
        
        """
        Step 03 : From the Funnel chart, select the Advanced Chart tab, then Charts, then select Pyramid chart. Click OK.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0',5)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1','pyramid')
        result_obj.wait_for_property("#MAINTABLE_wbody0_f g[class='legend'] text", 10)
        time.sleep(3)
        
        """
        Step 03.1 : Expect to see the following Pyramid Chart.
        """
        verify_Funnel_and_Pyramid_Chart('03')
        
        """
        Step 04 : From the Pyramid chart, select the Advanced Chart tab, then Charts, then select the first Bar Chart. Click OK.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0',5)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1','bar')
        result_obj.wait_for_property("#MAINTABLE_wbody0_f g[class='legend'] text", 2)
        time.sleep(3)
        
        """
        Step 04.1 : Expect to see the following Bar Chart.
        """
        verify_Bar_chart('04',False)
        
if __name__=='__main__' :
    unittest.main()