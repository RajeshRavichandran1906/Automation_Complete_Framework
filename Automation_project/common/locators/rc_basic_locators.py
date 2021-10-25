from selenium.webdriver.common.by import By
class RCBasicLocators(object):
    
    main_window=(By.CSS_SELECTOR, "#rcBiScheduleEditorWnd")
    rc_menu_btn=(By.CSS_SELECTOR, "#rcBiScheduleEditorWnd img[src*='reportcaster_32']")
    
    '''RC Toolbar'''
    toolbar=(By.CSS_SELECTOR, "#BasicScheduleEditor_toolBar")
    toolbar_save=(By.CSS_SELECTOR, "#BasicScheduleEditor_btnSave img")
    toolbar_run=(By.CSS_SELECTOR, "#BasicScheduleEditor_btnRun img")
    toolbar_help=(By.CSS_SELECTOR, "#BasicScheduleEditor_btnHelp img")
    
    '''RC Ribbon'''
    ribbon_save_and_close=(By.CSS_SELECTOR, "#BasicScheduleEditor_tabPage #BasicScheduleEditor_btnSaveClose img")
    ribbon_delete=(By.CSS_SELECTOR, "#BasicScheduleEditor_tabPage #BasicScheduleEditor_btnDelete img")
    ribbon_properties=(By.CSS_SELECTOR, "#BasicScheduleEditor_tabPage #BasicScheduleEditor_btnShowGeneral img")
    ribbon_recurrences=(By.CSS_SELECTOR, "#BasicScheduleEditor_tabPage #BasicScheduleEditor_btnShowOccurrence img")
    ribbon_task=(By.CSS_SELECTOR, "#BasicScheduleEditor_tabPage #BasicScheduleEditor_btnShowTask img")
    ribbon_distributions=(By.CSS_SELECTOR, "#BasicScheduleEditor_tabPage #BasicScheduleEditor_btnShowDistribution img")
    ribbon_notification=(By.CSS_SELECTOR, "#BasicScheduleEditor_tabPage #BasicScheduleEditor_btnShowSettings img")
    ribbon_log_report=(By.CSS_SELECTOR, "#BasicScheduleEditor_tabPage #BasicScheduleEditor_btnShowHistory img")

    '''Properties'''
    input_title=(By.CSS_SELECTOR, "#BasicScheduleEditor_schedGeneral #BasicScheduleEditor_nameTextField")
    input_summary=(By.CSS_SELECTOR, "#BasicScheduleEditor_schedGeneral #BasicScheduleEditor_notesTextArea")
    checkbox_delete_this_schedule=(By.CSS_SELECTOR, "#BasicScheduleEditor_schedGeneral #BasicScheduleEditor_deleteCheckBox input")
    checkbox_enabled=(By.CSS_SELECTOR, "#BasicScheduleEditor_schedGeneral #BasicScheduleEditor_statusCheckBox input")
    
    '''Schedule Recurrence window'''
    
    '''Task Dialog'''
    '''1. Task-WF Server Procedure'''
    '''General Tab'''
    wfserverproc_task_name=(By.CSS_SELECTOR, "#TaskStandardReportPane_folderTextField")
    wfserverproc_procedure_name=(By.CSS_SELECTOR, "#TaskStandardReportPane_procNameTextField")
    wfserverproc_server_name=(By.CSS_SELECTOR, "#TaskStandardReportPane_serverNameTextField")
    task_execution_id=(By.CSS_SELECTOR, "#TaskStandardReportPane_execidListComboBox input")
    task_password_btn=(By.CSS_SELECTOR, "#TaskStandardReportPane_execpassButton")
