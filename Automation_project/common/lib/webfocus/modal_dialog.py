from common.lib import html_controls
from common.lib.javascript import JavaScript
from common.lib.utillity import UtillityMethods
from common.lib.webfocus import ibx_custom_controls
from common.locators import modal_dialog as Locators
from common.lib.core_utility import CoreUtillityMethods
from common.lib.global_variables import Global_variables as GV
from common.locators import paris_home_page as paris_home_page_locators

class _Base_ :
    
    def __init__(self, driver):
        
        self.driver = driver
        self._utils_ = UtillityMethods(self.driver)
        self._core_utils_ = CoreUtillityMethods(self.driver)
        self._javascript_ = JavaScript(self.driver)
        
class Common(_Base_):
    
    def __init__(self, driver, model_title):
        
        super(Common, self).__init__(driver)
        self._locator_ = Locators.Common
        self._title_ = model_title
        
    def verify_title(self, expected_title, step_num):
        """
        Description : Verify the model title 
        :Usage - verify_title("New Folder", "02.02")
        """
        title_obj = self._utils_.validate_and_get_webdriver_object_using_locator(self._locator_.title_bar_caption, self._title_ + " modal dialog title")
        actual_text =  title_obj.text.strip()
        msg = "Step {0} : Verify [{1}] displayed in ['{1}'] dialog title bar".format(step_num, expected_title, self._title_)
        self._utils_.asequal(expected_title, actual_text, msg)
    
    def close(self, wait_for_close=True):
        """
        Description : Close the modal dialog by click on close icon
        """
        close_icon_obj = self._utils_.validate_and_get_webdriver_object_using_locator(self._locator_.close_icon, self._title_ + " dialog close icon")
        self._core_utils_.left_click(close_icon_obj)
        wait_for_close and self._utils_.synchronize_until_element_disappear(self._locator_.base_css, 20)
    
    def verify_close_icon_displayed(self, step_num):
        """
        Description : Verify whether close icon is displayed or not
        :Usage : verify_close_icon("04.03")
        """
        close_icon_obj = self._utils_.validate_and_get_webdriver_object_using_locator(self._locator_.close_icon, self._title_ + " dialog close icon")
        icon_value = self._javascript_.get_element_before_style_properties(close_icon_obj, 'content')
        status = all([close_icon_obj.is_displayed(), icon_value=='"\uE14C"'])
        msg = "Step {0} : Verify Close Icon(X) is displayed in [{1}] model dialog".format(step_num, self._title_)
        self._utils_.asequal(True, status, msg)
        
    def wait_for_appear(self, time_out=20):
        """
        Description : Web driver will wait until modal dialog appear on screen
        """
        self._utils_.synchronize_until_element_is_visible(self._locator_.base_css, time_out)
    
    def wait_for_diappear(self, time_out=10):
        """
        Description : Web driver will wait until modal dialog disappear from screen
        """
        self._utils_.synchronize_until_element_disappear(self._locator_.base_css, time_out)
    
    def verify_closed(self, step_num):
        """
        Description : Verify whether model dialog is closed
        :Usage - verify_closed('06.01')
        """
        model_object = self.driver.find_elements_by_css_selector(self._locator_.base_css)
        status = model_object[0].is_displayed() if model_object != [] else False
        msg = "Step {0} : Verify [{1}] model dialog closed".format(step_num, self._title_)
        self._utils_.asequal(False, status, msg)
    
    def verify_vertical_scrollbar_displayed(self, step_num):
        """
        Description : Verify whether vertical scroll is displayed or not
        :Usage - verify_vertical_scrollbar_displayed('04.01')
        """
        content_obj = self._utils_.validate_and_get_webdriver_object_using_locator(self._locator_.message, "[{0}] model dialog content".format(self._title_))
        scrollbar_status = self._javascript_.check_element_has_vertical_scrollbar(content_obj)
        overflow = content_obj.value_of_css_property('overflow-y')
        status = all([scrollbar_status, overflow=='auto'])
        msg = 'Step {0} : Verify vertical scrollbar displayed in [{1}] model dialog'.format(step_num, self._title_)
        self._utils_.asequal(True, status, msg)
        
