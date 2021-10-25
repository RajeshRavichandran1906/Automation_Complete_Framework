'''
Created on 09-May-2018

@author: AAkhan(AA14564)

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5824566
TestCase Name = Verify Upload data functionality
'''
import unittest, time, os, re
from common.lib import utillity, javascript, core_utility
from common.pages import wf_legacymainpage, vfour_portal_canvas, visualization_metadata, ia_resultarea, visualization_resultarea, visualization_ribbon, ia_run, vfour_miscelaneous, metadata
from common.lib.basetestcase import BaseTestCase
from selenium.common.exceptions import NoSuchElementException,\
    StaleElementReferenceException

class C5824566_TestClass(BaseTestCase):

    def test_C5824566(self):
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        jscript_obj=javascript.JavaScript(self.driver)
        meta_obj=metadata.MetaData(self.driver)
        wf_mainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        portal_canvas=vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        portal_misobj=vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        vis_result_obj=visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_reb_obj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_result_obj = ia_resultarea.IA_Resultarea(self.driver)
        ia_run_obj = ia_run.IA_Run(self.driver)
        welcome_page_parent_css = "#PortalResourcevBOX table tr td"
        projid=utillobj.parseinitfile('project_id')
        upload_folder_name='Upload'
        upload_dialog_css="#upldbartop"
        select_button_css=upload_dialog_css+" input[type='button'][value*='Select']"
        business_panel_css="[frame_id='MFRFrame'][class*='wc-multiframes-content-view']"
        business_panel_table_css=business_panel_css+" table.bi-tree-view-table tr table tr"
        load_and_next_css=".wc-ribbon-button-item.wc-ribbon-button-selected"
        target_load_dialog_css="[id^='BiDialog'] .active"
        file_picker_button=target_load_dialog_css+" [id^='BCFilePicker'] [id*='BiComponent'] i"
        target_load_dialog_label_css=target_load_dialog_css+" .window-content-pane [class='bi-label']"
        select_app_dialog_css="[id^='BiDialog'][id$='fpdialog'] .active"
        select_app_dialog_tree_view_css=select_app_dialog_css+" #filetree"
        select_app_dialog_tree_view_row_css=select_app_dialog_tree_view_css+" table tr td span:not([class])"
        select_app_dialog_input_text_css=select_app_dialog_css+" input[type='text']"
        select_app_dialog_ok_button_css=select_app_dialog_css+" .bi-button-label.wc-button:nth-child(1)"
        target_load_dialog_proceed_button_css=target_load_dialog_css+" .bi-button-label.wc-button:nth-child(1)"
        finished_window_css="table tr"
        finished_window_gobackhome_css="span[onclick*='GoBackHome']"
        metadata_css="#iaMetaDataBrowser div[id^='QbMetaDataTree-'] tr td"
        test_case_id='C5824566'
        
        def synchronize_with_visble_text(element_css, visble_element_text, expire_time, pause_time=1):
            timeout=0
            run_ = True
            while run_:
                timeout+=1
                if timeout == int(expire_time)+1:
                    print(str(element_css) + " Parent Css not having " + str(visble_element_text) + " visible text.")
                    run_=False
                    break
                try:
                    temp_str_value=self.driver.find_element_by_css_selector(element_css).get_attribute('value').strip().replace('\n','')
                except NoSuchElementException:
                    time.sleep(pause_time)
                    continue
                except StaleElementReferenceException:
                    time.sleep(pause_time)
                    continue
                str_value = re.sub(' ','',temp_str_value)
                if str_value == str(visble_element_text.replace(' ','')):
                    run_=False
                    break
            time.sleep(pause_time)
        
        def expand_tree(folder_path, tree_css=None, scroll_elem=None):
            """
            :Param : folder_path = 'S7068->AR-RP-193'
            :Usage expand_tree('S7068->AR-RP-193')
            @author: AAkhan
            """
            if scroll_elem!=None:
                scroll_obj=scroll_elem
            else:
                scroll_obj=self.driver.find_element_by_css_selector("#treeContainer")
            utillobj.click_on_screen(scroll_obj, 'middle')
            time.sleep(2)
            utillobj.click_on_screen(scroll_obj, 'middle', y_offset=-9)
            if tree_css != None:
                tree_rows=tree_css
            else:
                tree_rows="#bipTreePanel #treeView table>tbody>tr"
            folder_list=folder_path.split('->')
            for item in folder_list:
                repository_items = self.driver.find_elements_by_css_selector(tree_rows)
                resource_tree_list = javascript.JavaScript.get_elements_text(self, repository_items)
                status=False
                for text in resource_tree_list:
                    if item in text:
                        status=True
                        break
                if status!=True:
                    raise LookupError(item+ " Not Exist in setup "+ self.driver.current_url)
                try:
                    for i in range(len(repository_items)):
                        if item in repository_items[i].text.strip():
                            try:
                                portal_misobj.scroll_within_resource_tree(scroll_obj, repository_items[i])
                                print('click')
                                utillobj.click_on_screen(repository_items[i], 'middle', click_type=0)
                                time.sleep(3)
                                if item == folder_list[-1]:
                                    return (i)
                            except:
                                if item == folder_list[-1]:
                                    return (i)
                            break
                except NoSuchElementException as e:
                    print(e,item + " not found in Repository Tree view. It might be a Bug also.")
    
        """ Step 1: Launch WebFOCUS > Login as "administrator"
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, 'Domains', 50)
        
        """ Step 2: Right click on "P292_S10117_G432777" domain > Select New > Folder
        """
        """ Step 3: Enter Title as "Upload" > Click OK
        """
        wf_mainpageobj.create_folder(projid, upload_folder_name)
          
        """ Step 4: Right click on "Upload" folder > Select Upload > Data
        """
        wf_mainpageobj.select_menu(projid+'->'+upload_folder_name, upload_folder_name+'->Data')
        time.sleep(1)
        utillobj.switch_to_window(1)
        utillobj.synchronize_with_number_of_element(select_button_css, 1, 190)
          
        """ Step 5: Verify the Web Console Upload Dialog is displayed.
        """
        status=False
        try:
            status = self.driver.find_element_by_css_selector(upload_dialog_css).is_displayed()
        except NoSuchElementException:
            raise AssertionError("The Web Console Upload Dialog is not displayed.")
        utillobj.asequal(status, True, "Step 5: Verify the Web Console Upload Dialog is displayed.")
          
        """ Step 6: Click Select File button > Choose the attached "Target Accounts - US.xlsx" file
        """
        path=os.getcwd()+"\\data\\"
        wf_mainpageobj.upload_file(['Target_Account-US.xlsx'], file_path_location=path, parent_css=select_button_css)
          
        """ Step 7: Verify the following window is displayed
        """
        target_account_tab_css="[id^='item']"
        utillobj.synchronize_with_visble_text(target_account_tab_css, 'ibi_mfdtarget_accounts', 290)
        tar_acc_text = self.driver.find_element_by_css_selector(target_account_tab_css).text.strip()
        utillobj.asequal('ibi_mfdtarget_accounts', tar_acc_text, "Step 7: Verify the target_accounts tab is displayed.")
        status=False
        try:
            status=self.driver.find_element_by_css_selector(business_panel_css).is_displayed()
        except NoSuchElementException:
            raise AssertionError("The Web Console after Upload window is not displayed.")
        utillobj.asequal(status, True, "Step 7.1: Verify the 'Business View' panel is displayed.")
        tar_acc_text = self.driver.find_element_by_css_selector(business_panel_table_css).text.strip()
        utillobj.asin('target_accounts', tar_acc_text, "Step 7.2: Verify the 'Business View' panel table data is displayed.")
          
        """ Step 8: Close the Web Console browser.
        """
        self.driver.close()
        utillobj.switch_to_window(0, pause=0)
        time.sleep(1)
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, 'Domains', 50)
          
        """ Step 9: Now again Right click on "Upload" folder > Select Upload > Data
        """
        wf_mainpageobj.select_menu(projid+'->'+upload_folder_name, upload_folder_name+'->Data')
        time.sleep(1)
        utillobj.switch_to_window(1)
        utillobj.synchronize_with_number_of_element(select_button_css, 1, 190)
          
        """ Step 10: Click Select File button > Choose the attached "retail_data_extract. xlsx" file
                     Verify successful upload
        """
        path=os.getcwd()+"\\data\\"
        wf_mainpageobj.upload_file(['retail_data_extract.xlsx'], file_path_location=path, parent_css=select_button_css)
        target_account_tab_css="[id^='item']:nth-child(1)"
        utillobj.synchronize_with_visble_text(target_account_tab_css, 'ibi_mfdretail_sales', 290)
        tar_acc_text = self.driver.find_element_by_css_selector(target_account_tab_css).text.strip()
        utillobj.asequal('ibi_mfdretail_sales', tar_acc_text, "Step 10: Verify the retail_sales tab is displayed.")
        status=False
        try:
            status=self.driver.find_element_by_css_selector(business_panel_css).is_displayed()
        except NoSuchElementException:
            raise AssertionError("The Web Console after Upload window is not displayed.")
        utillobj.asequal(status, True, "Step 10.1: Verify the 'Business View' panel is displayed.")
        tar_acc_text = self.driver.find_element_by_css_selector(business_panel_table_css).text.strip()
        utillobj.asequal('removefoccache/upload/retail_data_extract_xlsx/retail_sales', tar_acc_text, "Step 10.2: Verify the 'Business View' panel table data is displayed.")
          
        """ Step 11: Click "Load and Next" button on the Ribbon
                     Verify Target Load Options is displayed
                     Note: Adapter connection will vary based on environment
        """
        load_and_next_elem=self.driver.find_element_by_css_selector(load_and_next_css)
        utillobj.default_click(load_and_next_elem)
        utillobj.synchronize_with_number_of_element(file_picker_button, 1, 190)
        status=False
        try:
            status = self.driver.find_element_by_css_selector(file_picker_button).is_displayed()
        except NoSuchElementException:
            raise AssertionError("Target Load Options is not displayed.")
        utillobj.asequal(status, True, "Step 11: Verify Target Load Options is displayed.")
          
        """ Step 12: Click "Show File Picker(...)" under Synonym application > Choose ibisamp location >Click OK
        """
        file_picker_button_elem=self.driver.find_element_by_css_selector(file_picker_button)
        utillobj.default_click(file_picker_button_elem)
        utillobj.synchronize_with_number_of_element(select_app_dialog_tree_view_css, 1, 190)
        scroll_obj=self.driver.find_element_by_css_selector(select_app_dialog_tree_view_css)
        expand_tree('ibisamp', tree_css=select_app_dialog_tree_view_row_css, scroll_elem=scroll_obj)
        scroll_obj=self.driver.find_element_by_css_selector(select_app_dialog_tree_view_css)
        expand_tree('ibisamp', tree_css=select_app_dialog_tree_view_row_css, scroll_elem=scroll_obj)
        synchronize_with_visble_text(select_app_dialog_input_text_css, 'ibisamp', 290)
        ok_button_elem = self.driver.find_element_by_css_selector(select_app_dialog_ok_button_css)
        utillobj.default_click(ok_button_elem)
        portal_misobj.synchronize_until_element_disappear(select_app_dialog_ok_button_css, 0, 190)
          
        """ Step 13: Uncheck "Bulk Load" checkbox (If this option is not available please ignore)
        """
        target_load_dialog_label_elems=self.driver.find_elements_by_css_selector(target_load_dialog_label_css)
        target_load_dialog_label_elems_list = jscript_obj.get_elements_text(target_load_dialog_label_elems)
        try:
            bulk_load_index=target_load_dialog_label_elems_list.index('Bulk Load')
            input_option=target_load_dialog_label_elems[bulk_load_index+1].find_element_by_css_selector("input[type='checkbox']")
            status=input_option.is_selected()
            print('status',status)
            if status==True:
                utillobj.default_click(input_option)
        except:
            '''
            bulk option not exist (If this option is not available please ignore)
            '''
          
        """ Step 14: Click "Proceed to Load"
        """
        target_load_dialog_proceed_button_elem=self.driver.find_element_by_css_selector(target_load_dialog_proceed_button_css)
        utillobj.default_click(target_load_dialog_proceed_button_elem)
        portal_misobj.synchronize_until_element_disappear(target_load_dialog_proceed_button_css, 0, 190)
          
        """ Step 15: Verify the following window is displayed
        """
        utillobj.synchronize_with_visble_text(finished_window_gobackhome_css, 'Go back Home', 190)
        expected_list=['What would you like to do next?', 'Gain Insight', 'Automatically generate content from your data', 'Create', 'Report\n\t\t\t\t\t\n\t\t\t\t\tChart\n\t\t\t\t\t\n\t\t\t\t\tDocument\n\t\t\t\t\t\n\t\t\t\t\tVisualization', 'Finish', 'Go back Home']
        finished_window_text_list=self.driver.find_elements_by_css_selector(finished_window_css)
        actual_list=[elem for elem in jscript_obj.get_elements_text(finished_window_text_list) if elem != '']
        utillobj.as_List_equal(actual_list, expected_list, "Step 15: Verify the following window is displayed")
          
        """ Step 16: Click "Go Back Home" under Finish
        """
        gobackhome_elem=self.driver.find_element_by_css_selector(finished_window_gobackhome_css)
        utillobj.default_click(gobackhome_elem)
        utillobj.switch_to_window(0, pause=0)
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, 'Domains', 50)
        
        """ Step 17: Right click on "Upload" folder > Select New > "Report"
        """
        wf_mainpageobj.select_menu(projid+'->'+upload_folder_name, 'New->Report')
        elem=self.driver.find_element_by_css_selector("#toolDlg .active #btnOK")
        utillobj.default_click(elem)
        utillobj.switch_to_window(1)
        
        """ Step 18: Verify the "retail_sales.mas" file is created under respective application path (ibisamp)
        """
        """ Step 19: Click Open
        """
        portal_canvas.open_files_from_repository_window('ibisamp', ['retail_sales'], msg='Step 18:')
        visible_text = 'Drag and drop fields onto thecanvas or into the query paneto begin building your report.'
        utillobj.synchronize_with_visble_text('#TableChart_1', visible_text, 190)
        
        """ Step 20: Double click on "Revenue" from Measure fields
        """
        """ Step 21: Double click on "Store Type" from Dimensions > Retail_sales > Stores
                     Verify the following Report is displayed
        """
        meta_obj.double_click_on_data_filed("Measure Groups->Retail_sales->Revenue")
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, 190)
        meta_obj.double_click_on_data_filed("Retail_sales", field_position=2)
        meta_obj.double_click_on_data_filed('Store->Store Type')
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 6, 190)
        vis_result_obj.verify_report_titles_on_preview(2, 2, 'TableChart_1', ['Store Type', 'Revenue'], "Step 20: Verify the Report is displayed.")
#         ia_result_obj.create_report_data_set('TableChart_1', 2, 2, test_case_id+'.xlsx')
        ia_result_obj.verify_report_data_set('TableChart_1', 2, 2, test_case_id+'.xlsx', "Step 20.1: Verify the Report is displayed.")
        
        """ Step 22: Click Run
                     Verify the same output is displayed
        """
        vis_reb_obj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame()
#         ia_run_obj.create_table_data_set("table[summary='Summary']", test_case_id+'_1.xlsx')
        ia_run_obj.verify_table_data_set("table[summary='Summary']", test_case_id+'_1.xlsx', "Step 21: Verify the same output is displayed.")
        utillobj.switch_to_default_content()
        
        """ Step 23: Click IA > Exit >Click No
        """
        vis_reb_obj.select_tool_menu_item('menu_exit')
        save_dialog_css="#saveAllDlg .active"
        utillobj.synchronize_with_number_of_element(save_dialog_css, 1, 90)
        elem=self.driver.find_element_by_css_selector(save_dialog_css+" #btnNo .bi-button-label")
        utillobj.default_click(elem)
        utillobj.switch_to_window(0, pause=0)
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, 'Domains', 50)
        
        """ Step 24: Click 'Sign out'
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()