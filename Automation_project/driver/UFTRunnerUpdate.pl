#!/usr/local/bin/perl
use English;
use Cwd;

my ($prodid,
    $relid,
    $confid,
    $pkgname,
    $suitepath,        
    $suiteid,
    $runid,
    $browser)=    
    @ARGV;

my $Conf = {};
my @resp = qx(\\\\bigrepos01\\bigscm\\admin\\bin\\getConf.pl $prodid $confid $relid);
chomp(@resp);
foreach my $resp (@resp) {
    my ($key,$val) = $resp =~ /^(\S+)\s+(.+)$/;
    $Conf->{$key} = $val;
}


print "$pkgname\n";

# to get the suite folder name
my $foldername = ${suitepath};
my @parts = split('/', $foldername);
my $suite_folder=$parts[@parts - 1];
print $suite_folder;
print "$cmd\n";

# created a new local_suite to use the workspace folder
my $new_localsuite_repos="d:\\${suite_folder}\\qa";
my $local_suite_repos="d:\\qa";
print $new_localsuite_repos;

$currdir=getcwd();

print "$cmd\n";
#system($cmd);
#added more time to copy folder manually
sleep 5;

my $file = "test_info.txt";
unlink $file;
if(-e $file) 
{
    print "File test_info.txt still exists!\n";
}
else 
{
    print "File test_info.txt deleted.\n";
}
sleep 10;

#$cmd="move $local_suite_repos\\${suitepath}\\test_info.txt  $local_suite_repos\\lib\\";
$cmd="move $new_localsuite_repos\\${suitepath}\\test_info.txt  $local_suite_repos\\lib\\";
print "$cmd\n";
system($cmd);
$cmd = "cscript $local_suite_repos\\lib\\runUFTUpdate.vbs" .
	   " $confid $relid $prodid $pkgname $suiteid $runid $browser $suite_folder";

print "$cmd\n";

#running QTP
    system($cmd);


$cmd="move $local_suite_repos ${currdir}\\";

print "$cmd\n";

system($cmd);
    




