
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, active_chart_rollup
from common.lib import utillity

class C2197658_TestClass(BaseTestCase):

    def test_C2197658(self):
        """
            TESTCASE VARIABLES
        """
#         Test_Case_ID = 'C2197658'
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        """
        Step 01:Execute the attached repro - 137842.fex.
        """
        utillobj.active_run_fex_api_login("137842.fex", "S7074", 'mrid', 'mrpass')      
        parent_css="#MAINTABLE_wbody0_f svg g>text"
        result_obj.wait_for_property(parent_css,19,expire_time=100)  
        time.sleep(12)
        
        """
        Step 01.1 : Expect to see the following Bar Chart.
        """ 
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST by COUNTRY, CAR", "Step 01.01 : Verify chart title ")
        result_obj.verify_xaxis_title("MAINTABLE_wbody0 ","COUNTRY : CAR","Step 01.02 : Verify Xaxis title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0 ","DEALER_COST","Step 01.03 :Verify Yaxis title")
        expected_xval_list=['ENGLAND/JAGUAR','ENGLAND/JENSEN', 'ENGLAND/TRIUMPH', 'FRANCE/PEUGEOT', 'ITALY/ALFA ROMEO','ITALY/MASERATI','JAPAN/DATSUN','JAPAN/TOYOTA','W GERMANY/AUDI','W GERMANY/BMW']
        expected_yval_list=['0','10K','20K','30K','40K','50K','60K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0_f', expected_xval_list, expected_yval_list," Step 01.04 : Verify chart XYlabels")
        result_obj.verify_number_of_riser("MAINTABLE_wbody0",1,10,"Step 01.05: Verify number of riser")
        utillobj.verify_chart_color("MAINTABLE_wbody0","riser!s0!g5!mbar!",'cerulean_blue',"Step 01.06:Verify Chart color")
        expected_tooltip_list=['DEALER_COST, ITALY/MASERATI: 25,000']
        miscelaneousobj.verify_active_chart_tooltip("MAINTABLE_wbody0","riser!s0!g5!mbar!", expected_tooltip_list,"Step 01.07:Verify active chart tooltip")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 01.08 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.09: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        ele=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0_ft tbody")
        utillobj.click_on_screen(ele, coordinate_type='middle')
        time.sleep(2)
        
        """
        Step 02:Now click on first icon in chart tool bar, and deselect 'DEALER COST' from 'Add (Y)'
        """
        
        rollobj.select_chartmenubar_option('MAINTABLE_0', 0, 'Add (Y)->DEALER_COST', 0, custom_css='cpop')
        time.sleep(4)
        actual=driver.find_element_by_css_selector("#MAINTABLE_wbody0 span").text.strip()
        expected="No data to chart"
        utillobj.asequal(actual,expected,"Step 02.01 :Verify whether it displays 'No data to Chart")
                         
        """
        Step 03:Reverse the action of step 3, again adding Dealer_Cost via the More Options/add(y) option.
        """
        ele=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 span")
        utillobj.click_on_screen(ele, coordinate_type='middle')
        time.sleep(2)
        
        rollobj.select_chartmenubar_option('MAINTABLE_0', 1, 'Add (Y)->DEALER_COST', 0, custom_css='cpop')
        time.sleep(4)
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST by COUNTRY, CAR", "Step 03.01 : Verify chart title ")
        result_obj.verify_xaxis_title("MAINTABLE_wbody0 ","COUNTRY : CAR","Step 03.02 : Verify Xaxis title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0 ","DEALER_COST","Step 03.03 :Verify Yaxis title")
        expected_xval_list=['ENGLAND/JAGUAR','ENGLAND/JENSEN', 'ENGLAND/TRIUMPH', 'FRANCE/PEUGEOT', 'ITALY/ALFA ROMEO','ITALY/MASERATI','JAPAN/DATSUN','JAPAN/TOYOTA','W GERMANY/AUDI','W GERMANY/BMW']
        expected_yval_list=['0','10K','20K','30K','40K','50K','60K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0_f', expected_xval_list, expected_yval_list," Step 03.04 : Verify chart XYlabels")
        result_obj.verify_number_of_riser("MAINTABLE_wbody0",1,10,"Step 03.05: Verify number of riser")
        utillobj.verify_chart_color("MAINTABLE_wbody0","riser!s0!g5!mbar!",'cerulean_blue',"Step 03.06:Verify Chart color")
        expected_tooltip_list=['DEALER_COST, ITALY/MASERATI: 25,000']
        miscelaneousobj.verify_active_chart_tooltip("MAINTABLE_wbody0","riser!s0!g5!mbar!", expected_tooltip_list,"Step 03.07:Verify active chart tooltip")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 03.08 : Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.09: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.10: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)

         
if __name__ == '__main__':
    unittest.main()