'''
Created on Jan 29, 2018
TestSuite ID :http://172.19.2.180/testrail/index.php?/suites/view/10851&group_by=cases:section_id&group_order=asc&group_id=175061
TestCase Name : Navigating the Page Menu- Duplicate, Rename and Delete page options.
TestCase ID :http://172.19.2.180/testrail/index.php?/cases/view/2358900
@author: KS13172
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous,ia_run
from common.lib import utillity

class C2358900_TestClass(BaseTestCase):

    def test_C2358900(self):
        
        """ TESTCASE VARIABLES """
        Test_Case_ID = "C2358900"
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step01: Upload the attached Multi_Page.fex to IA Document and Edit using IA Tool.
        Expect to see the following IA preview panel.
        """
        utillobj.infoassist_api_edit('Multi_Page','document','S10851_2', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_number_of_element("[class*='riser!']",4,80)
        
        resultobj.verify_legends(['Unit Sales','Dollar Sales'], "#TableChart_1",msg="Step 01:01: Verify Y-axis Title")
        resultobj.verify_xaxis_title("TableChart_1", 'Category : Product', "Step 01:02: Verify X-axis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 4, 'Step 01:03: Verify the total number of risers displayed on live-preview Chart')
        expected_yval_list=['0','0.5M','1M','1.5M','2M','2.5M','3M','3.5M','4M']
        expected_xval_list=['Coffee : Capuccino']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 01:04: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 01:05: Verify first bar color")
          
        """
        Step02: Click the Page Options dialog box from the upper right corner, initially set at Page 1.
        Expect to see the following Page Option menu appear in the upper right of the canvas.
        """
        liu=['Page 1', 'Page 2', 'New Page', 'Page Options...']
        ia_resultobj.select_or_verify_document_page_menu('Page 1','Page 1',verify='true',expected_popup_list=liu,msg='Step02: Verify Page Option menu appear')

        """
        Step03: Click the Page Options at the bottom of the menu, directly below the New Page entry.
        Expect to see the listing of available pages: Page 1 & Page 2.
        """ 
        ia_resultobj.select_or_verify_document_page_menu('Page Options...')
        utillobj.synchronize_with_number_of_element("#pageOptionsDlg #iaPageList",1,15)
        ia_resultobj.verify_document_page_options(page_list=['Page 1','Page 2'],msg="Step03: Verify pages, Page 1 & Page 2")
        
        """
        Step04: Click Page 2, to see available options for that page.
        Expect to see the page icons appear at the top of the menu.
        """
        ia_resultobj.select_page_in_document_page_options('Page 2')
        ia_resultobj.verify_document_page_options(enable_button_list=['rename','duplicate','moveup'],msg="Step04: Verify available options for that page")
       
        """
        Step05 :Click on the second icon, which is the Duplicate Page option.
        Expect to see the following page menu, with the default duplicate page added.
        """ 
        ia_resultobj.select_actions_in_document_page_options('duplicate')
        utillobj.synchronize_with_number_of_element("#pageOptionsDlg #iaPageList",1,15)
        ia_resultobj.verify_document_page_options(page_list=['Page 1', 'Page 2', 'Page 2 ( Copy )'],msg="Step05: Verify pages, Page 2 (Copy)")
         
        """
        Step06: Right click on Page 2 (Copy).
        Expect to see the following menu appear.
        """
        #right click on Page 2 (Copy)
        ia_resultobj.select_page_in_document_page_options('Page 2 ( Copy )',click_type='right')
        time.sleep(3)
#         utillobj.synchronize_with_number_of_element("[id^='BiPopup']",3,15)
        li=['Duplicate','Rename','Move Up','Delete']
        utillobj.verify_bipopup_list_item(expected_popup_list=li, msg='Step06: Verify right click menu appears')
        
        """
        Step07: Click on the Rename option.
        Expect to see Page 2 (Copy) highlighted.
        """
        utillobj.select_bipopup_list_item('Rename')
        utillobj.synchronize_with_number_of_element("#iaPageList input",1,15)
        
        """
        Step08: Change the title from Page 2 (Copy) to Duplicate Page 2 and press enter.
        Expect to see the updated listing of pages below.
        """
        field_elem=self.driver.find_element_by_css_selector("#iaPageList input")
        utillobj.set_text_field_using_actionchains(field_elem, "Duplicate Page 2")
        """
        Step09: Click OK for the page rename, then click the Run button to verify the page names.
        Expect to see the following Dashboard, now with three pages and the last one is 'Duplicate Page 2'.
        """
        ia_resultobj.select_page_in_document_page_options('Page 1',close_dialog_btn_name='ok')
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']",1,15)
        utillobj.switch_to_frame(pause=1) 
        pages=['Layouts','Page 1','Page 2','Duplicate Page 2']
        ia_runobj.verify_active_document_page_layout_menu("table[id='iLayTB$']",pages, "Step09: Verify all 3 pages")
        
        """
        Step10: Click Page 2, then Duplicate Page 2.
        Expect to see the same content on both Page 2 and Duplicate Page 2.
        """
        ia_runobj.select_active_document_page_layout_menu('Page 2')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1",1,15) 
       
        """ Verify chart in Page1 """
        expected_yval_list=['0', '3M', '6M', '9M', '12M']
        expected_xval_list=['Coffee : Ca...', 'Coffee : Es...', 'Coffee : Latte', 'Food : Biscotti']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step10.1:03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 20, 'Step10:1.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "bar_blue", "Step10:1.04: Verify  bar color")
        miscelanousobj.verify_chart_title('MAINTABLE_wbody1_ft', 'Budget Units, Budget Dollars by Category, Product', 'Step10:1.05: Verify Chart Title')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['More Options','Advanced Chart','Original Chart'],"Step10:1.06: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Aggregation'],"Step10:1.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step10:1.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resultobj.verify_legends(['Budget Units', 'Budget Dollars'], "#MAINTABLE_wbody1_f",msg="Step10:1.01: Verify Y-axis Title")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", "Category : Product", "Step10:1.02: Verify -xAxis Title")
        
        ia_runobj.select_active_document_page_layout_menu('Duplicate Page 2')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody2",1,15)
        
        """ Verify chart in Page1 """
        resultobj.verify_xaxis_title("MAINTABLE_wbody2", "Category : Product", "Step10:2.02: Verify -xAxis Title")
        expected_yval_list=['0', '3M', '6M', '9M', '12M']
        expected_xval_list=['Coffee : Ca...', 'Coffee : Es...', 'Coffee : Latte', 'Food : Biscotti']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody2", expected_xval_list, expected_yval_list, "Step10:2.03: Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 20, 'Step10:2.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g2!mbar!", "bar_blue", "Step10:2.04: Verify  bar color")
        miscelanousobj.verify_chart_title('MAINTABLE_wbody2_ft', 'Budget Units, Budget Dollars by Category, Product', 'Step10:2.05: Verify Chart Title')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu2', ['More Options','Advanced Chart','Original Chart'],"Step10:2.06: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu2', ['Aggregation'],"Step10:2.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('MAINTABLE_wmenu2', ['Sum'],"Step10:2.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resultobj.verify_legends(['Budget Units', 'Budget Dollars'], "#MAINTABLE_wbody2_f",msg="Step10:2.01: Verify Y-axis Title")
        
        """
        Step11: Exit the Report, access the canvas again, then click the Page icon in the upper right.
        Expect to see preview canvas positioned at Page 1, with the Page option menu again displayed.
        """   
        utillobj.switch_to_default_content()     
        resultobj.select_panel_caption_btn(0, select_type='close',custom_css="[class*='window'][class*='active'] [class*='window-caption']")
        time.sleep(3)   
#         utillobj.synchronize_with_number_of_element("[id^='BiPopup']", 9, 15)
        ia_resultobj.verify_current_document_page_name('Page 1', 'Step11: Verify default page is Page 1')        
        utillobj.synchronize_with_number_of_element("#pageOptionsDlg", 1, 15)
        
        liu=['Page 1', 'Page 2', 'Duplicate Page 2', 'New Page', 'Page Options...']
        ia_resultobj.select_or_verify_document_page_menu('Page 1',verify='true',expected_popup_list=liu,msg='Step11: Verify Page Option menu appear')
        
        """
        Step12: Click Page Options, right-click Duplicate Page 2, then click Delete.
        Expect to see Duplicate Page 2 removed from the available list of pages.
        """
        ia_resultobj.select_or_verify_document_page_menu('Page Options...')
        ia_resultobj.select_page_in_document_page_options('Duplicate Page 2',click_type='right')
        time.sleep(3)
#         utillobj.synchronize_with_number_of_element("[id^='BiPopup']",7,15)
        utillobj.select_bipopup_list_item('Delete')
        
        #need to replace with page option list verification
        utillobj.synchronize_with_number_of_element("#pageOptionsDlg #iaPageList",1,15)
        ia_resultobj.verify_document_page_options(page_list=['Page 1','Page 2'],msg="Step12: Verify pages, Duplicate Page 2 removed")
       
         
        
if __name__ == "__main__":
    unittest.main()    
        