#!/usr/local/bin/perl
use English;
use Cwd;

my ($prodid,
    $relid,
    $confid,
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


$pkg_path=$Conf->{winwfpkgpath};
$pkg_path=$Conf->{aspkgpath}
    if ($prodid eq 'as');

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

sleep 10;
$cmd="move $local_suite_repos\\${suitepath}\\test_info.txt  $local_suite_repos\\lib\\";
print "$cmd\n";
system($cmd);

$cmd = "cscript $local_suite_repos\\lib\\runUFTUpdate1.vbs" .
	   " $confid $relid $prodid $pkgname $suiteid $runid $browser";

print "$cmd\n";

#running QTP
    system($cmd);


$cmd="move $local_suite_repos ${currdir}\\";

print "$cmd\n";

system($cmd);
    




