
Option Explicit

Public language
Public nlsNewDomain
Public nlsNewStandardReport
Public nlsStdRpt
Public nlsNewStdRptGp
Public nlsNewRptObjGp
Public nlsNewRoj
Public nlsRptObj
Public nlsOther
Public nlsFilters
Public nlsDefine
Public nlsAppobj
Public nlsReport
Public nlsExpress
Public nlsNew
Public nlsAdministration
Public nlsEdit
Public nlsDone
Public nlsWebQuery
Public nlsPowerPainter
Public nlsReportAssistant
Public nlsGraphAssistant
Public nlsAdvancedGraphAssist
Public nlsAlertWizard
Public nlsEditor
Public nlsImportExternalFiles
Public nlsURL
Public nlsNewFolder
Public nlsName
Public nlsDataFile
Public nlsQuit
Public nlsRun
Public nlsSchedule
Public nlsEmail
Public nlsOptions
Public nlsNewdefinefield
Public nlsList
Public nlstree
Public nlsComputedfieldcreator
Public nlsFormat
Public nlsAddtoACROSS
Public nlsSumAdd
Public nlsPrintAdd
Public nlsSortByAdd
Public nlsprint
Public nlssum
Public nlsdefFld
Public nlsCmpute
Public nlsAdd
Public nlsSorting
Public nlsSubtotal
Public nlsSubtotalnumericsumprintfields
Public nlsNo
Public nlsOK
Public nlsYes
Public nlsOpen
Public nlsCancel
Public nlsEditSrc 
Public nlsDelete
Public nlsDeleteConfirmation
Public nlsAverageSquare
Public nlsHeadingTab
Public nlsHeading
Public nlsFooting
Public nlsImage
Public nlsReportOptions
Public nlsGraphTypes
Public nlsFieldSelection
Public nlsHeadings
Public nlsPage
Public nlsConsult
Public nlsGraph
Public nlsChtTitle
Public nlsChtSbTitle
Public nlsChartFootnote
Public nlsSetStyle
Public nlsSelectionCriteria
Public nlsJoinOptions
Public nlsProperties
Public nlsSettings
Public nlsXaxis
Public nlsYaxis
Public nlsPie
Public nlssbmt
Public nlsReset
Public nlsNewProc
Public nlsRefresh
Public nlsMRA
Public nlsGroups
Public nlsUsers
Public nlsRoles
Public nlsDomains
Public nlsClone
Public nls508
Public nlsAdv
Public nlsDataSrvr
Public nlsSvEntVal
Public nlsSvRpt
Public nlsShRpt
Public nlsRename
Public nlsAdmin
Public nlsSched
Public nlsLib
Public nlsRemove
Public nlssave
Public nlsSortAcrossRemove
Public nlsSumRemove
Public nlsSortByRemove
Public nlsPrintRemove
Public nlsCustomReports
Public nlsMyReports
Public nlsRunDeferred
Public nlsUtilities
Public nlsDeferredstatus
Public nlsView
Public nlsChart
Public nlsCut
Public nlsUpload
Public nlsDocument
Public nlsTitleChange
Public nlsFont
Public nlsMetadata
Public nlsFolder
Public nlsData
Public nlsFavorites
Public nlsSecurityCenter1
Public nlsSecurity
Public nlsMobile
Public nlsSecurityCenter
Public nlsGlobalFont
Public nlsParameters
Public nlsNewGroup
Public nlsOnDemandPaging
Public nlsCopy
Public nlsPaste
Public nlsInsertBtn
Public nlsNoSelection
Public nlsDashboard
Public nlsPublish
Public nlsAdministrator
Public nlsRepository
Public nlsAdministrationConsole

   
Public Function  TestForLang
   TestForLang=Lcase(parse_init_file(array("Language","QtpData")))
End Function


Public Sub CheckforBrowser
  If  Browser("name:=WebFOCUS Business Intelligence Dashboard").Exist(5) Then
                              Reporter.ReportEvent micPass,"Browser","Browser Exists"
 Else
		Reporter.ReportEvent micFail,"Windows Internet Explorer","Browser Does not exist"
		   Call TestForLang
		   Call ZH_HTMLRA_startup

End if	 
End Sub


Public sub ClickSearchDialogButtonA(strName)
'   Browser("name:=WebFOCUS Business Intelligence Dashboard").Dialog _
'     ("text:=Windows Internet Explorer","nativeclass:=#32770").Activate
'If (Browser("name:=WebFOCUS Business Intelligence Dashboard").Dialog _
'	  ("text:=Windows Internet Explorer").GetROProperty("visible"))="False" Then
'	Browser("name:=WebFOCUS Business Intelligence Dashboard").Dialog _
'     ("text:=Windows Internet Explorer","nativeclass:=#32770").SetTOProperty "visible", "true"
'End If
'   Window("title:=Windows Internet Explorer").Click
'	Browser("name:=WebFOCUS Business Intelligence Dashboard").Dialog _
'     ("text:=Windows Internet Explorer","nativeclass:=#32770").WinButton("text:=" & strName).Click

Browser("name:=WebFOCUS Business Intelligence Dashboard").Dialog("text:=Windows Internet Explorer","nativeclass:=#32770").WinButton("text:=OK").Click
End Sub






