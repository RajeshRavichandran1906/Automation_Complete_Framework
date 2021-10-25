from selenium.webdriver.common.by import By

class Banner:
    
    popup_css           =  ".pop-top[role='menu'] "
    top_banner_css      =  "div.hpreboot-top-bar "
    home                =  (By.CSS_SELECTOR, top_banner_css + "[title^='WebFOCUS']")
    my_workspace        =  (By.CSS_SELECTOR, top_banner_css + "[title='My Workspace']")
    shared_with_me      =  (By.CSS_SELECTOR, top_banner_css + "[title='Shared with Me']")
    workspaces          =  (By.CSS_SELECTOR, top_banner_css + "[title='Workspaces']")
    utilities           =  (By.CSS_SELECTOR, top_banner_css + "[title ='Utilities']")
    settings            =  (By.CSS_SELECTOR, top_banner_css + "[title ='Settings']")
    help                =  (By.CSS_SELECTOR, top_banner_css + "[title ='Help']")
    user                =  (By.CSS_SELECTOR, top_banner_css + "[title ='User']")
    invite_user         =  (By.CSS_SELECTOR, top_banner_css + "[title ='Invite User']")
    plus_icon           =  (By.CSS_SELECTOR, "div.hpreboot-post-icon")
    get_data            =  (By.CSS_SELECTOR, "div.toolbar-get-data")
    visualize_data      =  (By.CSS_SELECTOR, "div.toolbar-design-content")
    search_parent_css   =  "#searchContainer "
    search_textbox      =  (By.CSS_SELECTOR, search_parent_css + "input")
    search_results      =  (By.CSS_SELECTOR, search_parent_css + "li[role='option']")
    search_results_name =  (By.CSS_SELECTOR, search_results[1] + ">div:nth-child(2)>div:nth-child(1)")
    search_icon         =  (By.CSS_SELECTOR, search_parent_css + "button[title^='Find results']")
    search_clear_btn    =  (By.CSS_SELECTOR, search_parent_css + "button[title^='Clear']")
    top_bar_menus       =  (By.CSS_SELECTOR, top_banner_css + "div[title]")
    
    class ToolListMenu:
        
        root_css        =  ".pop-top.tool-list-menu "
        tools           =  (By.CSS_SELECTOR, root_css + ".tlm-start-dlg-radio")
        close_icon      =  (By.CSS_SELECTOR, root_css + ".tool-list-menu-close-icon")
        
class MyWorkspace:
    
    root_css                =   "div.homepage-content:not([style*='none']) .view-all-area "
    grid_view               =   (By.CSS_SELECTOR, root_css + "div.home-tile-contents:not([style*='none'])")
    list_view               =   (By.CSS_SELECTOR, root_css + "div.home-list-contents:not([style*='none'])")
    grid_view_items         =   (By.CSS_SELECTOR, grid_view[1] + " .test-item")
    list_view_items         =   (By.CSS_SELECTOR, list_view[1] + " div[role='row']>div[role='gridcell']:nth-child(2)")
    grid_view_button        =   (By.CSS_SELECTOR, root_css + ".grid-view-btn")
    list_view_button        =   (By.CSS_SELECTOR, root_css + ".list-view-btn")
    choose_colums_button    =   (By.CSS_SELECTOR, root_css + ".grid-view-menu-control-btn")
    
class SharedWithMe(MyWorkspace):
    pass

class Home(MyWorkspace):
    
    recent_section_css          = "div.home-recent"
    favorites_section_css       = "div.home-favorites"
    portals_section_css         = "div.home-portals"
    getting_section_css         = "div.home-getting-started"
    section_items_css           = "{0} .test-item"
    section_item_scroll_css     = "{0} .ibx-csl-items-box"
    view_all_css                = "{0} .view-all-btn"
    left_arrow                  =  (By.CSS_SELECTOR, MyWorkspace.root_css + ".wf-left-arrow")

