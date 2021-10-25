from common.locators import paris_home_page as paris_home_page_locators
from common.lib.web_element_utils import WebElementUtils
from common.lib.global_variables import Global_variables 
from common.lib.webfocus.context_menu import ContextMenu
from common.lib.core_utility import CoreUtillityMethods
from common.lib.webfocus import ibx_custom_controls
from selenium.webdriver.support.color import Color
from common.lib.utillity import UtillityMethods
from common.lib.webfocus import modal_dialog
from common.lib.javascript import JavaScript
from common.lib import html_controls
import keyboard

class __Common__:
    
    def __init__(self, driver):
        
        self.driver = driver
        self._core_utils = CoreUtillityMethods(self.driver)
        self._utils = UtillityMethods(self.driver)
        self._javascript = JavaScript(self.driver)
        self._web_element = WebElementUtils()
        
class Banner(__Common__):
    
    def __init__(self, driver):
        
        super(Banner, self).__init__(driver)
        self.locators = paris_home_page_locators.Banner
        
    def click_home(self):
        """
        Description : Left click on Home logo in banner area
        """
        home_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.home, "Home logo")
        self._core_utils.left_click(home_obj)
        self._utils.synchronize_with_visble_text(paris_home_page_locators.Home.favorites_section_css, "FAVORITES", 30)
    
    def click_my_workspace(self):
        """
        Description : Left click on My Workspace in banner area
        """
        my_workspace_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.my_workspace, "My workspace")
        self._core_utils.left_click(my_workspace_obj)
        my_workspace_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.my_workspace, "My workspace")
        ('current' not in my_workspace_obj.get_attribute("class")) and self._core_utils.left_click(my_workspace_obj)
        self._utils.synchronize_with_visble_text(paris_home_page_locators.MyWorkspace.root_css, "MY WORKSPACE", 30)
    
    def click_shared_with_me(self):
        """
        Description : Left click on Shared with Me in banner area
        """
        shared_with_me_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.shared_with_me, "Shared with Me")
        self._core_utils.left_click(shared_with_me_obj)
        shared_with_me_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.shared_with_me, "Shared with Me")
        ('current' not in shared_with_me_obj.get_attribute("class")) and self._core_utils.left_click(shared_with_me_obj)
        self._utils.synchronize_with_visble_text(paris_home_page_locators.SharedWithMe.root_css, "SHARED WITH ME", 30)
    
    def click_workspaces(self, switch_to_frame=False):
        """
        Description : Left click on Workspaces in banner area
        """
        workspaces_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.workspaces, "Workspaces")
        self._core_utils.left_click(workspaces_obj)
        workspaces_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.workspaces, "Workspaces")
        ('current' not in workspaces_obj.get_attribute("class")) and self._core_utils.left_click(workspaces_obj)
        self._utils.wait_for_page_loads(80, pause_time=2)
        self._utils.synchronize_until_element_is_visible(paris_home_page_locators.Workspaces.iframe_css, 80)
        (switch_to_frame) and Workspaces(self.driver).switch_to_frame()
        
    def click_utilities(self):
        """
        Description : Left click on utilities menu in banner area
        """
        utilities_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.utilities, "Utilities menu icon")
        self._core_utils.left_click(utilities_obj)
        self._utils.synchronize_until_element_is_visible(self.locators.popup_css, 10)
    
    def click_settings(self):
        """
        Description : Left click on settings menu in banner area
        """
        settings_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.settings, "Settings menu icon")
        self._core_utils.left_click(settings_obj)
        self._utils.synchronize_until_element_is_visible(self.locators.popup_css, 10)
    
    def click_help(self):
        """
        Description : Left click on Help menu in banner area
        """
        help_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.help, "Help menu icon")
        self._core_utils.left_click(help_obj)
        self._utils.synchronize_until_element_is_visible(self.locators.popup_css, 10)
    
    def click_invite_user(self):
        """
        Description : Left click on Invite user menu in banner area
        """
        invite_user = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.invite_user, "Invite user")
        self._core_utils.left_click(invite_user)
        ModalDialogs(self.driver).InviteUser.wait_for_appear()
        
    def click_user(self):
        """
        Description : Left click on User menu in banner area
        """
        user_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.user, "User menu icon")
        self._core_utils.left_click(user_obj)
        self._utils.synchronize_until_element_is_visible(self.locators.popup_css, 10)
    
    def click_plus(self):
        """
        Description : Left click on Plus Icon in banner area
        """
        plus_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.plus_icon, "Plus icon")
        self._core_utils.left_click(plus_obj)
    
    def click_get_data(self):
        """
        Description : Left click on Get Data in banner area
        """
        get_data_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.get_data, "Get Data")
        self._core_utils.left_click(get_data_obj)
    
    def click_visualize_data(self):
        """
        Description : Left click on Visualize Data in banner area
        """
        visualize_data_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.visualize_data, "Visualize Data")
        self._core_utils.left_click(visualize_data_obj)
    
    def sign_out(self):
        """
        Description : Left click on User icon and select sign out menu
        """
        self.click_user()
        ContextMenu(self.driver).select("Sign Out")
        self._utils.synchronize_until_element_is_visible("#SignonUserName", 30, 2)
    
    def verify_top_bar_menus_title(self, expected_title, step_num, assert_type='asequal'):
        """
        Description : Verify the visible top bar menus title
        :Usage - verify_top_bar_menus_title(['Home', 'My Workspace', 'Shared with Me', 'Workspaces', 'Utilities', 'Settings', 'Help', 'User'], "05.04")
        """
        tab_bar_menus = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.top_bar_menus, "Home page top bar menus")
        actual_title = [menu.get_attribute('title') for menu in tab_bar_menus if menu.is_displayed()]
        msg = "Step {0} : Verify home page top bar menus title".format(step_num)
        self._utils.verify_list_values(expected_title, actual_title, msg, assert_type)
    
    def close_page_message(self):
        """
        Description : Close the page message dialog at top of the banner if exits
        """
        close_btn = self.driver.find_elements_by_css_selector("div[data-ibx-type='pagemessages'] .post-message-close-button:not([style*='none'])>.ibx-label-icon")
        if close_btn != []:
            close_btn[0].is_displayed() and self._core_utils.left_click(close_btn[0])
            
    @property
    def ToolListMenu(self): return self._tool_list_menu_(self.driver)
    
    @property
    def Search(self): return self._search_(self.driver)
        
    class _tool_list_menu_(__Common__):
        
        def __init__(self, driver):
        
            super(Banner._tool_list_menu_, self).__init__(driver)
            self.locators = paris_home_page_locators.Banner.ToolListMenu
        
        def select_tool(self, tool_name):
            """
            Description : Left click on tool menu to select
            :Usage = select_tool("Create New Visualization")
            """
            tools_obj = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.tools, "Tool List Menu")
            tool_index = [index for index, tool in enumerate(tools_obj) if tool.text.strip().startswith(tool_name)]
            if len(tool_index) >0 :
                tool_obj = tools_obj[tool_index[0]]
                self._core_utils.left_click(tool_obj)
            else:
                msg = "[{0}] tool does not exists in Tool List Menu".format(tool_name)
                raise LookupError(msg)
        
        def close(self):
            """
            Description : Left click on close icon to close the Tool List Menu popup.
            """
            close_icon = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.close_icon, "Tool List Menu close icon")
            self._core_utils.left_click(close_icon)
    
    class _search_(__Common__):
        
        def __init__(self, driver):
            
            super().__init__(driver)
        
        @property
        def SearchBox(self):
            textbox_object = self._utils.validate_and_get_webdriver_object_using_locator(paris_home_page_locators.Banner.search_textbox, "Search TextBox")
            return html_controls.TextBox(textbox_object, "Search Textbox")
        
        @property
        def SearchButton(self):
            button_object = self._utils.validate_and_get_webdriver_object_using_locator(paris_home_page_locators.Banner.search_icon, "Search Button")
            return html_controls.Button(button_object, "Search Button")
        
        @property
        def ClearButton(self):
            button_object = self._utils.validate_and_get_webdriver_object_using_locator(paris_home_page_locators.Banner.search_clear_btn, "Search Clear Button")
            return html_controls.Button(button_object, "Search Clear Button")
        
        @property
        def Results(self): return Banner._search_._results_(self.driver)
            
        class _results_(__Common__):
            
            def __init__(self, driver):
            
                super().__init__(driver)
            
            def select(self, result_name):
                """
                Description : Select the searched result option by left click
                :Usage - select("Explore Sales Data")
                """
                resuts_object = self._utils.validate_and_get_webdriver_objects_using_locator(paris_home_page_locators.Banner.search_results_name, "Search results")
                error_msg = "[{0}] option not found in searched results".format(result_name)
                result_object = self._core_utils.get_element_object_by_text(resuts_object, result_name, error_msg=error_msg, scroll_into_view=False)
                self._core_utils.left_click(result_object)
                
            def verify(self, expected_results, step_num, assert_type='asin', include_tag=False):
                
                locator = paris_home_page_locators.Banner.search_results if include_tag else paris_home_page_locators.Banner.search_results_name
                result_objects = self.driver.find_elements(*locator)
                msg = "Step {0} : Verify search results".format(step_num)
                actual_results = [result.text.strip().replace("\n", " ") for result in result_objects if result.is_displayed()]
                self._utils.verify_list_values(expected_results, actual_results, msg, assert_type)
            
            def wait_for_visible(self):
                
                self._utils.synchronize_until_element_is_visible(paris_home_page_locators.Banner.search_parent_css + "div[role='listbox']", 30)
                
