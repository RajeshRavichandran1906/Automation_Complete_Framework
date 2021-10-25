#!/usr/bin/perl

use English;
use Cwd;
$currdir=getcwd();
$currdir=~ s/\//\\/;

$prodid=shift(@ARGV);
$confid=shift(@ARGV);
$relid=shift(@ARGV);
$browser=shift(@ARGV);
$proname=shift(@ARGV);
$srvid=shift(@ARGV);
$proid=shift(@ARGV);
$sid=shift(@ARGV);
$test_info_id=shift(@ARGV);
$initfile_id=shift(@ARGV);
$sname=shift(@ARGV);
$runner=shift(@ARGV);

$dbname=$relid;


$test_info_file="d:\\qa\\lib\\test_info.txt";
$tests_list_file="d:\\qa\\lib\\tests_list.txt";
$initFile="suite.txt";
$new_initFile="suite.init";


my $Conf = {};
my @resp = qx(\\\\bigrepos01\\bigscm\\admin\\bin\\getConf.pl $prodid $confid $relid);
chomp(@resp);
foreach my $resp (@resp) {
    my ($key,$val) = $resp =~ /^(\S+)\s+(.+)$/;
    $Conf->{$key} = $val;
}

$pkg_path=$Conf->{winwfpkgpath};
system("net use Q: $pkg_path orion1 /user:bigscm")
   if not( -e $pkg_path);
$pkg_date_dir = qx(dir /od /b ${pkg_path});
$pkg_date_dir=(split(/[\n\r]/,$pkg_date_dir))[-1]; 
chomp $pkg_date_dir;
$pkg_date_path = $pkg_path . "\\" . $pkg_date_dir;
$new_pkg_dir = `dir /od /b ${pkg_date_path}`;
$new_pkg_dir=(split(/[\n\r]/,$new_pkg_dir))[-1]; 
chomp $new_pkg_dir;
$pkgname=$new_pkg_dir;

print "$pkgname\n";

system("rm -r d:\\qa\\lib")
          if ( -e "d:\\qa\\lib");
system("mkdir d:\\qa\\lib");
      

chdir("C:\\Program Files\\LogiGear\\TestArchitect\\binclient");
$cmd="java -jar TAImportExportTool.jar --ExportFromID --server bigatmrepos01 --port 53400 ".
"--uid \"Nasir_Ahmed\" --pwd  --repoName $dbname --projectName $proname --ID $test_info_id ".
"--destinationFile d:\\qa\\lib\\test_info.txt --outputType txt --overwrite true";
system($cmd);

$cmd="java -jar TAImportExportTool.jar --ExportFromID --server bigatmrepos01 --port 53400 ".
"--uid \"Nasir_Ahmed\" --pwd  --repoName $dbname --projectName $proname --ID $initfile_id ".
"--destinationFile d:\\qa\\lib\\suite.txt --outputType txt --overwrite true";

system($cmd);

