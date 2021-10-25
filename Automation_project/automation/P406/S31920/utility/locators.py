'''
Created on Apr 08, 2019

@author: ml12793
'''
from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    '''this class contains reusable locators on the signin page'''
    uid = (By.ID,'SignonUserName')
    pwd = (By.ID, 'SignonPassName')
    submit= (By.ID, 'SignonbtnLogin')

class HomePageLocators(object):
    @staticmethod
    def create_xpath_locator_with_text(base_string, text):
        return By.XPATH, base_string.format(text)
    '''this class contains reusable locators on the new home page'''
    tree_folder_xpath_template = "//div[contains(@class, 'home-tree-node') and div[contains(text(), '{}')]]"
    tree_folder_xpath_template_exact = "//div[contains(@class, 'home-tree-node')]/div[text()='{}']"
    panel_content_button = (By.CSS_SELECTOR, '.left-main-panel-content-button')
    my_workspace_button = (By.CSS_SELECTOR, 'div[title="My Workspace"]')
    shared_with_me_button = (By.CSS_SELECTOR, 'div[title="Shared with Me"]')
    domain_button = (By.CSS_SELECTOR, 'div[title=Workspaces]')
    workspaces_iframe = (By.CSS_SELECTOR, '.ibx-iframe-frame')
    folder = (By.CSS_SELECTOR, '.folder-div')
    view_button = (By.CSS_SELECTOR, '.toolbar-button-div:first-child')
    file = (By.CSS_SELECTOR, '.file-item')
    common_tab = (By.CSS_SELECTOR, '.ibx-csl-item:first-child')
    other_tab = (By.CSS_SELECTOR, '.ibx-csl-item:last-child')
    designer_tab = (By.CSS_SELECTOR, '.ibx-csl-item:nth-child(3)')
    page_button = (By.CSS_SELECTOR, 'div[data-ibxp-text="Page"]')
    portal_button = (By.CSS_SELECTOR, 'div[data-ibxp-text="Portal"]')
    chart_button = (By.CSS_SELECTOR, 'div[data-ibxp-text="Chart"]')
    report_button = (By.CSS_SELECTOR, 'div[data-ibxp-text="Report"]')
    text_editor_button = (By.CSS_SELECTOR, 'div[data-ibxp-text="Text Editor"]')
    fex_button = (By.CSS_SELECTOR, 'div[data-ibxp-user-value="fex"]')
    right_click_menu_run = (By.CSS_SELECTOR, 'div[data-ibxp-command="cmdRun"]')
    right_click_menu_edit = (By.CSS_SELECTOR, 'div[data-ibxp-command="cmdEdit"]')
    right_click_menu_copy = (By.CSS_SELECTOR, 'div[data-ibxp-command="cmdCopy"]')
    right_click_menu_paste = (By.CSS_SELECTOR, 'div[data-ibxp-command="cmdPaste"]')
    right_click_menu_publish = (By.CSS_SELECTOR, 'div[data-ibxp-command="cmdPublish"]')  
    right_click_menu_duplicate = (By.CSS_SELECTOR, 'div[action="dup"]')   
    right_click_menu_delete = (By.CSS_SELECTOR, 'div[action="delete"]')  
    right_click_menu_run_as = (By.CSS_SELECTOR, 'div[data-ibx-name="miMenuItemRunDS"]')
    right_click_menu_run_in_new_window = (By.CSS_SELECTOR, 'div[action="runInWindow"]')
    right_click_menu_edit_with_text_editor = (By.CSS_SELECTOR, 'div[action="editor"]')
    right_click_menu_share = (By.CSS_SELECTOR, 'div[action="shareBasic"]')
    right_click_menu_unshare = (By.CSS_SELECTOR, 'div[action="unshare"]')
    right_click_menu_share_with = (By.CSS_SELECTOR, 'div[action="shareAdvanced"]')
    right_click_menu_properties = (By.CSS_SELECTOR, 'div[action="properties"]')
    output_popup = (By.CSS_SELECTOR, '.output-area')
    output_area_close_button = (By.CSS_SELECTOR, '.output-area-close-button')
    output_area_filter_category = (By.CSS_SELECTOR, 'div[data-ibxp-amper-name="PRODUCT_CATEGORY"]')