#******************************
    wfserverproc_browse_btn=(By.CSS_SELECTOR, "#rcBiTaskWFServerProc #TaskWFServerProcPane_procBrowseButton")
    
    wfserverproc_burst_report_checkbox=(By.CSS_SELECTOR, "#rcBiTaskWFServerProc #TaskWFServerProcPane_burstCheckBox input")
    wfserverproc_override_checkbox=(By.CSS_SELECTOR, "#rcBiTaskWFServerProc #TaskWFServerProcPane_overrideFormatCheckBox input")
    wfserverproc_save_report_as_input=(By.CSS_SELECTOR, "#rcBiTaskWFServerProc #TaskWFServerProcPane_saveasTextField")
    wfserverproc_enabled_input=(By.CSS_SELECTOR, "#rcBiTaskWFServerProc #TaskWFServerProcPane_statusCheckBox input")
    
    '''2. Task-WF Report'''
    standardreport_task_name=(By.CSS_SELECTOR, "#rcBiTaskStandardReportPane #TaskStandardReport_nameTextField")
    standardreport_path=(By.CSS_SELECTOR, "#rcBiTaskStandardReportPane #TaskStandardReportPane_folderTextField")
    standardreport_procedure=(By.CSS_SELECTOR, "#rcBiTaskStandardReportPane #TaskStandardReportPane_procNameTextField")
    standardreport_browse_btn=(By.CSS_SELECTOR, "#rcBiTaskStandardReportPane #TaskStandardReportPane_procBrowseButton")
    standardreport_server_name=(By.CSS_SELECTOR, "#rcBiTaskStandardReportPane #TaskStandardReportPane_serverNameTextField")
    standardreport_execution_id=(By.CSS_SELECTOR, "#rcBiTaskStandardReportPane #TaskStandardReportPane_execidListComboBox input")
    standardreport_password_btn=(By.CSS_SELECTOR, "#rcBiTaskStandardReportPane #TaskStandardReportPane_execpassButton")
    standardreport_burst_report_checkbox=(By.CSS_SELECTOR, "#rcBiTaskStandardReportPane #TaskStandardReportPane_burstCheckBox input")
    standardreport_override_checkbox=(By.CSS_SELECTOR, "#rcBiTaskStandardReportPane #TaskStandardReportPane_overrideFormatCheckBox input")
    standardreport_save_report_as_input=(By.CSS_SELECTOR, "#rcBiTaskStandardReportPane #TaskStandardReportPane_saveasTextField")
    standardreport_enabled_input=(By.CSS_SELECTOR, "#rcBiTaskStandardReportPane #TaskStandardReportPane_statusCheckBox input")
    
    '''3. Task-File'''
    file_task_name=(By.CSS_SELECTOR, "#rcBiTaskFile #TaskFile_nameTextField")
    file_name=(By.CSS_SELECTOR, "#rcBiTaskFile #TaskFile_fileNameTextField")
    file_save_report_as_input=(By.CSS_SELECTOR, "#rcBiTaskFile #TaskFile_saveasTextField")
    file_delete_the_file_checkbox=(By.CSS_SELECTOR, "#rcBiTaskFile #TaskFile_deleteCheckBox input")
    file_enabled_input=(By.CSS_SELECTOR, "#rcBiTaskFile #TaskFile_statusCheckBox input")
    
    '''4. Task-FTP'''
    ftp_task_name=(By.CSS_SELECTOR, "#rcBiTaskFTP #TaskFTP_nameTextField")
    ftp_server_name=(By.CSS_SELECTOR, "#rcBiTaskFTP #TaskFTP_serverNameTextField")
    ftp_account_name=(By.CSS_SELECTOR, "#rcBiTaskFTP #TaskFTP_userIdTextField")
    ftp_password_btn=(By.CSS_SELECTOR, "#rcBiTaskFTP #TaskFTP_passwordButton")
    ftp_file_name=(By.CSS_SELECTOR, "#rcBiTaskFTP #TaskFTP_fileNameTextField")
    ftp_file_transfer_mode=(By.CSS_SELECTOR, "#rcBiTaskFTP #TaskFTP_transferModeComboBox [id^='BiButton']")
    ftp_save_report_as_input=(By.CSS_SELECTOR, "#rcBiTaskFTP #TaskFTP_saveasTextField")
    ftp_delete_the_file_checkbox=(By.CSS_SELECTOR, "#rcBiTaskFTP #TaskFTP_deleteCheckBox input")
    ftp_enabled_input=(By.CSS_SELECTOR, "#rcBiTaskFTP #TaskFTP_statusCheckBox input")
    
    '''5. Task-URL'''
    url_task_name=(By.CSS_SELECTOR, "#rcBiTaskURL #TaskURL_nameTextField")
    url_address=(By.CSS_SELECTOR, "#rcBiTaskURL #TaskURLPane_urlAddressTextField")
    url_user_id=(By.CSS_SELECTOR, "#rcBiTaskURL #TaskURLPane_execidTextField")
    url_password_btn=(By.CSS_SELECTOR, "#rcBiTaskURL #TaskURLPane_execpassButton")
    url_save_report_as_input=(By.CSS_SELECTOR, "#rcBiTaskURL #TaskURLPane_saveasTextField")
    url_enabled_input=(By.CSS_SELECTOR, "#rcBiTaskURL #TaskURLPane_statusCheckBox input")
    
    '''Distribution Dialog'''
    distribution_dialog_ok=(By.CSS_SELECTOR, "#rcBiDistributeDlg #DistributeDlg_btnOK")
    distribution_dialog_cancel=(By.CSS_SELECTOR, "#rcBiDistributeDlg #DistributeDlg_btnCancel")
    
    '''1. Distribution-Email'''
    email_type=(By.CSS_SELECTOR, "#BasicScheduleEditor_schedDistribution #DistributeEmailPane_distTypeComboBox [id^='BiButton']")
    email_to=(By.CSS_SELECTOR, "#BasicScheduleEditor_schedDistribution #DistributeEmailPane_mailToTextField")
    email_from=(By.CSS_SELECTOR, "#BasicScheduleEditor_schedDistribution #DistributeEmailPane_mailFromTextField")
    email_reply_address=(By.CSS_SELECTOR, "#BasicScheduleEditor_schedDistribution #DistributeEmailPane_mailReplyTextField")
    email_subject=(By.CSS_SELECTOR, "#BasicScheduleEditor_schedDistribution #DistributeEmailPane_mailSubjectTextField")
    email_override_checkbox=(By.CSS_SELECTOR, "#BasicScheduleEditor_schedDistribution #DistributeEmailPane_zipminimumCheckBox input")
    email_enabled_input=(By.CSS_SELECTOR, "#BasicScheduleEditor_schedDistribution #DistributeEmailPane_statusCheckBox input")
    
    
    '''2. Distribution-FTP'''
    '''2.1. Distribution-FTP-General'''
    ftp_distribution_name=(By.CSS_SELECTOR, "#rcBiDistributeFTP #DistributeFTP_nameTextField")
    ftp_type=(By.CSS_SELECTOR, "#rcBiDistributeFTP #DistributeFTPPane_distTypeComboBox [id^='BiButton']")
    ftp_name_btn=(By.CSS_SELECTOR, "#rcBiDistributeFTP #DistributeFTPPane_toBrowseButton")
    ftp_name_input=(By.CSS_SELECTOR, "#rcBiDistributeFTP #DistributeFTPPane_addressValueTextField")
    ftp_directory_input=(By.CSS_SELECTOR, "#rcBiDistributeFTP #DistributeFTPPane_ftpServerDirectoryTextField")
    ftp_radio_input=(By.CSS_SELECTOR, "#rcBiDistributeFTP #DistributeFTPPane_zipSettingGroupBox div[id^='BiRadioButton']")
    ftp_zip_input=(By.CSS_SELECTOR, "#rcBiDistributeFTP #DistributeFTPPane_zipFileNameTextField")
    ftp_index_file_input=(By.CSS_SELECTOR, "#rcBiDistributeFTP #DistributeFTPPane_indexTextField")
    ftp_enabled_input=(By.CSS_SELECTOR, "#rcBiDistributeFTP #DistributeFTPPane_statusCheckBox input")
    '''2.2 Distribution-FTP-Options'''
    ftp_ftp_server_name=(By.CSS_SELECTOR, "#rcBiDistributeFTP #DistributeFTPOptionsPane_ftpServerNameTextField")
    ftp_account_name=(By.CSS_SELECTOR, "#rcBiDistributeFTP #DistributeFTPOptionsPane_ftpServerUserTextField")
    ftp_password_btn=(By.CSS_SELECTOR, "#rcBiDistributeFTP #DistributeFTPOptionsPane_ftpServerPasswordButton")
    
    
    '''3. Distribution-Printer'''
    printer_distribution_name=(By.CSS_SELECTOR, "#rcBiDistributePrint #DistributePrint_nameTextField")
    printer_type=(By.CSS_SELECTOR, "#rcBiDistributePrint #DistributePrint_distTypeComboBox [id^='BiButton']")
    printer_name_btn=(By.CSS_SELECTOR, "#rcBiDistributePrint #DistributePrint_toBrowseButton")
    printer_name_input=(By.CSS_SELECTOR, "#rcBiDistributePrint #DistributePrint_addressValueTextField")
    printer_enabled_input=(By.CSS_SELECTOR, "#rcBiDistributePrint #DistributePrint_statusCheckBox input")
    
    '''4. Distribution Report-Library'''
    library_distribution_name=(By.CSS_SELECTOR, "#rcBiDistributeLibrary #DistributeLibrary_nameTextField")
    library_folder_location_btn=(By.CSS_SELECTOR, "#rcBiDistributeLibrary #DistributeLibraryPane_folderButton")
    library_folder_location_input=(By.CSS_SELECTOR, "#rcBiDistributeLibrary #DistributeLibraryPane_folderTextField")
    library_advanced_btn=(By.CSS_SELECTOR, "#rcBiDistributeLibrary #DistributeLibraryPane_advancedButton")
    library_radio_input=(By.CSS_SELECTOR, "#rcBiDistributeLibrary div[id^='BiRadioButton']")
    library_access_list_btn=(By.CSS_SELECTOR, "#rcBiDistributeLibrary #DistributeLibraryPane_accessBrowseButton")
    library_access_list_input=(By.CSS_SELECTOR, "#rcBiDistributeLibrary #DistributeLibraryPane_accessNameTextField")
    library_limit_distribution_input=(By.CSS_SELECTOR, "#rcBiDistributeLibrary #DistributeLibraryPane_accessLimitCheckBox input")
    library_enabled_input=(By.CSS_SELECTOR, "#rcBiDistributeLibrary #DistributeLibraryPane_statusCheckBox input")
    
    '''5. Distribution-Repository'''
    repository_distribution_name=(By.CSS_SELECTOR, "#rcBiDistributeMR #DistributeMR_nameTextField")
    repository_folder_location_btn=(By.CSS_SELECTOR, "#rcBiDistributeMR #DistributeMR_folderButton")
    repository_folder_location_input=(By.CSS_SELECTOR, "#rcBiDistributeMR #DistributeMR_folderTextField")
    repository_enabled_input=(By.CSS_SELECTOR, "#rcBiDistributeMR #DistributeMR_statusCheckBox input")

    '''Notifications'''
    notification_type=(By.CSS_SELECTOR, "#ScheduleEditor_notifyGroupBox #ScheduleEditor_notifyComboBox [id^='BiButton']")
    reply_address=(By.CSS_SELECTOR, "#ScheduleEditor_notifyGroupBox #ScheduleEditor_notifyReplyTextField")
    reply_address=(By.CSS_SELECTOR, "#ScheduleEditor_notifyGroupBox #ScheduleEditor_notifySubjectTextField")
    brief_message_to=(By.CSS_SELECTOR, "#ScheduleEditor_notifyGroupBox #ScheduleEditor_notifyBriefTextField")
    full_message_to=(By.CSS_SELECTOR, "#ScheduleEditor_notifyGroupBox #ScheduleEditor_notifyFullTextField")
    
    '''Log Report'''
    refresh_btn=(By.CSS_SELECTOR, "##ScheduleEditor_schedHistory #ScheduleEditor_btnRefreshHistory")
