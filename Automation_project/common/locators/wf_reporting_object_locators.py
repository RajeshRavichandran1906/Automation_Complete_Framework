from selenium.webdriver.common.by import By
class WfReportingObjectLocators(object):
    
    Appbtn = (By.CSS_SELECTOR, "#applicationButton img")
    
    '''RO-Menu'''
    menu_save = (By.CSS_SELECTOR, "#applicationMenu #optionsSaveBtn img")
    menu_save_as = (By.CSS_SELECTOR, "#applicationMenu #optionsSaveAsBtn img")
    menu_run = (By.CSS_SELECTOR, "#applicationMenu #optionsRunBtn img")
    menu_close = (By.CSS_SELECTOR, "#applicationMenu #optionsCloseBtn img")
    menu_exit = (By.CSS_SELECTOR, "#applicationMenu #appExitButton img")
    
    '''RO-ToolBar'''
    toptoolbar_new = (By.CSS_SELECTOR, "#topToolBarBox #RoToolBar #newButton img")
    toptoolbar_open = (By.CSS_SELECTOR, "#topToolBarBox #RoToolBar #openROButton img")
    toptoolbar_save = (By.CSS_SELECTOR, "#topToolBarBox #RoToolBar #saveButton img")
    toptoolbar_undo = (By.CSS_SELECTOR, "#topToolBarBox #RoToolBar #undoButton img")
    toptoolbar_redo = (By.CSS_SELECTOR, "#topToolBarBox #RoToolBar #redoButton img")
    toptoolbar_showfex = (By.CSS_SELECTOR, "#topToolBarBox #RoToolBar #showFexButton img")
    toptoolbar_run = (By.CSS_SELECTOR, "#topToolBarBox #RoToolBar #runButton img")