class DesignerLocators(object):
    '''this class contains reusable locators on the designer page'''
    demension_tree_box = (By.CSS_SELECTOR, '.dimension-tree-box')
    pill_label = (By.CSS_SELECTOR, '.wfc-bucket-pill-label')
    preview_report_default = (By.CSS_SELECTOR, '.wfc-bc-output-div-report div')
    preview_report_div = (By.CSS_SELECTOR, '.wfc-bc-output-div-report')
    preview_report_title = (By.CSS_SELECTOR, '.arGrid .arGridColumnHeading b')
    preview_report_data = (By.CSS_SELECTOR, '.arGrid #IWindowBodyFBO_0_0 td')
    save_button = (By.CSS_SELECTOR, 'div[data-ibx-name=wfcTBButtonSave]')
    save_dialog = (By.CSS_SELECTOR, 'div[data-ibx-type=opensavedialog2]')
    save_dialog_input_title = (By.CSS_SELECTOR, '.sd-form-field-text-title input')
    save_dialog_save_button = (By.CSS_SELECTOR, 'div[data-ibx-name=btnOK]')
    main_menu_button = (By.CSS_SELECTOR, '.pd-logo')
    main_menu_close = (By.CSS_SELECTOR, 'div[data-ibx-name=wfcTBMenuClose]')
    new_page_dialog = (By.CSS_SELECTOR, 'div[data-ibx-type="pdNewPage"]')
    new_page_dialog_title = (By.CSS_SELECTOR, '.ibx-dialog-title-box')
    new_page_dialog_open_existing = (By.CSS_SELECTOR, '.pd-np-open')
    new_page_dialog_select_template = (By.CSS_SELECTOR, '.pd-np-label-select-template')
    new_page_dialog_template_item = (By.CSS_SELECTOR, '.pd-np-item')
    new_page_dialog_template_item_blank = (By.CSS_SELECTOR, '.pd-np-item:nth-child(2)')
    page_designer_tree_node = (By.CSS_SELECTOR, '.tnode-has-parent')
    page_designer_grid_box = (By.CSS_SELECTOR, 'div[data-ibx-type="pdPageSection"] .pd-page-section-grid-box:first-child')
    page_designer_tree = (By.CSS_SELECTOR, '.pd-tree')
    page_designer_quick_filter = (By.CSS_SELECTOR, 'div[title="Quick filter"]')
    page_designer_filter_bar = (By.CSS_SELECTOR, 'div[data-ibx-type="pdFilterGrid"]')
    page_designer_filter_bar_control = (By.CSS_SELECTOR, 'div[data-ibx-type="pdFilterGrid"] div.pd-filter-panel-content')
    page_designer_preview = (By.CSS_SELECTOR, 'div[title="Preview"]')
    page_designer_preview_floating_button = (By.CSS_SELECTOR, '.pd-preview-button')
    page_designer_container_maximize = (By.CSS_SELECTOR, 'div[data-ibx-type="pdContainer"] div[title="Maximize"]')
    page_designer_main_menu = (By.CSS_SELECTOR, '.pd-logo')
    page_designer_main_menu_close = (By.CSS_SELECTOR, 'div[data-ibx-name=miClose]')
    page_designer_warning_dialog_yes = (By.CSS_SELECTOR, '.pd-warning-dirty-yes')
    portal_designer_new_dialog_title = (By.CSS_SELECTOR, '.pvd-title')
    portal_designer_new_dialog_alias = (By.CSS_SELECTOR, '.pvd-alias')
    portal_designer_create_my_pages_menu_checkbox = (By.CSS_SELECTOR, '.pvd-pages-menu')
    portal_designer_create_button = (By.CSS_SELECTOR, '.ibx-dialog-ok-button')
    portal_designer_page_runner = (By.CSS_SELECTOR, 'div[data-ibx-type="pdPageRunner"]')
    portal_designer_run_filter = (By.CSS_SELECTOR, '.pd-header-button-filter')
    portal_designer_run_folder = (By.CSS_SELECTOR, '.ibx-accordion-page .bundle-folder-item')
    portal_designer_new_page_dialog = (By.CSS_SELECTOR, 'div[data-ibx-type="newPageFromTemplate"]')
    portal_designer_new_page_dialog_title = (By.CSS_SELECTOR, '.ibx-dialog-title-box')
    portal_designer_new_page_dialog_open_existing = (By.CSS_SELECTOR, '.np-open')
    portal_designer_new_page_dialog_select_template = (By.CSS_SELECTOR, '.np-label-select-template')
    portal_designer_new_page_dialog_template_item = (By.CSS_SELECTOR, '.np-item')
    portal_designer_new_page_dialog_template_item_grid21 = (By.CSS_SELECTOR, '.np-item:nth-child(2)')
    chart_designer_dimension_tree = (By.CSS_SELECTOR, '.wfc-mdfp-dimension-tree')
    chart_designer_dimension_tree_nodes = (By.CSS_SELECTOR, '.wfc-mdfp-dimension-tree .tnode-children')
    chart_designer_measure_tree_nodes = (By.CSS_SELECTOR, '.wfc-mdfp-measure-tree .tnode-children .ibx-label-text')
    chart_designer_search_box = (By.CSS_SELECTOR, '.wfc-mdfp-search-box input')
    chart_designer_right_click_add_to_chart = (By.CSS_SELECTOR, 'div[data-ibxp-command="idesCmdAddToChart"]')
    chart_designer_preview_xaxis_title = (By.CSS_SELECTOR, '.xaxisOrdinal-title')
    chart_designer_preview_xaxis_labels = (By.CSS_SELECTOR, 'text[class*="xaxisOrdinal-labels"]')
    chart_designer_preview_yaxis_title = (By.CSS_SELECTOR, '.yaxis-title')
    chart_designer_preview_yaxis_labels = (By.CSS_SELECTOR, 'text[class*="yaxis-labels"]')
    chart_designer_preview_risers = (By.CSS_SELECTOR, '.risers rect')  
    chart_designer_preview = (By.CSS_SELECTOR, 'div[title="Preview"]')
    chart_designer_preview_floating_button = (By.CSS_SELECTOR, '#idesToolPeviewBtn')
    chart_designer_iframe = (By.CSS_SELECTOR, '.ibx-iframe-frame')
    chart_designer_preview_default_string = (By.CSS_SELECTOR, '.drop-label .ibx-label-text')
    
