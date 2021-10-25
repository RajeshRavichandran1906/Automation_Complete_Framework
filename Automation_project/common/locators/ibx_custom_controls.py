from selenium.webdriver.common.by import By

class ibxCheckBoxSimple:
    
    checkbox    =   (By.CSS_SELECTOR, "[data-ibx-type='ibxCheckBoxSimple'][role='checkbox']:not([style*='none'])")
    marker      =   (By.CSS_SELECTOR, ".ibx-check-box-simple-marker")
    
    
class ibxRadioButtonSimple:
    
    radio_button    =   (By.CSS_SELECTOR, "div[data-ibx-type='ibxRadioButtonSimple'][role='radio']")
    marker          =   (By.CSS_SELECTOR, ".ibx-radio-button-simple-marker")
    

class ibxTree:
    
    tree_xpath = "//div[@data-ibx-type='mdTree']//div[normalize-space()='{}'][@role='treeitem']"
    child_tree_xpath = "/following-sibling::div//div[normalize-space()='{}'][@role='treeitem']"
    exapnd_icon = (By.CSS_SELECTOR, "div.tnode-btn-collapsed")
    collapse_icon = (By.CSS_SELECTOR, "div.tnode-btn-expanded")
    tree_items_label = (By.CSS_SELECTOR, "div.ibx-tree-node div.tnode-label")


class ContextMenu:
    
    context_menu = (By.CSS_SELECTOR, 'div[role="menu"] ')
    options = (By.CSS_SELECTOR, context_menu[1] + 'div[role*="menuitem"] ')
    option_labels = (By.CSS_SELECTOR, options[1] + ".ibx-label-text")


class ibxSelectItemList:
    
    item_list = (By.CSS_SELECTOR, "div[data-ibx-type='ibxSelectItemList']")
    options = (By.CSS_SELECTOR, item_list[1] + " div[data-ibx-type*='ibxSelect")
    multiselect_options = (By.CSS_SELECTOR, item_list[1] + " div[data-ibx-type='ibxSelectCheckItem']")


class ibxAccordionPage:
    
    accordion_pages = (By.CSS_SELECTOR, "div[data-ibx-type='ibxAccordionPage'] ")
    button = (By.CSS_SELECTOR, "div.ibx-accordion-page-button")
    labels = (By.CSS_SELECTOR, accordion_pages[1] + "div.ibx-accordion-button-text")
    

class ibxAccordionPane:
    
    accordion_panes = (By.CSS_SELECTOR, "div[data-ibx-type='ibxVAccordionPane'] ")
    button = (By.CSS_SELECTOR, "div.ibx-accordion-button")
    labels = (By.CSS_SELECTOR, accordion_panes[1] + "div.ibx-accordion-button-text")
    
    
class ibxCheckBox:
    
    checkbox = (By.CSS_SELECTOR, 'div[data-ibx-type="ibxCheckBox"][role="checkbox"]:not([style*="none"]) ')
    
    
class ibxRadioButton:

    radio_button = (By.CSS_SELECTOR, 'div[data-ibx-type="ibxRadioButton"][role="radio"]:not([style*="none"]) ')
    
    
class ibxDualListBox:
    
    dual_list_box = (By.CSS_SELECTOR, "div[data-ibx-type='dualListBox'] ")
    add_items = (By.CSS_SELECTOR, dual_list_box[1] + "div[data-ibx-name='wfcAddItems']")
    remove_items = (By.CSS_SELECTOR, dual_list_box[1] + "div[data-ibx-name='wfcRemoveItems']")
    all_options_side_rows = (By.CSS_SELECTOR, dual_list_box[1] + "div[class*='options-area'] [data-ibx-name='wfcSingleListBoxList'] div.ibx-data-grid-row")
    all_option_area_row_checkbox = (By.CSS_SELECTOR, dual_list_box[1] + " div.row-checkbox")
    
    
class ibxSpinner:
    
    spinner_box = (By.CSS_SELECTOR, '[data-ibx-type="ibxSpinner"] ')
    text_box = (By.CSS_SELECTOR, spinner_box[1] + 'input.ibx-spinner-text-input[role="spinbutton"] ')
    up_button = (By.CSS_SELECTOR, spinner_box[1] + 'div.ibx-spinner-btn-up ')
    down_button = (By.CSS_SELECTOR, spinner_box[1] + 'div.ibx-spinner-btn-down ')
    
    
class bucket:
    
    bucket = (By.CSS_SELECTOR, "div.pd-table-builder:not([style*='none']) div[data-ibx-type='bucket'] ") 
    bucket_ellipsis = (By.CSS_SELECTOR, bucket[1] + "div.wfc-bucket-popup-btn ")
    fields_area = (By.CSS_SELECTOR, bucket[1] + "div[data-ibx-name='bucketPills'] ")
    field_pill = (By.CSS_SELECTOR, bucket[1] + "div[data-ibx-type='bucketPill'] ")
    field_axis_icon = (By.CSS_SELECTOR, field_pill[1] + "div[data-ibx-name='fieldPillButton'] ")
    field_sort_icon = (By.CSS_SELECTOR, field_pill[1] + "div[data-ibx-name='fieldPillSortButton'] ")
    field_label = (By.CSS_SELECTOR, field_pill[1] + "div[data-ibx-name='pillLabel'] ")
    field_delete_icon = (By.CSS_SELECTOR, field_pill[1] + "div.ds-icon-close ")
    left_axis_icon = '"\ue9cf"'
    left_axis = (By.CSS_SELECTOR, "div.ds-icon-y-axis")
    right_axis_icon = '"\ueae8"'
    right_axis = (By.CSS_SELECTOR, "div.ds-icon-right-left")
    bottom_axis_icon = '"\ue9ce"'
    bottom_axis = (By.CSS_SELECTOR, "div.ds-icon-x-axis")
    top_column_icon = '"\ue9d7"'
    top_column = (By.CSS_SELECTOR, "div.ds-icon-columns")
    sort_ascending_icon = '"\uea63"'
    sort_ascending = (By.CSS_SELECTOR, "div.ds-icon-ascending")
    sort_decending_icon = '"\uea64"'
    sort_decending = (By.CSS_SELECTOR, "div.ds-icon-descending")    
    
    