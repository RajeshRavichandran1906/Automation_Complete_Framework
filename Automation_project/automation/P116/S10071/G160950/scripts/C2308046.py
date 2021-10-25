'''
Created on Jan 17, 2018

@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2308046
TestCase Name = AHTML:Cache: Incorrect Pie Chart displayed in dashboard (ACT-405)
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous
from common.lib import utillity


class C2308046_TestClass(BaseTestCase):

    def test_C2308046(self):
        
        """
        Step 01: Execute the attached repro - BS_Dashboard_CacheON.fex
        """
        
        utillobj = utillity.UtillityMethods(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        active_misobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login('BS_Dashboard_CacheON.fex','S10071_1','mrid','mrpass')
        
        def verify_bar_chart(parent_id,xaxis_labels,yaxis_labels,title, step_num):
            visul_result.verify_xaxis_title(parent_id, 'Country : Product Type', 'Step ' + step_num + '.1 : Verify X-Axis title')
            visul_result.verify_yaxis_title(parent_id, 'Quantity', 'Step ' + step_num + '.2 : Verify Y-Axis title')
            visul_result.verify_riser_chart_XY_labels(parent_id, xaxis_labels, yaxis_labels, 'Step ' + step_num + '.3 :Verify XY labels')
            visul_result.verify_number_of_riser(parent_id, 1, 25, 'Step ' + step_num + '.4 : Verify number of bar chart risers')
            utillobj.verify_chart_color(parent_id, 'riser!s0!g0!mbar!', 'bar_blue', 'Step ' + step_num + '.5 : Verify bar chart riser color')
            active_misobj.verify_chart_title('MAINTABLE_wbody0_ft',title,'Step ' + step_num + '.6 :Verify title')
            
            
        def verify_pie_chart(parent_id,label,legend,title,step_num):
            
            utillobj.verify_chart_color(parent_id,"riser!s4!g0!mwedge!",'brick_red',"Step"  + step_num + ".1b:Verify Fill Color")
            #Pie Label
            visul_result.verify_riser_pie_labels_and_legends(parent_id, label,"Step"  + step_num + ".2: Verify Chart Pie Label & Legend")
            #Pie Legend
            visul_result.verify_riser_legends(parent_id, legend, "Step"  + step_num + ".3: Verify Chart Pie Legends")
            #Title
            active_misobj.verify_chart_title(parent_id+'_ft',title,'Step ' + step_num + '.4 :Verify title')
            
        """
        Step02: Verify the pie chart displayed correctly.
        """        
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0", 1, 3)
        xaxis=['Canada : Au', 'Cananda : Ca', 'Cananda : Ca', 'Cananda : Of']
        yaxis=['0', '100K', '200K', '300K', '400K','500K','600K','700K']
        title='Quantity by Country, Product Type' 
        
        verify_bar_chart('MAINTABLE_wbody0',xaxis,yaxis ,title,'02.1')
        
        label=['Quantity']
        legend=['Country', 'Canada', 'France', 'Germany', 'Spain', 'United States']
        title='Quantity by Country'        
        verify_pie_chart('MAINTABLE_wbody1',label,legend,title,'02.2')
        visul_result.verify_number_of_pie_segment('#MAINTABLE_wbody1', 5, 1, "Step02.2.5: Verify the number of pie segments")
            
        label=['Quantity']
        legend=['Product Type','Audio','Camcorders','Cameras','Office','Video']
        title='Quantity by Product Type'         
        verify_pie_chart('MAINTABLE_wbody2',label,legend,title,'02.3')
        visul_result.verify_number_of_pie_segment('#MAINTABLE_wbody2', 5, 1, "Step02.3.5: Verify the number of pie segments")
         

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