class TextBox(_Base_, html_controls.TextBox):
    
    def __init__(self, driver, textbox_label, model_dialog_title, parent_object=None):
        
        _Base_.__init__(self, driver)
        self._dialog_title_ = model_dialog_title
        self._textbox_label_ = textbox_label
        self._parent_object_ = parent_object
        html_controls.TextBox.__init__(self, self._object_, self._textbox_label_)
        
    @property
    def _object_(self):
        
        css = Locators.Common.textbox_css.format(self._textbox_label_)
        textbox_object = self._utils_.validate_and_get_webdriver_object(css, "{0} textbox of {1} modal dialog".format(self._textbox_label_, self._dialog_title_), parent_object=self._parent_object_)
        return textbox_object
        
    def verify_disabled(self, step_num):
        """
        Description : Verify whether textbox is disabled or not
        :Usage - verify_disabled("01.02")
        """
        parent_obj = self._javascript_.get_parent_element(self._object_)
        opacity = parent_obj.value_of_css_property('opacity')
        pointer_events = parent_obj.value_of_css_property('pointer-events')
        status = all([opacity=='0.5', pointer_events=='none'])
        msg = "Step {0} : Verify [{1}] textbox disabled in [{2}] model dialog".format(step_num, self._textbox_label_, self._dialog_title_)
        self._utils_.asequal(True, status, msg)
    
    def verify_enabled(self, step_num):
        """
        Description : Verify whether textbox is enabled.
        :Usage - verify_enabled("01.02")
        """
        parent_obj = self._javascript_.get_parent_element(self._object_)
        pointer_events = parent_obj.value_of_css_property('pointer-events')
        msg = "Step {0} : Verify [{1}] textbox enabled in [{2}] model dialog".format(step_num, self._textbox_label_, self._dialog_title_)
        self._utils_.asequal('all', pointer_events, msg)
    
class Button(_Base_):
    
    def __init__(self, driver, button_name, model_dialog_title, parent_object=None):
        
        super(Button, self).__init__(driver)
        self._parent_object_ = parent_object
        self.__title__ = model_dialog_title
        self.__name__ = button_name
    
    @property
    def _object_(self):
        
        buttons_object = self._utils_.validate_and_get_webdriver_objects_using_locator(Locators.Common.buttons, "{0} modal dialog buttons".format(self.__title__), parent_object=self._parent_object_)
        buttons_index = self._javascript_.find_element_index_by_text(buttons_object, self.__name__)
        if buttons_index is None:
            msg = "[{0}] button does not displayed in [{1}] modal dialog".format(self.__name__, self.__title__)
            raise LookupError(msg)
        else:
            return buttons_object[buttons_index]
    
    def click(self):
        """
        Description : Left click on button
        """
        self._core_utils_.left_click(self._object_)
        self._utils_.wait_for_page_loads(50)
        
    def verify_enabled(self, step_num):
        """
        Description : Verify whether button is enabled
        :Usage - verify_disabled("02.01")
        """
        opacity = self._object_.value_of_css_property('opacity').strip()
        pointer_events = self._object_.value_of_css_property('pointer-events').strip()
        state = True if (opacity == '1' and pointer_events == 'all') else False
        msg = "Step {0} : Verify [{1}] button is enabled in [{2}]  modal dialog".format(step_num, self.__name__, self.__title__)
        self._utils_.asequal(True, state, msg)
    
    def verify_disabled(self, step_num):
        """
        Description : Verify whether button is disabled
        :Usage - verify_disabled("02.01")
        """
        opacity = self._object_.value_of_css_property('opacity').strip()
        pointer_events = self._object_.value_of_css_property('pointer-events').strip()
        state = True if (opacity == '0.5' and pointer_events == 'none') else False
        msg = "Step {0} : Verify [{1}] button is disabled in [{2}]  modal dialog".format(step_num, self.__name__, self.__title__)
        self._utils_.asequal(True, state, msg)

