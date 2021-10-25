from selenium.webdriver.common.by import By



class FilterToolbar:
    
    visual_filter_toolbar = (By.CSS_SELECTOR, "div[data-ibx-type='filterBar']")
    page_filter_toolbar = (By.CSS_SELECTOR, "div[data-ibx-type='pdFilterGrid']")
    field_name = (By.CSS_SELECTOR, "div[data-ibx-name='_fieldName'] div[class='ibx-label-text']")
    field_value = (By.CSS_SELECTOR, "div[data-ibx-name='_filterValue'] div[class='ibx-label-text']")