class IALocators(object):
    '''this class contains reusable locators in the IA tool'''
    metadata_browser = (By.CSS_SELECTOR, '#iaMetaDataBrowser')
    preview_visualization_default_string = (By.CSS_SELECTOR, '#TableChart_1 text.title')
    preview_visualization_chart_panel = (By.CSS_SELECTOR, '.chartPanel')
    preview_visualization_xaxis_title = (By.CSS_SELECTOR, '.chartPanel .xaxisOrdinal-title')
    preview_visualization_xaxis_labels = (By.CSS_SELECTOR, '.chartPanel text[class*="xaxisOrdinal-labels"]')
    preview_visualization_yaxis_title = (By.CSS_SELECTOR, '.chartPanel .yaxis-title')
    preview_visualization_yaxis_labels = (By.CSS_SELECTOR, '.chartPanel text[class*="yaxis-labels"]')
    preview_visualization_risers = (By.CSS_SELECTOR, '.chartPanel .risers rect[tdgtitle="placeholder"]')
    save_button = (By.CSS_SELECTOR, '#saveButton')
    save_dialog = (By.CSS_SELECTOR, '#dlgIbfsOpenFile7')
    save_dialog_input_title = (By.CSS_SELECTOR, '#IbfsOpenFileDialog7_cbFileName input')
    save_dialog_save_button = (By.CSS_SELECTOR, '#IbfsOpenFileDialog7_btnOK')
    
