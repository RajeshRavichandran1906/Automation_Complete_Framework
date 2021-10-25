#!/usr/local/bin/perl
use English;

my ($suite)=@ARGV;


if(($suite eq 'S10099_4')or($suite eq 'S10099_5')or($suite eq 'S10664_binning_1')or($suite eq 'S10664_binning_2')or
	($suite eq 'S10664_paperclipping_1')or($suite eq 'S10664_paperclipping_2')or($suite eq 'S10099_157158_drilldown_1')or
	($suite eq 'S10099_157154_filter_1')or($suite eq 'S10099_161124_filter_4')or($suite eq 'S10099_161125_bucket_1')){
         $projid="312";
}elsif(($suite eq 'S10674_ws_contextmenu_1') or ($suite eq 'S10674_ws_contextmenu_2') or ($suite eq 'S10674_ws_contextmenu_3') or ($suite eq 'S10674_ws_contextmenu_4') or ($suite eq 'S10674_ws_contextmenu_5')){
         $projid="242";
}elsif(($suite eq 'S10032_chart_1')or($suite eq 'S10032_visual_1')or($suite eq 'S10032_visual_2')or($suite eq 'S10032_visual_3')or($suite eq 'S10032_visual_4')or($suite eq 'S10032_visual_5')
		or($suite eq 'S10660_chart_1')or($suite eq 'S10660_chart_2')or($suite eq 'S10660_infoassist_2')or($suite eq 'S10032_esrimap_1')or($suite eq 'S10032_esrimap_2')
		or($suite eq 'S10660_visual_1')or($suite eq 'S10660_visual_2')or($suite eq 'S10660_esrimap_1')or($suite eq 'S10660_esrimap_2')or($suite eq 'S10032_infoassist_1')
		or($suite eq 'S10032_infoassist_2')or($suite eq 'S10032_infoassist_3')or($suite eq 'S10032_infoassist_4')or($suite eq 'S10032_infoassist_5')
		or($suite eq 'S10032_infoassist_6')or($suite eq 'S10032_leaflet_1')or($suite eq 'S10032_active_datatype_formats')or($suite eq 'S10032_ahtml_off')or($suite eq 'S10032_ahtml_on')
		or($suite eq 'S10117_Bip_V4_Portal')or($suite eq 'S10117_Bip_V4_Portal_1')or($suite eq 'S10117_Bip_V4_Portal_2')){
         $projid="292";
}elsif($suite eq 'S6811'){
         $projid="20";
}elsif(($suite eq 'S7385')or($suite eq 'S7385')){
         $projid="137";
}elsif(($suite eq 'S9970_part_1')or($suite eq 'S9970_part_2')or($suite eq 'S9970_part_3')){
         $projid="276";
}elsif(($suite eq 'S9164_pdf_chart_1')or($suite eq 'S9164_pdf_chart_2')){
         $projid="251";
}elsif(($suite eq 'S7067')or($suite eq 'S7068_filter_1')or($suite eq 'S7068_filter_2')or($suite eq 'S7068_medproj_1')
       or($suite eq 'S7069')or($suite eq 'S7070')or($suite eq 'S7071')or($suite eq 'S7072')or($suite eq 'S7073')or
       ($suite eq 'S7074')or($suite eq 'S7074_1')or($suite eq 'S7074_2')or($suite eq 'S7074_3')or($suite eq 'S7074_4')or
       ($suite eq 'S7074_5')or($suite eq 'S7075')or($suite eq 'S7076')or($suite eq 'S7077')or($suite eq 'S7078')or($suite eq 'S7215')or($suite eq 'S10071_1')or($suite eq 'S10071_2')or($suite eq 'S10071_3')or($suite eq 'S10071_4')or($suite eq 'S10071_5')or($suite eq 'S10851_1')
       or($suite eq 'S10851_2')or($suite eq 'S10670_1')or($suite eq 'S10670_2')){
         $projid="116";
}elsif($suite eq 'S10006'){
         $projid="278";
}elsif($suite eq 'S10038'){
         $projid="295";
}
print "$projid";