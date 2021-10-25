from selenium.webdriver.common.by import By


class Toolbar:
    
    base_css = "div.df-toolbar "
    save = (By.CSS_SELECTOR, base_css + "div[title='Save']")
    undo = (By.CSS_SELECTOR, base_css + "div[title='Undo']")
    redo = (By.CSS_SELECTOR, base_css + "div[title='Redo']")
    help = (By.CSS_SELECTOR, base_css + "div[title='Help']")
    advanced = (By.CSS_SELECTOR, base_css + "div[title='Advanced']")
    data = (By.CSS_SELECTOR, base_css + "div[title='Data tool']")
    visualization = (By.CSS_SELECTOR, base_css + "div[title='Visualization tool']")
    application_menu = (By.CSS_SELECTOR, base_css + "div.top-bar-file-menu")
    save_icon = (By.CSS_SELECTOR, "div.fa-save")
    undo_icon = (By.CSS_SELECTOR, "div.fa-undo")
    redo_icon = (By.CSS_SELECTOR, "div.fa-redo")
    help_icon = (By.CSS_SELECTOR, "div.fa-question-circle")
    advanced_icon = (By.CSS_SELECTOR, "div.ds-icon-setting")
    application_menu_dropdown_icon = (By.CSS_SELECTOR, "div.fa-caret-down")