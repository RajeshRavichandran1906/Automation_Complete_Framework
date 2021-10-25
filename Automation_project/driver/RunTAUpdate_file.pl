#!/usr/bin/perl

use English;
use Cwd;
$currdir=getcwd();
$currdir=~ s/\//\\/;

$prodid=shift(@ARGV);
$confid=shift(@ARGV);
$relid=shift(@ARGV);
$pkgname=shift(@ARGV);
$browser=shift(@ARGV);
$proname=shift(@ARGV);
$srvid=shift(@ARGV);
$proid=shift(@ARGV);
$sid=shift(@ARGV);
#$test_info_id=shift(@ARGV);
#$initfile_id=shift(@ARGV);
$runid=shift(@ARGV);
$runner=shift(@ARGV);
$dbname=$relid;
$dbname =~ s/m//;

$proname="\"$proname\"";
$test_info_file="d:/qa/lib/test_info.txt";
$tests_list_file="d:/qa/lib/tests_list.txt";
$lib="d:/qa/lib";
$initFile="$lib/suite.txt";

$new_initFile="$lib/suite.init";
#To get the TA repository IDs for test info and test init file.
@res=qx(get_ta_reposid.pl $relid $sid);
chomp(@res);
$test_info_id=$res[0];
$initfile_id=$res[1];
$mrid=$res[2];
print "$test_info_id\n";
print "$initfile_id\n";
#my $Conf = {};
#my @resp = qx(\\\\bigrepos01\\bigscm\\admin\\bin\\getConf.pl $prodid $confid $relid);
#chomp(@resp);
#foreach my $resp (@resp) {
#    my ($key,$val) = $resp =~ /^(\S+)\s+(.+)$/;
#    $Conf->{$key} = $val;
#}

#system("rm -rf $lib")
#          if ( -e $lib);
#system("mkdir $lib");
#system("chmod 777  $lib");
chdir("C:\\Program Files\\LogiGear\\TestArchitect\\binclient");
$cmd="java -jar TAImportExportTool.jar --ExportFromID --server bigatmrepos01 --port 53400 ".
"--uid \"Nasir_Ahmed\" --pwd  --repoName $dbname --projectName $proname --ID $test_info_id ".
"--destinationFile $test_info_file --outputType txt --overwrite true";
print "$cmd\n";
#system($cmd);

$cmd="java -jar TAImportExportTool.jar --ExportFromID --server bigatmrepos01 --port 53400 ".
"--uid \"Nasir_Ahmed\" --pwd  --repoName $dbname --projectName $proname --ID $initfile_id ".
"--destinationFile $initFile --outputType txt --overwrite true";
print "$cmd\n";
#system($cmd);

my @tests,@lines;
open(IN,$test_info_file) || die "ERROR: cannot open $tests_list_file for reading: $!";
print "IN\n";
while (<IN>) {
  if  (($_ =~ /C\d+/)or($_ =~ /StartUp/i)){
       $test = $_;
       chomp $test;
       push (@tests, $test);
       $test =~ s/^.*\\//;
       $test =~ s/\s+.*//;
       $test ="$test\n";
       push (@lines, $test);
       print "$test\n";
   }
}
close (IN) || die "ERROR: cannot close $tests_list_file: $!";

open(FILE, ">$tests_list_file") || die "File not found";
print "FILE\n";
print "$tests_list_file";
close(FILE);

system("mv $initFile $new_initFile");

#$nodeid=$Conf->{nodeid};
#$httpport=$Conf->{httpport};
#$wfcontext=$Conf->{httpport};
#$mrid=$Conf->{mrid};
#$mrpass=$Conf->{mrpass};
#open(FILE, "$new_initFile") || die "File not found";
#my @lines = <FILE>;
#close(FILE);

#my @newlines;
#foreach(@lines) {
#   $_ =~ s/confiDATA\s+(.+)//;
#   $_ =~ s/nodeid\s+(.+)/nodeid $nodeid/;
#   $_ =~ s/httpport\s+(.+)/httpport $httpport/;
#   $_ =~ s/confid\s+(.+)/confid $confid/;
#   $_ =~ s/pkgname\s+(.+)/pkgname $pkgname/;
#   $_ =~ s/browser\s+(.+)/browser $browser/;
#   $_ =~ s/mrid\s+(.+)/mrid $mrid/;
#   $_ =~ s/mrpass\s+(.+)/mrpass /;
#   push(@newlines,$_);
#}

