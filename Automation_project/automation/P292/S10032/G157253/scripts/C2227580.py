'''
Created on Dec 05, 2017

@author: PM14587
Testcase Name : Verify arranging output windows in Cascade, Tile Horizontally, Tile Vertically
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2227580
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_run,ia_resultarea
from common.lib import utillity

class C2227580_TestClass(BaseTestCase):

    def test_C2227580(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2227580'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        browser=utillobj.parseinitfile('browser')
        
        """
            Step 01 : Launch IA Report mode: http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        time.sleep(3)
        
        """
            Step 02 : Double click "COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST".
        """
        metaobj.datatree_field_click('COUNTRY',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,20,string_value='COUNTRY')
             
        metaobj.datatree_field_click('CAR',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 1,20,string_value='CAR')
             
        metaobj.datatree_field_click('DEALER_COST',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)", 1,20,string_value='DEALER_COST')
            
        metaobj.datatree_field_click('RETAIL_COST',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,20,string_value='RETAIL_COST')
        time.sleep(2)
          
        """
            Step 03 : Verify the following report is displayed.
        """
        iaresult.verify_row_total_report_titles_on_preview(4,4,'TableChart_1 ',['COUNTRY','CAR','DEALER_COST','RETAIL_COST'],'Step 03.1 : Verify the following report is displayed')
            
        """
            Step 04 : From the status bar, change "Single Tab" output to "New Tab" output.
        """
        ribbonobj.select_report_output_window('New Tab')
        time.sleep(2)
            
        """
            Step 05 : Click "Run" 4 times.
            Step 06 : Verify the output is displayed in four different tabs.
        """
        for i in range(1,5) :
            ribbonobj.select_top_toolbar_item('toolbar_run')
            title_css="#resultAreaWindowManager [id^='QbReportWindow']:nth-child("+str(i)+") div[class*='bi-window-caption']>div[id^='BiLabel']"
            utillobj.verify_element_text(title_css,"Report1["+str(i-1)+"]","Step 06."+str(i)+" : Verify Report title in Tab "+str(i))
            utillobj.switch_to_frame(3,frame_css="#resultAreaWindowManager [id^='QbReportWindow']:nth-child("+str(i)+") iframe[id^='ReportIframe']")
            iarun.verify_table_data_set("table[summary]",Test_Case_ID+'_DataSet_01.xlsx',"Step 06."+str(i)+" : Verify Report data in Tab "+str(i))
            utillobj.switch_to_default_content(2)
            
        """
            Step 07 : Select "View" > "Arrange (dropdown)" (Output Window Group) > "Cascade".
        """
        ribbonobj.select_ribbon_item('View','arrange',opt='Cascade',verify=True,expected_popup_list=['Cascade','Tile Horizontally','Tile Vertically'],msg='Step 07.1 : Verify View Arrange options')
        time.sleep(2)
          
        """
            Step 08 : Verify the following output
        """
        parent_tab=self.driver.find_element_by_css_selector("#resultAreaWindowManager")
        tab1=self.driver.find_element_by_css_selector("#resultAreaWindowManager [id^='QbReportWindow']:nth-child(1)")
        tab2=self.driver.find_element_by_css_selector("#resultAreaWindowManager [id^='QbReportWindow']:nth-child(2)")
        tab3=self.driver.find_element_by_css_selector("#resultAreaWindowManager [id^='QbReportWindow']:nth-child(3)")
        tab4=self.driver.find_element_by_css_selector("#resultAreaWindowManager [id^='QbReportWindow']:nth-child(4)")
        actual_x_gap=tab2.location['x']-tab1.location['x']
        actual_y_gap=tab2.location['y']-tab1.location['y']
           
        status0=True if (parent_tab.location['x']+1)==tab1.location['x'] and (parent_tab.location['y']+1)==tab1.location['y'] else False
        utillobj.asequal(status0,True,'Step 08.0 : Verify Report Tab 1 Arranged in Cascade view')
           
        status1=True if actual_x_gap>20 and actual_x_gap<30 and actual_x_gap==actual_y_gap else False
        utillobj.asequal(status1,True,'Step 08.1 : Verify Report Tab 2 Arranged in Cascade view')
           
        status2=True if (tab3.location['x']-tab2.location['x'])==(tab3.location['y']-tab2.location['y'])==actual_x_gap==actual_y_gap else False
        utillobj.asequal(status2,True,'Step 08.2 : Verify Report Tab 3 Arranged in Cascade view')
           
        status3=True if (tab4.location['x']-tab3.location['x'])==(tab4.location['y']-tab3.location['y'])==actual_x_gap==actual_y_gap else False
        utillobj.asequal(status3,True,'Step 08.3 : Verify Report Tab 4 Arranged in Cascade view')
           
        status4=True if tab1.size==tab2.size==tab3.size==tab1.size else False
        utillobj.asequal(status4,True,'Step 08.4 : Verify All Report Tab have same size')
           
        for i in range(1,5) :
            title_css="#resultAreaWindowManager [id^='QbReportWindow']:nth-child("+str(i)+") div[class*='bi-window-caption']>div[id^='BiLabel']"
            utillobj.verify_element_text(title_css,"Report1["+str(i-1)+"]","Step 08.5."+str(i)+" : Verify Report title in Tab "+str(i))
            utillobj.switch_to_frame(3,frame_css="#resultAreaWindowManager [id^='QbReportWindow']:nth-child("+str(i)+") iframe[id^='ReportIframe']")
            iarun.verify_table_data_set("table[summary]",Test_Case_ID+'_DataSet_01.xlsx',"Step 08.5."+str(i)+" : Verify Report data in Tab "+str(i))
            utillobj.switch_to_default_content(2)
           
        """
            Step 09 : Select "View" > "Arrange (dropdown)" (Output Window Group) > "Tile Horizontally".
        """
        ribbonobj.select_ribbon_item('View','arrange',opt='Tile Horizontally',verify=True,expected_popup_list=['Cascade','Tile Horizontally','Tile Vertically'],msg='Step 07.1 : Verify View Arrange options')
        time.sleep(2)
          
        """
            Step 10 : Verify the following output
        """
        parent_tab=self.driver.find_element_by_css_selector("#resultAreaWindowManager")
        tab1=self.driver.find_element_by_css_selector("#resultAreaWindowManager [id^='QbReportWindow']:nth-child(1)")
        tab2=self.driver.find_element_by_css_selector("#resultAreaWindowManager [id^='QbReportWindow']:nth-child(2)")
        tab3=self.driver.find_element_by_css_selector("#resultAreaWindowManager [id^='QbReportWindow']:nth-child(3)")
        tab4=self.driver.find_element_by_css_selector("#resultAreaWindowManager [id^='QbReportWindow']:nth-child(4)")
        actual_y_gap=tab1.location['y']-tab2.location['y']
        print('actual_y_gap:', actual_y_gap)
         
        status0=True if actual_y_gap in range(174,220) else False
        utillobj.asequal(status0,True,'Step 10.0 : Verify Report Tab 1 Arranged in Tile Horizontally view')
          
        status1=True if (tab2.location['y']-tab3.location['y']) in range((actual_y_gap-3),(actual_y_gap+3)) else False
        utillobj.asequal(status1,True,'Step 10.1 : Verify Report Tab 2 Arranged in Tile Horizontally view')
          
        status2=True if (tab3.location['y']-tab4.location['y']) in range((actual_y_gap-3),(actual_y_gap+3)) else False
        utillobj.asequal(status2,True,'Step 10.2 : Verify Report Tab 3 Arranged in Tile Horizontally view')
          
        status3=True if tab4.location['y'] in range((parent_tab.location['y']),(parent_tab.location['y']+2)) else False
        utillobj.asequal(status3,True,'Step 10.3 : Verify Report Tab 4 Arranged in Tile Horizontally view')
          
        status5=True if tab1.location['x']==tab2.location['x']==tab3.location['x']==tab1.location['x'] else False
        utillobj.asequal(status5,True,'Step 10.4 : Verify All Report Tab placed in same location')
          
        for i in range(1,5) :
            title_css="#resultAreaWindowManager [id^='QbReportWindow']:nth-child("+str(i)+") div[class*='bi-window-caption']>div[id^='BiLabel']"
            utillobj.verify_element_text(title_css,"Report1["+str(i-1)+"]","Step 10.5."+str(i)+" : Verify Report title in Tab "+str(i))
            utillobj.switch_to_frame(3,frame_css="#resultAreaWindowManager [id^='QbReportWindow']:nth-child("+str(i)+") iframe[id^='ReportIframe']")
            iarun.verify_table_data_set("table[summary]",Test_Case_ID+'_DataSet_01.xlsx',"Step 10.5."+str(i)+" : Verify Report data in Tab "+str(i))
            utillobj.switch_to_default_content(2)
 
        """
            Step 11 : Select "View" > "Arrange (dropdown)" (Output Window Group) > "Tile Vertically".
        """
        ribbonobj.select_ribbon_item('View','arrange',opt='Tile Vertically',verify=True,expected_popup_list=['Cascade','Tile Horizontally','Tile Vertically'],msg='Step 07.1 : Verify View Arrange options')
        time.sleep(2)
        
        """
            Step 12 : Verify the following output
        """
        parent_tab=self.driver.find_element_by_css_selector("#resultAreaWindowManager")
        tab1=self.driver.find_element_by_css_selector("#resultAreaWindowManager [id^='QbReportWindow']:nth-child(1)")
        tab2=self.driver.find_element_by_css_selector("#resultAreaWindowManager [id^='QbReportWindow']:nth-child(2)")
        tab3=self.driver.find_element_by_css_selector("#resultAreaWindowManager [id^='QbReportWindow']:nth-child(3)")
        tab4=self.driver.find_element_by_css_selector("#resultAreaWindowManager [id^='QbReportWindow']:nth-child(4)")
        actual_x_gap=tab3.location['x']-tab4.location['x']
        status0=True if int(actual_x_gap) in range(300,400) and tab4.location['x'] in range(parent_tab.location['x']-1,parent_tab.location['x']+4) else False
        utillobj.asequal(status0,True,'Step 12.0 : Verify Report Tab 4 Arranged in Tile Vertically view')
        
        status1=True if (tab2.location['x']-tab3.location['x']) in range((actual_x_gap-3),(actual_x_gap+3)) else False
        utillobj.asequal(status1,True,'Step 12.1 : Verify Report Tab 3 Arranged in Tile Horizontally view')
        
        status2=True if (tab1.location['x']-tab2.location['x']) in range((actual_x_gap-3),(actual_x_gap+3)) else False
        utillobj.asequal(status2,True,'Step 12.2 : Verify Report Tab 2 Arranged in Tile Horizontally view')
        
        status3=True if int(tab1.size['width']) in range((actual_x_gap-3),(actual_x_gap+3)) else False
        utillobj.asequal(status3,True,'Step 12.3 : Verify Report Tab 1 Arranged in Tile Horizontally view')
        
        status4=True if tab1.location['y']==tab2.location['y']==tab3.location['y']==tab4.location['y'] and tab1.size['height']==tab2.size['height']==tab3.size['height']==tab4.size['height'] else False
        utillobj.asequal(status4,True,'Step 12.4 :  Verify All Report Tab have same size')
        
        for i in range(1,5) :
            title_css="#resultAreaWindowManager [id^='QbReportWindow']:nth-child("+str(i)+") div[class*='bi-window-caption']>div[id^='BiLabel']"
            utillobj.verify_element_text(title_css,"Report1["+str(i-1)+"]","Step 12.4."+str(i)+" : Verify Report title in Tab "+str(i))
            utillobj.switch_to_frame(3,frame_css="#resultAreaWindowManager [id^='QbReportWindow']:nth-child("+str(i)+") iframe[id^='ReportIframe']")
            iarun.verify_table_data_set("table[summary]",Test_Case_ID+'_DataSet_01.xlsx',"Step 12.4."+str(i)+" : Verify Report data in Tab "+str(i))
            utillobj.switch_to_default_content(2)
            if browser=='IE' and i==2 :
                break
            
        """
            Step 13 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__=='__main__' :
    unittest.main()