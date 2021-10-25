#!/usr/local/bin/perl
use English;

my ($suite,$key)=@ARGV;


if($suite eq 'S7067'){
         %runids = ("ie", "57444", "ff", "54425", "cr", "56866","eg","54411","head_ie", 
                   "56737","head_ff", "56695", "head_cr", "56723","head_eg","56709");
         $runid=$runids{$key};
}elsif(($suite eq 'S7068_filter_1') or ($suite eq 'S7068_filter_2') or ($suite eq 'S7068_medproj_1')){
         %runids = ("ie", "57445", "ff", "54426", "cr", "56867","eg","54412","head_ie", 
                   "56738","head_ff", "56696", "head_cr", "56724","head_eg","56710");
         $runid=$runids{$key};
}elsif($suite eq 'S7069'){
         %runids = ("ie", "57446", "ff", "54427", "cr", "56868","eg","54413","head_ie", 
                   "56739","head_ff", "56697", "head_cr", "56725","head_eg","56711");
         $runid=$runids{$key};
}elsif($suite eq 'S7070'){
         %runids = ("ie", "57447", "ff", "54428", "cr", "56869","eg","54414","head_ie", 
                   "56740","head_ff", "56698", "head_cr", "56726","head_eg","56712");
         $runid=$runids{$key};
}elsif($suite eq 'S7071'){
         %runids = ("ie", "57448", "ff", "54429", "cr", "56870","eg","54415","head_ie", 
                   "56741","head_ff", "56699", "head_cr", "56727","head_eg","56713");
         $runid=$runids{$key};
}elsif($suite eq 'S7072'){
         %runids = ("ie", "57449", "ff", "54430", "cr", "56853","eg","54416","head_ie", 
                   "56742","head_ff", "56700", "head_cr", "56728","head_eg","56714");
         $runid=$runids{$key};
}elsif($suite eq 'S7073'){
         %runids = ("ie", "57450", "ff", "54431", "cr", "56871","eg","54417","head_ie", 
                   "56743","head_ff", "56701", "head_cr", "56729","head_eg","56715");
         $runid=$runids{$key};
}elsif(($suite eq 'S7074') or ($suite eq 'S7074_1') or ($suite eq 'S7074_2') or ($suite eq 'S7074_3') or ($suite eq 'S7074_4') or ($suite eq 'S7074_5')){
         %runids = ("ie", "57451", "ff", "54432", "cr", "56852","eg","54418","head_ie", 
                   "56744","head_ff", "56702", "head_cr", "56730","head_eg","56716");
         $runid=$runids{$key};
}elsif($suite eq 'S7075'){
         %runids = ("ie", "57452", "ff", "54433", "cr", "56872","eg","54419","head_ie", 
                   "56745","head_ff", "56703", "head_cr", "56731","head_eg","56717");
         $runid=$runids{$key};
}elsif($suite eq 'S7076'){
         %runids = ("ie", "57453", "ff", "54434", "cr", "56873","eg","54420","head_ie", 
                   "56746","head_ff", "56704", "head_cr", "56732","head_eg","56718");
         $runid=$runids{$key};
}elsif($suite eq 'S7078'){
         %runids = ("ie", "57454", "ff", "54435", "cr", "56874","eg","54422","head_ie", 
                   "56747","head_ff", "56705", "head_cr", "56733","head_eg","56719");
         $runid=$runids{$key};
}elsif($suite eq 'S7077'){
         %runids = ("ie", "57455", "ff", "54436", "cr", "56875","eg","48791","head_ie", 
                   "56748","head_ff", "56706", "head_cr", "56734","head_eg","56720");
         $runid=$runids{$key};
}elsif($suite eq 'S7215'){
         %runids = ("ie", "57456", "ff", "54437", "cr", "56876","eg","54423","head_ie", 
                   "56749","head_ff", "56707", "head_cr", "56735","head_eg","56721");
         $runid=$runids{$key};
}elsif(($suite eq 'S10099_4') or ($suite eq 'S10099_5')){
         %runids = ("ie", "54443", "ff", "54439", "cr", "57923","eg","53738","head_ie", 
                   "56751","head_ff", "56755", "head_cr", "56753","head_eg","56757");
         $runid=$runids{$key};
}elsif($suite eq 'S7385'){
         %runids = ("ie", "45699", "ff", "45701", "cr", "56915","eg","45705","head_ie", 
                   "56765","head_ff", "56763", "head_cr", "56761","head_eg","56759");
         $runid=$runids{$key};
}elsif($suite eq 'S10006'){
         %runids = ("ie", "46815", "ff", "46817", "cr", "56903","eg","46821","head_ie", 
                   "56773","head_ff", "56771", "head_cr", "56769","head_eg","56767");
         $runid=$runids{$key};
}elsif(($suite eq 'S10032_visual_1')or($suite eq 'S10032_visual_2')or
       ($suite eq 'S10032_visual_3')or($suite eq 'S10032_visual_4')or
       ($suite eq 'S10032_visual_5')){
         %runids = ("ie", "54560","ff", "54562", "cr", "57616","eg","54566","head_ie", 
                   "56039","head_ff", "56043", "head_cr", "56041","head_eg","56045",
                   "prod_cr","56942");
         $runid=$runids{$key};
}elsif(($suite eq 'S9970_part_1')or($suite eq 'S9970_part_2')or($suite eq 'S9970_part_3')){
         %runids = ("ie", "45699", "ff", "45701", "cr", "57929","eg","45705",
         			"8202_ie","58458","8202_ff", "58455", "8202_cr", "58607","8202_eg","",
         			"head_ie", "56765","head_ff", "56763", "head_cr", "56761","head_eg","56759");
         $runid=$runids{$key};
}
print "$runid";