Public Sub ZH_HTMLRA_startup
language=TestForLang
strDefBrowser=DefaultBrowser ( )
CreateSimplifyChineseDictionary
StartWFSuite_NLS
Window("regexpwndtitle:=Windows Internet Explorer","regexpwndclass:=IEFrame").Maximize
DoubleClickTreeLink "D - RA - NLS GUI QA"
DoubleClickTreeLink (nlsMyReports)
DoubleClickTreeLink (nlsCustomReports)
BIDReportingServerCredentals
RefreshDomainTree
DoubleClickTreeLink "D - RA - NLS GUI QA"
DoubleClickTreeLink (nlsStdRpt)
DoubleClickTreeLink "RA - NLS GUI QA"
End Sub

Public Sub CreateSimplifyChineseDictionary
language="simplifychinese"
nlsNewDomain="新域"
nlsNewStandardReport="New Standard Report"
nlsStdRpt="标准报告"
nlsNewStdRptGp="New Standard Report Group"
nlsNewRptObjGp="New Reporting Object Group"
nlsNewRoj="新报告对象"
nlsRptObj="报告对象"
nlsOther="其他"
nlsFilters="过滤器"
nlsSecurity="安全性"
nlsSecurityCenter="安全中心..."
nlsSecurityCenter1="安全中心"
nlsUpload="上载"
nlsRename="重命名"
nlsMetadata="元数据"
nlsWebQuery="WebQuery"
nlsDefine="定义"
nlsAppobj="应用程序对象"
nlsReport="报告"
nlsFavorites="收藏夹"
nlsMobile="移动收藏夹"
nlsNew="新建"
nlsEdit="编辑.*"
nlsExpress="Express"
nlsFolder="文件夹"
nlsDocument="文档"
nlsData="数据"
nlsDone="完成"
nlsCut="剪切"
nlsChart="图表"
nlsPowerPainter="Power Painter"
nlsReportAssistant="报告助手"
nlsGraphAssistant="图形助手"
nlsAdministration="管理"
nlsAdvancedGraphAssist="高级图形助手"
nlsAlertWizard="警报向导"
nlsEditor="编辑器"
nlsImportExternalFiles="Imoprt External File(s)"
nlsURL="URL..."
nlsNewFolder="新文件夹"
nlsName="名称："
nlsDataFile="数据文件："
nlsQuit="退出"
nlsRun="运行"
nlsConsult="查看"
nlsOptions="选项"
nlsSchedule="调度"
nlsEmail="电子邮件"
nlsNewdefinefield="新建定义字段"
nlsList="列表"
nlstree="树"
nlsComputedfieldcreator="已计算字段创建者"
nlsFormat="格式"
nlsAddtoACROSS="Add to ACROSS"
nlsSumAdd="总和：添加"
nlsPrintAdd="打印添加"
nlsSortByAdd="添加"
nlsprint="打印"
nlssum="总和"
nlsdefFld="定义字段"
nlsTitleChange="更改标题"
nlsCmpute="计算"
nlsAdd="添加"
nlsSorting="排序"
nlsSubtotal="小计"
nlsSubtotalnumericsumprintfields="数字总结/明细字段小计"
nlsNo="否"
nlsOK="确定"
nlsYes="是"
nlsCancel="取消"
nlsOpen="打开"
nlsEditSrc="编辑源"
nlsDelete="删除"
nlsImage="文档"
nlsDeleteConfirmation="DeleteConfirmation"
nlsAverageSquare="均方"
nlsHeadingTab="报告页眉"
nlsHeading="页眉"
nlsFooting="页脚"
nlsReportOptions="报告选项" 
nlsGraphTypes="图形类型"
nlsFieldSelection="字段选择"
nlsHeadings="页眉" 
nlsPage="页面"
nlsGraph="图形"
nlsChtTitle="图表标题"
nlsChtSbTitle="图表副标题"
nlsChartFootnote="图表脚注"
nlsSetStyle="设置样式..."
nlsSelectionCriteria="选择标准"
nlsJoinOptions="连接选项"
nlsProperties="属性"
nlsSettings="设置"
nlsXaxis="X 轴"
nlsYaxis="Y 轴"
nlsPie="饼形"
nlssbmt="提交"
nlsReset="复位"
nlsNewProc="New Procedure"
nlsRefresh="刷新"
nlsMRA="Managed Reporting 管理首页"
nlsGroups="组"
nlsUsers="用户"
nlsRoles="角色"
nlsDomains="域"
nlsClone="克隆"
nls508="508"
nlsAdv="高级"
nlsDataSrvr="数据服务器"
nlsSvEntVal="保存输入的值"
nlsSvRpt="保存报告"
nlsShRpt="共享报告"
nlsAdmin="管理员"
nlsSched="调度"
nlsLib="库"
nlsRemove="除去"
nlsSortAcrossRemove="除去"
nlsSumRemove="总和：除去"
nlsSortByRemove="除去"
nlsPrintRemove="打印除去"
nlssave="保存"
nlsCustomReports="定制报告"
nlsMyReports="我的报告"
nlsRunDeferred="延迟运行"
nlsUtilities="实用程序"
nlsDeferredstatus="延迟状态"
nlsView="查看"
nlsFont="字体..."
nlsGlobalFont="Global Font"
nlsParameters="参数名称"
nlsNewGroup="新组"
nlsOnDemandPaging="随需应变页面调度"
nlsCopy="复制"
nlsPaste="粘贴"
nlsInsertBtn="插入"
nlsNoSelection="没有任何选择"
nlsDashboard="Dashboard"
nlsPublish="发布"
nlsAdministrator="ExpressAdministrator"
nlsRepository="存储库"
nlsAdministrationConsole="管理控制台"

End Sub
