class MyWorkspace(__Common__):
    
    def __init__(self, driver):
        
        super(MyWorkspace, self).__init__(driver)
        self.locators = paris_home_page_locators.MyWorkspace
        self._section_ = "My Workspace"
    
    def verify_grid_view_displayed(self, step_num):
        """
        Description : Verify whether grid view is active in content area
        :Usage - verify_grid_view_displayed("02.01")
        """
        msg = "Step {0} : Verify Grid view is displayed in {1}".format(step_num, self._section_)
        self._utils.asequal(True, self._is_grid_view_displayed_(), msg)
        
    def verify_list_view_displayed(self, step_num):
        """
        Description : Verify whether list view is active in content area
        :Usage - verify_list_view_displayed("02.01")
        """
        msg = "Step {0} : Verify List view is displayed in {1}".format(step_num, self._section_)
        self._utils.asequal(True, self._is_list_view_displayed_(), msg)
    
    def select_item(self, name, index=1):
        """
        Description : Left click on item to select
        :Usage - select_item("C123456")
        """
        item_object = self._get_item_object_(name, index)
        self._core_utils.left_click(item_object)
        self._utils.wait_for_page_loads(5, pause_time=0.5)
    
    def right_click_on_item(self, name, index=1):
        """
        Description : Right click on item
        :Usage - right_click_on_item("C123456")
        """
        item_object = self._get_item_object_(name, index)
        self._core_utils.right_click(item_object)
        self._utils.wait_for_page_loads(5, pause_time=0.5)
    
    def double_click_on_item(self, name, index=1):
        """
        Description : Double click on file
        :Usage - double_click_on_item("C123456")
        """
        item_object = self._get_item_object_(name, index)
        self._core_utils.double_click(item_object)
        self._utils.wait_for_page_loads(5, pause_time=0.5)
    
    def verify_items(self, expected_items, step_num, assert_type='asin'):
        """
        Description : Verify the visible or invisible files
        :Usage : verify_items(["G130043"], "01.02")
        """
        item_locators, view = (self.locators.grid_view_items, "Grid") if self._is_grid_view_displayed_() else (self.locators.list_view_items, "List")
        item_objects = self.driver.find_elements(*item_locators)
        actual_items = [item.text.strip() for item in item_objects if item.is_displayed()]
        msg = "Step {0} : Verify items in {1} {2} view".format(step_num, self._section_, view)
        self._utils.verify_list_values(expected_items, actual_items, msg, assert_type)
        
    def _is_grid_view_displayed_(self):
        """
        Description : Return True if grid view is displayed in content area
        """
        grid_view = self.driver.find_elements(*self.locators.grid_view)
        status = True if grid_view != []  else False
        return status
    
    def _is_list_view_displayed_(self):
        """
        Description : Return True if list view is displayed in content area
        """
        list_view = self.driver.find_elements(*self.locators.list_view)
        status = True if list_view != []  else False
        return status
    
    def _get_item_object_(self, item_name, index = 1):
        """
        Description : Return the item object. If grid view is active then file object return from grid view else return from list view.
        """
        item_locators, view = (self.locators.grid_view_items, "Grid") if self._is_grid_view_displayed_() else (self.locators.list_view_items, "List")
        item_objects = self._utils.validate_and_get_webdriver_objects_using_locator(item_locators, self._section_ + " " + view  + " View items")
        error_msg = "[{0}] item does not exist in {1} {2} view".format(item_name, self._section_, view)
        item_object = self._core_utils.get_element_object_by_text_using_javascript(item_objects, item_name, error_msg, index)
        return  item_object

class __homerecents__(__Common__):
        
        def __init__(self, driver):
        
            super(__homerecents__, self).__init__(driver)
            self.__section__ = "Recent"
            self.__locators__ = paris_home_page_locators.Home
            self.__rootcss__ = self.__locators__.recent_section_css
        
        def select_item(self, name, index=1):
            """
            Description : Left click on item to select
            :Usage - select_item("C123456")
            """
            item_object = self._get_item_object_(name, index)
            self._core_utils.left_click(item_object)
            self._utils.wait_for_page_loads(5, pause_time=0.5)
    
        def right_click_on_item(self, name, index=1):
            """
            Description : Right click on item
            :Usage - right_click_on_item("C123456")
            """
            item_object = self._get_item_object_(name, index)
            self._core_utils.right_click(item_object)
            self._utils.wait_for_page_loads(5, pause_time=0.5)
        
        def double_click_on_item(self, name, index=1):
            """
            Description : Double click on file
            :Usage - double_click_on_item("C123456")
            """
            item_object = self._get_item_object_(name, index)
            self._core_utils.double_click(item_object)
            self._utils.wait_for_page_loads(5, pause_time=0.5)
        
        def click_view_all(self):
            """
            Description : Left click on View All link to view all items
            """
            view_all_css = self.__locators__.view_all_css.format(self.__rootcss__)
            view_all_objects = self._utils.validate_and_get_webdriver_object(view_all_css, self.__section__ + " section View All")
            self._javascript.scrollIntoView(view_all_objects)
            self._core_utils.left_click(view_all_objects)
            self._utils.wait_for_page_loads(10, pause_time=0.5)
            self._utils.synchronize_until_element_is_visible(self.__locators__.grid_view_button[1], 40)
            
        def verify_items(self, expected_items, step_num, assert_type='asin'):
            """
            Description : Verify the visible or invisible files
            :Usage : verify_items(["G130043"], "01.02")
            """
            section = self.driver.find_element_by_css_selector(self.__locators__.favorites_section_css)
            self._javascript.scrollIntoView(section)
            items_css = self.__locators__.section_items_css.format(self.__rootcss__)
            item_objects = self.driver.find_elements_by_css_selector(items_css)
            actual_items = [item.text.strip() for item in item_objects if item.is_displayed()]
            msg = "Step {0} : Verify items in Home {1} section".format(step_num, self.__section__)
            self._utils.verify_list_values(expected_items, actual_items, msg, assert_type)
            
        def _get_item_object_(self, item_name, index=1):
            """
            Description : Return the section item object
            """
            items_css = self.__locators__.section_items_css.format(self.__rootcss__)
            item_objects = self._utils.validate_and_get_webdriver_objects(items_css, self.__section__ + " section items")
            error_msg = "[{0}] item does not exist in Home {1} section".format(item_name, self.__section__)
            item_object = self._core_utils.get_element_object_by_text_using_javascript(item_objects, item_name, error_msg, index, scroll_into_view=False)
            item_scroll_object = self._utils.validate_and_get_webdriver_object(self.__locators__.section_item_scroll_css.format(self.__rootcss__), self.__section__ + " section scroll items")
            self._javascript.scrollIntoView(item_object)
            self._javascript.scrollLeft(item_scroll_object, item_object)
            return  item_object
        
class Home(__Common__):
    
    def __init__(self, driver):
        
        super(Home, self).__init__(driver)
    
    def verify_sections(self, expected_sections, step_num, assert_type='asequal'):
        """
        Description : Verify the Home tab sections names
        :Usage = verify_sections(['GETTING STARTED', 'RECENTS', 'FAVORITES', 'PORTALS'], "05.01")
        """
        section_objects = self.driver.find_elements_by_css_selector(".home-display-content .home-content-displayer-label")
        actual_sections = self._javascript.get_elements_text(section_objects)
        msg = "Step {0} : Verify the Home tab sections".format(step_num)
        self._utils.verify_list_values(expected_sections, actual_sections, msg, assert_type)
        
    @property
    def Recents(self):
        """ Return the __recents__ class object"""
        return __homerecents__(self.driver)
    
    @property
    def Favorites(self):
        """ Return the __favorites__ class object"""
        return self.__favorites__(self.driver)
    
    @property
    def Portals(self):
        """ Return the __portals__ class object"""
        return self.__portals__(self.driver)
    
    @property
    def GettingStarted(self):
        """ Return the _getting_started_ class object"""
        return self._getting_started_(self.driver)
    
    @property
    def ViewAll(self):
        """ Return the __portals__ class object"""
        return self.__viewall__(self.driver)
    
    class __viewall__(MyWorkspace):
        
        def __init__(self, driver):
            
            super(Home.__viewall__, self).__init__(driver)
            self.locators = paris_home_page_locators.Home
            self._section_ = "Home" 
            
        def click_left_arrow(self):
            """
            Description : Left click on Left Arrow button to go back to home view from view all page
            """
            left_arrow_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.left_arrow, "Left Arrow button")
            self._core_utils.left_click(left_arrow_obj)
            self._utils.wait_for_page_loads(30)
            self._utils.synchronize_with_visble_text(self.locators.favorites_section_css, 'FAVORITES', 15)
                    
    class __favorites__(__homerecents__):
        
        def __init__(self, driver):
            
            super(Home.__favorites__, self).__init__(driver)
            self.__rootcss__ = self.__locators__.favorites_section_css
            self.__section__ = "Favorites"
           
    class __portals__(__homerecents__):
        
        def __init__(self, driver):
            
            super(Home.__portals__, self).__init__(driver)
            self.__section__ = "Portals"
            self.__rootcss__ = self.__locators__.portals_section_css
            
    class _getting_started_(__homerecents__):
        
        def __init__(self, driver):
            
            super(Home._getting_started_, self).__init__(driver)
            self.__section__ = "Getting Started"
            self.__rootcss__ = self.__locators__.getting_section_css
            
class SharedWithMe(MyWorkspace):
    
    def __init__(self, driver):
        
        super(SharedWithMe, self).__init__(driver)
        self.locators = paris_home_page_locators.Home
        self._section_ = "Shared With Me"

