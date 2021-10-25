from selenium.webdriver.common.by import By
class VfourRibbonLocators(object):
    '''Portal_V4'''
    
    Appbtn = (By.CSS_SELECTOR, "#applicationButton")
 
    '''Portal-Menu'''
    menu_NewPortal = (By.CSS_SELECTOR, "#applicationMenu div[id^='BiToolBarButton'] img[src*='new_portalv4']")
    menu_NewPage = (By.CSS_SELECTOR, "#applicationMenu div[id^='BiToolBarButton'] img[src*='new_portal_pagev4']")
    menu_OpenPortal = (By.CSS_SELECTOR, "#applicationMenu div[id^='BiToolBarButton'] img[src*='folder_opened']")
    menu_Save = (By.CSS_SELECTOR, "#applicationMenu #optionsSaveBtn")
    menu_SaveAs = (By.CSS_SELECTOR, "#applicationMenu #optionsSaveAsBtn")
    menu_Exit = (By.CSS_SELECTOR, "#applicationMenu #appExitButton")
    
    '''Portal-ToolBar'''
    toolbar_save = (By.CSS_SELECTOR, "#topToolBar #saveButton")
        
    '''Ribbon bar'''
    Layoutribbon = (By.CSS_SELECTOR, "#BIPortalRibbon #LayoutTab_tabButton")
    Insertribbon = (By.CSS_SELECTOR, "#BIPortalRibbon #InsertTab_tabButton")
    styleribbon = (By.CSS_SELECTOR, "#BIPortalRibbon #StyleTab_tabButton")
    
    '''1. Layout_Tab'''
    Layout_Navigation = (By.CSS_SELECTOR, "#LayoutTab #LayoutNavigationMenuBtn")   
    Layout_Banner = (By.CSS_SELECTOR, "#LayoutTab #LayoutBannerMenuBtn")
    Layout_MenuBar = (By.CSS_SELECTOR, "#LayoutTab #LayoutMenuBarMenuBtn")
    Layout_Theme = (By.CSS_SELECTOR, "#LayoutTab div[id^='BiToolBarSplitMenuButton']")
    Layout_Security = (By.CSS_SELECTOR, "#LayoutTab #LayoutSecurityMenuBtn")
    Layout_Properties = (By.CSS_SELECTOR, "#LayoutTab #LayoutPropertiesMenuBtn")
    Layout_Layout = (By.CSS_SELECTOR, "#LayoutTab #LayoutPage")
          
    '''2. Insert_Tab'''
    Insert_Page = (By.CSS_SELECTOR, "#InsertTab #PagesTabContentCluster")
    Insert_Panel = (By.CSS_SELECTOR, "#InsertTab #ContainersPanelMenuBtn")
    Insert_Accordion = (By.CSS_SELECTOR, "#InsertTab #ContainersAccordionMenuBtn")
    Insert_Tabbed = (By.CSS_SELECTOR, "#InsertTab #ContainersTabbedMenuBtn")
    Insert_Responsive = (By.CSS_SELECTOR, "#InsertTab #ContainersFlexMenuBtn")
    Insert_EasySelector = (By.CSS_SELECTOR, "#InsertTab #ContainersEasySelectorMenuBtn")
    Insert_WebFOCUSResources = (By.CSS_SELECTOR, "#InsertTab #InsertWFueryMenuBtn")
    Insert_Image = (By.CSS_SELECTOR, "#InsertTab #InsertImageMenuBtn")
    Insert_ResourceTree = (By.CSS_SELECTOR, "#InsertTab #InsertResTree")
    Insert_PortalList = (By.CSS_SELECTOR, "#InsertTab #InsertPortalTree")
    Insert_Text = (By.CSS_SELECTOR, "#InsertTab #othersContainersText")
    
    '''3. Style_Tab'''
    Style_Normal = (By.CSS_SELECTOR, "#StyleTab #StyleTabStateCluster")
    Style_Image = (By.CSS_SELECTOR, "#StyleTab #StateBrowseBackgroundImage")
    Style_Repeat = (By.CSS_SELECTOR, "#StyleTab #StateBackgroundRepeatBtn")
    Style_Position = (By.CSS_SELECTOR, "#StyleTab #StateBackgroundPositionBtn")
    Style_Style = (By.CSS_SELECTOR, "#StyleTab #StateBorderStyleButton")
    Style_background_color = (By.CSS_SELECTOR, "#StateBackgroundColor")
    Style_border_width_up = (By.CSS_SELECTOR, "#StateBorder div[class*='bi-spinner-up-button']")
    Style_border_color = (By.CSS_SELECTOR, "#StateBorderColor")
    Style_font_bold = (By.CSS_SELECTOR, "#StyleStateTabFontCluster #FieldFontWeight img")
    Style_font_italic = (By.CSS_SELECTOR, "#StyleStateTabFontCluster #FieldFontStyle img")
    Style_font_underline = (By.CSS_SELECTOR, "#StyleStateTabFontCluster #FieldFontUnderline img")
    Style_font_color = (By.CSS_SELECTOR, "#StyleStateTabFontCluster #FieldFontColor img")
    
    