#open(FILE, ">$new_initFile") || die "File not found";
#print FILE @newlines;
#close(FILE);

$localhtmlpath="${currdir}/results";

$dir="$lib/Failure Captures";
$new_dir="${currdir}/Failure Captures";

system("rm -rf $localhtmlpath")
       if(-e $localhtmlpath); 
system("mkdir $localhtmlpath");
system("chmod 777 $localhtmlpath");
system("rm -rf \"$new_dir\"")
	if (-e $new_dir);
system("mkdir \"$new_dir\"");
system("chmod 777 \"$new_dir\"");
$TAbrowser=$browser;
$TAbrowser="chrome"
  if ( $browser eq 'cr');

     
foreach $testpath  (@tests) {
  $testid=$testpath;
  $testid=~ s/^.*\\//;
  $testid=~ s/\s+.*//;
  chomp $testid;

$cmd="\"C:\\Program Files\\LogiGear\\TestArchitect\\jre\\bin\\java.exe\" -jar -Xmx512m ".
"\"C:\\Program Files\\LogiGear\\TestArchitect\\binclient\\TACommandLine.jar\" ".
"/exechost localhost /execport 53600 /rshost bigatmrepos01 /rsport 53400 /lsaddr  \"taserv.ibi.com\" ".
"/lsport  \"14101\" /lsusr /dbtype  \"javadb\" /dbname  $dbname /uid \"bigatm\" /pwd \"04848616460\" ".
"/proid $proid /proname $proname /srvid $srvid /sessionid /var  $TAbrowser /resultname \"$testid\" /comment ".
"/mod \"$testpath\"   /openresult \"no\" /toolname \"TestArchitect Automation Playback\" ".
"/toolscript \"D:\\Harness_IB\\run.bat\" /toolpath \"D:/Harness_IB/run.bat\" /toolcmd /versions /delay \"0\"  ".
"/redunlsport  \"14101\" /xupath  /exportxmlpath  /startupsettings  /uploadresulttorepos \"/$proname/Results\" ".
"/exporthtmlpath  \"$localhtmlpath\"   /uploadresultcond  \"Passed;\" ".
"/testsetid  /timetraveling /udf \"build number		pkgname confid		\" ".
"/capturecond  \"Passed;Failed;Warning/Error\" /numofinteraction  \"3\" ".
"/exportscreenshotcond  \"true\" 2>&1";
print " Executing Test  .....$testid\n";
print "$cmd\n";
system($cmd);
print "****************\n";
print "dbname=";
print "$dbname\n";
print "proid=";
print "$proid\n";
print "proname=";
print "$proname\n";
print "srvid=";
print "$srvid\n";
print "TAbrowser=";
print "$TAbrowser\n";
print "testid=";
print "$testid\n";
print "testpath=";
print "$testpath\n";
print "proname=";
print "$proname\n";
print "localhtmlpath=";
print "$localhtmlpath\n";
print "****************\n";
sleep 30;
$target_base_file= qx(ls $localhtmlpath\\${testid}\*html);
chomp $target_base_file;
$target_base_file =~ s/^.*\///;
$target_base_file="\"${localhtmlpath}/${target_base_file}\"";
$target_base_file =~ s/\//\\/;
#$cmd="\\\\bigrepos01\\bigscm\\TA\\admin\\bin\\send_ta_result_to_trUpdate.pl $target_base_file ta $confid $relid $prodid $pkgname $testid $runid $browser";
$cmd="${currdir}\\send_ta_result_to_trUpdate.pl $target_base_file ta $confid $relid $prodid $pkgname $testid $runid $browser";
#system($cmd)
#   if($testid !~ /StartUp/i);
if(-e $dir){
          opendir my $dh, $dir or die "Could not open '$dir' for reading '$!'\n";
          while (my $thing = readdir $dh ) {
          system ("move \"$dir\\$thing\"  \"$new_dir\"\\")
                      if ($thing =~ /jpg/);
          }
closedir $dh;
}


}







          
 
    
