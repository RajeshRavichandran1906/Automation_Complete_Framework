from selenium.webdriver.common.by import By

class AsRibbonLocators(object):  
    tab_css="#IaToolbar #{0}Tab_tabButton" 
        
    '''Quick Access Toolbar (qat)'''
    qat_open = (By.NAME, ' ')
    qat_save = (By.NAME, 'Save')
    qat_save_all = (By.NAME, ' ')
    qat_undo = (By.NAME, ' ')
    qat_redo= (By.NAME, ' ')
    qat_cut= (By.NAME, ' ')
    qat_copy= (By.NAME, ' ')
    qat_paste= (By.NAME, ' ')
    qat_run= (By.NAME, ' ')
    
    '''AS-Application-Menu'''
    as_image=(By.NAME, 'Application Menu')
    as_menu_open =  (By.NAME, ' ')
    as_menu_save = (By.NAME, ' ')
    as_menu_save_as =  (By.NAME, ' ')
    as_menu_save_all =  (By.NAME, ' ')
    as_menu_run =  (By.NAME, ' ')
    as_menu_print= (By.NAME, ' ')
    as_menu_close =  (By.NAME, ' ')
    as_menu_options =  (By.NAME, ' ')
    as_menu_exit =  (By.NAME, ' ')
    
      
    ''''1. Home_Tab'''
    
    '''content'''
    home_data = (By.NAME, 'Data')
    home_report = (By.NAME, 'Report')
    home_chart = (By.NAME, 'Chart')
    home_html_document = (By.NAME, 'HTML / Document')

    '''utilities'''
    home_environments = (By.NAME, 'Environments')
    home_commandconsole = (By.NAME, 'Command Console')
        
    '''view'''
    home_environmentstree = (By.NAME, 'Environments Tree')
    home_environmentsdetail = (By.NAME, 'Environments Detail')
    home_filefolder = (By.NAME, 'File/Folder Properties')
    home_procedureview = (By.NAME, 'Procedure View')
    home_contextbar = (By.NAME, 'Context Bar')
    home_statusbar = (By.NAME, 'Status Bar')
    home_helpwizard = (By.NAME, 'Help Wizard')
    
    '''window'''
    home_windows = (By.NAME, 'Windows')
    
    '''2. HTML_Components_Tab'''
    
    '''Reports'''
    components_report = (By.NAME,'Report')
    components_chart = (By.NAME,'Chart')
 
    '''Generic elements'''
    components_image = (By.NAME,'Image')
    components_hyperlink = (By.NAME,'Hyperlink')
    components_button = (By.NAME,'Button')
    components_reset = (By.NAME,'Reset')
    components_saveselection = (By.NAME,'Save Selection')
    components_label = (By.NAME,'Label')
    components_text = (By.NAME,'Text')
    components_line = (By.NAME,'Line')
    components_menu = (By.NAME,'Menu"')
    components_table = (By.NAME,'Table')
    components_grid = (By.NAME,'Grid')
    
    '''containers'''
    components_form = (By.NAME,'Form')
    components_tab = (By.NAME,'Tab')
    components_accordion = (By.NAME,'Accordion')
    components_window = (By.NAME,'Window')
    components_outputwidget = (By.NAME,'Output Widget')
    components_maintaindataapp = (By.NAME,'Maintain Data App Window')
    components_groupbox = (By.NAME,'Group Box')
    components_panel = (By.NAME,'Panel')
    
    '''objects'''
    components_frame = (By.NAME,'Frame')
    components_flash = (By.NAME,'Flash')
    components_map = (By.NAME,'Map')
    components_gisflexviewer = (By.NAME,'GIS Flex Viewer...')
    components_html = (By.NAME,'HTML')
    components_esri_map=(By.NAME, 'ESRI Map')
    
    '''Controls '''
    controls_editbox = (By.NAME,'Edit Box')
    controls_hidden = (By.NAME,'Hidden')
    controls_dropdown = (By.NAME,'Drop Down')
    controls_listbox = (By.NAME,'List Box')
    controls_doublelist = (By.NAME,'Double list')
    controls_radiobutton = (By.NAME,'Radio Button')
    controls_checkbox = (By.NAME,'Check Box')
    controls_textarea = (By.NAME,'Text Area')
    controls_tree = (By.NAME,'Tree')
    controls_calendar = (By.NAME,'Calendar')
    controls_slider = (By.NAME,'Slider')
    
    '''Positioning (HTML\Document both contains same ribbons)''' 
    positioning_left = (By.NAME,'Left')
    positioning_right = (By.NAME,'Right')
    positioning_top = (By.NAME,'Top')
    positioning_bottom = (By.NAME,'Bottom')
    positioning_center = (By.NAME,'Center')
    positioning_middle = (By.NAME,'Middle')
    positioning_samewidth = (By.NAME,'Same Width')
    positioning_sameheight = (By.NAME,'Same Height')
    positioning_samesize = (By.NAME,'Same Size')
    positioning_togglesgrid = (By.NAME,'Toggles Grid')
    positioning_draganddrop = (By.NAME,'Drag and Drop')
    positioning_topleft = (By.NAME,'Top Left')
    positioning_topright = (By.NAME,'Top Right')
    positioning_bottomright = (By.NAME,'Bottom Right')
    positioning_bottomleft = (By.NAME,'Bottom Left')
    positioning_break = (By.NAME,'Break')
    positioning_show = (By.NAME,'Show')
    
    '''Test alignment contains
       Left, Center & Right Twice 
       Hence only shortcut keys can be used  for text alignment category'''
    
    positioning_fulljustification = (By.NAME,'Full Justification')
    positioning_toggleselection = (By.NAME,'Toggle Selection')
    positioning_updatelayout = (By.NAME,'Update  Layout')
    
    
    ''' Utilities '''
    utilities_add = (By.NAME,'Add')
    utilities_remove = (By.NAME,'Remove')
    utilities_sync = (By.NAME,'Sync')
    utilities_show = (By.NAME,'Show')
    utilities_unlock = (By.NAME,'Unlock')
    utilities_reportset = (By.NAME,'Report Set')
    utilities_visibility = (By.NAME,'Visibility')
    utilities_taborder = (By.NAME,'Tab Order')
    utilities_deletecontainer = (By.NAME,'Delete Container')
    utilities_refreshall = (By.NAME,'Refresh All')
    
    '''3. Document Canvas Tab'''
    
    '''Insert'''
    insert_report = (By.NAME,'Report')
    insert_chart = (By.NAME,'Chart')
    insert_image = (By.NAME,'Image')
    insert_text = (By.NAME,'Text')
    insert_line = (By.NAME,'Line')
    insert_editbox = (By.NAME,'Edit Box')
    insert_dropdown = (By.NAME,'Drop Down')
    insert_listbox = (By.NAME,'List Box')
    insert_radiobutton = (By.NAME,'Insert Radio Button')
    insert_checkbox = (By.NAME,'Check Box')
    insert_new = (By.NAME,'New')
    insert_existing = (By.NAME,'Existing')
    insert_tableofcontents = (By.NAME,'Table of Contents')
    insert_master = (By.NAME,'Master')
    insert_overflow = (By.NAME,'Overflow')
    insert_adddashboardbar = (By.NAME,'Add Dashboard Bar')
    
    '''Utilities'''
    
    utilities_showchainorder = (By.NAME,'Show Chain order')
    utilities_savedocumentas = (By.NAME,'Save Document As')
    utilities_savepageas = (By.NAME,'Save Page As')
    utilities_preprocesscode = (By.NAME,'Pre-process code')
    utilities_postprocesscode = (By.NAME,'Post-process code')
    utilities_refreshall = (By.NAME,'Refresh All')
    utilities_chrome = (By.NAME,'Chrome')
    utilities_ie = (By.NAME,'Internet Explorer')
    utilities_firefox = (By.NAME,'Firefox')
    utilities_edge = (By.NAME,'Edge')
    
    '''4.Procedure View'''
    
    '''text editor'''
    texteditor_find = (By.NAME,'Find')
    texteditor_next = (By.NAME,'Next')
    texteditor_previous = (By.NAME,'Previous')
    texteditor_replace = (By.NAME,'Replace')
    texteditor_selectall = (By.NAME,'Select All')
    texteditor_toggle = (By.NAME,'Toggle')
    '''Text editor contains
       Next & Previous Twice 
       Hence only shortcut keys can be used  for Text editor'''
    texteditor_deleteall = (By.NAME,'Delete All')
    texteditor_gotoline = (By.NAME,'Goto Line')
    texteditor_abupper = (By.NAME,'Upper')
    texteditor_ablower = (By.NAME,'Lower')
    texteditor_changecase = (By.NAME,'Change Case')
    texteditor_addcomment = (By.NAME,'Add Comment')
    texteditor_removecomment = (By.NAME,'Remove Comment')
    texteditor_fontstyle = (By.NAME,'Font Style')
    texteditor_autoindent = (By.NAME,'Auto Indent')
    texteditor_resetall = (By.NAME,'Reset All')
    
    '''5. Report'''
    
    '''Report'''
    report_filter = (By.NAME,'Filter')
    report_headerfooter = (By.NAME,'Header Footer')
    report_columntotal = (By.NAME,'Column Total')
    report_rowtotal = (By.NAME,'Row Total')
    report_precisionreport = (By.NAME,'Precision Report')
    report_compunddocument = (By.NAME,'Compound Document')
    report_universalconcatenation = (By.NAME,'Universal Concatenation')
    report_sorteddata = (By.NAME,'Sorted Data')
    report_customefieldplacement = (By.NAME,'Custom Field Placement')
    report_trafiiclights = (By.NAME,'Traffic Lights')
    report_changetheme = (By.NAME,'Change Theme')
    report_managetheme = (By.NAME,'Manage Theme')
    report_savetheme = (By.NAME,'Save Theme')
    report_scope = (By.NAME,'Scope')
    report_bold = (By.NAME,'Bold')
    report_italic = (By.NAME,'Italic')
    report_underline = (By.NAME,'Underline')
    report_nounderline = (By.NAME,'No Underline')
    report_left = (By.NAME,'Left')
    report_center = (By.NAME,'Center')
    report_right = (By.NAME,'Right')
    report_default = (By.NAME,'Default')
    report_reportwidth = (By.NAME,'Report Width')
    report_copystyle = (By.NAME,'Copy Style')
    report_pastestyle = (By.NAME,'Paste Style')
    report_fontname = (By.NAME,'Font Name')
    report_fontsize = (By.NAME,'Font Size')
    report_color = (By.NAME,'Color')
    report_backgroundcolor = (By.NAME,'Background Color')
    report_defaults = (By.NAME,'Defaults')
    report_bordersgrid = (By.NAME,'Borders/Grid')
    report_userstyle = (By.NAME,'User Style')
    report_userstyle = (By.NAME,'Drill Down')
    
    '''Format'''
    format_html = (By.NAME,'HTML')
    format_activereport = (By.NAME,'Active Report')
    format_pdf = (By.NAME,'PDF')
    format_activepdf = (By.NAME,'Active PDF')
    format_excel = (By.NAME,'Excel')
    format_powerpoint = (By.NAME,'PowerPoint')
    format_outputformat = (By.NAME,'Output Format')
    format_outputformatoptions = (By.NAME,'Output Format Options')
    format_destinationpchold = (By.NAME,'Destination (PCHOLD)')
    format_tableofcontents = (By.NAME,'Table of Contents')
    format_freeze = (By.NAME,'Freeze')
    format_ondemandpaging = (By.NAME,'On-Demand Paging')
    format_autodrill = (By.NAME,'Auto Drill')
    format_popupdesc = (By.NAME,'Popup Desc.')
    format_accordionreport = (By.NAME,'Accordion Report')
    format_repeatsortvalue = (By.NAME,'Repeat Sort Value')
    format_linesperpage = (By.NAME,'"Lines per Page')
    format_accessibility = (By.NAME,'Accessibility')
    format_mailinglabels = (By.NAME,'Mailing Labels')
    
    '''Data'''
    data_summarycompute = (By.NAME,'Summary (Compute)')
    data_acrosscompute = (By.NAME,'Across Compute')
    data_forecast = (By.NAME,'Forecast')
    data_generateparametergroup = (By.NAME,'Generate Parameter Group')
    data_removefromparametergroup = (By.NAME,'Remove from Parameter Group')
    
    '''Layout'''
    layout_margins = (By.NAME,'Margins')
    layout_reportpage = (By.NAME,'Report Page')
    layout_papertype = (By.NAME,'Paper Type')
    layout_units = (By.NAME,'Units')
    layout_pagenumbering = (By.NAME,'Page Numbering')
    layout_cellpadding = (By.NAME,'Cell Padding') 
    
    
    
    
    
    