class TextEditorLocators(object):
    '''this class contains reusable locators in the Text Editor tool'''
    ace_text_input = (By.CSS_SELECTOR, '.wf-ace-text-editor .ace_text-layer .ace_line')
    ace_text_input_line = (By.CSS_SELECTOR, '.wf-ace-text-editor .ace_text-layer .ace_line:last-child')
    ace_text_editor = (By.CSS_SELECTOR, '.wf-ace-text-editor')
    ace_text_layer = (By.CSS_SELECTOR, '.ace_text-layer')
    main_menu_button = (By.CSS_SELECTOR, 'div[data-ibx-name="_menuFile"]')
    main_menu_save_as = (By.CSS_SELECTOR, 'div[data-ibx-name="_fileSaveAs"]')
    main_menu_exit = (By.CSS_SELECTOR, 'div[data-ibx-name="_fileExit"]')
    save_dialog = (By.CSS_SELECTOR, 'div[data-ibx-type="opensavedialog2"]')
    save_dialog_input_title = (By.CSS_SELECTOR, '.sd-form-field-text-title input')
    save_dialog_save_button = (By.CSS_SELECTOR, '.ibx-dialog-ok-button')

class ServerLocators(object):
    load_button = (By.CSS_SELECTOR, 'div[qa="Load and Report"]')
    input_app_ibisamp = (By.CSS_SELECTOR, 'input[aria-label="ibisamp"]')
    input_default = (By.CSS_SELECTOR, 'input[aria-label="Text Input"]')
    console_frame = (By.CSS_SELECTOR, 'div[qa="ADPConfigured"]')
    
class WorkspaceLocators(object):
    @staticmethod
    def create_css_locator_with_text(base_string, text):
        return By.CSS_SELECTOR, base_string.format(text)
    list_view_elem = (By.CSS_SELECTOR, '.ibx-data-grid-row')
    grid_view_elem = (By.CSS_SELECTOR, '.domains-item-div > .test-item > .item-thumb-wrapper')
    list_view_title_elem = (By.CSS_SELECTOR, '.home-cell-private')
    list_view_title_elem_template = '.home-cell-private[title="{}"]'
    list_view_cell_template = '.dgrid-cell[title="{}"]'
    workspaces_crumb = (By.CSS_SELECTOR, 'div[title="Workspaces"].crumb-button')
    toolbar_set = (By.CSS_SELECTOR, '.toolbar-button-divset')
    grid_list_view_button = (By.CSS_SELECTOR, '.btn-how-view-grid')
    grid_view_controls = (By.CSS_SELECTOR, '.grid-view-controls')
    grid_view_button = (By.CSS_SELECTOR, '.grid-view-btn')
    list_view_button = (By.CSS_SELECTOR, '.list-view-btn')
    fex_context_menu = (By.CSS_SELECTOR, '.edit-menu')
    share_icon = (By.CSS_SELECTOR, '.fa-share-alt')
    share_with_others_dialog = (By.CSS_SELECTOR, '.share-with-others-dialog')
    share_with_others_search_bar = (By.CSS_SELECTOR, '.share-with-txt-search > input[role="textbox"]')
    share_with_item_template = '.sw-item-desc[title*="{}"]'
    properties_summary_box = (By.CSS_SELECTOR, '.ibx-text-area-ctrl')
    properties_title_box = (By.CSS_SELECTOR, '.properties-general-title-editbox')
    properties_ok_button = (By.CSS_SELECTOR, '.properties-general-ok-button')
    properties_cancel_button = (By.CSS_SELECTOR, '.properties-general-cancel-button')
    ibx_button_css = '.ibx-button-simple'
    ibx_text_label_css = '.ibx-label-text'
    caret_button = (By.CSS_SELECTOR, '.fa-caret-down')
    domain_items = (By.CSS_SELECTOR, '.domains-item-div')