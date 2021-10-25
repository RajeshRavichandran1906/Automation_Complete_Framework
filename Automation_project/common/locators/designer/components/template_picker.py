from selenium.webdriver.common.by import By


class TemplatePicker:
    
    base_css = "div.df-template-picker div.ibx-dialog-main-box"
    standard = "div.df-tp-list-standard"
    custom = "div.df-tp-list-custom"
    close = (By.CSS_SELECTOR, base_css + "div.ibx-title-bar-close-button")
    blank = (By.CSS_SELECTOR, standard + "div[title='Blank']")
    grid_2_1 = (By.CSS_SELECTOR, standard + "div[title='Grid 2-1']")
    grid_2_1_side = (By.CSS_SELECTOR, standard + "div[title='Grid 2-1 Side']")
    grid_3_3_3 = (By.CSS_SELECTOR, standard + "div[title='Grid 3-3-3']")
    grid_4_2_1 = (By.CSS_SELECTOR, standard + "div[title='Grid 4-2-1']")
    infoapp_1 = (By.CSS_SELECTOR, standard + "div[title='InfoApp 1']")
    workbench = (By.CSS_SELECTOR, standard + "div[title='Workbench']")