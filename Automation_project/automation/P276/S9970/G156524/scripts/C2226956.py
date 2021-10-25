'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226956
TestCase Name = Test drilling all the way down and up a long hierarchy path - HTML
'''
import unittest, time
from common.lib import utillity  
from common.wftools.report import Report
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon, ia_run

class C2226956_TestClass(BaseTestCase):
    
    def test_C2226956(self):
        
        """
        TESTCASE OBJECTS
        """
        report_ = Report(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        TESTCASE VARIABLES
        """ 
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2226956"
        Test_Case_ID = Test_ID+"_"+browser_type
        
        """    
            Step 01 : Open IA_Shell for edit using the API
            http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    
        """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn", 'Revenue', expire_time=40)
        time.sleep(8)
        
        """    
            Step 02 Click Format tab > Autodrill button  
        """
#         ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        report_.select_ia_ribbon_item("Format", "auto_drill")
        utillobj.synchronize_with_number_of_element("[id='FormatAutoDrill'][class*='checked']", 1, expire_time=5)
        
        """    
            Step 03 : Click RUN     
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(1)>td:nth-child(1)", 'Sale,Year', expire_time=20)
        
        """    
            Step 04 : Drill down - Click on North America under Store_Business,Region column and select "Drill down to Store Business Sub Region"    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",12,1,'Drill down to Store Business Sub Region')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(1)>td a", 'Home', expire_time=25)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 04.01 : Verify Drill down to Store Business Sub Region data set", desired_no_of_rows=15)
        
        """    
            Step 05 : Click on East and select "Drill down to Store Country"    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",13,1,'Drill down to Store Country')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(1)>td span:nth-child(5)", 'East', expire_time=25)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 05.01 : Verify Drill down to Store Country data set")
        
        """    
            Step 06 : Click on United States and select "Drill down to Store State Province"    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",5,1,'Drill down to Store State Province')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(1)>td span:nth-child(7)", 'UnitedStates', expire_time=25)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", "Step 06.01 : Verify Drill down to Store State Province data set", desired_no_of_rows=15)
        
        """    
            Step 07 : Click on New York and select "Drill down to Store City"    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",13,1,'Drill down to Store City')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(1)>td span:nth-child(9)", 'NewYork', expire_time=25)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds04.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds04.xlsx", "Step 07.01 : Verify Drill down to Store City data set")
        
        """    
            Step 08 : Click on New York and select "Drilldown to Store Postal Code "    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",5,1,'Drill down to Store Postal Code')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(1)>td span:nth-child(11)", 'NewYork', expire_time=25)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds05.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds05.xlsx", "Step 08.01 : Verify Drill down to Store Postal Code data set")
        
        """    
            Step 09 : Click on 10007 and select "Drilldown to Store Name"    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",5,1,'Drill down to Store Name')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(1)>td span:nth-child(13)", '10007', expire_time=25)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds06.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds06.xlsx", "Step 09.1 : Verify Drill down to Store Name data set")
        
        """    
            Step 10 : Now Click on New York and select "Drillup to Store Postal Code"    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",5,1,'Go up to Store Postal Code')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(5)>td:nth-child(1)", '10007', expire_time=25)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds05.xlsx", "Step 10.01 : Verify Drill up to Store Postal Code data set")
        
        """    
            Step 11 : Click on 10007 and select "Drillup to Store City"  
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",5,1,'Go up to Store City')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(5)>td:nth-child(1)", 'NewYork', expire_time=25)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds04.xlsx", "Step 11.01 : Verify Drill up to Store City data set")
        
        """    
            Step 12 : Click on New York and select "Drillup to Store State Province"    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",5,1,'Go up to Store State Province')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(5)>td:nth-child(1)", 'Massachusetts', expire_time=25)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", "Step 12.1 : Verify Drill up to Store State Province data set", desired_no_of_rows=15)
        
        """    
            Step 13 : Click on New York and select "Drillup to Store Country  
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",13,1,'Go up to Store Country')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(5)>td:nth-child(1)", 'UnitedStates', expire_time=25)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 13.01 : Verify Drill up to Store Country data set")
        
        """    
            Step 14 : Click on United States and select "Drillup to Store Business Sub Region"    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",5,1,'Go up to Store Business Sub Region')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(5)>td:nth-child(1)", 'Canada', expire_time=25)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 14.01 : Verify Drill up to Store Business Sub Region data set", desired_no_of_rows=15)
       
        """    
            Step 15 : Click on East and select "Drill up to Store Business Region"   
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",5,1,'Go up to Store Business Region')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(3)>td:nth-child(1)", 'EMEA', expire_time=25)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds00.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds00.xlsx", "Step 15.01 : Verify Drill up to Store Business Region data set", desired_no_of_rows=15)
        
        """    
            16 : Click IA > Save As> Type C2226956 > click Save    
        """
        utillobj.switch_to_default_content(4)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """    
            Step 17 : Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226956.fex&tool=report    
        """
        utillobj.infoassist_api_logout()
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn", 'Revenue', expire_time=40)
        
        """    
            Step 18 :  Click format tab and see Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_visble_text('#FormatTab', 'Features', ribbonobj.report_short_timesleep)
        report_.verify_ribbon_item_is_enabled('format_auto_drill', '18.01')
        
        """    
            Step 19. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        
if __name__ == '__main__':
    unittest.main()