#!/usr/local/bin/perl

use Cwd;
$workspace=getcwd();
$workspace=~ s/\//\\/;

$prodid = shift(@ARGV);
$confid = shift(@ARGV);
$relid = shift(@ARGV);
$browser = shift(@ARGV);
$projectFolder = shift(@ARGV);
$suiteFolder = shift(@ARGV);
$subsectionFolder = shift(@ARGV);
$seGridEnv = shift(@ARGV);

$relid = lc( $relid );
$targetFolder= "$workspace\\qa\\automation\\$projectFolder\\$suiteFolder\\$subsectionFolder";
my $Conf = {};
$initFile=$targetFolder."\\config.init";
#REMOVE THIS REDIRECT AT EARLIEST CHANCE. DO NOT HARDCODE LIKE THIS.
if ($relid eq '82xx_cdr') {
	$relid = '8204';
}
my @resp = qx(\\\\bigrepos01\\bigscm\\admin\\bin\\getConf.pl $prodid $confid $relid);

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
  }elsif($browser eq 'eg'){
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
   $_ =~ s/confid\s+(.+)/confid $confid/;
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
