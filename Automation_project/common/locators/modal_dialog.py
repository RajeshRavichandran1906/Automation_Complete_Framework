from selenium.webdriver.common.by import By

class Common:
    
    base_css            =  ".pop-top[role*='dialog'] "
    textbox_css         =  str(base_css + "div[data-ibxp-text='{0}'] ~ div [role='textbox']")
    toggle_button_css   =  str(base_css + "div[data-ibxp-text='{0}'] ~ div[data-ibx-type='ibxSwitch']")
    title_bar_caption   =  (By.CSS_SELECTOR, base_css + ".ibx-title-bar-caption")
    close_icon          =  (By.CSS_SELECTOR, base_css + ".ibx-title-bar-close-button")
    buttons             =  (By.CSS_SELECTOR, ".ibx-dialog-button-box .ibx-dialog-button:not([style*='none'])")
    labels              =  (By.CSS_SELECTOR, base_css + ".sd-input-div:not([style*='none'])>div.hp-form-field-title")
    message             =  (By.CSS_SELECTOR, base_css + ".ibx-dialog-content")
    
class HomePage:
    
    class V5Portal:
        
        root_css         =  ".create-pvd-dialog" + Common.base_css
        title_textbox    =  root_css + ".pvd-title input" 
        name_textbox     =  root_css + ".pvd-name input" 
        alias_textbox    =  root_css + ".pvd-alias input" 
        banner_toggle    =  root_css + ".portal-show-banner" 
        title_textbox    =  root_css + ".pvd-title input" 
        title_textbox    =  root_css + ".pvd-title input" 
    
    class NewTextResource:
        
        root_css         =   ".text-editor-startup" + Common.base_css
        file_type_tabs   =   (By.CSS_SELECTOR, root_css + ".ibx-tab-button")
        file_types       =   (By.CSS_SELECTOR, root_css + ".tpg-selected .text-editor-file-type")
    
    class ChangePassword:
        
        root_css         =   ".change-password" + Common.base_css
        textbox_css      =   root_css + "div[title='{0}'] ~ div input"
        labels           =   (By.CSS_SELECTOR, root_css + ".hp-reboot-text-field")
        warning_msg      =   (By.CSS_SELECTOR, root_css + ".form-fill-error-text")
        
class ShareWithOthers:
    
    base_css            =  ".share-with-others-dialog "
    search_textbox      =  (By.CSS_SELECTOR, base_css + ".share-with-txt-search input")
    search_dropdown     =  (By.CSS_SELECTOR, base_css + ".Share-with-menu-btn .ds-icon-caret-down")
    
    class UserGroupResults:
        
        base_css        =  "#shareWithDropdown "
        results         =  (By.CSS_SELECTOR, base_css + ".item-user-group ")
        descriptions    =  (By.CSS_SELECTOR, results[1] + ".sw-item-desc")
        names           =  (By.CSS_SELECTOR, results[1] + ".sw-item-name")
    
    class SharedWith:
        
        base_css        =  ".share-with-hbox "
        users_groups    =  (By.CSS_SELECTOR, base_css + ".share-with-item ")
        descriptions    =  (By.CSS_SELECTOR, users_groups[1] + ".sw-item-desc")
        names           =  (By.CSS_SELECTOR, users_groups[1] + ".sw-item-name")
        usergroup_icon  =  (By.CSS_SELECTOR, ".sw-item-icon")
        remove_icon     =  (By.CSS_SELECTOR, ".item-close-icon")

class Resources:
    
    base  = (By.CSS_SELECTOR, "div.open-dialog-resources")
    
    class NavigationBar:
        
        base_css             =  "div.sd-toolbar "
        breadcrumb_css       =  base_css + "div[data-ibx-type='breadCrumbTrail'] div[title='{0}'] "
        breadcrumb_arrow_css =  breadcrumb_css + "+ div.sd-right-carat .fa-chevron-right"
        breadcrumbs          =  (By.CSS_SELECTOR, base_css + "div[data-ibx-type='breadCrumbTrail'] div[title]")
        list_view            =  (By.CSS_SELECTOR, base_css + "[title='List View']")
        grid_view            =  (By.CSS_SELECTOR, base_css + "[title='Tile View']")
        refresh              =  (By.CSS_SELECTOR, base_css + "div.sd-btn-refresh")
        search               =  (By.CSS_SELECTOR, ".sd-txt-search input")
    
    class GridView:
        
        base_css        =   "div.sd-files-box-files:not([style*='none']) "
        files           =   (By.CSS_SELECTOR, base_css + ".file-item")
        folders          =   (By.CSS_SELECTOR, base_css + ".folder-item")
    
    class ListView:
        
        base_css        =   "div.sd-files-listing:not([style*='none'])"
        files           =   (By.CSS_SELECTOR, base_css + ".file-item")
        folders          =   (By.CSS_SELECTOR, base_css + ".folder-item")