class Workspaces(__Common__):
    
    def __init__(self, driver):
        
        super(Workspaces, self).__init__(driver)
        self.locators = paris_home_page_locators.Workspaces
        
    @property
    def NavigationBar(self):
        """ Return the __NavigationBar__ class object"""
        return Workspaces.__NavigationBar__(self.driver)

    @property
    def ResourcesTree(self):
        """ Return the __ResourcesTree__ class object"""
        return Workspaces.__ResourcesTree__(self.driver)
    
    @property
    def ActionBar(self):
        """ Return the __ActionBar__ class object"""
        return Workspaces.__ActionBar__(self.driver)
    
    @property
    def ContentArea(self):
        """ Return the __ContentArea__ class object"""
        return Workspaces.__ContentArea__(self.driver)
    
    def switch_to_frame(self):
        """
        Description : Switch to iframe to work on old home page workspaces 
        """
        self._core_utils.switch_to_frame(self.locators.iframe_css)
        self._utils.synchronize_until_element_is_visible(self.NavigationBar.locators.navigation_bar_css, 80)
        self._utils.wait_for_page_loads(40, pause_time=2)
        
    def switch_to_default_content(self):
        """
        Description : Switch to default content
        """
        self._core_utils.switch_to_default_content()
        
    class __NavigationBar__(__Common__):
        
        def __init__(self, driver):
            
            super(Workspaces.__NavigationBar__, self).__init__(driver)
            self.locators = paris_home_page_locators.Workspaces.NavigationBar
        
        def select_workspaces(self):
            """
            Description : Left click on Workspaces in breadcrumb
            """
            self.select_breadcrumb("Workspaces")
        
        def select_breadcrumb(self, name):
            """
            Description : Left click on given breadcrumb option
            :Usage - select_breadcrumb("My Content") 
            """
            breadcrumb_object =  self._utils.validate_and_get_webdriver_object(self.locators.breadcrumb_css.format(name), "Workspaces breadcrumb")
            self._core_utils.left_click(breadcrumb_object)
            self._utils.wait_for_page_loads(80, pause_time=1)
            self._utils.synchronize_until_element_is_visible(paris_home_page_locators.Workspaces.page_load_completed_css, 120)
            
        def click_breadcrumb_arrow(self, name):
            """
            Description : Left click on given breadcrumb arrow icon
            :Usage - select_breadcrumb("My Content") 
            """
            arrow_object =  self._utils.validate_and_get_webdriver_object(self.locators.breadcrumb_arrow_css.format(name), "Workspaces breadcrumb arrow")
            self._core_utils.left_click(arrow_object)
            self._utils.synchronize_until_element_is_visible(paris_home_page_locators.Banner.popup_css, 20)
        
        def verify_breadcrumbs(self, expected_breadcrumbs, step_num):
            """
            Description : Verify the breadcrumbs text
            :Usage - verify_breadcrumbs("Workspaces>P292_S28313>G671781", "02.01")
            """
            actual_breadcrumbs = ""
            breadcrumbs_object = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.breadcrumbs, "Workspaces breadcrumbs")
            for breadcrumb in breadcrumbs_object :
                breadcrumb_text = breadcrumb.text.strip()
                actual_breadcrumbs += breadcrumb_text
                breadcrumb_arrow_obj = self.driver.find_elements_by_css_selector(self.locators.breadcrumb_arrow_css.format(breadcrumb_text))
                if breadcrumb_arrow_obj != []:
                    arrow_text = self._javascript.get_element_before_style_properties(breadcrumb_arrow_obj[0], "content").replace('"\uf054"', ">")
                    actual_breadcrumbs += arrow_text
            msg = "Step {0} : Verify [{1}] breadcrumbs displayed in workspaces navigation bar".format(step_num, expected_breadcrumbs)
            self._utils.asequal(expected_breadcrumbs, actual_breadcrumbs, msg)
            
    class __ResourcesTree__(__Common__):
        
        def __init__(self, driver):
            super(Workspaces.__ResourcesTree__, self).__init__(driver)
            self.locators = paris_home_page_locators.Workspaces.ResourcesTree
        
        def select_workspaces(self):
            """
            Description : Left click on Workspaces 
            """
            self.select("Workspaces")
            
        def expand_workspaces(self):
            """
            Description : Select the tree by left click
            :Usage1 - expand("P292->S12345->G123456")
            """
            self.expand("Workspaces")
            
        def expand(self, tree_path):
            """
            Description : Expand the tree by clicking expand icon
            :Usage - expand("P292->S12345")
            """
            self._expand_tree_(tree_path.split("->"))
            self._utils.wait_for_page_loads(15, pause_time=1)
        
        def collapse(self, tree_path, collapse_parent=True):
            """
            Description : Collapse the tree by clicking collapse icon
            arg : collapse_parent = if True then collapse parent node otherwise collapse child nodes except parent
            :Usage - collapse("S12345->P292")
            """
            child_note_xpath = "/following-sibling::div//div[normalize-space()='{}']"
            tree_path = tree_path.split("->")[::-1]
            parent_node_xpath = "//div[@class='ibfs-tree']//div[normalize-space()='{}']".format(tree_path[0])
            for index in range(len(tree_path), 0, -1):
                if not collapse_parent and index == 1:
                    break
                target_node_xpath = child_note_xpath*(index-1)
                target_node_xpath = parent_node_xpath + target_node_xpath.format(*tree_path[1:index])
                nodes = self.driver.find_elements_by_xpath(target_node_xpath)
                if nodes != []:
                    self._javascript.scrollIntoView(nodes[0], wait_time=1)
                    collapse_icon = nodes[0].find_elements(*self.locators.collapse_icon)
                    (collapse_icon != []) and self._core_utils.left_click(collapse_icon[0])
                    self._utils.wait_for_page_loads(15, pause_time=1)
                else:
                    msg = "[{0}] folder not exists in home page workspace resources tree".format("->".join(tree_path[:index]))
                    raise KeyError(msg)
            
        def collapse_workspaces(self):
            """
            Description : Collapse the Workspaces by clicking collapse icon
            :Usage - collapse_workspaces()
            """
            self.collapse("Workspaces")
            
        def select(self, tree_path):
            """
            Description : Select the tree by left click
            :Usage1 - expand("P292->S12345->G123456")
            """
            tree_object = self._get_tree_object_(tree_path)
            self._core_utils.left_click(tree_object)
            self._utils.wait_for_page_loads(15, pause_time=2)
            self._utils.synchronize_until_element_is_visible(paris_home_page_locators.Workspaces.page_load_completed_css, 120)
        
        def double_click(self, tree_path):
            """
            Description : Select the tree by left click
            :Usage1 - expand("P292->S12345->G123456")
            """
            tree_object = self._get_tree_object_(tree_path)
            self._core_utils.double_click(tree_object)
            self._utils.wait_for_page_loads(15, pause_time=2)
            self._utils.synchronize_until_element_is_visible(paris_home_page_locators.Workspaces.page_load_completed_css, 120)
        
        def right_click(self, tree_path):
            """
            Description : Select the tree by left click
            :Usage1 - expand("P292->S12345->G123456")
            """
            tree_object = self._get_tree_object_(tree_path)
            self._core_utils.right_click(tree_object)
            self._utils.synchronize_until_element_is_visible(paris_home_page_locators.Banner.popup_css, 60)
        
        def verify_items(self, expected_items, step_num, assert_type='asin', parent_folder=None):
            """
            Description : Verify the visible or invisible resource items text in workspaces view
            :arg : parent_folder = If you wants to verify items under the specific folder then pass parent_folder. Exp: parent_folder="P292->S123456"
            :Usage : verify_items(["Workspaces", "1TestV3", "P292_S10660"], "01.02")
            """
            if parent_folder:
                parent_object = self._get_tree_object_(parent_folder)
                item_css = "#{} + div.ibfs-children .ibfs-label".format(parent_object.get_attribute("id"))
                items_object = self.driver.find_elements_by_css_selector(item_css)
            else:
                items_object = self.driver.find_elements(*self.locators.items)
            actual_items = [item.text.strip() for item in items_object if item.is_displayed()]
            msg = "Step {0} : Verify items in workspaces resources tree".format(step_num)
            self._utils.verify_list_values(expected_items, actual_items, msg, assert_type)
        
        def verify_unpublished_items(self, expected_items, step_num, assert_type='asin', parent_folder=None):
            """
            Description : Verify the visible or invisible resource items text in workspaces view
            :arg : parent_folder = If you wants to verify items under the specific folder then pass parent_folder. Exp: parent_folder="P292->S123456"
            :Usage : verify_unpublished_items(["Workspaces", "1TestV3", "P292_S10660"], "01.02")
            """
            if parent_folder:
                parent_object = self._get_tree_object_(parent_folder)
                item_css = "#{} + div.ibfs-children .ibfs-label".format(parent_object.get_attribute("id"))
                items_object = self.driver.find_elements_by_css_selector(item_css)
            else:
                items_object = self.driver.find_elements(*self.locators.items)
            actual_items = [item.text.strip() for item in items_object if item.is_displayed() and item.value_of_css_property('font-style') == 'italic']
            msg = "Step {0} : Verify unpublished items in workspaces resources tree".format(step_num)
            self._utils.verify_list_values(expected_items, actual_items, msg, assert_type)
            
        def verify_selected_item(self, expected_item, step_num):
            """
            Description : Verify the selected resource items text in workspaces view
            :Usage : verify_selected_item(["P292_S10660"], "01.02")
            """
            items_object = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.selected_item, "Workspaces resources selected tree")
            actual_items = [item.text.strip() for item in items_object if item.is_displayed()]
            msg = "Step {0} : Verify {1} item selected in workspaces resources tree".format(step_num, expected_item)
            self._utils.verify_list_values(expected_item, actual_items, msg)
        
        def verify_expanded(self, tree_path, step_num):
            """
            Description : Verify whether resource tree item is expanded or Not
            :Usage : verify_expanded("P292", "01.02")
            """
            tree_object = self._get_tree_object_(tree_path)
            expanded_icon = tree_object.find_elements(*self.locators.collapse_icon)
            if len(expanded_icon) > 0 :
                expected_value = '"\ue993"'
                expanded_icon_value = self._javascript.get_element_before_style_properties(expanded_icon[0], 'content')
                state = True if expected_value == expanded_icon_value else False
            else :
                state = False
            msg = "Step {0} : Verify [{1}] item expanded in workspaces resources tree".format(step_num, tree_path)
            self._utils.asequal(True, state, msg)
            
        def verify_collapsed(self, tree_path, step_num):
            """
            Description : Verify whether resource tree item is collapsed or Not
            :Usage : verify_collapsed("P292", "01.02")
            """
            tree_object = self._get_tree_object_(tree_path)
            collapsed_icon = tree_object.find_elements(*self.locators.expand_icon)
            if len(collapsed_icon) > 0 :
                expected_value = '"\ue98c"'
                expanded_icon_value = self._javascript.get_element_before_style_properties(collapsed_icon[0], 'content')
                state = True if expected_value == expanded_icon_value else False
            else :
                state = False
            msg = "Step {0} : Verify [{1}] item collapsed in workspaces resources tree".format(step_num, tree_path)
            self._utils.asequal(True, state, msg)
            
        def _expand_tree_(self, tree_path_list):
            """
            Description : Expand tree path and return the last tree path xpath value.
            :Usage : _expand_tree_("P292->S1300")
            """
            tree_xpath = "//div[@class='ibfs-tree']//div[normalize-space()='{0}']"
            for tree in tree_path_list:
                tree_xpath = tree_xpath.format(tree)
                tree_objects = self.driver.find_elements_by_xpath(tree_xpath)
                if tree_objects != [] :
                    tree_object = tree_objects[0]
                    self._javascript.scrollIntoView(tree_object, wait_time=1)
                    expand_icon_objs = tree_object.find_elements(*self.locators.expand_icon)
                    if expand_icon_objs != [] :
                        expand_icon_obj = expand_icon_objs[0]
                        self._core_utils.left_click(expand_icon_obj)
                        self._utils.wait_for_page_loads(15, pause_time=0.5)
                        self._utils.synchronize_until_element_is_visible(paris_home_page_locators.Workspaces.page_load_completed_css, 120)
                else :
                    msg = "[{0}] does not exists in paris home page resource tree".format(tree)
                    raise LookupError(msg)
                tree_xpath = tree_xpath + "/following-sibling::div//div[normalize-space()='{0}']"
            return tree_xpath
        
        def _get_tree_object_(self, tree_path):
            """
            Description : Return the tree object
            :Usage - _get_tree_object_("P292->S123456")
            """
            tree_path = tree_path.split("->")
            (tree_path[0] != 'Global Resources') and self.expand_workspaces()
            target_tree = tree_path[-1]
            tree_path = tree_path[:-1]
            tree_xpath = self._expand_tree_(tree_path)
            tree_objects = self.driver.find_elements_by_xpath(tree_xpath.format(target_tree))
            if tree_objects == [] :
                msg = "[{0}] does not exists in paris home page resource tree".format(target_tree)
                raise LookupError(msg)
            tree_object = tree_objects[0]
            self._javascript.scrollIntoView(tree_object, wait_time=1)
            return tree_object

    class __ActionBar__(__Common__):
        
        def __init__(self, driver):
            super(Workspaces.__ActionBar__, self).__init__(driver)
            self.locators = paris_home_page_locators.Workspaces.ActionBar
        
        def select_tab(self, tab_name):
            """
            Description : Left click on Tab button
            @Usage : select_tab("DATA")
            """
            tab_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.tabs, "Action bar tab")
            tab_name_list = [tab.text.strip() for tab in tab_objects]
            tab_index = tab_name_list.index(tab_name) if tab_name_list.count(tab_name) else None
            if tab_index is None :
                raise LookupError("[{0}] tab not displayed in action bar".format(tab_name))
            self._core_utils.left_click(tab_objects[tab_index])
            self._utils.wait_for_page_loads(5, pause_time=1.5)
            
        def select_tab_option(self, option_name):
            """
            Description : Left click on Tab button and left click on option
            @Usage : select_tab_option("Reporting Object")
            """
            option_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.tab_options, "Action bar tab options")
            option_index = self._javascript.find_element_index_by_text(option_objects, option_name)
            if option_index is None :
                raise LookupError("[{0}] tab not displayed in action bar".format(option_name))
            self._core_utils.left_click(option_objects[option_index])
        
        def verify_tabs(self, expected_tab, step_num, assert_type='asequal'):
            """
            Description : Verify the tabs
            @Usage : verify_tabs(["DATA", "APPLICATION", "INFOASSIST", "SCHEDULE", "OTHER"], "01.02")
            """
            tab_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.tabs, "Action bar tab")
            actual_tabs = [tab.text.strip() for tab in tab_objects if tab.is_displayed()]
            msg = "Step {0} : Verify action bar tabs.".format(step_num)
            self._utils.verify_list_values(expected_tab, actual_tabs, msg, assert_type)
        
        def verify_tab_options(self, expected_tab_options, step_num, assert_type='asequal'):
            """
            Description : Verify the tabs
            @Usage : verify_tabs(["Chart", "Visualization", "Report", "Document", "Sample Content", "Alert"], "01.02")
            """
            tab_option_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.tab_options, "Action bar tab options")
            actual_tab_options = [tab_option.text.strip() for tab_option in tab_option_objects if tab_option.is_displayed()]
            msg = "Step {0} : Verify action bar tab options.".format(step_num)
            self._utils.verify_list_values(expected_tab_options, actual_tab_options, msg, assert_type)
        
        def verify_selected_tab(self, expected_tab, step_num):
            """
            Description : Verify the selected tab
            @Usage : verify_selected_tab(["DATA"], "01.02")
            """
            selected_tab_objects = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.selected_tab, "Selected action bar tab")
            actual_tabs = [tab.text.strip() for tab in selected_tab_objects if tab.is_displayed()]
            msg = "Step {0} : Verify {1} tab selected in action bar".format(step_num, expected_tab)
            self._utils.asequal(expected_tab, actual_tabs, msg)
        
        def expand(self):
            """
            Description : Left click on Expand arrow to expand action bar
            """
            expand_obj  = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.expand, "Action bar expand arrow")
            expand_obj.is_displayed() and self._core_utils.left_click(expand_obj)
            
        def collapse(self):
            """
            Description : Left click on Collapse arrow to collapse action bar
            """
            collapse_obj  = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.collapse, "Action bar expand arrow")
            collapse_obj.is_displayed() and self._core_utils.left_click(collapse_obj)
        
        def verify_title(self, step_num):
            """
            Description : Verify the action bar title
            :Usage - verify_title("02.01")
            """
            actual_title  = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.title, "Action bar expand arrow").text.strip()
            msg = "Step {0} : Verify 'Action Bar' displayed in action bar title".format(step_num)
            self._utils.asequal("Action Bar", actual_title, msg)
        
        def verify_expanded(self, step_num):
            """
            Description : Verify whether action bar is expanded
            :Usage - verify_expanded("02.01")
            """
            action_bar_childers = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.childrens, "Action bar child elements")
            visible_status = [child.is_displayed() for child in action_bar_childers]
            actual_status = any(visible_status)
            msg = "Step {0} : Verify action bar is expanded".format(step_num)
            self._utils.asequal(True, actual_status, msg)
            
        def verify_collapsed(self, step_num):
            """
            Description : Verify whether action bar is collapsed
            :Usage - verify_collapsed("02.01")
            """
            action_bar_childers = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.childrens, "Action bar child elements")
            visible_status = [child.is_displayed() for child in action_bar_childers]
            actual_status = any(visible_status)
            msg = "Step {0} : Verify action bar is collapsed".format(step_num)
            self._utils.asequal(False, actual_status, msg)
            
        def verify_displayed(self, step_num):
            """
            Description : Verify whether action bar is displayed
            :Usage - verify_displayed("02.01")
            """
            actual_status = self._utils.validate_and_get_webdriver_object(self.locators.action_bar_css, "Action bar expand arrow").is_displayed()
            msg = "Step {0} : Verify action bar is displayed".format(step_num)
            self._utils.asequal(True, actual_status, msg)
        
        def verify_not_displayed(self, step_num):
            """
            Description : Verify whether action bar is not displayed
            :Usage - verify_not_displayed("02.01")
            """
            actual_status = self._utils.validate_and_get_webdriver_object(self.locators.action_bar_css, "Action bar expand arrow").is_displayed()
            msg = "Step {0} : Verify action bar is not displayed".format(step_num)
            self._utils.asequal(False, actual_status, msg)
            
    class __ContentArea__(__Common__):
        
        def __init__(self, driver):
            super(Workspaces.__ContentArea__, self).__init__(driver)
            self.locators = paris_home_page_locators.Workspaces.ContentArea
        
        def verify_grid_view_displayed(self, step_num):
            """
            Description : Verify whether grid view is active in content area
            :Usage - verify_grid_view_displayed("02.01")
            """
            msg = "Step {0} : Verify Grid view is displayed in workspaces content area".format(step_num)
            self._utils.asequal(True, self._is_grid_view_displayed_(), msg)
        
        def verify_list_view_displayed(self, step_num):
            """
            Description : Verify whether list view is active in content area
            :Usage - verify_list_view_displayed("02.01")
            """
            msg = "Step {0} : Verify List view is displayed in workspaces content area".format(step_num)
            self._utils.asequal(True, self._is_list_view_displayed_(), msg)
        
        def select_file(self, file_name, file_type=None):
            """
            Description : Left click on file to select
            :Usage - select_file("C123456")
            """
            file_object = self._get_file_object_(file_name, file_type)
            self._core_utils.left_click(file_object)
            self._utils.wait_for_page_loads(5, pause_time=0.5)
        
        def select_multiple_file(self, file_name_list):
            """
            Description : Select the multiple file using ctrl
            :Usage - select_multiple_file(["C123456", "C123455", "Chart"])
            """
            keyboard.press('ctrl')
            for file in file_name_list:
                file_object = self._get_file_object_(file)
                self._core_utils.python_left_click(file_object)
                self._utils.wait_for_page_loads(5, pause_time=0.5)
            keyboard.release('ctrl')
            
        def right_click_on_file(self, file_name, file_type=None):
            """
            Description : Right click on file
            :Usage - right_click_on_file("C123456")
            """
            file_object = self._get_file_object_(file_name, file_type)
            self._core_utils.right_click(file_object)
            self._utils.wait_for_page_loads(5, pause_time=0.5)
        
        def double_click_on_file(self, file_name, file_type=None):
            """
            Description : Double click on file
            :Usage - double_click_on_file("C123456")
            """
            file_object = self._get_file_object_(file_name, file_type)
            self._core_utils.double_click(file_object)
            self._utils.wait_for_page_loads(5, pause_time=0.5)
        
        def select_folder(self, folder_name):
            """
            Description : Left click on file to folder
            :Usage - select_folder("G123456")
            """
            folder_object = self._get_folder_object_(folder_name)
            self._core_utils.left_click(folder_object)
            self._utils.wait_for_page_loads(5, pause_time=0.5)
        
        def right_click_on_folder(self, folder_name):
            """
            Description : Right click on folder
            :Usage - right_click_on_folder("G123456")
            """
            folder_object = self._get_folder_object_(folder_name)
            self._core_utils.right_click(folder_object)
            self._utils.wait_for_page_loads(5, pause_time=0.5)
        
        def double_click_on_folder(self, folder_name):
            """
            Description : Double click on folder
            :Usage - double_click_on_folder("C123456")
            """
            folder_object = self._get_folder_object_(folder_name)
            self._core_utils.double_click(folder_object)
            self._utils.wait_for_page_loads(5, pause_time=0.5)
        
        def verify_folders(self, expected_folder, step_num, assert_type='asin'):
            """
            Description : Verify the visible or invisible folders
            :Usage : verify_folders(["G130043"], "01.02")
            """
            folders_locator = self.locators.grid_view_folders if self._is_grid_view_displayed_() else self.locators.list_view_folders
            folders_object = self.driver.find_elements(*folders_locator)
            actual_folders = [folder.text.strip() for folder in folders_object if folder.is_displayed()]
            msg = "Step {0} : Verify folders in workspaces content view".format(step_num)
            self._utils.verify_list_values(expected_folder, actual_folders, msg, assert_type)
        
        def verify_shared_folders(self, expected_folder, step_num, assert_type='asin'):
            """
            Description : Verify the shared folders by checking shared and user icon
            :Usage : verify_shared_folders(["G130043"], "01.02")
            """
            folders_locator = self.locators.grid_view_folders if self._is_grid_view_displayed_() else self.locators.list_view_folders
            folders_object = self.driver.find_elements(*folders_locator)
            actual_folders = []
            for folder in folders_object:
                shared_icon = folder.find_elements(*self.locators.shared_item_icon)
                shared_user_icon = folder.find_elements(*self.locators.shared_user_icon)
                if all([len(shared_icon)>0, len(shared_user_icon)>0]):
                    shared_icon_value = self._javascript.get_element_before_style_properties(shared_icon[0], 'content')
                    shared_user_value = self._javascript.get_element_before_style_properties(shared_user_icon[0], 'content')
                    status = all([shared_user_value=='"\uf007"', shared_icon_value=='"\uf1e0"', shared_icon[0].is_displayed(), shared_user_icon[0].is_displayed()])
                    if status:
                        actual_folders.append(folder.text.strip())
            msg = "Step {0} : Verify {1} folders shared".format(step_num, expected_folder)
            self._utils.verify_list_values(expected_folder, actual_folders, msg, assert_type)
        
        def verify_shared_files(self, expected_file, step_num, assert_type='asin'):
            """
            Description : Verify the shared files by checking shared and user icon
            :Usage : verify_shared_files(["G130043"], "01.02")
            """
            files_locator = self.locators.grid_view_files if self._is_grid_view_displayed_() else self.locators.list_view_files
            files_object = self.driver.find_elements(*files_locator)
            actual_file = []
            for file in files_object:
                shared_icon = file.find_elements(*self.locators.shared_item_icon)
                if len(shared_icon)>0:
                    shared_icon_value = self._javascript.get_element_before_style_properties(shared_icon[0], 'content')
                    status = all([shared_icon_value=='"\uf1e0"', shared_icon[0].is_displayed()])
                    if status:
                        actual_file.append(file.text.strip())
            msg = "Step {0} : Verify {1} file shared".format(step_num, expected_file)
            self._utils.verify_list_values(expected_file, actual_file, msg, assert_type)
        
        def verify_shortcut_folders(self, expected_folder, step_num, assert_type='asin'):
            """
            Description : Verify the shortcut folders by checking shortcut icon
            :Usage : verify_shortcut_folders(["G130043"], "01.02")
            """
            folders_locator = self.locators.grid_view_folders if self._is_grid_view_displayed_() else self.locators.list_view_folders
            folders_object = self.driver.find_elements(*folders_locator)
            actual_folders = []
            for folder in folders_object:
                shortcut_icon = folder.find_elements(*self.locators.shortcut_icon)
                if len(shortcut_icon) >0 :
                    shortcut_icon_value = self._javascript.get_element_before_style_properties(shortcut_icon[0], 'content')
                    status = all([shortcut_icon_value=='"\ue93b"',shortcut_icon[0].is_displayed()])
                    if status:
                        actual_folders.append(folder.text.strip())
            msg = "Step {0} : Verify shortcut folders".format(step_num)
            self._utils.verify_list_values(expected_folder, actual_folders, msg, assert_type)
        
        def verify_shortcut_files(self, expected_file, step_num, assert_type='asin'):
            """
            Description : Verify the shortcut files by checking shortcut icon
            :Usage : verify_shortcut_files(["Report1"], "01.02")
            """
            files_locator = self.locators.grid_view_files if self._is_grid_view_displayed_() else self.locators.list_view_files
            files_object = self.driver.find_elements(*files_locator)
            actual_file = []
            for file in files_object:
                shortcut_icon = file.find_elements(*self.locators.shortcut_icon)
                if len(shortcut_icon)>0:
                    shortcut_icon_value = self._javascript.get_element_before_style_properties(shortcut_icon[0], 'content')
                    status = all([shortcut_icon_value=='"\ue93b"', shortcut_icon[0].is_displayed()])
                    if status:
                        actual_file.append(file.text.strip())
            msg = "Step {0} : Verify shortcut files".format(step_num, expected_file)
            self._utils.verify_list_values(expected_file, actual_file, msg, assert_type)
            
        def verify_published_folders(self, expected_folder, step_num, assert_type='asin'):
            """
            Description : Verify the published folders
            :Usage : verify_published_folders(["G130043"], "01.02")
            """
            actual_folders = []
            if self._is_grid_view_displayed_():
                grid_folder_css = self.locators.grid_view_folders[1]+str(".folder-item-published")
                folders_object = self.driver.find_elements_by_css_selector(grid_folder_css)
                for folder in folders_object:
                    actual_folders.append(folder.text.strip())
            else:
                folders_object = self.driver.find_elements(*self.locators.list_view_folders)
                for folder in folders_object:
                    folder_icon = folder.find_element(*self.locators.list_view_folder_icon)
                    filter_val = folder_icon.value_of_css_property('filter')
                    if filter_val=='none':
                        actual_folders.append(folder.text.strip())
            msg = "Step {0} : Verify published folders in workspaces content view".format(step_num)
            self._utils.verify_list_values(expected_folder, actual_folders, msg, assert_type)
        
        def verify_unpublished_folders(self, expected_folder, step_num, assert_type='asin'):
            """
            Description : Verify the unpublished folders
            :Usage : verify_unpublished_folders(["G130043"], "01.02")
            """
            actual_folders = []
            if self._is_grid_view_displayed_():
                grid_folder_css=self.locators.grid_view_folders[1]+str(":not(.folder-item-published)")
                folders_object = self.driver.find_elements_by_css_selector(grid_folder_css)
                for folder in folders_object:
                    actual_folders.append(folder.text.strip())
            else:
                folders_object = self.driver.find_elements(*self.locators.list_view_folders)
                for folder in folders_object:
                    folder_icon = folder.find_element(*self.locators.list_view_folder_icon)
                    color = Color.from_string(folder_icon.value_of_css_property('color')).rgb
                    filter_val = folder_icon.value_of_css_property('filter')
                    if all([color=='rgb(124, 124, 124)', filter_val=='grayscale(1)']):
                        actual_folders.append(folder.text.strip())
            msg = "Step {0} : Verify unpublished folders in workspaces content view".format(step_num)
            self._utils.verify_list_values(expected_folder, actual_folders, msg, assert_type)
        
        def verify_folder_border_color(self, folder_name, step_num, expected_color='curious_blue1'):
            """
            Description : Verify the folder border color
            :Usage : verify_folder_border_color("G130043", "01.02")
            """
            folder_obj = self._get_folder_object_(folder_name)
            if self._is_list_view_displayed_():
                parent_xpath = "//div[@id='{0}']/parent::div".format(folder_obj.get_attribute('id'))
                folder_obj = self.driver.find_element_by_xpath(parent_xpath)
            msg = "Step {0} : Verify [{1}] folder border color".format(step_num, folder_name)
            self._utils.verify_element_color_using_css_property(None, expected_color, msg, 'border-top-color', folder_obj)
                
        def verify_files(self, expected_files, step_num, assert_type='asin'):
            """
            Description : Verify the visible or invisible files
            :Usage : verify_files(["C123456"], "01.02")
            """
            file_locator = self.locators.grid_view_files if self._is_grid_view_displayed_() else self.locators.list_view_files
            file_object = self.driver.find_elements(*file_locator)
            actual_files = [file.text.strip() for file in file_object if file.is_displayed()]
            msg = "Step {0} : Verify files in workspaces content view".format(step_num)
            self._utils.verify_list_values(expected_files, actual_files, msg, assert_type)
        
        def verify_file_summary(self, file_name, expected_summary, step_num, file_type=None):
            """
            Description : Verify the file summary
            :Usage : verify_file_summary("C123456", "This is chart file", "01.02")
            """
            file_object = self._get_file_object_(file_name, file_type)
            if self._is_grid_view_displayed_():
                self._core_utils.move_to_element(file_object)
                summary_obj = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.grid_view_summary, "File summary", parent_object=file_object)
                actual_summary = summary_obj.text.strip()
            else:
                actual_summary = self._get_list_view_cell_object_(file_name, 'Summary', file_type=file_type).text.strip()
            msg = "Step {0} : Verify [{1}] summary  displayed for [{2}] file".format(step_num, expected_summary, file_name)
            self._utils.asequal(expected_summary, actual_summary, msg)
            
        def delete_folder(self, folder_name):
            """
            Description : Delete the folder in content area.
            """
            self.right_click_on_folder(folder_name)
            modal = ModalDialogs(self.driver)
            ContextMenu(self.driver).select('Delete')
            modal.Alert.wait_for_appear()
            modal.Alert.OKButton.click()
            modal.Alert.wait_for_diappear()
            self._utils.wait_for_page_loads(30)
            self._utils.synchronize_until_element_is_visible(paris_home_page_locators.Workspaces.page_load_completed_css, 120)
            
        def delete_file(self, file_name):
            """
            Description : Delete the file in content area.
            """
            self.right_click_on_file(file_name)
            modal = ModalDialogs(self.driver)
            ContextMenu(self.driver).select('Delete')
            modal.Alert.wait_for_appear()
            modal.Alert.OKButton.click()
            modal.Alert.wait_for_diappear()
            self._utils.wait_for_page_loads(30)
            self._utils.synchronize_until_element_is_visible(paris_home_page_locators.Workspaces.page_load_completed_css, 120)
            
        def delete_folder_if_exists(self, folder_name):
            """
            Description : Delete the folder if exists in content area.
            """
            try :
                self.delete_folder(folder_name)
            except:
                pass
        
        def delete_file_if_exists(self, file_name):
            """
            Description : Delete the file if exists in content area.
            """
            try :
                self.delete_file(file_name)
            except:
                pass
            
        def _is_grid_view_displayed_(self):
            """
            Description : Return True if grid view is displayed in content area
            """
            grid_view = self.driver.find_elements(*self.locators.grid_view)
            status = True if grid_view != []  else False
            return status
        
        def _is_list_view_displayed_(self):
            """
            Description : Return True if list view is displayed in content area
            """
            list_view = self.driver.find_elements(*self.locators.list_view)
            status = True if list_view != []  else False
            return status
        
        def _get_list_view_cell_object_(self, file_name, column_name, file=True, file_type=None):
            """
            Description : Return the list view cell object based on file name column name
            for example, if you want to get summary cell object of any file then you can call this funtion
            :Usage - _get_list_view_cell_object("C1234567", 'Summary')
            """
            if self._is_list_view_displayed_():
                columns_obj = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.list_view_columns, "List view columns")
                column_index = self._javascript.find_element_index_by_text(columns_obj, column_name)
                if column_index is not None:
                    file_object = self._get_file_object_(file_name, file_type) if file else self._get_folder_object_()
                    row_object = self._javascript.get_parent_element(file_object)
                    cell_object = self._javascript.get_child_elements(row_object)[column_index]
                    return cell_object
                else:
                    msg = "[{0}] column does not displayed in content area list view".format(column_name)
                    raise LookupError(msg)
            else:
                msg = "List view does not displayed in content area"
                raise TabError(msg)
        
        def _get_file_object_(self, file_name, file_type=None):
            """
            Description : Return the file object. If grid view is active then file object return from grid view else return from list view.
            :param - file_type - file type to filter the file object. 
            :file_type : ['fex', 'url', 'folder']
            """
            file_type_value = ''
            if self._is_grid_view_displayed_():
                grid_view_file_types = {'fex' : 'fex', 'url' : 'url'}
                file_xpath = self.locators.gridview_file_xpath
                if file_type is not None :
                    file_type = file_type.lower()
                    file_type_value = grid_view_file_types.get(file_type)
            else:
                file_xpath = self.locators.listview_file_xpath
                list_view_file_types = {'fex' : 'fex', 'url' : 'url'}
                if file_type is not None :
                    file_type = file_type.lower()
                    file_type_value = list_view_file_types.get(file_type)
            if file_type_value is None :
                msg = "Currently we are not implemented [{0}] file type to filter the file object.".format(file_type)
                raise NotImplementedError(msg)
            file_xpath = file_xpath.format(file_name, file_type_value)
            file_objects = self.driver.find_elements_by_xpath(file_xpath)
            if file_objects == [] :
                msg = "[{0}] file does not exist in content area.".format(file_name)
                raise FileNotFoundError(msg)
            self._javascript.scrollIntoView(file_objects[0], wait_time=1)
            return file_objects[0]
            
        def _get_folder_object_(self, folder_name):
            """
            Description : Return the folder object. If grid view is active then file object return from grid view else return from list view.
            """
            if self._is_grid_view_displayed_():
                folders_locator = self.locators.grid_view_folders
            else :
                folders_locator = self.locators.list_view_folders
            folder_objects = self._utils.validate_and_get_webdriver_objects_using_locator(folders_locator, "Content grid view folder")
            folder_index = self._javascript.find_element_index_by_text(folder_objects, folder_name)
            if folder_index is None:
                msg = "[{0}] folder does not exist in content area.".format(folder_name)
                raise FileNotFoundError(msg)
            folder_object = folder_objects[folder_index]
            self._javascript.scrollIntoView(folder_object, wait_time=1)
            return folder_object
        
        def switch_to_list_view(self):
            """
            Description: Click on list view button to switch to list view
            """
            if self._is_grid_view_displayed_():
                list_view_button = self._utils.validate_and_get_webdriver_object_using_locator(paris_home_page_locators.Workspaces.NavigationBar.list_view, "Switch to list view button")
                self._core_utils.left_click(list_view_button)
                self._utils.wait_for_page_loads(30)
                self._utils.synchronize_until_element_is_visible(self.locators.list_view[1], 60)
                
        def switch_to_grid_view(self):
            """
            Description: Click on grid view button to switch to grid view
            """
            if self._is_list_view_displayed_():
                grid_view_button = self._utils.validate_and_get_webdriver_object_using_locator(paris_home_page_locators.Workspaces.NavigationBar.grid_view, "Switch to grid view button")
                self._core_utils.left_click(grid_view_button)
                self._utils.wait_for_page_loads(30)
                self._utils.synchronize_until_element_is_visible(self.locators.grid_view[1], 60)
        
        def click_choose_columns_icon(self):
            """
            Description: Left click on Choose column icon in list view.
            """
            choose_columns = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.listview_choose_columns, "List view choose columns icon")
            self._core_utils.left_click(choose_columns)
            
        def click_listview_column_heading(self, heading_name):
            """
            Description: Left click on list view column heading.
            :Usage - click_listview_column_heading("Title")
            """
            self._core_utils.left_click(self._get_listview_column_heading_obj(heading_name))
        
        def verify_list_view_columns_heading(self, expected, step_num, assert_type="equal"):
            """
            Description: Verify the List view columns heading text
            """
            headings = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.listview_columns_heading, "List view columns heading labels")
            actual_headings = [heading.text.strip() for heading in headings if heading.is_displayed()]
            self._utils.list_values_verification(expected, actual_headings, step_num, "List View Columns Heading", assert_type)
            
        def _get_listview_column_heading_obj(self, heading_name):
            """
            Description: Return the list view column heading object
            """
            headings_label = self._utils.validate_and_get_webdriver_objects(self.locators.listview_columns_heading[1] + " .ibx-label-text" , "List view columns heading labels")
            heading_index = self._javascript.find_element_index_by_text(headings_label, heading_name)
            if heading_index != None:
                headings = self._utils.validate_and_get_webdriver_objects_using_locator(self.locators.listview_columns_heading, "List view columns heading labels")
                return headings[heading_index]
            else:
                error_msg = "[{}] column heading not found in List View oh Home Page content area".format(heading_name)
                raise LookupError(error_msg)
            
