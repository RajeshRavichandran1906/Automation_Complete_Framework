'''
Created on Apr 08, 2019

'''
from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    '''this class contains reusable locators on the signin page'''
    uid = (By.ID,'SignonUserName')
    pwd = (By.ID, 'SignonPassName')
    submit= (By.ID, 'SignonbtnLogin')
    
class ParisHomeLocators(object):
    '''This class contains reusable locators on the Paris (8207) Homepage'''
    
    @staticmethod
    def create_xpath_locator_with_text(base_string, text):
        return By.XPATH, base_string.format(str(text))
    
    workspaces_button = (By.CSS_SELECTOR, '.workspaces-button')
    application_button = (By.XPATH, "//div[@data-ibx-type='ibxTabButton' and div[contains(text(), 'Application')]]")
    refresh_button = (By.XPATH, "//div[@data-ibx-type='ibxButtonSimple' and contains(@title, 'Refresh')]")
    view_button = (By.CSS_SELECTOR, '.toolbar-button-div:first-child')
    visualize_data_button = (By.XPATH, "//div[contains(@data-ibx-type, 'ibxButtonSimple') and div[contains(text(), 'Visualize Data')]]")
    plus_sign_button = (By.XPATH, "//div[@data-ibx-type='ibxMenuButton' and div[contains(@class, 'fa-plus')]]")
    plus_sign_menu_template = "//div[@data-ibxp-user-value='{}']"
    workspaces_iframe = (By.CSS_SELECTOR, '.ibx-iframe-frame')
    folder_tree = (By.CSS_SELECTOR, ".ibfs-tree")
    tree_folder_xpath_template = "//div[contains(@class, 'home-tree-node') and div[contains(text(), '{}')]]"
    content_folder_xpath_template = "//div[contains(@class, 'folder-item') and div/div/div[contains(text(), '{}')]]" 
    content_file_xpath_template = "//div[contains(@class, 'file-item') and div/div/div[contains(text(), '{}')]]"
    content_file_xpath_ibfs_path_template = "//div[@data-ibfs-path='{}']"
    portal_button = (By.CSS_SELECTOR, "div[data-ibxp-text='Portal']")
    title_in_dialog = (By.XPATH, "//div[@data-ibx-name='sdInputDivType' and div/div[contains(text(), 'Title')]]/div[@data-ibx-type='ibxTextField']/input")
    theme_in_dialog = (By.XPATH, "//div[@data-ibx-name='sdInputDivType' and div/div[contains(text(), 'Theme')]]/div[@data-ibx-type='ibxSelect']")
    light_theme_option_in_dialog = (By.XPATH, "//div[contains(@class, 'pop-top')]//div[contains(text(), 'Light')]")
    create_my_page_checkbox_in_dialog = (By.XPATH, "//div[@data-ibx-type='ibxCheckBoxSimple' and div[contains(text(), 'Create My Pages')]]/div[contains(@class, 'ibx-check-box-simple-marker')]")
    create_button_in_dialog = (By.XPATH, "//div[contains(@class, 'ibx-dialog-ok-button') and div[contains(text(), 'Create')]]")
    dropable_area = (By.CSS_SELECTOR, ".files-box.ibx-external-drop-target")
    publish_context_button = (By.CSS_SELECTOR, "div[data-ibx-command='cmdPublish']")
    copy_context_button = (By.CSS_SELECTOR, "div[data-ibx-command='cmdCopy']")
    open_context_button = (By.CSS_SELECTOR, "div[action='list']")
    delete_context_button = (By.CSS_SELECTOR, "div[data-ibxp-command='cmdDelete']")
    paste_context_button = (By.CSS_SELECTOR, "div[data-ibxp-command='cmdPaste']")
    run_context_button = (By.CSS_SELECTOR, "div[data-ibxp-command='cmdRun']")
    edit_context_button = (By.CSS_SELECTOR, "div[data-ibxp-command='cmdEdit']")
    delete_ok_button = (By.XPATH, "//div[@data-ibx-type='ibxDialog']//div[@data-ibx-name='btnOK']")
    current_popup_dialog = (By.CSS_SELECTOR, "div[data-ibx-type='ibxDialog']")
    fex_xpath_template = "//div[contains(@class, 'file-item')]//div[contains(text(),'{}')]"
    
