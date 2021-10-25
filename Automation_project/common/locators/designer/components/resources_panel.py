from selenium.webdriver.common.by import By

RESOURCE = (By.CSS_SELECTOR, "div.resource-container-box ")

class Fields:
    
    dimension_section = (By.CSS_SELECTOR, RESOURCE[1] + ".dimension-tree-box")
    measure_section = (By.CSS_SELECTOR,  RESOURCE[1] + ".measure-tree-box")
    variables_section = (By.CSS_SELECTOR,  RESOURCE[1] + ".wfc-mdfp-variables-tree")
    search_textbox = (By.CSS_SELECTOR,  RESOURCE[1] + ".wfc-mdfp-search input[type='search']")
    tab_buttons = (By.CSS_SELECTOR,  RESOURCE[1] +".ibx-tab-button")
    section_menu_button = (By.CSS_SELECTOR, ".md-split-box-menu-btn")

class Content:
    
    items = (By.CSS_SELECTOR,  RESOURCE[1] + "div.ibx-tree-browser-node>div.tnode-label")
    
class BasicContainers:
    
    containers = (By.CSS_SELECTOR,  "div.ibxtool-panel-basic-containers div.ds-draggable-button")

class Outline:
    
    tree_xpath = "//div[@data-ibx-type='dfOutlineTreeNode']//div[normalize-space()='{}'][@role='treeitem']"
    child_tree_xpath = "/following-sibling::div//div[normalize-space()='{}'][@role='treeitem']"
    exapnd_icon = (By.CSS_SELECTOR, "div.tnode-btn-collapsed")
    collapse_icon = (By.CSS_SELECTOR, "div.tnode-btn-expanded")
    tree_items_label = (By.CSS_SELECTOR, "div.ibx-tree-node div.tnode-label")
    
class Filters:
    
    add_all_filters_to_page = (By.CSS_SELECTOR, RESOURCE[1] + "div.df-filters-add-all")
    filter_options = (By.CSS_SELECTOR, "[data-ibx-type='dfFiltersTree'] div[role*='tree'] div.ibx-label-text")
    
    
    
    