class Alert(Common):
    
    def __init__(self, driver):
        
        self._title_ = "Alert Message"
        super(Alert, self).__init__(driver, self._title_)
    
    def verify_message(self, expected_msg, step_num):
        """
        Description : Verify the Alert dialog message
        :Usage - verify_message("Are you sure you want to delete  'Test' ?", "04.02")
        """
        actual_msg = self._utils_.validate_and_get_webdriver_object_using_locator(self._locator_.message, self._title_ + " modal dialog message").text.strip()
        msg = "Step {0} : Verify [{1}] displayed in ['{2}'] dialog".format(step_num, expected_msg, self._title_)
        self._utils_.asequal(expected_msg, actual_msg, msg)
    
    @property
    def OKButton(self): return Button(self.driver, "OK",  self._title_)
        
    @property
    def CancelButton(self): return Button(self.driver, "Cancel",  self._title_)
    
    @property
    def YesButton(self): return Button(self.driver, "Yes",  self._title_)

class ShareWithOthers(Common):
    
    def __init__(self, driver):
        
        self._title_ = "Share With Others"
        super(ShareWithOthers, self).__init__(driver, self._title_)
        self.locators = Locators.ShareWithOthers
    
    @property
    def SearchTextBox(self): return self._search_textbox_(self.driver)
    
    @property
    def UserGroupResults(self): return self._user_group_results_(self.driver)
    
    @property
    def SharedWith(self): return self._shared_with_(self.driver)
    
    @property
    def OKButton(self): return Button(self.driver, "OK",  self._title_)
        
    @property
    def CancelButton(self): return Button(self.driver, "Cancel",  self._title_)
    
    @property
    def ShareWithEveryone(self): return ibx_custom_controls.ibxCheckBoxSimple("Share with everyone")
    
    class _search_textbox_(TextBox):
        
        def __init__(self, driver):
            
            super(ShareWithOthers._search_textbox_, self).__init__(driver, "Search Input", "Share With Others")
        
        @property
        def _object_(self):
            textbox_object = self._utils_.validate_and_get_webdriver_object_using_locator(Locators.ShareWithOthers.search_textbox, "{0} textbox of {1} modal dialog".format(self._textbox_label_, self._dialog_title_))
            return textbox_object
        
        def click_dropdown_button(self):
            """
            Description : Left click on drop down button
            """
            drop_down = self._utils_.validate_and_get_webdriver_object_using_locator(Locators.ShareWithOthers.search_dropdown, "Share With Other Dialog Search Textbox drop down")
            self._core_utils_.left_click(drop_down)
        
        def verify_dropdown_dsiplayed(self, step_num):
            """
            Description : Verify whether User and Groups search text box dropdown button is dsiplayed
            """
            dropdown = self._utils_.validate_and_get_webdriver_object_using_locator(Locators.ShareWithOthers.search_dropdown, "Share With Other Dialog Search Textbox drop down")
            dropdown_value = self._javascript_.get_element_before_style_properties(dropdown, "content")
            state = True if(dropdown.is_displayed() and dropdown_value=='"\uea73"') else False
            msg = "Step {0} : Verify 'Users and groups' search textbox drop down displayed in Share with Others model dialog".format(step_num)
            self._utils_.asequal(True, state, msg)
    
    class _user_group_results_(_Base_):
        
        def __init__(self, driver):
             
            super(ShareWithOthers._user_group_results_, self).__init__(driver)
            self.locators = Locators.ShareWithOthers.UserGroupResults
        
        def verify_name_contains_searched_text(self, searched_text, step_num):
            """
            Description : Verify all results name contains searched Users/Groups
            :Usage - verify_name_contains_searched_text("Autodev", "05.02")
            """
            status = False
            for name in self._get_names_object_():
                if name.is_displayed():
                    if searched_text.lower() in name.text.lower():
                        status = True
                    else :
                        status = False
                        break
            msg = "Step {0} : Verify User/Group results name contains [{1}] in Share with others dialog".format(step_num, searched_text)
            self._utils_.asequal(True, status, msg)
            
        def verify_description_contains_searched_text(self, searched_text, step_num):
            """
            Description : Verify all results description contains searched Users/Groups
            :Usage - verify_description_contains_searched_text("Autodev", "05.02")
            """
            status = False
            for description in self._get_descriptions_object_():
                if description.is_displayed():
                    if searched_text.lower() in description.text.lower():
                        status = True
                    else :
                        status = False
                        break
            msg = "Step {0} : Verify User/Group results description contains [{1}] in Share with others dialog".format(step_num, searched_text)
            self._utils_.asequal(True, status, msg)
            
        def verify_descriptions_in_bold(self, step_num):
            """
            Description : Verify all results descriptions in bold style
            :Usage - verify_descriptions_in_bold("05.02")
            """
            status = False
            for description in self._get_descriptions_object_():
                if description.is_displayed() and ('bold' in description.get_attribute('style')):
                    status = True
                else :
                    status = False
                    break
            msg = "Step {0} : Verify User/Group results descriptions displayed in bold in Share with others dialog".format(step_num)
            self._utils_.asequal(True, status, msg)
        
        def wait_for_visible(self, time_out=30):
            """
            Description : Web driver will wait until User/Group results dialog visible on screen
            """
            self._utils_.wait_for_page_loads(15, pause_time=0.5)
            self._utils_.synchronize_until_element_is_visible(self.locators.base_css, time_out)
        
        def select(self, description):
            """
            Description : Left click on User/Group description to select.
            :Usage - select("autodevuser40")
            """
            error_msg = "[{0}] User/Group does not exist in Share with others results".format(description)
            description_obj = self._core_utils_.get_element_object_by_text_using_javascript(self._get_descriptions_object_(), description, error_msg)
            self._core_utils_.python_left_click(description_obj, yoffset=10)
            self._utils_.wait_for_page_loads(10, pause_time=2)
            
        def verify_disabled_results(self, expected_results, step_num, assert_type='asin'):
            """
            Description : Verify the disabled results(Gray out users/groups)
            :Usage - 
            """
            results = self._utils_.validate_and_get_webdriver_objects_using_locator(self.locators.results, "Share with other search results")
            actual_results = [result.text.strip().replace("\n", " ") for result in results if result.value_of_css_property("opacity")=='0.4']
            msg = "Step {0} : Verify {1} Users/Groups disabled in Share with others result dialog".format(step_num, expected_results)
            self._utils_.verify_list_values(expected_results, actual_results, msg, assert_type)   
            
        def _get_descriptions_object_(self):
            """
            Descriptions : Return the all descriptions object as list
            """
            descriptions_object = self._utils_.validate_and_get_webdriver_objects_using_locator(self.locators.descriptions, "Share with other search results description")
            return descriptions_object
        
        def _get_names_object_(self):
            """
            Descriptions : Return the all names object as list
            """
            names_object = self._utils_.validate_and_get_webdriver_objects_using_locator(self.locators.names, "Share with other search results names")
            return names_object
    
    class _shared_with_(_Base_):
        
        def __init__(self, driver):
             
            super(ShareWithOthers._shared_with_, self).__init__(driver)
            self.locators = Locators.ShareWithOthers.SharedWith
        
        def verify_users_and_groups(self, expected_values, step_num, assert_type='asin'):
            """
            Description : Verify the selected Users/Groups in Share with other 
            :Usage - verify_users_and_groups(["G458325:autodevuser203 autodevuser203(auto@devmail.com)"], "05.05")
            """
            actual_values = [item.text.strip().replace("\n", " ") for item in self.driver.find_elements(*self.locators.users_groups)]
            msg = "Step {0} : Verify {1} Users/Groups selected in Share with others dialog".format(step_num, expected_values)
            self._utils_.verify_list_values(expected_values, actual_values, msg, assert_type)   
            
        def verify_users(self, expected_users, step_num, assert_type='asin'):
            """
            Description : Verify the selected Users by checking users icon
            :Usage - verify_users(["autoadvuser01autoadvuser01(auto@devmail.com)"], "05.04")
            """
            actual_users = list()
            users_object = self.driver.find_elements(*self.locators.users_groups)
            for user in users_object:
                user_icon = self._utils_.validate_and_get_webdriver_object_using_locator(self.locators.usergroup_icon, "Selected User/Group icon", parent_object=user)
                user_icon_value = self._javascript_.get_element_after_style_properties(user_icon, 'content')
                if user_icon_value == '"\uf007"':
                    actual_users.append(user.text.strip().replace("\n", " "))
            msg = "Step {0} : Verify {1} Users selected in Share with others dialog".format(step_num, expected_users)
            self._utils_.verify_list_values(expected_users, actual_users, msg, assert_type)
            
        def verify_groups(self, expected_groups, step_num, assert_type='asin'):
            """
            Description : Verify the selected Users by checking users icon
            :Usage - verify_groups(["P406_S31920 Advanced Users P406_S31920/AdvancedUsers"], "05.04")
            """
            actual_groups = list()
            users_object = self.driver.find_elements(*self.locators.users_groups)
            for user in users_object:
                user_icon = self._utils_.validate_and_get_webdriver_object_using_locator(self.locators.usergroup_icon, "Selected User/Group icon", parent_object=user)
                user_icon_value = self._javascript_.get_element_after_style_properties(user_icon, 'content')
                if user_icon_value == '"\uf0c0"':
                    actual_groups.append(user.text.strip().replace("\n", " "))
            msg = "Step {0} : Verify {1} Users selected in Share with others dialog".format(step_num, expected_groups)
            self._utils_.verify_list_values(expected_groups, actual_groups, msg, assert_type)
        
        def verify_names_in_normal_text(self, step_num):
            """
            Description : Verify all selected Users/Groups descriptions in normal text 
            :Usage - verify_names_in_normal_text("05.01")
            """
            status = False
            for description in self.driver.find_elements(*self.locators.names):
                if description.is_displayed() and ('bold' not in description.get_attribute('style')):
                    status = True
                else :
                    status = False
                    break
            msg = "Step {0} : Verify selected Users/Groups names displayed in normal text in Share with others dialog".format(step_num)
            self._utils_.asequal(True, status, msg)
            
        def verify_descriptions_in_bold(self, step_num):
            """
            Description : Verify all selected Users/Groups descriptions in bold style
            :Usage - verify_descriptions_in_bold("05.02")
            """
            status = False
            for description in self.driver.find_elements(*self.locators.descriptions):
                if description.is_displayed() and ('bold' in description.get_attribute('style')):
                    status = True
                else :
                    status = False
                    break
            msg = "Step {0} : Verify selected Users/Groups descriptions displayed in bold in Share with others dialog".format(step_num)
            self._utils_.asequal(True, status, msg)
        
        def verify_remove_icon(self, step_num):
            """
            Description : Verify Remove icon(x) displayed in all selected Users/Groups
            :Usage - verify_remove_icon("05.02")
            """
            status = False
            for users_groups in self.driver.find_elements(*self.locators.users_groups):
                remove_btn_obj = self._utils_.validate_and_get_webdriver_object_using_locator(self.locators.remove_icon, "Selected User/Group remove icon", parent_object=users_groups)
                icon_value = self._javascript_.get_element_before_style_properties(remove_btn_obj, 'content')
                if remove_btn_obj.is_displayed() and ('"\uf00d"' == icon_value):
                    status = True
                else :
                    status = False
                    break
            msg = "Step {0} : Verify remove icon(x) displayed in all selected Users/Groups".format(step_num)
            self._utils_.asequal(True, status, msg)
        
        def remove(self, description):
            """
            Description : Left click on remove icon to remove the selected Users/Group
            :Usage - remove("autodevuser40")
            """
            error_msg = "[{0}] User/Group does not exist in selected Users/Groups".format(description)
            descriptions_objects = self._utils_.validate_and_get_webdriver_objects_using_locator(self.locators.descriptions, "Selected Users/Groups")
            description_index = self._javascript_.find_element_index_by_text(descriptions_objects, description)
            if description_index is not None:
                users = self._utils_.validate_and_get_webdriver_objects_using_locator(self.locators.users_groups, "Selected User/Group")
                remove_btn_obj = self._utils_.validate_and_get_webdriver_object_using_locator(self.locators.remove_icon, "Selected User/Group remove icon", parent_object=users[description_index])
                self._core_utils_.left_click(remove_btn_obj)
                self._utils_.wait_for_page_loads(5)
            else:
                raise LookupError(error_msg)