class DesignerLocators(object):
    '''this class contains reusable locators on the designer page'''
    
    @staticmethod
    def create_container_xpath_with_coordinate(x, y, base_xpath):
        return By.XPATH, base_xpath.format(x=str(x), y=str(y))
    
    designer_add_data_button = (By.CSS_SELECTOR, '.btn-add-data')
    designer_screen_header = (By.CSS_SELECTOR, '.df-screen-header')
    select_data_source = (By.CSS_SELECTOR, "div[data-ibxp-command='dfCmdAddData']")
    data_source_select_button = (By.XPATH, "//div[@data-ibx-type='selectdatasource']//div[@data-ibx-name='btnOK']")
    data_source_workspace_button = (By.XPATH, "//div[@data-ibx-type='selectdatasource']//div[@data-ibx-type='ibxMenuButton']")
    data_source_search_input = (By.XPATH, "//div[contains(@class, 'select-data-source-search')]/input")
    data_source_master_grid = (By.CSS_SELECTOR, "div[data-ibx-type='ibxDataGrid']")
    data_source_workspace_template = "//div[contains(@class, 'select-data-source-menu-item') and div/div[contains(text(), '{}')]]"
    data_source_master_template = "//div[contains(@data-ibfs-path, '{}.mas')]"
    data_source_title = (By.CSS_SELECTOR, "div[data-ibx-name='masterButton'] > div[class*='ibx-label-text']")
    eda_source_workspace_template = "//div[@title='{}']"
    designer_preview_timer = (By.CSS_SELECTOR, "div[data-ibx-type='previewTimer']")
    designer_search_box = (By.CSS_SELECTOR, '.wfc-mdfp-search-box input')
    designer_search_button = (By.CSS_SELECTOR, '.wfc-mdfp-search-btn')
    designer_dimension_tree = (By.CSS_SELECTOR, '.wfc-mdfp-dimension-tree')
    designer_measure_tree = (By.CSS_SELECTOR, '.wfc-mdfp-measure-tree')
    designer_filter_bar = (By.XPATH, "//div[div[@data-ibx-type='filterBar']]")
    designer_field_name_xpath_template = "//div[@data-ibx-type='mdTreeNode' and contains(@title, 'Title: {}')]"
    designer_dimension_tree_nodes = (By.CSS_SELECTOR, '.wfc-mdfp-dimension-tree .tnode-children')
    designer_measure_tree_nodes = (By.CSS_SELECTOR, '.wfc-mdfp-measure-tree .tnode-children .ibx-label-text')
    designer_right_click_add_to_chart = (By.CSS_SELECTOR, 'div[data-ibxp-command="idesCmdAddToChart"]')
    designer_bucket_xpath_template = "//div[contains(@class, 'pd-table-builder') and not(contains(@style,'display: none'))]//div[@data-ibx-type='bucket' and div/div/div[contains(text(), '{}')]]"#/div[@data-ibx-name='bucketPills']"
    designer_filter_bucket_xpath_template = "//div[contains(@class, 'pd-table-builder') and not(contains(@style,'display: none'))]//div[@data-ibx-type='filterBucket' and div/div/div[contains(text(), '')]]"
    designer_chart_type_expand_collapse = (By.CSS_SELECTOR, '.wfc-chartpicker-next-button')
    designer_chart_type_template = "//div[@data-ibx-name = 'uttpExtendedContainer']//div[@data-ibx-type='ibxButton' and contains(@title,'{}')]"
    designer_add_viz_button = (By.CSS_SELECTOR, "div[data-ibxp-command='dfCmdContentVisualization']")
    designer_convert_to_page_button = (By.CSS_SELECTOR, "div[data-ibxp-command='dfCmdContentPage']")
    designer_filter_button = (By.CSS_SELECTOR, "div[title='Add all filters to page']")
    designer_page_header = (By.CSS_SELECTOR, "div[data-ibx-name='_header']")
    designer_page_box = (By.CSS_SELECTOR, "div[data-ibx-type='pdPage']")
    designer_popup = (By.CSS_SELECTOR, "div[data-ibx-type='ibxDialog']")
    designer_popup_ok_btn = (By.XPATH, "//div[@data-ibxp-text='OK']")
    designer_popup_cancel_btn = (By.CSS_SELECTOR, "div[data-ibxp-text='Cancel']")
    designer_save_dialog = (By.CSS_SELECTOR, "div[data-ibx-type='opensavedialog2']")
    designer_save_dialog_breadcrumb_template = "//div[@data-ibx-type='ibxButtonSimple']/div[contains(@class, 'ibx-label-text') and contains(text(), '{}')]"
    designer_save_dialog_folder_template = "//div[@data-ibx-type='ibxLabel']/div[contains(@class, 'ibx-label-text') and contains(text(), '{}')]"
    designer_preview = (By.CSS_SELECTOR, ".wfc-bc-output-div")
    designer_save_button = (By.CSS_SELECTOR, "div[data-ibxp-command='dfCmdSave'][role='button']")
    save_file_title = (By.CSS_SELECTOR, "div[data-ibx-name='sdtxtFileTitle'] input")
    designer_container_coordinate_template = "//div[contains(@class, 'ui-draggable') and @data-gs-x={x} and @data-gs-y={y}]"
    designer_container_name_template = "//div[contains(@class, 'ui-draggable')]//div[contains(text(), '{}')]"
    designer_container_context_delete = (By.CSS_SELECTOR, "div[data-ibx-name='miDelete']")
    designer_format_tab_button = (By.XPATH, "//div[contains(@class, 'ibx-tab-button')]/div[contains(text(), 'Format')]")
    designer_format_theme = (By.CSS_SELECTOR, ".pd-ps-page-theme")
    designer_style_option_xpath_template = "//div[@data-ibx-type='ibxPopup' and contains(@class, 'pop-top')]//div[contains(text(),'{}')]"
    designer_format_container_style_xpath_template = "//div[@data-ibx-type='ibxRadioButton']/div[contains(text(), '{}')]"
    designer_format_container_theme = (By.XPATH, "//div[@data-ibx-name='formatTab' and contains(@class, 'tpg-selected')]//div[@data-ibx-name='chartThemeSelector']")
    designer_format_container_content = (By.XPATH, "//*[local-name()='g' and contains(@class, 'chartPanel')]")
    designer_cloud_chart_first_text = (By.CSS_SELECTOR, "g[class*='groupPanel'] > text")
    designer_logo_button = (By.CSS_SELECTOR, "div[title='WebFOCUS Designer']")
    designer_save_as_menu_option = (By.CSS_SELECTOR, "div[data-ibxp-command='dfCmdSaveAs'][role='menuitem']")
    designer_close_menu_option = (By.CSS_SELECTOR, "div[data-ibxp-command='dfCmdExit'][role='menuitem']")
    designer_template_option_xpath_template = "//div[contains(@class, 'df-tp-item') and @title='{}']"
    designer_folder_nav_xpath_template = "//div[contains(@class,'tnode-root')]/div[@role='treeitem']/div[contains(text(), '{}')]"
    designer_content_nav_xpath_template = "//div[contains(@class,'tnode-children')]/div[@data-ibx-type='pdTreeBrowserNode']/div[div[contains(text(), '{}')]]"
    designer_content_container_xpath_template = "//div[@data-ibx-type='pdContainer' and div/div/div[contains(text(), '{}')]]/div[contains(@class, 'pd-container-content')]"
    designer_filter_grid = (By.CSS_SELECTOR, "div[data-ibx-type='pdFilterGrid']")
    designer_filter_dropdown = (By.CSS_SELECTOR, ".pd-filter-panel-content")

