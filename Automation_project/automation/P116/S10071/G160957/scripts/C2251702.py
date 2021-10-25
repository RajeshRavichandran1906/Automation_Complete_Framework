'''
Created on 24-Jan-2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251702
TestCase Name = Active Document Filtering Issues Raised By Management (ACT-323).
'''
import unittest, time
from common.lib import utillity
from common.pages import ia_resultarea, active_miscelaneous,visualization_resultarea,active_chart_rollup
from common.lib.basetestcase import BaseTestCase

class C2251702_TestClass(BaseTestCase):

    def test_C2251702(self):
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_resultobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        active_mis_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_chartobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        """
        Step01: Execute the attached repro act-323.fex
        """         
        utillobj.active_run_fex_api_login('act-323.fex','S10071_4','mrid','mrpass')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0 ", 1, 70)        
        
        def verify_bar(step_no=None, bar_expected_number=None, xaxis_title=None,yaxis_title=None, x_label=None, y_label=None, bar_raiser_class=None, bar_expected_tooltip_list=None, bar_chart_title=None,filter_menu_in_chart=None,bar_color=None ):
                             
            '''verify bar-chart'''
#             
            vis_resultobj.verify_number_of_riser('MAINTABLE_wbody0', 1, bar_expected_number, "Step "+str(step_no)+".1: Verify number of riser in bar chart.")
            vis_resultobj.verify_xaxis_title('MAINTABLE_wbody0', xaxis_title, "Step "+str(step_no)+".2: Verify bar x-axis_title.")
            vis_resultobj.verify_yaxis_title('MAINTABLE_wbody0', yaxis_title, "Step "+str(step_no)+".3: Verify y-axis_title.")
            vis_resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', x_label, y_label, "Step "+str(step_no)+".4: Verify xy-axis_Labels.")
            active_mis_obj.verify_chart_title('MAINTABLE_wbody0', bar_chart_title, "Step "+str(step_no)+".5: Verify bar chart title.")
            active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu0 ', filter_menu_in_chart, "Step "+str(step_no)+".6: Verify bar menu bar.", custom_css="[title]")
            active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step "+str(step_no)+".7: Verify bar menu sum text.", custom_css=".arChartMenuBarContainer .tabPagingText1 [id*='SUM'] td[valign]", text=True)
