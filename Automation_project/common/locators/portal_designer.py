class Vfive_Designer(object):
    
    '==================================== create v5 portal window ===================================='
    
    'V5 main dialog'
    vfive_main_dialog_css = ".pop-top [data-ibx-name='vbMain']"
    
    'V5 main dialog title caption'
    vfive_main_dialog_title_css = "[data-ibx-name='titleBox'] [data-ibx-name=['caption'] .ibx-label-text"
    
    'V5 main dialog buttons [close, create, no, apply, cancel]'
    close_button_css= "[data-ibx-name='titleClose']"
    create_button_css = "[data-ibxp-text='OK']"
    no_button_css = "[data-ibxp-text='No']"
    apply_button_css = "[data-ibxp-text='Apply']"
    cancle_button_css = "[data-ibxp-text='Cancel']"
    
    'V5 main dialog content'
    vfive_horzontal_row_css = ".sd-input-div"
    title_label_css = "[data-ibxp-text='Title']"
    title_textbox_css = "[data-ibx-type='ibxTextField'].pvd-title"
    title_textbox_input_css = "[data-ibx-type='ibxTextField'].pvd-title input[type='text']"
    name_label_css = "[data-ibxp-text='Name']"
    name_textbox_css = "[data-ibx-type='ibxTextField'].pvd-name"
    name_textbox_input_css = "[data-ibx-type='ibxTextField'].pvd-name input[type='text']"
    alias_label_css = "[data-ibxp-text='Alias']"
    alias_textbox_css = "[data-ibx-type='ibxTextField'].pvd-alias"
    alias_textbox_input_css = "[data-ibx-type='ibxTextField'].pvd-alias input[type='text']"
    banner_label_css = "[data-ibxp-text='Banner']"
    banner_toggle_button_css = "[data-ibx-type='ibxSwitch'].portal-show-banner"
    show_portal_title_in_banner_checkbox_css = "[data-ibx-type='ibxCheckBoxSimple'].pvd-show-title-banner"
    show_portal_title_in_banner_checkbox_checked_css = "[data-ibx-type='ibxCheckBoxSimple'].pvd-show-title-banner .ibx-check-box-simple-marker-check"
    show_portal_title_in_banner_checkbox_unchecked_css = "[data-ibx-type='ibxCheckBoxSimple'].pvd-show-title-banner .ibx-check-box-simple-marker-uncheck"
    show_portal_title_in_banner_checkbox_label_css = "[data-ibx-type='ibxCheckBoxSimple'].pvd-show-title-banner .ibx-label-text"
    logo_label_css = "[data-ibxp-text='Logo']"
    logo_textbox_css = "[data-ibx-type='ibxTextField'].pvd-logo"
    logo_textbox_input_css = "[data-ibx-type='ibxTextField'].pvd-logo input[type='text']"
    logo_browser_button_css = ".pvd-logo-browser"
    navigation_label_css = "[data-ibxp-text='Navigation']"
    navigation_two_level_css = ".navigation-two-level-side"
    navigation_three_level_css = ".navigation-three-level"
    navigation_two_level_top_css = ".navigation-two-level-top"
    show_top_navigation_in_banner_checkbox_css = "[data-ibx-type='ibxCheckBoxSimple'].pvd-top-navigation"
    show_top_navigation_in_banner_checkbox_checked_css = "[data-ibx-type='ibxCheckBoxSimple'].pvd-top-navigation .ibx-check-box-simple-marker-check"
    show_top_navigation_in_banner_checkbox_unchecked_css = "[data-ibx-type='ibxCheckBoxSimple'].pvd-top-navigation .ibx-check-box-simple-marker-uncheck"
    show_top_navigation_in_banner_checkbox_label_css = "[data-ibx-type='ibxCheckBoxSimple'].pvd-top-navigation .ibx-label-text"
    theme_label_css = "[data-ibxp-text='Theme']"
    theme_textbox_css = "[data-ibx-type='ibxTextField'].pvd-theme"
    theme_textbox_input_css = "[data-ibx-type='ibxTextField'].pvd-theme input[type='text']"
    theme_drop_down_button_css = "ibx-select-open-btn"
    theme_selection_list_css= "[data-ibx-type='ibxSelectItemList'] [data-ibx-type='ibxSelectItem']" 
    url_label_css = "[data-ibxp-text='URL']"
    url_textbox_css = "[data-ibx-type='ibxTextField'].pvd-url"
    url_textbox_input_css = "[data-ibx-type='ibxTextField'].pvd-url input[type='text']"
    create_my_pages_menu_checkbox_css = "[data-ibx-type='ibxCheckBoxSimple'].pvd-pages-menu"
    create_my_pages_menu_checkbox_checked_css = "[data-ibx-type='ibxCheckBoxSimple'].pvd-pages-menu .ibx-check-box-simple-marker-check"
    create_my_pages_menu_checkbox_unchecked_css = "[data-ibx-type='ibxCheckBoxSimple'].pvd-pages-menu .ibx-check-box-simple-marker-uncheck"
    create_my_pages_menu_checkbox_label_css = "[data-ibx-type='ibxCheckBoxSimple'].pvd-pages-menu .ibx-label-text"
    
    '==================================== run v5 two level side portal window ===================================='
    
    top_banner_css = ".pvd-portal-banner"
    left_panel_css= ".pvd-container .pvd-left-main-panel .ibx-accordion-page"
    page_canvas= ".pvd-container .pvd-canvas-container"
    newpage_teplate_css= ".pop-top.new-page-from-template"
    current_page = "[data-ibx-type='pdPageRunner']:not([style*='none'])"
    page_heading_css = "[data-ibx-name='_header']"
    panel_css = "[data-ibx-type='pdContainer'][data-ibxp-type='panel']"
    left_panel_top_page_items_css = "div[class*='pvd-left-main-panel'][class*='bundle-folder-pages'] div[class*='folder-item']"
    left_panel_page_folders_container_css = "div[class*='pvd-left-main-panel'][data-ibx-type='ibxAccordionPane']"
    left_panel_page_folder_group_css = left_panel_page_folders_container_css + " div[data-ibx-type*='Accordion']"
    left_panel_page_folder_css = left_panel_page_folders_container_css + " .ibx-accordion-page-button"
    left_panel_page_folder_expand_icon_css = "div[class*='ibx-label-glyph'][class*='material-icons']:not([class*='acc-rotate-glyph']"
    left_panel_page_folder_collapse_css = "div[class*='ibx-label-glyph'][class*='material-icons'][class*='acc-rotate-glyph'] "
    left_panel_folder_item_css = ".ibx-accordion-page-content:not(.acc-cnt-closed) .bundle-folder-item"
    
    '==================================== run v5 three level portal window ===================================='
    
    TOP_LEVEL_FOLDER_PARENT_CSS = ".pvd-second-portal-banner.pvd-top-carousel"
    FOLDER_CSS = ".pvd-menu-button"
    SELECTED_FOLDER_CSS= ".pvd-menu-button.pvd-menu-btn-border"
    LEFT_PANEL_FOLDER_CSS= ".bundle-folder-item:not(.user-page-add) .ibx-accordion-page-button"
    SELECTED_LEFT_PANEL_FOLDER_CSS = ".bundle-folder-item:not(.user-page-add).radio-group-checked .ibx-accordion-page-button"
    ADD_NEW_PAGE_CSS = ".user-page-add .ibx-accordion-page-button"
    LABEL_TEXT_CSS = ".ibx-label-text"
    
    '==================================== run v5 two level top portal window ===================================='
    
    '==================================== run v5 canvas window ===================================='
    
    visible_page_css = "[data-ibx-type='pdPageRunner']:not([style*='left']) "
    page_header_css = visible_page_css + "[data-ibx-name='_header']"
    page_header_title_css = page_header_css + ' .pd-page-title'
    page_header_buttons_css = page_header_css + " div[title]"
    containers_css = visible_page_css + "div[data-ibx-type='pdContainer']"
    containers_title_css = containers_css + " .pd-container-title-bar"
    container_title_bar_buttons_css = ".pd-container-title-bar div[class*='pd-container-title-button'][title]"
    add_content_button_css = "div[title='Add content']"
    panel_container_css = ".pd-cont-relative>div[data-ibx-type='pdContent']"
    dialog_css = "div[data-ibx-type='ibxDialog'][class*='pop-top']"
    dialog_title_css = dialog_css + " .ibx-dialog-title-box"
    dialog_msg_css = dialog_css + " .ibx-dialog-content"
    dialog_buttons_css = dialog_css + " div[data-ibx-type='ibxButton']:not([style*='none'])>div[class='ibx-label-text']"
    dialog_close_icon_css = dialog_css + " .ibx-dialog-title-box div[title='Close']"
    
    '==================================== run v5 page template window ===================================='
    new_page_template_window_css = "div[data-ibx-type='newPageFromTemplate'][class*='pop-top']"
    new_page_template_window_title_bar_css = new_page_template_window_css + " .ibx-dialog-title-box"
    new_page_template_window_close_icon_css = new_page_template_window_css + " .ibx-title-bar-close-button"
    new_page_template_options_css = new_page_template_window_css + " .ibx-dialog-content .np-item"
    open_existing_page_button_css = new_page_template_window_css + " .ibx-dialog-content .np-open"
    select_template_label_css = new_page_template_window_css + " .ibx-dialog-content .np-label-select-template"