class ModalDialogs:
    
    def __init__(self, driver):
        
        self.driver = driver
    
    @property
    def ShareWithOthers(self) : return modal_dialog.ShareWithOthers(self.driver)
    
    @property
    def V5Portal(self): return self.__v5portal__(self.driver)
    
    @property
    def CollaborativePortal(self): return self.__v4portal__(self.driver)
    
    @property
    def Folder(self): return self.__folder__(self.driver)
    
    @property
    def URL(self): return self.__url__(self.driver)
    
    @property
    def Blog(self): return self.__blog__(self.driver)
    
    @property
    def Alert(self): return modal_dialog.Alert(self.driver)
    
    @property
    def NewWorkspace(self): return self.__new_workspace__(self.driver)
    
    @property
    def NewTextResource(self): return self.__new_text_resource__(self.driver)
    
    @property
    def ChangePassword(self): return self._change_password_(self.driver)
    
    @property
    def UploadCompleted(self): return self._upload_completed_(self.driver)
    
    @property
    def Resources(self): return modal_dialog.Resources(self.driver)
    
    @property
    def Shortcut(self): return self._shortcut_(self.driver)
    
    @property
    def InviteUser(self): return self._invite_users_(self.driver)
    
    @property
    def AboutWebFOCUS(self): return self._about_wf_(self.driver)
    
    @property
    def Import(self): return self._import_(self.driver)
    
    class __v5portal__(modal_dialog.Common):
        
        def __init__(self, driver):
            
            self._title_ = "V5 Portal"
            super(ModalDialogs.__v5portal__, self).__init__(driver, self._title_)

        @property
        def Title(self): return modal_dialog.TextBox(self.driver, "Title",  self._title_)
        
        @property
        def Name(self): return modal_dialog.TextBox(self.driver, "Name",  self._title_)
        
        @property
        def Alias(self): return modal_dialog.TextBox(self.driver, "Alias",  self._title_)
        
        @property
        def MaximumWidth(self): return modal_dialog.TextBox(self.driver, "Maximum width",  self._title_)
        
        @property
        def Theme(self): return modal_dialog.TextBox(self.driver, "Theme",  self._title_)
        
        @property
        def URL(self): return modal_dialog.TextBox(self.driver, "URL",  self._title_)
        
        @property
        def CreateButton(self): return modal_dialog.Button(self.driver, "Create",  self._title_)
        
        @property
        def ShowPortalTitle(self): return ibx_custom_controls.ibxCheckBoxSimple("Show portal title in banner")
        
        @property
        def ShowTopNavigation(self): return ibx_custom_controls.ibxCheckBoxSimple("Show top navigation in banner")
        
        @property
        def CreateMyPagesMenu(self): return ibx_custom_controls.ibxCheckBoxSimple("Create My Pages menu")
        
        @property
        def Banner(self): 
            toggle_object = self._utils_.validate_and_get_webdriver_object(self._locator_.toggle_button_css.format('Banner'), "Banner toggle button")
            return ibx_custom_controls.ibxSwitch(toggle_object, 'Banner')
        
        @property
        def CancelButton(self): return modal_dialog.Button(self.driver, "Cancel",  self._title_)
        
        @property
        def SaveButton(self): return modal_dialog.Button(self.driver, "Save",  self._title_)
        
        @property
        def Logo(self): return ModalDialogs.__v5portal__.__logo__(self.driver, "Logo", self._title_)
        
        @property
        def Navigation(self): return ModalDialogs.__v5portal__.__navigation__(self.driver)
        
        class __logo__(modal_dialog.TextBox):
            
            __browse_btn_css_ = ".sd-input-div .hp-form-browse-button"
            
            def __init__(self, driver, name, title):
        
                super(ModalDialogs.__v5portal__.__logo__, self).__init__(driver, name, title)
                
            def click_browse_button(self):
                """
                Description : Left click on browse button
                """
                browse_btn_obj = self._utils_.validate_and_get_webdriver_object(self.__browse_btn_css_, "Browse Button")
                self._core_utils_.left_click(browse_btn_obj)
                self._utils_.synchronize_with_visble_text('.pop-top', 'Select', 30)
                self._utils_.wait_for_page_loads(15)
            
            def verify_browse_button_displayed(self, step_num):
                """
                Description : Verify Browse button is displayed
                """
                btn_text = self._utils_.validate_and_get_webdriver_object(self.__browse_btn_css_, "Browse Button").text.strip()
                msg = "Step {0} : Verify Browse button is displayed next to Logo textbox".format(step_num)
                self._utils_.asequal('Browse', btn_text, msg)
                
        class __navigation__(__Common__):
            
            def __init__(self, driver):
        
                super(ModalDialogs.__v5portal__.__navigation__, self).__init__(driver)
            
            def select(self, title):
                """
                Description : Left click on given title navigation to select
                :Usage - select('Three-level')
                """
                self._core_utils.left_click(self._object_(title))
                
            def verify(self, step_num):
                """
                Description : Verify navigations
                :Usage - verify('05.03')
                """
                expected_navigations = ['Two-level side', 'Three-level', 'Two-level top']
                actual_navigations = [nav.get_attribute('title') for nav in self._objects_ if nav.is_displayed()]
                msg = "Step {0} : Verify {1} navigations displayed in V5 Portal dialog".format(step_num, expected_navigations)
                self._utils.asequal(expected_navigations, actual_navigations, msg)
            
            def verify_selected_navigation(self, expected_navigation, step_num):
                """
                Description : Verify the selected navigation 
                :Usage - verify_selected_navigation(['Three-level'], '05.03')
                """
                actual_navigation = []
                for navigation in self._objects_:
                    bg_color = Color.from_string(navigation.value_of_css_property('background-color')).rgb
                    ((bg_color=='rgb(238, 238, 238)') or (bg_color=='rgb(204, 204, 204)')) and actual_navigation.append(navigation.get_attribute('title'))
                msg = "Step {0} : Verify {1} navigation selected in V5 Portal dialog".format(step_num, expected_navigation)
                self._utils.asequal(expected_navigation, actual_navigation, msg)       
                
            @property
            def _objects_(self):
                """
                Description : Return the all navigations object as list
                """
                navigations_obj = self._utils.validate_and_get_webdriver_objects("div[data-ibxp-text='Navigation'] ~ div[title]", "V5 portal navigations")
                return navigations_obj
            
            def _object_(self, title):
                """
                Description : Return the specified navigation object
                """
                title_list = [nav.get_attribute('title') for nav in self._objects_]
                if title in title_list:
                    return self._objects_[title_list.index(title)]
                else:
                    raise LookupError("[{0}] Navigation does not exists in V5 Portal dialog".format(title))
        
    class __v4portal__(modal_dialog.Common):
        
        def __init__(self, driver):
            
            self._title_ = "Collaborative Portal"
            super(ModalDialogs.__v4portal__, self).__init__(driver, self._title_)

        @property
        def Title(self): return modal_dialog.TextBox(self.driver, "Title",  self._title_)
        
        @property
        def Name(self): return modal_dialog.TextBox(self.driver, "Name",  self._title_)
        
        @property
        def Path(self): return modal_dialog.TextBox(self.driver, "Path",  self._title_)
        
        @property
        def URL(self): return modal_dialog.TextBox(self.driver, "URL",  self._title_)
        
        @property
        def CreateButton(self): return modal_dialog.Button(self.driver, "Create",  self._title_)
        
        @property
        def CancelButton(self): return modal_dialog.Button(self.driver, "Cancel",  self._title_)
        
    class __folder__(modal_dialog.Common):
        
        def __init__(self, driver):
            
            self._title_ = "Folder"
            super(ModalDialogs.__folder__, self).__init__(driver, self._title_)
    
        @property
        def Title(self): return modal_dialog.TextBox(self.driver, "Title",  self._title_)
        
        @property
        def Name(self): return modal_dialog.TextBox(self.driver, "Name",  self._title_)
        
        @property
        def OKButton(self): return modal_dialog.Button(self.driver, "OK",  self._title_)
        
        @property
        def CancelButton(self): return modal_dialog.Button(self.driver, "Cancel",  self._title_)
    
    class __url__(modal_dialog.Common):
        
        def __init__(self, driver):
            
            self._title_ = "URL"
            super(ModalDialogs.__url__, self).__init__(driver, self._title_)
    
        @property
        def Title(self): return modal_dialog.TextBox(self.driver, "Title",  self._title_)
        
        @property
        def Name(self): return modal_dialog.TextBox(self.driver, "Name",  self._title_)
        
        @property
        def Summary(self): return modal_dialog.TextBox(self.driver, "Summary",  self._title_)
        
        @property
        def URL(self): return modal_dialog.TextBox(self.driver, "URL",  self._title_)
        
        @property
        def OKButton(self): return modal_dialog.Button(self.driver, "OK",  self._title_)
        
        @property
        def CancelButton(self): return modal_dialog.Button(self.driver, "Cancel",  self._title_)
        
        @property
        def UpdateButton(self): return modal_dialog.Button(self.driver, "Update",  self._title_)
    
    class __blog__(modal_dialog.Common):
        
        def __init__(self, driver):
            
            self._title_ = "Blog"
            super(ModalDialogs.__blog__, self).__init__(driver, self._title_)
    
        @property
        def Title(self): return modal_dialog.TextBox(self.driver, "Title",  self._title_)
        
        @property
        def Summary(self): return modal_dialog.TextBox(self.driver, "Summary",  self._title_)
        
        @property
        def OKButton(self): return modal_dialog.Button(self.driver, "OK",  self._title_)
        
        @property
        def CancelButton(self): return modal_dialog.Button(self.driver, "Cancel",  self._title_)
    
    class __new_workspace__(modal_dialog.Common):
        
        def __init__(self, driver):
            
            self._title_ = "New Workspace"
            super(ModalDialogs.__new_workspace__, self).__init__(driver, self._title_)
    
        @property
        def Type(self): return modal_dialog.TextBox(self.driver, "Type",  self._title_)
        
        @property
        def Title(self): return modal_dialog.TextBox(self.driver, "Title",  self._title_)
        
        @property
        def Name(self): return modal_dialog.TextBox(self.driver, "Name",  self._title_)
        
        @property
        def OKButton(self): return modal_dialog.Button(self.driver, "OK",  self._title_)
        
        @property
        def CancelButton(self): return modal_dialog.Button(self.driver, "Cancel",  self._title_)
        
        @property
        def CreateReportingServerApplication(self): return ibx_custom_controls.ibxCheckBoxSimple('Create Reporting Server Application')
    
    class __new_text_resource__(modal_dialog.Common):
        
        def __init__(self, driver):
            
            self._title_ = "New Text Resource"
            self._locators_ = modal_dialog.Locators.HomePage.NewTextResource
            super(ModalDialogs.__new_text_resource__, self).__init__(driver, self._title_)
        
        def select_tab(self, tab_name):
            """
            Description : Left click on file type tab to select
            :Usage - select_tab("WEB")
            """
            tabs_obj = self._utils_.validate_and_get_webdriver_objects_using_locator(self._locators_.file_type_tabs, self._title_ + " File type tabs")
            error_msg = "[{0}] file type tab does not exists in [{1}] dialog".format(tab_name, self._title_)
            tab_object = self._core_utils_.get_element_object_by_text(tabs_obj, tab_name, error_msg=error_msg, scroll_into_view=False)
            self._core_utils_.left_click(tab_object)
        
        def select_file_type(self, file_type, tab_name=None):
            """
            Description : Description : Left click on file type to select
            :Usage - select_file_type("FOCEXEC (fex)")
            """
            (tab_name != None) and self.select_tab(tab_name)
            file_types_obj = self._utils_.validate_and_get_webdriver_objects_using_locator(self._locators_.file_types, self._title_ + " File types")
            error_msg = "[{0}] file type does not exists in [{1}] dialog".format(file_type, self._title_)
            file_type_obj = self._core_utils_.get_element_object_by_text(file_types_obj, file_type, error_msg=error_msg, scroll_into_view=False)
            self._core_utils_.left_click(file_type_obj)
            
        def verify_tabs(self, expected_tabs, step_num, assert_type='asequal'):
            """
            Description : Verify the file type tabs
            :Usage - verify_tabs(['CONTENT', 'WEB', 'DATA SCIENCE'], "05.01")
            """
            msg = "Step {0} : Verify {1} file type tabs displayed in {2} dialog".format(step_num, expected_tabs, self._title_)
            actual_tabs = [tab.text.strip() for tab in self.driver.find_elements(*self._locators_.file_type_tabs)]
            self._utils_.verify_list_values(expected_tabs, actual_tabs, msg, assert_type)
        
        def verify_file_types(self, expected_files, step_num, assert_type='asequal'):
            """
            Description : Verify the file types
            :Usage - verify_file_types(['FOCEXEC (fex)', 'WebFOCUS Style Sheet (sty)', 'Plain Text (txt)', 'SQL Script (sql)'], "05.01")
            """
            msg = "Step {0} : Verify {1} file types displayed in {2} dialog".format(step_num, expected_files, self._title_)
            actual_files = [tab.text.strip() for tab in self.driver.find_elements(*self._locators_.file_types)]
            self._utils_.verify_list_values(expected_files, actual_files, msg, assert_type)
        
        def verify_selected_tab(self, expected_tabs, step_num):
            """
            Description : Verify the selected tab in text editor
            :Usage - verify_selected_tab(['CONTENT'], "05.01")
            """
            tabs_obj = self._utils_.validate_and_get_webdriver_objects_using_locator(self._locators_.file_type_tabs, self._title_ + " File type tabs")
            actual_tabs = []
            for tab in tabs_obj:
                color = Color.from_string(tab.value_of_css_property('color')).rgba
                bg_img = self._javascript_.get_element_after_style_properties(tab, 'background-image')
                status = all([color=='rgba(52, 81, 94, 1)', bg_img=='radial-gradient(circle at 0px 0px, rgb(52, 85, 219), rgb(145, 44, 167))'])
                status and actual_tabs.append(tab.text.strip())
            msg = "Step {0} : Verify {1} tab selected in {2} dialog".format(step_num, expected_tabs, self._title_)
            self._utils_.asequal(expected_tabs, actual_tabs, msg)
    
    class _change_password_(modal_dialog.Common):
        
        def __init__(self, driver):
            
            self._title_    = "Change Password"
            self._locators_ = modal_dialog.Locators.HomePage.ChangePassword
            super(ModalDialogs._change_password_, self).__init__(driver, self._title_)
        
        @property 
        def UserName(self): return html_controls.TextBox(self._get_textbox_object_('User name'), 'User name')
        
        @property 
        def OldPassword(self): return html_controls.TextBox(self._get_textbox_object_('Old Password'), 'Old Password')
        
        @property 
        def NewPassword(self): return html_controls.TextBox(self._get_textbox_object_('New Password'), 'New Password')
        
        @property 
        def ConfirmNewPassword(self): return html_controls.TextBox(self._get_textbox_object_('Confirm New Password'), 'Confirm New Password')
        
        @property
        def CancelButton(self): return modal_dialog.Button(self.driver, "Cancel",  self._title_)
        
        @property
        def ChangePasswordButton(self): return modal_dialog.Button(self.driver, "Change Password",  self._title_)
        
        @property
        def ErrorMessage(self): 
            error_msg_obj = self._utils_.validate_and_get_webdriver_object_using_locator(self._locators_.warning_msg, "Change Password Error Message Label")
            return html_controls.Label(error_msg_obj, 'Change Password Error Message')
            
        def _get_textbox_object_(self, title):
            """
            Description : Return the textbox object
            """
            textbox_object = self._utils_.validate_and_get_webdriver_object(self._locators_.textbox_css.format(title), title + " Textbox")
            return textbox_object
        
    class _upload_completed_(modal_dialog.Common):
        
        def __init__(self, driver):
            
            self._title_    = "Upload completed"
            super(ModalDialogs._upload_completed_, self).__init__(driver, self._title_)
        
        def verify_messages(self, expected_msgs, step_num, assert_type='asequal'):
            """
            Description : Verify the uploaded messages
            :Usage : verify_messages(['sample.png Type not supported', 'sample2.png Type not supported'], '04.01')
            """
            msg_css = self._locator_.message[1] + " .upload-vbox"
            msgs_obj = self._utils_.validate_and_get_webdriver_objects(msg_css, "Upload completed dialog message")
            actual_msgs = [msg.text.strip().replace('\n', ' ') for msg in msgs_obj]
            msg = 'Step {0} : Verify Upload completed model dialog messages'.format(step_num)
            self._utils_.verify_list_values(expected_msgs, actual_msgs, msg, assert_type)
        
    class _shortcut_(modal_dialog.Common):
        
        def __init__(self, driver):
            
            self._title_    = "Shortcut"
            super(ModalDialogs._shortcut_, self).__init__(driver, self._title_)
        
        @property
        def Type(self): return ModalDialogs._shortcut_._type_()
        
        @property
        def TargetPath(self): return ModalDialogs._shortcut_._target_path_('Target path', 'Shortcut')
        
        @property
        def Title(self): return modal_dialog.TextBox(self.driver, "Title",  self._title_)
        
        @property
        def Summary(self): return modal_dialog.TextBox(self.driver, "Summary",  self._title_)
        
        @property
        def OKButton(self): return modal_dialog.Button(self.driver, "OK",  self._title_)
        
        @property
        def CancelButton(self): return modal_dialog.Button(self.driver, "Cancel",  self._title_)
        
        class _type_:
            
            @property
            def RepositoryFile(self): return ibx_custom_controls.ibxRadioButtonSimple('Repository file')
            
            @property
            def MasterFile(self): return ibx_custom_controls.ibxRadioButtonSimple('Master file')
        
        class _target_path_(modal_dialog.TextBox):
            
            def __init__(self, name, model_title):
                
                super(ModalDialogs._shortcut_._target_path_, self).__init__(Global_variables.webdriver, name, model_title)
            
            @property
            def BrowseButton(self):return html_controls.Button(Global_variables.webdriver.find_element_by_id("sdbtnBrowse"), 'Shortcut browse')
    
    class _invite_users_(modal_dialog.Common):
        
        def __init__(self, driver):
            
            self._title_    = "Invite Users"
            super(ModalDialogs._invite_users_, self).__init__(driver, self._title_)
            
        @property
        def FirstName(self): return modal_dialog.TextBox(self.driver, "First Name", self._title_)
        
        @property
        def LastName(self): return modal_dialog.TextBox(self.driver, "Last Name", self._title_)
        
        @property
        def BusinessEmail(self): return modal_dialog.TextBox(self.driver, "Business Email Address", self._title_)
        
        @property
        def CancelButton(self): return modal_dialog.Button(self.driver, "Cancel",  self._title_) 
        
        @property
        def InviteButton(self): return modal_dialog.Button(self.driver, "Invite",  self._title_)  
        
        @property
        def ErrorMessage(self): 
            error_label_css = modal_dialog.Locators.Common.base_css + ".invite-form-fill-error-text"
            self._utils_.synchronize_until_element_is_visible(error_label_css, 20)
            error_msg_obj = self._utils_.validate_and_get_webdriver_object(error_label_css, "Invite user Error Message Label")
            if error_msg_obj.is_displayed()==False:
                raise LookupError("Invite user Error Message label does not displayed")    
            return html_controls.Label(error_msg_obj, 'Invite user Error Message')
    
    class _about_wf_(modal_dialog.Common):
        
        def __init__(self, driver):
            
            self._title_    = "About WebFOCUS"
            super().__init__(driver, self._title_)
        
        @property
        def OKButton(self): return modal_dialog.Button(self.driver, "OK",  self._title_)
        
        def verify_labels(self, expected, step_num, ):
            """
            Description : Verify the labels
            """
            labels_object = self.driver.find_elements_by_css_selector(modal_dialog.Locators.Common.base_css + " .help-about-text-field")
            actual = [label.text.strip() for label in labels_object if label.is_displayed()]
            msg = "Step {0} : Verify the About WebFOCUS labels".format(step_num)
            self._utils_.verify_list_values(expected, actual, msg, assert_type="asequal")
    
    class _import_(modal_dialog.Common):
        
        def __init__(self, driver):
            
            self._title_ = "Import"
            super().__init__(driver, self._title_)
            