#             vis_resultobj.verify_default_tooltip_values('MAINTABLE_wbody0', bar_raiser_class, bar_expected_tooltip_list, "Step "+str(step_no)+".8: Verify bar tooltip.")
            utillobj.verify_chart_color('MAINTABLE_wbody0', bar_raiser_class, bar_color, "Step "+str(step_no)+".8: Verify bar color.")
            
        def verify_pie(step_no,css,pie_expected_number=None, pie_raiser_class=None, pie_expected_tooltip_list=None, pie_datalable=None, pie_chart_title=None,
                             expected_legend_list=None, filter_menu_in_chart=None, pie_legend=None, pie_color=None):
            
            '''verify pie-chart'''
            ia_resultobj.verify_number_of_chart_segment("MAINTABLE_wbody"+str(css), pie_expected_number, "Step "+str(step_no)+".1: Verify number of riser in bar chart.")
            vis_resultobj.verify_riser_pie_labels_and_legends("MAINTABLE_wbody"+str(css), pie_legend, "Step "+str(step_no)+".2: Verify pie legends.")
            vis_resultobj.verify_data_labels("MAINTABLE_wbody"+str(css), pie_datalable, "Step "+str(step_no)+".3: Verify pie data label.", custom_css=".chartPanel text[class*='mdataLabels']")
            active_mis_obj.verify_chart_title("MAINTABLE_wbody"+str(css), pie_chart_title, "Step "+str(step_no)+".4: Verify pie chart title.")
            active_mis_obj.verify_arChartToolbar("MAINTABLE_wmenu"+str(css), filter_menu_in_chart, "Step "+str(step_no)+".5: Verify bar menu bar.", custom_css="[title]")
            active_mis_obj.verify_arChartToolbar("MAINTABLE_wmenu"+str(css), ['Sum'],"Step "+str(step_no)+".6: Verify bar menu sum text.", custom_css=".arChartMenuBarContainer .tabPagingText1 [id*='SUM'] td[valign]", text=True)
            vis_resultobj.verify_default_tooltip_values("MAINTABLE_wbody"+str(css), pie_raiser_class, pie_expected_tooltip_list, "Step "+str(step_no)+".7: Verify pie tooltip.")
            if expected_legend_list!=None:
                vis_resultobj.verify_legends(expected_legend_list, "#MAINTABLE_wbody"+str(css), legend_length=4, msg="Step "+str(step_no)+".8: Verify pie legends.")
            parent_elem = self.driver.find_element_by_id("MAINTABLE_wbody"+str(css))
            utillobj.click_on_screen(parent_elem, 'top_middle', click_type=0)
            time.sleep(1)
            utillobj.verify_chart_color("MAINTABLE_wbody"+str(css), pie_raiser_class, pie_color, "Step "+str(step_no)+".9: Verify pie color.")
            
        step_no=1.1
        bar_expected_number=75
        xaxis_title='Country : Product Category'
        yaxis_title='Line Total'
        x_label=['Canada','Canada','Canada','Canada','Canada']
        y_label=['0','50M','100M','150M','200M','250M','300M']
        bar_chart_title='Line Total by Country, Product Category'
        bar_raiser_class="riser!s0!g1!mbar"
        bar_expected_tooltip_list=['Line Total, Canada/Audio Systems:15,132,844.00']
        bar_color='cerulean_blue_1'
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation']
         
        verify_bar(step_no,bar_expected_number,xaxis_title, yaxis_title, x_label, y_label, bar_raiser_class, bar_expected_tooltip_list, bar_chart_title,filter_menu_in_chart,bar_color)
        step_no=1.2
        pie_expected_number=5
        pie_legend=['Line Total']
        pie_datalable=['12%', '4%', '6%','4%','74%']
        pie_chart_title='Line Total by Country'
        pie_raiser_class="riser!s0!g0!mwedge"
        pie_expected_tooltip_list=['Canada:181.7M (11.63%)']
        expected_legend_list=['Canada','France','Germany','Spain','United States']
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation']
        pie_color='cerulean_blue_1'
 
        verify_pie(step_no,1,pie_expected_number, pie_raiser_class, pie_expected_tooltip_list, pie_datalable, pie_chart_title, expected_legend_list, filter_menu_in_chart, pie_legend=pie_legend, pie_color=pie_color)
         
        step_no=1.3
        pie_expected_number=15
        pie_legend=['Line Total']
        pie_datalable=['3%', '8%', '3%', '21%', '24%', '12%', '1%', '1%', '3%', '3%', '1%', '2%', '5%', '11%', '1%']
        pie_chart_title='Line Total by Product Category'
        pie_raiser_class="riser!s0!g0!mwedge"
        pie_expected_tooltip_list=['Amplifiers/PreAmps/Tuners:42.4M (2.71%)']
        expected_legend_list=['Amplifiers', 'Audio', 'CD Players', 'DVD', 'DVD']
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation']
        pie_color='cerulean_blue_1'
 
        verify_pie(step_no,2,pie_expected_number, pie_raiser_class, pie_expected_tooltip_list, pie_datalable, pie_chart_title, expected_legend_list, filter_menu_in_chart, pie_legend=pie_legend, pie_color=pie_color)
         
        """
        Step02: From the bottom left PIE chart, left click on the United States slice and select Exclude from Chart.
        """
        vis_resultobj.create_lasso('MAINTABLE_wbody1', 'path', 'riser!s4!g0!mwedge', offsetx=5, offsety=5)
        vis_resultobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        wait_css="#MAINTABLE_1 [class*='legend-labels!s0!']"
        wait_text='Canada'
        utillobj.synchronize_with_visble_text(wait_css, wait_text, 25)
        
        
        """
        Expect to see the Document, now with the United States Bars and the PIE slice for United States excluded.
        Also expect to see the legend for the PIE chart altered and a Filter icon appear at the top.
        Notice that it's easier to see the remaining Bars.
        """         
        step_no=2.1
        bar_expected_number=60
        xaxis_title='Country : Product Category'
        yaxis_title='Line Total'
        x_label=['Canada','Canada','Canada','Canada','Canada']
        y_label=['0','10M','20M','30M','40M','50M']
        bar_chart_title='Line Total by Country, Product Category'
        bar_raiser_class="riser!s0!g1!mbar"
        bar_expected_tooltip_list=['Line Total, Canada/Audio Systems:15,132,844.00']
        bar_color='cerulean_blue_1'
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Remove Filter']
        
        verify_bar(step_no,bar_expected_number,xaxis_title, yaxis_title, x_label, y_label, bar_raiser_class,bar_expected_tooltip_list, bar_chart_title,filter_menu_in_chart,bar_color)
        
        step_no=2.2
        pie_expected_number=4
        pie_legend=['Line Total']
        pie_datalable=['45%', '16%', '21%', '17%']
        pie_chart_title='Line Total by Country'
        pie_raiser_class="riser!s0!g0!mwedge"
        pie_expected_tooltip_list=['Canada:181.7M (45.10%)']
        expected_legend_list=['Canada','France','Germany','Spain']
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Remove Filter']
        pie_color='cerulean_blue_1'
 
        verify_pie(step_no,1,pie_expected_number, pie_raiser_class, pie_expected_tooltip_list, pie_datalable, pie_chart_title, expected_legend_list, filter_menu_in_chart, pie_legend=pie_legend, pie_color=pie_color)
         
        step_no=2.3
        pie_expected_number=15
        pie_legend=['Line Total']
        pie_datalable=['3%', '8%', '3%', '21%', '24%', '12%', '1%', '1%', '3%', '3%', '1%', '2%', '5%', '11%', '1%']
        pie_chart_title='Line Total by Product Category'
        pie_raiser_class="riser!s0!g0!mwedge"
        pie_expected_tooltip_list=['Amplifiers/PreAmps/Tuners:42.4M (2.71%)']
        expected_legend_list=['Amplifiers', 'Audio', 'CD Players', 'DVD', 'DVD']
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation','Remove Filter']
        pie_color='cerulean_blue_1'
 
        verify_pie(step_no,2,pie_expected_number, pie_raiser_class,pie_expected_tooltip_list, pie_datalable, pie_chart_title, expected_legend_list, filter_menu_in_chart, pie_legend=pie_legend, pie_color=pie_color)
        
        """
        Step03: From the bottom right PIE chart, left click the slice at the 3-o'clock for DVD, which shows 21%.
        Select Exclude from chart.
        """
        vis_resultobj.create_lasso('MAINTABLE_wbody2', 'path', 'riser!s3!g0!mwedge', offsetx=5, offsety=5)
        vis_resultobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        wait_css="#MAINTABLE_2 [class*='legend-labels!s3!']"
        wait_text='DVD Camcorders'
        utillobj.synchronize_with_visble_text(wait_css, wait_text, 25)
        
        
        step_no=3.1
        bar_expected_number=56
        xaxis_title='Country : Product Category'
        yaxis_title='Line Total'
        x_label=['Canada','Canada','Canada','Canada','Canada']
        y_label=['0','10M','20M','30M','40M','50M']
        bar_chart_title='Line Total by Country, Product Category'
        bar_raiser_class="riser!s0!g1!mbar"
        bar_expected_tooltip_list=['Line Total, Canada/Audio Systems:15,132,844.00']
        bar_color='cerulean_blue_1'
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Remove Filter']
        
        verify_bar(step_no,bar_expected_number,xaxis_title, yaxis_title, x_label, y_label, bar_raiser_class, bar_expected_tooltip_list, bar_chart_title,filter_menu_in_chart,bar_color)
        
        step_no=3.2
        pie_expected_number=4
        pie_legend=['Line Total']
        pie_datalable=['45%', '16%', '21%', '17%']
        pie_chart_title='Line Total by Country'
        pie_raiser_class="riser!s0!g0!mwedge"
        pie_expected_tooltip_list=['Canada:181.7M (45.10%)']
        expected_legend_list=['Canada','France','Germany','Spain']
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Remove Filter']
        pie_color='cerulean_blue_1'
 
        verify_pie(step_no,1,pie_expected_number, pie_raiser_class, pie_expected_tooltip_list, pie_datalable,pie_chart_title, expected_legend_list, filter_menu_in_chart, pie_legend=pie_legend,pie_color=pie_color)
         
        step_no=3.3
        pie_expected_number=14
        pie_legend=['Line Total']
        pie_datalable=['3%', '10%', '4%', '31%', '15%', '1%', '2%', '4%', '4%', '1%', '3%', '7%', '14%', '2%']
        pie_chart_title='Line Total by Product Category'
        pie_raiser_class="riser!s0!g0!mwedge"
        pie_expected_tooltip_list=['Amplifiers/PreAmps/Tuners:42.4M (3.44%)']
        expected_legend_list=['Amplifiers', 'Audio', 'CD Players', 'DVD', 'Digital']
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation','Remove Filter']
        pie_color='cerulean_blue_1'
 
        verify_pie(step_no,2,pie_expected_number, pie_raiser_class, pie_expected_tooltip_list, pie_datalable,pie_chart_title, expected_legend_list, filter_menu_in_chart, pie_legend=pie_legend,pie_color=pie_color)
        
        """
        Step04: Back on the Bar Chart, left-click the second Bar for 
        Canada/Audio Systems. 
        Select Exclude from Chart.
        """
        vis_resultobj.create_lasso('MAINTABLE_wbody0', 'rect', 'riser!s0!g1!mbar', offsetx=5, offsety=5)
        vis_resultobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0 [class*='xaxisOrdinal-labels!g']", 55, 25)
        
        step_no=4.1
        bar_expected_number=55
        xaxis_title='Country : Product Category'
        yaxis_title='Line Total'
        x_label=['Canada','Canada','Canada','Canada','Canada']
        y_label=['0','10M','20M','30M','40M','50M']
        bar_chart_title='Line Total by Country, Product Category'
        bar_raiser_class="riser!s0!g1!mbar"
        bar_expected_tooltip_list=['Line Total, Canada/CD Players and Recorders:5,600,154.00']
        bar_color='cerulean_blue_1'
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Remove Filter']
        
        verify_bar(step_no,bar_expected_number,xaxis_title, yaxis_title, x_label, y_label, bar_raiser_class,bar_expected_tooltip_list, bar_chart_title,filter_menu_in_chart,bar_color)
        
        step_no=4.2
        pie_expected_number=4
        pie_legend=['Line Total']
        pie_datalable=['45%', '16%', '21%', '17%']
        pie_chart_title='Line Total by Country'
        pie_raiser_class="riser!s0!g0!mwedge"
        pie_expected_tooltip_list=['Canada:181.7M (45.10%)']
        expected_legend_list=['Canada','France','Germany','Spain']
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Remove Filter']
        pie_color='cerulean_blue_1'
 
        verify_pie(step_no,1,pie_expected_number, pie_raiser_class, pie_expected_tooltip_list, pie_datalable,pie_chart_title, expected_legend_list, filter_menu_in_chart, pie_legend=pie_legend, pie_color=pie_color)
         
        step_no=4.3
        pie_expected_number=14
        pie_legend=['Line Total']
        pie_datalable=['3%', '10%', '4%', '31%', '15%', '1%', '2%', '4%', '4%', '1%', '3%', '7%', '14%', '2%']
        pie_chart_title='Line Total by Product Category'
        pie_raiser_class="riser!s0!g0!mwedge"
        pie_expected_tooltip_list=['Amplifiers/PreAmps/Tuners:42.4M (3.44%)']
        expected_legend_list=['Amplifiers/PreAmps/Tuners', 'Audio Systems', 'CD Players and Recorders', 'DVD Camcorders', 'Digital Cameras', 'Digital8 Camcorders', 'Handheld and PDA', 'MP3', 'MiniDV Camcorders', 'Organizers', 'Receivers', 'Speakers', 'TV', 'VCR']
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation','Remove Filter']
        pie_color='cerulean_blue_1'
 
        verify_pie(step_no,2,pie_expected_number, pie_raiser_class, pie_expected_tooltip_list, pie_datalable, pie_chart_title, expected_legend_list, filter_menu_in_chart, pie_legend=pie_legend,pie_color=pie_color)
        
        """
        Step05: Draw a box that touches all remaining Canada Bars, the menu should indicate 13 points(bars). 
        Select exclude from chart.
        """
        src_ele=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class^='riser!s0!g0!mbar!']")
        src=utillobj.get_object_screen_coordinate(src_ele, coordinate_type='bottom_left',x_offset=-5,y_offset=5)
        tgt_ele=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class^='riser!s0!g12!mbar!']")
        tgt=utillobj.get_object_screen_coordinate(tgt_ele, coordinate_type='top_right',y_offset=-5)
        utillobj.drag_drop_on_screen(sx_offset=src['x'],sy_offset=src['y'],tx_offset=tgt['x'],ty_offset=tgt['y'])
