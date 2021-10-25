from selenium.webdriver.common.by import By
class WfAlertAssistLocators(object):
    
    Appbtn = (By.CSS_SELECTOR, "#applicationButton img")
    
    '''AA-Menu'''
    menu_save = (By.CSS_SELECTOR, "#applicationMenu #optionsSaveBtn img")
    menu_save_as = (By.CSS_SELECTOR, "#applicationMenu #optionsSaveAsBtn img")
    menu_run = (By.CSS_SELECTOR, "#applicationMenu #optionsRunBtn img")
    menu_close = (By.CSS_SELECTOR, "#applicationMenu #optionsCloseBtn img")
    menu_exit = (By.CSS_SELECTOR, "#applicationMenu #appExitButton img")
    
    '''AA-ToolBar'''
    toptoolbar_new = (By.CSS_SELECTOR, "#topToolBarBox #AAToolBar #toolbarNewButton img")
    toptoolbar_open = (By.CSS_SELECTOR, "#topToolBarBox #AAToolBar #toolbarOpenAAButton img")
    toptoolbar_save = (By.CSS_SELECTOR, "#topToolBarBox #AAToolBar #toolbarSaveButton img")
    toptoolbar_undo = (By.CSS_SELECTOR, "#topToolBarBox #AAToolBar #toolbarUndoButton img")
    toptoolbar_redo = (By.CSS_SELECTOR, "#topToolBarBox #AAToolBar #toolbarRedoButton img")
    toptoolbar_showfex = (By.CSS_SELECTOR, "#topToolBarBox #AAToolBar #toolbarShowFexButton img")
    toptoolbar_run = (By.CSS_SELECTOR, "#topToolBarBox #AAToolBar #toolbarRunButton img")