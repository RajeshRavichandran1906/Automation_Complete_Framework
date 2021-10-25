from selenium.webdriver.common.by import By
class VisualizationMetadataLocators(object):
    
    ''' Data Pane '''
    data_pane = (By.ID,"iaMetaDataBrowser")
    SearchField = (By.CSS_SELECTOR, 'input#metaDataSearchTxtFld')
    Selected_Field = (By.XPATH, '//*[contains(@class,"selected")]/td')
    '''Add Fields'''
    Selected_Field_text = (By.XPATH, '//*[contains(@class,"selected")]/td')
    Selected_Field_image = (By.XPATH, '//*[contains(@class,"selected")]/td/img[2]')
    Initial_RC_Menu = (By.XPATH, "//div[contains(@style,'inherit')]/div/table/tbody/tr[*]/td[contains(text(),'Sum')]")
    Selected_RC_Menu = (By.XPATH, '//div[contains(@style,"inherit")]/div/table/tbody/tr[contains(@bi-moz-focused,"true")]/td[2]')
    Initial_RC_Submenu_img = (By.XPATH, "//div[contains(@style,'inherit')]/div/table/tbody/tr[*]/td[contains(text(),'Color')]/../td/img")
    Initial_RC_Submenu_Grid_img = (By.XPATH, "//div[contains(@style,'inherit')]/div/table/tbody/tr[*]/td[contains(text(),'Rows')]/../td/img")
    Selected_RC_Submenu = (By.XPATH, '//div[contains(@style,"inherit")]/div/table/tbody/tr[contains(@bi-moz-focused,"true")]/td[2]')
    
    
    '''Query Pane > Locators saved here'''
    query_pane = (By.ID, 'queryBoxColumn')
    field_querypane = '//div[(@id="queryTreeColumn")]//td[.="{0}"]//img[2]'
    
    querycolumn = (By.XPATH, "//*[@id='queryTreeColumn']/*[@class='bi-tree-view-body-content']/table/tbody") 
    
    '''Filter pane Range > Locators  saved here'''
    range_operatorDropdown = (By.XPATH, "//div[contains(@id,'avOperatorComboBox')]/div/div[2]")
    changeOperator_GT_orequalto = (By.XPATH, "//*[contains(text(),'Greater than or equal to')]")
    changeOperator_LT_orequalto = (By.XPATH, "//*[contains(text(),'Less than or equal to')]")
    changeOperator_Range = (By.XPATH, "//*[contains(text(),'Range')]")
    sort_Asc = (By.XPATH, "//div[contains(text(),'Ascending')]")
    From = (By.XPATH, "//div[contains(@id,'avfFromValue')]/input")
    Starting_Date = (By.XPATH,"//div[contains(text(),'Starting Date')]/../div/input")
    Ending_Date = (By.XPATH,"//div[contains(text(),'Ending Date')]/../div/input")
    searchBox = (By.ID, 'avSearchValueText')
    operatorDropdown = (By.XPATH, "//div[contains(@id,'avAlphaOperatorComboBox')]/div/div[2]")
    changeOperator_notequal = (By.XPATH, "//*[contains(text(),'Not equal to')]")
    changeOperator_equal = (By.XPATH, "//*[contains(text(),'Equal to')]")
    sortDropdown = (By.XPATH, "//div[contains(@id,'avfSortValuesComboBox')]/div/div[2]")
    sortOption = (By.XPATH, "//div[contains(text(),'Descending')]")
    uncheckShowPrompt = (By.XPATH, "//div[contains(@id,'avFilterShowPrompt')]/input")
    clickOK = (By.CSS_SELECTOR, '#avFilterOkBtn')
    filter_pane_right_click_menus = '//td[contains(text(),"{0}")]'
    filterPane = (By.ID, 'qbFilterWindow')
    aggregationComboBox = (By.XPATH, "//div[contains(@id,'avAggregationComboBox')]/div/div[2]")
    count = (By.XPATH, "//div[starts-with(@id,'BiPopup')]/div/div[contains(text(),'Count')]")
    distinct_count = (By.XPATH, "//div[starts-with(@id,'BiPopup')]/div/div[contains(text(),'Distinct Count')]")
    aggregation_val = "//*[contains(text(), '{0}') and starts-with(@id,'BiComboBoxItem')]"
    cancel_filter = (By.ID, 'avFilterCancelBtn')
    filterpane_scroll = (By.XPATH, '//*[@class="bi-scroll-bar scroll-bar-vertical"]//div[starts-with(@id, "BiMoveHandle")]')
