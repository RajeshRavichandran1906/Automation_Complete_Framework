#!/usr/local/bin/perl
use English;
use Cwd;

my ($prodid,
    $relid,
    $confid,
    $pkgname,
    $suitepath,        
    $suiteid,
    $projectid,
    $runid,
    $browser)=    
    @ARGV;


$currdir=getcwd();


my $local_suite_repos="d:\\qa";
#delete any exiting qtp environment
if (-d $local_suite_repos) {
    print ("rd /S /Q $local_suite_repos\n");
    system("rd /S /Q $local_suite_repos");
   
} 

system("mkdir $local_suite_repos");
chmod (0777,$local_suite_repos);
$cmd ="move ${currdir}\\qa\\lib  $local_suite_repos\\";
print "$cmd\n";
system($cmd);
$cmd ="move ${currdir}\\$suitepath  $local_suite_repos\\";
print "$cmd\n";
system($cmd);

sleep 10;
$cmd="python $local_suite_repos\\lib\\write_test.py $projectid $suiteid $suitepath";
print "$cmd\n";
system($cmd);

$cmd = "cscript $local_suite_repos\\lib\\runUFTUpdate.vbs" .
	   " $confid $relid $prodid $pkgname $suiteid $runid $browser";

print "$cmd\n";

#running QTP
    system($cmd);


$cmd="move $local_suite_repos ${currdir}\\";

print "$cmd\n";

system($cmd);