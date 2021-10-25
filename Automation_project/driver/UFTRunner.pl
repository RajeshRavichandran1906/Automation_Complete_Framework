#!/usr/local/bin/perl
use English;
use FindBin;
use lib "$FindBin::Bin";
use CGI::Util qw(escape unescape); # escape('a?b:c') == 'a%3Fb%3Ac'
use Fcntl 'O_RDONLY';
use Cwd;


my ($T,$F) = (1,0);

my $q = ($OSNAME eq 'MSWin32' ? '"' : "'");

my $usage = " usage: run_qtp.pl.pl  <psid>" .
    " <prodid> <relid> <confid> <pkgname> <suiteid> <suitename>";


my ($prodid,
    $relid,
    $confid,        
    $suitepath,
    $suiteid,
    $sname,             
    $browser )=    
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


chdir($currdir);
#Run rsh to bigscm05 to create qtp test environment
$cmd = "wget -O suite.jar -t 0" .
    " \"http://cvs.ibi.com:3007/pkg_cgi/getSuiteJar.pl?prodid=${prodid}" .
    "&relid=${relid}&confid=${confid}&pkgname=${pkgname}&suite=${suitepath}\" 2>nul" ;

$resp= qx($cmd);

my $local_suite_repos="d:\\qa";
#delete any exiting qtp environment
if (-d $local_suite_repos) {
    print ("rd /S /Q $local_suite_repos\n");
    system("rd /S /Q $local_suite_repos");
   
} 

$suitDir="$currdir\\suite.jar";

if (-e $suitDir){
    $resp=qx(jar -xf suite.jar);
    unlink($suitDir);
} else {  
    print"suite.jar file is not present\n";
}

sleep 60;
system("move ${currdir}\\qa  d:\\");
 
sleep 60;
  
$cmd = "cscript d:\\qa\\lib\\runUFT.vbs" .
	   " $confid $relid $prodid $pkgname $suiteid \"$sname\" $browser";
print "$cmd\n";

#running QTP
    system($cmd);

system("move d:\\qa  ${currdir}\\");
    




