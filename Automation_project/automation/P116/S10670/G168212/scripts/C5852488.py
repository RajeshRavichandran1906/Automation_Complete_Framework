'''
Created on Dec 31, 2018

@author: Vpriya

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10670&group_by=cases:section_id&group_id=168212&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5852488
TestCase Name =AHTML: Restore MekkoBasic Chart via API.
.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility
from common.wftools import active_chart

class C5852488_TestClass(BaseTestCase):

    def test_C5852488(self):
        
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
        fex_name='MekkoBasic'
        expected_chart_title='DEALER_COST, RETAIL_COST by CAR'
        expected_xlabel_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEU...', 'TRI...', 'T...', 'D...']
        expected_ylabel_list=['0%', '20%', '40%', '60%', '80%', '100%']
        expected_legend_list=['DEALER_COST', 'RETAIL_COST']
        expected_xtitle_list=['CAR']
        MEDIUM_WAIT_TIME = 90
        
        """
        Step:1 Sign in to WebFOCUS
        http://machine:port/{alias}
        """
        """
        Step:2 Restore the saved Vertical Dual Axis Absolute Line.fex using below API
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=
        IBFS%253A%252FWFC%252FRepository%252FP116_S10670%252FG168276%252F&BIP_item=MekkoBasic.fex
        """
        active_chartobj.run_fex_using_api_url(folder_path,fex_name,mrid='mrid',mrpass='mrpass',run_chart_css='#MAINTABLE_wbody0',wait_time=MEDIUM_WAIT_TIME)
    
        """
        Step:3 Verify the MekkoBasic Chart is generated.
        """
        active_chartobj.verify_chart_title(expected_chart_title, msg='Step:3', parent_css='#MAINTABLE_wbody0')
        active_chartobj.verify_x_axis_label_and_length_in_run_window(expected_xlabel_list,msg="Step 3.1")
        
#         active_chartobj.verify_x_axis_label_in_run_window(expected_xlabel_list,msg="Step 3.1")
        active_chartobj.verify_y_axis_label_in_run_window(expected_ylabel_list,msg="Step 3.2")
        active_chartobj.verify_x_axis_label_and_length_in_run_window(['108K', '56,500', '40,990', '35,800', '32,790', '11,033', '10,241', '9,392', '6,...', '5,...'], xyz_axis_label_css="text[class*='stackTotalLabel']",msg="Step 3.3")
        active_chartobj.verify_legends_in_run_window(expected_legend_list, legend_length=2, msg="Step:3.4")
        active_chartobj.verify_x_axis_title_in_run_window(expected_xtitle_list,msg="Step:3.5")
        active_chartobj.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 03.6', parent_css='#MAINTABLE_wmenu0')
        active_chartobj.verify_number_of_risers_in_run_window('rect',1,20,msg="Step:03.7 Verify Number of risers")
        active_chartobj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s0!g0!mbar!']",'bar_blue',parent_css='#MAINTABLE_wbody0',msg="Step 03.8")
        active_chartobj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s1!g2!mbar!']", 'pale_green',parent_css='#MAINTABLE_wbody0',msg="Step 03.9")
        
        """
        Step 4:Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
        

if __name__ == '__main__':
    unittest.main()