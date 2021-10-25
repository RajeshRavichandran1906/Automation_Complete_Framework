import time, keyboard
from common.lib.base import BasePage
from common.pages.infographic import InfoGraphic as info_graphic
from common.pages.visualization_metadata import Visualization_Metadata as visual_metaobj
from common.pages.ia_ribbon import IA_Ribbon as ribbonobject
from common.wftools.login import Login as wf_login
from common.lib.utillity import UtillityMethods as utillobj
from common.pages.visualization_ribbon import Visualization_Ribbon as visual_ribbobobj

class InfoGraphics(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(InfoGraphics, self).__init__(driver)

    def signin_to_WF_with_user(self, oUser,oPassword,page_css,wait_time=0):
        '''
        This function login to WF with user sepecified
        @param oUser: 'mruser' specify the user type - developer/advanced user/basic user
        @param oPassword: 'mrpass' specify the password
        @param page_css: specify the CSS used to sync and then pass it to next line execution
        '''
        wait_time=self.report_long_timesleep if wait_time==0 else wait_time
        wf_login.invoke_home_page(self,oUser,oPassword)
        utillobj.synchronize_with_visble_text(self,page_css, 'Workspaces', wait_time)
        
    def run_infographic_using_api_url(self, oProjFolder, oProjSubFolder, oFex_Name, oSyncCSS, no_of_element, oUser, wait_time=0):
        '''
        @summary: This function will run Infographic fex using api link 
        @param oProjFolder: 'specify the ProjectID_suiteID
        @param oProjSubFolder: specify the Group ID
        @param oFex_Name: specify the Fex Name
        @param oSyncCSS: specigy the css used for sync
        @param no_of_element: specify the number of elements for the specifed synccss
        @param oUser: specify user type
        '''
        wait_time=self.chart_long_timesleep if wait_time==0 else wait_time
        info_graphic.run_infographic_using_api(self,oProjFolder, oProjSubFolder, oFex_Name, oUser)
        utillobj.synchronize_with_number_of_element(self,oSyncCSS, no_of_element, wait_time)
    
    def restore_infographic_using_api_url(self, oProjFolder, oProjSubFolder, oFex_Name, oSyncCSS, no_of_element, oUser, wait_time=0):
        '''
        Desc:- This function will restore Infographic fex using api link 
        @param oProjFolder: 'specify the ProjectID_suiteID
        @param oProjSubFolder: specify the Group ID
        @param oFex_Name: specify the Fex Name
        @param oSyncCSS: specigy the css used for sync
        @param no_of_element: specify the number of elements for the specifed synccss
        @param oUser: specify user type
        '''
        wait_time=self.chart_long_timesleep if wait_time==0 else wait_time
        info_graphic.restore_infographic_using_api(self,oProjFolder, oProjSubFolder, oFex_Name, oUser)
        utillobj.synchronize_with_number_of_element(self,oSyncCSS, no_of_element, wait_time)
    
    def delete_text_from_header_footer_dialog(self, tabname_css, del_COUNT):
        textbox_obj=self.driver.find_element_by_css_selector(tabname_css)
        utillobj.click_on_screen(self,textbox_obj, coordinate_type='middle', click_type=0)
        time.sleep(1)
        keyboard.send('home')
        time.sleep(1)
        count=0
        while count<del_COUNT:
            keyboard.send('del')
            count+=1
        time.sleep(1)
    
    def delete_and_enter_text_in_header_footer_dialog(self, tabname_css, del_COUNT, TEXT):
        textbox_obj=self.driver.find_element_by_css_selector(tabname_css)
        utillobj.click_on_screen(self,textbox_obj, coordinate_type='middle', click_type=0)
        time.sleep(1)
        keyboard.send('home')
        time.sleep(1)
        count=0
        while count<del_COUNT:
            keyboard.send('del')
            count+=1
        time.sleep(1)
        keyboard.write(TEXT, delay=1)
        time.sleep(3)
        
    def scrolled_into_view(self, object_to_view):
        '''
        This function bring the hidden DOM object to View
        '''
        time.sleep(1)
        self.driver.execute_script('arguments[0].scrollIntoView(true);',object_to_view)
        time.sleep(2)
    
    def select_item_in_top_toolbar(self, top_toolbar_item_name):
        '''
        Desc: This function is specific to click on top toolbar buttons - new, run, undo, redo, run.
        '''
        ribbonobject.select_ia_top_toolbar_item(self, top_toolbar_item_name)
        
    def run_chart_from_toptoolbar(self):
        '''
        Desc: This is used to run visualization from the top toolbar.
        '''
        ribbonobject.select_ia_top_toolbar_item(self, 'run')
    
    def verify_all_fields_in_query_pane(self, expected_fields, msg):
        """
        Desc: This function will verify all fields listed in querypane
        """
        visual_metaobj.verify_query_panel_all_field(self, expected_fields,msg)
    
    def right_click_on_field_under_query_tree(self, field_name, field_position, context_menu_path):
        '''
        Desc:- This function is used to right click on the field in query tree and select the item from the context menu
        '''
        visual_metaobj.select_querytree_field(self, field_name, 'right', field_position, context_menu_path)
    
    def select_item_from_ribbon(self, tab_name, ribbon_button_name_path):
        '''
        Desc: This is used to select chart type.
        '''
        visual_ribbobobj.select_visualization_ribbon_item(self, tab_name, ribbon_button_name_path)
        
    def drag_field_from_data_tree_to_query_pane(self, field_name, field_position, bucket_name, bucket_position=1):
        '''
        Desc:- This function is used to drag and drop data field to the specified bucket in query tree.
        :param - field_position: 1,2 .. (first match is 1)
        :param - bucket_position: 1,2 .. (first match is 1)
        :usage drag_field_from_data_tree_to_query_pane("PRICE_DOLLARS_BIN_1",1,"Model",1)
        '''
        visual_metaobj.drag_and_drop_from_data_tree_to_query_tree(self, field_name, field_position, bucket_name,bucket_position)
    
    def click_bibutton_in_dialog(self, btn_css, btn_name):
        '''
        Desc: This is used to click on any button whose ID start with 'BiButton'.
        @param: btn_css: "div[id^='BiDialog'] div[class=bi-button-label]"
        @param: btn_name: "OK"
        '''        
        dialog_btns=self.driver.find_elements_by_css_selector(btn_css)
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index(btn_name)].click()
        time.sleep(5)
    