class Resources(Common):
    
    def __init__(self, driver):
        
        self._title_ = "Resources"
        self._locators_ = Locators.Resources
        super(Resources, self).__init__(driver, self._title_)
    
    @property
    def GridView(self):
        
        if self._is_list_view_displayed_():
            self.NavigationBar.GridView.click()
            self._utils_.wait_for_page_loads(20, 3)
        return Resources._grid_view_()
    
    @property
    def ListView(self): return Resources._list_view_()
    
    @property
    def NavigationBar(self): return self._navigation_bar_()
        
    @property
    def Title(self):  return TextBox(GV.webdriver, 'Title', self._title_)
    
    @property
    def Name(self):  return TextBox(GV.webdriver, 'Name', self._title_)
    
    @property
    def SaveButton(self): return Button(self.driver, "Save",  self._title_, self._parent_obj_)
        
    @property
    def CancelButton(self): return Button(self.driver, "Cancel",  self._title_, self._parent_obj_)
    
    @property
    def SelectButton(self): return Button(self.driver, "Select",  self._title_, self._parent_obj_)
    
    @property
    def _parent_obj_(self): return self._utils_.validate_and_get_webdriver_object_using_locator(Locators.Resources.base, "Resources Dialog")
    
    def _is_grid_view_displayed_(self):
        """
        Description : Return True if grid view is displayed in content area
        """
        grid_view = self.driver.find_elements_by_css_selector(self._locators_.GridView.base_css)
        status = True if grid_view != []  else False
        return status
        
    def _is_list_view_displayed_(self):
        """
        Description : Return True if list view is displayed in content area
        """
        list_view = self.driver.find_elements_by_css_selector(self._locators_.ListView.base_css)
        status = True if list_view != []  else False
        return status
    
    class _navigation_bar_:
        
        @property
        def BreadCrumb(self): return Resources._navigation_bar_._breadcrumb_()
        
        @property
        def Search(self): 
            object_ = GV.webdriver.find_element(*Locators.Resources.NavigationBar.search)
            return html_controls.TextBox(object_, "Resources Search")
        
        @property
        def GridView(self): return Resources._navigation_bar_._gridview_()
        
        @property
        def ListView(self): return Resources._navigation_bar_._listview_()
        
        @property
        def Refresh(self): return Resources._navigation_bar_._refresh_()
        
        class _breadcrumb_(_Base_):
            
            def __init__(self):
                super(Resources._navigation_bar_._breadcrumb_, self).__init__(GV.webdriver)
                self._locators_  = Locators.Resources.NavigationBar
                
            def select_workspaces(self):
                """
                Description : Left click on Workspaces in breadcrumb
                """
                self.select("Workspaces")
        
            def select(self, name):
                """
                Description : Left click on given breadcrumb option
                :Usage - select_breadcrumb("My Content") 
                """
                self._utils_.synchronize_with_visble_text(self._locators_.base_css, name, 60)
                breadcrumb_object =  self._utils_.validate_and_get_webdriver_object(self._locators_.breadcrumb_css.format(name), "Workspaces breadcrumb")
                self._core_utils_.left_click(breadcrumb_object)
                self._utils_.wait_for_page_loads(80, pause_time=1)
                self._utils_.synchronize_until_element_is_visible(paris_home_page_locators.Workspaces.page_load_completed_css, 120)
                
            def click_arrow(self, name):
                """
                Description : Left click on given breadcrumb arrow icon
                :Usage - select_breadcrumb("My Content") 
                """
                self._utils_.synchronize_with_visble_text(self._locators_.base_css, name, 60)
                arrow_object =  self._utils_.validate_and_get_webdriver_object(self._locators_.breadcrumb_arrow_css.format(name), "Workspaces breadcrumb arrow")
                self._core_utils_.left_click(arrow_object)
                self._utils_.synchronize_until_element_is_visible(paris_home_page_locators.Banner.popup_css, 20)
            
            def verify(self, expected_breadcrumbs, step_num):
                """
                Description : Verify the breadcrumbs text
                :Usage - verify_breadcrumbs("Workspaces>P292_S28313>G671781", "02.01")
                """
                actual_breadcrumbs = ""
                breadcrumbs_object = self._utils_.validate_and_get_webdriver_objects_using_locator(self._locators_.breadcrumbs, "Workspaces breadcrumbs")
                for breadcrumb in breadcrumbs_object :
                    breadcrumb_text = breadcrumb.text.strip()
                    actual_breadcrumbs += breadcrumb_text
                    breadcrumb_arrow_obj = self.driver.find_elements_by_css_selector(self._locators_.breadcrumb_arrow_css.format(breadcrumb_text))
                    if breadcrumb_arrow_obj != []:
                        arrow_text = self._javascript_.get_element_before_style_properties(breadcrumb_arrow_obj[0], "content").replace('"\uf054"', ">")
                        actual_breadcrumbs += arrow_text
                msg = "Step {0} : Verify [{1}] breadcrumbs displayed in Resources dialog".format(step_num, expected_breadcrumbs)
                self._utils_.asequal(expected_breadcrumbs, actual_breadcrumbs, msg)
            
        class _gridview_(_Base_):
            
            def __init__(self):
                super(Resources._navigation_bar_._gridview_, self).__init__(GV.webdriver)
            
            @property
            def _object__(self): return self._utils_.validate_and_get_webdriver_object_using_locator(Locators.Resources.NavigationBar.grid_view, "Resources GridView Button")
            
            def click(self): self._core_utils_.left_click(self._object__)
            
        class _listview_(_Base_):
            
            def __init__(self):
                super(Resources._navigation_bar_._listview_, self).__init__(GV.webdriver)
            
            def click(self): self._core_utils_.left_click(self._object__)
            
            @property
            def _object__(self): return self._utils_.validate_and_get_webdriver_object_using_locator(Locators.Resources.NavigationBar.list_view, "Resources ListView Button")
        
        class _refresh_(_Base_):
            
            def __init__(self):
                super(Resources._navigation_bar_._refresh_, self).__init__(GV.webdriver)
            
            def click(self): self._core_utils_.left_click(self._object__)
            
            @property
            def _object__(self): return self._utils_.validate_and_get_webdriver_object_using_locator(Locators.Resources.NavigationBar.refresh, "Resources Refresh Button")
            
    class _grid_view_():
        
        @property
        def Files(self): return Resources._grid_view_._files_()
        
        @property
        def Folders(self): return Resources._grid_view_._folders_()
        
        class _files_(_Base_):
         
            def __init__(self):   
                super(Resources._grid_view_._files_, self).__init__(GV.webdriver)
            
            def click(self, file_name, index=1):
                """
                Description : Left click in file
                :Usage = click('Report1')
                """
                self._core_utils_.left_click(self._object_(file_name, index))
            
            def double_click(self, file_name, index=1):
                """
                Description : Double click in file
                :Usage = double_click('Report1')
                """
                self._core_utils_.double_click(self._object_(file_name, index))
            
            def verify(self, expected_files, step_num, assert_type='asin'):
                """
                Description : Verify the visible or invisible files
                :Usage : verify_files(["C123456"], "01.02")
                """
                file_object = self.driver.find_elements(*Locators.Resources.GridView.files)
                actual_files = [file.text.strip() for file in file_object if file.is_displayed()]
                msg = "Step {0} : Verify files in Resources dialog grid view".format(step_num)
                self._utils_.verify_list_values(expected_files, actual_files, msg, assert_type) 
            
            def _object_(self, file_name, index=1):
                """
                Description : Return the file object
                """
                file_objects = self._utils_.validate_and_get_webdriver_objects_using_locator(Locators.Resources.GridView.files, "Resources GridView Files")
                msg = "[{0}] File does not exits in Resources dialog grid view".format(file_name)
                file_object = self._core_utils_.get_element_object_by_text_using_javascript(file_objects, file_name, error_msg=msg, index=index)
                return file_object
        
        class _folders_(_Base_):
         
            def __init__(self):   
                super(Resources._grid_view_._folders_, self).__init__(GV.webdriver)
            
            def click(self, folder_name, index=1):
                """
                Description : Left click in Folder
                :Usage = click('Reports')
                """
                self._core_utils_.left_click(self._object_(folder_name, index))
            
            def double_click(self, folder_path):
                """
                Description : Double click in file
                :Usage = double_click('Report1')
                """
                folders = folder_path.split('->')
                for folder_name in folders:
                    self._core_utils_.double_click(self._object_(folder_name))
                    self._utils_.wait_for_page_loads(30, pause_time=0)
                    self._utils_.synchronize_until_element_is_visible(paris_home_page_locators.Workspaces.page_load_completed_css, 120)
                    
            def verify(self, expected_folders, step_num, assert_type='asin'):
                """
                Description : Verify the visible or invisible folders
                :Usage : expected_folders(["Repots"], "01.02")
                """
                folder_object = self.driver.find_elements(*Locators.Resources.GridView.folders)
                actual_folders = [folder.text.strip() for folder in folder_object if folder.is_displayed()]
                msg = "Step {0} : Verify folders in Resources dialog grid view".format(step_num)
                self._utils_.verify_list_values(expected_folders, actual_folders, msg, assert_type) 
            
            def _object_(self, folder_name, index=1):
                """
                Description : Return the file object
                """
                folder_objects = self._utils_.validate_and_get_webdriver_objects_using_locator(Locators.Resources.GridView.folders, "Resources GridView Files")
                msg = "[{0}] File folder not exits in Resources dialog grid view".format(folder_name)
                folder_object = self._core_utils_.get_element_object_by_text_using_javascript(folder_objects, folder_name, error_msg=msg, index=index)
                return folder_object
            
    class _list_view_():
        
        @property
        def Files(self): return Resources._grid_view_._files_()
        
        @property
        def Folders(self): return Resources._grid_view_._folders_()
        
        class _files_(_Base_):
         
            def __init__(self):   
                super(Resources._list_view_._files_, self).__init__(GV.webdriver)
            
            def click(self, file_name, index=1):
                """
                Description : Left click in file
                :Usage = click('Report1')
                """
                self._core_utils_.left_click(self._object_(file_name, index))
            
            def double_click(self, file_name, index=1):
                """
                Description : Double click in file
                :Usage = double_click('Report1')
                """
                self._core_utils_.double_click(self._object_(file_name, index))
            
            def verify(self, expected_files, step_num, assert_type='asin'):
                """
                Description : Verify the visible or invisible files
                :Usage : verify_files(["C123456"], "01.02")
                """
                file_object = self.driver.find_elements(*Locators.Resources.GridView.files)
                actual_files = [file.text.strip() for file in file_object if file.is_displayed()]
                msg = "Step {0} : Verify files in Resources dialog grid view".format(step_num)
                self._utils_.verify_list_values(expected_files, actual_files, msg, assert_type) 
            
            def _object_(self, file_name, index=1):
                """
                Description : Return the file object
                """
                file_objects = self._utils_.validate_and_get_webdriver_objects_using_locator(Locators.Resources.GridView.files, "Resources GridView Files")
                msg = "[{0}] File does not exits in Resources dialog grid view".format(file_name)
                file_object = self._core_utils_.get_element_object_by_text_using_javascript(file_objects, file_name, error_msg=msg, index=index)
                return file_object
        
        class _folders_(_Base_):
         
            def __init__(self):   
                super(Resources._list_view_._folders_, self).__init__(GV.webdriver)
            
            def click(self, folder_name, index=1):
                """
                Description : Left click in Folder
                :Usage = click('Reports')
                """
                self._core_utils_.left_click(self._object_(folder_name, index))
            
            def double_click(self, folder_path):
                """
                Description : Double click in file
                :Usage = double_click('Report1')
                """
                folders = folder_path.split('->')
                for folder_name in folders:
                    self._core_utils_.double_click(self._object_(folder_name))
                    self._utils_.wait_for_page_loads(30, pause_time=0)
                    self._utils_.synchronize_until_element_is_visible(paris_home_page_locators.Workspaces.page_load_completed_css, 120)
                    
            def verify(self, expected_folders, step_num, assert_type='asin'):
                """
                Description : Verify the visible or invisible folders
                :Usage : expected_folders(["Repots"], "01.02")
                """
                folder_object = self.driver.find_elements(*Locators.Resources.GridView.folders)
                actual_folders = [folder.text.strip() for folder in folder_object if folder.is_displayed()]
                msg = "Step {0} : Verify folders in Resources dialog grid view".format(step_num)
                self._utils_.verify_list_values(expected_folders, actual_folders, msg, assert_type) 
            
            def _object_(self, folder_name, index=1):
                """
                Description : Return the file object
                """
                folder_objects = self._utils_.validate_and_get_webdriver_objects_using_locator(Locators.Resources.GridView.folders, "Resources GridView Files")
                msg = "[{0}] File folder not exits in Resources dialog grid view".format(folder_name)
                folder_object = self._core_utils_.get_element_object_by_text_using_javascript(folder_objects, folder_name, error_msg=msg, index=index)
                return folder_object