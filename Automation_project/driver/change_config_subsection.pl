#!/usr/local/bin/perl

use Cwd;
use English;
$workspace=getcwd();
if($OSNAME eq 'MSWin32'){$workspace=~ s/\//\\/;}

$prodid = shift(@ARGV);
$confid = shift(@ARGV);
$relid = shift(@ARGV);
$browser = shift(@ARGV);
$suiteFolder = shift(@ARGV);
$subsectionFolder = shift(@ARGV);
$seGridEnv = shift(@ARGV);

$relid = lc( $relid );
$targetFolder= (($OSNAME eq 'MSWin32') ? "$workspace\\qa\\selenium\\${suiteFolder}\\${subsectionFolder}" : "$workspace/qa/selenium/$suiteFolder/$subsectionFolder");
my $Conf = {};
$initFile=$targetFolder.(($OSNAME eq 'MSWin32') ? "\\config.init" : "/config.init");

my @resp = (($OSNAME eq 'MSWin32') ? qx(perl \\\\na1prdfs01\\foc_cifs\\bigscm\\admin\\bin\\getconf.pl $prodid $confid $relid) : qx(perl //bigrepos01.ibi.com/getConf.pl $prodid $confid $relid));

chomp(@resp);
foreach my $resp (@resp) {
    my ($key,$val) = $resp =~ /^(\S+)\s+(.+)$/;
    $Conf->{$key} = $val;
}

$browser = lc( $browser );
if ($browser eq 'ff'){
   $browser='Firefox';
  }elsif($browser eq 'ie'){
    $browser='IE';
   $browser_driver='D:\IEDriverServer.exe';
  }elsif($browser eq 'cr'){
   $browser='Chrome';
   $browser_driver='D:\chromedriver.exe';
  }elsif($browser eq 'sa'){
   $browser='Safari';
  }elsif($browser eq 'eg' || $browser eq 'ceg'){
   $browser='Edge';
   $browser_driver='D:\MicrosoftWebDriver.exe';
  }
  
$nodeid=$Conf->{nodeid};
$wfnode=$Conf->{wfnode};
$httpport=$Conf->{httpport};
$wfcontext=$Conf->{wfcontext};
#$mrid=$Conf->{mrid};
#$mrpass=$Conf->{mrpass};

open(FILE, $initFile) || die "File not found";
my @lines = <FILE>;
close(FILE);

my @newlines;
foreach(@lines) {
   $_ =~ s/nodeid\s+(.+)/nodeid $nodeid/;
   $_ =~ s/httpport\s+(.+)/httpport $httpport/;
   $_ =~ s/wfcontext\s+(.+)/wfcontext $wfcontext/;
   $_ =~ s/browser\s+(.+)/browser $browser/;
   $_ =~ s/browser_driver\s+(.+)/browser_driver $browser_driver/; 
   $_ =~ s/se_grid_env\s+(.+)/se_grid_env $seGridEnv/;
   push(@newlines,$_);
}

open(FILE, ">$initFile") || die "File not found";
print FILE @newlines;
close(FILE);

print "Updated config.init\n";
print @newlines;
print "\n";
