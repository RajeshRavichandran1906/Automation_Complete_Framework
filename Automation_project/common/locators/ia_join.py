from selenium.webdriver.common.by import By

PARENT_ID = "#dlgJoin"

class Header :
    
    Caption     = (By.CSS_SELECTOR, PARENT_ID + ">.window-active>.window-caption")
    
class TopToolBar :
    
    AddNew      = (By.ID, "dlgJoin_btnAddMaster")
    Edit        = (By.ID, "dlgJoin_btnEditJoin")
    Remove      = (By.ID, "dlgJoin_btnDeleteJoin")
    Filter      = (By.ID, "dlgJoin_btnEditWhere")
    View        = (By.ID, "dlgJoin_btnToggleView")
    IndexOnly   = (By.ID, "dlgJoin_btnFilterIndex")
    Blend       = (By.ID, "dlgJoin_btnJoinBlend")

class Canvas :
    
    JoinPanels      = (By.CSS_SELECTOR, PARENT_ID + " [id^='JoinPanel']")
    JoinPanelsTitle = (By.CSS_SELECTOR, JoinPanels[1] + " .window-caption")
    JoinFields      = (By.CSS_SELECTOR, ".bi-tree-view-table>tbody>tr>td")
    
class BottomToolBar :
    
    Ok      = (By.ID, "dlgJoin_btnOK")
    Cancel  = (By.ID, "dlgJoin_btnCancel")
    