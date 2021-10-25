from selenium.webdriver.common.by import By

class WfMainPageLocators(object):
    CONTENT_CSS = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text"
    CONTENT_ICON_CSS = ".main-panel .left-main-panel [class*='chart'][class*='bar'][class*='fa']"
    PORTAL_ICON_CSS = ".main-panel .left-main-panel [class*='circle']:not([class*='question'])"
    FAVORITE_ICON_CSS = ".main-panel .left-main-panel .left-main-panel-favorites-button [class*='star'][class*='fa']:not([id])"
    HELP_ICON_CSS = ".main-panel .left-main-panel [class*='fa'][class*='question'][class*='circle']"
    FILES_BOX_CSS = ".content-box.ibx-widget .files-box .content-title-btn-name .ibx-label-text"
    REPOSITORY_TREE_CSS = ".left-pane .ibfs-tree"
    files_item_css = ".file-item"
    content_area_css = ".content-box"  
    files_item_published_css = ".file-item-published"
    FOLDER_ITEM_PUBLISHED = ".folder-item-published"
    NEW_PORTAL_CREATE_BTN_CSS = ".pop-top [class*='ok-button']"
    ALERT_MESSAGE_CSS = ".pop-top .form-fill-error-text"
    ACTION_BAR_CSS = "div.create-new-box"
    folders_css = ".sd-content-title-label-folders .content-title-label"
    BUTTON_CSS = ".ibx-button[role='button']"
    RUN_SPINER_CSS = ".ibx-waiting-global .fa-spinner"
    ACTION_TAB_CSS = "{0} .ibx-csl-items-box div.ibx-tab-button".format(ACTION_BAR_CSS)
    banner_administrator = (By.CSS_SELECTOR,"#topBannerMenuBox span[id^='BiWelcomeBannerMenuButton']")
    banner_administration = (By.CSS_SELECTOR, "#topBannerMenuBox #AdministrationMainLink")
    banner_tools = (By.CSS_SELECTOR, "#topBannerMenuBox #SignonBannerPanelToolsMenuBtn")
    banner_help = (By.CSS_SELECTOR, "#topBannerMenuBox #SignonBannerPanelHelpMenuBtn")
    banner_sign_out = (By.CSS_SELECTOR, "#topBannerMenuBox #SignoffBannerBtn")
    master_file_container_css = ".pop-top .files-box-files-area"
    master_file_css = master_file_container_css + " [title='{0}'] .ibx-label-text"
    run_dialog_css = "div.output-area.pop-top"
    run_title_css = run_dialog_css + " .output-area-label"
    run_open_in_new_window_css =  run_dialog_css +  " [title='Open in new window']"
    run_close_css = run_dialog_css + " [title='Close']"
    run_frame_css = run_dialog_css + " .output-area-frame>iframe"