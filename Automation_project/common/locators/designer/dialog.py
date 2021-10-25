from selenium.webdriver.common.by import By

class Base:
    
    dialog = (By.CSS_SELECTOR, "div.pop-modal[role='dialog'][aria-hidden='false']")
    title = (By.CSS_SELECTOR, "div.ibx-title-bar-caption")
    close_icon = (By.CSS_SELECTOR, "div.ibx-title-bar-close-button")
    buttons = (By.CSS_SELECTOR, ".ibx-dialog-button-box .ibx-dialog-button:not([style*='none'])")
    
class ChooseTemplate(Base):
    
    dialog = (By.CSS_SELECTOR, "div.df-template-picker[role='dialog']")
    common_templates = (By.CSS_SELECTOR, "div.df-tp-list-standard>div.df-tp-item")
    custome_templates = (By.CSS_SELECTOR, "div.df-tp-list-custom>div.df-tp-item")
    
class AddContent(Base):
    
    add_content = (By.CSS_SELECTOR, "div.pd-add-content-button")
    dropdown_button = (By.CSS_SELECTOR, "div.ibx-menu-button")
    
class AddFilterControls(Base):
     
    parameter_checkbox = (By.CSS_SELECTOR, "div.pd-af-all div.ibx-check-box-simple-marker")
    parameter_option_checkbox_xpath = "//div[contains(@class, 'pd-af-list-cell')] [normalize-space()='{0}']//parent::div/preceding-sibling::div[1]/div[contains(@class,'ibx-check-box-simple-marker')]"
    parameter_control_dropdown_xpath = "//div[contains(@class, 'pd-af-list-cell')] [normalize-space()='{0}']//parent::div/following-sibling::div[3]/div[contains(@class,'pd-af-select')]/input"

class Alert(Base):
    
    buttons = (By.CSS_SELECTOR, "div.pd-warning-dirty-button")
    message = (By.CSS_SELECTOR, "pd-warning-dirty-label")
    
class ConvertControlTo(Base):
    
    convert_options = (By.CSS_SELECTOR, Base.dialog[1] + " div.pd-filter-btn:not([style*='none'])")
    
class DataSourceDialog(Base):
    
    dialog = (By.CSS_SELECTOR, "div.select-data-source[role='dialog']")
    breadcrumb = (By.CSS_SELECTOR, "div.breadcrumb-hbox div.bc-btn ")
    
    class ToolBar:
        
        workspace = (By.CSS_SELECTOR, "div.select-data-source-split-menu-button")
        filter_by_type = (By.CSS_SELECTOR, 'div[title="Filter by type"]')
        grid_view = (By.CSS_SELECTOR, 'div.ibx-sm-selectable[title="Switch to tile view"]')
        list_view = (By.CSS_SELECTOR, 'div.ibx-sm-selectable[title="Switch to list view"]')
        select_columns_displayed = (By.CSS_SELECTOR, 'div.ibx-sm-selectable[title="Select columns displayed"]')
        switch_to_flat_view = (By.CSS_SELECTOR, 'div[title="Switch to flat view"]')
        switch_to_folder_view = (By.CSS_SELECTOR, 'div[title="Switch to folder view"]')
        search = (By.CSS_SELECTOR, 'div.select-data-source-search')
    
    class GridView:
        
        files = (By.CSS_SELECTOR, 'div.domains-item-div [role="listitem"]')
        folders = (By.CSS_SELECTOR, 'div.domains-folder-div div.home-content-page-folder')
        
        
    class ListView:
        
        header = (By.CSS_SELECTOR, 'div.home-list-contents div.dgrid-header-col-bar-group')
        content = (By.CSS_SELECTOR, 'div.home-list-contents .dgrid-grid')
        rows = "div[class^='ibx-data-grid-row'] [role='gridcell'][title='{0}']"