my @tests,@lines;
open(IN,$test_info_file) || die "ERROR: cannot open $tests_list_file for reading: $!";
while (<IN>) {
       next
          if($_ =~ /#/);
      if  ($_ =~ /C\d+/) {
       $test = $_;
       chomp $test;
       push (@tests, $test);
       $test =~ s/^.*\\//;
       $test =~ s/\s+.*//;
       $test ="$test\n";
       push (@lines, $test);
   
   }
}
close (IN) || die "ERROR: cannot close $tests_list_file: $!";

open(FILE, ">$tests_list_file") || die "File not found";
print FILE @lines;
close(FILE);

system("ren d:\\qa\\lib\\$initFile $new_initFile");

$nodeid=$Conf->{nodeid};
$httpport=$Conf->{httpport};
$wfcontext=$Conf->{httpport};
open(FILE, "d:\\qa\\lib\\$new_initFile") || die "File not found";
my @lines = <FILE>;
close(FILE);

my @newlines;
foreach(@lines) {
   $_ =~ s/confiDATA\s+(.+)//;
   $_ =~ s/nodeid\s+(.+)/nodeid $nodeid/;
   $_ =~ s/httpport\s+(.+)/httpport $httpport/;
   $_ =~ s/confid\s+(.+)/confid $confid/;
   $_ =~ s/pkgname\s+(.+)/pkgname $pkgname/;
   $_ =~ s/browser\s+(.+)/browser $browser/;
   push(@newlines,$_);
}

open(FILE, ">d:\\qa\\lib\\$new_initFile") || die "File not found";
print FILE @newlines;
close(FILE);

chdir("$currdir");

$exporthtmlpath = "\\\\bigport\\perf-data\$\\TA\\results\\${relid}\\${sid}\\$pkgname";
$localhtmlpath="${currdir}\\results";

$cmd="\\\\bigrepos01\\bigscm\\ta\\admin\\bin\\create_tr_auto_run.pl ".
"prodid=$prodid relid=$relid pkgname=$pkgname confid=$confid testtool=ta sid=$sid ".
"sname=\"$sname\" runbox=$runner browser=$browser runpath=d:\\qa\\lib";
system($cmd);

$dir="d:\\qa\\lib\\Failure Captures";
$new_dir="${currdir}\\Failure Captures";


system("rm -r $exporthtmlpath")
           if(-e $exporthtmlpath);
system("mkdir $exporthtmlpath");

system("rm -r $localhtmlpath")
           if(-e $localhtmlpath);
system("mkdir $localhtmlpath");
system("rm -r \"$new_dir\"")
           if (-e $new_dir);
system("mkdir \"$new_dir\"");
     
foreach $testpath  (@tests) {
  $testid=$testpath;
  $testid=~ s/^.*\\//;
  $testid=~ s/\s+.*//;
  chomp $testid;

$cmd="\"C:\\Program Files\\LogiGear\\TestArchitect\\jre\\bin\\java.exe\" -jar -Xmx512m ".
"\"C:\\Program Files\\LogiGear\\TestArchitect\\binclient\\TACommandLine.jar\" ".
"/exechost localhost /execport 53600 /rshost 172.19.26.46 /rsport 53400 /lsaddr  \"taserv.ibi.com\" ".
"/lsport  \"14101\" /lsusr /dbtype  \"javadb\" /dbname  $dbname /uid \"bigatm\" /pwd \"04848616460\" ".
"/proid $proid /proname $proname /srvid $srvid /sessionid /var  $browser /resultname \"$testid\" /comment ".
"/mod \"$testpath\"   /openresult \"no\" /toolname \"TestArchitect Automation Playback\" ".
"/toolscript \"D:\\Harness_IB\\run.bat\" /toolpath \"D:/Harness_IB/run.bat\" /toolcmd /versions /delay \"0\"  ".
"/redunlsport  \"14101\" /xupath  /exportxmlpath  /startupsettings  /uploadresulttorepos \"/$proname/Results\" ".
"/exporthtmlpath  \"$localhtmlpath\"   /uploadresultcond  \"Passed;\" ".
"/testsetid  /timetraveling /udf \"build number		pkgname confid		\" ".
"/capturecond  \"Passed;Failed;Warning/Error\" /numofinteraction  \"3\" ".
"/exportscreenshotcond  \"true\" 2>&1";
print " Executing Test no .....$testid\n";
system($cmd);
$cmd="copy /y $localhtmlpath\\${testid}\*html $exporthtmlpath\\ 2>&1";
system($cmd);
$cmd="\\\\bigport\\perf-data\$\\admin\\bin\\atm_out.pl ta $confid $relid $prodid $pkgname $sid $testid qa\\lib";
system($cmd);


if(-e $dir){
          opendir my $dh, $dir or die "Could not open '$dir' for reading '$!'\n";
          while (my $thing = readdir $dh ) {
          system ("move \"$dir\\$thing\"  \"$new_dir\"\\")
                      if ($thing =~ /jpg/);
          }

closedir $dh;
}


}







          
 
    
