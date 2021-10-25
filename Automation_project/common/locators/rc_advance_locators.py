from selenium.webdriver.common.by import By
class RCAdvanceLocators(object):
    
    main_window=(By.CSS_SELECTOR, "#rcBiScheduleEditorWnd")
    rc_menu_btn=(By.CSS_SELECTOR, "#rcBiScheduleEditorWnd img[src*='reportcaster_32']")
    
    '''RC Toolbar'''
    toolbar=(By.CSS_SELECTOR, "#ScheduleEditor_toolBar")
    toolbar_save=(By.CSS_SELECTOR, "#ScheduleEditor_btnSave img")
    toolbar_run=(By.CSS_SELECTOR, "#ScheduleEditor_btnRun img")
    toolbar_help=(By.CSS_SELECTOR, "#ScheduleEditor_btnHelp img")
    
    '''RC Ribbon'''
    ribbon_save_and_close=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnSaveClose img")
    ribbon_delete=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnDelete img")
    ribbon_properties=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnShowGeneral img")
    
    ribbon_recurrences=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnShowOccurrences img")
    ribbon_recurrences_new=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnItemRecurrenceNew img")
    ribbon_recurrences_edit=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnItemRecurrenceEdit img")
    ribbon_recurrences_remove=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnItemRecurrenceRemove img")
    
    ribbon_task=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnShowTasks img")
    ribbon_task_new=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnItemTasksNew [id^='BiToolBarMenuButton']")
    ribbon_task_edit=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnItemTasksEdit img")
    ribbon_task_remove=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnItemTasksRemove img")
    
    ribbon_distributions=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnShowDistributions img")
    ribbon_distributions_new=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnItemDistsNew [id^='BiToolBarMenuButton']")
    ribbon_distributions_edit=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnItemDistsEdit img")
    ribbon_distributions_remove=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnItemDistsRemove img")
    
    ribbon_notification=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnShowSettings img")
    ribbon_log_report=(By.CSS_SELECTOR, "#ScheduleEditor_tabPage #ScheduleEditor_btnShowHistory img")

    '''Properties'''
    input_title=(By.CSS_SELECTOR, "#ScheduleEditor_schedGeneral #ScheduleEditor_nameTextField")
    input_summary=(By.CSS_SELECTOR, "#ScheduleEditor_schedGeneral #ScheduleEditor_notesTextArea")
    checkbox_delete_this_schedule=(By.CSS_SELECTOR, "#ScheduleEditor_schedGeneral #ScheduleEditor_deleteCheckBox input")
    checkbox_enabled=(By.CSS_SELECTOR, "#ScheduleEditor_schedGeneral #ScheduleEditor_statusCheckBox input")
    
    '''Schedule Recurrence window'''
    run_once=(By.CSS_SELECTOR, "#rcBiOccurrenceDlg #rc_scheduleeditor_recurrence_type_once input")
    minutes=(By.CSS_SELECTOR, "#rcBiOccurrenceDlg #rc_scheduleeditor_recurrence_type_minute input")
    hourly=(By.CSS_SELECTOR, "#rcBiOccurrenceDlg #rc_scheduleeditor_recurrence_type_hour input")
    daily=(By.CSS_SELECTOR, "#rcBiOccurrenceDlg #rc_scheduleeditor_recurrence_type_day input")
    weekly=(By.CSS_SELECTOR, "#rcBiOccurrenceDlg #rc_scheduleeditor_recurrence_type_week input")
    monthly=(By.CSS_SELECTOR, "#rcBiOccurrenceDlg #rc_scheduleeditor_recurrence_type_month input")
    yearly=(By.CSS_SELECTOR, "#rcBiOccurrenceDlg #rc_scheduleeditor_recurrence_type_year input")
    custom=(By.CSS_SELECTOR, "#rcBiOccurrenceDlg #rc_scheduleeditor_recurrence_type_custom input")
    
    recurrence_ok=(By.CSS_SELECTOR, "#rcBiOccurrenceDlg #OccurrenceDlg_btnOK")
    recurrence_cancel=(By.CSS_SELECTOR, "#rcBiOccurrenceDlg #OccurrenceDlg_btnCancel")
    
    '''Task Dialog'''
    task_dialog_ok=(By.CSS_SELECTOR, "#rcBiTaskDlg #TaskDlg_btnOK")
    task_dialog_cancel=(By.CSS_SELECTOR, "#rcBiTaskDlg #TaskDlg_btnCancel")
    
    '''1. Task-WF Server Procedure'''
    '''General Tab'''
    wfserverproc_task_name=(By.CSS_SELECTOR, "#rcBiTaskWFServerProc #TaskWFServerProc_nameTextField")
    wfserverproc_server_name=(By.CSS_SELECTOR, "#rcBiTaskWFServerProc #TaskWFServerProcPane_serverListComboBox input")
    wfserverproc_execution_id=(By.CSS_SELECTOR, "#rcBiTaskWFServerProc #TaskWFServerProcPane_execidListComboBox input")
    wfserverproc_password_btn=(By.CSS_SELECTOR, "#rcBiTaskWFServerProc #TaskWFServerProcPane_execpassButton")
    wfserverproc_browse_btn=(By.CSS_SELECTOR, "#rcBiTaskWFServerProc #TaskWFServerProcPane_procBrowseButton")
    wfserverproc_procedure_name=(By.CSS_SELECTOR, "#rcBiTaskWFServerProc #TaskWFServerProcPane_procNameTextField")
    wfserverproc_burst_report_checkbox=(By.CSS_SELECTOR, "#rcBiTaskWFServerProc #TaskWFServerProcPane_burstCheckBox input")
    wfserverproc_override_checkbox=(By.CSS_SELECTOR, "#rcBiTaskWFServerProc #TaskWFServerProcPane_overrideFormatCheckBox input")
    wfserverproc_save_report_as_input=(By.CSS_SELECTOR, "#rcBiTaskWFServerProc #TaskWFServerProcPane_saveasTextField")
    wfserverproc_enabled_input=(By.CSS_SELECTOR, "#rcBiTaskWFServerProc #TaskWFServerProcPane_statusCheckBox input")
    
    '''2. Task-WF Report'''
    standardreport_task_name=(By.CSS_SELECTOR, "#rcBiTaskStandardReport #TaskStandardReport_nameTextField")
    standardreport_path=(By.CSS_SELECTOR, "#rcBiTaskStandardReport #TaskStandardReportPane_folderTextField")
    standardreport_procedure=(By.CSS_SELECTOR, "#rcBiTaskStandardReport #TaskStandardReportPane_procNameTextField")
    standardreport_browse_btn=(By.CSS_SELECTOR, "#rcBiTaskStandardReport #TaskStandardReportPane_procBrowseButton")
    standardreport_server_name=(By.CSS_SELECTOR, "#rcBiTaskStandardReport #TaskStandardReportPane_serverNameTextField")
    standardreport_execution_id=(By.CSS_SELECTOR, "#rcBiTaskStandardReport #TaskStandardReportPane_execidListComboBox input")
    standardreport_password_btn=(By.CSS_SELECTOR, "#rcBiTaskStandardReport #TaskStandardReportPane_execpassButton")
    standardreport_burst_report_checkbox=(By.CSS_SELECTOR, "#rcBiTaskStandardReport #TaskStandardReportPane_burstCheckBox input")
    standardreport_override_checkbox=(By.CSS_SELECTOR, "#rcBiTaskStandardReport #TaskStandardReportPane_overrideFormatCheckBox input")
    standardreport_save_report_as_input=(By.CSS_SELECTOR, "#rcBiTaskStandardReport #TaskStandardReportPane_saveasTextField")
    standardreport_enabled_input=(By.CSS_SELECTOR, "#rcBiTaskStandardReport #TaskStandardReportPane_statusCheckBox input")
    
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
    email_distribution_name=(By.CSS_SELECTOR, "#rcBiDistributeEmail #DistributeEmail_nameTextField")
    email_type=(By.CSS_SELECTOR, "#rcBiDistributeEmail #DistributeEmailPane_distTypeComboBox [id^='BiButton']")
    email_to=(By.CSS_SELECTOR, "#rcBiDistributeEmail #DistributeEmailPane_mailToTextField")
    email_from=(By.CSS_SELECTOR, "#rcBiDistributeEmail #DistributeEmailPane_mailFromTextField")
    email_reply_address=(By.CSS_SELECTOR, "#rcBiDistributeEmail #DistributeEmailPane_mailReplyTextField")
    email_subject=(By.CSS_SELECTOR, "#rcBiDistributeEmail #DistributeEmailPane_mailSubjectTextField")
    email_override_checkbox=(By.CSS_SELECTOR, "#rcBiDistributeEmail #DistributeEmailPane_zipminimumCheckBox input")
    email_enabled_input=(By.CSS_SELECTOR, "#rcBiDistributeEmail #DistributeEmailPane_statusCheckBox input")
    
    
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
