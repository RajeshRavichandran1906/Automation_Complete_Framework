'''
Created on jan 2, 2019

@author: Vpriya

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10670&group_by=cases:section_id&group_order=asc&group_id=168212
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313416
TestCase Name = AHTML: Mekko Chart Basic chart using additional Buckets.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart
from common.wftools import chart
from common.lib import utillity,core_utility

class C2313416_TestClass(BaseTestCase):

    def test_C2313416(self):
        
        """
            TESTCASE VARIABLES
        """ 
        active_chart_obj=active_chart.Active_Chart(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        chart_obj=chart.Chart(self.driver)
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        project_id=core_utill_obj.parseinitfile('project_id')
        suite_id=core_utill_obj.parseinitfile('suite_id')
        group_id=core_utill_obj.parseinitfile('group_id')
        folder_path=project_id+'_'+suite_id+'/'+group_id
        fex_name="MekkoBasic"
        legend_css="text[class='legend-labels!s1!']"
        MEDIUM_WAIT_TIME = 90
        expected_xlabel_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PE...', 'TR...', 'T', 'D']
        expected_ylabel_list=['0%', '20%', '40%', '60%', '80%', '100%']
        expected_chart_title="DEALER_COST, RETAIL_COST by CAR"
        expected_xtitle_list=['CAR']
        expected_legend_list=['DEALER_COST', 'RETAIL_COST']
        expected_default_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235  (45.35%)', 'Filter Chart', 'Exclude from Chart']
        expected_sales_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235  (45.35%)', 'SALES:30200', 'Filter Chart', 'Exclude from Chart']
        expected_lseats_tooltip_list=['SEATS:2', 'CAR:ALFA ROMEO', 'DEALER_COST:16,235  (45.35%)', 'Filter Chart', 'Exclude from Chart']
        expected_hseats_tooltip_list=['SEATS:5', 'CAR:PEUGEOT', 'DEALER_COST:4,631  (45.22%)', 'Filter Chart', 'Exclude from Chart']
        run_label=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEUGEOT', 'TRIUMPH', 'TOYOTA', 'DATSUN']
        xyz_axis_label_css="svg > g text[class^='xaxis'][class*='labels']"
        
        """
        Step 01:Open FEX:
        http://machine:port/ibiapps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FMekkoBucketizedCharts%2FMekkoBasic.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_path,fex_name=fex_name, mrid='mrid',mrpass='mrpass')
        utill_obj.synchronize_with_visble_text(legend_css,'RETAIL_COST',MEDIUM_WAIT_TIME)
 
        """
        Step 02:
        Click the Run button.
        Hover over the lower(blue) area for Alfa Romeo.
        """
        chart_obj.run_chart_from_toptoolbar()
        utill_obj.switch_to_frame(pause=2)
        
        """
        Expect to see the following Active Mekko, with the default Tooltip information.
        """
        active_chart_obj.verify_x_axis_label_in_run_window(expected_xlabel_list,msg="Step 02.01")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_ylabel_list,msg="Step 02.02")
        active_chart_obj.verify_chart_title(expected_chart_title,parent_css="#MAINTABLE_wbody0",msg="Step 02.03")
        active_chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#MAINTABLE_wbody0",legend_length=2, msg="Step 02.04")
        active_chart_obj.verify_x_axis_title_in_run_window(expected_xtitle_list, parent_css="#MAINTABLE_wbody0",msg="Step 02.05")
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 02.06', parent_css='#MAINTABLE_wmenu0')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s0!g2!mbar!']",'bar_blue',parent_css='#MAINTABLE_wbody0',msg="Step 02.07")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s1!g2!mbar!']",'pale_green',parent_css='#MAINTABLE_wbody0',msg="Step 02.08")
        chart_obj.verify_tooltip_in_run_window("riser!s0!g0!mbar!", expected_default_tooltip_list, msg="Step 02.09", parent_css='#MAINTABLE_wbody0')
        
        """
        Step:03
        Drag the field SALES to the Tooltip area.
        """
        utill_obj.switch_to_default_content()
        active_chart_obj.drag_field_from_data_tree_to_query_pane('SALES',1,'Tooltip',1)
        
        """
        Expect to see the SALES field under the Tooltip area in the Query panel.
        """
        active_chart_obj.verify_field_listed_under_querytree('Tooltip', 'SALES', 1, msg="Step 03.01")
        
        
        """
        Step:04
        Click the Run button.
        Hover over lower area(blue) for Alfa Romeo.
        """
        chart_obj.run_chart_from_toptoolbar()
        utill_obj.switch_to_frame(pause=2)
        
        """
        Expect to see the SALES field added to the Tooltip information.
        """
        chart_obj.verify_tooltip_in_run_window("riser!s0!g0!mbar!", expected_sales_tooltip_list, msg="Step 04.01", parent_css='#MAINTABLE_wbody0')
    
        """
        Step:05 Now remove SALES from Tooltip area.
        """
        utill_obj.switch_to_default_content()
        chart_obj.right_click_on_field_under_query_tree('SALES', 1,'Delete')
        
        """
        Step:06
        Drag the field SEATS to the Multigraph area.
        """
        active_chart_obj.drag_field_from_data_tree_to_query_pane('SEATS',1,'Multi-graph',1)
        
        """
        Expect to see the SEATS field under the Multigraph area in the Query panel.
        """
        active_chart_obj.verify_field_listed_under_querytree('Multi-graph', 'SEATS', 1, msg="Step 06.01")
        
        """
        Step:07 Click the Run button.
        """
        chart_obj.run_chart_from_toptoolbar()
        utill_obj.switch_to_frame(pause=2)
        
        """
        Expect to see the data reordered, with Alfa Romeo first and Peugeot last.
        """
        active_chart_obj.verify_x_axis_label_in_run_window(run_label,msg="Step 07.01")
        x_label_elem=utill_obj.validate_and_get_webdriver_objects(xyz_axis_label_css,"XY_label_css")
        expected_list=['ALFA ROMEO','PEUGEOT']
        actual_label_list=[i.text for i in x_label_elem]
        for option in expected_list:
            if option in actual_label_list:
                act_status, exp_status=True, True
            else:
                act_status=actual_label_list
                exp_status=option
        utill_obj.asequal(exp_status,act_status,"Step:07.02")
        
        """
        Step:08
        Hover over the lower area(blue) for Alfa Romeo.
        """
        """
        Expect to see 2 Seats for Alfa Romeo.
        This is the lowest value of SEATS.
        """
        chart_obj.verify_tooltip_in_run_window("riser!s0!g0!mbar!", expected_lseats_tooltip_list, msg="Step 08.01", parent_css='#MAINTABLE_wbody0')
        
        """
        Step:09
        Hover over the lower area(blue) for Peugeot.
        """
        """
        Expect to see 5 Seats for Peugeot.
        This is the highest value of SEATS.
        """
        chart_obj.verify_tooltip_in_run_window("riser!s0!g9!mbar!", expected_hseats_tooltip_list, msg="Step 09.01", parent_css='#MAINTABLE_wbody0')
        
        """
        Step:10
        Move the SEATS field from the Multigraph area to the Animate area.
        """
        utill_obj.switch_to_default_content()
        active_chart_obj.drag_field_within_query_pane('SEATS','Animate')
        
        """
        Expect to see the SEATS field under the Animate area in the Query panel.
        """
        active_chart_obj.verify_field_listed_under_querytree('Animate', 'SEATS', 1, msg="Step 10.01")
        
        """
        Step:11
        Click the Run button.
        Hover over the lower area(blue) for Jaguar.
        """
        chart_obj.run_chart_from_toptoolbar()
        utill_obj.switch_to_frame(pause=2)
        
        """
        Expect to see the following Mekko Chart, showing only CARs with 2 SEATS.
        """
        expected_tooltip1=['SEATS:2', 'CAR:ALFA ROMEO', 'DEALER_COST:11,320  (45.35%)', 'Filter Chart', 'Exclude from Chart']
        chart_obj.verify_tooltip_in_run_window("riser!s0!g0!mbar!", expected_tooltip1, msg="Step 11.01", parent_css='#MAINTABLE_wbody0')
        
        """
        Step:12
        Move the slider control at the top to position 4.
        Hover over the lower area(blue) for Jensen.
        """
        chart_obj.move_chart_slider_in_run_window('4', parent_css='#MAINTABLE_wbody0')
        
        """
        Expect to see the following Mekko Chart, showing only CARs with 4 SEATS.
        """
        expected_tooltip_list2=['SEATS:4', 'CAR:ALFA ROMEO', 'DEALER_COST:4,915  (45.34%)', 'Filter Chart', 'Exclude from Chart']
        chart_obj.verify_tooltip_values('MAINTABLE_wbody0', "riser!s0!g0!mbar!", expected_tooltip_list2, msg="Step 12.01")
        
        
        """
        Step:13
        Move the slider control at the top to position 5.
        Hover over the lower area(blue) for Audi.
        """
        chart_obj.move_chart_slider_in_run_window('5', parent_css='#MAINTABLE_wbody0')
        
        """
        Expect to see the following Mekko Chart, showing only CARs with 5 SEATS.
        """
        
        expected_tooltip3=['SEATS:5', 'CAR:AUDI', 'DEALER_COST:5,063  (45.89%)', 'Filter Chart', 'Exclude from Chart']
        chart_obj.verify_tooltip_values('MAINTABLE_wbody0', "riser!s0!g8!mbar!", expected_tooltip3, msg="Step 13.01")
        
        
        """
            Step 14: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__=='__main__' :
    unittest.main()