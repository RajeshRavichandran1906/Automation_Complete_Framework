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

$currdir=getcwd();


my $local_suite_repos="d:\\qa";
#delete any exiting qtp environment
if (-d $local_suite_repos) {
    print ("rd /S /Q $local_suite_repos\n");
    system("rd /S /Q $local_suite_repos");
   
} 

$cmd ="move ${currdir}\\qa  d:\\";

print "$cmd\n";
system($cmd);
#added more time to copy folder manually
#sleep 120;
$cmd="move $local_suite_repos\\${suitepath}\\test_info.txt  $local_suite_repos\\lib\\";
print "$cmd\n";
system($cmd);
