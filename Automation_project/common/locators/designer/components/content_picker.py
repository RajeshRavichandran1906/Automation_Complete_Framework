from selenium.webdriver.common.by import By

class ContentPicker:
    
    base_css = "div.unifiedToolTypePicker "
    section_xapth = "//div[contains(@class, 'dw-right-side-picker')]//div[normalize-space()='{}'][contains(@class,'wfc-unifiedToolTypePicker-page')]"
    section_header = (By.CSS_SELECTOR, ".ibx-accordion-page-button")
    exapnd_icon = (By.CSS_SELECTOR, base_css + "div.wfc-chartpicker-next-button .fa-arrow-left")
    collapse_icon = (By.CSS_SELECTOR, base_css + "div.wfc-chartpicker-next-button .fa-arrow-right")
    all_content_container = (By.CSS_SELECTOR, base_css + "div.wfc-unifiedToolTypePicker-collapsed-container")