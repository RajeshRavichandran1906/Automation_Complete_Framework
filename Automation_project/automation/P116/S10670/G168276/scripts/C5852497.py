'''
Created on Dec 28,2018

@author:Vpriya

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10670&group_by=cases:section_id&group_id=168276&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5852497
TestCase Name = AHTML: Restore Vertical Dual-Axis Absolute Line Chart via API.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility
from common.wftools import active_chart

class C5852497_TestClass(BaseTestCase):

    def test_C5852497(self):
        
        """
        CLASS OBJECTS
        """
        active_chartobj = active_chart.Active_Chart(self.driver)
        
        """
            TESTCASE VARIABLES
        """     
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        project_id=core_utill_obj.parseinitfile('project_id')
        suite_id=core_utill_obj.parseinitfile('suite_id')
        group_id=core_utill_obj.parseinitfile('group_id')
        folder_path=project_id+'_'+suite_id+'/'+group_id
        fex_name='Vertical_Dual_Axis_Absolute_Line'
        expected_chart_title='DEALER_COST, LENGTH by CAR'
        expected_xlabel_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_ylabel_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        expected_legend_list=['DEALER_COST', 'LENGTH']
        expected_xtitle_list=['CAR']
        expected_ytitle_list=['DEALER_COST']
        MEDIUM_WAIT_TIME = 90
        
        """
        Step:1 Sign in to WebFOCUS
        http://machine:port/{alias}
        """
        """
        Step:2 Restore the saved Vertical Dual Axis Absolute Line.fex using below API
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=
        IBFS%253A%252FWFC%252FRepository%252FP116_S10670%252FG168276%252F&BIP_item=Vertical_Dual_Axis_Absolute_Line.fex
        """
        active_chartobj.run_fex_using_api_url(folder_path,fex_name,mrid='mrid',mrpass='mrpass',run_chart_css='#MAINTABLE_wbody0',wait_time=MEDIUM_WAIT_TIME)
    
        """
        Step:3 Verify the Vertical Dual Axis Absolute Line Chart is generated.
        """
        active_chartobj.verify_chart_title(expected_chart_title, msg='Step 3.0', parent_css='#MAINTABLE_wbody0')
        active_chartobj.verify_x_axis_label_in_run_window(expected_xlabel_list,msg="Step 3.1")
        active_chartobj.verify_y_axis_label_in_run_window(expected_ylabel_list,msg="Step 3.2")
        active_chartobj.verify_y_axis_label_in_run_window(['0', '300', '600', '900', '1,200'], xyz_axis_label_css="text[class*='y2axis-labels']",msg="Step 3.3")
        active_chartobj.verify_legends_in_run_window(expected_legend_list, legend_length=2, msg="Step 3.4")
        active_chartobj.verify_x_axis_title_in_run_window(expected_xtitle_list,msg="Step 3.5")
        active_chartobj.verify_y_axis_title_in_run_window(expected_ytitle_list,msg="Step 3.6")
        active_chartobj.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 03.7', parent_css='#MAINTABLE_wmenu0')
        active_chartobj.verify_number_of_risers_in_run_window('path',1,2,msg="Step 3.8: Verify Number of risers")
        active_chartobj.verify_chart_color_using_get_css_property_in_run_window("path[class='riser!s0!g0!mline!']", 'bar_blue',parent_css='#MAINTABLE_wbody0',attribute='stroke',msg="Step 03.09")
        active_chartobj.verify_chart_color_using_get_css_property_in_run_window("path[class='riser!s1!g0!mline!']", 'pale_green',parent_css='#MAINTABLE_wbody0',attribute='stroke',msg="Step 03.10")
        
        
        """
        Step 4:Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()