class NotifyPopup(__Common__):
    
    def __init__(self, driver):
        
        super(NotifyPopup, self).__init__(driver)
        self.locators = paris_home_page_locators.NotifyPopup
    
    def verify_background_color(self, step_num, color_name='fruit_salad'):
        """
        Description : Verify the background color
        """
        notify_object = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.notify_popup, "Notify Popup")
        msg = "Step {0} : Verify Notify Popup displayed with [{1}] background color".format(step_num, color_name)
        self._utils.verify_element_color_using_css_property(None, color_name, msg, attribute='background-color', element_obj=notify_object)
    
    def verify_transparent(self, step_num):
        """
        Description : Verify the transparent value
        :Usage - verify_transparent("01.04")
        """
        notify_object = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.notify_popup, "Notify Popup")
        value = notify_object.value_of_css_property('opacity')
        msg = "Step {0} : Verify Notify Popup displayed as transparent".format(step_num)
        self._utils.asequal('0.8', value, msg)
        
    def verify_text(self, expected_text, step_num):
        """
        Description : Verify the text
        :Usage - verify_text("Favorite already exists ", "03.04")
        """
        actual_text = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.notify_popup, "Notify Popup").text.strip()
        msg = "Step {0} : Verify [{1}] displayed in Notify Popup".format(step_num, expected_text)
        self._utils.asequal(expected_text, actual_text, msg)
    
    def wait_for_visible(self, wait_time=10):
        """
        Description : Wait web driver until Notify Ppouop visible on screen
        """
        self._utils.synchronize_until_element_is_visible(self.locators.notify_popup[1], wait_time, pause_time=0)
        
    def close(self):
        """
        Description : Left click on close icon to close the Notify Popup
        :Usage - close()
        """
        notify_object = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.close_button, "Notify Popup close icon")
        self._core_utils.left_click(notify_object)
        
