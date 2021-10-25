from selenium.webdriver.common.by import By
class BIPDesignRibbonLocators(object):
    
    Appbtn = (By.CSS_SELECTOR, "#applicationButton img")
    
    tab_css="#BIPortalRibbon #{0}Tab_tabButton" 
    
    
    ''' Series '''
    marker_options = "// *[contains(text(), '{0}')]"
    series_marker = (By.CSS_SELECTOR, "#SeriesChartMarker img")
    
    '''Quick Access Toolbar'''
    error_message = (By.CSS_SELECTOR, '#MAINTABLE_messageContainer_text1 > table:nth-child(1) > tbody > tr > td:nth-child(2) > div > pre > h5')
    error_message_close = (By.CSS_SELECTOR, '#MAINTABLE_messageContainer_menu1 > div > div > img')
   
    '''BIP-Menu'''
    menu_save = (By.CSS_SELECTOR, "#applicationMenu #optionsSaveBtn img")
    menu_exit = (By.CSS_SELECTOR, "#applicationMenu #appExitButton img")
    
    '''IA-ToolBar'''
    toolbar_save = (By.CSS_SELECTOR, "#topToolBar #saveButton img")
    
    '''1. Layout'''
    '''Portal'''
    layout_navigation = (By.CSS_SELECTOR, "#LayoutNavigationMenuBtn div[class$='drop-down-arrow']")
    layout_banner = (By.CSS_SELECTOR, "#LayoutBannerMenuBtn div[class$='drop-down-arrow']")
    layout_menubar = (By.CSS_SELECTOR, "#LayoutMenuBarMenuBtn div[class$='drop-down-arrow']")
    layout_theme = (By.CSS_SELECTOR, "#LayoutTab img[src*='images/report_themes']")
    layout_security = (By.CSS_SELECTOR, "#LayoutSecurityMenuBtn img")
    layout_properties = (By.CSS_SELECTOR, "#LayoutPropertiesMenuBtn img")
    '''Page & Banner'''
    layout_layout = (By.CSS_SELECTOR, "#LayoutPageLayoutMenuBtn div[class$='drop-down-arrow']")
    
    '''2. Insert'''
    '''Pages'''
    insert_page = (By.CSS_SELECTOR, "#PagesTabContentCluster img[src*='new_portal_pagev4']")
    '''Containers'''
    insert_panel = (By.CSS_SELECTOR, "#ContainersTabContentCluster #ContainersPanelMenuBtn img")
    insert_accordion = (By.CSS_SELECTOR, "#ContainersTabContentCluster #ContainersAccordionMenuBtn img")
    insert_tabbed = (By.CSS_SELECTOR, "#ContainersTabContentCluster #ContainersTabbedMenuBtn img")
    insert_responsive = (By.CSS_SELECTOR, "#ContainersTabContentCluster #ContainersFlexMenuBtn img")
    insert_easyselector = (By.CSS_SELECTOR, "#ContainersTabContentCluster #ContainersEasySelectorMenuBtn img")
    '''Content'''
    insert_webfocusresource = (By.CSS_SELECTOR, "#InsertTabContentCluster #InsertWFueryMenuBtn img")
    insert_image = (By.CSS_SELECTOR, "#InsertTabContentCluster #InsertImageMenuBtn img")
    insert_resourcetree = (By.CSS_SELECTOR, "#InsertTabContentCluster #InsertResTree img")
    insert_portallist = (By.CSS_SELECTOR, "#InsertTabContentCluster #InsertPortalTree img")
    insert_text = (By.CSS_SELECTOR, "#InsertTabContentCluster #othersContainersText img")
    
    '''3. Style'''

    
    
    