'''
Created on 29-Jan-2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10851
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2358903
TestCase Name = Add Global filter in a Document for charts (GRMERGE=ADVANCED).
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, active_miscelaneous, visualization_resultarea, ia_run, wf_legacymainpage, active_filter_selection
from common.lib.basetestcase import BaseTestCase

class C2358903_TestClass(BaseTestCase):

    def test_C2358903(self):
        """
        TESTCASE VARIABLES
        """
        test_case_id = 'C2358903'
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        active_mis_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        main_pageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        actfilter = active_filter_selection.Active_Filter_Selection(self.driver)
        
        def verify_live_preview_chart(parent_id, number_of_riser, step_no, x_title, y_title, x_lable, y_lable, xy_label_length, riser_class, color):
            vis_resultobj.verify_number_of_riser(parent_id, 1, number_of_riser, "Step "+str(step_no)+" .1: Verify number of bar riser.")
            vis_resultobj.verify_xaxis_title(parent_id, x_title, "Step "+str(step_no)+" .2: Verify x_title in bar chart.")
            vis_resultobj.verify_yaxis_title(parent_id, y_title, "Step "+str(step_no)+" .3: Verify y_title in bar chart.")
            vis_resultobj.verify_riser_chart_XY_labels(parent_id, x_lable, y_lable, "Step "+str(step_no)+" .4: Verify xy_label in bar chart.", x_axis_label_length=xy_label_length)
            utillobj.verify_chart_color(parent_id, riser_class, color, "Step "+str(step_no)+" .5: Verify color in bar chart.")
            
        def veify_run_chart(parent_id, number_of_riser, step_no, x_title, y_title, x_lable, y_lable, xy_label_length, raiser_class, color, chart_title, bar_filter_menu, bar_tooltip):
            vis_resultobj.verify_number_of_riser(parent_id+'_f', 1, number_of_riser, "Step "+str(step_no)+".1: Verify number of riser in bar chart.")
            vis_resultobj.verify_xaxis_title(parent_id, x_title, "Step "+str(step_no)+".2: Verify bar x-axis_title.")
            vis_resultobj.verify_yaxis_title(parent_id, y_title, "Step "+str(step_no)+".3: Verify bar y-axis_title.")
            vis_resultobj.verify_riser_chart_XY_labels(parent_id, x_lable, y_lable, "Step "+str(step_no)+".4: Verify bar-xy-axis_Labels.", x_axis_label_length=xy_label_length)
            utillobj.verify_chart_color(parent_id, raiser_class, color, "Step "+str(step_no)+".5: Verify bar chart color.")
            active_mis_obj.verify_chart_title(parent_id, chart_title, "Step "+str(step_no)+".6: Verify bar chart title.")
            active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu'+str(parent_id[-1]), bar_filter_menu, "Step "+str(step_no)+".26: Verify bar filter menu..", custom_css="[title]")
            active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu'+str(parent_id[-1]), ['Sum'],"Step "+str(step_no)+".27: Verify bar menu sum text.", custom_css=".arChartMenuBarContainer .tabPagingText1 [id*='SUM'] td[valign]", text=True)
            vis_resultobj.verify_default_tooltip_values(parent_id, raiser_class, bar_tooltip, "Step "+str(step_no)+".28: Verify bar tooltip.")
            
        """ Step 1: Create a new Document using the ggsales file.
                    Select Active Report as the Output Format.
                    From the Insert icon, add a Text Box with the text "Global Filter for Document containing Reports" .
                    Expect to see the following Document canvas with the Text Box added.
        """
        utillobj.infoassist_api_login('document', 'ibisamp/ggsales', 'S10851_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 25)
        vis_ribbon.switch_ia_tab('Home')
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 1: Verify output format as Active report.")
        vis_ribbon.select_ribbon_item("Insert", "Text_Box")
        ia_resultobj.enter_text_in_Textbox('Text_1', "Global Filter for Document containing Reports")
        expected_value = "Global Filter for Document containing Reports"
        ia_resultobj.verify_document_objects('#Text_1', 'textbox', 'Step 1.1: Verify "Global Filter for Document containing Reports" enterd in textbox.', expected_value=expected_value)
            
        """ Step 2: Use the Insert button to add a Chart underneath the TextBox.
                    Add Unit Sales as the measure and State as the X Axis sort field.
                    Expect to see the following Chart preview pane appear.
        """
        vis_ribbon.select_ribbon_item("Insert", "Chart")
        utillobj.synchronize_with_number_of_element("#TableChart_1 text[class*='xaxis']", 5, 15)
        ia_resultobj.drag_drop_document_component('#TableChart_1', '#Text_1', 110, 110, target_drop_point='bottom_right')
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(7)"
        utillobj.synchronize_with_visble_text(element_css, 'UnitSales', 25)
            
        vis_metadata.datatree_field_click('State', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(9)"
        utillobj.synchronize_with_visble_text(element_css, 'State', 25)
            
        x_lable=['CA', 'CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA']
        y_lable=['0', '20K', '40K', '60K', '80K', '100K']
        verify_live_preview_chart('TableChart_1', 11, '2', 'State', 'Unit Sales', x_lable, y_lable, 2, 'riser!s0!g0!mbar', 'bar_blue1')
            
        """ Step 3: Click the Page button at the top left to create a second page for the Document.
                    Expect to see a blank canvas for Page 2.
        """
        ia_resultobj.select_or_verify_document_page_menu('New Page')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 25)
        page2_canvas_text = self.driver.find_element_by_css_selector("#theCanvas").text.strip()
        utillobj.asequal('', page2_canvas_text, "Step 3: Verify Page 2 canvas is blank.")
            
        """ Step 4: Using the Insert button, add another Chart to the canvas.
                    Select fields State and Category for the X Axis and Unit Sales for the measure.
                    Move the Chart slightly upwards, so that the entire Chart preview is visible.
                    Expect to see the preview pane for the Page 2 Chart.
        """
        vis_ribbon.select_ribbon_item("Insert", "Chart")
        utillobj.synchronize_with_number_of_element("#TableChart_2 text[class*='xaxis']", 5, 15)
        vis_metadata.datatree_field_click('State', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(8)"
        utillobj.synchronize_with_visble_text(element_css, 'State', 25)
            
        vis_metadata.datatree_field_click('Category', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(9)"
        utillobj.synchronize_with_visble_text(element_css, 'Category', 25)
            
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(7)"
        utillobj.synchronize_with_visble_text(element_css, 'UnitSales', 25)
            
        ia_resultobj.drag_drop_document_component('#TableChart_2', '#TableChart_2', 50, -25, target_drop_point='top_right')
        x_lable=['CA : Coffee', 'CT : Coffee', 'FL : Coffee', 'GA : Coffee', 'IL : Coffee', 'MA : Coffee', 'MO : Coffee', 'NY : Coffee', 'TN : Coffee', 'TX : Coffee', 'WA : Coffee']
        y_lable=['0', '20K', '40K', '60K', '80K', '100K']
        verify_live_preview_chart('TableChart_2', 11, '4', 'State : Category', 'Unit Sales', x_lable, y_lable, 7, 'riser!s0!g0!mbar', 'bar_blue1')
            
        """ Step 5: Save the report as C358903.fex and run the report
        """
        vis_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(test_case_id)
        time.sleep(2)
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=3)
        ia_runobj.select_active_document_page_layout_menu('Page 1')
        utillobj.synchronize_with_number_of_element("[id^='LOBJText'] table > tbody > tr", 1, 15)
        expected_value = ['Global Filter for Document containing Reports']
        ia_runobj.verify_document_objects("[id^='LOBJText']", 'textbox', 'Step 5: Verify "Global Filter for Document containing Reports" enterd in textbox.', expected_value_list=expected_value)
        x_lable=['CA', 'CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA']
        y_lable=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K']
        chart_title='Unit Sales BY State'
        bar_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        bar_tooltip=['State:CA', 'Unit Sales:610570', 'Filter Chart', 'Exclude from Chart']
        veify_run_chart('MAINTABLE_wbody0', 11, 5.1, 'State', 'Unit Sales', x_lable, y_lable, 2, 'riser!s0!g0!mbar', 'bar_blue1', chart_title, bar_filter_menu, bar_tooltip)
            
        ia_runobj.select_active_document_page_layout_menu('Page 2')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1", 1, 15)
        x_lable=['CA : Coffee', 'CA : Food', 'CA : Gifts', 'CT : Coffee', 'CT : Food', 'CT : Gifts', 'FL : Coffee', 'FL : Food', 'FL : Gifts', 'GA : Coffee', 'GA : Food', 'GA : Gifts', 'IL : Coffee', 'IL : Food', 'IL : Gifts', 'MA : Coffee', 'MA : Food', 'MA : Gifts', 'MO : Coffee', 'MO : Food', 'MO : Gifts', 'NY : Coffee']
        y_lable=['0', '40K', '80K', '120K', '160K', '200K', '240K', '280K']
        chart_title='Unit Sales BY State, Category'
        bar_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        bar_tooltip=['State:CA', 'Category:Coffee', 'Unit Sales:235583', 'Filter Chart', 'Exclude from Chart']
        veify_run_chart('MAINTABLE_wbody1', 33, 5.2, 'State : Category', 'Unit Sales', x_lable, y_lable, 2, 'riser!s0!g0!mbar', 'bar_blue1', chart_title, bar_filter_menu, bar_tooltip)
        ia_runobj.verify_active_document_page_layout_menu("[id^='iLayTB']", ['Layouts', 'Page 1', 'Page 2'], "Step 5.3: Verify page menu layout.")
        utillobj.switch_to_default_content(pause=2)
        utillobj.infoassist_api_logout()
            
        """ Step 6: Edit the saved Fex with the Text Editor and change the Keyword/Value combination from SHOW_GLOBALFILTER=OFF to SHOW_GLOBALFILTER=ON.
                    Save each changed version and exit the editor.
                    Expect to see the changed line in each saved Fex.
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#PortalResourcevBOX table tr td", 'Domains', 25)
        main_pageobj.select_menu('P116->S10851_2->'+test_case_id, 'Edit With...->Text Editor')
        utillobj.synchronize_with_number_of_element("#bipEditor [class*='active'] #bipEditorArea", 1, 25)
        main_pageobj.edit_fex_in_text_editor(find='SHOW_GLOBALFILTER=OFF', repl='SHOW_GLOBALFILTER=ON')
        utillobj.synchronize_with_number_of_element("#bipEditor [class*='active'] #bipEditorArea", 0, 25)
            
        main_pageobj.select_menu('P116->S10851_2->'+test_case_id, 'Edit With...->Text Editor')
        utillobj.synchronize_with_number_of_element("#bipEditor [class*='active'] #bipEditorArea", 1, 25)
        expected_syntax_list = ["SHOW_GLOBALFILTER=ON"]
        texteditor_text = self.driver.find_element_by_css_selector("#bipEditor [class*='active'] #bipEditorArea").get_attribute('value')
        for syntax in expected_syntax_list :
            if syntax in texteditor_text :
                status=True
            else:
                status=False
                break
        utillity.UtillityMethods.asequal(self,True,status,"Step 6: Verify changes saved in text editor syntax.")
        elem = self.driver.find_element_by_css_selector("#bipEditor [class*='active'] [class*='window'][class*='close']")
        utillobj.click_on_screen(elem, 'middle', click_type=0)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        """ Step 7: Execute the saved Document(GLOBALFILTER=ON)
                    Expect to see the following initial display for each version.
                    Page 1 containing 11 Bars:
                    Page 2 containing 33 Bars, 3 Categories for each of the 11 States:
        """
        utillobj.active_run_fex_api_login(test_case_id+'.fex', 'S10851_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("div#MAINTABLE_wbody0", 1, 25)
        ia_runobj.select_active_document_page_layout_menu('Page 1')
        time.sleep(5)
        utillobj.synchronize_with_number_of_element("div#MAINTABLE_wbody0", 1, 25)
        expected_value = ['Global Filter for Document containing Reports']
        ia_runobj.verify_document_objects("[id^='LOBJText']", 'textbox', 'Step 7: Verify "Global Filter for Document containing Reports" enterd in textbox.', expected_value_list=expected_value)
        x_lable=['CA', 'CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA']
        y_lable=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K']
        chart_title='Unit Sales BY State'
        bar_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        bar_tooltip=['State:CA', 'Unit Sales:610570', 'Filter Chart', 'Exclude from Chart']
        veify_run_chart('MAINTABLE_wbody0', 11, '7.1', 'State', 'Unit Sales', x_lable, y_lable, 2, 'riser!s0!g0!mbar', 'bar_blue1', chart_title, bar_filter_menu, bar_tooltip)
         
        ia_runobj.select_active_document_page_layout_menu('Page 2')
        time.sleep(5)
        utillobj.synchronize_with_number_of_element("div#MAINTABLE_wbody1", 1, 25)
        x_lable=['CA : Coffee', 'CA : Food', 'CA : Gifts', 'CT : Coffee', 'CT : Food', 'CT : Gifts', 'FL : Coffee', 'FL : Food', 'FL : Gifts', 'GA : Coffee', 'GA : Food', 'GA : Gifts', 'IL : Coffee', 'IL : Food', 'IL : Gifts', 'MA : Coffee', 'MA : Food', 'MA : Gifts', 'MO : Coffee', 'MO : Food', 'MO : Gifts', 'NY : Coffee']
        y_lable=['0', '40K', '80K', '120K', '160K', '200K', '240K', '280K']
        chart_title='Unit Sales BY State, Category'
        bar_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        bar_tooltip=['State:CA', 'Category:Coffee', 'Unit Sales:235583', 'Filter Chart', 'Exclude from Chart']
        veify_run_chart('MAINTABLE_wbody1', 33, '7.2', 'State : Category', 'Unit Sales', x_lable, y_lable, 2, 'riser!s0!g0!mbar', 'bar_blue1', chart_title, bar_filter_menu, bar_tooltip)
        ia_runobj.verify_active_document_page_layout_menu("[id^='iLayTB']", ['Layouts', 'Page 1', 'Page 2', ''], "Step 7.3: Verify page menu layout.")
        utillobj.verify_element_visiblty(element_css="form[name='mergeform'] [id^='iLayTB'] tr td span[title='Global Filter'] img", msg="Step 7.4: Verify Filter option visible in Layout menu.")
        
        """ Step 8: Tap the Global Filter icon to apply a Global filter to the Document.
                    Expect to see the Global Filter panel appear.
        """
        ia_runobj.select_active_document_page_layout_menu('Page 1')
        time.sleep(5)
        utillobj.synchronize_with_number_of_element("div#MAINTABLE_wbody0", 1, 25)
        global_filter_obj = self.driver.find_element_by_css_selector("form[name='mergeform'] [id^='iLayTB'] tr td span[title='Global Filter'] img")
        utillobj.click_on_screen(global_filter_obj, 'middle', click_type=0)
        utillobj.synchronize_with_number_of_element("#wall1[style*='block']", 1, 15)
        utillobj.verify_element_text("#wall1[style*='block'] .arWindowBarTitle", 'Global Filter', "Step 8: Verify Global Filter panel appear.")
            
        """ Step 9: Click the Add Condition tab and select State as the Filter field.
                    Change the operator from Equals to Not equal.
                    From the drop down list of values select CA & CT for exclusion.
                    Expect to see the following Filter panel.
        """
        actfilter.add_global_condition_field('State', parent_menu_css="0_globalop_x__0")
        utillobj.synchronize_with_visble_text("#FiltTable1 tr.arFilterItem:nth-child(2)  td span[title]", 'State', 9)
        actfilter.verify_filter_selection_dialog(True, 'Step 9: Verify Filter that the selection menu appears:',['State', 'Equals'],row_num=2)
        actfilter.verify_filter_values_menu_list(1, ['CA', 'CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA'], "Step 9.1: Verify Filter that the selection menu appears:")
        actfilter.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 9.2: Verify Filter that the selection menu appears:")
        actfilter.create_filter(1, 'Not equal', value1='CA', value2='CT')
        
        """ Step 10: Click the Filter button to apply the selections.
                    Expect to see the following Filtered reports.
                    Page 1 containing 9 Bars, with CA & CT removed.
                    Page 2 containing 27 Bars, with CA & CT removed.
        """
        actfilter.filter_button_click('Filter')
        utillobj.synchronize_with_number_of_element("[id^='dt0_ftp'][style*='block']", 0, 10)
        expected_value = ['Global Filter for Document containing Reports']
        ia_runobj.verify_document_objects("[id^='LOBJText']", 'textbox', 'Step 10: Verify "Global Filter for Document containing Reports" enterd in textbox.', expected_value_list=expected_value)
        x_lable=['FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA']
        y_lable=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        chart_title='Unit Sales BY State'
        bar_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        bar_tooltip=['State:FL', 'Unit Sales:310302', 'Filter Chart', 'Exclude from Chart']
        veify_run_chart('MAINTABLE_wbody0', 9, '10.1', 'State', 'Unit Sales', x_lable, y_lable, 2, 'riser!s0!g0!mbar', 'bar_blue1', chart_title, bar_filter_menu, bar_tooltip)
        
        ia_runobj.select_active_document_page_layout_menu('Page 2')
        time.sleep(5)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1", 1, 15)
        x_lable=['FL : Coffee', 'FL : Food', 'FL : Gifts', 'GA : Coffee', 'GA : Food', 'GA : Gifts', 'IL : Coffee', 'IL : Food', 'IL : Gifts', 'MA : Coffee', 'MA : Food', 'MA : Gifts', 'MO : Coffee', 'MO : Food', 'MO : Gifts', 'NY : Coffee', 'NY : Food', 'NY : Gifts', 'TN : Coffee', 'TN : Food', 'TN : Gifts', 'TX : Coffee']
        y_lable=['0', '30K', '60K', '90K', '120K', '150K']
        chart_title='Unit Sales BY State, Category'
        bar_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        bar_tooltip=['State:FL', 'Category:Coffee', 'Unit Sales:114996', 'Filter Chart', 'Exclude from Chart']
        veify_run_chart('MAINTABLE_wbody1', 27, '10.2', 'State : Category', 'Unit Sales', x_lable, y_lable, 2, 'riser!s0!g0!mbar', 'bar_blue1', chart_title, bar_filter_menu, bar_tooltip)
        ia_runobj.verify_active_document_page_layout_menu("[id^='iLayTB']", ['Layouts', 'Page 1', 'Page 2', ''], "Step 10.3: Verify page menu layout.")
        
        """ Step 11: Click on Clear All button and click on the Global Filter x button to close
                     Expect to see the original reports, with all States appearing.
        """
        actfilter.filter_button_click('Clear All')
        active_mis_obj.close_popup_dialog('1')
        utillobj.synchronize_with_number_of_element("#wall1[style*='block']", 0, 10)
        ia_runobj.select_active_document_page_layout_menu('Page 1')
        time.sleep(5)
        expected_value = ['Global Filter for Document containing Reports']
        ia_runobj.verify_document_objects("[id^='LOBJText']", 'textbox', 'Step 11: Verify "Global Filter for Document containing Reports" enterd in textbox.', expected_value_list=expected_value)
        x_lable=['CA', 'CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA']
        y_lable=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K']
        chart_title='Unit Sales BY State'
        bar_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        bar_tooltip=['State:CA', 'Unit Sales:610570', 'Filter Chart', 'Exclude from Chart']
        veify_run_chart('MAINTABLE_wbody0', 11, '11.1', 'State', 'Unit Sales', x_lable, y_lable, 2, 'riser!s0!g0!mbar', 'bar_blue1', chart_title, bar_filter_menu, bar_tooltip)
        
        ia_runobj.select_active_document_page_layout_menu('Page 2')
        time.sleep(5)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1", 1, 15)
        x_lable=['CA : Coffee', 'CA : Food', 'CA : Gifts', 'CT : Coffee', 'CT : Food', 'CT : Gifts', 'FL : Coffee', 'FL : Food', 'FL : Gifts', 'GA : Coffee', 'GA : Food', 'GA : Gifts', 'IL : Coffee', 'IL : Food', 'IL : Gifts', 'MA : Coffee', 'MA : Food', 'MA : Gifts', 'MO : Coffee', 'MO : Food', 'MO : Gifts', 'NY : Coffee']
        y_lable=['0', '40K', '80K', '120K', '160K', '200K', '240K', '280K']
        chart_title='Unit Sales BY State, Category'
        bar_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        bar_tooltip=['State:CA', 'Category:Coffee', 'Unit Sales:235583', 'Filter Chart', 'Exclude from Chart']
        veify_run_chart('MAINTABLE_wbody1', 33, '11.2', 'State : Category', 'Unit Sales', x_lable, y_lable, 2, 'riser!s0!g0!mbar', 'bar_blue1', chart_title, bar_filter_menu, bar_tooltip)
        ia_runobj.verify_active_document_page_layout_menu("[id^='iLayTB']", ['Layouts', 'Page 1', 'Page 2', ''], "Step 11.3: Verify page menu layout.")
        
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()