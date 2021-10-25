#!/usr/local/bin/perl
use English;

my ($rel,$suite)=@ARGV;
if(($rel eq '8201m') or ($rel eq '8202')){
	if($suite eq 'S1427-Part1'){
	         %reposids = ("test_info_id", "bax69nr0371f","initfile_id", "bax69nq8ofbc","mruser","autodevuser28");
	}elsif($suite eq 'S1427-Part2'){
	         %reposids = ("test_info_id", "bax7008gsuy8","initfile_id", "bax70087mvk2","mruser","autodevuser28");
	}elsif($suite eq 'S1427-Part3'){
	         %reposids = ("test_info_id", "bc3pjx7viiwf","initfile_id", "bc3pjc5y53wy","mruser","autodevuser28");
	}elsif($suite eq 'S1428'){
	         %reposids = ("test_info_id", "bcpmjnalxhyy","initfile_id", "bcpmoc6m2oqj","mruser","autodevuser28");
	}elsif($suite eq 'S1431'){
	         %reposids = ("test_info_id", "bcpmph91rb9s","initfile_id", "bcpmpmski3pd","mruser","autodevuser28");
	}elsif($suite eq 'S6443'){
	         %reposids = ("test_info_id", "bcpmrw233l03","initfile_id", "bcpms6g5eu3n","mruser","autodevuser28");
	}else{print "wrong Suite ID is passed.\n";}
}elsif($rel eq 'head'){
	if($suite eq 'S9066'){
	         %reposids = ("test_info_id", "b93guux9pxx5","initfile_id", "b93gcnjkpfl5","mruser","autodevuser39");
	}else{print "wrong Suite ID is passed.\n";}
}else{print "wrong release ID is passed.\n";}
print "$reposids{'test_info_id'}\n";
print "$reposids{'initfile_id'}\n";
print "$reposids{'mruser'}\n";