class DialogLocators(object):
    folder_breadcrumb_template = "//div[@data-ibx-type='ibxButtonSimple']/div[contains(@class, 'ibx-label-text') and contains(text(), '{}')]"
    folder_template = "//div[contains(@class, 'folder-div') and div/div[contains(@class, 'ibx-label-text') and contains(text(), '{}')]]"
    dialog_item_template = "//div[contains(@class, 'file-item') and div/div/div[contains(text(), '{}')]]"        
    title_textbox = (By.CSS_SELECTOR, "div[data-ibx-name='sdtxtFileTitle'] input")
    dialog_popup = (By.CSS_SELECTOR, "div[data-ibx-type='ibxDialog']")
    ok_btn = (By.XPATH, "//div[@data-ibxp-text='OK']")
    cancel_btn = (By.CSS_SELECTOR, "div[data-ibxp-text='Cancel']")
        
class PortalRuntimeLocators(object):
    
    page_name_xpath_template = "//div[contains(@class, 'bundle-folder-item') and div[contains(text(), '{}')]]"
    page_add_plus_sign = (By.CSS_SELECTOR, ".bundle-folder-pgbuilder")
    link_to_exiting_page = (By.XPATH, "//div[@data-ibx-type='ibxButton' and div[contains(text(), 'Link to an existing page')]]")
    page_container = (By.XPATH, "//div[contains(@class, 'wfc-bc-output-div')]")
    page_container_content = (By.XPATH, "//*[local-name()='g' and contains(@class, 'chartPanel')]")