class Workspaces:
    
    iframe_css              =  ".home-old-workspaces iframe"
    page_load_completed_css =  "body.ibx-visible"
    
    class NavigationBar:
        
        navigation_bar_css   =  "div.toolbar "
        breadcrumb_css       =  "div.toolbar div[data-ibx-type='breadCrumbTrail'] div[title='{0}'] "
        breadcrumb_arrow_css =  breadcrumb_css + "+ div.sd-right-carat .fa-chevron-right"
        breadcrumbs          =  (By.CSS_SELECTOR, "div.toolbar div[data-ibx-type='breadCrumbTrail'] div[title]")
        list_view            =  (By.CSS_SELECTOR, navigation_bar_css + ".btn-how-view-grid:not([style*='none'])")
        grid_view            =  (By.CSS_SELECTOR, navigation_bar_css + ".btn-how-view:not([style*='none'])")
        refresh              =  (By.CSS_SELECTOR, navigation_bar_css + "div.btn-refresh")
    
    class ResourcesTree:
        
        resources_tree_css  =  "div.left-pane .ibfs-tree "
        expand_icon         =  (By.CSS_SELECTOR, "div[class*='ds-icon-caret-right']")
        collapse_icon       =  (By.CSS_SELECTOR, "div[class*='ds-icon-caret-down']")
        selected_item       =  (By.CSS_SELECTOR, resources_tree_css + ".ibfs-item-selected")
        collapse            =  (By.CSS_SELECTOR, "div.left-pane div.tree-collapse-button")
        expand              =  (By.CSS_SELECTOR, "div.tree-showcollapse-button:not([style*='none'])")
        items               =  (By.CSS_SELECTOR, resources_tree_css + " .ibfs-label")
        
    class ActionBar:
        
        action_bar_css      =   "div.create-new-box "
        tabs                =  (By.CSS_SELECTOR, action_bar_css + ".ibx-tab-button")
        tab_options         =  (By.CSS_SELECTOR, "{0}.action-bar-tab.tpg-selected .create-new-item, {0}.domains-new-items-box .create-new-item".format(action_bar_css))
        collapse            =  (By.CSS_SELECTOR, action_bar_css + "[title='Collapse actions bar']")
        expand              =  (By.CSS_SELECTOR, action_bar_css + "[title='Expand actions bar']")
        selected_tab        =  (By.CSS_SELECTOR, tabs[1] + ".checked")
        title               =  (By.CSS_SELECTOR, action_bar_css + ".content-title-action-label")
        childrens           =  (By.CSS_SELECTOR, action_bar_css + ">div:not(.content-title-bar)")    
        
    class ContentArea:
        
        content_area_css        =  "div.files-box"
        gridview_xpth           =  "//div[@id='files-box-area'][not(contains(@style, 'none'))]"
        gridview_file_xpath     =  gridview_xpth + "//img[contains(@src, '{1}')]//parent::div//following-sibling::div[normalize-space() = '{0}'][contains(@class, 'file-item-hbox')]/parent::div" 
        listview_file_xpath     =  "//div[@id='files-listing-area'][not(contains(@style, 'none'))]//div[normalize-space()='{0}'][@title]//div[not(contains(@class, 'fa-folder'))][contains(@class,'ibx-glyph-{1}')]//parent::div[@title]"
        grid_view               =  (By.CSS_SELECTOR, "div.files-box-files:not([style*='none']) ")
        grid_view_files         =  (By.CSS_SELECTOR, grid_view[1] + ".file-item")
        grid_view_folders       =  (By.CSS_SELECTOR, grid_view[1] + ".folder-item .folder-div")
        list_view               =  (By.CSS_SELECTOR, "div.files-listing:not([style*='none']) ")
        list_view_files         =  (By.CSS_SELECTOR, list_view[1] + "div[data-ibx-type='ibxLabel']:not([class*='files-box-files-'])")
        list_view_folders       =  (By.CSS_SELECTOR, list_view[1] + "[class*='files-box-files-'].grid-cell-data")
        list_view_folder_icon   =  (By.CSS_SELECTOR, ".ibx-label-icon")
        grid_view_summary       =  (By.CSS_SELECTOR, ".file-item-text-box")
        listview_columns_heading=  (By.CSS_SELECTOR, list_view[1] + ".grid-cell-title")
        shared_item_icon        =  (By.CSS_SELECTOR, ".fa-share-alt")
        shared_user_icon        =  (By.CSS_SELECTOR, ".fa-user")
        shortcut_icon           =  (By.CSS_SELECTOR, ".ds-icon-shortcut")
        listview_choose_columns =  (By.CSS_SELECTOR, list_view[1] + "div[title='Choose columns'] div.fa-cog")
        grid_view_sorting       =  (By.CSS_SELECTOR, grid_view[1] + ".content-title-btn-name")
        grid_view_sorted_arrow  =  (By.CSS_SELECTOR, grid_view[1] + ".content-title-buttons .material-icons")
        
class NotifyPopup :
    
    notify_popup  =  (By.CSS_SELECTOR, ".pop-top.notify-popup")
    close_button  =  (By.CSS_SELECTOR, notify_popup[1] + " .notify-popup-content-close-button")

class RunWindow :
    
    run_window          =  (By.CSS_SELECTOR, ".output-area.pop-top ")
    close_icon          =  (By.CSS_SELECTOR, run_window[1] + ".output-area-close-button")
    title               =  (By.CSS_SELECTOR, run_window[1] + ".output-area-titlebar")
    open_in_new_win     =  (By.CSS_SELECTOR, run_window[1] + ".output-area-popout-button")
    frame               =  (By.CSS_SELECTOR, run_window[1] + ".output-area-frame iframe")

class GetDataFrame:
    
    content_css         =  ".wcx-multiframes-content-view"             
    frame               =  (By.CSS_SELECTOR, ".get-data-dlg iframe")
    close_icon          =  (By.CSS_SELECTOR, ".ds-modal-header-close .ibx-label-icon")
    header_title        =  (By.CSS_SELECTOR, ".ds-modal-header-title")
    cancel_button       =  (By.CSS_SELECTOR, "div[qa='Cancel']")
    select_button       =  (By.CSS_SELECTOR, "div[qa='Select']")
    
    class GetData:
    
        local_files     =   (By.CSS_SELECTOR, ".wcx-wctable[wctable='ADP_table_UPL'] .wcx-grid-iconview-cell[title]")
        server_files    =   (By.CSS_SELECTOR, ".wcx-wctable[wctable='ADP_table_DBMS'] .wcx-grid-iconview-cell[title]")
    
    class UploadingData:
        
        class Sheets:
            
            application_folder = (By.XPATH, "//div[normalize-space()='Application Folder:'][contains(@class, 'wcx-form-item')]/following-sibling::div[contains(@class, 'btn-link')]")
    
    class SelectApplicationFolder:
        
        lisview_folders = (By.CSS_SELECTOR, ".wcx-grid-body-row .c0")
            
            