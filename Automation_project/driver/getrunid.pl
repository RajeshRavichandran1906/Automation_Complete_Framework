#!/usr/local/bin/perl
use English;

my ($suite,$key)=@ARGV;

if(($suite eq 'S10032_active_datatype_formats') or ($suite eq 'S10032_ahtml_off') or ($suite eq 'S10032_ahtml_on')){
         %runids = ("8202m_cr", "61306", "8202m_ff", "61318", "8202m_ie", "61310",
         			"8201m_cr", "62603", "8201m_ff", "62611", "8201m_ie", "62607",
         			"82xx_ie", "64287", "82xx_cr", "64127", "82xx_ff", "64284");
         $runid=$runids{$key};
}elsif(($suite eq 'S10674_ws_contextmenu_1') or ($suite eq 'S10674_ws_contextmenu_2') or ($suite eq 'S10674_ws_contextmenu_3') or ($suite eq 'S10674_ws_contextmenu_4') or ($suite eq 'S10674_ws_contextmenu_5')){
         %runids = ("8202_ie", "61048", "8202_cr", "61048", "8202_ff", "61048");
         $runid=$runids{$key};
}elsif(($suite eq 'S10032_infoassist_1') or ($suite eq 'S10032_infoassist_2') or ($suite eq 'S10032_infoassist_3') or ($suite eq 'S10032_infoassist_4') or ($suite eq 'S10032_infoassist_5') or ($suite eq 'S10032_infoassist_6')){
         %runids = ("8202_ie", "59814", "8202_cr", "59669", "8202_ff", "59657",
         			"82xx_ie", "64291", "82xx_cr", "64123", "82xx_ff", "64290");
         $runid=$runids{$key};
}elsif($suite eq 'S10032_leaflet_1'){
         %runids = ("8202_ie", "59814", "8202_cr", "59669", "8202_ff", "59657",
         			"82xx_ie", "64290", "82xx_cr", "64123", "82xx_ff", "64294");
         $runid=$runids{$key};
}elsif(($suite eq 'S10032_esrimap_1') or ($suite eq 'S10032_esrimap_2') or ($suite eq 'S10032_chart_1')){
         %runids = ("8202_ie", "59814", "8202_cr", "59669", "8202_ff", "59657",
         			"82xx_ie", "64290", "82xx_cr", "64123", "82xx_ff", "64294");
         $runid=$runids{$key};
}elsif(($suite eq 'S10660_infoassist_2') or ($suite eq 'S10660_chart_1') or ($suite eq 'S10660_chart_2') or ($suite eq 'S10660_visual_1') or ($suite eq 'S10660_visual_2')
		or ($suite eq 'S10660_esrimap_1') or ($suite eq 'S10660_esrimap_2') or ($suite eq 'S10660_leaflet_1')){
         %runids = ("8202_ie", "59815", "8202_cr", "59813", "8202_ff", "59832",
         			"82xx_ie", "59815", "82xx_cr", "64124", "82xx_ff", "64073");
         $runid=$runids{$key};
}elsif(($suite eq 'S10664_binning_1')or($suite eq 'S10664_binning_2')or($suite eq 'S10664_paperclipping_1')or($suite eq 'S10664_paperclipping_2')){
         %runids = ("82xx_ie", "64257","82xx_ff", "64260", "82xx_cr", "64254","8202_eg","54553",
         			"head_ie", "56801","head_ff", "56803", "head_cr", "56805","head_eg","56799");
         $runid=$runids{$key};
}elsif(($suite eq 'S10117_Bip_V4_Portal_1')or($suite eq 'S10117_Bip_V4_Portal_2') or ($suite eq 'S10117_G246489')){
         %runids = ("8201m_ie", "", "8201m_ff", "58176", "8201m_cr", "58631","8201m_eg","",
         			"8202_ie","58176","8202_ff", "58168", "8202_cr", "59828","8202_eg","", "82xx_ff", "64285", "82xx_cr", "64128", "82xx_ie", "64288",
         			"head_ie","","head_ff", "", "head_cr", "","head_eg","");
         $runid=$runids{$key};
}elsif($suite eq 'S10117_chart_visual_1'){
         %runids = ("8201m_ie", "", "8201m_ff", "58176", "8201m_cr", "58631","8201m_eg","",
         			"8202_ie","58176","8202_ff", "58168", "8202_cr", "59828","8202_eg","", "82xx_ff", "64296", "82xx_cr", "64125", "82xx_ie", "64292",
         			"head_ie","","head_ff", "", "head_cr", "","head_eg","");
         $runid=$runids{$key};
}elsif($suite eq 'S7067'){
         %runids = ("82xx_ie", "64239", "82xx_ff", "64223", "82xx_cr", "64207","82xx_eg","54411",
         			"8202m_ie","61405","8202m_ff", "61421", "8202m_cr", "61389","8202_eg","",
         			"8201m_ie","56737","8201m_ff", "56695", "8201m_cr", "62725","8201m_eg","56709");
         $runid=$runids{$key};
}elsif(($suite eq 'S7068_filter_1') or ($suite eq 'S7068_filter_2') or ($suite eq 'S7068_medproj_1')){
         %runids = ("82xx_ie", "64240", "82xx_ff", "64224", "82xx_cr", "64208","82xx_eg","54412",
         			"8202m_ie","61406","8202m_ff", "61422", "8202m_cr", "61390","8202_eg","",
         			"8201m_ie","56738","8201m_ff", "56696", "8201m_cr", "62726","8201m_eg","56710");
         $runid=$runids{$key};
}elsif($suite eq 'S7069'){
         %runids = ("82xx_ie", "64241", "82xx_ff", "64225", "82xx_cr", "64209","82xx_eg","54413",
         			"8202m_ie","61407","8202m_ff", "61423", "8202m_cr", "61391","8202_eg","",
         			"8201m_ie","56739","8201m_ff", "56697", "8201m_cr", "62727","8201m_eg","56711");
         $runid=$runids{$key};
}elsif($suite eq 'S7070'){
         %runids = ("82xx_ie", "64242", "82xx_ff", "64226", "82xx_cr", "64210","82xx_eg","54414",
         			"8202m_ie","61408","8202m_ff", "61424", "8202m_cr", "61392","8202_eg","",
         			"8201m_ie","56740","8201m_ff", "56698", "8201m_cr", "62728","8201m_eg","56712");
         $runid=$runids{$key};
}elsif($suite eq 'S7071'){
         %runids = ("82xx_ie", "61880", "82xx_ff", "61896", "82xx_cr", "64394","82xx_eg","54415",
         			"8202m_ie","61409","8202m_ff", "61425", "8202m_cr", "61393","8202_eg","",
         			"8201m_ie","56741","8201m_ff", "56699", "8201m_cr", "62729","8201m_eg","56713");
         $runid=$runids{$key};
}elsif($suite eq 'S7072'){
         %runids = ("82xx_ie", "64243", "82xx_ff", "64227", "82xx_cr", "64211","82xx_eg","54416",
         			"8202m_ie","61410","8202m_ff", "61426", "8202m_cr", "61394","8202_eg","",
         			"8201m_ie","56742","8201m_ff", "56700", "8201m_cr", "62730","8201m_eg","56714");
         $runid=$runids{$key};
}elsif($suite eq 'S7073'){
         %runids = ("82xx_ie", "64244", "82xx_ff", "64228", "82xx_cr", "64212","82xx_eg","54417",
         			"8202m_ie","61411","8202m_ff", "61427", "8202m_cr", "61395","8202_eg","",
         			"8201m_ie","56743","8201m_ff", "56701", "8201m_cr", "62731","8201m_eg","56715");
         $runid=$runids{$key};
}elsif(($suite eq 'S7074') or ($suite eq 'S7074_1') or ($suite eq 'S7074_2') or ($suite eq 'S7074_3') or ($suite eq 'S7074_4') or ($suite eq 'S7074_5')){
         %runids = ("82xx_ie", "64245", "82xx_ff", "64229", "82xx_cr", "64862","82xx_eg","54418",
         			"8202m_ie","61412","8202m_ff", "61428", "8202m_cr", "61396","8202_eg","",
         			"8201m_ie","62748","8201m_ff", "62697", "8201m_cr", "63345","8201m_eg","56716");
         $runid=$runids{$key};
}elsif($suite eq 'S7075'){
         %runids = ("82xx_ie", "64246", "82xx_ff", "64230", "82xx_cr", "64214","82xx_eg","54419",
         			"8202m_ie","61413","8202m_ff", "61429", "8202m_cr", "61397","8202_eg","",
         			"8201m_ie","56745","8201m_ff", "56703", "8201m_cr", "62733","8201m_eg","56717");
         $runid=$runids{$key};
}elsif($suite eq 'S7076'){
         %runids = ("82xx_ie", "64247", "82xx_ff", "64231", "82xx_cr", "64215","82xx_eg","54420",
         			"8202m_ie","61414","8202m_ff", "61430", "8202m_cr", "61398","8202_eg","",
         			"8201m_ie","56746","8201m_ff", "56704", "8201m_cr", "62734","8201m_eg","56718");
         $runid=$runids{$key};
}elsif($suite eq 'S7078'){
         %runids = ("82xx_ie", "64248", "82xx_ff", "64232", "82xx_cr", "64216","82xx_eg","54422",
         			"8202m_ie","61415","8202m_ff", "61431", "8202m_cr", "61399","8202_eg","",
         			"8201m_ie","56747","8201m_ff", "56705", "8201m_cr", "62735","8201m_eg","56719");
         $runid=$runids{$key};
}elsif($suite eq 'S7077'){
         %runids = ("82xx_ie", "64249", "82xx_ff", "64233", "82xx_cr", "64217","82xx_eg","48791",
         			"8202m_ie","61416","8202m_ff", "61432", "8202m_cr", "61400","8202_eg","",
         			"8201m_ie","56748","8201m_ff", "56706", "8201m_cr", "62736","8201m_eg","56720");
         $runid=$runids{$key};
}elsif($suite eq 'S7215'){
         %runids = ("82xx_ie", "64250", "82xx_ff", "64234", "82xx_cr", "64218","82xx_eg","54423",
         			"8202m_ie","61418","8202m_ff", "61433", "8202m_cr", "61401","8202_eg","",
         			"8201m_ie","56749","8201m_ff", "56707", "8201m_cr", "62737","8201m_eg","56721");
         $runid=$runids{$key};
}elsif(($suite eq 'S10071_1') or ($suite eq 'S10071_2') or ($suite eq 'S10071_3') or ($suite eq 'S10071_4') or ($suite eq 'S10071_5')){
         %runids = ("82xx_ie", "64251", "82xx_ff", "64235", "82xx_cr", "64868","82xx_eg","",
         			"8202m_ie","61444","8202m_ff", "61445", "8202m_cr", "61237","8202_eg","",
         			"head_ie","","head_ff", "", "head_cr", "","head_eg","");
         $runid=$runids{$key};
}elsif(($suite eq 'S10851_1') or ($suite eq 'S10851_2')){
         %runids = ("82xx_ie", "64237", "82xx_ff", "64221", "82xx_cr", "64205","82xx_eg","",
         			"8202m_ie","61419","8202m_ff", "61435", "8202m_cr", "61360","8202_eg","",
         			"head_ie","","head_ff", "", "head_cr", "","head_eg","");
         $runid=$runids{$key};     
}elsif(($suite eq 'S10670_1') or ($suite eq 'S10670_2')){
         %runids = ("82xx_ie", "64238", "82xx_ff", "64222", "82xx_cr", "64855","82xx_eg","",
         			"8202m_ie","61417","8202m_ff", "61434", "8202m_cr", "61388","8202_eg","",
         			"head_ie","","head_ff", "", "head_cr", "","head_eg","");
         $runid=$runids{$key};
}elsif(($suite eq 'S10099_4') or ($suite eq 'S10099_5')){
         %runids = ("ie", "54443", "ff", "54439", "cr", "56977","eg","53738",
         			"8202_ie","","8202_ff", "59399", "8202_cr", "59879","8202_eg","", "82xx_cr", "64253", "82xx_ie", "64256", "82xx_ff", "64259",
         			"head_ie","56751","head_ff", "56755", "head_cr", "56753","head_eg","56757");
         $runid=$runids{$key};
}elsif($suite eq 'S7385'){
         %runids = ("ie", "45699", "ff", "45701", "cr", "56915","eg","45705","head_ie", 
                   "56765","head_ff", "56763", "head_cr", "56761","head_eg","56759");
         $runid=$runids{$key};
}elsif($suite eq 'S10006'){
         %runids = ("ie", "46815", "ff", "46817", "cr", "56903","eg","46821",
         			"8202_ie","","8202_ff", "58582", "8202_cr", "58580","8202_eg","", "82xx_cr", "64268", "82xx_ie", "64270", "82xx_ff", "64272",
         			"head_ie", "56773","head_ff", "56771", "head_cr", "65022","head_eg","56767");
         $runid=$runids{$key};
}elsif($suite eq 'S9163'){
         %runids = ("ff", "54217","head_ff", "56775");
         $runid=$runids{$key};
}elsif($suite eq 'S9164'){
         %runids = ("ff", "53445","head_ff", "56776");
         $runid=$runids{$key};
}elsif($suite eq 'S9165'){
         %runids = ("ff", "43206","head_ff", "56779");
         $runid=$runids{$key};
}elsif($suite eq 'S9166'){
         %runids = ("ff", "54592","head_ff", "56781");
         $runid=$runids{$key};
}elsif($suite eq 'S6940'){
         %runids = ("ie", "48824","ff", "48935", "cr", "48938","eg","48941");
         $runid=$runids{$key};
}elsif(($suite eq 'S9164_pdf_chart_1')or($suite eq 'S9164_pdf_chart_2')){
         %runids = ("ie", "54167","ff", "54165", "cr", "56940","eg","54171",
         			"8202_ie","59871","8202_ff", "59812", "8202_cr", "59869","8202_eg","", "82xx_cr", "64262", "82xx_ie", "64264", "82xx_ff", "64266",
			        "head_ie","56787","head_ff", "56777", "head_cr", "65024","head_eg","56784");
         $runid=$runids{$key};
}elsif($suite eq 'S6811'){
         %runids = ("ie", "54574","ff", "54570", "cr", "54568","eg","54572","head_ie", 
                   "56789","head_ff", "56793", "head_cr", "56795","head_eg","56791");
         $runid=$runids{$key};
}elsif($suite eq 'S9082'){
         %runids = ("ie", "54208","head_ie","56797");
         $runid=$runids{$key};
}elsif(($suite eq 'S9970_part_1')or($suite eq 'S9970_part_2')or($suite eq 'S9970_part_3')){
         %runids = ("ie", "45699", "ff", "45701", "cr", "57929","eg","45705",
         			"8202_ie","58458","8202_ff", "58455", "8202_cr", "58607","8202_eg","",
         			"head_ie", "56765","head_ff", "56763", "head_cr", "56761","head_eg","56759",
         			"82xx_cr", "64278", "82xx_ie", "64280", "82xx_ff", "64282");
         $runid=$runids{$key};
}elsif(($suite eq 'S10032_visual_1')or($suite eq 'S10032_visual_2')or
       ($suite eq 'S10032_visual_3')or($suite eq 'S10032_visual_4')or
       ($suite eq 'S10032_visual_5')){
         %runids = ("ie", "54560","ff", "54562", "cr", "54564","eg","54566",
         			"8201m_ie","59814","8201m_ff", "59657", "8201m_cr", "58630","8201m_eg","",
         			"8202_ie","59814","8202_ff", "59657", "8202_cr", "59669","8202_eg","",
         			"82xx_ie","64291","82xx_ff", "64295", "82xx_cr", "64123","82xx_eg","",
         			"head_ie", "56039","head_ff", "56043", "head_cr", "56041","head_eg","56045",
                   "prod_cr","56942");
         $runid=$runids{$key};
}elsif(($suite eq 'S1427_Part1')or($suite eq 'S1427_Part2')or($suite eq 'S1427_Part3')or($suite eq 'S1427_Part4')){
         %runids = ("ie", "54517","ff", "55931", "cr", "55933","head_ie", 
                   "56815","head_ff", "56811", "head_cr", "56807","head_eg","56045", "82xx_cr", "64276");
         $runid=$runids{$key};
}elsif($suite eq 'S1427-Part2'){
         %runids = ("ie", "55935","ff", "54577", "cr", "55939","head_ie", 
                   "56816","head_ff", "55937", "head_cr", "56808","head_eg","56045", "82xx_cr", "64276");
         $runid=$runids{$key};
}elsif($suite eq 'S1427-Part3'){
         %runids = ("ie", "55936","ff", "54577", "cr", "55940","head_ie", 
                   "56817","head_ff", "55938", "head_cr", "56809","head_eg","56045", "82xx_cr", "64276");
         $runid=$runids{$key};
}elsif($suite eq 'S8938_win_gui'){
         %runids = ("ie", "55416","ff", "55416", "cr", "55416","eg","55416");
         $runid=$runids{$key};
}elsif(($suite eq 'S8938_win7_gui_install')or($suite eq 'S8938_win7_gui_unistall')){
         %runids = ("ie", "55959","ff", "55416", "cr", "55416","eg","55416", "head_ie", "56885");
         $runid=$runids{$key};
}elsif($suite eq 'S1757_settings_1'){
         %runids = ("ie", "54555","ff", "55959", "cr", "55959","eg","55959","head_ie", 
                   "56819","head_ff", "56825", "head_cr", "56823","head_eg","56821");
         $runid=$runids{$key};
}elsif($suite eq 'S1428'){
         %runids = ("ie", "55929","ff", "55931", "cr", "55933");
         $runid=$runids{$key};
}elsif($suite eq 'S1431'){
         %runids = ("ie", "55935","ff", "55937", "cr", "55939");
         $runid=$runids{$key};
}elsif($suite eq 'S6443'){
         %runids = ("ie", "55936","ff", "55938", "cr", "55940");
         $runid=$runids{$key};
}elsif($suite eq 'S10141_action_android_1'){
         %runids = ("8201m_cr", "55724", "head_cr", "56847","8202m_cr", "62670", "82xx_cr","62658", "8203_cr","64814");
         $runid=$runids{$key};
}elsif($suite eq 'S10141_active_report_android_web_1'){
         %runids = ("8201m_cr", "", "head_cr", "56849", "head_sf", "58633", "8202m_cr", "62670", "8202m_sf", "60798", "82xx_sf", "62661", "82xx_cr","62658", "8203_sf", "64812", "8203_cr","58365");
         $runid=$runids{$key};
}elsif($suite eq 'S10141_MobileViewer_ActiveReport'){
         %runids = ("8201m_cr", "", "head_cr", "", "head_sf", "58633", "8202m_cr", "62670", "8202m_sf", "60798", "82xx_sf", "62661", "82xx_cr","62658", "8203_sf", "64812", "8203_cr","64814");
         $runid=$runids{$key};
}elsif($suite eq 'S10032_as_esri_map'){
         %runids = ("8201m_cr", "56883", "head_cr", "","8202_cr", "58465");
         $runid=$runids{$key};
}elsif($suite eq 'S10032_rest_licensing'){
         %runids = ("cr", "57946", "head_cr", "58170", "82xx_cr", "64008", "82xx_ff", "64067");
         $runid=$runids{$key};
}elsif($suite eq 'S8938_full_install'){
         %runids = ("cr", "57006", "head_cr", "57006");
         $runid=$runids{$key};
}elsif($suite eq 'S17982_USBANK'){
         %runids = ("8201m_ie", "", "82xx_ie", "72673", "head_ie", "77399", "8203_ie", "", "82xx_cdr_ie", "84839");
         $runid=$runids{$key};
}elsif(($suite eq 'S10189_USBANK')or($suite eq 'S10189_HillmanGroup')or($suite eq 'S10189_ParkerHannifin_Part_1')or($suite eq 'S10189_ParkerHannifin_Part_2')or($suite eq 'S10189_ParkerHannifin_Part_3')or($suite eq 'S10189_VOYA')or($suite eq 'S10189_VMMC_Part_1')or($suite eq 'S10189_VMMC_Part_2')or($suite eq 'S10189_VMMC_Part_3')){
         %runids = ("8201m_ie", "70495", "82xx_ie", "72672", "head_ie", "77398", "8203_ie", "65294", "82xx_cdr_ie", "84838");
         $runid=$runids{$key};
}elsif(($suite eq 'S10099_157158_drilldown_1')or($suite eq 'S10099_157154_filter_1')or($suite eq 'S10099_161124_filter_4')or
		($suite eq 'S10099_161125_bucket_part1')){
         %runids = ("82xx_ie", "64256", "82xx_cr", "64253", "82xx_ff", "64259");
         $runid=$runids{$key};
}elsif($suite eq 'S10038'){
         %runids = ("ie", "","ff", "", "cr", "","eg","",
         			"8202_ie","","8202_ff", "", "8202_cr", "59836","8202_eg","",
         			"head_ie", "","head_ff", "", "head_cr", "","head_eg","");
         $runid=$runids{$key};
}
print "$runid";