class RunWindow(__Common__):
    
    def __init__(self, driver):
        
        super(RunWindow, self).__init__(driver)
        self.locators = paris_home_page_locators.RunWindow
    
    def wait_for_visible(self, wait_time=10):
        """
        Description : Web driver wait until Run Window visible on screen
        """
        self._utils.synchronize_until_element_is_visible(self.locators.run_window[1], wait_time, pause_time=0.5)
    
    def close(self):
        """
        Description : Left click on close icon to close the Run Window
        :Usage - close()
        """
        close_icon = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.close_icon, "Run Window close icon")
        self._core_utils.left_click(close_icon)
    
    def verify_title(self, expected_title, step_num):
        """
        Description : Verify the text
        :Usage - verify_title("C123456", "03.04")
        """
        actual_title = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.title, "Run Window title").text.strip()
        msg = "Step {0} : Verify [{1}] displayed in Run window toolbar title".format(step_num, expected_title)
        self._utils.asequal(expected_title, actual_title, msg)
    
    def verify_not_displayed(self, step_num):
        """
        Description : Verify whether Run window not displayed
        :Usage - verify_not_displayed("03.04")
        """
        run_window = self.driver.find_elements(*self.locators.run_window) == []
        msg = "Step {0} : Verify Run window not displayed in home page".format(step_num)
        self._utils.asequal(True, run_window, msg)
        
    def open_in_new_window(self):
        """
        Description : Left click on Open in new window icon
        """
        open_icon = self._utils.validate_and_get_webdriver_object_using_locator(self.locators.open_in_new_win, "Open in new window icon")
        self._core_utils.left_click(open_icon)
        self._core_utils.switch_to_new_window()
        
    def switch_to_frame(self):
        """
        Description : Switch to iframe 
        """
        self._web_element.wait_until_element_visible(self.locators.frame, 60)
        self._core_utils.switch_to_frame(self.locators.frame[1])
        self._utils.wait_for_page_loads(80, pause_time=2)
        
    def switch_to_default_content(self):
        """
        Description : Switch to default content
        """
        self._core_utils.switch_to_default_content()
