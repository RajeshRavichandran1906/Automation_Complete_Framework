#!/usr/local/bin/perl
use English;
use Cwd;
my $windows = ($OSNAME eq 'MSWin32');
$workspace=getcwd();
my ($prodid,
    $relid,
    $confid,
    $pkgname,
    $suitepath,        
    $suiteid,
    $runid)=    
    @ARGV;

$tool=5;


my $slash="\\";
my $nul="/nul 2>&1";
my $remove="rd /S /Q ";
my $dir="d:\\";
my $lib="$dir\\qa\\lib";
my $testnode = $ENV{computername};
my $q='"';
my $testdir="$dir\qa\\$suitepath";
$resultfile = "$testdir\\outfiles\\result.txt";
system("rm -f $resultfile") if (-e $resultfile);
my $runSoap="C:\\Program Files\\SmartBear\\SoapUI-5.2.1\\bin\\testrunner.bat";

if (not $windows){  #for unix OS (always wf)
  $slash = "/";
  $nul="/dev/null 2>&1";
  $remove="rm -fr ";
  $dir="$ENV{HOME}";
  $lib="$dir/qa/lib";
  $testnode = qx(hostname);
  $q="'";
  $testdir="$dir/qa/$suitepath";
  $runSoap="$dir/qa/lib/soapStart.sh"; 
}

my $qadir="$dir${slash}qa";
#chdir($dir);
#unlink($qadir)
# if (-e $qadir);

#if (-e $qadir){
#  $cmd="rm -rf $qadir";
#  system($cmd);
#  }
     
#system("rm -rf $qadir") if (-d $qadir);
#system("move $workspace\\qa $qadir");
#system("cp -r $workspace\\qa $qadir");

$soapproject=$testdir.$slash."REST_suite1.xml";
$projectfolder=$testdir;
$projectfolder=~ s/.*\// /;
chomp $projectfolder;

chmod(0775,$runSoap) if (not $windows);
$cmd="\"$runSoap\" -s${projectfolder} $soapproject";
system($cmd);

@string=(84, 111, 108, 115, 116, 111, 121, 49, 57, 56, 54);
$param = undef;
foreach $item (@string) {
       chomp $item;    
       $char = chr(${item});
       $param = "${param}" . "${char}";
}

$param = undef;
$param = "Li47OFB.CFpL1diBiImX-iDa9PymKNq7v47dAz4nR";
%rel = ("8105m", "2", "8106", "3", "head", "4", "8200", "5", "8201", "9", "8201m", "11","8202", "14","8202m", "17", "82xx", "20", "8203", "21",
		"8203M", "22", "8203M2", "23", "8203M3", "24", "8204", "25", "8204M", "26", "8204M2", "27", "8204M3", "28", "82xx_cdr", "999");

%conf = ("391","2","455","3","487","4","489","5","506","6","223","7","281","8","338","9","508","10","232","11",
         "250","12","279","13","302","14","323","15","334","16","348","17","394","18","396","19","401","20",
         "408","21","453","22","471","23","485","24","501","25","502","26","515","27","500","28","513","29",
         "512","30","507","31","486","32","496","33","498","34","497","35","577","36","291","37","292",
         "38","293","39","294","40","295","41","296","42","341","43","342","44","343","45","344","46","345",
         "47","346","48","591","49","592","50","593","51","594","52","595","53","596","54","bue1","55",
         "bue2","56","wf1","57","as1","58","366","59","wf3","65","wf4","66","wf5","67", "wf2", "82", "724", "108",
         "756", "131", "739", "120", "795", "144","784", "145","726", "110","697", "97");
%prod=("wf","1","as","2","wq","3","wx","4","wb","5");

$suiteid =~ s/s//i;

my $Res = {};
$tests_list = undef;
open(IN,$resultfile) || die "ERROR: cannot open $tests_list_file for reading: $!";
while (<IN>) {
   if  ($_ =~ /C\d+/) {
       my ($key,$val) = $_ =~ /^(\S+)\s+(.+)$/; 
       push(@test,$key);
       $Res->{$key} = $val;
       $tests_list = $tests_list . $key . ",";
   }
}
close (IN) || die "ERROR: cannot close $tests_list_file: $!";
$tests_list =~ s/\,$//;
$tests_list =~ s/C//ig;
$cnt=0;
$x=@test;
print "size is $x";
$relid= lc $relid;
foreach $test (@test){
  if ($Res->{$test} eq "PASS") {
     $status = 1;
     }else {
     $status = 5;
    }
  $cnt=$cnt+1;
  $tcid = $test;
  $tcid =~ s/C//i;
  $cmd="\\\\bigrepos01\\bigscm\\TA\\admin\\php\\php   ".
      "\\\\bigrepos01\\bigscm\\TA\\admin\\php\\add_result.php  $param "
     ."$runid $tcid $status $pkgname 2 $rel{$relid} $conf{$confid} $tool $prod{$prodid} $nul";
  #print "\n$cmd\n";
  #system($cmd);
  $tem_dir=getcwd();
  $cmd="python $tem_dir\\qa\\selenium\\driver\\add_result.py  $runid $tcid $status $pkgname 2 $rel{$relid} $conf{$confid} $tool $prod{$prodid} $nul";
  print "\n$cmd\n";
  system($cmd);
}
print "Count= $cnt\n";
system("move $qadir $workspace");
#system("cp -rf $qadir $workspace");