#         vis_resultobj.verify_default_tooltip_values('MAINTABLE_wbody0', bar_raiser_class, bar_expected_tooltip_list, "Step "+str(step_no)+".8: Verify bar tooltip.")
        expected_tooltip_list = ['13 points', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        vis_resultobj.verify_lasso_tooltip(expected_tooltip_list, 'Step 05.01')
#         utillobj.synchronize_with_number_of_element("div[id^='ibi'][class=tdgchart-tooltip] .tdgchart-tooltip-pad", 11, 45)
        vis_resultobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        
        """
        Expect to see the Document, with all Bars for Canada excluded.
        The Bar Chart should now begin with Bars for France.
        """
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0 [class*='xaxisOrdinal-labels!g']", 42, 25)
        
        step_no=5.1
        bar_expected_number=42
        xaxis_title='Country : Product Category'
        yaxis_title='Line Total'
        x_label=['France','France','France','France','France']
        y_label=['0','4M','8M','12M','16M','20M','24M']
        bar_chart_title='Line Total by Country, Product Category'
        bar_raiser_class="riser!s0!g1!mbar"
        bar_expected_tooltip_list=['Line Total, France/Audio Systems:5,909,051.00']
        bar_color='cerulean_blue_1'
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Remove Filter']
        
        verify_bar(step_no,bar_expected_number,xaxis_title, yaxis_title, x_label, y_label, bar_raiser_class,bar_expected_tooltip_list, bar_chart_title,filter_menu_in_chart,bar_color)
        
        """
        Step06: From the bottom left PIE chart, click the Filter icon to remove the Exclusion of the United States slice.
        Expect to see the Document with the slice for United States return, the legend now showing United States again and the Filter icon removed from the top of the chart.
        """
        active_chartobj.click_pivot_menu_bar_items('MAINTABLE_wmenu1', 8)
        
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0 [class*='xaxisOrdinal-labels!g']", 75, 25)
        
        step_no=6.1
        bar_expected_number=75
        xaxis_title='Country : Product Category'
        yaxis_title='Line Total'
        x_label=['Canada','Canada','Canada','Canada','Canada']
        y_label=['0','50M','100M','150M','200M','250M','300M']
        bar_chart_title='Line Total by Country, Product Category'
        bar_raiser_class="riser!s0!g1!mbar"
        bar_expected_tooltip_list=['Line Total, Canada/Audio Systems:15,132,844.00']
        bar_color='cerulean_blue_1'
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation']
         
        verify_bar(step_no,bar_expected_number,xaxis_title, yaxis_title, x_label, y_label, bar_raiser_class,bar_expected_tooltip_list, bar_chart_title,filter_menu_in_chart,bar_color)
        step_no=6.2
        pie_expected_number=5
        pie_legend=['Line Total']
        pie_datalable=['12%', '4%', '6%','4%','74%']
        pie_chart_title='Line Total by Country'
        pie_raiser_class="riser!s0!g0!mwedge"
        pie_expected_tooltip_list=['Canada:181.7M (11.63%)']
        expected_legend_list=['Canada','France','Germany','Spain','United States']
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation']
        pie_color='cerulean_blue_1'
 
        verify_pie(step_no,1,pie_expected_number, pie_raiser_class, pie_expected_tooltip_list, pie_datalable,pie_chart_title, expected_legend_list, filter_menu_in_chart, pie_legend=pie_legend, pie_color=pie_color)
         
        step_no=6.3
        pie_expected_number=15
        pie_legend=['Line Total']
        pie_datalable=['3%', '8%', '3%', '21%', '24%', '12%', '1%', '1%', '3%', '3%', '1%', '2%', '5%', '11%', '1%']
        pie_chart_title='Line Total by Product Category'
        pie_raiser_class="riser!s0!g0!mwedge"
        pie_expected_tooltip_list=['Amplifiers/PreAmps/Tuners:42.4M (2.71%)']
        expected_legend_list=['Amplifiers', 'Audio', 'CD Players', 'DVD', 'DVD']
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation']
        pie_color='cerulean_blue_1'
 
        verify_pie(step_no,2,pie_expected_number, pie_raiser_class,pie_expected_tooltip_list, pie_datalable,pie_chart_title, expected_legend_list, filter_menu_in_chart, pie_legend=pie_legend,pie_color=pie_color)
        
        
if __name__ == '__main__':
    unittest.main()